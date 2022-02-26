"""
realisation of Notebook. Classes
"""
import datetime
# Store the next available id for all new notes
last_id = 0
class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''
    def __init__(self, memo, tags=''):
        '''
        initialize a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id
        >>> n1 = Note("hello first")
        >>> n1.id
        1
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id
    def match(self, filter):
        '''
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        
        Search is case sensitive and matches both text and
        tags
        >>> n1 = Note("hello first")
        >>> n1.match('hello')
        True
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''
    Represent a collection of notes that can be tagged,
    modified, and searched
    '''
    def __init__(self):
        '''
        Initialize a notebook with an empty list
        '''
        self.notes = []
    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list
        >>> n = Notebook()
        >>> n.new_note("hello world")
        >>> n.new_note("hello again")
        '''
        self.notes.append(Note(memo, tags))
    def _find_note(self, note_id):
        '''
        Locate the note with the given id.
        >>> n = Notebook()
        >>> n._find_note('hello')
        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None
    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.
        >>> n = Notebook()
        >>> n.modify_memo(1, "hi world")
        False
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False
    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its
        tags to the given value
        '''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break
    def search(self, filter):
        '''
        Find all notes that match the given filter
        string
        >>> n = Notebook()
        >>> n.search("hello")
        []
        '''
        return [note for note in self.notes if note.match(filter)]
