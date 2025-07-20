from openai import OpenAI
import os


BASE_URL = "http://localhost:12434/engines/llama.cpp/v1/"

client = OpenAI(base_url=BASE_URL, api_key="docker_api_key")

MODEL = "ai/smollm2:latest"
PROMPT = "Travel Itinerary to Bangalore"

messages = [
    {"role": "user", "content": PROMPT}
]

response = client.chat.completions.create(
    model=MODEL,
    messages=messages
)

print(response.choices[0].message.content)