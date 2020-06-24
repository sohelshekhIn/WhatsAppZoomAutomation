# # arrays = ["hello", "kemcho", "majama"]
# # for i in range(len(arrays)):
# #     name = arrays[i]
# #     print(name)

# import pyautogui
# import os
# import time
# import datetime

# # time.sleep(10)
# # pyautogui.keyDown('altleft')
# # pyautogui.keyDown('f4')
# # pyautogui.keyUp('altleft')
# # pyautogui.keyUp('f4')
# # print(isinstance(datetime.datetime.now().strftime("%H:%M"),int))
# # print(isinstance(datetime.datetime.now().strftime("%H:%M"),str))
# meetingStart = ["8", "29","9","10","10","00"]

# # meetingStart = ["8:04","9:10","10:00"]
# # i = 1
# status = True
# while status:
#     timeH = int(datetime.datetime.now().strftime("%H"))
#     timeM = int(datetime.datetime.now().strftime("%M"))
#     time = datetime.datetime.now().strftime("%H:%M")

#     if int(timeH) >=  int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
#         timeId = 0
#         print(time)
#         status = False

#     elif int(timeH) >=  int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
#         timeId = 1
#         print(time)
#         status = False

#     elif int(timeH) >=  int(meetingStart[4]) and int(timeM) >= int(meetingStart[5]):
#         timeId = 2
#         print(time)
#         status = False

# # print(time)
# # print(timeId)
# # print(isinstance(meetingStart[0],int))
# # print(isinstance(meetingStart[0],str))

# def hello():
#     print("Hello")
#     def start():
#         print("Start")


import sys
print(sys.getrecursionlimit())
