import openai
from models import db, Law, Article, Question

openai.api_key = 'YOUR_OPENAI_KEY'

def generate_and_import_questions(law_text, count=10):
    # Chamada à API do OpenAI para gerar questões
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role':'system','content':'Você é um gerador de questões.'},
            {'role':'user','content':f'Gere {count} questões certo/errado e múltipla escolha com fundamentação literal a partir do texto da lei: {law_text}'}
        ]
    )
    # Lógica de parsing e inserção das questões no BD (a implementar)
    return