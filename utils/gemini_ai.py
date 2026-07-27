import os

import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.6-flash")


class GeminiLLM:

    def invoke(self, prompt):

        response = model.generate_content(prompt)

        class Result:
            def __init__(self, text):
                self.content = text

        return Result(response.text)