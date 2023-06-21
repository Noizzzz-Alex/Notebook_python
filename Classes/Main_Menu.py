from Classes.NoteService import NoteService
from Classes.Notebook import Notebook


def menu():
    FILE_PATH = "Notes/notes.json"
    note_repository = Notebook(FILE_PATH)
    note_service = NoteService(note_repository)

    while True:
        print("1. Создать заметку")
        print("2. Вывести список заметок")
        print("3. Редактировать заголовок заметки")
        print("4. Редактировать текст заметки")
        print("5. Удалить заметку")
        print("6. Выход")
        choice = input("Выберите действие (1-6): ")

        if choice == "1":
            title = input("Введите заголовок заметки: ")
            body = input("Введите текст заметки: ")
            note_service.create_note(title, body)
            print("Заметка успешно создана.")
        elif choice == "2":
            notes = note_service.get_all_notes()
            print("Список заметок:")
            for note in notes:
                print(f"ID: {note.note_id}")
                print(f"Заголовок: {note.title}")
                print(f"Дата/время создания: {note.created_at}")
                print()
        elif choice == "3":
            note_id = input("Введите ID заметки для редактирования заголовка: ")
            new_title = input("Введите новый заголовок заметки: ")
            try:
                note_service.edit_note_title(note_id, new_title)
                print("Заголовок заметки успешно отредактирован.")
            except ValueError as e:
                print(str(e))
        elif choice == "4":
            note_id = input("Введите ID заметки для редактирования текста: ")
            new_body = input("Введите новый текст заметки: ")
            try:
                note_service.edit_note_body(note_id, new_body)
                print("Текст заметки успешно отредактирован.")
            except ValueError as e:
                print(str(e))
        elif choice == "5":
            note_id = input("Введите ID заметки для удаления: ")
            try:
                note_service.delete_note(note_id)
                print("Заметка успешно удалена.")
            except ValueError as e:
                print(str(e))
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")
