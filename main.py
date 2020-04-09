import datetime

from os import system, name

from time import sleep

from IPython.display import clear_output  # For Jupyter Notebook

import threading as th

Real_Time = True


def key_capture_thread():
    global Real_Time
    input()
    Real_Time = False


def art():
    clear()
    clear_output(wait=True)

    print(" ██████╗ ██████╗ ██╗   ██╗██╗██████╗        ██╗ █████╗ ")
    print("██╔════╝██╔═══██╗██║   ██║██║██╔══██╗      ███║██╔══██╗")
    print("██║     ██║   ██║██║   ██║██║██║  ██║█████╗╚██║╚██████║")
    print("██║     ██║   ██║╚██╗ ██╔╝██║██║  ██║╚════╝ ██║ ╚═══██║")
    print("╚██████╗╚██████╔╝ ╚████╔╝ ██║██████╔╝       ██║ █████╔╝")
    print(" ╚═════╝ ╚═════╝   ╚═══╝  ╚═╝╚═════╝        ╚═╝ ╚════╝")
    print("\n")

    sleep(0.75)


def clear():

    # For windows
    if name == "nt":
        _ = system("cls")

    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def instructions():
    print("Welcome to The Real-Time COVID-19")
    print("Bay Area Quarantine 😷 Countdown Clock.\n")
    print("The Current Date to Be Released is: 4/7/20, 00:00:00 PST.\n")
    print("To Stop, Please Press:[ ENTER ].\n")


def clear_msg():
    print("This message will clear in 5.")
    sleep(1)
    print("4.")
    sleep(1)
    print("3.")
    sleep(1)
    print("2.")
    sleep(1)
    print("1.")
    sleep(1)
    clear()
    clear_output(wait=True)


def main():
    clear_msg()
    th.Thread(
        target=key_capture_thread, args=(), name="key_capture_thread", daemon=True
    ).start()

    while Real_Time:

        delta = datetime.datetime(2020, 5, 1) - datetime.datetime.now().replace(
            microsecond=0
        )
        clear()
        clear_output(wait=True)
        print("Today's Date and Time:", datetime.datetime.now().replace(microsecond=0))
        print("Time Left in Quarantine:", delta, "...")
        print("                                  ", "H  M  S")
        # Used for computers with (PST) Time. 
        """
        sleep(.99)
        delta = datetime.datetime(2020, 4, 5, 1) - datetime.datetime.now().replace(
            microsecond=0
        )
        clear()
        clear_output(wait=True)
        sleep(.01)
        print("Time Left in Quarantine:", delta, "...")
        print("                                  ", "H  M  S")
        """
        # This is used for Computers/Servers with (UTC) time.


if __name__ == "__main__":
    art()
    instructions()
    main()
