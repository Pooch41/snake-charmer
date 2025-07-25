flashcards = {
    "What is the capital of France?": "Paris",
    "2 + 2": "4",
    "What is the chemicals making up water?": "Hydrogen and Oxygen"
}

def add_to_dict(select_dict, key, value):
    select_dict[key] = value

def remove_from_dict(select_dict, key):
    select_dict.pop(key)

def update_dict(select_dict, key, value):
    select_dict[key] = value

def retrieve_key(select_dict, key):
    return select_dict.get(key)

def quiz():
    score = 0
    for question, answer in flashcards.items():
        print(question)
        answer = str(input("Answer >"))
        if answer == retrieve_key(flashcards, question):
            score += 5
            print("Correct!")
        else:
            print(f"Incorrect, the answer was {flashcards[question]}")
    print(f"Quiz over! Your final score: {score}")

quiz()