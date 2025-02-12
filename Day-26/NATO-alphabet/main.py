import pandas
nato = pandas.read_csv('nato_phonetic_alphabet.csv')

nato_dict = {row.letter: row.code for (index, row) in nato.iterrows()}
user_input = input("Enter a word: ").upper()
output_nato = [nato_dict[letter] for letter in user_input]

print(output_nato)
