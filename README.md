# notebook

We have 2 files here. The first one called notebook.py has 2 classes, which we use in the second fine menu.py.

notebook.py:

class Note represents a ote in our notebook and matchs against a string in searches and store tags for each note.Function __init__ initializes a note with memo and optionalspace-separated tags and automatically sets the note's creation date and a unique id. Function match determines if this note matches the filter text. Return True if it matches, False otherwise.

class Notebook represents a collection of notes that can be tagged,modified, and searched. '__init__' initializes a notebook with an empty list; 'new_notes' - creates a new note and add it to the list;
'find_note' locates the note with the diven id; 'modify_memo' finds the note wih the given id and changes its memo to the given value; 'modify_tags' finds the note with the given is and changes its tags to the given value and 'search' finds all notes that match the given filter string.

menu.py:

here we import our 2 classes from previous file. class Menu dispayes a menu and responds to choices when run. def 'desplay_menu' prints the options of the menu; def 'run' displayes the menu and responds to choises; def 'show_notes' shows notes(func for the first option in menu); def 'search_note' is for the second option in menu. It searches a note, which you wrote in the input; def 'add_note' is for the third option in menu. It adds a note, which you wrote in the input; def 'modify_note' is for the fourth option in menu. It modifies a note, which id, memo and tags you wrote in the input; the last one function in this class is 'quit' and it prints 'Thank you for using your notebook today'
