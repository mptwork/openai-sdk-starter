from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
import os

from starlette_prometheus import metrics, PrometheusMiddleware


# Initialize the FastAPI app
app = FastAPI()

# Add the Prometheus middleware to the app
app.add_middleware(PrometheusMiddleware)

# Register the Prometheus metrics endpoint
app.add_route("/metrics", metrics)

# Set the OpenAI API key from an environment variable
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Define a request model for the text to summarize
class SummarizeRequest(BaseModel):
    text: str

# Define a response model for the summary
class SummarizeResponse(BaseModel):
    summary: str

# Define an endpoint for summarizing text
@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(request: SummarizeRequest):
    try:
        # Use the OpenAI SDK to generate a summary
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=f"Please summarize the following text:\n{request.text}",
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5,
        )

        # Extract the summary from the OpenAI response
        summary = response.choices[0].text.strip()

        return SummarizeResponse(summary=summary)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
