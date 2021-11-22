DICT_RULE = {}

def readGrammar(grammar_file="grammar.txt"):
    with open(grammar_file) as cfg:
        lines = cfg.readlines()
    return [x.replace("->", "").split() for x in lines]


def addRule(rule):

    global DICT_RULE

    if rule[0] not in DICT_RULE:
        DICT_RULE[rule[0]] = []
    DICT_RULE[rule[0]].append(rule[1:])


def convertGrammar(grammar):

    unit_productions, result = [], []
    res_append = result.append
    index = 0
    global DICT_RULE

    for rule in grammar:
        new_rules = []
        if len(rule) == 2 and rule[1][0] != "'":
            unit_productions.append(rule)
            addRule(rule)
            continue
        elif len(rule) > 2:
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    rule[item[1]] = f"{rule[0]}{str(index)}"
                    new_rules += [f"{rule[0]}{str(index)}", item[0]]
                index += 1
            while len(rule) > 3:
                new_rules.append([f"{rule[0]}{str(index)}", rule[1], rule[2]])
                rule = [rule[0]] + [f"{rule[0]}{str(index)}"] + rule[3:]
                index += 1
        addRule(rule)
        res_append(rule)
        if new_rules:
            result.extend(new_rules)
    while unit_productions:
        rule = unit_productions.pop()
        if rule[1] in DICT_RULE:
            for item in DICT_RULE[rule[1]]:
                new_rule = [rule[0]] + item
                if len(new_rule) > 2 or new_rule[1][0] == "'":
                    result.insert(0, new_rule)
                else:
                    unit_productions.append(new_rule)
                addRule(new_rule)
    return result