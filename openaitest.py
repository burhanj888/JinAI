from openai import OpenAI
from config import apikey

client = OpenAI(api_key=apikey)



response = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "test"
        }
      ]
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

# ChatCompletion(id='chatcmpl-9mpfvvkHDRjYyK6ley71gSe5iKKNY', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='Test received! How can I assist you today?', role='assistant', function_call=None, tool_calls=None))], created=1721425411, model='gpt-4o-mini-2024-07-18', object='chat.completion', system_fingerprint='fp_8b761cb050', usage=CompletionUsage(completion_tokens=10, prompt_tokens=8, total_tokens=18))

print(response)