import json
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
        habits[choice]["streak"] += 1
        habits[choice]["last_checked"] = str(date.today())
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

run_alfred()