import os
import collections

SearchResult = collections.namedtuple("SearchResult", "file, line, text")

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

    match_count = 0

    #print results
    for match in matches:
        match_count += 1
        #print(match)
        #print("----------MATCH-----------")
        #print("file {}" .format(match.file))
        #print("line: {} ".format(match.line))
        #print("match text: {}" .format(match.text.strip()))
        #print()
    print("{}".format(match_count))


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

        #if its a folder call search_folders function
        if os.path.isdir(full_item):
            matches = search_folders(full_item, text)
            all_matches.extend(matches)
        else:

            #if its a - file search it
            matches = search_file(full_item, text)
            all_matches.extend(matches)


    return all_matches



def search_file(full_path, search_text):
    matches=[]
    with open(full_path, "r", encoding = "utf-8") as fin:

        line_num = 0
        for line in fin:
            line_num += 1
            #if find is > 0 append the line to matches
            if line.lower().find(search_text) >= 0:
                m = SearchResult(line = line_num, file = full_path, text = line)
                matches.append(m)

    return matches



if __name__ == "__main__":
    main()