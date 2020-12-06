import journal

def print_header():
    print('---------------------')
    print('     Journal App')
    print('---------------------')

def run_event_loop():
    print('What do you want to do with your journal?')
    userInput = None
    journal_name = "My jounral"
    journal_data = journal.load(journal_name)

    while userInput != "X":
        userInput = input("[L]ist entries\n[A]dd to entry\nE[x]it:\n")
        userInput = userInput.upper().strip()

        if userInput == "L":
            list_entries(journal_data)
        elif userInput == "A":
            add_entry(journal_data)
        #elif userInput == "X":
        #    print("Good bye")
        elif userInput != "X":
            print("Sorry I don't understand that")

    journal.save(journal_name,journal_data)

def list_entries(data):
    print("Your journal entries: ")
    entries = reversed(data)
    for key, entry in enumerate(entries):
        print(str(key+1)+":"+entry)

def add_entry(data):
    text = input("Type your entry, enter <enter> to exit: ")
    journal.add_entry(text,data)

def main():
    print_header()
    run_event_loop()


if __name__ == "__main__":
    main()