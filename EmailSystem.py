import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os
from tkinter import *
from tkinter import messagebox

def sendEmail():

    # mail server parameters
    smtpHost = "smtp.gmail.com"
    smtpPort = 587
    mailUname = 'YOUR Email'
    mailPwd = 'Your Password'
    fromEmail = 'same email'
    
    # mail body, recepients, attachment files
    mailSubject = sub.get()
    # mailContentHtml = "Hi, Hope u are fine. <br/> This is a <b>test</b> mail from python script using an awesome library called <b>smtplib</b>"
    mailContent = messag.get()
    
    recepientsMailList = ['abcd@domain.com']  #You can add any number of emails you want to send
        
    #The attached files should be in the same folder as the program
    attachmentFpaths = ["smtp.png","KING.mp4"]
    
    # create message object
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    msg.attach(MIMEText(mailContent, 'plain'))
    # msg.attach(MIMEText(mailContentHtml, 'html'))
    
    # create file attachments
    
    for aPath in attachmentFpaths:
        # check if file exists
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(aPath, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        'attachment; filename="{0}"'.format(os.path.basename(aPath)))
        msg.attach(part)

    # Send message object as email using smptplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    messagebox.showinfo("Message","Execution complete...")
    s.quit()

    # check if errors occured and handle them accordingly
    if not len(sendErrs.keys()) == 0:
        raise Exception("Errors occurred while sending email", sendErrs)


    # sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,
    #         mailSubject, mailContent, recepientsMailList, attachmentFpaths)

# Graphical User Interface using Tkinter
Kartikey = Tk()
Kartikey.geometry("500x500")
Kartikey.minsize(500,500)
Kartikey.maxsize(500,500)
Kartikey.title("EMAIL SENDING SYSTEM......")

backg = Canvas(Kartikey)
Search = Frame(backg,bg = "GREY12")
img1 = PhotoImage(file=r"Path of File\GUII.png")

heading = Label(text = "EMAIL SENDING SYSTEM BY PYTHON",bg = "green",fg = "black",font = "10",width="500",height = "3")
heading.pack()

subject_field = Label(text="Subject: ")
email_body_field = Label(text="Message: ")

subject_field.place(x=15,y=70)
email_body_field.place(x=15,y=140)

sub = StringVar()
messag = StringVar()

address_entry = Entry(textvariable=sub,width="30",font="25")
email_body_entry = Entry(textvariable=messag,width="50",font="30")
 
address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)
 
button = Button(Kartikey,text="Send Message",command=sendEmail,width="30",height="2",bg="grey")
 
button.place(x=15,y=220)

backg.create_image(0,0,image = img1,anchor=NW)
backg.pack(fill="both",expand = True)
backg.config(bg = "GREY12")

Kartikey.mainloop()

# Label(Search,text = "Enter Subject: ",bg = "WHITE",fg = "GREY12",font =" 30 ").grid(row=0,column=0)
# Entry(Search,bg = "Grey5",textvariable=address,fg="White").grid(row=0,column=1)

# Label(Search1,text = "Enter Content: ",bg = "WHITE",fg = "GREY12",font =" 30 ").grid(row=1,column=0)
# Entry(Search1,bg = "Grey5",textvariable=mail,fg="White").grid(row=1,column=1)
# Button(Search1,image = se,borderwidth=0,bg = "WHITE",activebackground="WHITE",command=sendEmail).grid(row=2,column=2,padx=(20, 0))

# # Label(Search2,text = "Enter number of email addresses you want to send the mail to: ",bg = "WHITE",fg = "GREY12",font =" 30 ").grid(row=2,column=0)
# # Entry(Search2,bg = "Grey5",textvariable=ser,fg="White").grid(row=2,column=1)
# # Button(Search2,image = se,borderwidth=0,bg = "WHITE",activebackground="WHITE").grid(row=2,column=2,padx=(20, 0))

# # Label(Search3,text = "Enter Email Address: ",bg = "WHITE",fg = "GREY12",font =" 30 ").grid(row=3,column=0)
# # Entry(Search3,bg = "Grey5",textvariable=ser,fg="White").grid(row=3,column=1)
# # Button(Search3,image = se,borderwidth=0,bg = "WHITE",activebackground="WHITE").grid(row=3,column=2,padx=(20, 0))

# backg.create_image(0,0,image = bg,anchor = NW)
# backg.create_image(100,100,image = t)

# backg.create_window(200,250,window=Search)
# backg.create_window(201,300,window=Search1)
# backg.pack(fill="both",expand=True)
# backg.config(bg = "GREY12")

# messagebox.showinfo("Message","Execution complete...")

# Kartikey.mainloop()

