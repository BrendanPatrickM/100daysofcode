import pandas


def translate():
    word_to_translate = input('Enter word to translate: ').upper()
    spelling_list = [nato_dict[letter] for letter in word_to_translate]
    print(spelling_list)


nato_data_frame = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in
             nato_data_frame.iterrows()}

complete = False
while not complete:
    try:
        translate()
    except KeyError:
        print('Sorry, please only use letters of the alphabet')
    else:
        complete = True
