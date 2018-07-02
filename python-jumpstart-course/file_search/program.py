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

    matches = search_folders(folder, text)

    #print results
    for match in matches:
        print(match)



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
    return text.lower()



def search_folders(folder, text):

    all_matches=[]
    #listdir gives only filename, not full path name
    items = os.listdir(folder)


    for item in items:
        #adding path + name of folder as full path
        full_item = os.path.join(folder, item)

        #if its a folder skip it
        if os.path.isdir(item):
            continue
        #if its a - file search it
        matches = search_file(full_item, text)
        all_matches.extend(matches)

    return all_matches



def search_file(full_path, search_text):
    matches=[]
    with open(full_path, "r", encoding = "utf-8") as fin:

        for line in fin:
            if line.lower().find(search_text) >= 0:
                matches.append(line)

    return matches



if __name__ == "__main__":
    main()