import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data (only required for the first time)
nltk.download('punkt')

# Define pairs of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you! How about you?", "I'm just a bot, but I'm here to help!"]
    ],
    [
        r"what is your name ?",
        ["I am a chatbot. You can call me ChatGPT!", "I'm your friendly neighborhood chatbot!"]
    ],
    [
        r"what can you do ?",
        ["I can answer your questions, provide information, or just chat with you!", "I'm here to assist you with any queries you have."]
    ],
    [
        r"quit|bye|exit",
        ["Goodbye! Have a great day!", "Bye! Feel free to come back anytime."]
    ],
    [
        r"tell me about (.*)",
        ["I'm sorry, I don't have information about %1. Can you ask something else?", "I'm not sure about %1. Let me know if you have other questions!"]
    ],
    [
        r"help",
        ["Sure! I can help you. What do you need assistance with?", "I'm here to help. What's your question?"]
    ],
    [
        r"what is the weather like today ?",
        ["I'm not connected to a weather service, but you can check your local weather app!", "I don't have real-time weather data. Sorry!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem! Happy to help."]
    ],
    [
        r"what is ai ?",
        ["AI stands for Artificial Intelligence. It refers to machines designed to perform tasks that typically require human intelligence, such as learning, reasoning, and problem-solving."]
    ],
    [
        r"what is machine learning ?",
        ["Machine Learning is a subset of AI that involves training algorithms to learn patterns from data and make predictions or decisions without being explicitly programmed."]
    ],
    [
        r"what is nlp ?",
        ["NLP stands for Natural Language Processing. It is a field of AI that focuses on enabling machines to understand, interpret, and generate human language."]
    ],
    [
        r"who created you ?",
        ["I was created by a developer using Python and the NLTK library.", "I'm a simple chatbot built with Python!"]
    ],
    [
        r"what is python ?",
        ["Python is a high-level programming language known for its simplicity and readability. It is widely used for web development, data analysis, AI, and more."]
    ],
    [
        r"how does a chatbot work ?",
        ["Chatbots work by processing user input, understanding the intent using NLP techniques, and generating appropriate responses based on predefined rules or machine learning models."]
    ],
    [
        r"what are your limitations ?",
        ["I am a rule-based chatbot, so my responses are limited to predefined patterns. I cannot learn or adapt on my own like advanced AI models."]
    ],
    [
        r"can you learn ?",
        ["No, I cannot learn on my own. I am a rule-based chatbot and can only respond based on predefined patterns."]
    ],
    [
        r"what is your purpose ?",
        ["My purpose is to assist you by answering your questions and providing information to the best of my abilities."]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "What do you call fake spaghetti? An impasta!"]
    ],
    [
        r"what is the capital of (.*)",
        ["I'm not sure about the capital of %1. You might want to check a geography resource!", "I don't have that information. Sorry!"]
    ],
    [
        r"what is the meaning of life ?",
        ["The meaning of life is a philosophical question. Some say it's 42, according to 'The Hitchhiker's Guide to the Galaxy'!", "That's a deep question! It depends on your perspective."]
    ]
]

# Create a chatbot
chatbot = Chat(pairs, reflections)

# Function to start the chatbot
def start_chat():
    print("Hello! I'm your AI chatbot. Type 'quit' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "bye", "exit"]:
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    start_chat()