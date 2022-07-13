

import time
import kehan
import test




print(kehan.x)
print("Project Zeus")
kehan.beep1()
time.sleep(1)
kehan.beep1()

kehan.speak("Welcome to project zeus")
kehan.speak("To access the program please authenticate yourself")
kehan.auth()
time.sleep(2)
while True:
    print("Select Option")
    kehan.speak("Please Select an option")
    print("1: Target Selection")
    print("2: Soldier Manifest")
    option = int(input("Enter your Option: "))
    time.sleep(1)
    kehan.speak("Option Selected")

    if option == 1:
        kehan.map2()
        kehan.speak("Showing satellite imagery now")
        time.sleep(1)
        kehan.speak("Target Selection Complete")
    elif option == 2:
        kehan.speak("Opening soldier manifest")
        time.sleep(1)
        kehan.manifest()
        time.sleep(10)




