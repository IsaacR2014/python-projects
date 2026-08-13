import anthropic

client = anthropic.Anthropic()

while True:
    question = input("Ask Claude (or type 'quit'): ")
    if question.lower() == "quit":
        break
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    print(message.content[0].text)

