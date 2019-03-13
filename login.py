from getpass import getpass
import os
import time

def menu():
      while True:
           os.system("clear")
           print ("\n\n")
           print ("\033[1;96m██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗\n██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝\n██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗  \n██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝  \n╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗\n ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝")
           try:
                e = getpass('\033[1;92m [+] Enter Password \033[1;93m: ')
                if e=="crot":
                   print(' [√] LOGIN SUCCESS ...')
                   time.sleep(1)
                   os.system('clear')
                   break
                else:
                      print("\033[1;91m [!] Wrong Password")
                      time.sleep(1)
           except Exception:
                      print("\033[1;91m [!] Wrong Password")
                      time.sleep(1)
           except KeyboardInterrupt:
                      os.system('killall -9 com.termux')
                      print("\033[1;91m [!] Wrong Password")
                      time.sleep(1)
menu()
