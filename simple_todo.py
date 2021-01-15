# Base strings for prompt
enter_action = '\nEnter -1- to view all items, -2- to add items or -3- to remove items.' \
               'Enter -4- to erase all your items\n'
enter_time = 'When is the activity for?\nEnter 24 hour time with no colon.\n'
enter_activity = 'What is the activity?\n'

# Determines which action to perform
read = 'read'
write = 'write'
delete = 'delete'
erase_file = 'erase_file'


def prompt_for_action():
    action = int(input(enter_action))
    if action < 1 or action > 4:
        prompt_for_action()
    return action


def verify_action(action):
    if action == 1:
        action = read

        file = access_external_file(action)
        print(file)
        # return main()
        exit()

    elif action == 2:
        return write

    elif action == 3:
        return delete

    elif action == 4:
        action = erase_file
        access_external_file(action)
        print('new file made')
        exit()
        
    else:
        print('failed to choose action')


"""
Used for all data entry and verification
"""


def prompt_for_data(string):
    data = input(string)
    return data


def verify_time_data(time):
    if 0 < int(time) < 2400 and len(time) == 4:
        return True
    return False


def format_time(time):
    pass


def verify_activity_data(activity):
    pass


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
            doc.close()

        elif action == delete:
            pass

        elif action == erase_file:
            print('test')
            doc.truncate(0)

        else:
            print('failed to use file')


def main():
    prompt_action = prompt_for_action()
    action = verify_action(prompt_action)

    while True:

        time = prompt_for_data(enter_time)
        if verify_time_data(time) is False:
            raise ValueError('Time is not a 4-position number between 0000 and 2399\n')

        activity = prompt_for_data(enter_activity)
        if verify_activity_data(activity) is False:
            raise ValueError('Activity is not valid\n')

        processed_data = f'{time} --- {activity}\n'

        access_external_file(action, processed_data)

        if data_entry_loop_control() is False:
            break

    print('main() completed')


if __name__ == '__main__':
    main()

