import smtplib


maillist=["test1@gmail.com","test2@gmail.com","test3@gmail.com","test4@gmail.com","test5@gmail.com","test6@gmail.com","test7@gmail.com","test8@gmail.com","test9@gmail.com","test10@gmail.com",]
a=input("Enter the text you want to send in email:- ")
for dest in maillist:
    s=smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login("sender@gmail.com","sender_password")
    s.sendmail("sender@gmail.com",dest,a)
    s.quit()