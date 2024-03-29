import ui as ui
import storage as storage
import sys

# TODO:
# - It should not be possible to schedule a meeting that overlaps 
#   with existing meeting                                                              NOT DONE
# - There should be a "compact meetings" feature that moves meetings to 
#   earliest possible time (starting from 8). For instance, if we 
#   have a schedule like this:
#  9 - 10 Meeting A
# 12 - 13 Meeting B
# 13 - 15 Meeting C

# Then, after compacting, it should be changed to:
#  8 -  9 Meeting A
#  9 - 10 Meeting B
# 10 - 12 Meeting C                                                                     NOT DONE

# - It should be possible to edit a meeting (change title, duration, or time).          DONE
# - Make sure to check if the new meeting time is validated.                            NOT DONE                            
# - Make canceling the meeting by index (from enumerate) of meeting                     DONE
# - Update README.md                                                                    DONE


def sorting_list_by_start_time_of_the_meeting(table):
    sorted_list = sorted(table, key=lambda x: x[2])

    return sorted_list 


def compact_meetings(table):
    timetable = sorting_list_by_start_time_of_the_meeting(table)
    print(timetable)

    pass


def total_number_of_meeting_hours(table):
    list_of_duration_of_meetings = []
    INDEX_OF_DURATION_TIME_OF_MEETING_IN_TIMETABLE = 1

    for meeting in table:
        list_of_duration_of_meetings.append(int(meeting[INDEX_OF_DURATION_TIME_OF_MEETING_IN_TIMETABLE]))

    sum_of_all_duration_of_meetings = 0
    for duration in list_of_duration_of_meetings:
        sum_of_all_duration_of_meetings += duration

    return(sum_of_all_duration_of_meetings)

# def validate_on_working_hours(table, start_time, duration_time):
#     if input_meeting_hour >= 8 and input_meeting_hour <= 18:
#             table.append(ask_input)
#             is_running = False
#         else:
#             ui.print_error_message("ERROR: Meeting is outside of your working hours (8 to 18)!")        # TODO: should ask again only about start time!


def edit_a_meeting(table, title_of_meeting):
    ui.print_text('Schedule a new meeting')
    TITLE_LIST = ['Enter a meeting title ', 'Enter duration in hours (1 or 2): ', 'Enter start time: ']
    ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about a meeting')
    
    INDEX_OF_TITLE_OF_MEETING_IN_TIMETABLE = 0
    INDEX_OF_DURATION_TIME_OF_MEETING_IN_TIMETABLE = 1
    INDEX_OF_START_TIME_OF_MEETING_IN_TIMETABLE = 2
    
    INDEX_OF_TITLE_OF_MEETING_IN_ASK_INPUT = 0
    INDEX_OF_DURATION_TIME_OF_MEETING_IN_ASK_INPUT = 1
    INDEX_OF_START_TIME_OF_MEETING_IN_ASK_INPUT = 2
    
    for title_of_meeting_to_edit, meeting in enumerate(table):
        if meeting[0] == title_of_meeting:
            meeting[INDEX_OF_TITLE_OF_MEETING_IN_TIMETABLE] = ask_input[INDEX_OF_TITLE_OF_MEETING_IN_ASK_INPUT]
            meeting[INDEX_OF_DURATION_TIME_OF_MEETING_IN_TIMETABLE] = ask_input[INDEX_OF_DURATION_TIME_OF_MEETING_IN_ASK_INPUT]
            meeting[INDEX_OF_START_TIME_OF_MEETING_IN_TIMETABLE] = ask_input[INDEX_OF_START_TIME_OF_MEETING_IN_ASK_INPUT]

    return table


def find_title_by_index_from_enumerate_table(table, index):
    INDEX_POSITION = 0
    INDEX_OF_FIRST_ELEMENT_OF_INDEX_LIST = 0
    NUMBER_TO_DISTRACT_BECAUES_INDEXING_IS_FROM_ZER0 = 1

    title_of_meeting = table[int(index[INDEX_OF_FIRST_ELEMENT_OF_INDEX_LIST]) - NUMBER_TO_DISTRACT_BECAUES_INDEXING_IS_FROM_ZER0][INDEX_POSITION]
    # number_of_id = number_of_id - 1
    # print(title_of_meeting)
    return title_of_meeting


def copy_table(table):
    copied_table = list(table)
    return copied_table


