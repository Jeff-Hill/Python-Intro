def bake_cake(batter, temperature, time):
    oven = {
        "type": "electric",
        "model": "GE",
        "volume": 17,
        "contents": None,
        "temp": 0
    }

    oven["contents"] = batter
    oven["temperature"] = temperature

    return f'Your cake was baked for {time} minutes at {temperature} degrees'