import random

def list_the_words(filename):
    with open(filename, 'r') as file:
        contents = file.read()

    return contents.split()


# Specify the path to the .txt file(s)

### NOUNS ###
fruits = list_the_words('data\\username-generator\\fruits.txt')
animals = list_the_words('data\\username-generator\\animals.txt')
### NOUNS ###

### ADJECTIVES AND VERBS ###
verbs_and_adjectives = list_the_words('data\\username-generator\\verbs-and-adjectives.txt')
### ADJECTIVES AND VERBS ###

combined_wordlist = []
combined_wordlist.extend(fruits)
combined_wordlist.extend(animals)

random_word = random.choice(combined_wordlist)
random_adjective_or_verb = random.choice(verbs_and_adjectives)
random_numbers = random.randrange(1000)

# Print the randomly chosen word
print(f'Randomly generated username:\n\n {random_adjective_or_verb}{random_word}{random_numbers}\n')
