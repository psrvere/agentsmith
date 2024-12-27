from openai import OpenAI as OpenAIClient, AsyncOpenAI as AsyncOpenAIClient
from pydantic import BaseModel, ConfigDict
from typing import Optional, Dict, Any
import os
import requests

class OpenAILLM(BaseModel):
  api_key: Optional[str] = None
  organization: Optional[str] = None
  project: Optional[str] = None
  model_config = ConfigDict(arbitrary_types_allowed=True)
  client: Optional[OpenAIClient] = None

  def get_client(self):
    if self.client:
      return self.client
    
    self.api_key = self.api_key or os.getenv("OPENAI_API_KEY")
    if not self.api_key:
      print(f"Error: OPENAI_API_KEY is not set")

    _client_params: Dict[str, Any] = {}
    if self.api_key:
      _client_params["api_key"] = self.api_key
    if self.organization:
      _client_params["organization"] = self.organization
    if self.project:
      _client_params["project"] = self.project
    return OpenAIClient(**_client_params)
  
  def request(self) -> Dict[str, Any]:
    url: str = 'https://api.openai.com/v1/chat/completions'

    self.api_key = self.api_key or os.getenv("OPENAI_API_KEY")
    if not self.api_key:
      print(f"Error: OPENAI_API_KEY is not set")

    print("OpenAI API key:", self.api_key)

    headers: Dict[str, Any] = {
      'Authorization': f'Bearer {self.api_key}',
      'Content-Type': 'application/json'
    }

    data = {
      "model": "gpt-4o-mini",
      "messages": [
        {
          "role": "user",
          "content": "Hello, how are you?"
        }
      ],
      "temperature": 0.7,
    }

    response = requests.post(url, headers=headers, json=data)
    return response