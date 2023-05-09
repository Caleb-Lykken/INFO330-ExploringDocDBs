# Caleb Lykken INFO 330
# 4/26/2021
# This program imports the pokemon data from the sqlite3 database into the mongoDB database

from pymongo import MongoClient
import sqlite3

# Create a connection to the MongoDB database
mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

#create a connection to the sqlite3 database
conn = sqlite3.connect('pokemon.sqlite')
cursor = conn.cursor()

# Create a select statment to get the pokemon column into a varible
cursor.execute("SELECT id, name, pokedex_number, hp, attack, defense, speed, sp_attack, sp_defense FROM pokemon")
pokemon = cursor.fetchall()

# Create a select statment to get all of the pokemon types
cursor.execute("select pokemon.name as pokemon_name, ability.name as ability_name from pokemon join pokemon_abilities on pokemon_id = pokedex_number join ability on ability_id = ability.id")
Abilites = cursor.fetchall()

# Create a select statement to get all of the pokemon types
cursor.execute("select name, type1, type2  from pokemon_types_view")
Types = cursor.fetchall()
# close the connection to the sqlite3 database
conn.close()

# Create a function to print types in format "type1", "type2"
def print_types(name, types):
    print_type = []
    for type in types:
        if(name == type[0]):
            print_type.append(type[1])
            if(type[2] != ""):
                print_type.append(type[2])
    return (print_type)

# Create a function to print abilities in format "ability1", "ability2"
def print_abilities(name, abilities):
    abilities_print = []
    for ability in abilities:
        if(name == ability[0]):
            
            abilities_print.append(ability[1])
    return (abilities_print)


# define a function to convert a list to string
def listToString(s):
    return (','.join(map(str, s)))

#import the pokemon data into mongoDB
for poke in pokemon:
    pokemonColl.insert_one({
        "id": poke[0],
        "name": poke[1],
        "pokedex_number": poke[2],
        "types": print_types(poke[1], Types),
        "hp": poke[3],
        "attack": poke[4],
        "defense": poke[5],
        "speed": poke[6],
        "sp_attack": poke[7],
        "sp_defense": poke[8],
        "abilities": print_abilities(poke[1], Abilites)
    })

