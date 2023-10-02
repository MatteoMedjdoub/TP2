class FizzBuzz:
    def affiche ():
        output = ""
        for i in range(1,101):
            if i % 3 == 0:
                output += "Fizz"
            if i % 5 == 0:
                output += "Buzz"
            elif i % 15 == 0:
                output = str(i)