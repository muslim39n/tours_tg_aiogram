
def tour_messages(data):
    page, all_pages, tours = data['page'], data['all_pages'], data['data']

    msg_txt = f"Страница {page}/{all_pages}\n\n"
    
    for tour in tours:
        msg_txt += f"<b>{tour['title']}</b>\nСтоимость: {tour['price']} KZT\nТурагенство: {tour['travel_agency']}\nПодробнее: /tour_{tour['id']} \n\n"

    return msg_txt