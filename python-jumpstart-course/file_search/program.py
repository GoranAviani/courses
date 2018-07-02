
def main():
    print_header()
    folder = get_folder_from_user()
    if not folder:
        print("Sorry we cant search tat location.")
        return

    text = get_search_text_from_user()
    if not text:
        print("We cant search for nothing")

    search_folders(folder, text)

def print_header():
    print("---------------------------------------------------")
    print("                  File searching app")
    print("---------------------------------------------------")


def get_folder_from_user():
    fodler = input("what folder do you want to search")
    #folder is empty, none or if it is just whitespace
    if not folder or folder.strip():
        return None


def get_search_text_from_user():
    pass

def search_folders():
    pass




if __name__ == "__main__":
    main()