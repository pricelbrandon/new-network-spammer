#generates a random SSID and Password ever 60 seconds by default, editable.
#nmcli must be installed, (prob sudo apt install network-manager)
#replace wlan0 with desired wifi interface. (wlan0 or driver ID (wlxe4fac...etc. from "tcpdump --list-interfaces")
#must run as sudo or root since it's doing network management things.
#Check to see what your gotchi can see, and whitelist all of those static networks as this is intended to run for a long time.
#Whitelist instructions here https://pwnagotchi.org/getting-started/configuration/index.html

#CREATE YOUR GOTCHI WHITELIST
#CREATE YOUR GOTCHI WHITELIST
#CREATE YOUR GOTCHI WHITELIST
#CREATE YOUR GOTCHI WHITELIST
#CREATE YOUR GOTCHI WHITELIST
#CREATE YOUR GOTCHI WHITELIST
#CREATE YOUR GOTCHI WHITELIST

import random
import string
import subprocess
import time

# Function to generate a random string
def generate_random_string(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Generate random SSID
ssid_chars = string.ascii_letters + string.digits
ssid = generate_random_string(8, ssid_chars)

# Generate random Password
password_chars = string.ascii_letters + string.digits + "!@#$%^&*()-_+=?"
password = generate_random_string(12, password_chars)

print(f"Starting Ad-hoc Network with SSID: {ssid} and Password: {password}")

# Start Ad-hoc network
subprocess.run(f'netsh wlan set hostednetwork mode=allow ssid={ssid} key={password} keyUsage=persistent', shell=True, stdout=subprocess.DEVNULL)
subprocess.run('netsh wlan start hostednetwork', shell=True, stdout=subprocess.DEVNULL)

# Wait for 60 seconds
time.sleep(60)

# Stop Ad-hoc network
subprocess.run('netsh wlan stop hostednetwork', shell=True, stdout=subprocess.DEVNULL)

print("Ad-hoc Network stopped.")
