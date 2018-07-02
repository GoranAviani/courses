import os


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
    folder = input("what folder do you want to search")
    #folder is empty, none or if it is just whitespace
    if not folder or not folder.strip():
        return None

    #if it is not a directory
    if not os.path.isdir(folder):
        return None

    #return absolute path of folder
    return os.path.abspath(folder)


def get_search_text_from_user():
    text = input("What do you want to search for, single phrases only")
    return text



def search_folders(folder, text):
    print("searching {} for {}".format(folder, text))




if __name__ == "__main__":
    main()