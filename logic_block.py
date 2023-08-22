from pathlib import Path

def take_in(word_pair: str)->dict:
    word = word_pair.split('-')[0]
    translation = word_pair.split('-')[-1]
    return {word:translation}

def read_from(id: str)->list:
    word_pairs = list()
    if Path(f'data\{id}.txt').is_file():
        words = open(f'data\{id}.txt', 'r')
        for i in words:
            word_pairs.append(i)
        words.close
        return sorted(word_pairs)
    else:
        return 'error. database has no such id'


def saving(vocab: dict, id: str):
    if Path(f'data\{id}.txt').is_file():
        write_pair = open(f'data\{id}.txt', 'a+t')
        for i in vocab:
            write_pair.write(f'\n{i}-{vocab[i]}')
        write_pair.close
    else:
        write_pair = open(f'data\{id}.txt', 'x')
        for i in vocab:
            write_pair.write(f'{i}-{vocab[i]}')
        write_pair.close
    return None

def delete(word: str, id: str)->str:
    word_pairs = list()
    if Path(f'data\{id}.txt').is_file():
        words = open(f'data\{id}.txt', 'a+t')
        for i in words:
            word_pairs.append(i)
        words.truncate(0)
        words.close
        for j in word_pairs:
            if j.split('-')[0] == word or j.split(' -')[0] == word or j.split(' - ')[0] == word or j.split('- ')[0] == word:
                pass
            else:
                saving(take_in(j), id)
        return "Successfully"
    else:
        return 'error. database has no such id'

def letter_request(letter: str, word_pairs: list)->list:
    alfabet = {
        'A' : 'a',
        'B' : 'b',
        'C' : 'c',
        'D' : 'd',
        'E' : 'e',
        'F' : 'f',
        'G' : 'g',
        'H' : 'h',
        'I' : 'i',
        'J' : 'j',
        'K' : 'k',
        'L' : 'l',
        'M' : 'm',
        'N' : 'n',
        'O' : 'o',
        'P' : 'p',
        'R' : 'r',
        'S' : 's',
        'T' : 't',
        'U' : 'u',
        'V' : 'v',
        'W' : 'w',
        'X' : 'x',
        'Y' : 'y',
        'Z' : 'z'
    }
    resulting = list()
    for i in word_pairs:
        if i[0] == letter or i[0] == alfabet[letter]:
            resulting.append(i)
    return resulting

if __name__ == '__main__':

    local_vocab_w = dict()
    local_vocab_r = dict()
    output_words = str()

    user_id = str(input('Write your id'))
    words = input('Write your words with translation, separate word and translation with \"-\" ')
    #local_vocab_w = local_vocab_w|take_in(words)
    #letter = input('write first letter of words that you want to pull: ')
    saving(local_vocab_w, user_id)
    #q = read_from(user_id)
    word = 'we'
    kk = '13'
    #delete(word,kk)
    '''for i in q:
        if i[0] == letter:
            output_words += '(o) ' + f'{i}'
    print(output_words)'''