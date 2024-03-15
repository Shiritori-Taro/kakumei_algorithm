types = set([
"暴力","食べ物","地名","社会","動物","感情","植物","理科","遊び","人物","服飾","工作",
"芸術","人体","時間","機械","医療","物語","暴言","数学","天気","虫","宗教","スポーツ","ノーマル",""])

class Word:

    def __init__(self,list:list,my_dmg:int,ene_dmg:int):
        self.name = list[0]
        if(len(list) == 1):
            self.type1 = ""
            self.type2 = ""
        elif(len(list) == 2):
            if(list[1] in types):
                self.type1 = list[1]
            else:
                self.type1 = ""
            self.type2 = ""
        elif(len(list) == 3):
            if(list[1] in types):
                self.type1 = list[1]
            else:
                self.type1 = ""
            if(list[2] in types):
                self.type2 = list[2]
            else:
                self.type2 = ""
        self.my_max_damage = my_dmg
        self.ene_max_damage = ene_dmg

    def get_word(self):
        return self.name

    def get_type1(self):
        return self.type1
    
    def get_type2(self):
        return self.type2
    
    def get_my_dmg(self):
        return self.my_max_damage

    def get_ene_dmg(self):
        return self.ene_max_damage

    def is_notype(self):
        return self.type1 == "" and self.type2 == ""
    
    def is_simple(self):
        return self.type1 != "" and self.type2 == ""

    def is_multi(self):
        return self.type1 != "" and self.type2 != ""
    
    def include(self,type):
        if(type == ""):
            return self.type1 == type
        if(type != ""):
            return self.type1 == type or self.type2 == type

    def Oremoji_ikaseru(self):
        return len(self.name) >= 7