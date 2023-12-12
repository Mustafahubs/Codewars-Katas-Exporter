def number(bus_stops):
    LastBusStop_pass = 0
    First_Passengers = 0
    Second_Passengers = 0
    for firstN in bus_stops:
        FirstEle = firstN[0]
        First_Passengers += FirstEle
    for secondN in bus_stops:
        SecondEle = secondN[1]
        Second_Passengers += SecondEle
    LastBusStop_pass = First_Passengers - Second_Passengers
    return LastBusStop_pass