######  https://github.com/Helhest/agilepythonnyc ||| git@github.com:Helhest/agilepythonnyc.git


#libraries


import pyfiglet 
import sys 
import socket 
import datetime


from rich import print
# Now we are going to implement a banner type on the user interface to make it look better for the user
# https://pypi.org/project/pyfiglet/
# To further improve on the accessibility of the code, we are going to color code whenever the port scanning program finds an open port
# python -m pip install rich

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)



target = input(str("Enter the IP Address or URL: "))

openports = []

time = datetime.datetime.now()


## After we aqquire the IP address from the user, we are going to let the user know that the program is running 

print("_" * 50)
print("Scanning Target: " + target)
print("Scanning started at: " + time.strftime("%c"))
print("_" * 50)
print("\nScaning...")

# Now we are going to start the port scanner itself

try: 
    for port in range(1,1000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)

        result = s.connect_ex((target,port))

        if result == 0 : 
            print("[bold green] [!!] [bold green] Port  {} is open [/bold green]".format(port))
            openports.append(port)
        else: 
            print("[red] [!!]  Port  {} is closed [/red]".format(port))
        s.close()
    print(openports)




except KeyboardInterrupt:
    # When the user wants to terminate the program
    print("\nExiting..")
    print("\nYou stopped the program at port",port)
    print("\nThe open ports of",target,"are:",openports)
    sys.exit()

except socket.error: 
    print("\nHost not responding.")
    sys.exit()
