import os


def load(journal_name):

    data =[]

    filename = get_full_path(journal_name)
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for entry in file.readlines():
                data.append(entry.strip('\n'))

    return data


def save(journal_name, journal_data):
    filename = get_full_path(journal_name)
    print(str(filename))
    print("Saving to {}.".format(filename))

    with open(filename, 'w') as file:
        for entry in journal_data:
            file.write(entry + '\n')


def add_entry(text, data):
    return data.append(text)

def get_full_path(journal_name):
    return os.path.abspath(os.path.join('.','journals/' + journal_name + '.myextension'))