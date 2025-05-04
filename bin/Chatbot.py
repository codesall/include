def chatbot():
    print("Customer Support Bot: Hello! How can I assist you today?")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ").lower()

        if 'exit' in user_input:
            print("Customer Support Bot: Thank you for chatting with us. Have a great day!")
            break

        elif 'refund' in user_input:
            print("Customer Support Bot: To request a refund, please visit our Refunds page or contact support@example.com.")

        elif 'order status' in user_input or 'track' in user_input:
            print("Customer Support Bot: You can track your order using the tracking link sent to your email.")

        elif 'cancel order' in user_input:
            print("Customer Support Bot: To cancel an order, go to your orders page and click on 'Cancel Order'.")

        elif 'return policy' in user_input:
            print("Customer Support Bot: Our return policy allows returns within 30 days of delivery.")

        elif 'payment' in user_input or 'failed' in user_input:
            print("Customer Support Bot: Please ensure your card details are correct or try a different payment method.")

        else:
            print("Customer Support Bot: I'm sorry, I didn't understand that. Please rephrase your question or contact support@example.com.")

# Run the chatbot
chatbot()
