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
# print(setUPData)

# if setUPData == "INITIALIZE":
#     setup = input("Done: ")
#     if setup == "hello":

# pickle.dump("INITIALIZE", open("data.dat", "wb"))
# else:
#     print("Setup already done")
# SubjectCode = {
#   "maths": {
#     "id": "4351864441",
#     "pass": "4441"
#   },
#   "hindi": {
#     "id": "9729663083",
#     "pass": "123456"
#   },
#   "pe": {
#     "id": "3020221759",
#     "pass": "12345"
#   },
#   "it": {
#     "id": "2298966093",
#     "pass": "150620"
#   },
#   "eng_lr": {
#     "id": "3335982496",
#     "pass": "434241"
#   },
#   "eng_gr": {
#     "id": "7155941385",
#     "pass": "978714"
#   },
#   "ss_ks": {
#     "id": "2086408197",
#     "pass": "208208"
#   },
#   "ss_geo": {
#     "id": "2932997323",
#     "pass": "860837"
#   },
#   "sci_sm": {
#     "id": "8975302030",
#     "pass": "286080"
#   },
#   "sci_am": {
#     "id": "8011052266",
#     "pass": "226476"
#   }
# }
# lect = []
# meetingId = []
# meetingPass = []
# pos = ""







# lectureSubjject = ["maths", "hindi", "pe", "it", "eng_lr", "eng_gr", "ss_ks", "ss_geo", "sci_sm", "sci_am"]
# lectureMeetingId = ["4351864441", "9729663083", "3020221759", "2298966093", "3335982496", "7155941385","2086408197", "2932997323","8975302030","8011052266"]
# lectureMeetingPass = ["4441","123456","12345","150620","434241","978714","208208","860837","286080","226476"]

# def LectureToId(lectures):
#     if lectures[i].lower() in "english":
#         lastDigit = input("Enter first three digit of English's Meeting Id: ")
#         if lastDigit in "333":
#             meetingId.append(lectureMeetingId[4])
#             meetingPass.append(lectureMeetingPass[4])             
#         elif lastDigit in "715":
#             meetingId.append(lectureMeetingId[5])
#             meetingPass.append(lectureMeetingPass[5])
#     elif lectures[i].lower() in "science":
#         lastDigit = input("Enter first three digit of Science's Meeting Id: ")
#         if lastDigit in "897":
#             meetingId.append(lectureMeetingId[10])
#             meetingPass.append(lectureMeetingPass[10])
#         elif lastDigit in "801":
#             meetingId.append(lectureMeetingId[11])
#             meetingPass.append(lectureMeetingPass[11])
#     elif lectures[i].lower() in "ss":
#         lastDigit = input("Enter first three digit of S.S's Meeting Id: ")
#         if lastDigit in "208":
#             meetingId.append(lectureMeetingId[8])
#             meetingPass.append(lectureMeetingPass[8])
#         elif lastDigit in "293":
#             meetingId.append(lectureMeetingId[9])
#             meetingPass.append(lectureMeetingPass[9])
#     elif lectures[i].lower() in "hindi":
#         meetingId.append(lectureMeetingId[1])
#         meetingPass.append(lectureMeetingPass[1])
#     elif lectures[i].lower() in "maths":
#         meetingId.append(lectureMeetingId[0])
#         meetingPass.append(lectureMeetingPass[0])
#     elif lectures[i].lower() in "pe":
#         meetingId.append(lectureMeetingId[2])
#         meetingPass.append(lectureMeetingPass[2])
#     elif lectures[i].lower() in "it":
#         meetingId.append(lectureMeetingId[3])
#         meetingPass.append(lectureMeetingPass[3])
#     else:
#         print("Enter valid answer!")



# no_lectures = input("Number of lectures: ")
# for i in range(int(no_lectures)):
#     if i+1 == 1:
#       pos = "st"
#     elif i+1 == 2:
#       pos = "nd"
#     elif i+1 == 3:
#       pos = "rd"
#     elif i+1 == 4:
#         pos = "rth"

#     lect.append(input(str(i+1) + pos + " lecture: ")) 
#     LectureToId(lect)


# print(meetingId,meetingPass)

# "C:\\Users\\sohel\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
# response = input("Enter: ")
# response.replace("\", "\\")
# print(response)
zoom_path = "C:\\Users\\sohel\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"

print("")
print("Initializing setup")
print("")
print("")
print("Refer documentation in GitHub")
print("")
print("")
print("Search for the file in your system with your user! (in double backward slaches): ")
print(zoom_path)
pathO = input("Enter app location of zoom:")
print(pathO)
print("")
print("Ending Initialize...")
pickle.dump(pathO, open("data.dat", "wb"))
zoom_path = pathO