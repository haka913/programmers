def changeSound(song):
    return song.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')


def solution(m, musicinfos):
    m = changeSound(m)
    dic = dict()

    answer = ''
    for str in musicinfos:
        start, end, title, song = str.split(',')
        h1, m1 = map(int, start.split(':'))
        h2, m2 = map(int, end.split(':'))
        time = (h2 - h1) * 60 + m2 - m1
        song = changeSound(song)
        song = song * (time // len(song)) + song[0:time % len(song)]
        dic[song] = title

    for song in dic.keys():
        if m in song:
            if answer == '':
                answer = song
            else:
                if len(answer) < len(song):
                    answer = song

    return dic[answer] if answer != '' else "(None)"

print(solution(m='ABCDEFG', musicinfos=['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']))
