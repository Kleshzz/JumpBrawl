# Данный бот делался ZoxDev если вы получили его от других лиц то поздравляю у вас на VPS/VDS ратник который ворует ваш уебанский хост, а нехуй было брать чужой труд и сливать, те кто сольют тем пизда!
import sys
import telebot
import sqlite3
import time
from datetime import datetime
from telebot import TeleBot
from telebot import types
from telebot.types import Message
from difflib import SequenceMatcher
import logging
import json
import re
import os
import random 
import psutil
from ping3 import ping
from core import Server
import datetime
import days
import threading
from termcolor import colored
import pyfiglet
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

ascii_banner = pyfiglet.figlet_format("Kleshzz")
colored_banner = colored(ascii_banner, color='red')
print(colored_banner)
print(colored(f"Bot created by @Nonedge (@KleshzzDev)", 'red'))
print(colored(f"Version 3.2.2", 'red'))
print(colored(f"started!", 'green'))

# Хуета
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Дебаг хуйня
urllib3_logger = logging.getLogger('urllib3')
urllib3_logger.setLevel(logging.WARNING)

# Хуйня
for handler in urllib3_logger.handlers[:]:
    urllib3_logger.removeHandler(handler)

# Хуйня
logger = logging.getLogger(__name__)

bot = telebot.TeleBot('8491461055:AAFX6NZ2ORpN8dQIZoztxdS2bV6OF4VBTts')  # Замените на ваш API ключ

# Айди пидоров старших и младших
admins = {5299823442}
tehs = {}
managers = {}
creator1 = {}
creator2 = {}
creator3 = {}
 
