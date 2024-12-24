import requests

URL = 'https://api.pokemonbattle.ru'
TOKEN = 'b190b348ab32a0fe317581337a612e49'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "irina@mail.ru",
    "password": "Loveqa123"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Мёрфи",
    "photo_id": 154
}
body_change = {
    "pokemon_id": "168279",
    "name": "Mark",
    "photo_id": 163
}
body_pokeball = {
    "pokemon_id": "168279"
}
body_battle = {
    "attacking_pokemon": "168279",
    "defending_pokemon": "168260"
}


'''response = requests.post(url = f'{URL}/v2/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/v2/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.put(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

'''response_pokeball = requests.post(url = f'{URL}/v2/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)'''

'''response_battle = requests.post(url = f'{URL}/v2/battle', headers = HEADER, json = body_battle)
print(response_battle.text)'''

response_create = requests.post(url = f'{URL}/v2/pokemons', headers = HEADER, json = body_create)
print(response_create.text)