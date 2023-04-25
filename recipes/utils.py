import random

def get_random_quote():
    quotes = [
        "Be the change that you wish to see in the world.",
        "Success is not final, failure is not fatal: it is the courage to continue that counts.",
        "Believe you can and you're halfway there.",
        "Happiness is not something ready made. It comes from your own actions.",
        "If you can dream it, you can achieve it.",
        "Don't watch the clock; do what it does. Keep going.",
        "The only way to do great work is to love what you do.",
        "Strive not to be a success, but rather to be of value."
    ]
    print("here in utils.py")
    return random.choice(quotes)