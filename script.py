import os
import pyautogui
import win32gui
import keyboard
from pynput.keyboard import Key, Controller
import time
from datetime import date

today = date.today()
d1 = today.strftime("%d/%m/%Y")
today = d1.split("/")
for i in range(3): today[i] = int(today[i])
print(today)

def compare_date(d1, d2):
    if (d1[1] < d2[1]): return 1
    if (d1[0] < d2[0] and d1[1] == d2[1]): return 1
    return 0

def diff_dates(date, today):         # две даты сегодня и заданная возвращает примерное кол-во разницу
    if (date[1] == today[1]): return today[0] - date[0]
    if (today[1] - date[1] == 1): return today[0] + (30 - date[0])
    return 99

def swap(list):
    list[0] = int(list[0]) + int(list[1])
    list[1] = int(list[0]) - int(list[1])
    list[0] = int(list[0]) - int(list[1])
    list[2] = int(list[2])
    return list

f = open('C:\\Users\\Hola\\Desktop\\dm_updated\\server_csgo\\csgo\\addons\\sourcemod\\logs\\DropsSummoner.log', 'r', encoding="utf8")

def convertid(Z,Y):
    V = int(0x0110000100000000)
    return Z*2+V+Y

base = []
new = []

for line in f:
     line1 = line.split()
     line_data = line1[1].split("/")      #сплитанул дату
     line_data = swap(line_data)         #привел к нужному формату
     #print(line)
     if(line_data[2] == today[2]):                                        #выборка за этот и предыдущий месяцы
         if(line_data[1] == today[1] or today[1] - line_data[1] == 1):
             id = line.split("<")
             id = id[2].split(">")[0]
             id = convertid(int(id.split(":")[2]),int(id.split(":")[1])) #получаем стим айди
             #nickname = line[6].split("<")[0]
             base.append([line_data, id, line])



for i in range(len(base)):
     curr_id = base[i]
     #last_one_curr = curr_id
     for n in range(i + 1, len(base)):
         if (base[i][1] == base[n][1]):
             if compare_date(curr_id[0],base[n][0]):
                 #last_one_curr = curr_id
                 curr_id = base[n]
     if (diff_dates(curr_id[0], today) > 6):
        new.append(curr_id)
        #print(curr_id[1], curr_id[0])#,curr_id[0][0] - last_one_curr[0][0])

for i in range(len(new)):
    check_id = int(new[i][1])
    if (check_id == 76561199025649361): print("1")
    if (check_id == 76561198262294780): print("2")
    if (check_id == 76561198016392117): print("3")
    if (check_id == 76561199367207668): print("4")
    if (check_id == 76561199418119727): print("5")
    if (check_id == 76561199366941057): print("6")
    if (check_id == 76561198800853604): print("7")
    if (check_id == 76561199057968797): print("8")
    if (check_id == 76561198180975669): print("9")
    if (check_id == 76561199083003372): print("10")
    if (check_id == 76561198953823219): print("11")
    if (check_id == 76561199081644264): print("12")

    if (check_id == 76561198186608538): print("1")
    if (check_id == 76561199089815217): print("2")
    if (check_id == 76561199362521587): print("3")
    if (check_id == 76561199362145959): print("4")
    if (check_id == 76561199415714391): print("5")
    if (check_id == 76561199023579787): print("6")
    if (check_id == 76561198423739829): print("7")
    if (check_id == 76561199120964798): print("8")
    if (check_id == 76561198096955499): print("9")
    if (check_id == 76561199075845483): print("10")
    if (check_id == 76561198863848648): print("11")
    if (check_id == 76561199016555750): print("12")


