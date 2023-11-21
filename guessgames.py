from random import randint

def guess1():
    """
    Hàm chơi đoán số: Nhập số từ bàn phím để đoán số bí mật
    """
    secret_number = 7
    guess = int(input("What number am I thinking of? "))
    if secret_number == guess:
        print("Yay! You got it.")
    else:
        print("No, that's not it.")

def guess2():
    secret_number = randint(1, 100)
    while True:
        guess = int(input("What number am I thinking of? "))
        if secret_number == guess:
            print("Yay! You got it.")
            break
        else:
            print("No, that's not it.")
            
def guess3():
    secret_number = randint(1, 100)
    while True:
        guess = int(input("What number am I thinking of? "))
        if secret_number == guess:
            print("Yay! You got it.")
            break
        elif secret_number > guess:
            print("No, that's too low.")
        else:
            print("No, that's too high.")