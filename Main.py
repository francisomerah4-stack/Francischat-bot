# main.py
# FrancisChat-Bot — a simple AI chatbot that learns from user input

import json
import random

# Save and load memory from a JSON file
MEMORY_FILE = "chat_memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_memory(memory):
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

def get_response(user_input, memory):
    user_input = user_input.lower()

    # If bot has seen this before
    if user_input in memory:
        return random.choice(memory[user_input])

    # Default replies
    default_responses = [
        "That's interesting! Tell me more.",
        "Hmm, I see. What else?",
        "Can you explain that a bit more?",
        "I'm still learning from you!",
    ]
    return random.choice(default_responses)

def main():
    print("🤖 FrancisChat-Bot: Hello! I’m your AI assistant. Type 'bye' to quit.\n")
    memory = load_memory()

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("🤖 FrancisChat-Bot: Bye! See you next time 👋")
            save_memory(memory)
            break

        response = get_response(user_input, memory)
        print("🤖 FrancisChat-Bot:", response)

        # Learn new things
        feedback = input("(Teach me) What should I reply next time when you say that? (Press Enter to skip): ")
        if feedback:
            if user_input not in memory:
                memory[user_input] = []
            memory[user_input].append(feedback)

main()
