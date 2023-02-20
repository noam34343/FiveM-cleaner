# Python Login system v2 << basic fivem cleaner
import os, time

def login():
    print("[1] Login")
    print("[2] Register")
    select = input("> ")
    if select == '1':
        user = input("enter your username: ")
        with open('save.txt') as f:
            if user in f.read():
                print(f"your username: {user}") # formatting
                os.system('cls')
                password = input("enter your password: ")
                with open ('save.txt') as f:
                    if password in f.read():
                        print("Successfully logged into account!")
               

            else:
                print("sorry! we cannot find your information! try again later.")
                os._exit(0)
  

    else:
        if select == '2':
            register = input("username:")
            register2 = input("password:")
            register3 = input("license key: ")
            with open ("keys.txt") as f:
                if register3 in f.read():
                    print("Successfully created account!")
                    file = open ('save.txt', "w")
                    file.write(f"someone registerd account! his details here\nusername: {register}\npassword: {register2}")
        else:
            print("Not Valid Option")
            os._exit(0)
            



login()

def cleaner():
    print("[1] Start Cleaner")
    print('[2] Exit')
    select = input('> ')
    if select == '2':
        os._exit(0)
    else:
        if select == '1':
            print("Finding your os name..")
            time.sleep(3)
            user = os.getlogin()
            print("Starting your cleaner!")
            os.remove(rf'C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\CitizenFX_SubProcess_chrome.bin')
            os.remove(rf'C:\\Users\{user}\\AppData\\Local\\FiveM\\FiveM.app\\CitizenFX_SubProcess_game_1604.bin')
            os.remove(rf'C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\CitizenFX_SubProcess_game_2189.bin')
            os.remove(rf'C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\logs')
            os.remove(rf'C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\citizen')
            os.remove(rf'C:\\Users\\{user}\\AppData\\Local\\DigitalEntitlements')
            os.remove(rf'C:\\Users\\{user}\\AppData\\Local\\FiveM\\FiveM.app\\data\\cache')
            os.remove(rf'C:\\Users\\{user}\\AppData\\Roaming\\CitizenFX')
            print("Done cleaning!")
            print("Resetting your internet connection..")
            os.system('cls')
            os.system('ipconfig /renew')
            os.system('ipconfig /release')
            os.system('netsh winsock reset')
            os.system('ipconfig /release')
            os.system('ipconfig /renew')
            exit = input("press any key to exit the cleaner...")
            os._exit(0)
            
