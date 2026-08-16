import anthropic

roles = {
    "1": ("Python Tutor", "You are a friendly Python coding tutor for beginners. Always use simple code examples."),
    "2": ("Code Reviewer", "You are an expert Python code reviewer. Point out bugs and suggest improvements."),
    "3": ("Pirate", "You are a pirate who answers everything in pirate speak!"),
    "4": ("Custom", None),
    "5": ("Study Buddy", "You are a friendly study buddy. When given a topic, create 5 quiz questions about it, then quiz the user one question at a time. After each answer, tell them if they're right or wrong and explain why.")
}

client = anthropic.Anthropic()
conversation = []

def show_history():
    with open("chat_history.txt", "a") as f:
        pass
    with open("chat_history.txt", "r") as f:
        history = f.read()
    if history:
        view = input("View chat history? yes/no: ").lower()
        if view == "yes":
            print(history)
        clear = input("Clear chat history? yes/no: ").lower()
        if clear == "yes":
            open("chat_history.txt", "w").close()

def save_history():
    with open("chat_history.txt", "a") as f:
        for msg in conversation:
            if msg["role"] == "user":
                f.write(f"You: {msg['content']}\n")
            else:
                f.write(f"Claude: {msg['content']}\n")

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

show_history()
system = pick_role()

while True:
    question = input("Ask Claude (or type 'quit'): ")
    if question.lower() == "quit":
        save_history()
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