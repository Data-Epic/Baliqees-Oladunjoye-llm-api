# Customer Support Assistant 
The Customer Support Assistant is a simple, rule-based Python assistant designed to help respond to customer inquiries about a smoked food business. It provides relevant replies to frequently asked questions about available products and politely handles unusual queries. This project is beginner-friendly and can be extended for other types of businesses.

Setup Instructions

Clone the Repository

Open your terminal or Git Bash and run:

git clone https://github.com/Data-Epic/Baliqees-Oladunjoye-llm-api.git

cd customer_support

# Install Required Dependencies
	If you have a requirements.txt file:
	pip install -r requirements.txt
	If not, simply install pytest manually for testing:
	pip install pytest
# How to Run the Assistant
You can run the assistant from your Python script or shell by importing the class and calling the get_response() method.
from CSA import CustomerSupportAssistant
assistant = CustomerSupportAssistant()
response = assistant.get_response("Do you sell smoked fish?")
print(response)
To ensure the assistant is working correctly, you can run:
Pytest
This will execute all test cases in test_CSA.py.

# Example Usage
assistant.get_response("Do you sell smoked chicken?")
#Output: "Yes! We offer delicious smoked chicken prepared with traditional spices..."

assistant.get_response("Do you sell dragons?")
#Output: "Thank you for reaching out! Unfortunately, we don't sell dragons as they are mythical creatures..."

Limitations
The assistant uses simple keyword matching and may not understand very complex or unrelated questions.


It does not connect to a live inventory or database.


It cannot learn or adapt based on user input (no machine learning is used).


# Future Improvements
Add natural language processing (NLP) for better question understanding.


Integrate a web interface or chatbot (e.g., WhatsApp, Telegram, or web app).


Connect to a real-time product inventory system.


Enable logging and feedback handling for improvement over time.


Support for multilingual responses and personalization.


# Author
Baliqees Oladunjoye
LinkedIn: https://www.linkedin.com/in/baliqees-oladunjoye-986260bb/
Email: baliqeesoladunjoye@gmail.com






