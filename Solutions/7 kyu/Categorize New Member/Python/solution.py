def open_or_senior(member_list):
    category_list = []
    for member in member_list:
        if member[0] >= 55 and member[1] > 7:
            category_list.append("Senior")
        else:
            category_list.append("Open")
    return category_list
