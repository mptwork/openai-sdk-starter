import json
from fastapi.testclient import TestClient

from main import app, SummarizeRequest, SummarizeResponse

client = TestClient(app)

def test_summarize():
    # Define some example text to summarize
    text = "The quick brown fox jumps over the lazy dog."

    # Send a POST request to the /summarize endpoint with the example text
    response = client.post("/summarize", json={"text": text})
    # Ensure that the response has a status code of 200 OK
    assert response.status_code == 200

    # Ensure that the response body contains a summary
    summary_response = SummarizeResponse.parse_raw(response.text)
    print(summary_response)
    assert summary_response.summary is not None
    assert isinstance(summary_response.summary, str)


