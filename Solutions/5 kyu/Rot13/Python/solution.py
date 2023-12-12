def rot13(message):
    ROT13_Dict = {'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z'}
    rot13_dict = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z'}
    Reverse_Dict = {'N':'A','O':'B','P':'C','Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
    reverse_dict = {'n':'a','o':'b','p':'c','q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m'}
    result = ''
    for let in message:
        if let.isalpha():
            if let in ROT13_Dict:
                result += ROT13_Dict[let]
            if let in rot13_dict:
                result += rot13_dict[let]
            if let in Reverse_Dict:
                result += Reverse_Dict[let]
            if let in reverse_dict:
                result += reverse_dict[let]
        else:
            result += let
    return result
    