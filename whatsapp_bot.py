import pyautogui as pt
import pyperclip as pc
from pynput.mouse import Controller, Button
from time import sleep
from whatsapp_responses import response

mouse = Controller()
pt.FAILSAFE = True

# arahan untuk whatsapp bot
class WhatsApp:

    def __init__(self, speed=.7, click_speed=.9):
        self.speed = speed
        self.click_speed = click_speed
        self.message = ''
        self.last_message = ''

    # Mengetahui apakah ada pesan masuk atau tidak
    def check_green_dot(self) :
        global green
        position = pt.locateOnScreen('img/hijau.png', confidence=.75)
        if position == None : green = False
        else : green = True
           
    # fungsi untuk menempatkan kursor ke grup yg disematkan jika tidak ada pesan
    def nav_group(self) :
        try :
            position = pt.locateOnScreen('img/sematkan.png', confidence=.8)
            pt.moveTo(position[0:2], duration=.1)
            pt.moveRel(-100, 0, duration=.1)
            pt.doubleClick(interval=.3)
        except Exception as e :
            print('Exception (nav_group) : ', e)

    # Fungsi untuk ke new message yg ditanddai dengan adanya titik hijau
    def nav_green_dot(self):
        try:
            position = pt.locateOnScreen('img/hijau.png', confidence=.75)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-100, 0, duration=self.speed)
            pt.doubleClick(interval=self.click_speed)
        except Exception as e:
            print('Exception (nav_green_dot): ', e)


    # Fungsi agar kursor mengarah ke pesan yg akan di respon
    def nav_message(self):
        try:
            position = pt.locateOnScreen('img/klip.png', confidence=.7)
            pt.moveTo(position[0:2], duration=self.speed)
            pt.moveRel(-10, -50, duration=self.speed)  # Ubah x,y nya jika mousenya kurang tepat
        except Exception as e:
            print('Exception (nav_message): ', e)

    # Fungsi untuk mendapatkan / copy isi pesan
    def get_message(self):
        mouse.click(Button.left, 3)
        sleep(self.speed)
        mouse.click(Button.right, 1)
        sleep(self.speed)
        pt.moveRel(10, 5, duration=self.speed)  # x,y nya harus sesuaikan dengan letak "copy" pada device kalian
        mouse.click(Button.left, 1)
        sleep(1)

        # pesan ditempel pada sistem kemudian di proses
        self.message = pc.paste()
        print('Pesan dia : ', self.message)

    # Mengirim pesan yg sudah di proses
    def send_message(self):
        try:
        # Mengecek apakah message nya sama 
            if self.message != self.last_message: 
                # eksekusi jika message nya beda
                bot_response = response(self.message)
                print('Pesan bot : ', bot_response)
                pt.typewrite(bot_response)
                pt.typewrite('\n')  # Mengirim pesan
                # menetapkan message barusan sebagai message yg sama
                self.last_message = self.message
            else:
                # tidak akan mengirim message karena message yg di copy sama dengan message yg terakhir di proses
                print('No new messages...')

        except Exception as e:
            print('Exception (send_message): ', e)


# Inisialisasi wa_bot sebagai class di atas
wa_bot = WhatsApp(speed=.3, click_speed=.5)

# Menjalankan program dalam looping / perulangan
while True :
    wa_bot.check_green_dot()
    while green == True :
        print(green)
        wa_bot.nav_green_dot()
        wa_bot.nav_message()
        wa_bot.get_message()
        wa_bot.send_message()
        wa_bot.check_green_dot()
    while green == False :
        print(green)
        wa_bot.nav_group()
        wa_bot.check_green_dot()
        
        sleep(4)