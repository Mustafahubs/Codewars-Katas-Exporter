def hello(name=''):
    if name == '':
        return "Hello, World!"
    else:
        Captial_name = name.title()
        return f"{'Hello'}, {Captial_name}!"