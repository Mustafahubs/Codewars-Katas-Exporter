def accum(given_string):
    store = ''
    New_string = given_string.lower()
    for ind,let in enumerate(New_string):
        upperLet = let.upper()
        store += upperLet
        multiply = let*ind
        store+=multiply
        store+='-'
    result = store[:-1]
    return result