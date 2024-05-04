def Red(skk):
    print("\033[91m {}\033[00m" .format(skk))


def Green(skk):
    print("\033[92m {}\033[00m" .format(skk))


def Yellow(skk):
    print("\033[93m {}\033[00m" .format(skk))


def LightPurple(skk):
    print("\033[94m {}\033[00m" .format(skk))


def Purple(skk):
    print("\033[95m {}\033[00m" .format(skk))


def Cyan(skk):
    print("\033[96m {}\033[00m" .format(skk))


def LightGray(skk):
    print("\033[97m {}\033[00m" .format(skk))


def Black(skk):
    print("\033[98m {}\033[00m" .format(skk))

class colors:
    class bg:
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        #lightgrey = '\033[47m'
    class fg:
        black = '\033[30m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
        purple = '\033[35m'
        #blue = '\033[34m'
        #cyan = '\033[36m'
        #lightgrey = '\033[37m'
        #darkgrey = '\033[90m'
        #lightred = '\033[91m'
        #lightgreen = '\033[92m'
        yellow = '\033[93m'
        orange = '\033[33m'
        #red = '\033[31m'
        #green = '\033[32m'
        
print( "SKk", colors.fg.yellow, "Amartya")
print( "SKk", colors.fg.orange, "Amartya")
