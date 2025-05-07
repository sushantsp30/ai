def shopping_chatbot():
    print(" Welcome to ShopBot! How can I help you today?")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            print("ShopBot: Hello! How can I assist you today?")
        elif "track" in user or "order" in user:
            print("ShopBot: Please enter your order ID to track your order.")
        elif "return" in user or "refund" in user:
            print("ShopBot: Our return policy allows returns within 30 days. Would you like to start a return?")
        elif "product" in user or "item" in user:
            print("ShopBot: Please specify the product name you're looking for.")
        elif "payment" in user or "pay" in user:
            print("ShopBot: We accept credit card, debit card, and UPI payments.")
        elif "bye" in user or "exit" in user:
            print("ShopBot: Thank you for visiting. Have a great day! ")
            break
        else:
            print("ShopBot: I'm sorry, I didn't understand that. Could you rephrase?")

# Call the chatbot function to start it
if __name__ == "__main__":
    shopping_chatbot()
