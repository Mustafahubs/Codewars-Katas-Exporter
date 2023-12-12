def rental_car_cost(days):
    daily_rate = 40
    if days >= 7:
        return days * daily_rate - 50
    elif days >= 3:
        return days * daily_rate - 20
    else:
        return days * daily_rate
