import ui as ui
import storage as storage
import sys


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

    # print('-----------------------------')
    # ui.print_schedule_for_the_day(timetable)
    # print('-----------------------------')

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
        print('Im in canceling')
        pass
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