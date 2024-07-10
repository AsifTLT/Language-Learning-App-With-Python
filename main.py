import random

words = [
    {"spanish": "hola", "english": "hello"},
    {"spanish": "adiós", "english": "goodbye"},
    {"spanish": "por favor", "english": "please"},
    {"spanish": "gracias", "english": "thank you"},
    {"spanish": "lo siento", "english": "sorry"},
    {"spanish": "sí", "english": "yes"},
    {"spanish": "no", "english": "no"},
    {"spanish": "¿cómo estás?", "english": "how are you?"},
    {"spanish": "bien", "english": "well"},
    {"spanish": "mal", "english": "bad"},
    {"spanish": "buenos días", "english": "good morning"},
    {"spanish": "buenas tardes", "english": "good afternoon"},
    {"spanish": "buenas noches", "english": "good night"},
    {"spanish": "¿qué tal?", "english": "what's up?"},
    {"spanish": "mucho gusto", "english": "nice to meet you"},
    {"spanish": "¿dónde está...?", "english": "where is...?"},
    {"spanish": "baño", "english": "bathroom"},
    {"spanish": "comida", "english": "food"},
    {"spanish": "agua", "english": "water"},
    {"spanish": "amigo", "english": "friend"},
    {"spanish": "familia", "english": "family"},
    {"spanish": "casa", "english": "house"},
    {"spanish": "trabajo", "english": "work"},
    {"spanish": "escuela", "english": "school"},
    {"spanish": "tiempo", "english": "time"},
    {"spanish": "dinero", "english": "money"},
    {"spanish": "mañana", "english": "tomorrow"},
    {"spanish": "hoy", "english": "today"},
    {"spanish": "ayer", "english": "yesterday"},
    {"spanish": "feliz", "english": "happy"},
    {"spanish": "triste", "english": "sad"},
    {"spanish": "grande", "english": "big"},
    {"spanish": "pequeño", "english": "small"},
    {"spanish": "nuevo", "english": "new"},
    {"spanish": "viejo", "english": "old"},
    {"spanish": "rápido", "english": "fast"},
    {"spanish": "lento", "english": "slow"},
    {"spanish": "calor", "english": "hot"},
    {"spanish": "frío", "english": "cold"},
    {"spanish": "bonito", "english": "pretty"},
    {"spanish": "feo", "english": "ugly"},
    {"spanish": "fácil", "english": "easy"},
    {"spanish": "difícil", "english": "difficult"},
    {"spanish": "cerca", "english": "near"},
    {"spanish": "lejos", "english": "far"},
    {"spanish": "día", "english": "day"},
    {"spanish": "noche", "english": "night"},
    {"spanish": "semana", "english": "week"},
    {"spanish": "mes", "english": "month"},
    {"spanish": "año", "english": "year"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"},
]

def quiz_user(words):
    random.shuffle(words)
    score = 0
    
    for word in words:
        print(f"What is the English translation of '{word['spanish']}'? ")
        user_answer = input("Your Answer: ").strip().lower()
        correct_answer = word['english'].lower()
        
        if user_answer == correct_answer:
            print("Correct Answer!!\n")
            score += 1
        else:
            print(f"Wrong, The Correct Answer is '{word['english']}'\n")    

    print(f"Quiz Complete! Your Score is: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning FlashCards App! ")
    input("Press Enter to Start the Quiz: ")
    quiz_user(words)

if __name__ == "__main__":
    main()
