import cyk
import lexer
import token_expressions
import sys
import os
import cekVar
import CFGtoCNF


if len(sys.argv) > 1:
    fileUji = str(sys.argv[1])
else:
    fileUji = str(input("Ketikkan nama File yang ingin dicek: "))

while (not os.path.isfile(fileUji)):
        print("\033[91mFile Tidak ditemukan, ketikkan nama file yang sesuai!\033[0m")
        fileUji = str(input("Ketikkan nama File yang ingin dicek: "))

#Menghasilkan file CNF.txt dari grammar.txt
fileGrammar = "grammar.txt"
CFGtoCNF.convertGrammar(CFGtoCNF.readGrammar(fileGrammar))

#file CNF.txt
fileCNF = "CNF.txt"

text = open(fileUji).read()
lx = lexer.Lexer(token_expressions.tex, skip_whitespace=False)
lxForLine = lexer.Lexer(token_expressions.tex, skip_whitespace=False)

# lx = lexer.Lexer(rules_lexer.rules, skip_whitespace=False)
# lxForLine = lexer.Lexer(rules_lexer.rules, skip_whitespace=False)

lx.input(text)
lxForLine.input(text)



lenOfLine =1
#Hitung banyak baris
for tokens in lxForLine.tokens():
    # print(tokens)
    if (tokens == 'NEWLINE'):
        lenOfLine +=1
    elif (tokens == 'BREAK NEWLINE'):
        lenOfLine +=1

# print(lenOfLine)
#Buat Array buat nampung



line =[[] for i in range(lenOfLine)]
i = 0
for tokens in lx.tokens():
    if (tokens!=''):
        if (tokens == 'NEWLINE'):
            i+=1
        elif (tokens == 'BREAK NEWLINE'):
            line[i].append('BREAK')
            i+=1
        else:
            line[i].append(tokens)
            
                

# for i in range(lenOfLine):
    

#State
ErrorFound = False
if_count = 0
isMultiLine = False
indexLine = 0
multiLineIdx =0

while (ErrorFound == False and indexLine!=lenOfLine):
    if (line[indexLine].count('TRIPLEQUOTE') != 0):
        if (isMultiLine):
            isMultiLine = False
            multiLineIdx = indexLine
        else:
            isMultiLine = True
            multiLineIdx = indexLine
    else :
        
        if (line[indexLine] == ' ' or line[indexLine] == ''):
                print("",end='')
        elif (not isMultiLine):
            
            if (not cekVar.variableValid(line[indexLine])):
                
                print("Syntax Error!")
                print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine+1))
                ErrorFound =True
            elif (line[indexLine].count(' IF') != 0) :
                
                temp = line[indexLine].copy()
                line[indexLine].clear()
                for x in temp:
                    y = x.replace(' IF', 'IF')
                    line[indexLine].append(y)
                if_count += 1
                
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileCNF)))):
                    
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine+1))
                    ErrorFound =True
            elif line[indexLine].count('BREAK') != 0 :

                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileCNF)))):
                    
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine+1))
                    ErrorFound =True
                   
            elif line[indexLine].count('ELIF') != 0:
                if if_count > 0 :
                    line[indexLine].insert(0,'ELIFTOK')
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileCNF)))):
                    
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine+1))
                    ErrorFound =True

            elif line[indexLine].count('ELSE') != 0 :
                if if_count > 0 :
                    line[indexLine].insert(0,'ELIFTOK')
                if_count -= 1
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileCNF)))):
                    
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine+1))
                    ErrorFound =True

            else :
                
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileCNF)))):
                    
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine+1))
                    ErrorFound =True  
    indexLine += 1


if (not ErrorFound and isMultiLine):
    
    indexLine = multiLineIdx +1
    print("Syntax Error!")
    print("Terdapat kesalahan syntax pada line \033[91m{}\033[0m".format(indexLine))
    ErrorFound =True

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
if (not ErrorFound) :
    print('\033[96m'+ "Accepted!" + '\033[0m')
    print("Tidak ditemukan kesalahan syntax pada file")
else:
    text = text.split('\n')
    for i in range(len(text)):
        if (i == indexLine-1):
            print('\033[91m' + text[i] + '\033[0m')
        else:
            print(text[i])

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
