import os
import time
import pickle
import atexit
import psutil
import datetime
import pyautogui
zoom_path = "C:\\Users\\sohel\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
setUpStatus = pickle.load(open("data.dat", "rb"))

if setUpStatus == "INITIALIZE":
    print("")
    print("Initializing setup")
    time.sleep(2)
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1.5)
    print("...")
    time.sleep(1.5)
    print("Refer documentation in GitHub")
    print(".")
    time.sleep(3)
    print(".")
    time.sleep(3)
    print("Search for the file in your system with your user! (in double backward slaches): ")
    time.sleep(2)
    print(zoom_path)
    time.sleep(3)
    pathO = input("Enter app location of zoom:")
    print(pathO)
    print("")
    time.sleep(3)
    print("Ending Initialize...")
    pickle.dump("INITIALIZED", open("data.dat", "wb"))
    pickle.dump(pathO, open("zoom.dat", "wb"))
    zoom_path = pathO


try:
    zoPath = pickle.load(open("zoom.dat", "rb"))
    zoom_path = zoPath
    print("")
    print("Please Wait...")
    print("")
except FileNotFoundError:
    print("")
    print("Error zoom.dat file not found, re-install it from GitHub to solve issue!")
    print("")
    print("Exiting...")
    os._exit(0)


lect = []
meetingId = []
meetingPass = []


lectureSubjject = ["maths", "hindi", "pe", "it", "eng_lr",
                   "eng_gr", "ss_ks", "ss_geo", "sci_sm", "sci_am"]
lectureMeetingId = ["4351864441", "9729663083", "3020221759", "2298966093",
                    "3335982496", "7155941385", "2086408197", "2932997323", "8975302030", "8011052266"]
lectureMeetingPass = ["4441", "123456", "12345", "150620",
                      "434241", "978714", "208208", "860837", "286080", "226476"]


# zoom pixel info/config
zoom_start_button = (957, 518)
zoom_meeting_id = (943, 484)
zoom_turnOff_video_btn = (804, 646)
zoom_proceed_meeting_btn = (990, 679)
zoom_meeting_password = (840, 486)
zoom_meeting_join_btn = (969, 685)


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False


def LectureToId(lectures):
    if lectures[i].lower() in "english":
        lastDigit = input("Enter first three digit of English's Meeting Id: ")
        if lastDigit in "333":
            meetingId.append(lectureMeetingId[4])
            meetingPass.append(lectureMeetingPass[4])
        elif lastDigit in "715":
            meetingId.append(lectureMeetingId[5])
            meetingPass.append(lectureMeetingPass[5])
    elif lectures[i].lower() in "science":
        lastDigit = input("Enter first three digit of Science's Meeting Id: ")
        if lastDigit in "897":
            meetingId.append(lectureMeetingId[8])
            meetingPass.append(lectureMeetingPass[8])
        elif lastDigit in "801":
            meetingId.append(lectureMeetingId[9])
            meetingPass.append(lectureMeetingPass[9])
    elif lectures[i].lower() in "ss":
        lastDigit = input("Enter first three digit of S.S's Meeting Id: ")
        if lastDigit in "208":
            meetingId.append(lectureMeetingId[6])
            meetingPass.append(lectureMeetingPass[6])
        elif lastDigit in "293":
            meetingId.append(lectureMeetingId[7])
            meetingPass.append(lectureMeetingPass[7])
    elif lectures[i].lower() in "hindi":
        meetingId.append(lectureMeetingId[1])
        meetingPass.append(lectureMeetingPass[1])
    elif lectures[i].lower() in "maths":
        meetingId.append(lectureMeetingId[0])
        meetingPass.append(lectureMeetingPass[0])
    elif lectures[i].lower() in "pe":
        meetingId.append(lectureMeetingId[2])
        meetingPass.append(lectureMeetingPass[2])
    elif lectures[i].lower() in "it":
        meetingId.append(lectureMeetingId[3])
        meetingPass.append(lectureMeetingPass[3])
    else:
        print("Enter valid answer!")


print("")
print("")

no_lectures = input("Number of lectures: ")
for i in range(int(no_lectures)):
    if i+1 == 1:
        pos = "st"
    elif i+1 == 2:
        pos = "nd"
    elif i+1 == 3:
        pos = "rd"
    elif i+1 == 4:
        pos = "rth"

    lect.append(input(str(i+1) + pos + " lecture: "))
    LectureToId(lect)


meetingStart = ["8", "20", "9", "10", "10", "00"]
meetingEnd = ["9", "00", "9", "50", "10", "40"]
meetingEndOne = ["9", "00"]
meetingEndTwo = ["9", "50"]
meetingEndThree = ["10", "40"]
meetingEndFour = ["11", "30"]


