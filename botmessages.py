
START_MESSAGE = '''
Привет!
Это чат-бот для поиска \U0001F525 горящих туров с Алматы.

Ниже можешь выбрать страну, и найти подходящие для тебя туры. 
'''

CHOOSE_COUNTRY_MESSAGE = '''
Ниже можешь выбрать страну, и найти подходящие для тебя туры. 
'''

def tour_list(data):
    page, all_pages, tours = data['page'], data['all_pages'], data['data']

    msg_txt = f"Страница {page}/{all_pages}\n\n"
    
    for tour in tours:
        msg_txt += f"<b>{tour['title']}</b>\nСтоимость: {tour['price']} KZT\nТурагенство: {tour['travel_agency']}\nПодробнее: /tour_{tour['id']} \n\n"

    return msg_txt

def tour_detail(tour):
    red_exclamation_mark = '\U00002757'
    msg_txt = f"{red_exclamation_mark} {tour['country']['name_ru']}\n"
    msg_txt += f'<b>{tour["title"]}</b>\n\n'
    

    if tour['description'] is not None and tour['description'] != '':
        msg_txt += tour['description'] + '\n\n'

    msg_txt += 'Откуда: ' + tour['from_city']['name_ru'] + '\n'
    msg_txt += 'Цена: ' + str(tour['price']) + '\n' 
    msg_txt += f"{tour['date'][8:]}.{tour['date'][6:8]}, на {tour['days']} дней\n\n"

    for service in tour['services']:
        msg_txt += '\U0001F538 ' + service['name'] + '\n'

    msg_txt += '\nКонтакты: \n'
    msg_txt += '\U0001F4DE ' + tour['phone_number'] + '\n'
    
    if 'phone_number_2' in tour and tour['phone_number_2'] is not None and tour['phone_number_2'] != '':
        msg_txt += '\U0001F4DE ' + tour['phone_number_2'] + '\n'

    
    if 'telegram' in tour and tour['telegram'] is not None and tour['telegram'] != '':
        msg_txt += '\U0001F4F1 ' + tour['telegram'] + '\n'
  
    if 'telegram' in tour and tour['telegram'] is not None and tour['telegram'] != '':
        msg_txt += '\U0001F4F1 ' + tour['telegram'] + '\n'

    if 'travel_agency' in tour and tour['travel_agency'] is not None and tour['travel_agency'] != '':
        msg_txt += 'Турагент:  ' + tour['travel_agency'] + '\n'
  
    return msg_txt

