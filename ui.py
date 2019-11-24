def print_schedule_for_the_day(table):
    print("++++++++++++++++++++++")
    for meeting in table:
        meeting_hour = int(meeting[2])
        meeting_duration = int(meeting[1])
        meeting_end_hour = meeting_hour + meeting_duration 
        meeting_title = meeting[0]
        print(meeting_hour, "-", meeting_end_hour, meeting_title)
    print("++++++++++++++++++++++")
    pass


def print_table(table):
    print(table)


def print_menu(title, list_options, exit_message):
    print()
    print(title)
    
    index_of_first_element_of_the_list = 0
    index_of_first_letter_of_option = 0
    for element in list_options:
        print('    ({}) {}'.format(list_options[index_of_first_element_of_the_list][index_of_first_letter_of_option], element))
        index_of_first_element_of_the_list += 1
    print('    ({}) {}'.format(exit_message[index_of_first_letter_of_option], exit_message))


def return_headline_for_menu_title_(head):
    head_centered = head.center(60)
    headlne2 = '\033[1;34;49m {} \033[0;37;49m'.format(head_centered)
    return headlne2


def get_inputs(list_labels, title):
    print()
    print(title)
    inputs = []
    for label in list_labels:
        print(label)
        user_input = input()
        inputs.append(user_input)
    return inputs


# def print_one_day(table, day):
#     day.lower()
#     if day == "monday":
#         index_of_first_day_of_the_week = 0
#         print(table[0])
#         for index, hour in enumerate(table[index_of_first_day_of_the_week]):
#             print("{}. {}".format(index + 1, hour))
#     elif day == "tuesday":
#         print(table[1])
#     elif day == "wednesday":
#         print(table[2])
#     elif day == "thursday":
#         print(table[3])
#     elif day == "friday":
#         print(table[4])
#     elif day == "saturday":
#         print(table[5])
#     elif day == "sunday":
#         print(table[6])


def blank_line():
    print() 


def print_text(string):
    print(string)


def print_dashes_for_canceling_error():
    error_message_cancel = "ERROR: There is no meeting starting at that time!"
    length_of_error_message = len(error_message_cancel)
    print("-" * length_of_error_message)


def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """
    print('Error! WARNING! WTF? {}'.format(message))
    # your code


def print_enumerate_table(table):
    # for i, item in enumerate(table, 1):
        # print('{}. {}'.format(i, item))
    
    for index, meeting in enumerate(table):
        
        meeting_hour = int(meeting[2])
        meeting_duration = int(meeting[1])
        meeting_end_hour = meeting_hour + meeting_duration 
        meeting_title = meeting[0]
        # print('-------------------------')
        # print(meeting_hour, "-", meeting_end_hour, meeting_title)
        # print('-------------------------')
        print(f'{index + 1}. {meeting_hour} - {meeting_end_hour} {meeting_title}')


def print_result(result, label):
    blank_line()
    print(label)
    print(result)


def line_of_equals():
    print("====================================================")


def clear_terminal():
    print("\033c")