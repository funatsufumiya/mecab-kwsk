import sys
import MeCab
import jaconv

args = sys.argv[1:]
# print(args)
if(len(args) == 0):
    print("引数がありません")
    sys.exit()

def k1_to_kw(kana):
    k = kana[0]
    k2 = kana[0:2]
    k3 = kana[0:3]
    # print(k3)

    if False:
        return None
    elif(k3 in ['しゃう', 'しゅう', 'しょう']):
        return 'sh '
    elif(k3 in ['ちゃう', 'ちゅう', 'ちょう']):
        return 'ch '
    elif(k3 in ['きゃう', 'きゅう', 'きょう']):
        return 'ky '
    elif(k2 in ['しゃ', 'しゅ', 'しょ']):
        return 'sh'
    elif(k2 in ['ちゃ', 'ちゅ', 'ちょ']):
        return 'ch'
    elif(k2 in ['きゃ', 'きゅ', 'きょ']):
        return 'ky'
    elif(k in ['あ','い','う','え','お']):
        if(k == 'あ'):
            return 'a'
        elif(k == 'い'):
            return 'i'
        elif(k == 'う'):
            return 'u'
        elif(k == 'え'):
            return 'e'
        elif(k == 'お'):
            return 'o'
        else:
            return None
    elif(k2 in ['かい','きい','くう','けう','こう']):
        return 'k '
    elif(k in ['が','ぎ','ぐ','げ','ご']):
        return 'g'
    elif(k in ['か','き','く','け','こ']):
        return 'k'
    elif(k in ['さ', 'し', 'す', 'せ', 'そ']):
        return 's'
    elif(k in ['ざ', 'じ', 'ず', 'ぜ', 'ぞ']):
        return 'z'
    elif(k in ['た', 'ち', 'つ', 'て', 'と']):
        return 't'
    elif(k in ['だ', 'ぢ', 'づ', 'で', 'ど']):
        return 'd'
    elif(k in ['な', 'に', 'ぬ', 'ね', 'の']):
        return 'n'
    elif(k in ['は', 'ひ', 'ふ', 'へ', 'ほ']):
        return 'h'
    elif(k in ['ま', 'み', 'む', 'め', 'も']):
        return 'm'
    elif(k in ['や', 'ゆ', 'よ']):
        return 'y'
    elif(k in ['ら', 'り', 'る', 'れ', 'ろ']):
        return 'r'
    elif(k in ['わ', 'を']):
        return 'w'
    elif(k in ['ん']):
        return 'n'
    else:
        return None


def kana_to_kwsk(kana):
    kana = jaconv.kata2hira(kana)
    # print(kana)
    res = []

    while len(kana) > 0:
        r = k1_to_kw(kana)
        if(r != None):
            res.append(r.replace(' ', ''))
            kana = kana[(len(r)):]
        else:
            res.append('')
            kana = kana[1:]

    return res


input = args[0]

mecab = MeCab.Tagger('-Ochasen')
res = mecab.parse(input)
res = list(map(lambda x: x.split('\t'), res.split('\n')))
res = res[:-2]
words = list(map(lambda x: x[0], res))
kanas = list(map(lambda x: x[1], res))
kwsks = list(map(lambda x: ''.join(kana_to_kwsk(x)), kanas))
print(words)
print(kanas)
print(kwsks)
