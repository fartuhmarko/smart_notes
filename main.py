from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QInputDialog
import json 
app = QApplication([])


window = QWidget()

text = QTextEdit()
lineText = QLineEdit()
Button = QPushButton()
notes_list = QListWidget()
tags_list = QListWidget()
main_lain = QHBoxLayout()
line1 = QVBoxLayout()
line2 = QVBoxLayout()




note_create = QPushButton("СТВОРИТИ ЗАМІТКУ")
note_delete = QPushButton("ВИДАЛИТИ ЗАМІТКУ")
note_save = QPushButton("ЗБЕРЕГТИ ЗАМІТКУ")
note_add = QPushButton("ДОДАТИ ДО ЗАМІТКИ")
note_unpin = QPushButton("ВІДКРІПИТИ ВІД ЗАМІТКИ")
note_search = QPushButton("ШУКАТИ ЗАМІТКУ ПО ТЕГУ")

note_save.setStyleSheet('''
background-color: #6bc9db                                        
    '''                    )
note_delete.setStyleSheet('''
background-color: #b01038                     
    ''')
note_create.setStyleSheet('''
background-color: #0be36c                      
    ''')
note_add.setStyleSheet('''
background-color: #c7c72a                     
    ''')
note_unpin.setStyleSheet('''
background-color: #75f505                      
    ''')
note_search.setStyleSheet('''
background-color: #e105f5                          
    ''')
line2.addWidget(notes_list)
line2.addWidget(note_create)
line2.addWidget(note_delete)
line2.addWidget(note_save)

line2.addWidget(tags_list)
line2.addWidget(lineText)
line2.addWidget(note_add)
line2.addWidget(note_unpin)
line2.addWidget(note_search)


line1.addWidget(text)
notes = {}

def add_note():
    note_name, ok = QInputDialog.getText(window, "Нова замітка", "Назва нотатки")
    if ok and note_name !="":
        notes[note_name] = {
            "text": "",
            "tags":[]
        }
        notes_list.addItem(note_name)

def writeFile():
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=True, sort_keys=True, indent=4)

def show_note():
    note_name = notes_list.currentItem().text()
    text.setText(notes[note_name]["text"])

def add_tag():
    note_name = notes_list.currentItem().text()
    tag = lineText.text()
    notes[note_name]["tags"].append(tag)
    tags_list.addItem(tag)
    writeFile()

def del_tag():
    note_name = notes_list.currentItem().text()
    tag_name = tags_list.currentItem().text()

    notes[note_name]["tags"].remove(tag_name)
    tags_list.clear()
    tags_list.addItems(notes[note_name]["tags"])
    
    writeFile()

def search_note_bytag():
    tag = lineText.text()
    if(note_search.text()=="Search"):
        filtered = {}
        for key in notes:
            if tag in notes[key]["tags"]:
                print(notes[key])
                filtered[key] = notes[key]
    

        notes_list.clear()
        notes_list.addItems(filtered)
        tags_list.clear()
        lineText.clear()
        note_search.setText("Відмінити пошук")


    else:
        note_search.setText("Search")
        notes_list.clear()
        notes_list.addItems(notes)
        tags_list.clear
note_search.clicked.connect(search_note_bytag)



note_add.clicked.connect(add_tag)

notes_list.itemClicked.connect(show_note)

with open("notes.json", "r", encoding="utf-8") as file:
    note = json.load(file)

note_create.clicked.connect(add_note)

main_lain.addLayout(line1, stretch=2)
main_lain.addLayout(line2, stretch=1)
window.setLayout(main_lain)
window.show()
app.exec_()
