def recommend_crop(temp, humidity):

    if 25 <= temp <= 35 and humidity >= 60:
        return "🌾 Rice"

    elif 20 <= temp <= 30:
        return "🌽 Wheat"

    elif temp > 30:
        return "🌽 Maize"

    else:
        return "🥬 Vegetables"