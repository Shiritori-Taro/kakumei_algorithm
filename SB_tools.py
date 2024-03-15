import csv

#タイプ相性表
type_table = [
        #0: Normal, 1: Effective, 2: Not Effective, 3: No Damage
        [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1, 1, 3, 3, 2, 1, 1, 1 ,0], # Violence
        [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ,3], # Food
        [ 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], # Place
        [ 1, 0, 0, 2, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0 ,0], # Society
        [ 2, 1, 0, 0, 2, 0, 1, 2, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ,0], # Animal
        [ 2, 0, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 3, 0, 0, 2, 2, 0, 0, 2, 0, 0 ,0], # Emotion
        [ 0, 1, 1, 0, 2, 0, 2, 0, 2, 0, 2, 2, 0, 1, 1, 2, 0, 0, 0, 0, 0, 2, 0, 0, 0 ,0], # Plant
        [ 0, 0, 0, 0, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0 ,0], # Science
        [ 2, 2, 0, 0, 0, 0, 1, 0, 2, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0 ,0], # Playing
        [ 2, 0, 0, 2, 2, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0 ,0], # Person
        [ 2, 0, 0, 0, 0, 0, 1, 0, 2, 0, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], # Clothing
        [ 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], # Work
        [ 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0 ,0], # Art
        [ 2, 1, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], # Body
        [ 0, 1, 0, 0, 0, 0, 2, 0, 2, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], # Time
        [ 2, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0], # Machine
        [ 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 ,3], # Health
        [ 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 0, 0 ,0], # Tale
        [ 2, 2, 0, 1, 2, 1, 2, 0, 1, 1, 1, 0, 1, 1, 0, 2, 0, 0, 1, 1, 3, 2, 2, 1, 0 ,0], # Insult
        [ 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0 ,0], # Math
        [ 1, 1, 1, 1, 0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 0, 2, 2, 0, 1, 0 ,0], # Weather
        [ 1, 1, 0, 0, 1, 0, 1, 2, 0, 0, 2, 0, 0, 1, 0, 2, 1, 0, 1, 0, 0, 2, 0, 0, 0 ,0], # Bug
        [ 2, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 2, 0, 0 ,0], # Religion
        [ 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 2, 0 ,0], # Sports
        [ 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2 ,0], # Normal
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0]  # NoType        
]

#タイプ付き単語全て読み込み

typed_words = dict()
def load_typed_words():
    with open('dic/typed.csv', 'r', encoding='utf-8-sig') as typed_file:
            reader = csv.reader(typed_file)
            typed_words_not_processing = list(reader)
    for i in typed_words_not_processing:
        #1個目:言葉、2個目:タイプ1、3個目:タイプ2
        info = i[0].split(' ')
        if(info[0][0] not in typed_words):
            typed_words[info[0][0]] = [info]
        else:
            typed_words[info[0][0]].append(info)

