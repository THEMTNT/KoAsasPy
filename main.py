import time
import os
from pynput import mouse, keyboard
import ctypes
import pyautogui
import keyboard as kb
from colorama import Fore

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

os.system("color 2")
skill_flag = False  # global skill_flag değişkeni


def minor():
    keyboard_controller.press('7')
    time.sleep(0.01)
    keyboard_controller.release('7')
    keyboard_controller.press('8')
    time.sleep(0.01)
    keyboard_controller.release('8')


def cure():
    global skill_flag
    keyboard_controller.press(keyboard.Key.f3)
    time.sleep(0.01)
    keyboard_controller.release(keyboard.Key.f3)
    keyboard_controller.press('3')
    time.sleep(0.01)
    keyboard_controller.release('3')


def rkey(key):
    keyboard_controller.press(key)
    time.sleep(0.01)
    keyboard_controller.release(key)
    keyboard_controller.press('r')
    time.sleep(0.01)
    keyboard_controller.release('r')
    keyboard_controller.press('r')
    time.sleep(0.01)
    keyboard_controller.release('r')
    keyboard_controller.release(key)


def skill(key):
    global skill_flag
    if caps_lock_state() == 1:

        try:
            if key.char == '3' and not skill_flag:
                skill_flag = True
                rkey('3')
            if key.char == '4' and not skill_flag:
                skill_flag = True
                rkey('4')
            if key.char == '5' and not skill_flag:
                skill_flag = True
                rkey('5')
            if key.char == '6' and not skill_flag:
                skill_flag = True
                rkey('6')
            if key.char == 'v' and not skill_flag:
                skill_flag = True
                cure()

        except AttributeError:
            pass


def on_click(x, y, button, pressed):
    if button == mouse.Button.right and caps_lock_state() == 1:
        minor()


def on_press(key):
    skill(key)


def on_release(key):
    global skill_flag
    if key == keyboard.Key.f3:
        skill_flag = True
    else:
        skill_flag = False  # skill_flag değişkenini False olarak ayarla
    pass


def barkordinatal(yazi):
    print("{} barının hangi noktasından koordinat almak istiyorsanız imleci oraya götürüp 'k' tuşuna basınız.".format(
        yazi))
    while True:
        if kb.is_pressed('k'):
            x, y = pyautogui.position()
            print("{} bar koordinatları alındı.".format(yazi))
            return x, y
            break
        else:
            pass


def otominorsor():
    print("Otomatik can ve mana degeri okutup minor ve mana basmasini istiyormusunuz?")
    print(
        "Evet dediginiz taktirde can ve mana barindan basmasini istediginiz noktanin pixelini okutmaniz istenecektir.")
    a = input("E/H\n")
    if a == 'e' or a == 'E':
        return True
    else:
        return False


def canminorbas():
    global hpx, hpy, mpx, mpy
    canr, cang, canb, = pyautogui.pixel(hpx, hpy)
    manar, manag, manab = pyautogui.pixel(mpx, mpy)

    if canr < 10:
        minor()
        
    if manab < 10:
        keyboard_controller.press('2')
        time.sleep(0.01)
        keyboard_controller.release('2')


def caps_lock_state():
    hllDll = ctypes.WinDLL("User32.dll")
    VK_CAPITAL = 0x14
    return hllDll.GetKeyState(VK_CAPITAL)


def bilgilendirme():
    print(
        "Asas Makro Programi\n________________________________________________________________________________________________\n1-Light Feet\n2-Mana Potion\n3-Skill\n4-Skill\n5-Skill\n6-Skill\n7-Minor\n8-Minor\nF3(3)-Cure\n________________________________________________________________________________________________\nKullanimi:\n3-4-5-6 tuslarina bastiginizda extradan rr atar(3 e bastiginizda 3rr gibi)\nMouse sag tusa bastiginizda 7878 basar.\nV tusuna bastiginizda ise cure icin f3-3 tusuna basar.\n________________________________________________________________________________________________\nCapslock tusu aktif oldugunda bot aktif pasif oldugunda bot pasif olur.")


listener_keyboard = keyboard.Listener(on_press=on_press, on_release=on_release)

listener_mouse = mouse.Listener(on_click=on_click)

listener_keyboard.start()
listener_mouse.start()

secim = otominorsor()
if secim:
    hpx, hpy = barkordinatal("HP")
    time.sleep(1)
    mpx, mpy = barkordinatal("MP")
else:
    pass
os.system('cls')
bilgilendirme()

while True:
    if caps_lock_state() == 1:
        print(Fore.GREEN + "Bot Aktif...", end="\r")
        if secim:
            canminorbas()
        else:
            pass
    else:
        print(Fore.RED + "Bot Pasif...", end="\r")
        time.sleep(1)

listener_mouse.join()
listener_keyboard.join()
