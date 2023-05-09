from pymongo import MongoClient

mongoClient = MongoClient("mongodb://localhost/pokemon")
pokemonDB = mongoClient['pokemondb']
pokemonColl = pokemonDB['pokemon_data']

# Write a query that returns all the Pokemon named "Pikachu"
pikachu = pokemonColl.find({"name": "Pikachu"})

# Write a query that returns all the Pokemon with an attack greater than 150
attack = pokemonColl.find({"attack": {"$gt": 150}})

# Write a query that returns all the Pokemon with an ability of "Overgrow" 
overgrow = pokemonColl.find({"abilities": {"$in": ["Overgrow"]}})