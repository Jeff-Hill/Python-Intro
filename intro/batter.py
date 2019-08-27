def make_cake_batter(ingredients):
    cake_batter = 0
    for value in ingredients.values():
        cake_batter += value

    return cake_batter