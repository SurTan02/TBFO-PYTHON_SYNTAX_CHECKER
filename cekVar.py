import string

def fa(check):
    first_el = list(string.ascii_letters)
    first_el.append('_')
    if check[0] not in first_el:
        return False
    for n in range(10):
        first_el.append(n)
    for i in range(1, len(check)):
        if (check[i] not in first_el):
            return False
    return True

arrOfOperator = ['PLUS','MINUS','POWER','MULTIPLY', 'ASSIGNS','EQUALS','NOT_EQUAL','GREATER_OR_EQUAL_THAN','GREATER_THAN','LESS_THAN','LESS_OR_EQUAL_THAN']

def variableValid (sentence):
    flag = True
    if (len(sentence) != 0):
        if 'ASSIGNS' in sentence:
            if (sentence[0] == 'NUMBER') or (sentence[0] in arrOfOperator):
                flag = not(fa(sentence[0]))
            elif (sentence[0] == 'IDENTIFIER' and sentence[1] != 'ASSIGNS'):
                flag = not(fa(sentence[0]))
        if (flag and  sentence[-1] in arrOfOperator):
            
            flag = not(fa(sentence[0]))
        elif (flag and  sentence[0] in arrOfOperator):
            
            if (sentence[0] != "PLUS" and sentence[0]!= "MINUS"):
                
                flag = not(fa(sentence[0]))
    return flag

if __name__ == "__main__":
    if fa("_tring"):
        print('valid')
    else:
        print('not valid')
