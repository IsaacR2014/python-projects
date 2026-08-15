import anthropic
roles = {
    "1": ("Python Tutor", "You are a friendly Python coding tutor for beginners. Always use simple code examples."),
    "2": ("Code Reviewer", "You are an expert Python code reviewer. Point out bugs and suggest improvements."),
    "3": ("Pirate", "You are a pirate who answers everything in pirate speak!"),
    "4": ("Custom", None)
}
client = anthropic.Anthropic()
conversation = []
def pick_role():
    print("Pick a role:")
    for key, (name, _) in roles.items():
        print(f"{key}. {name}")
    choice = input("Enter number: ")
    if choice in roles:
        name, prompt = roles[choice]
        if prompt is None:
            prompt = input("Type your custom role: ")
        print(f"Selected: {name}")
        return prompt
    else:
        print("Invalid choice! Try again.")
        return pick_role()  
system = pick_role()
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