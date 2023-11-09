import openai


class CLS_GPTBot:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def query(self, prompt, engine="gpt-4-1106-preview", temperature=0.7):
        try:
            response = openai.ChatCompletion.create(
                model=engine,  # "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature = temperature
            )
            chatbot_response = response['choices'][0]['message']['content']
            print("Chatbot:", chatbot_response)
        except openai.OpenAIError as e:
            print(f"An error occurred: {e}")
            return None


# Usage example
if __name__ == "__main__":
    # You should replace 'your-api-key' with your actual OpenAI API key
    api_key = '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'
    gpt = GPTWrapper(api_key)

    prompt = "Translate the following English text to French: 'Hello, how are you?'"
    response = gpt.query(prompt)
    print(response)
