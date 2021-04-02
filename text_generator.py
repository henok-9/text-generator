from nltk import regexp_tokenize
from nltk import WhitespaceTokenizer


def tokenization():
    while True:
        prompt = input('>')

        if prompt == 'exit':
            exit()
        try:
            file = open(prompt, 'r', encoding='utf-8')
            # tokens = regexp_tokenize(file.read(), r"[\w!]+")
            tokens = WhitespaceTokenizer().tokenize(file.read())
            token_count = len(tokens)
            unique_tokens_count = len(set(tokens))
            print(f'Corpus statistics\nAll tokens: {token_count}\nUnique tokens: {unique_tokens_count}')
            break
        except FileNotFoundError:
            print('File not found in directory')
        
        
    while True:
        idx = input()

        if idx == 'exit':
            exit()
        try:
            print(tokens[int(idx)])
        except TypeError:
            print('Type Error. Please input an integer.')
        except IndexError:
            print('Index Error. Please input an integer that is in the range of the corpus.')
        except ValueError:
            print('Value Error. Please input an integer.')


tokenization()


