from smith.llm import OpenAILLM

def make_request():
  print("Making request...")
  client = OpenAILLM()
  response = client.request()
  if response.status_code != 200:
    print(f"Error: Request failed with status code {response.status_code} and message {response.text}")

  if response.status_code == 200:
    print(f"Response: {response.text}")

  return response

if __name__ == "__main__":
  make_request()