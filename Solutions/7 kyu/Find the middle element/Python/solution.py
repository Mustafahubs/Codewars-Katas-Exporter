def gimme(input_array):
    sorted_array = sorted(input_array) 
    middle_number = sorted_array[1]  
    index = input_array.index(middle_number)
    return index
