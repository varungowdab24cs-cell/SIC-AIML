
from groq import Groq 

# Read API keys
with open("C:\\Users\\SIC\\Desktop\\Projects\\practices\\api-key.txt", "r") as f:
    api_key = f.read().strip()


# Initialize Groq client
client = Groq(api_key="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")


# Select model
model = "llama-3.1-8b-instant"  # Replace with your desired model

# Chat function
# (Removed accidental imports that shadow `client` and `model`)



def chat():

    # Welcome message
    print("Welcome to the chatbot!")

    # Conversation history (list)
    conversation_history = []

    # Inifinite loop
    while True:
    
        # User input
        user_input = input("You: ")

        # Check for the exit condition (exit, quit, end)
        if user_input.lower() in ["exit", "quit", "end"]:
            print("AI: Goodbye!")
            break

        # Add user input to conversation history
        conversation_history.append({"role": "user", "content": user_input})

        # Build a prompt using conversation history
        prompt = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation_history])
        try:

            # Get the Groq response
            response = client.chat.completions.create(
                model=model,
                messages=conversation_history
            )


            # extract the output text
            ai_output = response.choices[0].message.content



            # print the output text
            print(f"AI: {ai_output}")


            # add the ai message into the conversation history as an object with a role
            conversation_history.append({"role": "assistant", "content": ai_output})

        except Exception as e:

            # Add an exception message
            print(f"AI: Sorry, I encountered an error: {str(e)}")

# run the chatbot
if __name__ == "__main__":
    chat()