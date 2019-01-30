import pyautogui as py
import time
import os
class App:
    @staticmethod
    def open(app_name):
        # Requries Synapse applications
        py.hotkey('ctrl','space')
        time.sleep(1.5)
        py.typewrite(app_name)
        time.sleep(0.5)
        py.press('enter')
        # print('This will open '+app_name)
class Project:
    editor='atom'
    path='/home/nikhil/Projects/'
    @staticmethod
    def open(project_name):
        print("[Opening Project {}]".format(project_name))
        os.system(Project.editor+' '+Project.path+project_name)




def main():
    Project.open('Ai')
if __name__ == '__main__':
    main()
