from nltk import word_tokenize 
from nltk import regexp_tokenize



def tokenization(file_name):
    file = open(file_name, 'r', encoding='utf-8')
    tokens = regexp_tokenize(file.read(), r"[\w'\-!]+")
    token_count = len(tokens)
    unique_tokens_count = len(set(tokens))

    while True:
        prompt = input('>')
        if prompt == file_name:
            print(f'Corpus statistics\nAll tokens: {token_count}\nUnique tokens: {unique_tokens_count}')
        else:
            try:
                print(tokens[int(prompt)])
            except TypeError:
                print('Type Error. Please input an integer.')
            except IndexError:
                print('Index Error. Please input an integer that is in the range of the corpus.')
            except ValueError:
                print('Value Error. Please input an integer.')

        if prompt == 'exit':
            exit()



tokenization(input())