def cancel_meeting(FILE_PATH, timetable):
    is_running = True
    while is_running:
        copied_table = copy_table(timetable)
        # storage.write_table_to_file(FILE_PATH, remove(timetable, ui.get_inputs(["Enter the start time of the meeting you want to remove"], "REMOVING")))
        storage.write_table_to_file(FILE_PATH, remove(timetable, find_title_by_index_from_enumerate_table(timetable, ui.get_inputs(["Enter index of the meeting you want to remove"], "REMOVING"))))
        # print(copied_table)
        # print(timetable)
        if copied_table != timetable:
            is_running = False


def remove(table, title):
    TITLE_INDEX_POSITION = 0
    list_with_meeting_to_remove = []

    for index, meeting in enumerate(table):
        if meeting[TITLE_INDEX_POSITION] == title:
            table.pop(index)
            list_with_meeting_to_remove.append(index)

    length_of_list_if_list_is_empty = 0
    if len(list_with_meeting_to_remove) == length_of_list_if_list_is_empty:
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
    # INDEX_OF_DURATION_OF_MEETING = 1      # NOT USED right nows

    is_running = True
    while is_running:
        ui.print_text('Schedule a new meeting')
        TITLE_LIST = ['Enter a meeting title ', 'Enter duration in hours (1 or 2): ', 'Enter start time: ']
        ask_input = ui.get_inputs(TITLE_LIST, 'Please enter information about a meeting')
        
        input_meeting_hour = int(ask_input[INDEX_OF_START_TIME_OF_MEETING])
        # input_meeting_duration = int(ask_input[INDEX_OF_DURATION_OF_MEETING]) # NOT USED right now
        # input_end_meeting_time = input_meeting_hour + input_meeting_duration      # NOT USED right now

        if input_meeting_hour >= 8 and input_meeting_hour <= 17:        # TODO: change magic numbers
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
                
            #     if meeting_time == input_meeting_hour or meeting_time == input_end_meeting_time or meeting_end_time == input_meeting_hour or meeting_end_time == input_end_meeting_time:
            #         ui.print_error_message("ERROR: Meeting overlaps with existing meeting!")
            #         break
            #     else:
            #         table.append(ask_input)
            #         print('I AM HEEEERE')
            #         is_running = False
            #         break
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
    timetable = sorting_list_by_start_time_of_the_meeting(timetable)

    ui.blank_line()
    ui.line_of_equals()
    ui.print_text("Your schedule for today:")
    if len(timetable) == 0:
        ui.print_text("(empty)")
    else:
        ui.print_schedule_for_the_day(timetable)
    ui.line_of_equals()


def choose():
    # FILE_PATH = "timetable.csv"
    # timetable = storage.get_table_from_file(FILE_PATH)
    FILE_PATH = "timetable_simple.csv"
    timetable = storage.get_table_from_file(FILE_PATH)
    timetable = sorting_list_by_start_time_of_the_meeting(timetable)

    # TODO: printing for the specific day schedule!
    # inputs = ui.get_inputs(["Please enter a name of the day of the week"])
    # ui.print_one_day(timetable, inputs[0].lower())
    # ui.print_one_day(timetable, 'monday')

    inputs = ui.get_inputs(["Please enter a letter (s/c/u/q/t/e): "], "")
    option = inputs[0]
    if option == "s":
        ui.clear_terminal()
        ui.blank_line()
        print('-----------------------------')
        # timetable = [[""] * 24 for day in range(7)]  
        # timetable[0][15] = "meeting with Jane"
        # storage.write_table_to_file(FILE_PATH, timetable)

        storage.write_table_to_file(FILE_PATH, schedule(timetable))
        ui.print_text("Meeting added")
        ui.print_schedule_for_the_day(timetable)
    elif option == "c":
        # schedule_for_the_day()
        ui.print_enumerate_table(timetable)
        cancel_meeting(FILE_PATH, timetable)
    elif option == "u":
        ui.print_enumerate_table(timetable)
        to_be_updated = ui.get_inputs(['Insert index of file to update'], "UPDATING")
        storage.write_table_to_file(FILE_PATH, edit_a_meeting(timetable, find_title_by_index_from_enumerate_table(timetable, to_be_updated)))
    elif option == "t":
        total_hours = total_number_of_meeting_hours(timetable)
        ui.print_result(total_hours, "Total number of hours today:")

    elif option == 'e':
        compact_meetings(timetable)
    elif option == "q":
        print('Im in quiting')
        sys.exit(0)
    elif option == "????":
        pass

    else:
        raise KeyError("There is no such option.")


def handle_menu():
    options = ["schedule a new meeting",
               "cancel an existing meeting",
               "updating a meeting",
               "total time of meeting in the day",
               "everything earlier"]

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