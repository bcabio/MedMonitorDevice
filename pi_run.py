import time, requests
import RPi.GPIO as GPIO

INPUT_PIN = 23

URL = "https://mangohacksflask.herokuapp.com/drawer_update"

current_status = True

GPIO.setmode(GPIO.BCM)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# check GPIO device for status of drawer position
def check_status():
    # read GPIO
    pin_status = GPIO.input(INPUT_PIN) # true is closed, false is open, so 
    print (pin_status)

    # return output
    return (pin_status) # invert so true is open, false is closed

# push data = {isOpen, timestamp} to our database
def push_results(status):
    # Collect and organize data into a json we can send
    timestamp = time.time()
    data = {}
    data["isOpen"] = status
    data["ts"] = timestamp

    # Upload to server
    response = r.requests.post(url = URL, data = data)

    return

# Execute infinite process loop
while(True):
    new_status = check_status()
    # If our drawer is in a different state than when we last changed states...
    if (new_status != current_status):
        push_results(new_status)
        current_status = new_status

    # Wait x seconds for next check
    time.sleep(1)