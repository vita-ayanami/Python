#ПОДКЮЧАЕМ БИБЛИОТЕКИ, НЕОБХОДИМЫЕ ДЛЯ РАБОТЫ.
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="your_token")
session_api = vk_session.get_api()
longpool = VkLongPoll(vk_session)

#СОЗДАНА ФУНКЦИЯ ДЛЯ ОБРАБОТКИ СООБЩЕНИЙ ПОЛЬЗОВАТЕЛЯ И ОТВЕТА БОТА НА НИХ.
def send_some_msg(id, some_text):
    vk_session.method("messages.send", {"user_id":id, "message":some_text,"random_id":0})
#УЧАСТОК КОДА, РЕАЛИЗУЮЩИЙ КОМАНДУ "ПОМОЩЬ".
for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg = event.text.upper().lower().title()
            id = event.user_id
            if msg == "/Помощь":
                send_some_msg(id, "/пис - проверяет размер члена")

#УЧАСТОК КОДА, РЕАЛИЗУЮЩИЙ, БЕЗ ПРЕУВЕЛЕЧЕНИЯ, САМУЮ НУЖНУЮ КОМАНДУ БОТА - РАЗМЕР ЧЛЕНА.
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            msg2 = event.text.upper().lower().title()
            id = event.user_id
            if msg2 == "/Пис":
                A = random.randint(0, 200)
                send_some_msg(id, "Размер твоего члена: " + str(A) + " сантиметров!")