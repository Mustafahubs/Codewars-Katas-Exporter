def friend(name):
    Friends = []
    for n in name:
        if len(n) == 4:
            Friends.append(n)
    return Friends
