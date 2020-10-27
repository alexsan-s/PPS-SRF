import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
root = Tk()
root.geometry('1024x548')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
root.title('PPS - SRF')
frame.config(background='white')
# label = Label(frame, text="PPS - SRF",bg='white',font=('Times 35 bold'))
# label.pack(side=TOP)
filename = PhotoImage(file=".\demo.png")
background_label = Label(frame, image=filename)
background_label.pack(side=TOP)

menu = Menu(root)
root.config(menu=menu)


def hel():
    help(cv2)


def Contri():
    tkinter.messagebox.showinfo("Contribuidores", "\nAlexsander da Silva")


def anotherWin():
    tkinter.messagebox.showinfo(
        "Sobre", 'PPS - SRF versão v1.0\n Uitilizando\n-OpenCV\n-Numpy\n-Tkinter\n Em Python 3')


def web():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()


def webrec():
    capture = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    op = cv2.VideoWriter('Sample1.avi', fourcc, 11.0, (640, 480))
    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', frame)
        op.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    op.release()
    capture.release()
    cv2.destroyAllWindows()


def webdet():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x+w, y+h), font,
                        1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eye_g = eye_glass.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye_g:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)

        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    capture.release()
    cv2.destroyAllWindows()


def webdetRec():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    op = cv2.VideoWriter('Sample2.avi', fourcc, 9.0, (640, 480))

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x+w, y+h), font,
                        1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eye_g = eye_glass.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eye_g:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)
        op.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    op.release()
    capture.release()
    cv2.destroyAllWindows()


def alert():
    mixer.init()
    alert = mixer.Sound('beep-07.wav')
    alert.play()
    time.sleep(0.1)
    alert.play()


def blink():
    capture = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

    while True:
        ret, frame = capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)

        for (x, y, w, h) in faces:
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, 'Face', (x+w, y+h), font,
                        1, (250, 250, 250), 2, cv2.LINE_AA)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for(ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey),
                              (ex+ew, ey+eh), (0, 255, 0), 2)

            blink = blink_cascade.detectMultiScale(roi_gray)
            for(eyx, eyy, eyw, eyh) in blink:
                cv2.rectangle(roi_color, (eyx, eyy),
                              (eyx+eyw, eyy+eyh), (255, 255, 0), 2)
                alert()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()


subm1 = Menu(menu)
menu.add_cascade(label="Camera", menu=subm1)
subm1.add_command(label="Abrir a camera", command=web)
subm1.add_command(label="Gravar", command=webrec)
subm1.add_command(label="Detectar face", command=webdet)
subm1.add_command(label="Detectar face e gravar", command=webdetRec)
subm1.add_command(label="Detectar olhos", command=blink)


subm2 = Menu(menu)
menu.add_cascade(label="Ferramentas", menu=subm2)
subm2.add_command(label="Abrir Documentos CV", command=hel)

subm3 = Menu(menu)
menu.add_cascade(label="Sobre", menu=subm3)
subm3.add_command(label="PPS - SRF", command=anotherWin)
subm3.add_command(label="Aluno", command=Contri)

root.mainloop()
