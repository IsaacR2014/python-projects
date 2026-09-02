import json
import anthropic
from datetime import date
def load_habits():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except:
        return []
def save_habits(habits):
    with open("habits.json", "w") as f:
        json.dump(habits, f)

def add_habit(habits):
    name = input("What will the name of your habit be? ")
    habits.append({"name": name, "streak": 0, "last_checked": None})
    save_habits(habits)
    print(f"Habit '{name}' added!")
    return habits
def view_habits(habits):
    if not habits:
        print("No habits yet! Add one first.")
        add_habit(habits)
        return
    print("📋 YOUR HABITS")
    for i, habit in enumerate(habits, 1):
        if habit["streak"] > 0:
            print(f"{i}. {habit['name']} - 🔥 {habit['streak']} day streak!")
        else:
            print(f"{i}. {habit['name']} - 💀 No streak yet")
def check_in(habits):
    view_habits(habits)
    choice = int(input("Which habit did you complete? (enter number): ")) - 1
    if 0 <= choice < len(habits):
        today = str(date.today())
        if habits[choice]["last_checked"] == today:
            print("Already checked in today! Come back tomorrow! 😄")
        else:
            habits[choice]["streak"] += 1
            habits[choice]["last_checked"] = today
            save_habits(habits)
            print(f"✅ Great job! {habits[choice]['name']} streak: {habits[choice]['streak']} days!")
    else:
        print("Invalid choice!")
    return habits
def run_alfred():
    habits = load_habits()
    print("👋 Welcome to Alfred!")
    while True:
        print("\n1. View habits")
        print("2. Add habit")
        print("3. Check in")
        print("4. Quit")
        print("5. Talk to Alfred")
        print("6. Uncheck a habit")
        print("7. Delete alfreds chat history")
        choice = input("Choose: ")
        if choice == "1":
            view_habits(habits)
        elif choice == "2":
            habits = add_habit(habits)
        elif choice == "3":
            habits = check_in(habits)
        elif choice == "4":
            print("See you tomorrow! 💪")
            break
        elif choice == "5":
            talk_to_alfred(habits)
        elif choice == "6":
            habits = uncheck_habit(habits)
        elif choice == "7":
            show_history()
        
def talk_to_alfred(habits):
    show_history()
    client = anthropic.Anthropic()
    conversation = []
    system = f"You are Alfred, a supportive life coach AI. The user's current habits and streaks are: {habits}. Use this to motivate them. Be encouraging and positive!"
    print("Alfred: Hi! I'm Alfred your personal coach! Type 'bye' to exit.")
    while True:
        msg = input("You: ")
        if msg.strip() == "":
            continue
        if msg.lower() == "bye":
            print("Alfred: See you tomorrow! Keep it up! 💪")
            save_history(conversation)
            break
        conversation.append({"role": "user", "content": msg})
        response = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=1024,
            system=system,
            messages=conversation[-10:]
        )
        reply = response.content[0].text
        print(f"Alfred: {reply}")
        conversation.append({"role": "assistant", "content": reply})
def uncheck_habit(habits):
    view_habits(habits)
    choice = int(input("Which habit to uncheck? (enter number): ")) - 1
    if 0 <= choice < len(habits):
        if habits[choice]["last_checked"] == str(date.today()):
            habits[choice]["streak"] -= 1
            habits[choice]["last_checked"] = None
            save_habits(habits)
            print(f"↩️ Unchecked {habits[choice]['name']}!")
        else:
            print("This habit wasn't checked today!")
    else:
        print("Invalid choice!")
    return habits
def show_history():
    with open("alfred_history.txt", "a") as f:
        pass
    with open("alfred_history.txt", "r") as f:
        history = f.read()
    if history:
        view = input("View chat history? yes/no: ").lower()
        if view == "yes":
            print(history)
        clear = input("Clear chat history? yes/no: ").lower()
        if clear == "yes":
            open("alfred_history.txt", "w").close()
def save_history(conversation):
    with open("alfred_history.txt", "a") as f:
        for msg in conversation:
            if msg["role"] == "user":
                f.write(f"You: {msg['content']}\n")
            else:
                f.write(f"Claude: {msg['content']}\n")

run_alfred()