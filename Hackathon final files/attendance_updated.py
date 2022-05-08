import test
import time
import pickle
f=open("daytable.dat",'rb')
l=[]
while True:
    try:
        a=pickle.load(f)
        l.append(a)
    except:
        break
f.close()
print(l)

while True:
    a=time.localtime()
    b=int(str(a[3])+str(a[4]))
    if b==int(l[0][1][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[1][1]):
                test.mail(l[1][3])
                test.mail(l[0])
                break
    if b==int(l[0][2][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[2][1]):
                test.mail(l[2][3])
                test.mail(l[0])
                break
    if b==int(l[0][3][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[3][1]):
                test.mail(l[3][3])
                test.mail(l[0])
                break
    if b==int(l[0][4][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[4][1]):
                test.mail(l[4][3])
                test.mail(l[0])
                break
    if b==int(l[0][5][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[5][1]):
                test.mail(l[5][3])
                test.mail(l[0])
                break
    if b==int(l[0][6][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[6][1]):
                test.mail(l[6][3])
                test.mail(l[0])
                break
    if b==int(l[0][7][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[7][1]):
                test.mail(l[7][3])
                test.mail(l[0])
                break
    if b==int(l[0][8][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[8][1]):
                test.mail(l[8][3])
                test.mail(l[0])
                break
    if b==int(l[0][9][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[9][1]):
                test.mail(l[9][3])
                test.mail(l[0])
                break
    if b==int(l[0][10][0]):
        while True:
            try:
                test.main()
                break
            except UnboundLocalError:
                print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
                input("Press enter to retry\n")
                continue
            a=time.localtime()
            b=int(str(a[3])+str(a[4]))
            if b==int(l[10][1]):
                test.mail(l[10][3])
                test.mail(l[0])
                break
    if b>=2200:
        break

