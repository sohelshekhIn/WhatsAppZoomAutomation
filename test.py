# arrays = ["hello", "kemcho", "majama"]
# for i in range(len(arrays)):
#     name = arrays[i]
#     print(name)

import pyautogui
import os
import time
import datetime

# time.sleep(10)
# pyautogui.keyDown('altleft')
# pyautogui.keyDown('f4')
# pyautogui.keyUp('altleft')
# pyautogui.keyUp('f4')
# print(isinstance(datetime.datetime.now().strftime("%H:%M"),int))
# print(isinstance(datetime.datetime.now().strftime("%H:%M"),str))
meetingStart = ["8", "4","9","10","10","00"]

meetingStart = ["8:04","9:10","10:00"]
# i = 1
# while i > 2:
timeH = datetime.datetime.now().strftime("%H")
timeM = datetime.datetime.now().strftime("%M")
time = datetime.datetime.now().strftime("%H:%M")

if int(time) >= meetingStart[0]:
    timeId = 0
elif time >= meetingStart[1]:
    timeId = 1
elif time >= meetingStart[2]:
    timeId = 2

print(time)
print(timeId)
print(isinstance(meetingStart[0],int))
print(isinstance(meetingStart[0],str))