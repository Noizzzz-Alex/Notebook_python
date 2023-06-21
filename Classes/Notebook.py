import json
import os

from Classes.Note import Note


class Notebook:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_notes(self):
        if not os.path.exists(self.file_path):
            return []
        with open(self.file_path, "r") as file:
            try:
                notes_data = json.load(file)
                return [self._deserialize_note(note_data) for note_data in notes_data]
            except json.JSONDecodeError:
                return []

    def save_notes(self, notes):
        notes_data = [self._serialize_note(note) for note in notes]
        with open(self.file_path, "w") as file:
            json.dump(notes_data, file, indent=4)

    def _serialize_note(self, note):
        return {
            "id": note.note_id,
            "title": note.title,
            "body": note.body,
            "created_at": note.created_at,
            "updated_at": note.updated_at
        }

    def _deserialize_note(self, note_data):
        return Note(
            note_data["id"],
            note_data["title"],
            note_data["body"],
            note_data["created_at"],
            note_data["updated_at"]
        )