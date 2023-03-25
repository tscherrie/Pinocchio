import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"]

response = openai.Completion.create(
    engine="davinci-codex",
    prompt="This is a test.",
    max_tokens=10,
    n=1,
    stop=None,
    temperature=0.5,
)

print(response.choices[0].text.strip())