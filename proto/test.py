import cv2
from pyzbar.pyzbar import decode
from smtplib import *
students = int(input("Enter the number of students: "))
RN = [i for i in range(1, students+1)]

def barcoderead(image):
    img = image
    Barcodes = decode(img)
    for Barcode in Barcodes:
        #(x, y, w, h) = Barcode.rect
        data = (Barcode.data)
        print(data)
    return data.decode("ASCII")

def mail():
    sm = SMTP("smtp.gmail.com", 587)
    sm.starttls()

    send_email_id = "dummytestcollege12@gmail.com"
    send_email_pass = "College1234"
    sm.login(send_email_id, send_email_pass)

    
    message = str(RN)
    sm.sendmail(send_email_id, "21z248@psgtech.ac.in", message)

    sm.quit()

    print("Sent mail")


def main():
    while True:
        cam = cv2.VideoCapture("http://192.168.193.115:8080/video")
        #cam = cv2.VideoCapture(1)
        result, image = cam.read()
        if result:
            #cv2.imshow("test"+str(i), image)
            rolln = barcoderead(image)
            cv2.imwrite(rolln+".png", image)
            RN.remove(int(rolln[-2:]))
            #cv2.destroyWindow("test"+str(i))
        else:
            print("No image")
        option = str(input("Press enter to continue or type \"exit\" to quit: "))
        if (option).lower() == "exit":
            break
        else:
            pass

    mail()
    return 0

if __name__ == "__main__":
    main()