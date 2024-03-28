from docx import Document
import random


def load_vocabulary(filenames):
    vocabulary = {}
    for filename in filenames:
        document = Document(filename)
        for table in document.tables:
            for row in table.rows:
                if len(row.cells) == 3:
                    mandarin, pinyin, deutsch = row.cells[0].text, row.cells[1].text, row.cells[2].text
                    vocabulary[mandarin] = (pinyin, deutsch)
                else:
                    print(f'Warnung: Eine Zeile in {filename} hat nicht genau 3 Zellen. Diese Zeile wurde übersprungen.')
    return vocabulary

def quiz(voabulary):
    items = list(vocabulary.items())
    random.shuffle(items)
    for mandarin, (pinyin, deutsch) in items:
        print(f"What is the meaning of {mandarin}({pinyin})?")
        answer = input().strip().lower()
        if answer in deutsch.lower():
            print(f"Richtig! {deutsch}! Hier ein Keks: 🍪")
        else:
            print(f"Leider falsch :c Richtig ist {deutsch}")
            
if __name__ == "__main__":
    filenames_input = input('Bitte geben Sie den Pfad der Vokabeldateien ein (durch Komma getrennt, inklusive .docx): ')
    filenames = [filename.strip() for filename in filenames_input.split(',')]
    vocabulary = load_vocabulary(filenames)
    print(f"Lade Vokabel aus Datei(-en) {filenames}")
    print("Eingaben bitte immer wie folgt : 'zahl: 18', 'nomen: Haus' etc.")
    quiz(vocabulary)