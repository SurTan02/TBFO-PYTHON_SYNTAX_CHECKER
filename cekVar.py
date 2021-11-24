arrOfOperator = ['PLUS','MINUS','POWER','MULTIPLY', 'EQUALS','DOUBLEEQUAL','NOT_EQUAL','GREATER_OR_EQUAL_THAN','GREATER_THAN','LESS_THAN','LESS_OR_EQUAL_THAN']

def variableValid (sentence):
    flag = True
    if (len(sentence) != 0):
        if 'EQUALS' in sentence:
            if (sentence[0] == 'NUMBER') or (sentence[0] in arrOfOperator):
                
                flag = False
        if (flag and  sentence[-1] in arrOfOperator):
            
            flag = False
        elif (flag and  sentence[0] in arrOfOperator):
            
            if (sentence[0] != "PLUS" and sentence[0]!= "MINUS"):
                
                flag = False
    return flag

