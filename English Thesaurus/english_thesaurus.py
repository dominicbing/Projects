import json
from difflib import get_close_matches

# Loading the Data in from the JSON file
data = json.load(open("data.json"))

# Function will take a word given by the user and find the closest match in the JSON file
def translate(w):
    
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    
    # Checking if a similar word exists in the JSON file
    elif len(get_close_matches(w, data.keys())) > 0:
        # Will prompt the user if they meant the most similar word in the JSON file
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

# Prompting the user for the word
word = input("Enter word: ")
output = translate(word)

# If there are several definitions for a word, return them in a readable format
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
