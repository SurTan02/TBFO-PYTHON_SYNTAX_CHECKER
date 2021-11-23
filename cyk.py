
def MapOfCNF(filename):

    file = open(filename).read()
    rules = file.split('\n')

    chomskyGrammar = {}
    for i in range (len(rules)-1):
        
        leftSide,RightSide = rules[i].split(' -> ')
        RightSide = RightSide.replace(" ","")
        RightSide = RightSide.split('|')
        # print(leftSide)
        for j in range (len(RightSide)):
            #Cek apakah sudah ada map yang memetakan leftside dan rightside(/more)
            #jika belum maka diassign
            
                
            if (chomskyGrammar.get(RightSide[j]) == None):
                
                chomskyGrammar.update({RightSide[j] : [leftSide]})
                
            else :
                chomskyGrammar[RightSide[j]].append(leftSide)
                # if RightSide[j] == "'NUMBER'":
                #     print(chomskyGrammar.get(RightSide[j]))
                #     print(RightSide[j])
                #     print("aaa",  chomskyGrammar[RightSide[j]])
                # if (chomskyGrammar.get(RightSide[j])[0] not in chomskyGrammar[RightSide[j]]):
                
    # print(chomskyGrammar["IDENTIFIER"])
    
    chomskyGrammar["'IDENTIFIER'"].append('IDENTIFIER3')
    chomskyGrammar["'IDENTIFIER'"].append('OBJ27')
    chomskyGrammar["'IDENTIFIER'"].append('AR112')
    chomskyGrammar["'IDENTIFIER'"].append('AR113')
    chomskyGrammar["'STRING'"].append('STRING')
    # chomskyGrammar["'INTEGER'"] = chomskyGrammar["'NUMBER'"]
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
        
        terminal = "'" +sentence[i] +"'"
        # print( (chomskyGrammar[terminal]))
        
        if (sentence[i] in chomskyGrammar):
            cykTable[0][i] = (chomskyGrammar[sentence[i]])
        elif ( terminal in chomskyGrammar):
            
            cykTable[0][i] = ( (chomskyGrammar[terminal]))
            # print(cykTable[0][i])
   

    # Inisialisasi baris atas 
    for i in range(1,len(sentence)):
        for j in range(len(sentence)-i):
            for k in range(i):
                for p1 in cykTable[i-k-1][j]:
                    for p2 in cykTable[k][j+i-k]:
                        
                        # if (i==1 and j==1 and p1+p2 in chomskyGrammar):
                        #     # p1 = "'" +p1 +"', "
                        #     # p2 = "'" +p2 +"'"
                        #     print("adala" , p1+p2)
                        #     print(chomskyGrammar[p1+p2])
                        if (p1+p2 in chomskyGrammar):
                            
                            
                            cykTable[i][j] +=chomskyGrammar[p1+p2]
                            

    return(cykTable)


def printTable(table):
    for i in range(len(table)):
        for j in range(len(table)-i):
            print(table[i][j],end="")
        print("")

def cekValid(table):
    if ("S" in table[-1][-1]):
        return True
    else:
        return False


if __name__ == '__main__':

    sentence = 'aaabbbcc'
    MapOfCNF("tes_g.txt")
    
    printTable( CYK(sentence,MapOfCNF("tes_g.txt")))
    if ("S" in CYK(sentence,MapOfCNF("tes_g.txt"))[-1][-1]):
        print("udah benar")
    else:
        print("salah")
    
