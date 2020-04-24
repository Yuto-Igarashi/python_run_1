
def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            print("FizzBuzz 3の倍数かつ5の倍数:",i)
        elif i%3==0:
            print("Fizz 3の倍数:",i)
        elif i%5==0:
            print("Buzz 5の倍数:",i)

if __name__ == "__main__":
    fizzbuzz()