# This function indentify that variable declared in the programm can be called anywhere in th program
def main():
    height = get_height()
    for i in range (height):
     print("#")

def get_height():
    while True:
        try:
            n = int(input("Height: "))
            if n > 0:
                break
        except ValueError:
                print("This is not an int")

    return n

main()