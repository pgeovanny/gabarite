from models import Answer, Question
from sqlalchemy import func

def get_stats(user_id):
    # Return dummy stats structure
    return {'total': 100, 'correct': 80, 'per_difficulty': {'Fácil': 50, 'Médio': 30, 'Difícil': 20}}