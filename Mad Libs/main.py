gender = input("Gender : ") # Takes a Gender
noun = input("Noun : ") # Takes a Noun
pronoun = input("pronun : ") # Takes a Pronoun
adjective = input("adjective : ") # Takes a Adjective
verb = input("verb : ") # Takes a Verb
if gender.lower() == "male" or gender.lower() == "female" or gender.lower() == "gay" or gender.lower() == "lesbian": # if gender is male or female it woll be converted in boy or girl and if its gay or lesbian will be converted respectively
    if gender.lower() =="male" or gender.lower == "gay":
        gender = "boy"
    else:
        gender = "girl"

gender = gender.lower()
noun = noun.title()
titpronoun = pronoun.title()
lopronoun = pronoun.lower()
adjective = adjective.lower()
verb = verb.lower()

print(f"once upon a time there was a {gender} named {noun} he was {verb}ing in a car. \n{titpronoun} was {adjective} but {lopronoun} didn\'t care about it. End") # Outputting a Story
