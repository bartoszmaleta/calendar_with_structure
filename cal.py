import ui as ui


def choose():
    inputs = ui.get_inputs(["Please enter a letter (s/c/q): "], "")
    option = inputs[0]
    if option == "1":
        pass
        # store.start_module()
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
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
        handle_menu()
        try:
            choose()
        except KeyError as err:
            ui.print_error_message(str(err))


if __name__ == '__main__':
    main()