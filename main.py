import cyk
import lexer
import token_expressions

# mungkin langsung pake cnf.txt
# atau pnaggil cfg2cnf(grammar.txt)
fileGrammar = "grammar.txt"
fileUji = str(input("Ketikkan nama File Uji: "))
text = open(fileUji).read()

lx = lexer.Lexer(token_expressions.tex, skip_whitespace=True)
lx.input(text)
array =[]

for tokens in lx.tokens():
    print(tokens.type)
    array.append(tokens.type)



if ("S" in cyk.CYK(array,cyk.MapOfCNF(fileGrammar))[-1][-1]):
    print("Terkonfirmasi Benar")
else:
    print("Salah")