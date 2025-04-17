import os
import re  # Added for cleaning response
import logging
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv(dotenv_path=".env")

# Configure logging
logging.basicConfig(filename='chat_logs.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

class CustomerSupportAssistant:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables.")
        self.client = Groq(api_key=self.api_key)
        self.context = (
            "You are a helpful, polite, and knowledgeable customer support assistant for Beem Farms, "
            "a company that sells high-quality packaged smoked chicken, meat, fish, snails, and similar products. "
            "You assist customers with their inquiries, complaints, and product information, including availability, pricing, storage tips, and delivery options. "
            "If a question is outside your capabilities, like strange or unrelated questions (e.g., asking about dragons or magic), "
            "politely inform the customer that a human agent will follow up."
        )

    def get_response(self, user_input):
        try:
            response = self.client.chat.completions.create(
                model="deepseek-r1-distill-llama-70b",
                messages=[
                    {"role": "system", "content": self.context},
                    {"role": "user", "content": user_input}
                ]
            )
            raw_response = response.choices[0].message.content.strip()
            # 🔍 Clean out <think>...</think> block if it exists
            cleaned_response = re.sub(r"<think>.*?</think>", "", raw_response, flags=re.DOTALL).strip()
            return cleaned_response
        except Exception as e:
            return f"Sorry, something went wrong: {str(e)}"

def log_chat(user_input, assistant_response):
    logging.info(f"User: {user_input}")
    logging.info(f"Assistant: {assistant_response}")

def main():
    print("\U0001F4AC Welcome to the Beem Farms Customer Support Assistant!")
    print("I can help with complaints, product inquiries, or feedback. Type 'exit' to quit.\n")

    assistant = CustomerSupportAssistant()

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("\U0001F44B Thank you for chatting with us. Have a great day!")
            break

        if not user_input:
            print("🤖 Assistant: Could you please rephrase or provide more details?")
            continue

        assistant_response = assistant.get_response(user_input)
        print(f"\n🤖 Assistant: {assistant_response}\n")
        print("(Type 'exit' if that will be all.)\n")

        log_chat(user_input, assistant_response)

if __name__ == "__main__":
    main()
