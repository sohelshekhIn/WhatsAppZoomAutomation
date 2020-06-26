import os
import time
import psutil
import datetime
import pyautogui

meetingId = ["7155941385","4351864441", "2298966093"]
meetingPass = ["978714", "4441", "150260"]


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


no_lectures = input("number of lectures: ")
lect = []

for i in range(no_lectures):
  lect.append(input("Lecture "+ i))
   


ZOOM_PATH = "C:\\Users\\sohel\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"


# zoom pixel info/config
zoom_start_button = (957,518)
zoom_meeting_id = (943,484)
zoom_turnOff_video_btn = (804,646)
zoom_proceed_meeting_btn = (990,679)
zoom_meeting_password = (840,486)
zoom_meeting_join_btn = (969,685)


def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;
  



meetingStart =  ["8", "20","9","10","10","00"]
meetingEnd = ["9","00","9","50","10","40"]

meetingEndOne = ["9","00"]
meetingEndTwo = ["9","50"]
meetingEndThree = ["10","40"]
meetingEndFour = ["11", "30"]


def zoomAttendMeeting(meetingCode,startStatus):
    # Automating zoom
    if startStatus:
      os.startfile(ZOOM_PATH)

    for i in range(len(meetingId)):
      time.sleep(10)
      if checkIfProcessRunning('zoom'):
          pyautogui.click(zoom_start_button[0], zoom_start_button[1])
          time.sleep(5)
          pyautogui.click(zoom_meeting_id[0],zoom_meeting_id[1])
          pyautogui.write(meetingId[int(meetingCode)])
          pyautogui.click(zoom_turnOff_video_btn[0],zoom_turnOff_video_btn[1])
          pyautogui.click(zoom_proceed_meeting_btn[0],zoom_proceed_meeting_btn[1])
          time.sleep(3)
          pyautogui.click(zoom_meeting_password[0],zoom_meeting_password[1])
          pyautogui.write(meetingPass[int(meetingCode)])
          pyautogui.click(zoom_meeting_join_btn[0],zoom_meeting_join_btn[1])
          time.sleep(10)
          while True:
            timeH = int(datetime.datetime.now().strftime("%H"))
            timeM = int(datetime.datetime.now().strftime("%M"))
            time.sleep(30)
            if int(meetingCode) == 0:
              if timeH == meetingEndOne[0] and timeM == meetingEndOne[1]:
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
  while status:
    timeH = int(datetime.datetime.now().strftime("%H"))
    timeM = int(datetime.datetime.now().strftime("%M"))

    if no_lectures == 1:
      if int(timeH) >=  int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
        if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
          checkTiming()
          print("Meeting will start soon!")
      else:
        if checkIfProcessRunning('zoom'):
          zoomAttendMeeting(0,False)
        else:
          zoomAttendMeeting(0, True)
          status = False

    elif no_lectures == 2:
      if int(timeH) >=  int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
        if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
          checkTiming()
          print("Meeting will start soon!")
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(0,False)
          else:
            zoomAttendMeeting(0, True)
            status = False

      elif int(timeH) >=  int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
        if timeH >= int(meetingEnd[2]) and timeM >= int(meetingEnd[3]):
          print("Meeting will start soon!")
          checkTiming()
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(1,False)
          else:      
            zoomAttendMeeting(1,True)
            status = False

    elif no_lectures == 3:
      if int(timeH) >=  int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
        if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
          checkTiming()
          print("Meeting will start soon!")
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(0,False)
          else:
            zoomAttendMeeting(0, True)
            status = False

      elif int(timeH) >=  int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
        if timeH >= int(meetingEnd[2]) and timeM >= int(meetingEnd[3]):
          print("Meeting will start soon!")
          checkTiming()
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(1,False)
          else:      
            zoomAttendMeeting(1,True)
            status = False
      elif int(timeH) >=  int(meetingStart[4]) and int(timeM) >= int(meetingStart[5]):
        if timeH >= int(meetingEnd[4]) and timeM >= int(meetingEnd[5]):
          print("Meeting will start soon!")
          checkTiming()
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(2,False)
          else:
            zoomAttendMeeting(2,True)
            status = False
    elif no_lectures == 4:
      if int(timeH) >=  int(meetingStart[0]) and int(timeM) >= int(meetingStart[1]):
        if timeH >= int(meetingEnd[0]) and timeM >= int(meetingEnd[1]):
          checkTiming()
          print("Meeting will start soon!")
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(0,False)
          else:
            zoomAttendMeeting(0, True)
            status = False

      elif int(timeH) >=  int(meetingStart[2]) and int(timeM) >= int(meetingStart[3]):
        if timeH >= int(meetingEnd[2]) and timeM >= int(meetingEnd[3]):
          print("Meeting will start soon!")
          checkTiming()
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(1,False)
          else:      
            zoomAttendMeeting(1,True)
            status = False
      elif int(timeH) >=  int(meetingStart[4]) and int(timeM) >= int(meetingStart[5]):
        if timeH >= int(meetingEnd[4]) and timeM >= int(meetingEnd[5]):
          print("Meeting will start soon!")
          checkTiming()
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(2,False)
          else:
            zoomAttendMeeting(2,True)
            status = False
      elif int(timeH) >= int(meetingStart[6]) and int(timeM) >= int(meetingStart[7]):
        if timeH >= int(meetingEnd[6] and timeM >= int(meetingEnd[7])):
          print("Metting will start soon!")
          checkTiming()
        else:
          if checkIfProcessRunning('zoom'):
            zoomAttendMeeting(3,False)
          else:
            zoomAttendMeeting(3,True)
            status = False
          



checkTiming()