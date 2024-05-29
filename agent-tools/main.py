from dotenv import dotenv_values

import flask
import functions_framework

import google.generativeai as genai

config = dotenv_values(".env")

GEMINI_API_KEY = config["GEMINIPRO_API"]
PROJECT_ID = config["PROJECT_ID"]
REGION = config["REGION"]

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

# @functions_framework.http
def generate_joke(request: flask.Request) -> flask.typing.ResponseReturnValue:

    SAFETY_SETTINGS = {
    'HATE':'BLOCK_ONLY_HIGH',
    'HARASSMENT':'BLOCK_ONLY_HIGH',
    'SEXUAL':'BLOCK_MEDIUM_AND_ABOVE',
    'DANGEROUS':'BLOCK_LOW_AND_ABOVE'
    }

    generation_config = genai.GenerationConfig(
        candidate_count=1,
        max_output_tokens=500,
        stop_sequences=['x'],
        temperature=0.9
        )

    prompt = "Tell me a random joke about plants"
    response = model.generate_content(prompt,
                                    safety_settings=SAFETY_SETTINGS,
                                    generation_config=generation_config
                                    )

    print(response.text)
    
   
    return response.text