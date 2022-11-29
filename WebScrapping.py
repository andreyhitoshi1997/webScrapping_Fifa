import requests
from time import sleep
from datetime import datetime

def get_match_data(date, firstCountry, secondCountry):
    return requests.get(
        url = f'https://temporeal.lance.com.br/storage/matches/copa-do-mundo-2022-{date}-{firstCountry}x{secondCountry}.json'
    ).json()

last_update = None

date = input('Entre com uma data valida DD-MM-YYYY: ')
firstCountry = input("Primeiro Pais: ")
secondCountry = input("Segundo Pais: ")

while True:
    match_data = get_match_data(date, firstCountry, secondCountry)
    narrations = match_data['match']['narrations']
    last_narration = narrations[len(narrations)-1]
    last_narration_time = datetime.strptime(last_narration['created_at'], "%Y-%m-%dT%H:%M:%S.000000Z")

    if(not last_update) or (last_narration_time > last_update):
        last_update = last_narration_time
        last_narration_moment = narrations[len(narrations)-1]['moment']
        last_narration_text = narrations[len(narrations)-1]['text']
        print(f'.\n.\n {last_narration_moment}" - {last_narration_text}')
    sleep(3)