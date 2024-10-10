def simple_chatbot(user_input):
    
    # Rules = ("hello/hi": "Hello! How can I help you now?")    
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you now?"
    
    # Rules =("who are you": "I am a simple chatbot program created to assist you!")
    elif "who are you" in user_input:
        return "I am a simple chatbot program created to assist you!"
    
    # Rules =("what is your name ": "My name is chatbot!")
    elif "what is your name" in user_input:
        return "My name is chatbot!"
    
    # Rules = ("how are you": "I'm just a program, but thanks for asking! How can I help you?")
    elif "how are you" in user_input:
        return "I'm just a program, but thanks for asking! How can I help you?"

    # Rules = ("help": "Sure! Please tell me how can i help you?")
    elif "help" in user_input:
        return "Sure! Please tell me how can i help you?"

    # Rules = ("bye": "Goodbye! Have a great day!")
    elif "bye" in user_input in user_input:
        return "Goodbye! Have a great day!"
    
    # Rules = ("exit": "End of the conversation!")
    elif"exit" in user_input:
        return "End of the conversation!"

    else:
        return "I'm sorry, I didn't get you. Plese try again"

# Example of conversation loop
def chat():
    print("Welcome to the chatbot! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        response = simple_chatbot(user_input)
        print("Chatbot:", response)
        
        if user_input in ["exit"]:
            break

# Start the chat
chat()          