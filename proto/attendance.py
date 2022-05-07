import test
import time

def main():
    while True:
        try:
            test.main()
            break

        except UnboundLocalError:
            print("Image not captured properly/bar code missing. Please try again. If the issue persists try cleaning the lens.\n")
            input("Press enter to retry\n")
            continue

main()