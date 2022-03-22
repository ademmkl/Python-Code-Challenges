import smtplib

def sendMail(gmail,subject,message):

    try:
        sender = "ademk014689@gmail.com"
        password = "2357_pakaPAKA"
        content = "Subject:{}\n{}".format(subject, message)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, gmail, content.encode("utf-8"))
        server.close()

        print("Gönderim başarılı.")
    except Exception as e:
        print("Hata!")
        print(e)



sendMail("ademkl123@gmail.com", "Test", "Hi!")