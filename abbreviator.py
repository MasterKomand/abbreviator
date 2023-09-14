#3д надписи

error_title = """
███████╗██████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
█████╗░░██████╔╝██████╔╝██║░░██║██████╔╝
██╔══╝░░██╔══██╗██╔══██╗██║░░██║██╔══██╗
███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝
"""

title_title = """
░█████╗░██████╗░██████╗░██████╗░███████╗██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
███████║██████╦╝██████╦╝██████╔╝█████╗░░╚██╗░██╔╝██║███████║░░░██║░░░██║░░██║██████╔╝
██╔══██║██╔══██╗██╔══██╗██╔══██╗██╔══╝░░░╚████╔╝░██║██╔══██║░░░██║░░░██║░░██║██╔══██╗
██║░░██║██████╦╝██████╦╝██║░░██║███████╗░░╚██╔╝░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
╚═╝░░╚═╝╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
"""

loading_loading = """
██╗░░░░░░█████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
██║░░░░░██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
██║░░░░░██║░░██║███████║██║░░██║██║██╔██╗██║██║░░██╗░
██║░░░░░██║░░██║██╔══██║██║░░██║██║██║╚████║██║░░╚██╗
███████╗╚█████╔╝██║░░██║██████╔╝██║██║░╚███║╚██████╔╝
╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░
"""

loading_success = """
░██████╗██╗░░░██╗░█████╗░░█████╗░███████╗░██████╗░██████╗
██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░██║░░░██║██║░░╚═╝██║░░╚═╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██║░░░██║██║░░██╗██║░░██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝╚██████╔╝╚█████╔╝╚█████╔╝███████╗██████╔╝██████╔╝
╚═════╝░░╚═════╝░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═════╝░
"""

#основной код

print(loading_loading)

try:
    from platform import platform
except:
    try:
        os.system("pip install platform")
    except:
        os.system("pip3 install platform")
    from platform import platform
puk = platform()[0], platform()[1], platform()[2], platform()[3], platform()[4], platform()[5], platform()[6]
if puk == ('W', 'i', 'n', 'd', 'o', 'w', 's'):
    delet = 'cls'
    dr = '\\'
else:
    delet = 'clear'
    dr = '/'
import os
import time
try:
    import requests
except:
    try:
        os.system('pip install requests')
    except:
        os.system('pip install requests')
    import requests
try:
    import pyshorteners
except:
    os.system('pip install pyshorteners')

#функции

def error(text):
    os.system(delet)
    print(error_title)
    print(text)
    time.sleep(3)
    start()

def title():
    os.system(delet)
    print(title_title)

try:
    test_connect = requests.get('https://www.google.com/')
    programm_continue = True
    os.system(delet)
    print(loading_success)
    time.sleep(3)
except:
    programm_continue = False

if programm_continue == True:
    #menu

    menu1 = '1: Сократить ссылку'
    menu2 = '2: Об утилиты'

    #short

    short = pyshorteners.Shortener()

    #функция старта

    def start():
        title()
        print(menu1)
        print(menu2)
        try:
            test_menu = int(input('\nВаш выбор: '))
            title()
            if test_menu == 1:
                print('Вам нужно ввести ссылку чтобы её скрыть, но проверьте её на достоверность и правильно введите!\n')
                url = input('Введите ссылку: ')
                os.system(delet)
                print(loading_loading)
                print('Генерация ссылки..')
                try:
                    url_generated = short.clckru.short(url)
                    os.system(delet)
                    print(loading_success)
                    print('Ссылка сгенерировалась!')
                    time.sleep(3)
                    title()
                    print(f'Ваша ссылка: {url_generated}\n')
                    input('Нажмите "enter"!')
                    start()
                except:
                    error('Неизвестная ошибка!')
            else:
                if test_menu == 2:
                    title()
                    print('Сделано командой: HackerRullerTools!\nДля скрытия зловредных ссылок!\nПрисоединяйтесь к нам!\n')
                    input('Нажмите "enter"!')
                    start()
                else:
                    error('Ваш выбор неккоректный!')
        except ValueError:
            error('Ваш выбор неккоректный!')

    #начало

    start()
else:
    os.system(delet)
    print(error_title)
    print('Проверьте интернет соединение!')
    time.sleep(3)
