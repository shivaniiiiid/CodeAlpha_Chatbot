# chatbot.py

import nltk
from nltk.tokenize import word_tokenize
import random

# Download required data
nltk.download('punkt')

# Response database (basic intent simulation)
responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you?"],
    "name": ["I'm CodeBot, your Python assistant.", "They call me CodeBot!"],
    "how_are_you": ["I'm doing great, thank you!", "Functioning as expected!"],
    "goodbye": ["Goodbye! Have a great day!", "Bye! Take care!", "See you soon!"],
    "default": ["I'm not sure I understand that.", "Could you rephrase that?", "Hmm... I didn't get that."]
}

# Keyword mapping to intents
intent_keywords = {
    "greeting": ["hello", "hi", "hey"],
    "name": ["your name", "who are you"],
    "how_are_you": ["how are you", "how are things", "how's it going"],
    "goodbye": ["bye", "goodbye", "exit", "see you"]
}

def get_intent(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    for intent, keywords in intent_keywords.items():
        for word in keywords:
            if word in user_input or word in tokens:
                return intent
    return "default"

def respond(user_input):
    intent = get_intent(user_input)
    return random.choice(responses[intent])

# Chat loop
print(" Hello! I'm CodeBot. Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ")
    if 'exit' in user_input.lower():
        print("CodeBot:", random.choice(responses["goodbye"]))
        break
    response = respond(user_input)
    print("CodeBot:", response)
