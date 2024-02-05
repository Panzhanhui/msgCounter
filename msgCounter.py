import os
import re
import sys
import threading
import time
import pyperclip
import keyboard


def readMsg():
    global queue
    queue = []

    b = 'Blessings2.txt'
    if not os.path.exists(b):
        with open(b, 'w'):
            pass
    with open(b, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # 按行读取文件内容
        if not lines:
            print('empty>>>>>>fill')
            sys.exit()

        for line in lines:
            if not line:
                continue
            # 打印每一行（去除行末换行符）
            queue.append(re.sub(r'[\d+\.]?', '',  line.strip()))
    return queue


def sendMsg():
    global queue
    queue = readMsg()
    for _ in queue:
        pyperclip.copy(queue.pop(0))
        time.sleep(1)
        keyboard.press_and_release('ctrl+v')
        time.sleep(1)
        keyboard.press_and_release('enter')


def heart_beat():
    # 打印当前时间

    # print(time.strftime('%Y-%m-%d %H:%M:%S'))
    sendMsg()
    keyboard.on_press_key("esc", on_esc_pressed)
    # 每隔3秒执行一次
    threading.Timer(1*30, heart_beat).start()

def on_esc_pressed(event):
        sys.exit()



# 保持程序运行，直到按下 Ctrl+C 终止程序


time.sleep(5)
heart_beat()
