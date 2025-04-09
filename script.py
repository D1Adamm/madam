from dotenv import load_dotenv
from openai import OpenAI

# Loading environment variables
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OpenAIAPI")

# OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a hepfull chatbot"},
                  {"role": "user", "content": prompt}]
    )

    print(response.choices[0].message.content)
    
    return response.choices[0].message.content

prompt = input("Write something to ask to Kody: ")
