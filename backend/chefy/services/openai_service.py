import openai

class openAiService:
    def chat_gpt(self, msg):
        # Set the API key
        openai.api_key = "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"

        # Set the model to use
        model_engine = "text-davinci-002"

        # Set the prompt
        # prompt = "What is the weather like today?"

        # Generate a response
        completion = openai.Completion.create(engine=model_engine, prompt=msg, max_tokens=1024, n=1,stop=None,temperature=0.5)
        response = completion.choices[0].text
        print(completion, response)
        return response
