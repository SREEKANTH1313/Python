print("Welcome to Amigos Website tutorial")
mail_id = input("Enter your mal id: ")
# print(first_name , lastname
username = mail_id[: mail_id.index('@')]
domain = mail_id[mail_id.index('@') + 1: ]
print(f"your username: {username} and domain name: {domain}")
