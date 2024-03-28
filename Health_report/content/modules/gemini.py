import os

import google.generativeai as genai
from IPython.display import display

GOOGLE_API_KEY = ''


genai.configure(api_key=GOOGLE_API_KEY, transport='rest')

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)

    # Set up the model
generation_config = {
"temperature": 0.3,
"top_p": 1,
"top_k": 1,
"max_output_tokens": 2000,
}


model = genai.GenerativeModel(model_name="gemini-pro",
                            generation_config=generation_config)

class Gemini:
    def askGemini(self, prompt):
        response = model.generate_content(prompt)
        return response
