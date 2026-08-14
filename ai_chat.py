import anthropic

client = anthropic.Anthropic()
conversation = []

while True:
    question = input("Ask Claude (or type 'quit'): ")
    if question.lower() == "quit":
        break
    
    conversation.append({"role": "user", "content": question})
    
    message = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        messages=conversation
    )
    
    reply = message.content[0].text
    print(reply)
    conversation.append({"role": "assistant", "content": reply})