def zoomAttendMeeting(meetingCode, startStatus):
    # Automating zoom
    if startStatus:
        os.startfile(zoom_path)

    for i in range(len(meetingId)):
        time.sleep(10)
        if checkIfProcessRunning('zoom'):
            pyautogui.click(zoom_start_button[0], zoom_start_button[1])
            time.sleep(5)
            pyautogui.click(zoom_meeting_id[0], zoom_meeting_id[1])
            pyautogui.write(meetingId[int(meetingCode)])
            pyautogui.click(
                zoom_turnOff_video_btn[0], zoom_turnOff_video_btn[1])
            pyautogui.click(
                zoom_proceed_meeting_btn[0], zoom_proceed_meeting_btn[1])
            time.sleep(3)
            pyautogui.click(zoom_meeting_password[0], zoom_meeting_password[1])
            pyautogui.write(meetingPass[int(meetingCode)])
            pyautogui.click(zoom_meeting_join_btn[0], zoom_meeting_join_btn[1])
            time.sleep(10)
            while True:
                timeH = int(datetime.datetime.now().strftime("%H"))
                timeM = int(datetime.datetime.now().strftime("%M"))
                time.sleep(30)
                if int(meetingCode) == 0:
                    if timeH == meetingEndOne[0] and timeM == meetingEndOne[1]:
                        print("")
                        print("Ending meeting!")
                        print("")
                        pyautogui.keyDown('altleft')
                        pyautogui.keyDown('f4')
                        pyautogui.keyUp('altleft')
                        pyautogui.keyUp('f4')
                        pyautogui.keyDown('altleft')
                        pyautogui.keyDown('f4')
                        pyautogui.keyUp('altleft')
                        pyautogui.keyUp('f4')
                    elif int(meetingCode) == 1:
                        if timeH == meetingEndTwo[0] and timeM == meetingEndTwo[1]:
                            pyautogui.keyDown('altleft')
                            pyautogui.keyDown('f4')
                            pyautogui.keyUp('altleft')
                            pyautogui.keyUp('f4')
                            pyautogui.keyDown('altleft')
                            pyautogui.keyDown('f4')
                            pyautogui.keyUp('altleft')
                            pyautogui.keyUp('f4')
                    elif int(meetingCode) == 2:
                        if timeH == meetingEndThree[0] and timeM == meetingEndThree[1]:
                            pyautogui.keyDown('altleft')
                            pyautogui.keyDown('f4')
                            pyautogui.keyUp('altleft')
                            pyautogui.keyUp('f4')
                            pyautogui.keyDown('altleft')
                            pyautogui.keyDown('f4')
                            pyautogui.keyUp('altleft')
                            pyautogui.keyUp('f4')
                    elif int(meetingCode) == 3:
                        if timeH == meetingEndFour[0] and timeM == meetingEndFour[1]:
                            pyautogui.keyDown('altleft')
                            pyautogui.keyDown('f4')
                            pyautogui.keyUp('altleft')
                            pyautogui.keyUp('f4')
                            pyautogui.keyDown('altleft')
                            pyautogui.keyDown('f4')
                            pyautogui.keyUp('altleft')
                            pyautogui.keyUp('f4')
        else:
            pass


def checkTiming():
    status = True
    print("Checking Timing")
    print("")
    while status:
        timeH = int(datetime.datetime.now().strftime("%H"))
        timeM = int(datetime.datetime.now().strftime("%M"))

        if no_lectures == 1:
            if int(timeH) >= int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
                if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
                    checkTiming()
                    print("Meeting will start soon!")
            else:
                if checkIfProcessRunning('zoom'):
                    zoomAttendMeeting(0, False)
                else:
                    zoomAttendMeeting(0, True)
                    status = False

        elif no_lectures == 2:
            if int(timeH) >= int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
                if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
                    checkTiming()
                    print("Meeting will start soon!")
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(0, False)
                    else:
                        zoomAttendMeeting(0, True)
                        status = False

            elif int(timeH) >= int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
                if timeH >= int(meetingEnd[2]) and timeM >= int(meetingEnd[3]):
                    print("Meeting will start soon!")
                    checkTiming()
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(1, False)
                    else:
                        zoomAttendMeeting(1, True)
                        status = False

        elif no_lectures == 3:
            if int(timeH) >= int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
                if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
                    checkTiming()
                    print("Meeting will start soon!")
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(0, False)
                    else:
                        zoomAttendMeeting(0, True)
                        status = False

            elif int(timeH) >= int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
                if timeH >= int(meetingEnd[2]) and timeM >= int(meetingEnd[3]):
                    print("Meeting will start soon!")
                    checkTiming()
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(1, False)
                    else:
                        zoomAttendMeeting(1, True)
                        status = False
            elif int(timeH) >= int(meetingStart[4]) and int(timeM) >= int(meetingStart[5]):
                if timeH >= int(meetingEnd[4]) and timeM >= int(meetingEnd[5]):
                    print("Meeting will start soon!")
                    checkTiming()
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(2, False)
                    else:
                        zoomAttendMeeting(2, True)
                        status = False
        elif no_lectures == 4:
            if int(timeH) >= int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
                if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
                    checkTiming()
                    print("Meeting will start soon!")
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(0, False)
                    else:
                        zoomAttendMeeting(0, True)
                        status = False

            elif int(timeH) >= int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
                if timeH >= int(meetingEnd[2]) and timeM >= int(meetingEnd[3]):
                    print("Meeting will start soon!")
                    checkTiming()
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(1, False)
                    else:
                        zoomAttendMeeting(1, True)
                        status = False
            elif int(timeH) >= int(meetingStart[4]) and int(timeM) >= int(meetingStart[5]):
                if timeH >= int(meetingEnd[4]) and timeM >= int(meetingEnd[5]):
                    print("Meeting will start soon!")
                    checkTiming()
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(2, False)
                    else:
                        zoomAttendMeeting(2, True)
                        status = False
            elif int(timeH) >= int(meetingStart[6]) and int(timeM) >= int(meetingStart[7]):
                if timeH >= int(meetingEnd[6] and timeM >= int(meetingEnd[7])):
                    print("Metting will start soon!")
                    checkTiming()
                else:
                    if checkIfProcessRunning('zoom'):
                        zoomAttendMeeting(3, False)
                    else:
                        zoomAttendMeeting(3, True)
                        status = False
            else:
                print("")
                print("Sorry, No lecture at the moment!")


checkTiming()


def exiting():
    if len(meetingId) >= 2:
        response = input("Do you  want to exit (y/n): ")
        if response.lower() == "y":
            print("You will required to enter details again when restart!")
            print("Exiting...")
            time.sleep(5)
            os._exit(0)
    else:
        print("Exiting in 3s")
        time.sleep(3)
        os._exit(0)


atexit.register(exiting)
