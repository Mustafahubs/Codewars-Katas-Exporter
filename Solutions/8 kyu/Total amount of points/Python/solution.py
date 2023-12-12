def points(match_results):
    total_points = 0
    for result in match_results:
        x, y = result.split(":")
        if int(x) > int(y):
            total_points += 3
        elif int(x) == int(y):
            total_points += 1
    return total_points
