######  https://github.com/Helhest/agilepython/blob/main/portscanner.py ||| git@github.com:Helhest/agilepython.git




#libraries


import pyfiglet 
import sys 
import socket 
import datetime

# Now we are going to implement a banner type on the user interface to make it look better for the user


ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

target = input(str("Enter the IP Address: "))

time = datetime.datetime.now()


## After we aqquire the IP address from the user, we are going to let the user know that the program is running 

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + time.strftime("%c"))
print("_" * 50)
print("\nScaning...")

# Now we are going to start the port scanner itself

try: 
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target,port))

        if result == 0 : 
            print("[!!] Port {} is open".format(port))
            print("We'll keep searching.")
        s.close()



except KeyboardInterrupt:
    # When the user wants to terminate the program
    print("\nExiting..")
    sys.exit()

except socket.error: 
    print("\nHost not responding.")
    sys.exit()