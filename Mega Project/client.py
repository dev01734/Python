from openai import OpenAI

client = OpenAI(
    api_key = "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"
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named Aurora, skilled in general task like Alexa and Siri."},
        {
            "role": "user",
            "content": "What is Coding?"
        }
    ]
)

print(completion.choices[0].message.content)