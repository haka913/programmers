# n = 3
# words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']


# n = 2
# words =['hello', 'one', 'even', 'never', 'now', 'world', 'draw']
n = 5
words =['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']

def soltuion(n, words):
    idx = 0
    lis = []
    tmp=''
    for i, word in enumerate(words):
        if i == 0:
            lis.append(word)
            tmp = word[-1]
            continue

        if word[0] == tmp:
            if word in lis:
                print("duplicated")
                idx = i
                break
            else:
                lis.append(word)
                tmp = word[-1]
        else:
            print("wrong different")
            idx = i
            break

        if lis == words:
            return [0, 0]

    return [(idx%n)+1, (idx//n)+1]

print(soltuion(n,words))