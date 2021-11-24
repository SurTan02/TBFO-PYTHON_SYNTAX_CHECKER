
def MapOfCNF(filename):

    file = open(filename).read()
    rules = file.split('\n')

    CNFMap = {}
    for i in range (len(rules)-1):
        
        leftSide,RightSide = rules[i].split(' -> ')
        RightSide = RightSide.replace(" ","")
        RightSide = RightSide.split('|')
        for j in range (len(RightSide)):
            #Cek apakah sudah ada map yang memetakan leftside dan rightside(/more)
            #jika belum maka diassign
            
            if (CNFMap.get(RightSide[j]) == None):
                
                CNFMap.update({RightSide[j] : [leftSide]})
                
            else :
                CNFMap[RightSide[j]].append(leftSide)
                
   
    
    CNFMap["'IDENTIFIER'"].append('IDENTIFIER3')
    CNFMap["'IDENTIFIER'"].append('OBJ27')
    CNFMap["'IDENTIFIER'"].append('AR112')
    CNFMap["'IDENTIFIER'"].append('AR113')
    CNFMap["'STRING'"].append('STRING')
    return CNFMap


def CYK(sentence, CNFMap):
    
    cykTable = [[[] for j in range(i)] for i in range(len(sentence),0,-1)]
    
    # Inisialisasi baris pertama 
    for i in range(len(sentence)):
        
        terminal = "'" +sentence[i] +"'"
        
        if (sentence[i] in CNFMap):
            cykTable[0][i] = (CNFMap[sentence[i]])
        elif ( terminal in CNFMap):
            
            cykTable[0][i] = ( (CNFMap[terminal]))
   

    # Inisialisasi baris atas 
    for i in range(1,len(sentence)):
        for j in range(len(sentence)-i):
            for k in range(i):
                for p1 in cykTable[i-k-1][j]:
                    for p2 in cykTable[k][j+i-k]:
                        if (p1+p2 in CNFMap):
                            cykTable[i][j] +=CNFMap[p1+p2]
                            

    return(cykTable)


def printTable(table):
    for i in range(len(table)):
        for j in range(len(table)-i):
            print(table[i][j],end="")
        print("")

def cekValid(table):
    if (len(table) == 0):
        return True
    else:
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
    