#最大打点
def get_max_damage(word,my_atk_status,ene_def_status,ransuu=0.85,type1=None,type2=None,bouryoku=True):

    
    if(word == ""):return [-1,"",""]
    if(word == None):return [-1,"",""]

    max_damage = 0
    output_word = ""
    change_ability = ""
    kashiramoji = get_next_initial(word)
    dtype1 = ""
    dtype2 = ""   

    if(typed_words == dict()):load_typed_words()
    
    if(type1 == None and type2 == None):
        for i in typed_words[word[0]]:
            if(i[0] == word):
                dtype1 = i[1]
                if(len(i) == 3):
                    dtype2 = i[2]
                else:
                    dtype2 = ""
                break
    else:
        if(type1 in type_number):
            dtype1 = type1
        else:
            if(type1 != None):
                print("タイプ「"+str(type1)+"」は見つかりませんでした。")
            dtype1 = ""
        if(type2 in type_number):
            dtype2 = type2
        else:
            if(type2 != None):
                print("タイプ「"+str(type2)+"」は見つかりませんでした。")
            dtype2 = ""

    for i in typed_words[kashiramoji]:

        selected_word = i[0]       

        #if(selected_word in used_words):continue
        if(selected_word[0] != kashiramoji):continue
            
        atype1 = ""
        atype2 = ""
        status_effect = my_atk_status/ene_def_status

        atype1 = i[1]
        if(len(i) == 3):
            atype2 = i[2]
        else:
            atype2 = ""

        if(not bouryoku and (atype1 == "暴力" or atype2 == "暴力")):continue
        #急所すべきか
        kyuusyo_subeki = False

        if((atype1 == "人体" or atype2 == "人体")or
            (atype1 == "暴言" or atype2 == "暴言")):
            if(len(selected_word) >= 7 and status_effect < 0.75):
                kyuusyo_subeki = True
            if(len(selected_word) == 6 and status_effect < 1):
                kyuusyo_subeki = True
            if(len(selected_word) <= 5):
                kyuusyo_subeki = True


        if((atype1 == "人体" or atype2 == "人体") and kyuusyo_subeki):
            ability_effect = 1.5
            ability = "からて"
            if(status_effect < 1):status_effect = 1
        elif((atype1 == "暴言" or atype2 == "暴言" )and kyuusyo_subeki):
            ability_effect = 1.5
            ability = "ずぼし"
            if(status_effect < 1):status_effect = 1
        elif(len(selected_word) >= 7 and not kyuusyo_subeki):
            ability_effect = 2
            ability = "俺文字"
        elif(len(selected_word) == 6):
            ability_effect = 1.5
            ability = "俺文字"
        elif(atype1 == "理科" or atype2 == "理科"):
            ability_effect = 1.5
            ability = "じっけん"
        elif(atype1 == "地名" or atype2 == "地名"):
            ability_effect = 1.5
            ability = "グローバル"
        elif(atype1 == "人物" or atype2 == "人物"):
            ability_effect = 1.5
            ability = "きょじん"
        elif(atype1 == "宗教" or atype2 == "宗教"):
            ability_effect = 1.5
            ability = "しんこうしん"
        else:
            ability_effect = 1
            ability = ""

        if(dtype1 == ""):ransuu = 1


        damage = int(int(10 * type_effect(atype1,atype2,dtype1,dtype2) * status_effect * ransuu) * ability_effect)


        if(damage > max_damage):
            max_damage = damage
            output_word = selected_word
            change_ability = ability

    return [max_damage , output_word , change_ability]


#タイプの倍率を返す
def type_effect(attacktype1,attacktype2,defencetype1,defencetype2):

    a = type_table[type_to_num(attacktype1)][type_to_num(defencetype1)]
    b = type_table[type_to_num(attacktype1)][type_to_num(defencetype2)]
    c = type_table[type_to_num(attacktype2)][type_to_num(defencetype1)]
    d = type_table[type_to_num(attacktype2)][type_to_num(defencetype2)]

    kari = [a,b,c,d]

    ans = 1
    for i in kari:
        if(i == 0):{}
        if(i == 1):ans *= 2
        if(i == 2):ans *= 0.5
        if(i == 3):ans = 0

    return ans

#タイプ名を受け取りそれに対応する数字を返す
def type_to_num(input_string):
    if input_string in type_number:
        return type_number[input_string]
    else:
        return -1

#上2つとセットのタイプと数を結びつけた辞書
type_number = {
        "暴力":0     ,   "食べ物":1  ,   "地名":2    ,   "社会"  :3  ,   "動物":4    ,   "感情"    :5,
        "植物":6     ,   "理科"  :7  ,   "遊び":8    ,   "人物"  :9  ,   "服飾":10   ,   "工作"    :11,
        "芸術":12    ,   "人体"  :13 ,   "時間":14   ,   "機械"  :15 ,   "医療":16   ,   "物語"    :17,
        "暴言":18    ,   "数学"  :19 ,   "天気":20   ,   "虫"    :21 ,   "宗教":22   ,   "スポーツ":23,
        "ノーマル":24,   "":25
}


#頭文字を取得
def get_next_initial(word):
    if(word[-1] == "ゃ"):return 'や'
    if(word[-1] == "ゅ"):return 'ゆ'
    if(word[-1] == "ょ"):return 'よ'
    if(word[-1] == "ぁ"):return 'あ'
    if(word[-1] == "ぃ"):return 'い'
    if(word[-1] == "ぅ"):return 'う'
    if(word[-1] == "ぇ"):return 'え'
    if(word[-1] == "ぉ"):return 'お'
    if(word[-1] == "っ"):return 'つ'
    if(word[-1] == "ぢ"):return 'じ'
    if(word[-1] == "づ"):return 'ず'
    if(word[-1] == "を"):return 'お'
    if(word[-1] == "ー"):return get_next_initial(word[0:len(word) - 1])
    return word[-1]
