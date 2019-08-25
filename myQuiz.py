def q1():
    print("1. What is Windows XP?")
    print("a) An operating system for Mac")
    print("b) An operating system for Windows")
    print("c) An operating system for Mac")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
        q2()
    else:
        print("Sorry, that was the wrong answer!")


def q2():
    print("2. What is Apple's latest device?")
    print("a) iPhone")
    print("b) MacBook Pro")
    print("c) iPod Touch")

    answer = str(input("What's the right answer: "))

    if answer == "b":
        print("well done, that's correct!")
    else:
        print("Sorry, that was the wrong answer!")

    q3()

def q3():
    print("3. Who is the CEO of Google?")
    print("a) Jamal N")
    print("b) Kamal G")
    print("c) Sundor J")

    answer = str(input("What's the right answer: "))

    if answer == "c":
        print("well done, that's correct!")
    else:
        print("Sorry, that was the wrong answer!")

q1()