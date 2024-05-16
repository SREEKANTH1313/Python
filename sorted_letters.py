print("Please enter a name or some words")
user_input = input(" : ")
words = " "
for indx, char in enumerate(user_input):
    if indx == 0:
        words += char.upper()
    else:
        words += char.lower()
print(words)
    
