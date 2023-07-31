import requests

token = '53e6b3cb721ec006b71a55b6fe72bf75'


'''response = requests.post ('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token ,
    "email": "germdan@dolnikov.ru",
    "password": "Iloveqa1"
}, headers = {'Content-Type' : 'application/json'})

print (response.status_code)'''

'''response_act = requests.post ('https://api.pokemonbattle.me:9104/trainers/confirm_email', json = {
    "trainer_token": token ,
    "email": "germdan@dolnikov.ru",
    "password": "Iloveqa1"
}, headers = {'Content-Type' : 'application/json'})

print (response_act.status_code)'''

response_add_pokemon = requests.post ('https://api.pokemonbattle.me:9104/pokemons', json = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})

print (response_add_pokemon.text)

response_add_new_name = requests.put ('https://api.pokemonbattle.me:9104/pokemons', json = {
    "pokemon_id": "5757",
    "name": "NewName",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})

print (response_add_new_name.text)

response_catch = requests.post ('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {
    "pokemon_id": "5757"
}, headers = {'Content-Type' : 'application/json', 
              'trainer_token' : token})

print (response_catch.text)
