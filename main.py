from typing import Counter, Tuple
import cyk
import lexer
import token_expressions
import CFGtoCNF
import datetime as time

# mungkin langsung pake cnf.txt
# atau pnaggil cfg2cnf(grammar.txt)
# fileGrammar = "grammar.txt"
fileGrammar = "CNF3.txt"
fileUji = str(input("Ketikkan nama File Uji: "))
text = open(fileUji).read()

lx = lexer.Lexer(token_expressions.tex, skip_whitespace=False)
lxForLine = lexer.Lexer(token_expressions.tex, skip_whitespace=False)
# lx = lexer.Lexer(rules_lexer.rules, skip_whitespace=False)
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


# for i in range(lenOfLine):
#     print(line[i])

#State
ErrorFound = False
if_toggle = 0
multiline_toggle = False
start_time = time.datetime.now()
total_success = 0
total_error = 0
line_counter = 0

while (ErrorFound == False and line_counter!=lenOfLine):
    # print(line[line_counter])
    # if ("S" in cyk.CYK(line[line_counter],cyk.MapOfCNF(fileGrammar))[-1][-1]):
    #     print("Terkonfirmasi Benar")
    # else:
    #     cyk.printTable(cyk.CYK(line[line_counter],cyk.MapOfCNF(fileGrammar))[-1])
    #     print("======================================")
    # print((line[line_counter].count('TRIPLEQUOTE')))
    if (line[line_counter].count('TRIPLEQUOTE') != 0) and multiline_toggle == False :
        multiline_toggle = True
        total_success += 1                
    elif (line[line_counter].count('TRIPLEQUOTE') != 0) and multiline_toggle == True :
            multiline_toggle = False
            total_success += 1
    else :
        
        if (line[line_counter] == ' ' or line[line_counter] == ''):
                print("",end='')
                total_success += 1
        elif multiline_toggle == False :
            if (line[line_counter].count('IF') != 0) :
                # print(line[line_counter])
                if_toggle += 1
                
                if (cyk.cekValid(cyk.CYK(line[line_counter],cyk.MapOfCNF(fileGrammar)))):
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter+1))
                    total_error += 1
                    ErrorFound =True
                   
            elif line[line_counter].count('ELIF') != 0:
                if if_toggle > 0 :
                    line[line_counter].insert(0,'ELIFTOK')
                if (cyk.cekValid(cyk.CYK(line[line_counter],cyk.MapOfCNF(fileGrammar)))):
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter+1))
                    total_error += 1
                    ErrorFound =True
            elif line[line_counter].count('ELSE') != 0 :
                if if_toggle > 0 :
                    line[line_counter].insert(0,'ELIFTOK')
                if_toggle -= 1
                if (cyk.cekValid(cyk.CYK(line[line_counter],cyk.MapOfCNF(fileGrammar)))):
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter+1))
                    total_error += 1
                    ErrorFound =True
            else :
                
                if (cyk.cekValid(cyk.CYK(line[line_counter],cyk.MapOfCNF(fileGrammar))) ==True):
                    total_success += 1
                else :
                    print("Error at line {}.".format(line_counter+1))
                    total_error += 1
                    ErrorFound =True
    line_counter += 1
    
if (total_error == 0) :
    print("ACCEPTED")

# for i in range(lenOfLine):
#     # cyk.printTable (cyk.CYK(line[i],cyk.MapOfCNF(fileGrammar)))
#     # print("=======")
#     # print("=======")
#     if ("S" in cyk.CYK(line[i],cyk.MapOfCNF(fileGrammar))[-1][-1]):
#         print("Terkonfirmasi Benar")
#     else:
#         print("Salah")
