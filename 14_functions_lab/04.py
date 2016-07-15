_author_ = 'mariag'

def longer_than(length ,*args):
    if type(length) != int:
            raise Exception ("longer_than expects first parameter integer")        
    list_res = []
    for word in args:
        if type(word) != str:
            raise Exception ("longer_than expects (int, [str])")
        if len(word)>length:
            list_res.append(word)
    return list_res

print longer_than(3,"she","loves","you","yeee","ye","yeee")