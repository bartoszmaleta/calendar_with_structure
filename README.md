# calendar_with_structure
A console program that manages a meeting schedule.


Calendar
In this exercise, you will be writing a console program that manages a meeting schedule.

The exercise is divided into milestones. You should complete a milestone (and make sure your program works!) before moving to the next milestone.

====================================================
Structure
Your program should use multiple modules:

- cal.py: main program
- ui.py: printing data, asking user for input
- storage.py: saving and loading files (after you implement it)

You should not use any global variables. If you need to store state (for example, a list of meetings), you will need to pass it to the functions that need it.

Do not call the file calendar.py because it will clash with Python's built in calendar module

====================================================
Program features

Milestone 1: Schedule and cancel
- The program should allow you to schedule 1-hour or 2-hour meetings. The        meeting times should be at full hour (like 9:00). The meetings have a title.
- It should be possible to cancel a meeting.
- Make sure user input is validated! The program should keep asking until the    user enters the right data.

Example session:

    $ python3 cal.py

    Your schedule for the day:
    (empty)

    Menu:
    (s) schedule a new meeting
    (c) cancel an existing meeting
    (q) quit

    Your choice: s
    Schedule a new meeting.
    Enter meeting title: Lunch
    Enter duration in hours (1 or 2): 1
    Enter start time: 12
    Meeting added.

    Your schedule for the day:
    12 - 13 Lunch

    Menu: ...

Canceling a meeting:

    Your choice: c
    Cancel an existing meeting.
    Enter the start time: 13
    ERROR: There is no meeting starting at that time!
    Enter the start time: 12
    Meeting canceled.

    Your schedule for the day:
    (empty)

====================================================
Milestone 2: Validate meeting time
- The meetings should be between 8 and 18. It should not be possible to          schedule a meeting outside these hours.
- It should not be possible to schedule a meeting that overlaps with existing    meeting

For example:

    Your choice: s
    Schedule a new meeting.
    Enter meeting title: Meeting with Piotr
    Enter duration in hours (1 or 2): 2
    Enter start time: 17
    ERROR: Meeting is outside of your working hours (8 to 18)!
    Enter start time: 12
    ERROR: Meeting overlaps with existing meeting!
    Enter start time: 13
    Meeting added.

    Your schedule for the day:
    12 - 13 Lunch
    13 - 15 Meeting with Piotr

====================================================
Milestone 3: Save and load
Now, make the program store the schedule in a file (meetings.txt). The program should load the data on start, and store it when the schedule is updated.

For instance, the schedule above could be stored like this:

    12,13,Lunch
    13,15,Meeting with Piotr

====================================================
Milestone 4: More features
- It should be possible to edit a meeting (change title, duration, or time).     Make sure to check if the new meeting time is validated.
- The program should display the total meeting duration (how many hours of meetings).

- There should be a "compact meetings" feature that moves meetings to earliest   possible time (starting from 8). For instance, if we have a schedule like      this:
     9 - 10 Meeting A
    12 - 13 Meeting B
    13 - 15 Meeting C
    Then, after compacting, it should be changed to:
     8 -  9 Meeting A
     9 - 10 Meeting B
    10 - 12 Meeting C