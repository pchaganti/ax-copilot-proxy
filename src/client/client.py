import os
from litellm import completion

def run_litellm_non_stream():
    """Calls local server in non-stream mode using LiteLLM."""
    try:
        response = completion(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Create a fibonacci function in Python"}],
            stream=False
        )
        print("Non-streaming response:", response)
    except Exception as e:
        print("Error in non-stream mode:", e)

def run_litellm_stream():
    """Calls local server in stream mode using LiteLLM."""
    try:
        response_stream = completion(
            model="gpt-4o",
            messages=[{"role": "user", "content": "Create a fibonacci function in Python"}],
            stream=True
        )
        print("Streaming response:")
        for chunk in response_stream:
            print(chunk, end="", flush=True)
    except Exception as e:
        print("Error in streaming mode:", e)

if __name__ == "__main__":
    print("Running LiteLLM Client Non-Stream Mode:")
    run_litellm_non_stream()
    print("\nRunning LiteLLM Client Stream Mode:")
    run_litellm_stream()
