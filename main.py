from typing import Counter, Tuple
import cyk
import lexer
import token_expressions
import rules_lexer

#CNF Sudah diconvert sebelum program ini dijalankan
fileGrammar = "CNF.txt"
fileUji = str(input("Ketikkan nama File Uji: "))
text = open(fileUji).read()

#Ntar nando hapus ini
# lx = lexer.Lexer(token_expressions.tex, skip_whitespace=False)
# lxForLine = lexer.Lexer(token_expressions.tex, skip_whitespace=False)
lx = lexer.Lexer(rules_lexer.rules, skip_whitespace=False)
lxForLine = lexer.Lexer(rules_lexer.rules, skip_whitespace=False)
lx.input(text)
lxForLine.input(text)


lenOfLine =1
#Hitung banyak baris
for tokens in lxForLine.tokens():
    if (tokens == 'NEWLINE'):
        lenOfLine +=1


#Buat Array buat nampung
line =[[] for i in range(lenOfLine)]
i = 0
for tokens in lx.tokens():
    if (tokens!=''):
        if (tokens == 'NEWLINE'):
            i+=1
            
        else:
            line[i].append(tokens)



#State
ErrorFound = False
if_toggle = 0
isMultiLine = False
indexLine = 0

while (ErrorFound == False and indexLine!=lenOfLine):
    if (line[indexLine].count('TRIPLEQUOTE') != 0):
        if (isMultiLine):
            isMultiLine = False       
        else:
            isMultiLine = True   
    else :
        
        if (line[indexLine] == ' ' or line[indexLine] == ''):
                print("",end='')
        elif (not isMultiLine):
            if (line[indexLine].count(' IF') != 0) :

                temp = line[indexLine].copy()
                line[indexLine].clear()
                for x in temp:
                    y = x.replace(' IF', 'IF')
                    line[indexLine].append(y)
                if_toggle += 1
                
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileGrammar)))):
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line {}.".format(indexLine+1))
                  
                    ErrorFound =True
                   
            elif line[indexLine].count('ELIF') != 0:
                if if_toggle > 0 :
                    line[indexLine].insert(0,'ELIFTOK')
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileGrammar)))):
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line {}.".format(indexLine+1))
                    
                    ErrorFound =True
            elif line[indexLine].count('ELSE') != 0 :
                if if_toggle > 0 :
                    line[indexLine].insert(0,'ELIFTOK')
                if_toggle -= 1
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileGrammar)))):
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line {}.".format(indexLine+1))
                    ErrorFound =True
            else :
                if (not cyk.cekValid(cyk.CYK(line[indexLine],cyk.MapOfCNF(fileGrammar)))):
                    print("Syntax Error!")
                    print("Terdapat kesalahan syntax pada line {}.".format(indexLine+1))
                   
                    ErrorFound =True
    indexLine += 1
    
if (not ErrorFound) :
    print("Accepted!\nTidak ditemukan kesalahan syntax pada file")

    