def init_db():
    conn = sqlite3.connect('users.db')  # Название созданной бд
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS accountconnect
        (lowID INTEGER PRIMARY KEY, trophies INTEGER, name TEXT, id_user INTEGER, token TEXT, username TEXT)
    ''')
    conn.commit()
    conn.close()
    
init_db()

# Стартуй сука
@bot.message_handler(commands=['start'])
def start(message):
    response = (
        'Добро пожаловать в бота Jump Brawl!\n\n'
        'TG: @JumpBrawl\n\n'
        '⛔Команды:\n\n'
        '/name [name] - Узнать об аккаунте\n'
        '/info [id] - Узнать об аккаунте.\n'
        '/connect [id] [token] - Привязать аккаунт.\n'
        '/profile - Просмотр профиля.\n'
        '/unlink - Отвязать аккаунт.\n'
        '/top - Посмотреть топы.\n'
        '/recovery [old id] [new token] - Востановить аккаунт.\n\n'
        '/creator - Контент мейкеры\n'
    )
    try:
        bot.reply_to(message, response)
    except Exception as e:
        logger.error(f"Failed to reply to /start command: {e}")

# Админ команды
@bot.message_handler(commands=['admin'])
def admin_command(message):
    user_id = message.from_user.id
    
    if user_id not in admins:
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return

    try:
        bot.reply_to(message, (
            'Admin Commands!\n\n⛔ Команды:\n\n'
            '/vip [id] - Дать ВИП.\n'
            '/unvip [id] - Забрать ВИП.\n'
            '/settokens [id] [amount] - Установить токены.\n'
            '/addtokens [id] [amount] - Добавить токены.\n'
            '/untokens [id] [amount] - Забрать токены.\n'
            '/setgems [id] [amount] - Установить гемы.\n'
            '/addgems [id] [amount] - Добавить гемы.\n'
            '/ungems [id] [amount] - Забрать гемы.\n'
            '/setgold [id] [amount] - Установить золото.\n'
            '/addgold [id] [amount] - Добавить золото.\n'
            '/ungold [id] [amount] - Забрать золото.\n'
            '/unroom - Очистить румы.\n'
            '/teh - Тех. Перерыв.\n'
            '/unteh - Убрать Тех. Перерыв.\n'
            '/ban [id] - Забанить.\n'
            '/unban [id] - Разбанить.\n'
            '/code [code] - Создать код.\n'
            '/code_list - Список кодов.\n'
            '/uncode [code] - Удалить код.\n'
            '/autoshop - Автомагазин.\n'
            '/upshop - Обновить магазин.\n'
            '/rename [id] [new_name] - Изменить имя.\n'
            '/theme [theme] - Тема.\n'
            '/status [status] - Статус.\n'
            '/resetclubs - Удалить клубы.\n'
            '/bd - Сохранить базу данных сервера.\n'
            '/delete - [id] Удалить аккаунт.\n'
            '/addadmin [telegramid] - Добавить админа.\n'
            '/addteh [telegramid] - Добавить Тех.Админа.\n'
            '/addmanager [telegramid] - Добавить Менеджера.\n'
            '/token [id] - Просмотреть токены.\n'
            '/account [id] [token] - Востановить аккаунт.\n'
            '/resetbp [id] - Сброс BrawlPass.\n'
            '/addpass [id] - Дать BrawlPass.\n'
            '/removepass [id] - Забрать BrawlPass.\n'
            '/antiddos - Очистка.\n'
            '/new_offer - Новая акция от 11 до беск.\n'
            '/remove_offer - Удалить акцию с 11.\n'
        ))
    except Exception as e:
        logger.error(f"Failed to reply to /admin command: {e}")
        
@bot.message_handler(commands=['tehadmin'])
def admin_command(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in tehs:
        bot.send_message(message.chat.id, "❌ Вы не являетесь Тех.Админом!")
        return

    try:
        bot.reply_to(message, (
            'Teh.Admin Commands!\n\n⛔ Команды:\n\n'
            '/vip [id] - Дать ВИП.\n'
            '/unvip [id] - Забрать ВИП.\n'
            '/settokens [id] [amount] - Установить токены.\n'
            '/addtokens [id] [amount] - Добавить токены.\n'
            '/untokens [id] [amount] - Забрать токены.\n'
            '/setgems [id] [amount] - Установить гемы.\n'
            '/addgems [id] [amount] - Добавить гемы.\n'
            '/ungems [id] [amount] - Забрать гемы.\n'
            '/setgold [id] [amount] - Установить золото.\n'
            '/addgold [id] [amount] - Добавить золото.\n'
            '/ungold [id] [amount] - Забрать золото.\n'
            '/unroom - Очистить румы.\n'
            '/teh - Тех. Перерыв.\n'
            '/unteh - Убрать Тех. Перерыв.\n'
            '/ban [id] - Забанить.\n'
            '/unban [id] - Разбанить.\n'
            '/code [code] - Создать код.\n'
            '/code_list - Список кодов.\n'
            '/uncode [code] - Удалить код.\n'
            '/autoshop - Автомагазин.\n'
            '/upshop - Обновить магазин.\n'
            '/rename [id] [new_name] - Изменить имя.\n'
            '/theme [theme] - Тема.\n'
            '/status [status] - Статус.\n'
            '/resetclubs - Удалить клубы.\n'
            '/delete - [id] Удалить аккаунт.\n'
            '/addmanager [telegramid] - Добавить Менеджера.\n'
            '/token [id] - Просмотреть токены.\n'
            '/account [id] [token] - Востановить аккаунт.\n'
            '/resetbp [id] - Сброс BrawlPass.\n'
            '/addpass [id] - Дать BrawlPass.\n'
            '/removepass [id] - Забрать BrawlPass.\n'
        ))
    except Exception as e:
        logger.error(f"Failed to reply to /tehadmin command: {e}")

@bot.message_handler(commands=['manager'])
def admin_command(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in managers and user_id not in tehs:
        bot.send_message(message.chat.id, "❌ Вы не являетесь Менеджером!")
        return

    try:
        bot.reply_to(message, (
            'Manager Commands!\n\n⛔ Команды:\n\n'
            '/vip [id] - Дать ВИП.\n'
            '/unvip [id] - Забрать ВИП.\n'
            '/settokens [id] [amount] - Установить токены.\n'
            '/addtokens [id] [amount] - Добавить токены.\n'
            '/untokens [id] [amount] - Забрать токены.\n'
            '/addgems [id] [amount] - Добавить гемы.\n'
            '/ungems [id] [amount] - Забрать гемы.\n'
            '/addgold [id] [amount] - Добавить золото.\n'
            '/ungold [id] [amount] - Забрать золото.\n'
            '/resetbp [id] - Сброс BrawlPass.\n'
            '/addpass [id] - Дать BrawlPass.\n'
            '/removepass [id] - Забрать BrawlPass.\n'
        ))
    except Exception as e:
        logger.error(f"Failed to reply to /manager command: {e}")

@bot.message_handler(commands=['creator'])
def admin_command(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in managers and user_id not in tehs and user_id not in creator1 and user_id not in creator2 and user_id not in creator3:
        bot.send_message(message.chat.id, "❌ Вы не являетесь Контент мейкером!")
        return

    try:
        bot.reply_to(message, (
            'Какой ваш уровень?!\n\n⛔ Команды:\n\n'
            '/creator1 - 1 Уровень\n'
            '/creator2 - 2 Уровень\n'
            '/creator3 - 3 Уровень\n'
        ))
    except Exception as e:
        logger.error(f"Failed to reply to /creator command: {e}")
        
REWARD_INTERVAL = 604800  # 1 неделя в секундах епта

rewards_running = False
last_distribution_time = 0

def distribute_rewards():
    global last_distribution_time
    while True:
        current_time = time.time()
        
        if current_time - last_distribution_time >= REWARD_INTERVAL:  # ну тут интервал
            try:
                with sqlite3.connect('database/Player/plr.db') as plr_conn:
                    plr_cursor = plr_conn.cursor()
                    plr_cursor.execute("SELECT lowID FROM plrs")
                    creators = plr_cursor.fetchall()

                    for (lowID,) in creators:
                        gems, gold, BPTOKEN = get_rewards(lowID)
                        
                        if gems > 0 or gold > 0 or BPTOKEN > 0:
                            plr_cursor.execute(
                                "UPDATE plrs SET gems = gems + ?, gold = gold + ?, BPTOKEN = BPTOKEN + ? WHERE lowID = ?",
                                (gems, gold, BPTOKEN, lowID)
                            )
                            plr_conn.commit()

                            message = f"🎉 Вы получили награду: {gems} Гемов, {gold} Золота, {BPTOKEN} Токенов!"
                            bot.send_message(lowID, message)
                admin_message = "Сервер был перезапущен/награда выдана!"
                for admin_id in admins:
                    bot.send_message(admin_id, admin_message)

                last_distribution_time = current_time
            
            except Exception as e:
                logger.error(f"Error in distributing rewards: {e}")

        time.sleep(1)

def get_rewards(lowID): #награды контенткрейтерам
    if lowID in creator1:
        return 10, 50, 100
    elif lowID in creator2:
        return 20, 150, 300
    elif lowID in creator3:
        return 50, 300, 750
    return 0, 0, 0

@bot.message_handler(commands=['content'])
def content_command(message):
    user_id = message.from_user.id
    if user_id in (admins | tehs | managers):
        threading.Thread(target=immediate_distribution, daemon=True).start()
        bot.reply_to(message, "✅ Награды контентмейкерам были выданы немедленно.")
    else:
        bot.reply_to(message, "❌ У вас нет прав для выполнения этой команды!")

def immediate_distribution():
    try:
        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()
            plr_cursor.execute("SELECT lowID FROM plrs")
            creators = plr_cursor.fetchall()

            for (lowID,) in creators:
                gems, gold, BPTOKEN = get_rewards(lowID)
                
                if gems > 0 or gold > 0 or BPTOKEN > 0:
                    plr_cursor.execute(
                        "UPDATE plrs SET gems = gems + ?, gold = gold + ?, BPTOKEN = BPTOKEN + ? WHERE lowID = ?",
                        (gems, gold, BPTOKEN, lowID)
                    )
                    plr_conn.commit()

                    message = f"🎉 Вы получили награду: {gems} Гемов, {gold} Золота, {BPTOKEN} Токенов!"
                    bot.send_message(lowID, message)

    except Exception as e:
        logger.error(f"Error in immediate distribution: {e}")

def create_creator_handler(level, gems, gold, BPTOKEN):
    level = set(level)  # Уровень контенмейкерсва

    def creator_command(message):
        user_id = message.from_user.id
        
        if user_id not in (admins | managers | tehs | level):
            bot.send_message(message.chat.id, "❌ Вы не являетесь Контент мейкером!")
            return

        try:
            with sqlite3.connect('users.db') as users_conn:
                users_cursor = users_conn.cursor()
                users_cursor.execute("SELECT lowID FROM accountconnect WHERE id_user = ?", (user_id,))
                row = users_cursor.fetchone()

                if row:
                    lowID = row[0]
                    with sqlite3.connect('database/Player/plr.db') as plr_conn:
                        plr_cursor = plr_conn.cursor()
                        plr_cursor.execute("SELECT SCC FROM plrs WHERE lowID = ?", (lowID,))
                        code_row = plr_cursor.fetchone()

                        author_code = code_row[0] if code_row and code_row[0] else "нет кода"

                        plr_cursor.execute("SELECT COUNT(*) FROM plrs WHERE SCC = ?", (author_code,))
                        count = plr_cursor.fetchone()[0] if author_code != "нет кода" else 0

                        plr_cursor.execute(
                            "UPDATE plrs SET gems = gems + ?, gold = gold + ?, BPTOKEN = BPTOKEN + ? WHERE lowID = ?",
                            (gems, gold, BPTOKEN, lowID)
                        )
                        plr_conn.commit()

                        response_message = (
                            f'⛔ Ваш успех!\n\n'
                            f'1. Каждую неделю вы будете получать:\n'
                            f'{gems} Гемов, {gold} золота, {BPTOKEN} Токенов\n\n'
                            f"🔍 Кодом автора пользуются {count} аккаунта(ов).\n"
                            f"🔍 Ваш код: {author_code}"
                        )
                else:
                    response_message = "❌ Ошибка: Вы не привязали аккаунт."

            bot.reply_to(message, response_message)

        except Exception as e:
            logger.error(f"Failed to reply to creator command: {e}")
            bot.send_message(message.chat.id, "❌ Произошла ошибка при выполнении команды.")

    return creator_command

# Уровни креатерства
bot.message_handler(commands=['creator1'])(create_creator_handler(creator1, 10, 50, 100))
bot.message_handler(commands=['creator2'])(create_creator_handler(creator2, 20, 150, 300))
bot.message_handler(commands=['creator3'])(create_creator_handler(creator3, 50, 300, 750))

threading.Thread(target=distribute_rewards, daemon=True).start()

        
@bot.message_handler(commands=['profile'])
def handle_profile(message):
    user_id = message.from_user.id

    try:
        with sqlite3.connect('users.db') as users_conn:
            users_cursor = users_conn.cursor()
            users_cursor.execute("SELECT lowID FROM accountconnect WHERE id_user = ?", (user_id,))
            row = users_cursor.fetchone()

            if row:
                lowID = row[0]

                with sqlite3.connect('database/Player/plr.db') as plr_conn:
                    plr_cursor = plr_conn.cursor()
                    plr_cursor.execute("SELECT token, name, trophies, gems, gold, starpoints, tickets, vip, SCC FROM plrs WHERE lowID = ?", (lowID,))
                    plr_row = plr_cursor.fetchone()

                    if plr_row:
                        token, name, trophies, gems, gold, starpoints, tickets, vip, SCC = plr_row
                        vip_status = "Есть" if vip in [1, 2, 3] else "Отсутствует"

                        with open("config.json", "r", encoding='utf-8') as f:
                            config = json.load(f)
                        bp_status = "Куплен" if lowID in config["buybp"] else "Отсутствует"

                        name = escape_markdown(name.strip())
                        author_code_status = SCC if SCC else "Отсутствует"

                        roles = []
                        rewards = ""
                        if user_id in creator1:
                            roles.append("Creator - 1 Уровень")
                            rewards = "10 Гемов, 50 золота, 100 Токенов каждую неделю."
                        elif user_id in creator2:
                            roles.append("Creator - 2 Уровень")
                            rewards = "20 Гемов, 150 золота, 300 Токенов каждую неделю.\n5 Гемов, 75 золота, 150 Токенов за каждое использование кода."
                        elif user_id in creator3:
                            roles.append("Creator - 3 Уровень")
                            rewards = "50 Гемов, 300 золота, 750 Токенов каждую неделю.\n15 Гемов, 150 золота, 300 Токенов за каждое использование кода.\nVIP статус."
                        if user_id in admins:
                            roles.append("Администратор")
                        if user_id in tehs:
                            roles.append("Тех.Админ")
                        if user_id in managers:
                            roles.append("Менеджер")

                        role_str = ", ".join(roles) if roles else "Игрок"

                        profile_info = (f"🤠 Статистика аккаунта: {name}:\n\n🆔 ID: {lowID}\n📱 Токен: {token}\n\n"
                                        f"🏆 Трофеи: {trophies}\n💎 Гемы: {gems}\n💸 Монеты: {gold}\n"
                                        f"🎟️ Билеты: {tickets}\n⭐ Старпоинты: {starpoints}\n\n"
                                        f"💳 VIP: {vip_status}\n🎫 BrawlPass: {bp_status}\n"
                                        f"🔑 Код автора: {author_code_status}\n"
                                        f"🌟 Роль: {role_str}\n")

                        if rewards:
                            profile_info += f"🎁 Награды: {rewards}"

                        bot.send_message(user_id, profile_info)
                    else:
                        bot.send_message(user_id, "❌ Ошибка! Аккаунт не найден.")
            else:
                bot.send_message(user_id, "❌ Вы не привязали аккаунт. Используйте команду /connect.")
    except Exception as e:
        logger.error(f"Error in /profile command: {e}")
        bot.send_message(user_id, f"❌ Произошла ошибка: {str(e)}")
        
@bot.message_handler(commands=['antiddos'])
def handle_antiddos(message: types.Message):
    if message.from_user.id not in admins and message.from_user.id not in tehs:
        bot.send_message(message.chat.id, "❌ У вас нет прав для выполнения этой команды.")
        return

    bot.send_message(message.chat.id, "Выберите метод:\n"
                                       "1. Очистить аккаунт по имени\n"
                                       "2. Очистить аккаунт по трофеям\n"
                                       "3. Очистить клуб\n"
                                       "4. Очистить список друзей\n"
                                       "5. Очистить бот-клуб\n"
                                       "6. Очистить аккаунт по имени++")

    bot.register_next_step_handler(message, process_antiddos_selection)

def process_antiddos_selection(message: types.Message):
    choice = message.text

    try:
        if choice == '1':
            clear_accounts_by_name(message.from_user.id)
        elif choice == '2':
            clear_accounts_by_trophies(message.from_user.id)
        elif choice == '3':
            clear_club(message.from_user.id)
        elif choice == '4':
            clear_friends_list(message.from_user.id)
        elif choice == '5':
            clear_bot_club(message.from_user.id)
        elif choice == '6':
            clear_accounts_by_name_plus(message.from_user.id)
        else:
            bot.send_message(message.from_user.id, "❌ Неверный выбор. Пожалуйста, попробуйте снова.")
    except Exception as e:
        bot.send_message(message.from_user.id, f"❌ Произошла ошибка: {str(e)}")

def clear_accounts_by_name(user_id):
    try:
        with open('config.json', 'r') as config:
            settings = json.load(config)

        with sqlite3.connect('database/Player/plr.db') as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT lowID FROM plrs WHERE name IN ({})".format(','.join(['?'] * len(settings['DelName']))), settings['DelName'])
            rows = cursor.fetchall()

            for row in rows:
                cursor.execute("DELETE FROM plrs WHERE lowID=?", (row[0],))
            conn.commit()

        bot.send_message(user_id, "✅ Аккаунты по имени очищены.")
    except Exception as e:
        logging.error(f"Failed to clear accounts by name: {e}")

def clear_accounts_by_trophies(user_id):
    try:
        with sqlite3.connect('database/Player/plr.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM plrs WHERE trophies = 0")
            conn.commit()

        bot.send_message(user_id, "✅ Аккаунты по трофеям очищены.")
    except Exception as e:
        logging.error(f"Failed to clear accounts by trophies: {e}")

def clear_club(user_id):
    try:
        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET quests = ?", ('[]',))
            conn.commit()

        bot.send_message(user_id, "✅ Клубы очищены.")
    except Exception as e:
        logging.error(f"Failed to clear clubs: {e}")

def clear_friends_list(user_id):
    try:
        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET friends = ? WHERE friends IS NOT NULL", (json.dumps([]),))
            conn.commit()

        bot.send_message(user_id, "✅ Списки друзей очищены.")
    except Exception as e:
        logging.error(f"Failed to clear friends list: {e}")

def clear_bot_club(user_id):
    try:
        with open('config.json', 'r') as config:
            settings = json.load(config)

        with sqlite3.connect('database/Club/clubs.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM clubs WHERE LENGTH(clubID) = 28")
            conn.commit()

        bot.send_message(user_id, "✅ Бот-клубы очищены.")
    except Exception as e:
        logging.error(f"Failed to clear bot clubs: {e}")

def clear_accounts_by_name_plus(user_id):
    try:
        with sqlite3.connect('database/Player/plr.db') as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM plrs WHERE name LIKE 'player%'")
            conn.commit()

        bot.send_message(user_id, "✅ Аккаунты по имени++ очищены.")
    except Exception as e:
        logging.error(f"Failed to clear accounts by name++: {e}")
        
@bot.message_handler(commands=['delete'])
def handle_delete(message: types.Message):
    user_id = message.from_user.id
    command_parts = message.text.split()
    
    if user_id not in admins and user_id not in tehs:
        bot.send_message(user_id, "❌ У вас нет прав для выполнения этой команды.")
        return

    if len(command_parts) != 2:
        bot.send_message(user_id, "Неверный формат команды. Используйте: /delete [id]")
        return

    try:
        lowID_to_delete = command_parts[1]

        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()
            plr_cursor.execute("DELETE FROM plrs WHERE lowID = ?", (lowID_to_delete,))
            plr_conn.commit()

            if plr_cursor.rowcount > 0:
                bot.send_message(user_id, f"✅ Аккаунт с lowID {lowID_to_delete} был успешно удален.")
            else:
                bot.send_message(user_id, "❌ Аккаунт не найден.")
    except Exception as e:
        logging.error(f"Error in /delete command: {e}")
        bot.send_message(user_id, f"❌ Произошла ошибка: {str(e)}")
        
@bot.message_handler(commands=['addadmin'])
def add_admin(message: Message):
    if message.from_user.id in admins:
        try:
            new_admin_id = int(message.text.split()[1])
            if new_admin_id in admins:
                bot.reply_to(message, "❌ Этот пользователь уже является администратором.")
            else:
                admins.add(new_admin_id)
                bot.reply_to(message, f"✅ Пользователь {new_admin_id} был добавлен в администраторы.")
        except (IndexError, ValueError):
            bot.reply_to(message, "Использование: /addadmin [telegramid]")
    else:
        bot.reply_to(message, "❌ У вас нет прав для выполнения этого действия.")

@bot.message_handler(commands=['addteh'])
def add_tech(message: Message):
    if message.from_user.id in admins:
        try:
            new_tech_id = int(message.text.split()[1])
            if new_tech_id in tehs:
                bot.reply_to(message, "❌ Этот пользователь уже является техническим администратором.")
            else:
                teh.add(new_tech_id)
                bot.reply_to(message, f"✅ Пользователь {new_tech_id} был добавлен в технические администраторы.")
        except (IndexError, ValueError):
            bot.reply_to(message, "Использование: /addteh [telegramid]")
    else:
        bot.reply_to(message, "❌ У вас нет прав для выполнения этого действия.")

@bot.message_handler(commands=['addmanager'])
def add_manager(message: Message):
    if message.from_user.id in admins and user_id in tehs:
        try:
            new_manager_id = int(message.text.split()[1])
            if new_manager_id in managers:
                bot.reply_to(message, "❌ Этот пользователь уже является менеджером.")
            else:
                autoshop.append(new_manager_id)
                bot.reply_to(message, f"✅ Пользователь {new_manager_id} был добавлен в менеджеры.")
        except (IndexError, ValueError):
            bot.reply_to(message, "Использование: /addmanager [telegramid]")
    else:
        bot.reply_to(message, "❌ У вас нет прав для выполнения этого действия.")

@bot.message_handler(commands=['unlink'])
def unlink_account(message):
    user_id = message.from_user.id

    try:
        with sqlite3.connect('users.db') as bot_db_connection:
            bot_db_cursor = bot_db_connection.cursor()

            bot_db_cursor.execute("SELECT lowID, name FROM accountconnect WHERE id_user = ?", (user_id,))
            result = bot_db_cursor.fetchone()

            if result:
                lowID, name = result

                bot_db_cursor.execute("DELETE FROM accountconnect WHERE id_user = ?", (user_id,))
                bot_db_connection.commit()

                bot.send_message(message.chat.id, f"✅ Ваш аккаунт успешно отвязан: {name}.\n\n🆔 ID: {lowID}")
            else:
                bot.send_message(message.chat.id, "❌ Вы не привязали аккаунт. Используйте команду /connect.")
    except Exception as e:
        logger.error(f"Error in /unlink command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

def send_top(message, top_type='trophies', page=1):
    try:
        with sqlite3.connect('database/Player/plr.db') as server_db_connection:
            server_db_cursor = server_db_connection.cursor()

            limit = 10
            offset = (page - 1) * limit
            
            if top_type == 'trophies':
                server_db_cursor.execute("SELECT name, trophies FROM plrs ORDER BY trophies DESC LIMIT ? OFFSET ?", (limit, offset))
                top_accounts = server_db_cursor.fetchall()
                header = "🏆 Топ аккаунты по кубкам:\n\n"
            else:
                server_db_cursor.execute("SELECT name, gems, gold, starpoints FROM plrs ORDER BY (gems + gold + starpoints) DESC LIMIT ? OFFSET ?", (limit, offset))
                top_accounts = server_db_cursor.fetchall()
                header = "💎 Топ аккаунты по ресурсам:\n\n"

            if top_accounts:
                top_info = header
                for idx, account in enumerate(top_accounts, start=offset + 1):
                    if top_type == 'trophies':
                        name, trophies = account
                        top_info += f"{idx}. {name}:\n🏆 Кубки: {trophies}\n\n"
                    else:
                        name, gems, gold, starpoints = account
                        top_info += f"{idx}. {name}:\n💎 Гемы: {gems}\n💰 Монеты: {gold}\n⭐ Старпоинты: {starpoints}\n\n"
                
                keyboard = types.InlineKeyboardMarkup()
                if page > 1:
                    keyboard.add(types.InlineKeyboardButton('⬅️ Назад', callback_data=f'top_{top_type}_{page-1}'))
                keyboard.add(types.InlineKeyboardButton('➡️ Далее', callback_data=f'top_{top_type}_{page+1}'))
                
                bot.send_message(message.chat.id, top_info, reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id, "❌ Топ аккаунтов не найден!")
    except Exception as e:
        logger.error(f"Error in send_top function: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

@bot.message_handler(commands=['top'])
def top_command(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton('Топ по кубкам', callback_data='top_trophies_1'))
    keyboard.add(types.InlineKeyboardButton('Топ по ресурсам', callback_data='top_resources_1'))
    
    bot.send_message(message.chat.id, "Выберите тип топа:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data.startswith('top_'))
def handle_top_callback(call):
    top_type, page = call.data.split('_')[1:3]
    page = int(page)
    
    if page < 1:
        page = 1
    
    send_top(call.message, top_type, page)
    
    bot.delete_message(call.message.chat.id, call.message.message_id)

@bot.message_handler(commands=['token'])
def token_command(message):
    user_id = message.from_user.id

    if user_id not in admins and user_id not in tehs:
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return

    try:
        args = message.text.split()
        if len(args) != 2:
            bot.send_message(message.chat.id, "❌ Используйте команду в формате: /token [lowID]")
            return
        
        lowID = int(args[1])

        with sqlite3.connect('database/Player/plr.db') as server_db_connection:
            server_db_cursor = server_db_connection.cursor()
            
            server_db_cursor.execute("SELECT token, name, trophies, gems, gold, starpoints, tickets, vip FROM plrs WHERE lowID = ?", (lowID,))
            result = server_db_cursor.fetchone()
            
            if result:
                token, name, trophies, gems, gold, starpoints, tickets, vip = result
                vip_status = "Есть" if vip in [1, 2, 3] else "Отсутствует"
                
                token_info = (f"🆔 ID: {lowID}\n\n"
                              f"📱 Токен: `{token}`\n")
                bot.send_message(message.chat.id, token_info, parse_mode='Markdown')
            else:
                bot.send_message(message.chat.id, "❌ Аккаунт с указанным lowID не найден!")
    
    except ValueError:
        bot.send_message(message.chat.id, "❌ Неверный формат lowID. Убедитесь, что вы вводите число.")
    except Exception as e:
        logger.error(f"Error in /token command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

@bot.message_handler(commands=['account'])
def update_token(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in tehs:
        bot.send_message(message.chat.id, "❌ Вы не являетесь техадминистратором!")
        return
    
    parts = message.text.split()
    if len(parts) != 3:
        bot.reply_to(message, "Правильное использование: /account ID NEW_TOKEN")
        return
    
    player_id = parts[1]
    new_token = parts[2]
    
    try:
        with sqlite3.connect('database/Player/plr.db') as conn:
            cursor = conn.cursor()
            
            cursor.execute("SELECT * FROM plrs WHERE lowID=?", (player_id,))
            if cursor.fetchone() is None:
                bot.reply_to(message, f"Игрок с ID {player_id} не найден.")
                return
            
            cursor.execute("UPDATE plrs SET token = ? WHERE lowID = ?", (new_token, player_id))
            conn.commit()
            
            bot.send_message(chat_id=message.chat.id, text=f"Токен для игрока с ID {player_id} успешно обновлён.")
    except Exception as e:
        logger.error(f"Error in /account command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

def escape_markdown(text):
    """ Escape MarkdownV2 special characters """
    text = re.sub(r'([_\*`\[\]()~|>#+-=|{}.!])', r'\\\1', text)
    return text

def escape_markdown_v2(text):
    """Escape characters for MarkdownV2."""
    characters_to_escape = ['_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!']
    for char in characters_to_escape:
        text = text.replace(char, f'\\{char}')
    return text

def format_value(value):
    """Format the value to include 'отрицательное' if it's negative."""
    if value < 0:
        return f"{abs(value)} Отрицательное"
    return str(value)

@bot.message_handler(commands=['connect'])
def connect_command(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise ValueError("Неверный формат команды. Введите \n/connect [ваш айди] [ваш токен]\n\nВаш айди и токен в игре! Например 1 AxH24bHs4Ijf84RsuN7gnzx")

        player_id = int(parts[1])
        token = parts[2]
    except (IndexError, ValueError):
        bot.send_message(message.chat.id, "Введите \n/connect [ваш айди] [ваш токен]\n\nВаш айди и токен в игре! Например 1 ABC123")
        return

    try:
        user_id = message.from_user.id
        username = message.from_user.username

        with sqlite3.connect('users.db') as bot_db_connection:
            bot_db_cursor = bot_db_connection.cursor()

            bot_db_cursor.execute('''
                CREATE TABLE IF NOT EXISTS accountconnect
                (lowID INTEGER PRIMARY KEY, trophies INTEGER, name TEXT, id_user INTEGER, token TEXT, username TEXT)
            ''')
            bot_db_connection.commit()

            bot_db_cursor.execute("SELECT lowID, token FROM accountconnect WHERE id_user = ?", (user_id,))
            existing_account = bot_db_cursor.fetchone()

            if existing_account:
                existing_lowID, existing_token = existing_account
                if existing_token != token:
                    bot.send_message(message.chat.id, "❌ Этот аккаунт уже привязан к другому пользователю или токен неверен!")
                    return
                bot.send_message(message.chat.id, "❌ Аккаунт уже привязан!")
                return

            with sqlite3.connect('database/Player/plr.db') as server_db_connection:
                server_db_cursor = server_db_connection.cursor()

                server_db_cursor.execute("SELECT lowID, trophies, name, token FROM plrs WHERE lowID = ?", (player_id,))
                player_data = server_db_cursor.fetchone()

                if player_data:
                    player_lowID, player_trophies, player_name, player_token = player_data

                    # Проверяем, совпадает ли хотя бы половина символов токена
                    similarity_ratio = SequenceMatcher(None, token, player_token).ratio()
                    if similarity_ratio >= 0.5:
                        bot_db_cursor.execute("INSERT INTO accountconnect (lowID, trophies, name, id_user, token, username) VALUES (?, ?, ?, ?, ?, ?)", (player_lowID, player_trophies, player_name, user_id, token, username))
                        bot_db_connection.commit()

                        bot.send_message(message.chat.id, f"🏴 Ваш аккаунт привязан! {player_name}:\n\n🆔 ID: {player_lowID}\n🏆 Кубки: {player_trophies}")
                    else:
                        bot.send_message(message.chat.id, "❌ Токен неверен!")
                else:
                    bot.send_message(message.chat.id, "❌ Аккаунт с указанным айди не найден!")
    except Exception as e:
        logger.error(f"Error in /connect command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

def escape_markdown_v2(text):
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    for char in escape_chars:
        text = text.replace(char, f'\\{char}')
    return text

def format_value(value):
    return f"{value}" if value >= 0 else f"-{abs(value)}"

def escape_html(text):
    import html
    return html.escape(text)

@bot.message_handler(commands=['info'])
def info_command(message):
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "❌ Используйте команду в формате: /info [lowID]")
        return

    try:
        lowID = int(args[1])
    except ValueError:
        bot.send_message(message.chat.id, "❌ Неверный формат lowID. Убедитесь, что вы вводите число.")
        return

    try:
        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()
            plr_cursor.execute("SELECT token, name, trophies, gems, gold, starpoints, tickets, vip, SCC FROM plrs WHERE lowID = ?", (lowID,))
            plr_row = plr_cursor.fetchone()

            if plr_row:
                token, name, trophies, gems, gold, starpoints, tickets, vip, SCC = plr_row
                vip_status = "Есть" if vip in [1, 2, 3] else "Отсутствует"

                with open("config.json", "r", encoding='utf-8') as f:
                    config = json.load(f)

                # Проверка статуса VIP в config.json
                if lowID not in config["vips"]:
                    vip_status = "Отсутствует"

                bp_status = "Куплен" if lowID in config.get("buybp", []) else "Отсутствует"
                author_code_status = SCC if SCC else "Отсутствует"
                name = escape_html(name.strip())

                trophies = format_value(trophies)
                gems = format_value(gems)
                gold = format_value(gold)
                starpoints = format_value(starpoints)
                tickets = format_value(tickets)

                with sqlite3.connect('users.db') as bot_db_connection:
                    bot_db_cursor = bot_db_connection.cursor()
                    bot_db_cursor.execute("SELECT username FROM accountconnect WHERE lowID = ?", (lowID,))
                    user_row = bot_db_cursor.fetchone()

                registration_info = f"Подтвержден: @{user_row[0]}" if user_row else "Аккаунт: Не подтвержден"

                roles = []
                if lowID in creator1:
                    roles.append("Creator - 1 Уровень")
                if lowID in creator2:
                    roles.append("Creator - 2 Уровень")
                if lowID in creator3:
                    roles.append("Creator - 3 Уровень")
                if lowID in admins:
                    roles.append("Администратор")
                if lowID in tehs:
                    roles.append("Тех.Админ")
                if lowID in managers:
                    roles.append("Менеджер")

                role_str = ", ".join(roles) if roles else "Игрок"

                profile_info = (f"🤠 Статистика аккаунта: {name}:\n\n"
                                f"🆔 ID: {lowID}\n📱 Токен: `ONLYADMIN`\n\n"
                                f"🏆 Трофеи: {trophies}\n💎 Гемы: {gems}\n💸 Монеты: {gold}\n"
                                f"🎟️ Билеты: {tickets}\n⭐ Старпоинты: {starpoints}\n\n"
                                f"💳 VIP: {vip_status}\n🎫 BrawlPass: {bp_status}\n"
                                f"🔑 Код автора: {author_code_status}\n\n"
                                f"{registration_info}\n")

                try:
                    bot.send_message(message.chat.id, profile_info, parse_mode='HTML')
                except Exception as e:
                    logger.error(f"Error sending message: {e}")
                    bot.send_message(message.chat.id, "❌ Произошла ошибка при отправке сообщения.")
            else:
                bot.send_message(message.chat.id, "❌ Аккаунт с указанным lowID не найден.")
    except Exception as e:
        logger.error(f"Error in /info command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")


@bot.message_handler(commands=['resetbp'])
def reset_brawl_pass(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in tehs and user_id not in managers:
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return
    
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "❌ Используйте команду в формате: /resetbp [lowID]")
        return

    try:
        lowID = int(args[1])
    except ValueError:
        bot.send_message(message.chat.id, "❌ Неверный формат lowID. Убедитесь, что вы вводите число.")
        return

    try:
        freepass_data = json.dumps([])
        buypass_data = json.dumps([])
        
        with sqlite3.connect('database/Player/plr.db') as server_db_connection:
            server_db_cursor = server_db_connection.cursor()

            server_db_cursor.execute("UPDATE plrs SET freepass = ?, buypass = ?, BPTOKEN = ? WHERE lowID = ?", 
                                    (freepass_data, buypass_data, 0, lowID))
            server_db_connection.commit()

            bot.send_message(message.chat.id, f"✅ Brawl Pass для аккаунта с ID {lowID} успешно сброшен.")
    except Exception as e:
        logger.error(f"Error in /resetbp command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")
        
@bot.message_handler(commands=['addpass'])
def add_brawl_pass(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in tehs and user_id not in managers:
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return
    
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "❌ Используйте команду в формате: /addpass [lowID]")
        return

    try:
        lowID = int(args[1])
    except ValueError:
        bot.send_message(message.chat.id, "❌ Неверный формат lowID. Убедитесь, что вы вводите число.")
        return

    try:
        with open("config.json", "r", encoding='utf-8') as f:
            config = json.load(f)

        if lowID not in config["buybp"]:
            config["buybp"].append(lowID)
            bot.send_message(message.chat.id, f"✅ Brawl Pass добавлен для игрока с ID {lowID}.")
        else:
            bot.send_message(message.chat.id, f"❌ Brawl Pass уже добавлен для игрока с ID {lowID}.")

        with open("config.json", "w", encoding='utf-8') as f:
            json.dump(config, f, indent=4)

    except Exception as e:
        logger.error(f"Error in /addpass command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

@bot.message_handler(commands=['removepass'])
def remove_brawl_pass(message):
    user_id = message.from_user.id
    
    if user_id not in admins and user_id not in tehs and user_id not in managers:
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return
    
    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "❌ Используйте команду в формате: /removepass [lowID]")
        return

    try:
        lowID = int(args[1])
    except ValueError:
        bot.send_message(message.chat.id, "❌ Неверный формат lowID. Убедитесь, что вы вводите число.")
        return

    try:
        with open("config.json", "r", encoding='utf-8') as f:
            config = json.load(f)

        if lowID in config["buybp"]:
            config["buybp"].remove(lowID)
            bot.send_message(message.chat.id, f"✅ Brawl Pass удален для игрока с ID {lowID}.")
        else:
            bot.send_message(message.chat.id, f"❌ Brawl Pass не найден для игрока с ID {lowID}.")

        with open("config.json", "w", encoding='utf-8') as f:
            json.dump(config, f, indent=4)
        
    except Exception as e:
        logger.error(f"Error in /removepass command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")
        
def escape_markdown(text):
    """ Escape MarkdownV2 special characters """
    return re.sub(r'([_*\[\]()~`>#+-=|{}.!])', r'\\\1', text)

@bot.message_handler(commands=['name'])
def name_command(message):
    args = message.text.split(maxsplit=1)
    
    if len(args) != 2:
        bot.send_message(message.chat.id, "❌ Используйте команду в формате: /name [имя]")
        return

    name = args[1].strip()

    try:
        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()

            plr_cursor.execute("SELECT lowID, name FROM plrs WHERE name = ?", (name,))
            plr_rows = plr_cursor.fetchall()

            if plr_rows:
                account_list = "\n".join([f"{idx + 1}. ID: {row[0]}, Имя: {row[1]}" for idx, row in enumerate(plr_rows)])
                
                keyboard = types.InlineKeyboardMarkup()
                for idx, row in enumerate(plr_rows):
                    button_text = f"ID: {row[0]}, Имя: {row[1]}"
                    keyboard.add(types.InlineKeyboardButton(button_text, callback_data=f'name_{row[0]}'))

                bot.send_message(message.chat.id, f"Найдено несколько аккаунтов с именем `{name}`:\n\n{account_list}", reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id, "❌ Аккаунт с указанным именем не найден.")
    except Exception as e:
        logger.error(f"Error in /name command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

@bot.callback_query_handler(func=lambda call: call.data.startswith('name_'))
def handle_name_selection(call):
    lowID = int(call.data.split('_')[1])
    
    try:
        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()

            plr_cursor.execute("SELECT token, name, trophies, gems, gold, starpoints, tickets, vip, SCC FROM plrs WHERE lowID = ?", (lowID,))
            plr_row = plr_cursor.fetchone()

            if plr_row:
                token, name, trophies, gems, gold, starpoints, tickets, vip, SCC = plr_row
                vip_status = "Есть" if vip in [1, 2, 3] else "Отсутствует"

                with open("config.json", "r", encoding='utf-8') as f:
                    config = json.load(f)
                bp_status = "Куплен" if lowID in config["buybp"] else "Отсутствует"

                author_code_status = SCC if SCC else "Отсутствует"
                name = escape_markdown(name.strip())
                
                with sqlite3.connect('users.db') as bot_db_connection:
                    bot_db_cursor = bot_db_connection.cursor()
                    bot_db_cursor.execute("SELECT username FROM accountconnect WHERE lowID = ?", (lowID,))
                    user_row = bot_db_cursor.fetchone()

                if user_row:
                    username = user_row[0]
                    registration_info = f"Подтвержден: @{username}"
                else:
                    registration_info = "Аккаунт: Не подтвержден"
                
                if user_row:
                    username = user_row[0]
                    registration_info = f"Подтвержден: @{username}"
                else:
                    registration_info = "Аккаунт: Не подтвержден"
                
                profile_info = (f"🤠 Статистика аккаунта: {escape_markdown(name)}:\n\n🆔 ID: {lowID}\n📱 Токен: `ONLYADMIN`\n\n"
                                f"🏆 Трофеи: {trophies}\n💎 Гемы: {gems}\n💸 Монеты: {gold}\n"
                                f"🎟️ Билеты: {tickets}\n⭐ Старпоинты: {starpoints}\n\n"
                                f"💳 VIP: {vip_status}\n🎫 BrawlPass: {bp_status}\n"
                                f"🔑 Код автора: {author_code_status}\n\n"
                                f"{registration_info}")
                bot.send_message(call.message.chat.id, profile_info, parse_mode='HTML')
            else:
                bot.send_message(call.message.chat.id, "❌ Ошибка: выбранный аккаунт не найден.")
    except Exception as e:
        logger.error(f"Error in handle_name_selection callback: {e}")
        bot.send_message(call.message.chat.id, f"❌ Произошла ошибка: {str(e)}")
        
@bot.message_handler(commands=['recovery'])
def recovery_command(message):
    user_id = message.from_user.id

    try:
        with sqlite3.connect('users.db') as bot_db_connection:
            bot_db_cursor = bot_db_connection.cursor()
            
            bot_db_cursor.execute("SELECT lowID FROM accountconnect WHERE id_user = ?", (user_id,))
            profile_info = bot_db_cursor.fetchone()

            if not profile_info:
                bot.send_message(message.chat.id, "❌ Ваш профиль не активен. Сначала используйте команду /profile для активации профиля.")
                return
            
            user_lowID = profile_info[0]

        parts = message.text.split()
        if len(parts) != 3:
            bot.send_message(message.chat.id, "❌ Используйте команду в формате: /recovery [lowID] [новый токен]")
            return
        
        lowID = int(parts[1])
        new_token = parts[2]

        if lowID != user_lowID:
            bot.send_message(message.chat.id, "❌ Вы не можете изменять токен для данного lowID, так как это не ваш профиль.")
            return

        with sqlite3.connect('database/Player/plr.db') as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM plrs WHERE lowID = ?", (lowID,))
            player = cursor.fetchone()

            if player is None:
                bot.send_message(message.chat.id, f"❌ Игрок с ID {lowID} не найден.")
                return

            old_token = player[1]  # Предполагается, что токен находится во втором столбце

            # Удаляем аккаунт с новым токеном
            cursor.execute("DELETE FROM plrs WHERE token = ?", (new_token,))
            
            # Обновляем токен для текущего игрока
            cursor.execute("UPDATE plrs SET token = ? WHERE lowID = ?", (new_token, lowID))
            conn.commit()

            bot.send_message(chat_id=message.chat.id, text=f"✅ Токен для игрока с ID {lowID} успешно обновлён. Аккаунт с новым токеном был удалён.")

    except Exception as e:
        logger.error(f"Error in /recovery command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

def dball():
    conn = sqlite3.connect("database/Player/plr.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM plrs")
    return cur.fetchall()

config_file_path = 'config.json'

def load_config():
    try:
        with open(config_file_path, 'r', encoding='utf-8') as file:
            config = json.load(file)
        return config
    except (FileNotFoundError, json.JSONDecodeError):
        return None

def save_config(config):
    try:
        with open(config_file_path, 'w', encoding='utf-8') as file:
            json.dump(config, file, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return False

def update_maintenance_status(new_status):
    config = load_config()
    if config:
        config['maintenance'] = new_status
        return save_config(config)
    return False

def is_admin(user_id):
    return user_id in admins, tehs


# Структура для скинов
skins = {
    "common": [29, 15, 2, 103, 109, 167, 27, 120, 139, 111, 137, 152,],  # ID скинов
    "rare": [25, 102, 58, 98, 28, 92, 158, 130, 88, 165, 93, 104, 132, 108, 45, 125, 117, 11, 126, 131, 20, 100],
    "epic": [52, 159, 79, 64, 44, 123, 163, 91, 57, 160, 99, 30, 128, 71, 59, 26, 68, 147, 50, 75, 96, 110, 101, 118],
    "legendary": [94, 49, 95]
}

# Привязка цен к редкостям
skin_prices = {
    "common": (29, 29),
    "rare": (79, 79),
    "epic": (149, 149),
    "legendary": (299, 299)
}

def get_offers():
    with open("Logic/offers.json", "r",encoding='utf-8') as f:
        data = json.load(f)

    offer_list = "Список акций:\n"
    for offer_id, offer_data in data.items():
        vault=offer_data['ShopType']
        daily=offer_data['ShopDisplay']
        current=""
        types=""
        if vault==1:current="Золото"
        elif vault==0:current="Кристаллы"
        if daily==1:types="Ежедневная"
        elif daily==0:types="Обычная"
        offer_list += f"\nАкция #{offer_id}\n"
        offer_list += f"Название: {offer_data['OfferTitle']}\n"
        offer_list += f"Тип: {types}\n"
        offer_list += f"Боец: {offer_data['BrawlerID'][0]}\n"
        offer_list += f"Скин: {offer_data['SkinID'][0]}\n"
        offer_list += f"Валюта: {current}\n"
        offer_list += f"Стоимость: {offer_data['Cost']}\n"
        offer_list += f"Множитель: {offer_data['Multiplier'][0]}\n"

    return offer_list
@bot.message_handler(commands=['list'])
def handle_list_offers(message):
    offer_list = get_offers()

    bot.send_message(chat_id=message.chat.id, text=offer_list)
    
    
@bot.message_handler(commands=['new_offer'])
def add_offer(message):
    user_id = message.from_user.id
    if user_id in admins:
        offer_data = message.text.split()
        
        if len(offer_data) != 10:  # Expecting exactly 10 parts
            bot.reply_to(message, 'Используйте команду /new_offer с аргументами в формате: /new_offer <ID> <OfferTitle> <Cost> <Multiplier> <BrawlerID> <SkinID> <OfferBGR> <ShopType> <ShopDisplay>')
            return
        
        print("Received offer data:", offer_data)  # Debugging output
        
        try:
            new_offer = {
                'ID': [int(offer_data[1]), 0, 0],
                'OfferTitle': offer_data[2],
                'Cost': int(offer_data[3]),
                'OldCost': 0,
                'Multiplier': [int(offer_data[4]), 0, 0],
                'BrawlerID': [int(offer_data[5]), 0, 0],
                'SkinID': [int(offer_data[6]), 0, 0],
                'WhoBuyed': [],
                'Timer': 86400,
                'OfferBGR': offer_data[7],
                'ShopType': int(offer_data[8]),  # Expecting integer
                'ShopDisplay': int(offer_data[9])
            }
        except ValueError as e:
            bot.reply_to(message, f'Ошибка при вводе данных: {e}')
            return

        # Attempt to read and write the offers file
        try:
            with open('Logic/offers.json', 'r', encoding='utf-8') as f:
                offers = json.load(f)
            offers[str(len(offers))] = new_offer
            
            with open('Logic/offers.json', 'w', encoding='utf-8') as f:
                json.dump(offers, f, indent=4)

            bot.reply_to(message, '✅ Новая акция успешно добавлена!')
        
        except PermissionError:
            bot.reply_to(message, "❌ У меня нет прав для записи в файл offers.json. Пожалуйста, проверьте права доступа.")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['rename'])
def change_name(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "❌ Правильное использование /rename [id] [new name]")
        else:
            user_id = message.from_user.id
            id = message.text.split()[1]
            ammount = message.text.split()[2]
            conn = sqlite3.connect("database/Player/plr.db")
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET name = ? WHERE lowID = ?", (ammount, id))
            conn.commit()
            conn.close()
            bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку c айди {id} изменили имя на {ammount}.")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['remove_offer'])
def remove_offer(message):
    user_id = message.from_user.id
    if user_id in admins:
    	if len(message.text.split()) != 2:
    	   bot.reply_to(message, 'Используйте команду /remove_offer с аргументом в формате: /remove_offer <ID>')
    	   return
    	offer_id = message.text.split()[1]
    	with open('Logic/offers.json', 'r', encoding='utf-8') as f:
    		offers = json.load(f)
    	if offer_id not in offers:
    		bot.reply_to(message, f'❌ Акция с ID {offer_id} не найдена')
    		return
    	offers.pop(offer_id)
    	with open('Logic/offers.json', 'w', encoding='utf-8') as f:
    		json.dump(offers, f)
    	bot.reply_to(message, f'✅ Акция с ID {offer_id} удалена')
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")
        
@bot.message_handler(commands=['theme'])
def theme(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Выбери ID темы\n0 - Обычная\n1 - Новый год (Снег)\n2 - Красный новый год\n3 - От клеш рояля\n4 - Обычный фон с дефолт музыкой\n5 - Желтые панды\n7 - Роботы Зелёный фон\n8 - Хэллуин 2019\n9 - Пиратский фон (Новый год 2020)\n10 - Фон с обновы с мистером п.\n11 - Футбольный фон\n12 - Годовщина Supercell\n13 - Базар Тары\n14 - Лето с монстрами\nИспользовать команду /theme ID")
        else:
            user_id = message.from_user.id
            theme_id = message.text.split()[1]
            conn = sqlite3.connect("database/Player/plr.db")
            c = conn.cursor()
            c.execute(f"UPDATE plrs SET theme={theme_id}")
            conn.commit()
            c.execute("SELECT * FROM plrs")
            conn.close()
            bot.send_message(chat_id=message.chat.id, text=f"✅ Айди всех записей был изменён на {theme_id}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")
        
@bot.message_handler(commands=['code'])
def new_code(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /code [new code](На англ)")
        else:
            code = message.text.split()[1]
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if code not in config["CCC"]:
                config["CCC"].append(code)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"✅ Новый код {code}, Был добавлен!")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"❌ Код {code} уже существует!")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['code_list'])
def code_list(message):
    with open('config.json', 'r') as f:
        data = json.load(f)
    code_list = '\n'.join(data["CCC"])
    bot.send_message(chat_id=message.chat.id, text=f"Список кодов: \n{code_list}")
    	
    	
@bot.message_handler(commands=['uncode'])
def del_code(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "❌ Правильное использование /uncode [code]")
        else:
            code = message.text.split()[1]
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if code in config["CCC"]:
                config["CCC"].remove(code)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"✅ Код {code}, Был удалён!")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"❌ Код {code} не найден!")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['code_info'])
def code_info(message):
    user_id = message.from_user.id
    if user_id not in admins and user_id not in tehs and user_id not in creator1 and user_id not in creator2 and user_id not in creator3:
        bot.reply_to(message, "❌ Вы не имеете доступ к данной команде!")
        return

    args = message.text.split()
    if len(args) != 2:
        bot.send_message(message.chat.id, "❌ Используйте команду в формате: /code_info [code]")
        return

    code = args[1]
    
    try:
        with open("config.json", "r", encoding='utf-8') as f:
            config = json.load(f)

        if code not in config["CCC"]:
            bot.send_message(message.chat.id, f"❌ Код {code} не найден.")
            return
        
        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()
            plr_cursor.execute("SELECT COUNT(*) FROM plrs WHERE SCC = ?", (code,))
            count = plr_cursor.fetchone()[0]

        if count > 0:
            bot.send_message(chat_id=message.chat.id, text=f"🔍 Код {code} используется {count} аккаунтами.")
        else:
            bot.send_message(chat_id=message.chat.id, text=f"❌ Код {code} не используется ни одним аккаунтом.")
    
    except FileNotFoundError:
        bot.send_message(message.chat.id, "❌ Файл конфигурации не найден.")
    except json.JSONDecodeError:
        bot.send_message(message.chat.id, "❌ Ошибка чтения конфигурации. Проверьте файл config.json.")
    except Exception as e:
        logger.error(f"Error in /code_info command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")

@bot.message_handler(commands=['vip'])
def add_vip(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in managers:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /vip [id]")
        else:
            vip_id = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if vip_id not in config["vips"]:
                config["vips"].append(vip_id)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"✅ Вип статус был выдан игроку с ID {vip_id}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"❌ Вип статус уже есть у ID {vip_id}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

		
@bot.message_handler(commands=['unvip'])
def del_vip(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in managers:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /unvip [id]")
        else:
            code = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if code in config["vips"]:
                config["vips"].remove(code)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"✅ Вип статус был удален у игрока с ID {code}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"❌ Вип статус не найден у игрока с ID {code}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")


@bot.message_handler(commands=['upshop'])
def auto_shop(message):
    user_id = message.from_user.id
    if user_id in managers  or user_id in admins or user_id in tehs:
        with open('Logic/offers.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        for i in range(12):
            if i <= 5:
                new_offer = {
                    'ID': [8, 0, 0],
                    'OfferTitle': "daily",
                    'Cost': random.randint(10, 228),
                    'OldCost': 0,
                    'Multiplier': [random.randint(1, 500), 0, 0],
                    'BrawlerID': [random.randint(1, 32), 0, 0],
                    'SkinID': [0, 0, 0],
                    'WhoBuyed': [],
                    'Timer': 86400,
                    'OfferBGR': "offer_gems",
                    'ShopType': 1,
                    'ShopDisplay': 1
                }
                rarity = random.choice(['common', 'rare', 'epic', 'legendary'])
                cost = random.randint(*get_price_range_by_rarity(rarity))
                new_offer['Cost'] = cost
                
                skin_id = random.choice(get_skin_ids_by_rarity(rarity))
                new_offer['SkinID'] = [skin_id, 0, 0]
                data[i] = new_offer
            elif i > 5:
                with open('config.json', 'r', encoding='utf-8') as f:
                    settings = json.load(f)
                skins = settings['Skinse']
                random_skin = random.choice(skins)
                settings['Skinse'] = skins
                with open('config.json', 'w', encoding='utf-8') as f:
                    json.dump(settings, f, indent=4, ensure_ascii=False)
                new_offer = {
                    'ID': [4, 0, 0],
                    'OfferTitle': "ЕЖЕДНЕВНЫЙ СКИН",
                    'Cost': 0,
                    'OldCost': 0,
                    'Multiplier': [0, 0, 0],
                    'BrawlerID': [0, 0, 0],
                    'SkinID': [random_skin, 0, 0],
                    'WhoBuyed': [],
                    'Timer': 86400,
                    'OfferBGR': "0",
                    'ShopType': 0,
                    'ShopDisplay': 0
                }
                rarity = random.choice(['common', 'rare', 'epic', 'legendary'])
                cost = random.randint(*get_price_range_by_rarity(rarity))
                new_offer['Cost'] = cost
                
                skin_id = random.choice(get_skin_ids_by_rarity(rarity))
                new_offer['SkinID'] = [skin_id, 0, 0]
                data[i] = new_offer
        with open('Logic/offers.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        bot.reply_to(message, '✅ Акции успешно обновлены!')
    else:
        bot.reply_to(message, "❌ У вас недостаточно прав!")
        
        
def get_skin_ids_by_rarity(rarity):
    skin_ids = {
        'common': [29, 15, 2, 103, 109, 167, 27, 120, 139, 111, 137, 152, 75],
        'rare': [25, 102, 58, 98, 28, 92, 158, 130, 88, 165, 93, 104, 132, 108, 45, 125, 117, 11, 126, 131, 20, 100],
        'epic': [52, 159, 79, 64, 44, 123, 163, 91, 57, 160, 99, 30, 128, 71, 59, 26, 68, 147, 50, 96, 110, 101, 118],
        'legendary': [94, 49, 95]
    }
    return skin_ids.get(rarity, [])  

def get_price_range_by_rarity(rarity):
    price_ranges = {
        'common': (29, 30),
        'rare': (79, 80),
        'epic': (149, 150),
        'legendary': (299, 300)
    }
    return price_ranges.get(rarity, (10, 20)) 
		
def is_numeric(value):
    return value.isdigit()

def validate_integer(value):
    try:
        int_value = int(value)
        if int_value <= 0:
            return False
        return True
    except ValueError:
        return False

@bot.message_handler(commands=['setgems'])
def set_gems(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in managers:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /setgems [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество гемов должно быть положительным числом!")
            return

        conn = sqlite3.connect("database/Player/plr.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE plrs SET gems = ? WHERE lowID = ?", (amount, id))
        conn.commit()
        conn.close()
        bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} установили {amount} гемов")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['addgems'])
def add_gems(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in managers:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /addgems [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество гемов должно быть положительным числом!")
            return

        conn = sqlite3.connect("database/Player/plr.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE plrs SET gems = gems + ? WHERE lowID = ?", (amount, id))
        conn.commit()
        conn.close()
        bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} добавлено {amount} гемов")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['ungems'])
def ungems(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in managers:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /ungems [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество гемов должно быть положительным числом!")
            return

        conn = sqlite3.connect("database/Player/plr.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE plrs SET gems = gems - ? WHERE lowID = ?", (amount, id))
        conn.commit()
        conn.close()
        bot.send_message(chat_id=message.chat.id, text=f"✅ У игрока с айди {id} убрано {amount} гемов")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")
        
def is_numeric(value):
    return value.isdigit()

def validate_integer(value, non_negative=False):
    try:
        int_value = int(value)
        if non_negative:
            return int_value >= 0
        return int_value > 0
    except ValueError:
        return False

@bot.message_handler(commands=['setgold'])
def set_gold(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /setgold [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount, non_negative=True):
            bot.reply_to(message, "❌ Количество золота должно быть числом >= 0!")
            return

        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET gold = ? WHERE lowID = ?", (amount, id))
            conn.commit()
        
        bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} установлено {amount} золота")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['addgold'])
def add_gold(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /addgold [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество золота должно быть числом > 0!")
            return

        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET gold = gold + ? WHERE lowID = ?", (amount, id))
            conn.commit()
        
        bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} добавлено {amount} золота")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['ungold'])
def un_gold(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /ungold [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество золота должно быть числом > 0!")
            return

        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET gold = gold - ? WHERE lowID = ?", (amount, id))
            conn.commit()
        
        bot.send_message(chat_id=message.chat.id, text=f"✅ У игрока с айди {id} убрано {amount} золота")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")
		
@bot.message_handler(commands=['settokens'])
def set_tokens(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in tehs: 
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /settokens [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount, non_negative=True):
            bot.reply_to(message, "❌ Количество токенов должно быть числом >= 0!")
            return

        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET BPTOKEN = ? WHERE lowID = ?", (amount, id))
            conn.commit()
        
        bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} установлены {amount} токенов")
    else:
        bot.reply_to(message, "❌ У вас нет прав на эту команду!")

@bot.message_handler(commands=['addtokens'])
def add_tokens(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in tehs: 
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /addtokens [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество токенов должно быть числом > 0!")
            return

        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET BPTOKEN = BPTOKEN + ? WHERE lowID = ?", (amount, id))
            conn.commit()
        
        bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} добавлено {amount} токенов")
    else:
        bot.reply_to(message, "❌ У вас нет прав на эту команду!")

@bot.message_handler(commands=['untokens'])
def un_tokens(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs or user_id in tehs: 
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /untokens [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество токенов должно быть числом > 0!")
            return

        with sqlite3.connect("database/Player/plr.db") as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE plrs SET BPTOKEN = BPTOKEN - ? WHERE lowID = ?", (amount, id))
            conn.commit()
        
        bot.send_message(chat_id=message.chat.id, text=f"✅ У игрока с айди {id} убрано {amount} токенов")
    else:
        bot.reply_to(message, "❌ У вас нет прав на эту команду!")
        
@bot.message_handler(commands=['ban'])
def ban(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /ban [id]")
        else:
            vip_id = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if vip_id not in config["banID"]:
                config["banID"].append(vip_id)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"✅ Бан был выдан игроку {vip_id}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"❌ Бан уже есть у игрока {vip_id}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['unban'])
def ban(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            bot.reply_to(message, "Правильное использование /unban [id]")
        else:
            vip_id = int(message.text.split()[1])
            with open("config.json", "r", encoding='utf-8') as f:
                config = json.load(f)
            if vip_id in config["banID"]:
                config["banID"].remove(vip_id)
                with open("config.json", "w", encoding='utf-8') as f:
                    json.dump(config, f, indent=4)
                bot.send_message(chat_id=message.chat.id, text=f"✅ Разбан был выдан игроку {vip_id}")
            else:
                bot.send_message(chat_id=message.chat.id, text=f"❌ У игрока {vip_id} отсутствует бан")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['unroom'])
def clear_room(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        if len(message.text.split()) < 2:
            user_id = message.from_user.id
            plrsinfo = "database/Player/plr.db"
            if os.path.exists(plrsinfo):
                conn = sqlite3.connect("database/Player/plr.db")
                c = conn.cursor()
                c.execute("UPDATE plrs SET roomID=0")
                c.execute("SELECT * FROM plrs")
                conn.commit()
                conn.close()
                bot.reply_to(message, '✅ Команды были очищены!')
            else:
                bot.reply_to(message, "❌ Вы не являетесь администратором!")

def is_numeric(value):
    return value.isdigit()

def validate_integer(value, non_negative=False):
    try:
        int_value = int(value)
        if non_negative:
            return int_value >= 0
        return int_value > 0
    except ValueError:
        return False

def is_numeric(value):
    """Check if the value is a numeric string."""
    return value.isdigit()

def validate_integer(value, non_negative=False):
    """Validate and convert a string to an integer, optionally enforcing non-negativity."""
    try:
        value = int(value)
        if non_negative and value < 0:
            return False
        return True
    except ValueError:
        return False

@bot.message_handler(commands=['settrophies'])
def set_trophies(message):
    user_id = message.from_user.id
    if user_id in admins:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /settrophies [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount, non_negative=True):
            bot.reply_to(message, "❌ Количество трофеев должно быть числом >= 0!")
            return

        amount = int(amount)

        try:
            with sqlite3.connect("database/Player/plr.db") as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE plrs SET trophies = ? WHERE lowID = ?", (amount, id))
                conn.commit()
            bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} установлено {amount} трофеев")
        except Exception as e:
            logger.error(f"Error in /settrophies command: {e}")
            bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['addtrophies'])
def add_trophies(message):
    user_id = message.from_user.id
    if user_id in admins:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /addtrophies [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество трофеев должно быть числом > 0!")
            return

        amount = int(amount)

        try:
            with sqlite3.connect("database/Player/plr.db") as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE plrs SET trophies = trophies + ? WHERE lowID = ?", (amount, id))
                conn.commit()
            bot.send_message(chat_id=message.chat.id, text=f"✅ Игроку с айди {id} добавлено {amount} трофеев")
        except Exception as e:
            logger.error(f"Error in /addtrophies command: {e}")
            bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

@bot.message_handler(commands=['untrophies'])
def remove_trophies(message):
    user_id = message.from_user.id
    if user_id in admins:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Правильное использование /untrophies [id] [amount]")
            return
        
        id, amount = parts[1], parts[2]

        if not is_numeric(id):
            bot.reply_to(message, "❌ ID должно быть числом!")
            return

        if not validate_integer(amount):
            bot.reply_to(message, "❌ Количество трофеев должно быть числом > 0!")
            return

        amount = int(amount)

        try:
            with sqlite3.connect("database/Player/plr.db") as conn:
                cursor = conn.cursor()
                cursor.execute("UPDATE plrs SET trophies = trophies - ? WHERE lowID = ?", (amount, id))
                conn.commit()
            bot.send_message(chat_id=message.chat.id, text=f"✅ У игрока с айди {id} убрано {amount} трофеев")
        except Exception as e:
            logger.error(f"Error in /untrophies command: {e}")
            bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")


@bot.message_handler(commands=['teh'])
def enable_maintenance(message):
    if is_admin(message.from_user.id):
        if update_maintenance_status(True):
            bot.reply_to(message, "✅ Технический перерыв был включен!")
        else:
            bot.reply_to(message, "❌ Произошла ошибка при включении технического перерыва.")
    else:
        bot.reply_to(message, "❌Вы не являетесь администратором!")

@bot.message_handler(commands=['unteh'])
def disable_maintenance(message):
    if is_admin(message.from_user.id):
        if update_maintenance_status(False):
            bot.reply_to(message, "✅ Технический перерыв был выключен!")
        else:
            bot.reply_to(message, "❌ Произошла ошибка при выключении технического перерыва.")
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")

def get_disk_usage():
    try:
        usage = psutil.disk_usage('/')
        return usage.percent // 100
    except Exception as e:
        return f"Error: {e}"

def get_ping(host='asuranodes.fun'):
    try:
        response_time = ping(host)
        if response_time is not None:
            inflated_ping = response_time * 1000
            return f"{inflated_ping:.2f}"
        else:
            return "Не удалось измерить"
    except Exception as e:
        return f"Error: {e}"

@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if user_id in admins or user_id in tehs:
        try:
            with open('config.json', 'r') as f:
                data = json.load(f)
                ban_list = len(data.get("banID", []))
                vip_list = len(data.get("vips", []))
        except FileNotFoundError:
            bot.reply_to(message, "❌ Файл конфигурации не найден.")
            return
        except json.JSONDecodeError:
            bot.reply_to(message, "❌ Ошибка чтения файла конфигурации.")
            return
        except Exception as e:
            bot.reply_to(message, f"❌ Произошла неожиданная ошибка: {e}")
            return

        try:
            player_list = len(dball())
        except Exception as e:
            player_list = f"Ошибка: {e}"

        ram_usage = psutil.virtual_memory().percent // 10
        cpu_usage = psutil.cpu_percent()
        disk_usage = get_disk_usage()
        ping_time = get_ping()

        status_message = (
            f'Всего создано аккаунтов: {player_list}\n'
            f'Игроков в бане: {ban_list}\n'
            f'Игроков с VIP: {vip_list}\n\n'
            f'RAM: {ram_usage}%\n'
            f'CPU: {cpu_usage}%\n'
            f'Диск: {disk_usage}%\n'
            f'Пинг: {ping_time} ms'
        )
        bot.reply_to(message, status_message)
    else:
        bot.reply_to(message, "❌ Вы не являетесь администратором!")
        
@bot.message_handler(commands=['resetclubs'])
def reset_clubs_command(message):
    if not is_admin(message.from_user.id):
        bot.send_message(message.chat.id, "❌ У вас нет прав для выполнения этой команды.")
        return

    try:
        with sqlite3.connect('database/Player/plr.db') as plr_conn:
            plr_cursor = plr_conn.cursor()

            plr_cursor.execute("UPDATE plrs SET ClubID = 0, ClubRole = 0")
            plr_conn.commit()

        club_files = ['database/Club/clubs.db', 'database/Club/chats.db']
        for file in club_files:
            if os.path.exists(file):
                os.remove(file)

        bot.send_message(message.chat.id, "✅ Данные клубов были успешно сброшены и файлы удалены.")
    except Exception as e:
        logger.error(f"Error in /resetclubs command: {e}")
        bot.send_message(message.chat.id, f"❌ Произошла ошибка: {str(e)}")
        
dbplayers = 'database/Player/plr.db'
dbclubs = 'database/Club/clubs.db'
dbchat = 'database/Club/chats.db'
        
@bot.message_handler(commands=['bd'])
def handle_bd_command(message):
    if not is_admin(message.from_user.id):
        bot.reply_to(message, "❌ Вы не имеете прав для выполнения этой команды.")
        return

    files = [dbplayers, dbclubs, dbchat]

    for file_path in files:
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                bot.send_document(chat_id=message.chat.id, document=file, caption=f'Файл: {os.path.basename(file_path)}')
        else:
            bot.reply_to(message, f"❌ Файл {os.path.basename(file_path)} не найден")

    bot.reply_to(message, "✅ Все доступные файлы отправлены в Telegram.")
    
@bot.message_handler(commands=['addcode'])
def new_code(message):
    user_id = message.from_user.id
    if user_id in creator2 or user_id in creator3:
        with sqlite3.connect('users.db') as users_conn:
            users_cursor = users_conn.cursor()
            users_cursor.execute("SELECT lowID FROM accountconnect WHERE id_user = ?", (user_id,))
            row = users_cursor.fetchone()

            if row:
                lowID = row[0]
                with sqlite3.connect('database/Player/plr.db') as plr_conn:
                    plr_cursor = plr_conn.cursor()
                    plr_cursor.execute("SELECT SCC FROM plrs WHERE lowID = ?", (lowID,))
                    code_row = plr_cursor.fetchone()

                    if code_row and code_row[0]:
                        bot.reply_to(message, "❌ Вы уже имеете код. Удалите его, прежде чем создать новый.")
                        return

                if len(message.text.split()) < 2:
                    bot.reply_to(message, "Правильное использование /code [new code](На англ)")
                else:
                    code = message.text.split()[1]
                    with open("config.json", "r", encoding='utf-8') as f:
                        config = json.load(f)
                    if code not in config["CCC"]:
                        config["CCC"].append(code)
                        with open("config.json", "w", encoding='utf-8') as f:
                            json.dump(config, f, indent=4)

                        plr_cursor.execute("UPDATE plrs SET SCC = ? WHERE lowID = ?", (code, lowID))
                        plr_conn.commit()

                        bot.send_message(chat_id=message.chat.id, text=f"✅ Новый код {code} был добавлен!")
                    else:
                        bot.send_message(chat_id=message.chat.id, text=f"❌ Код {code} уже существует!")
            else:
                bot.reply_to(message, "❌ Вы не привязали аккаунт. Используйте команду /connect.")
    else:
        bot.reply_to(message, "❌ Вы не являетесь контентмейкером!")


@bot.message_handler(commands=['event1'])
def event1(message: types.Message):
    user_id = message.from_user.id
    
    if not is_admin(user_id):
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return

    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, укажите 'true' или 'false'.")
        return

    value = message.text.split()[1].lower()

    if value == "true":
        EventSettings.set_double_trophies(True)
        bot.send_message(message.chat.id, "DOUBLE_TROPHIES установлено на True.")
    elif value == "false":
        EventSettings.set_double_trophies(False)
        bot.send_message(message.chat.id, "DOUBLE_TROPHIES установлено на False.")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, укажите 'true' или 'false'.")

    # Для отладки
    print("DOUBLE_TROPHIES:", EventSettings.get_double_trophies())

@bot.message_handler(commands=['event2'])
def event2(message: types.Message):
    user_id = message.from_user.id
    
    if not is_admin(user_id):
        bot.send_message(message.chat.id, "❌ Вы не являетесь администратором!")
        return

    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Пожалуйста, укажите 'true' или 'false'.")
        return

    value = message.text.split()[1].lower()

    if value == "true":
        EventSettings.set_double_tokens(True)
        bot.send_message(message.chat.id, "DOUBLE_TOKENS установлено на True.")
    elif value == "false":
        EventSettings.set_double_tokens(False)
        bot.send_message(message.chat.id, "DOUBLE_TOKENS установлено на False.")
    else:
        bot.send_message(message.chat.id, "Пожалуйста, укажите 'true' или 'false'.")

    # Проверка установленных значений
    print("DOUBLE_TOKENS:", EventSettings.get_double_tokens())
        
@bot.message_handler(commands=['delcode'])
def del_code(message):
    user_id = message.from_user.id
    if user_id in creator2 or user_id in creator3:
        with sqlite3.connect('users.db') as users_conn:
            users_cursor = users_conn.cursor()
            users_cursor.execute("SELECT lowID FROM accountconnect WHERE id_user = ?", (user_id,))
            row = users_cursor.fetchone()

            if row:
                lowID = row[0]
                with sqlite3.connect('database/Player/plr.db') as plr_conn:
                    plr_cursor = plr_conn.cursor()
                    plr_cursor.execute("SELECT SCC FROM plrs WHERE lowID = ?", (lowID,))
                    code_row = plr_cursor.fetchone()

                    if code_row and code_row[0]:
                        code = code_row[0]
                        with open("config.json", "r", encoding='utf-8') as f:
                            config = json.load(f)

                        if code in config["CCC"]:
                            config["CCC"].remove(code)
                            with open("config.json", "w", encoding='utf-8') as f:
                                json.dump(config, f, indent=4)

                            plr_cursor.execute("UPDATE plrs SET SCC = NULL WHERE lowID = ?", (lowID,))
                            plr_conn.commit()

                            bot.send_message(chat_id=message.chat.id, text=f"✅ Код {code} был удалён!")
                        else:
                            bot.send_message(chat_id=message.chat.id, text="❌ Код не найден!")
                    else:
                        bot.send_message(chat_id=message.chat.id, text="❌ У вас нет кода для удаления.")
            else:
                bot.reply_to(message, "❌ Вы не привязали аккаунт. Используйте команду /connect.")
    else:
        bot.reply_to(message, "❌ Вы не являетесь контентмейкером!")
    
bot.polling(none_stop=True, interval=2)