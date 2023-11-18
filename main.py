from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QListWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit

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




main_lain.addLayout(line1, stretch=2)
main_lain.addLayout(line2, stretch=1)
window.setLayout(main_lain)
window.show()
app.exec_()