from datetime import datetime
import time

print("🤖 Hello! I'm ChatBot. Type 'exit' anytime to end the chat.")
print("-" * 60)

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ['hello', 'hi', 'hey']:
        print("Bot: Hello there! 👋 How can I assist you today?")

    elif user_input == 'how are you':
        print("Bot: I'm just a bunch of Python code, but I'm running smoothly! 💻")

    elif user_input == 'what is your name':
        print("Bot: I'm ChatBot 🤖 — your simple rule-based assistant!")

    elif user_input == 'time':
        current_time = datetime.now().strftime("%I:%M %p")
        print(f"Bot: The current time is {current_time} ⏰")

    elif user_input == 'date':
        current_date = datetime.now().strftime("%A, %d %B %Y")
        print(f"Bot: Today's date is {current_date} 📅")

    elif user_input == 'help':
        print("Bot: 🤔 Try saying:")
        print(" 👉 'hello', 'how are you', 'time', 'date', 'bye', or 'exit'")

    elif user_input == 'bye':
        print("Bot: Bye! 👋 Have a great day ahead! 😊")
        break

    elif user_input == 'exit':
        print("Bot: Exiting the chat. Stay safe and happy coding! ✨")
        break

    else:
        print("Bot: 😕 Oops! I didn't get that. Try typing 'help' for suggestions.")

    time.sleep(0.5)

print("-" * 50)
print("🤖 Thank you for chatting with me! Goodbye! 👋")