def roll_call_dwarves(list_of_dwarves_names):
    counter = 1
    for dwarf in list_of_dwarves_names:
        print(f"{counter}. {dwarf}")
        counter += 1


def summon_captain_planet(planeteer_calls):
    return [f"{element.title()}!" for element in planeteer_calls]


def long_planeteer_calls(words):
    x = False
    for word in words:
        if len(word) > 4:
            x = True
        else:
            pass
    return x


def find_the_cheese(list_of_strings):
    cheeses = ["cheddar", "gouda", "camembert"]
    for string in list_of_strings:
        if string in cheeses:
            return string
