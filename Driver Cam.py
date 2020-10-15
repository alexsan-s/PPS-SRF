import numpy
from pygame import mixer
import time
import cv2
from tkinter import *
import tkinter.messagebox
root=Tk()
root.geometry('1024x548')
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
root.title('PPS - SRF')
frame.config(background='white')
# label = Label(frame, text="PPS - SRF",bg='white',font=('Times 35 bold'))
# label.pack(side=TOP)
filename = PhotoImage(file=".\demo.png")
background_label = Label(frame,image=filename)
background_label.pack(side=TOP)



def hel():
   help(cv2)

def Contri():
   tkinter.messagebox.showinfo("Contribuidores","\n1.Alexsander da Sikva")


def anotherWin():
   tkinter.messagebox.showinfo("Sobre",'PPS - SRF versão v1.0\n Uitilizando\n-OpenCV\n-Numpy\n-Tkinter\n Em Python 3')
                                    
   

menu = Menu(root)
root.config(menu=menu)

subm1 = Menu(menu)
menu.add_cascade(label="Ferramentas",menu=subm1)
subm1.add_command(label="Abrir Documentos CV",command=hel)

subm2 = Menu(menu)
menu.add_cascade(label="Sobre",menu=subm2)
subm2.add_command(label="PPS - SRF",command=anotherWin)
subm2.add_command(label="Contribuidores",command=Contri)



def exitt():
   exit()

  
def web():
   capture =cv2.VideoCapture(0)
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   capture.release()
   cv2.destroyAllWindows()

def webrec():
   capture =cv2.VideoCapture(0)
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample1.avi',fourcc,11.0,(640,480))
   while True:
      ret,frame=capture.read()
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      cv2.imshow('frame',frame)
      op.write(frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
         break
   op.release()
   capture.release()
   cv2.destroyAllWindows()   

def webdet():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          
           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

       
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   capture.release()
   cv2.destroyAllWindows()
def webdetRec():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_glass = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
   fourcc=cv2.VideoWriter_fourcc(*'XVID') 
   op=cv2.VideoWriter('Sample2.avi',fourcc,9.0,(640,480))

   while True:
       ret, frame = capture.read()
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       faces = face_cascade.detectMultiScale(gray)
    

       for (x,y,w,h) in faces:
           font = cv2.FONT_HERSHEY_COMPLEX
           cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
           cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
           roi_gray = gray[y:y+h, x:x+w]
           roi_color = frame[y:y+h, x:x+w]
        
          

           eye_g = eye_glass.detectMultiScale(roi_gray)
           for (ex,ey,ew,eh) in eye_g:
              cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
       op.write(frame)
       cv2.imshow('frame',frame)
       if cv2.waitKey(1) & 0xff == ord('q'):
          break
   op.release()      
   capture.release()
   cv2.destroyAllWindows()

   
def alert():
   mixer.init()
   alert=mixer.Sound('beep-07.wav')
   alert.play()
   time.sleep(0.1)
   alert.play()   
   
def blink():
   capture =cv2.VideoCapture(0)
   face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
   eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
   blink_cascade = cv2.CascadeClassifier('CustomBlinkCascade.xml')

   while True:
      ret, frame = capture.read()
      gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray)

      for (x,y,w,h) in faces:
         font = cv2.FONT_HERSHEY_COMPLEX
         cv2.putText(frame,'Face',(x+w,y+h),font,1,(250,250,250),2,cv2.LINE_AA)
         cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
         roi_gray = gray[y:y+h, x:x+w]
         roi_color = frame[y:y+h, x:x+w]

         eyes = eye_cascade.detectMultiScale(roi_gray)
         for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

         blink = blink_cascade.detectMultiScale(roi_gray)
         for(eyx,eyy,eyw,eyh) in blink:
            cv2.rectangle(roi_color,(eyx,eyy),(eyx+eyw,eyy+eyh),(255,255,0),2)
            alert()
      cv2.imshow('frame',frame)
      if cv2.waitKey(1) & 0xFF ==ord('q'):
          break
         
  
   capture.release()
   cv2.destroyAllWindows()

   
but1=Button(frame,padx=5,pady=5,width=25,bg='white',fg='black',relief=GROOVE,command=web,text='ABRIR CAMERA',font=('helvetica 15 bold'))
but1.place(x=645,y=104)

but2=Button(frame,padx=5,pady=5,width=25,bg='white',fg='black',relief=GROOVE,command=webrec,text='ABRIR CAMERA & GRAVAR',font=('helvetica 15 bold'))
but2.place(x=645,y=176)

but3=Button(frame,padx=5,pady=5,width=25,bg='white',fg='black',relief=GROOVE,command=webdet,text='ABRIR CAMERA & DETECTAR',font=('helvetica 15 bold'))
but3.place(x=645,y=250)

but4=Button(frame,padx=5,pady=5,width=25,bg='white',fg='black',relief=GROOVE,command=webdetRec,text='DETECTAR & GRAVAR',font=('helvetica 15 bold'))
but4.place(x=645,y=322)

but5=Button(frame,padx=5,pady=5,width=34,bg='white',fg='black',relief=GROOVE,command=blink,text='DETECTAR PISCADA DE OLHOS & GRAVAR',font=('helvetica 15 bold'))
but5.place(x=590,y=400)

but5=Button(frame,padx=5,pady=5,width=5,bg='white',fg='red',relief=GROOVE,text='SAIR',command=exitt,font=('helvetica 15 bold'))
but5.place(x=758,y=478)


root.mainloop()

