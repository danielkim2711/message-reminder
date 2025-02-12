import time
import pyautogui
import schedule
import pandas as pd
from datetime import datetime
import pyperclip
import sys

def get_today_message():
    df = pd.read_csv('messages.csv')
    today = datetime.today().strftime('%Y-%m-%d')
    message_row = df[df['date'] == today]
    return message_row['message'].values[0] if not message_row.empty else '오늘의 메시지가 없습니다.'

def send_message():
    message = get_today_message()
    pyperclip.copy(message)

    pyautogui.click(x=945, y=373)
    pyautogui.press('enter')

    time.sleep(5)

    pyautogui.keyDown('command')
    pyautogui.keyDown('v')
    pyautogui.keyUp('v')
    pyautogui.keyUp('command')

    print(message)
    pyautogui.press('enter')
    pyautogui.keyDown('command')
    pyautogui.keyDown('q')
    pyautogui.keyUp('q')
    pyautogui.keyUp('command')
    print('Done!')

    sys.exit()

# print(pyautogui.position())

# schedule.every().day.at('07:00').do(send_message)
schedule.every(1).minutes.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)
