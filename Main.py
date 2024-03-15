import SB_tools
from Word import Word
from get_dic import get_dict
import copy

play_words = dict()

def player1_turn(word:Word,chain=[],max_len=100,kaiki=1,HP=[60,60]):
    global print_progress
    chain = copy.deepcopy(chain)
    chain.append(word.get_word())

    #途中経過(デバッグ用)
    if(print_progress):
        with open("test.txt","a+",encoding="utf-8") as f:
            print(max_len,chain,HP,file=f)
    

    #「ざ」など続く単語がなかったら終了
    if(SB_tools.get_next_initial(chain[-1]) not in play_words):return chain
    
    #勝てる時用の最短チェインを保存
    best_chain = chain
    #負ける時用の最大チェインを保存
    longest_chain = chain
    player1_HP_now_org,player2_HP_now_org = HP

    #例えば「ういいれ」で最大長さ4って分かった後に「うーむ」で5以上探すの無駄だよねっていうやつ
    max = max_len
    for new in play_words[SB_tools.get_next_initial(chain[-1])]:
        player1_HP_now,player2_HP_now = player1_HP_now_org,player2_HP_now_org

        #今まで見つかった最短よりも長くなったら無視でok
        if(len(best_chain) > max):break
        #「～ど→どらいぶ」みたいに1手で詰みとれたら最短確定だよね
        if(len(best_chain) - len(chain) == 1):break
        #今までに使用してたら飛ばす(禁止単語設定)
        if(new.get_word() in used_words):continue
        #単語が使用済みなら飛ばす
        if(new.get_word() in chain):continue
        #HP足りなくても飛ばす
        if(player1_HP_now <= new.get_ene_dmg()):continue
        
        #タイプありorなしで乱数設定
        if(word.get_type1() == "" and word.get_type2() == ""):
            ransuu = 1
        else:
            ransuu = my_ransuu

        #ダメージ計算
        player2_HP_now = player2_HP_now_org - int(10 * SB_tools.type_effect(new.get_type1(),new.get_type2(),word.get_type1(),word.get_type2()) * status_effect_me * ransuu)

        #回帰
        new_chain = player2_turn(new,chain=chain,max_len=max,kaiki=kaiki+1,HP=[player1_HP_now,player2_HP_now])

        #勝てるとき
        if(len(new_chain)%2 == 0):
            #初期値のとき更新
            if(best_chain == chain):
                best_chain = new_chain
                if(max > len(best_chain)):max = len(best_chain)
            #1回以上更新されたとき
            else:
                #以前のチェインよりも短く詰ませられたら更新
                if(len(best_chain) > len(new_chain)):
                    best_chain = new_chain
                    if(max > len(best_chain)):max = len(best_chain)

        #負ける時用に最長のチェイン保持
        if(len(new_chain) > len(longest_chain)):
            longest_chain = new_chain

    #1回も更新がなかったら(1回も勝てなかったら)最長を返す
    if(best_chain == chain):
        return longest_chain
    #勝てたらベストを返す
    else:
        return best_chain

def player2_turn(word:Word,chain=[],max_len=100,kaiki=0,HP=[60,60]):
    global print_progress
    chain = copy.deepcopy(chain)
    chain.append(word.get_word())
    
    if(print_progress):
        with open("test.txt","a+",encoding="utf-8") as f:
            print(max_len,chain,HP,file=f)
    

    if(SB_tools.get_next_initial(chain[-1]) not in play_words):return chain

    best_chain = chain
    player1_HP_now_org,player2_HP_now_org = HP
    longest_chain = chain
    max = max_len
    for new in play_words[SB_tools.get_next_initial(chain[-1])]:
        player1_HP_now,player2_HP_now = player1_HP_now_org,player2_HP_now_org
        if(len(best_chain) > max):break            
        if(len(best_chain) - len(chain) == 1):break
        if(new.get_word() in used_words):continue
        if(new.get_word() in chain):continue
        if(player2_HP_now <= new.get_my_dmg()):continue

        if(word.get_type1() == "" and word.get_type2() == ""):
            ransuu = 1
        else:
            ransuu = ene_ransuu

        player1_HP_now = player1_HP_now_org - int(10 * SB_tools.type_effect(new.get_type1(),new.get_type2(),word.get_type1(),word.get_type2()) * status_effect_ene * ransuu)

        new_chain = player1_turn(new,chain=chain,kaiki=kaiki+1,max_len=max,HP=[player1_HP_now,player2_HP_now])

        #勝てるとき
        if(len(new_chain)%2 == 1):
            if(best_chain == chain):
                best_chain = new_chain
                if(max > len(best_chain)):max = len(best_chain)
            else:
                if(len(best_chain) > len(new_chain)):
                    best_chain = new_chain
                    if(max > len(best_chain)):max = len(best_chain)
                    
        if(len(new_chain) > len(longest_chain)):
            longest_chain = new_chain

    if(best_chain == chain):
        return longest_chain
    else:
        return best_chain

if __name__ == "__main__":
    #ここで設定-----
    my_HP =53
    my_atk=0.5
    my_def=1
    my_ransuu=0.85
    ene_HP = 60
    ene_atk=1
    ene_def=1
    ene_ransuu=0.99
    first_word = "わ"
    type1 = "遊び"
    type2 = "虫"

    #test.txtに途中経過記述
    print_progress = 0
    #禁止ワード一覧設定
    used_words = []
    #---------------

    status_effect_me = my_atk/ene_def
    status_effect_ene = my_def/ene_atk

    play_words = get_dict(
                            my_atk=my_atk,
                            my_def=my_def,
                            my_ransuu=my_ransuu,
                            ene_atk=ene_atk,
                            ene_def=ene_def,
                            ene_ransuu=ene_ransuu
                            )

    result = player1_turn(Word([first_word,type1,type2],1,1),HP=[my_HP,ene_HP])
    print(len(result),result)