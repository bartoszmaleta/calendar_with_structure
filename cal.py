import ui as ui
import storage as storage
import sys


def copy_table(table):
    copied_table = list(table)
    return copied_table


def cancel_meeting(FILE_PATH, timetable):
    is_running = True
    while is_running:
        copied_table = copy_table(timetable)
        storage.write_table_to_file(FILE_PATH, remove(timetable, ui.get_inputs(["Enter the start time of the meeting you want to remove"], "REMOVING")))
        # print(copied_table)
        # print(timetable)
        if copied_table != timetable:
            is_running = False


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
        ui.print_error_message("ERROR: There is no meeting starting at that time!")
        ui.print_dashes_for_canceling_error()
        ui.blank_line
    else:
        ui.print_text("Meeting canceled")
    return table


def schedule(table):
    INDEX_OF_START_TIME_OF_MEETING = 2
    INDEX_OF_DURATION_OF_MEETING = 1

    is_running = True
    while is_running:
        ui.print_text('Schedule a new meeting')
        TITLE_LIST = ['Enter a meeting title ', 'Enter duration in hours (1 or 2): ', 'Enter start time: ']
        ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about a meeting')
        
        input_meeting_hour = int(ask_input[INDEX_OF_START_TIME_OF_MEETING])
        input_meeting_duration = int(ask_input[INDEX_OF_DURATION_OF_MEETING])
        input_end_meeting_time = input_meeting_hour + input_meeting_duration

        if input_meeting_hour >= 8 and input_meeting_hour <= 18:
            table.append(ask_input)
            is_running = False
            
            # TODO: It should not be possible to schedule a meeting that overlaps with existing meeting!!!!!!!!!!!!!!!!!!!!
            # for meeting in table:
            #     meeting_time = int(meeting[INDEX_OF_START_TIME_OF_MEETING])
            #     meeting_duration = int(meeting[INDEX_OF_DURATION_OF_MEETING])
            #     meeting_end_time = meeting_time + meeting_duration
                
            #     print(meeting_time)
            #     print(type(meeting_time))
            #     print(input_meeting_hour)
            #     print(type(input_meeting_hour))

            #     # if meeting_time != input_meeting_hour and meeting_time != input_end_meeting_time and meeting_end_time != input_meeting_hour and meeting_end_time != input_end_meeting_time:
            #     if meeting_time != input_meeting_hour:
            #         table.append(ask_input)
            #         print('I AM HEEEERE')
            #         is_running = False
            #     else:
            #         ui.print_error_message("ERROR: Meeting overlaps with existing meeting!")
        else:
            ui.print_error_message("ERROR: Meeting is outside of your working hours (8 to 18)!")        # TODO: should ask again only about start time!
    # while True:
    #     copied_table = copy_table(table)
        
    #     if copied_table != table:
    #         break

    return table


def schedule_for_the_day():
    ui.blank_line()
    FILE_PATH = "timetable_simple.csv"
    timetable = storage.get_table_from_file(FILE_PATH)

    ui.blank_line()
    ui.print_text("Your schedule for today:")
    if len(timetable) == 0:
        ui.print_text("(empty)")
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
        ui.print_text("Meeting added")
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