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

# SubjectCode = {
#   "maths":{
#     "id":"4351864441",
#     "pass":"4441"
#   },
#   "hindi":{
#     "id":"9729663083",
#     "pass":"123456"
#   },
#   "pe":{
#     "id":"3020221759",
#     "pass":"12345"
#   },
#   "it":{
#     "id":"2298966093",
#     "pass":"150620"
#   },
#   "english":{
#     "lr":{
#       "id":"3335982496",
#       "pass":"434241"
#     },
#     "gr":{
#       "id":"7155941385",
#       "pass":"978714"
#     }

#   },
#   "ss":{
#     "ks":{
#       "id":"2086408197",
#       "pass":"208208"
#     },
#     "geo":{
#       "id":"2932997323",
#       "pass":"860837"
#     }
#   },
#     "sci_sm":{
#       "id":"8975302030",
#       "pass":"286080"
#     },
#   "sci_am":{
#     "id":"8011052266",
#     "pass":"226476"
#     }
  
# }

# print(SubjectCode["it"]["id"])

# no_lectures = input("No. of lect: ")
# lect =  []

# for i in range(int(no_lectures)):
#   lect.append(input("Lecture "+ str(i+1) + ": "))

# print(lect.)



# import pickle

# setUPData = pickle.load(open("data.dat", "rb"))

# if setUPData == "INITIALIZE":
#     setup = input("Done: ")
#     if setup == "hello":

#         pickle.dump("INITIALIZED", open("data.dat", "wb"))
# else:
#     print("Setup already done")
SubjectCode = {
  "maths": {
    "id": "4351864441",
    "pass": "4441"
  },
  "hindi": {
    "id": "9729663083",
    "pass": "123456"
  },
  "pe": {
    "id": "3020221759",
    "pass": "12345"
  },
  "it": {
    "id": "2298966093",
    "pass": "150620"
  },
  "eng_lr": {
    "id": "3335982496",
    "pass": "434241"
  },
  "eng_gr": {
    "id": "7155941385",
    "pass": "978714"
  },
  "ss_ks": {
    "id": "2086408197",
    "pass": "208208"
  },
  "ss_geo": {
    "id": "2932997323",
    "pass": "860837"
  },
  "sci_sm": {
    "id": "8975302030",
    "pass": "286080"
  },
  "sci_am": {
    "id": "8011052266",
    "pass": "226476"
  }
}
lect = []

# for ii in range(len(SubjectCode)):
#     pass


print(SubjectCode.items()["pt"])

# def LectureToId(lectures):
#   for i in range(len(lectures)):
#     for ii in range(len(SubjectCode)):
#       if lectures[i] in SubjectCode[ii]:
#         print(SubjectCode[ii],SubjectCode[ii][id])


# no_lectures = input("number of lectures: ")
# for i in range(int(no_lectures)):
#   lect.append(input("Lecture "+ str(i+1) + ": "))
   

# LectureToId(lect)
