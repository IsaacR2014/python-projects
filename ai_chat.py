import anthropic
import json
score = 0
roles = {
    "0": ("Quit", None),
    "1": ("Python Tutor", "You are a friendly Python coding tutor for beginners. Always use simple code examples."),
    "2": ("Code Reviewer", "You are an expert Python code reviewer. Point out bugs and suggest improvements."),
    "3": ("Pirate", "You are a pirate who answers everything in pirate speak!"),
    "4": ("Custom", None),
    "5": ("Study Buddy", "You are a friendly study buddy. When given a topic, create 5 quiz questions about it, then quiz the user one question at a time. After each answer, tell them if they're right or wrong and explain why."),
    "6": ("Trivia Master", "You are a Trivia Master. Ask exactly 10 questions one at a time. After each answer respond with either 'CORRECT!' or 'INCORRECT!' followed by the explanation. Keep track of the score and show it after question 10.You MUST respond with the exact word CORRECT or INCORRECT in capitals after every answer, no exceptions!")
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
    clear_leaderboard()  # add this line at the end!

def clear_leaderboard():
    try:
        with open("trivia_leaderboard.json", "r") as f:
            data = f.read()
        if data:
            clear = input("Clear trivia leaderboard? yes/no: ").lower()
            if clear == "yes":
                open("trivia_leaderboard.json", "w").close()
                print("Leaderboard cleared!")
    except:
        pass 

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
    if choice == "0":
        exit()
    if choice in roles:
        
        name, prompt = roles[choice]
        if prompt is None:
            prompt = input("Type your custom role: ")
        print(f"Selected: {name}")
        return prompt
    else:
        print("Invalid choice! Try again.")
        return pick_role()
def save_score_to_leaderboard(name, score):
    try:
        with open("trivia_leaderboard.json", "r") as f:
            leaderboard = json.load(f)
    except:
        leaderboard = []
    
    leaderboard.append({"name": name, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    leaderboard = leaderboard[:5]
    
    with open("trivia_leaderboard.json", "w") as f:
        json.dump(leaderboard, f)
    
    print("🏆 LEADERBOARD 🏆")
    for i, entry in enumerate(leaderboard, 1):
        print(f"{i}. {entry['name']}: {entry['score']}")
show_history()
system = pick_role()
is_trivia = system == roles["6"][1]
name = input("Enter your name (or 'anonymous'): ")
while True:
    question = input("Ask Claude (or type 'quit'): ")
    if question.lower() == "quit":
        if is_trivia:
            save_score_to_leaderboard(name, score)
        print(f"Final score: {score}")
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
    if "CORRECT!" in reply and "INCORRECT!" not in reply:
        score += 1
    conversation.append({"role": "assistant", "content": reply})