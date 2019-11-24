import ui as ui
import storage as storage
import sys


def copy_table(table):
    copied_table = list(table)
    return copied_table


def cancel_meeting(FILE_PATH, timetable):
    while True:
        copied_table = copy_table(timetable)
        storage.write_table_to_file(FILE_PATH, remove(timetable, ui.get_inputs(["Enter the start time of the meeting you want to remove"], "REMOVING")))
        # print(copied_table)
        # print(timetable)
        if copied_table != timetable:
            break


def remove(table, start_time):
    INDEX_OF_START_TIME_OF_MEETING = 2
    start_time = start_time[0]
    list_with_meeting_to_remove = []

    for index, meeting in enumerate(table):
        # print(type(meeting[INDEX_OF_START_TIME_OF_MEETING]))
        # print(meeting[INDEX_OF_START_TIME_OF_MEETING])
        # print(type(start_time))
        # print(start_time)
        # print(meeting)
        if meeting[INDEX_OF_START_TIME_OF_MEETING] == start_time:
            table.pop(index)
            list_with_meeting_to_remove.append(index)
    
    if len(list_with_meeting_to_remove) == 0:
        ui.blank_line
        ui.print_dashes_for_canceling_error()
        ui.printing_string("ERROR: There is no meeting starting at that time!")
        ui.print_dashes_for_canceling_error()
        ui.blank_line
    else:
        ui.printing_string("Meeting canceled")
    return table


def schedule(table):
    ui.printing_string('Schedule a new meeting')
    TITLE_LIST = ['Enter a meeting title ', 'Enter duration in hours (1 or 2): ', 'Enter start time: ']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about a meeting')
    table.append(ask_input)

    return table


def schedule_for_the_day():
    ui.blank_line()
    FILE_PATH = "timetable_simple.csv"
    timetable = storage.get_table_from_file(FILE_PATH)

    ui.blank_line()
    ui.printing_string("Your schedule for today:")
    if len(timetable) == 0:
        ui.printing_string("(empty)")
    else:
        ui.print_schedule_for_the_day(timetable)


def choose():
    # FILE_PATH = "timetable.csv"
    # timetable = storage.get_table_from_file(FILE_PATH)
    FILE_PATH = "timetable_simple.csv"
    timetable = storage.get_table_from_file(FILE_PATH)

    # TODO: printing for the specific day schedule!
    # inputs = ui.get_inputs(["Please enter a name of the day of the week"])
    # ui.print_one_day(timetable, inputs[0].lower())
    # ui.print_one_day(timetable, 'monday')

    inputs = ui.get_inputs(["Please enter a letter (s/c/q): "], "")
    option = inputs[0]
    if option == "s":
        ui.blank_line()
        print('-----------------------------')
        # timetable = [[""] * 24 for day in range(7)]  
        # timetable[0][15] = "meeting with Jane"
        # storage.write_table_to_file(FILE_PATH, timetable)

        storage.write_table_to_file(FILE_PATH, schedule(timetable))
        ui.printing_string("Meeting added")
        ui.print_schedule_for_the_day(timetable)
    elif option == "c":
        # OLD WAY, without error handling (wrong start time input)
        # storage.write_table_to_file(FILE_PATH, remove(timetable, ui.get_inputs(["Enter the start time of the meeting you want to remove"], "REMOVING"))) 
        schedule_for_the_day()
        cancel_meeting(FILE_PATH, timetable)
    elif option == "q":
        print('Im in quiting')
        sys.exit(0)
    elif option == "????":
        pass

    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["schedule a new meeting",
               "cancel an existing meeting"]

    menu_title = "Main menu"
    menu_title = ui.return_headline_for_menu_title_(menu_title)
    ui.print_menu(menu_title, options, "quit")


def main():
    while True:
        schedule_for_the_day()
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()