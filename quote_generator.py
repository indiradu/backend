from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
 
 
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Разрешить запросы с вашего React приложения
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quotes = [
    'I dont now...',
    'Success is my only option, filure is not',
    'Hard work beats talent when talent fails to work hard',
    'Hard work pays off',
    'Dream big, work hard',
    'Impossible = I am possible',
    'What stands on the way becomes the way',
]
 
def generate_quote():
    return quotes[random.randint(0, len(quotes) - 1)]
 
@app.get("/generate_quote")
def get_quote():
    return {'quote': generate_quote()}

#http://localhost:5173