import json
import random
import schedule
import time
from datetime import datetime

# Скины
skins = {
    29: (29, 0, 1),
    52: (149, 0, 1),
    159: (149, 0, 1),

    15: (29, 0, 1),
    79: (149, 0, 1),

    2: (29, 0, 1),
    103: (29, 0, 1),

    25: (79, 0, 1),
    64: (149, 0, 1),
    102: (79, 0, 1),

    44: (149, 0, 1),
    123: (149, 0, 1),
    163: (149, 0, 1),

    58: (79, 0, 1),
    91: (149, 0, 1),

    57: (149, 0, 1),
    97: (299, 0, 1),
    160: (149, 0, 1),

    94: (299, 0, 1),
    98: (79, 0, 1),
    99: (149, 0, 1),

    109: (29, 0, 1),

    167: (29, 0, 1),

    28: (79, 0, 1),
    30: (149, 0, 1),
    128: (149, 0, 1),

    71: (149, 0, 1),

    27: (29, 0, 1),
    59: (149, 0, 1),
    92: (79, 0, 1),

    158: (79, 0, 1),

    26: (149, 0, 1),
    68: (149, 0, 1),
    130: (79, 0, 1),

    88: (79, 0, 1),
    165: (79, 0, 1),

    93: (79, 0, 1),
    104: (79, 59, 1),
    132: (79, 0, 1),

    108: (79, 0, 1),
    120: (29, 0, 1),
    147: (149, 0, 1),

    45: (79, 0, 1),
    125: (79, 0, 1),

    139: (29, 0, 1),

    111: (29, 0, 1),

    50: (149, 79, 1),
    75: (149, 0, 1),

    117: (79, 0, 1),

    137: (29, 0, 1),

    152: (29, 0, 1),

    11: (79, 0, 1),
    96: (149, 0, 1),

    110: (149, 0, 1),
    126: (79, 0, 1),
    131: (79, 0, 1),

    20: (79, 0, 1),
    49: (299, 0, 1),
    95: (299, 0, 1),
    100: (79, 0, 1),
    101: (149, 0, 1),

    118: (149, 0, 1),
}

def update_offers():
    # Получаем уникальные скины
    all_skins = list(skins.keys())
    selected_skins = random.sample(all_skins, 5)

    boici0 = random.choice(range(1, 38))
    boici1 = random.choice(range(1, 38))
    boici2 = random.choice(range(1, 38))
    boici3 = random.choice([0, 3])

    cost0 = random.randint(1, 50)
    cost1 = random.randint(1, 50)
    cost2 = random.randint(1, 50)
    cost3 = random.randint(1, 50)

    mult0 = random.randint(10, 100)
    mult1 = random.randint(10, 100)
    mult2 = random.randint(10, 100)
    mult3 = random.randint(10, 100)

    with open('offers.json', 'r') as f:
        data = json.load(f)

    for i in range(9):
        data[str(i)]['WhoBuyed'] = []

    # Скины
    for i, skin in enumerate(selected_skins, start=4):
        data[str(i)]['SkinID'] = [skin, 0, 0, 0]
        data[str(i)]['Cost'] = skins[skin][0]
        data[str(i)]['OldCost'] = skins[skin][1]
        data[str(i)]['Multiplier'] = [skins[skin][2], 0, 0, 0]

    # Акции дня
    data['0']['Cost'] = cost0
    data['0']['Multiplier'] = [mult0, 0, 0, 0]
    data['0']['BrawlerID'] = [boici0, 0, 0, 0]

    data['1']['Cost'] = cost1
    data['1']['Multiplier'] = [mult1, 0, 0, 0]
    data['1']['BrawlerID'] = [boici1, 0, 0, 0]

    data['2']['Cost'] = cost2
    data['2']['Multiplier'] = [mult2, 0, 0, 0]
    data['2']['BrawlerID'] = [boici2, 0, 0, 0]

    data['3']['Cost'] = cost3
    data['3']['Multiplier'] = [mult3, 0, 0, 0]
    data['3']['BrawlerID'] = [boici3, 0, 0, 0]

    with open('offers.json', 'w') as f:
        json.dump(data, f)

    # Магаз обновлён в консоли
    now = datetime.now()
    print(f"Магазин обновлен: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Обновление магазина каждые 5 минут
schedule.every(1).minutes.do(update_offers)

# Бесконечный цикл для выполнения задач по расписанию
while True:
    schedule.run_pending()
    time.sleep(1)