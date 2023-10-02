spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = [food["name"] for food in spicy_foods]
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = [food for food in spicy_foods if food["heat_level"] > 5]
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        emoji_heat_level = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_heat_level}")
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
        elif food is not None:
            print(f"Spicy Food from {cuisine}: {food['name']} | Heat Level: 🌶🌶🌶")
        else:
             print(f"No spicy food found for {cuisine}.")

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food["heat_level"] > 5:
            emoji_heat_level = "🌶" * food["heat_level"]
            print(f"{food['name']} ({food['cuisine']}) | Heat Level: {emoji_heat_level}")
print_spiciest_foods(spicy_foods)

def get_average_heat_level(spicy_foods):
    if not spicy_foods:
        return 0
    total_heat = sum(food["heat_level"] for food in spicy_foods)
    average = total_heat / len(spicy_foods)
    return int(average)

average = get_average_heat_level(spicy_foods)
print(f"Average Heat Level: {average}")

def create_spicy_food(spicy_foods, spicy_food):
    new_spicy_foods = spicy_foods.copy()
    new_spicy_foods.append(spicy_food)
    return new_spicy_foods
