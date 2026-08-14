import anthropic

client = anthropic.Anthropic()
conversation = []

system = input("What role should Claude play? (press Enter for default): ")
if system == "":
    system = "You are a helpful assistant"

while True:
    question = input("Ask Claude (or type 'quit'): ")
    if question.lower() == "quit":
        break
    conversation.append({"role": "user", "content": question})
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system=system,
        messages=conversation
    )
    reply = message.content[0].text
    print(reply)
    conversation.append({"role": "assistant", "content": reply})