command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print ("The Car started")
    elif command == "stop":
        print ("The Car stopped")
    elif command == "help":
        print ("""
               Start - to get your engine running
               Stop - to switch your engine off
               quit - to quit
               """)
    elif command == "quit":
        break
    else:
        print ("Sorry, I dont understand that")
