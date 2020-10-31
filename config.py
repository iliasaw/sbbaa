import json

# Getting the token from json file


instar_info = """Hello. В этом уно может участвовать максимум 8 человек.
Бот создаёт сначало комнаты и роли, а также добовляет эмодзи на сервер. Выбор карты в боте необычный к примеру чтобы выбрать карту: **красная 6**, то надо написать: `r 6`.
Если вы незнаете правила то зайдите на этот сайт: https://igorek.info/kartochnaya-igra-uno-pravila-igryi-v-uno/""".expandtabs(2)

# Uno Config
category_name = "UNO | Игра"

seat_amount = 8
channel_names = [f"uno-комната-{numb}" for numb in range(1, seat_amount + 1)]
role_names = [f"{numb} | UNO Права к комнате" for numb in range(1, seat_amount + 1)]

# Function

def format_time(seconds):
    out = ""

    m, s = divmod(int(seconds), 60)
    h, m = divmod(m, 60)

    if h > 0:
        out += f"{h}h"
    out += f"{m}m{s}s"

    return out
