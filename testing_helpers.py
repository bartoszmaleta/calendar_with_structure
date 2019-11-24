import ui as ui
import storage as storage
FILE_PATH = "timetable_simple.csv"

timetable = storage.get_table_from_file(FILE_PATH)
 

def remove(table, start_time):
    INDEX_OF_START_TIME_OF_MEETING = 2
    INDEX_OF_START_TIME_FROM_INPUT_LIST = 0
    start_time = start_time[INDEX_OF_START_TIME_FROM_INPUT_LIST]
    list_with_meeting_to_remove = []

    for index, meeting in enumerate(table):
        if meeting[INDEX_OF_START_TIME_OF_MEETING] == start_time:
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


def print_enumerate_table(table):
    for i, item in enumerate(table, 1):
        print('{}. {}'.format(i, item))
