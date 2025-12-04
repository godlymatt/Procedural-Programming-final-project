import sys

def read_money():
    try:
        with open("money.txt", "r") as infile:
            for line in infile:
                new_line = line
                money = float(new_line)
                return money
    except FileNotFoundError:
            print("The file money.txt cannot be fount please check your files and try again.")
            sys.exit()
        
        


def write_money(balance):
    with open("money.txt", "w") as outfile:
        outfile.write(str(balance))