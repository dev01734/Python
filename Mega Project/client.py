from openai import OpenAI

client = OpenAI(
    api_key = ""
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
