placeholder = "[name]"

with open("../Mail/Input/Letters/starting_letter.txt", mode="r") as file:
    content = file.read()

with open("../Mail/Input/Names/invited_names.txt", mode="r") as names:
    names = names.readlines()

with open("../Mail/Input/Letters/starting_letter.txt", mode="a") as file:
    for name in names:
        mail = content.replace(placeholder, name.strip())
        with open(f"../Mail/Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as letter:
            letter.write(mail)