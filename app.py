command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else: 
            started = True
            print("The Car started")
    elif command == "stop":
        if not started:
            print("The car is already stopped")
        else:
            started = False
            print("The Car stopped")
    elif command == "help":
        print("""
Start - to get your engine running
Stop - to switch your engine off
Quit - to quit
               """)
    elif command == "quit":
        break
    else:
        print("Sorry, I dont understand that")
