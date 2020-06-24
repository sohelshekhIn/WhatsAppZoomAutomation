import os
import time
import psutil
import datetime
import pyautogui
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# name = input("Paste exact name of user")
name = "Class 10 C (20-21)"

# WebDriver Path
PATH = "C:\dev\chromedriver.exe"
PROFILE = "C:\\Users\\sohel\\AppData\\Local\\Google\\Chrome\\User Data\\Default"
ZOOM_PATH = "C:\\Users\\sohel\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
msgXPath ="//*[@id='main']/div[3]/div/div/div[3]/div[7]/div/div/div/div[2]/div/span[1]/span"


# zoom pixel info/config
zoom_start_button = (957,518)
zoom_meeting_id = (943,484)
zoom_turnOff_video_btn = (804,646)
zoom_proceed_meeting_btn = (990,679)
zoom_meeting_password = (840,486)
zoom_meeting_join_btn = (969,685)


# # selenium config
# options = webdriver.ChromeOptions() 
# options.add_argument(r"user-data-dir="+PROFILE) #Path to your chrome profile
# driver = webdriver.Chrome(executable_path=PATH, chrome_options=options)
# # Whatsapp Site Link
# whatsAppLink = "https://web.whatsapp.com"
# driver.maximize_window()
# driver.get(whatsAppLink)
# time.sleep(8) #So whatsapp can load
# user = driver.find_element_by_xpath(f'//span[@title = "{name}"]')
# user.click()
# try:
#     msg = driver.find_element_by_xpath(msgXPath)
#     msg = msg.text

#     if "Please find the details of the Virtual Class for tomorrow" in msg:
#       print("Yes, it is")
#     else:
#       print("no")
# except Exception as e:
#     if "Message: no such element: Unable to locate element" in e:
#         print("Element not found")
#         exit(0)

# div[7] describes the msg length
# time.sleep(555000)



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

# # meetingId = "744 1278 6077"
# # password = "7GWX3M"

# meetingId = "4351864441"
# password = "4441"
meetingId = ["123456789","123456123","123456321"]
meetingPass = ["123456","654321","789456"]

  # Automating zoom
os.startfile(ZOOM_PATH)

for i in range(len(meetingId)):
  time.sleep(10)
  if checkIfProcessRunning('zoom'):
      pyautogui.click(zoom_start_button[0], zoom_start_button[1])
      time.sleep(5)
      pyautogui.click(zoom_meeting_id[0],zoom_meeting_id[1])
      pyautogui.write(meetingId[i])
      pyautogui.click(zoom_turnOff_video_btn[0],zoom_turnOff_video_btn[1])
      pyautogui.click(zoom_proceed_meeting_btn[0],zoom_proceed_meeting_btn[1])
      time.sleep(3)
      pyautogui.click(zoom_meeting_password[0],zoom_meeting_password[1])
      pyautogui.write(meetingPass[i])
      pyautogui.click(zoom_meeting_join_btn[0],zoom_meeting_join_btn[1])

  else:
      pass