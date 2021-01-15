from datetime import datetime

# Base strings for prompt
enter_action = '\nEnter -1- to view all items, -2- to add items or -3- to remove items.' \
               'Enter -4- to erase all your items\n'
enter_time = 'When is the activity for?\nEnter 24 hour time with no colon.\n'
enter_activity = 'What is the activity?\n'

# Determines which action to perform
read = 'read'
write = 'write'
delete = 'delete'
erase = 'erase'
actions = [read, write, delete, erase]


def prompt_for_action():
    action = int(input(enter_action))
    if 0 >= action or action > len(actions):
        raise ValueError('Input exceeds options available')
        # prompt_for_action() --> retains the current value of 'action'
    return actions[action - 1]


def read_file():
    file = access_external_file(read)
    print(file)
    exit()


def erase_file():
    access_external_file(erase)
    print('new file made')
    exit()


"""
Used for all data entry and verification
"""


def prompt_for_data(string):
    return input(string)


# Boolean
def verify_time_data(time):
    if 0 < int(time) < 2400 and len(time) == 4:
        return True
    return False


def format_time(time):
    convert = datetime.strptime(time, '%H%M')
    return convert.strftime('%I:%M %p')


def verify_activity_data(activity):
    pass


# Boolean
def data_entry_loop_control():
    go_on = input('Enter \'y\' to continue entering items.\n')
    if go_on == 'y':
        return True
    return False


"""
Used for accessing file
action == what to do to file
data == what to pass in/remove from doc
"""


def access_external_file(action, data=None):
    with open('simple_todo_test.txt', 'a+') as doc:

        if action == read:
            doc.seek(0)
            return doc.read()
        elif action == write:
            doc.write(data)
        elif action == delete:
            print('delete')
        elif action == erase:
            doc.truncate(0)
        else:
            print('failed to use file')
        doc.close()


def main():
    action = prompt_for_action()

    # no input required conditionals
    if action == read:
        read_file()
    if action == erase:
        erase_file()
    # while loop for continual input
    while True:

        time = prompt_for_data(enter_time)
        if verify_time_data(time) is False:
            raise ValueError('Time is not a 4-position number between 0000 and 2399\n')
        formatted_time = format_time(time)

        activity = prompt_for_data(enter_activity)
        if verify_activity_data(activity) is False:
            raise ValueError('Activity is not valid\n')

        processed_data = f'{formatted_time} --> {activity}\n'

        access_external_file(action, processed_data)

        if data_entry_loop_control() is False:
            break

    print('main() completed')


if __name__ == '__main__':
    main()
