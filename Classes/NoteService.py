from datetime import datetime

from Classes.Note import Note


class NoteService:
    def __init__(self, note_repository):
        self.note_repository = note_repository

    def create_note(self, title, body):
        note_id = str(len(self.note_repository.load_notes()) + 1)
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        updated_at = created_at
        note = Note(note_id, title, body, created_at, updated_at)
        notes = self.note_repository.load_notes()
        notes.append(note)
        self.note_repository.save_notes(notes)

    def get_all_notes(self):
        return self.note_repository.load_notes()

    def edit_note_title(self, note_id, new_title):
        notes = self.note_repository.load_notes()
        for note in notes:
            if note.note_id == note_id:
                note.title = new_title
                note.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.note_repository.save_notes(notes)
                return
        raise ValueError("Note with the specified ID was not found.")

    def edit_note_body(self, note_id, new_body):
        notes = self.note_repository.load_notes()
        for note in notes:
            if note.note_id == note_id:
                note.body = new_body
                note.updated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.note_repository.save_notes(notes)
                return
        raise ValueError("Note with the specified ID was not found.")

    def delete_note(self, note_id):
        notes = self.note_repository.load_notes()
        for note in notes:
            if note.note_id == note_id:
                notes.remove(note)
                self.note_repository.save_notes(notes)
                return
        raise ValueError("Note with the specified ID was not found.")

    def filter_notes_by_date(self, date):
        notes = self.note_repository.load_notes()
        filtered_notes = []
        for note in notes:
            if note.created_at.startswith(date):
                filtered_notes.append(note)
        return filtered_notes