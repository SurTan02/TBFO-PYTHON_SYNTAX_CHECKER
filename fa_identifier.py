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
        
if __name__ == "__main__":
    if fa("_tring"):
        print('valid')
    else:
        print('not valid')