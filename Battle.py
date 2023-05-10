import random
from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

def fetch(pokemonid):
    return pokemonColl.find_one({"pokedex_number":pokemonid})

def battle(pokemon1, pokemon2):
    print("Let the Pokemon battle begin! ================")
    print("It's " + pokemon1['name'] + " vs " + pokemon2['name'])
    pokemon1stats = 0
    pokemon2stats = 0
    for stat in ['hp', 'attack', 'defense', 'speed', 'sp_attack', 'sp_defense']:
        
        if pokemon1[stat] > pokemon2[stat]:
            print(pokemon1['name'] + " has the advantage in " + stat)
            pokemon1stats += 1
        elif pokemon2[stat] > pokemon1[stat]:
            print(pokemon2['name'] + "'s " + stat + " is superior")
            pokemon2stats += 1
    # old winning conditions
    ##winner = random.randrange(2)
    ##if winner == 0: print("Battle results: " + pokemon1['name'])
    ##if winner == 1: print("Battle results: " + pokemon2['name'])

    # new winning conditions
    # counts up the number of stats each pokemon won
    # the winner is the pokemon with the most stats
    if pokemon1stats > pokemon2stats:
        print("Battle results: " + pokemon1['name'])
    elif pokemon2stats > pokemon1stats:
        print("Battle results: " + pokemon2['name'])
    else:
        print("Battle results: It's a tie!")

def main():
    # Fetch two pokemon from the MongoDB database
    pokemon1 = fetch(random.randrange(801))
    pokemon2 = fetch(random.randrange(801))

    # Pit them against one another
    battle(pokemon1, pokemon2)

main()
