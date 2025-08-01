def chatbot():
    print("🤖 Chatbot: Hello! Type something to start a conversation (type 'exit' to end).")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("🤖 Chatbot: Hi!")
        elif user_input == "how are you":
            print("🤖 Chatbot: I'm fine, thanks! How about you?")
        elif user_input == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day!")
            break
        elif user_input == "exit":
            print("🤖 Chatbot: Chat ended.")
            break
        else:
            print("🤖 Chatbot: Sorry, I didn't understand that.")


chatbot()
