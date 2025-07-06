import openai
from models import db, Law, Article, Question

openai.api_key = 'YOUR_OPENAI_KEY'

def generate_and_import_questions(law_text, count=10):
    # Call OpenAI to generate questions based on law_text
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[{'role':'system','content':'You are a question generator.'},
                  {'role':'user','content':f'Generate {count} true/false and multiple-choice questions from the following law text: {law_text}'}]
    )
    # Parse and save questions (omitted for brevity)
    # This is a stub; implement parsing logic here
    return