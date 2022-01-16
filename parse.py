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
    elif(k3 in ['という']):
        return 'ti '
    elif(k3 in ['しゃう', 'しゅう', 'しょう']):
        return 's  '
    elif(k3 in ['じゃう', 'じゅう', 'じょう']):
        return 'j  '
    elif(k3 in ['しゃい', 'しゅい', 'しょい']):
        return 'sh '
    elif(k3 in ['じゃい', 'じゅい', 'じょい']):
        return 'j  '
    elif(k3 in ['りゃい', 'りゅい', 'りょい']):
        return 'ry '
    elif(k3 in ['ちゃう', 'ちゅう', 'ちょう']):
        return 'ch '
    elif(k3 in ['きゃう', 'きゅう', 'きょう']):
        return 'ky '
    elif(k3 in ['りゃう', 'りゅう', 'りょう']):
        return 'ry '
    elif(k2 in ['しゃ', 'しゅ', 'しょ']):
        return 'sh'
    elif(k2 in ['じゃ', 'じゅ', 'じょ']):
        return 'j '
    elif(k2 in ['りゃ', 'りゅ', 'りょ']):
        return 'ry'
    elif(k2 in ['ちゃ', 'ちゅ', 'ちょ']):
        return 'ch'
    elif(k2 in ['きゃ', 'きゅ', 'きょ']):
        return 'ky'
    elif(k2 in ['ああ', 'いい', 'うう', 'ええ', 'おお']):
        if(k == 'あ'):
            return 'a '
        elif(k == 'い'):
            return 'i '
        elif(k == 'う'):
            return 'u '
        elif(k == 'え'):
            return 'e '
        elif(k == 'お'):
            return 'o '
    elif(k2 in ['あう', 'いう', 'えう', 'おう']):
        if(k == 'あ'):
            return 'a '
        elif(k == 'い'):
            return 'i '
        elif(k == 'う'):
            return 'u '
        elif(k == 'え'):
            return 'e '
        elif(k == 'お'):
            return 'o '
    elif(k in ['あ', 'い', 'う', 'え', 'お']):
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
    elif(k2 in ['かい', 'きい', 'くい', 'けい', 'こい']):
        return 'k '
    elif(k2 in ['かう', 'きう', 'くう', 'けう', 'こう']):
        return 'k '
    elif(k in ['が', 'ぎ', 'ぐ', 'げ', 'ご']):
        return 'g'
    elif(k in ['か', 'き', 'く', 'け', 'こ']):
        return 'k'
    elif(k2 in ['さい', 'しい', 'すい', 'せい', 'そい']):
        return 's '
    elif(k2 in ['さう', 'しう', 'すう', 'せう', 'そう']):
        return 's '
    elif(k in ['さ', 'し', 'す', 'せ', 'そ']):
        return 's'
    elif(k in ['ざ', 'じ', 'ず', 'ぜ', 'ぞ']):
        return 'z'
    elif(k2 in ['たい', 'ちい', 'つい', 'てい', 'とい']):
        return 't '
    elif(k2 in ['たう', 'ちう', 'つう', 'てう', 'とう']):
        return 't '
    elif(k in ['た', 'ち', 'つ', 'て', 'と']):
        return 't'
    elif(k2 in ['だい', 'ぢい', 'づい', 'でい', 'どい']):
        return 'd '
    elif(k2 in ['だう', 'ぢう', 'づう', 'でう', 'どう']):
        return 'd '
    elif(k in ['だ', 'ぢ', 'づ', 'で', 'ど']):
        return 'd'
    elif(k2 in ['ない', 'にい', 'ぬい', 'ねい', 'のい']):
        return 'n '
    elif(k2 in ['なう', 'にう', 'ぬう', 'ねう', 'のう']):
        return 'n '
    elif(k in ['な', 'に', 'ぬ', 'ね', 'の']):
        return 'n'
    elif(k2 in ['はい', 'ひい', 'ふい', 'へい', 'ほい']):
        return 'h '
    elif(k2 in ['はう', 'ひう', 'ふう', 'へう', 'ほう']):
        return 'h '
    elif(k in ['は', 'ひ', 'ふ', 'へ', 'ほ']):
        return 'h'
    elif(k2 in ['ばい', 'びい', 'ぶい', 'べい', 'ぼい']):
        return 'b '
    elif(k2 in ['ばう', 'びう', 'ぶう', 'べう', 'ぼう']):
        return 'b '
    elif(k in ['ば', 'び', 'ぶ', 'べ', 'ぼ']):
        return 'b'
    elif(k2 in ['ぱい', 'ぴい', 'ぷい', 'ぺい', 'ぽい']):
        return 'p '
    elif(k2 in ['ぱう', 'ぴう', 'ぷう', 'ぺう', 'ぽう']):
        return 'p '
    elif(k in ['ぱ', 'ぴ', 'ぷ', 'ぺ', 'ぽ']):
        return 'p'
    elif(k2 in ['まい', 'みい', 'むい', 'めい', 'もい']):
        return 'm '
    elif(k2 in ['まう', 'みう', 'むう', 'めう', 'もう']):
        return 'm '
    elif(k in ['ま', 'み', 'む', 'め', 'も']):
        return 'm'
    elif(k2 in ['やう', 'ゆう', 'よう']):
        return 'y '
    elif(k in ['や', 'ゆ', 'よ']):
        return 'y'
    elif(k2 in ['らい', 'りい', 'るい', 'れい', 'ろい']):
        return 'r '
    elif(k2 in ['らう', 'りう', 'るう', 'れう', 'ろう']):
        return 'r '
    elif(k in ['ら', 'り', 'る', 'れ', 'ろ']):
        return 'r'
    elif(k in ['わ', 'を']):
        return 'w'
    # elif(k in ['ん']):
    #     return 'n'
    elif(k in ['.', '。']):
        return '.'
    elif(k in [',', '、']):
        return ','
    # elif(k in ['-', 'ー']):
    #     return '-'
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
print(' '.join(words))
print(' '.join(kanas))
print(' '.join(kwsks))
print(''.join(kwsks))
