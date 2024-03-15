import SB_tools
import csv
from Word import Word

alphabet = [
        "あ","い","う","え","お",
        "か","き","く","け","こ",
        "さ","し","す","せ","そ",
        "た","ち","つ","て","と",
        "な","に","ぬ","ね","の",
        "は","ひ","ふ","へ","ほ",
        "ま","み","む","め","も",
        "や",     "ゆ",     "よ",
        "ら","り","る","れ","ろ",
        "わ","を",
        "が","ぎ","ぐ","げ","ご",
        "ざ","じ","ず","ぜ","ぞ",
        "だ",          "で","ど",
        "ば","び","ぶ","べ","ぼ",
        "ぱ","ぴ","ぷ","ぺ","ぽ"]
play_words = dict()
gotou_num = dict()
gobi_num = dict()

def load_dict(my_atk,my_def,my_ransuu,ene_atk,ene_def,ene_ransuu):
    with open('dic/play.txt', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if(len(row[0].split()) == 1):
                word = row[0]
                type1 = "遊び"
                type2 = ""
            elif(len(row[0].split()) == 2):
                word = row[0].split()[0]
                type1 = row[0].split()[1]
                type2 = ""
            elif(len(row[0].split()) == 3):
                word = row[0].split()[0]
                type1 = row[0].split()[1]
                type2 = row[0].split()[2]
            my_dmg = SB_tools.get_max_damage(word,my_atk,ene_def,my_ransuu,type1=type1,type2=type2)[0]
            ene_dmg = SB_tools.get_max_damage(word,my_def,ene_atk,ene_ransuu,type1=type1,type2=type2)[0]

            #前からのばしてこうね
            if(row[0].split()[0][0] not in play_words):
                play_words[row[0].split()[0][0]] = [Word(row[0].split(),my_dmg,ene_dmg)]
            else:
                play_words[row[0].split()[0][0]].append(Word(row[0].split(),my_dmg,ene_dmg))

    for i in play_words:
        for j in play_words[i]:
            gotou_num[SB_tools.get_next_initial(j.get_word())] = 0
            gotou_num[i] = 0
            gobi_num[SB_tools.get_next_initial(j.get_word())] = 0
            gobi_num[i] = 0
    for i in play_words:
        for j in play_words[i]:
            gotou_num[j.get_word()[0]] += 1
            gobi_num[SB_tools.get_next_initial(j.get_word())] += 1

def sort_dic():
    global gotou_num,gobi_num,play_words

    yuusendo = dict()
    for i in gotou_num:
        yuusendo[i] = 100

    sorted_gotou_num = dict(sorted(gotou_num.items(),key=lambda x:x[1]))
    sorted_gobi_num = dict(sorted(gobi_num.items(),key=lambda x:x[1]))

    for w in sorted_gotou_num:
        num = sorted_gotou_num[w]
        #「ざ」とか遊びタイプがないとき
        if(num == 0):
            #その語尾終わりの言葉があったら語頭の優先度を最強に
            if(sorted_gobi_num[w] >= 1):
                yuusendo[w] = 0
        else:
            break

    #最大打点の最小値を記録(「ぶ」の枠を抽出)
    syokiti = 1000
    min_damage_dict = dict()
    for i in alphabet:
        min_damage_dict[SB_tools.get_next_initial(i)] = syokiti
    for i in play_words:
        for j in play_words[i]:
            tmp = min(j.get_my_dmg(),j.get_ene_dmg())
            if(tmp < min_damage_dict[SB_tools.get_next_initial(j.get_word()[0])]):
                min_damage_dict[SB_tools.get_next_initial(j.get_word()[0])] = tmp
    min_damage_dict = dict(sorted(min_damage_dict.items(),key=lambda x:x[1],reverse=True))

    #最小ダメージが51くらいだったら優先度を次に最強に
    for i in min_damage_dict:
        if(min_damage_dict[i] != syokiti and min_damage_dict[i] >= 51):
            yuusendo[i] = 1

    #最後に(最大打点が51未満の(これでやったら順番微妙だったので素で))語頭の遊び単語の少なさで少なさで優先度付け(なんとなく強い気がするので)
    for i,alp in enumerate(sorted_gotou_num):
        if(yuusendo[alp] == 100):
            yuusendo[alp] = i + 2
    #print(dict(sorted(yuusendo.items(),key=lambda x:x[1])))
            
    #ソート実行
    for i in play_words:
        play_words[i] = sorted(play_words[i],key=lambda x:yuusendo[SB_tools.get_next_initial(x.get_word())])

def get_dict(my_atk,my_def,my_ransuu,ene_atk,ene_def,ene_ransuu):
    global play_words
    play_words = dict()
    load_dict(my_atk,my_def,my_ransuu,ene_atk,ene_def,ene_ransuu)
    sort_dic()
    return play_words

def get_type(name):
    for i in play_words[name[0]]:
        if(i.get_word() == name):
            return [i.get_type1(),i.get_type2()]
    return ["",""]

if(__name__ == "__main__"):
    dic = get_dict(0.5,1,0.85,1,1,0.99)
    for i in dic:
        for j in dic[i]:
            print(j.get_word(),end=",")
        print("\n")
