import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor


widgets={'logo':[],'button':[],'prompt':[],'check':[],'save':[],'try_again':[],'message':[],'again':[],'ext':[]}

globals_={'check_ok':False,'file':[],'text':[]}


app=QApplication(sys.argv)
window=QWidget()
window.setWindowTitle('List of Names')
window.setFixedWidth(1000)
window.setStyleSheet('background:#161219;')


grid=QGridLayout()


image=QPixmap('1st app\\logo.png')
image=image.scaledToHeight(400)
logo=QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter)
logo.setStyleSheet('margin-top:50px;')
widgets['logo'].append(logo)

message=QLabel()
message.setText('')
message.setStyleSheet('font-size:23px; color:white; padding:10px 10px; margin:10px 250px')
widgets['message'].append(message)

ext=QPushButton('Exit')
ext.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
ext.setStyleSheet('*{ border:4px solid "#303030"; border-radius:10px; font-size:17px; color:"grey"; padding:10px 15px; margin:0 10px;}*:hover{background:"#CD0000";color:"grey";}')
widgets['ext'].append(ext)

grid.addWidget(widgets['ext'][-1],3,0,1,3,QtCore.Qt.AlignCenter)
grid.addWidget(widgets['message'][-1],1,0,1,3,QtCore.Qt.AlignCenter)
grid.addWidget(widgets['logo'][-1],0,0,1,3)

ext.clicked.connect(QApplication.instance().quit)

def clear_widg(widg):
    if widgets[widg] !=[]:
        widgets[widg][-1].hide()
        widgets[widg].pop()


def frame_start():

    button=QPushButton('Enter Username')
    button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    button.setStyleSheet('*{ border:4px solid "#303030"; border-radius:14px; font-size:35px; color:"white"; padding:10px 10px; margin:10px 200px;}*:hover{background:"#CD661D";color:"green";}')
    widgets['button'].append(button)

    grid.addWidget(widgets['button'][-1],1,1)

    button.clicked.connect(frame_main)


def frame_main():

    globals_['file']=[]
    globals_['text']=[]
    globals_['check_ok']=False

    file=open(r'1st app\\names.txt','a+')
    globals_['file'].append(file)

    widgets['message'][-1].setText('')

    for i in ['try_again','button','again','save','prompt','save','check']:
        clear_widg(i)

    prompt=QLineEdit()
    prompt.setMaxLength(40)
    prompt.setPlaceholderText("Enter your text")
    prompt.setStyleSheet('border:4px solid "black"; border-radius:14px; font-size:25px; color:white; padding:5px 10px; margin:5px 250px')
    widgets['prompt'].append(prompt)

    save=QPushButton('Save')
    save.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    save.setStyleSheet('border:3px solid "white"; border-radius:5px; font-size:20px; color:white; padding:5px 100px; margin:10px 180px')
    widgets['save'].append(save)

    check=QPushButton('Check')
    check.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
    check.setStyleSheet('border:3px solid "white"; border-radius:5px; font-size:20px; color:white; padding:5px 100px; margin:10px 180px')
    widgets['check'].append(check)

    grid.addWidget(widgets['prompt'][-1],1,0,1,3)
    grid.addWidget(widgets['check'][-1],2,1)
    grid.addWidget(widgets['save'][-1],2,2)

    check.clicked.connect(frame_check)
    save.clicked.connect(frame_save)


def frame_check():

    globals_['text'].append(widgets['prompt'][-1].text())

    for i in ['check','prompt','again']:
        clear_widg(i)

    def again():
        clear_widg('save')
        try_again=QPushButton('Try Again')
        try_again.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        try_again.setStyleSheet('border:3px solid "white"; border-radius:5px; font-size:20px; color:white; padding:5px 100px; margin:10px 180px')
        widgets['try_again'].append(try_again)

        grid.addWidget(widgets['try_again'][-1],2,1)
        
        try_again.clicked.connect(frame_main)


    globals_['file'][-1].seek(0)

    if globals_['text'][-1]=='':
        widgets['message'][-1].setText('Type Smth')

        again()

    elif globals_['text'][-1].lower() in globals_['file'][-1].read().lower():
        widgets['message'][-1].setText('Already here')

        again()
   
    else:
        globals_['check_ok']=True
        
        again=QPushButton('Again?')
        again.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        again.setStyleSheet('border:3px solid "white"; border-radius:5px; font-size:20px; color:white; padding:5px 100px; margin:10px 180px')
        widgets['again'].append(again)

        widgets['message'][-1].setText('You can save now')
        
        grid.addWidget(widgets['again'][-1],2,1)
        
        widgets['again'][-1].clicked.connect(frame_main)
        widgets['save'][-1].clicked.connect(frame_save)


def frame_save():
    widgets['save'][-1].clicked.disconnect(frame_save)
    if globals_['check_ok']==True:
        
        for i in ['check','prompt','save']:
            clear_widg(i)

        globals_['file'][-1].write('\n{}'.format(globals_['text'][-1]))
        globals_['file'][-1].close()
        globals_['check_ok']=False

        widgets['message'][-1].setText('Succesfully Saved!')

        widgets['again'][-1].setStyleSheet('border:3px solid "white"; border-radius:5px; font-size:20px; color:white; padding:5px 10px; margin:10px 420px')

        grid.addWidget(widgets['again'][-1],2,0,1,3)
        
        widgets['again'][-1].clicked.connect(frame_main)

    
    elif globals_['check_ok']==False:
        for i in ['check','prompt','save','again']:
            clear_widg(i)
        widgets['message'][-1].setText('Check First!')
        QtCore.QTimer.singleShot(1500,frame_main)


     
frame_start()


window.setLayout(grid)
window.show()


sys.exit(app.exec())