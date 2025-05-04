import nltk
from nltk.chat.util import Chat, reflections

# Download necessary NLTK data
nltk.download('punkt')

# Define some simple conversation patterns
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?"]
    ],
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm just a bot, but I'm doing great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["No worries!", "It's okay.", "Don't worry about it."]
    ],
    [
        r"i'm (.*) doing good",
        ["That's great to hear!", "Awesome!"]
    ],
    [
        r"what is your name ?",
        ["I'm a chatbot created by Aditya.", "You can call me ChatBot."]
    ],
    [
        r"how old are you?",
        ["I'm timeless!"]
    ],
    [
        r"what can you do?",
        ["I can chat with you and answer basic questions."]
    ],
    [
        r"(.*) help (.*)",
        ["Sure, I'm here to help you. What do you need?"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "See you later!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you please rephrase?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Start conversation
print("Hi! I'm ChatBot. Type 'bye' or 'exit' to end the chat.")
chatbot.converse()
