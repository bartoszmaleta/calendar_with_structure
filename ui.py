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