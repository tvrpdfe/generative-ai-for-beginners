from openai import OpenAI
import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

# configure OpenAI service client 
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

deployment="deepseek-v4-flash"

# add your completion code
# prompt = "Complete the following: Once upon a time there was a"
prompt = "Complete the following in chinese, 800 words: Once upon a time there was a girl"
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages)

# print response
if completion.choices and completion.choices[0].message is not None:
    print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.
