def MapOfCNF(filename):

    file = open(filename).read()
    rules = file.split('\n')

    chomskyGrammar = {}
    for i in range (len(rules)-1):
        leftSide = rules[i].split(' -> ')[0]
        RightSide = (rules[i].split(' -> ')[1])
        MoreRightSide = RightSide.replace(" ","")
        # MoreRightSide = RightSide.split('|')
        
        for j in range (len(MoreRightSide)):
            #Cek apakah sudah ada map yang memetakan leftside dan rightside(/more)
            #jika belum maka diassign
            if (chomskyGrammar.get(MoreRightSide[j]) == None):
                chomskyGrammar.update({MoreRightSide[j] : [leftSide]})
            else : 
                chomskyGrammar[MoreRightSide[j]].append(leftSide)
    return chomskyGrammar

def listOfLexered(filename):
# Fungsi ini mengembalikan list yang berisi kata dari input file yg telah diproses lexer

    file = open(filename).read()
    member = file.split('\n')
    
    arrayOfLexered=["" for i in range (len(member))]
    for i in range(len(member)):
        arrayOfLexered[i] = member[i].split('(')[0]
    
    return arrayOfLexered

def CYK(sentence, chomskyGrammar):
    
    cykTable = [[[] for j in range(i)] for i in range(len(sentence),0,-1)]

    # Inisialisasi baris pertama 
    for i in range(len(sentence)):
        if (sentence[i] in chomskyGrammar):
            cykTable[0][i] = (chomskyGrammar[sentence[i]])
            

    # Inisialisasi baris atas 
    for i in range(1,len(sentence)):
        for j in range(len(sentence)-i):
            for k in range(i):
                for P1 in cykTable[i-k-1][j]:
                    for P2 in cykTable[k][j+i-k]:
                        if (P1+P2 in chomskyGrammar):
                            cykTable[i][j]=chomskyGrammar[P1+P2]
                            

    return(cykTable)


def printTable(table):
    for i in range(len(table)):
        for j in range(len(table)-i):
            print(table[i][j],end="")
        print("")


if __name__ == '__main__':

    sentence = 'aaabbbcc'
    MapOfCNF("tes_g.txt")
    if ("S" in CYK(sentence,MapOfCNF("tes_g.txt"))[-1][-1]):
        print("udah benar")
    else:
        print("salah")
    
