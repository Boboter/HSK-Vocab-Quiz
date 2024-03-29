from docx import Document
import random
import re

def load_vocabulary(filenames):
    vocabulary = {}
    for filename in filenames:
        document = Document(filename)
        for table in document.tables:
            for row in table.rows:
                if len(row.cells) == 3: # Falls es kein Beispiel gibt
                    mandarin, pinyin, deutsch, beispiel = row.cells[0].text, row.cells[1].text, row.cells[2].text, ""
                    vocabulary[mandarin] = (pinyin, deutsch, beispiel)
                elif len(row.cells) == 4: # Falls es ein Beispiel gibt
                    mandarin, pinyin, deutsch, beispiel = row.cells[0].text, row.cells[1].text, row.cells[2].text, row.cells[3].text
                    vocabulary[mandarin] = (pinyin, deutsch, beispiel)
                else:   # Falls das Dokument (teilweise) in falscher Form vorliegt
                    print(f'Warnung: Zeile in {filename} übersprungen.')
    return vocabulary

def quiz(voabulary):
    items = list(vocabulary.items())
    random.shuffle(items)
    for mandarin, (pinyin, deutsch, beispiel) in items:
        print(f"Was heißt {mandarin}({pinyin})?\nBeispiel: {beispiel}")
        match = re.search(r'\((.*?)\)', deutsch)
        if match:
            expected_input = match.group(1)
        else:
            expected_input = deutsch
        answer = input().strip().lower()
        if answer == expected_input.lower().strip():
            print(f"{deutsch}! Hier ein Keks: 🍪")
        else:
            print(f"Richtig ist {deutsch}!")

if __name__ == "__main__":
    filenames_input = input('Bitte geben Sie den Pfad der Vokabeldateien ein (durch Komma getrennt, inklusive .docx): ')
    filenames = [filename.strip() for filename in filenames_input.split(',')]
    print(f"Lade Vokabel aus Datei(-en) {filenames}")
    vocabulary = load_vocabulary(filenames)
    quiz(vocabulary)