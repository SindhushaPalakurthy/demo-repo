from playsound import playsound
import time

CLEAR = "\033[2J"   #clears the screen before printing output
CLEAR_AND_RETURN = "\033[H" # prints the updated output in the same line instead of new line everytime


def alarm(seconds):
    time_elapsed = 0
     
    print(CLEAR)
    while time_elapsed < seconds :
        time.sleep(1)
        time_elapsed += 1

        time_left = seconds - time_elapsed
        minutes_left = time_left // 60
        seconds_left = time_left % 60

        print(f"{CLEAR_AND_RETURN}ALARM will sound in: {minutes_left:02d}:{seconds_left:02d}")

    playsound("alarm.mp3")   

minutes = int(input("How many minutes to wait: "))     
seconds = int(input("How many seconds to wait: "))  
total_seconds = minutes * 60 + seconds
alarm(total_seconds)
