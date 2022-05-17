"""In this program you are asked to implement a small text machine with a set of simple capabilities. The procedure
is that at the beginning of the program, the program receives an initial text string (up to 1000 in length) from the
input. Then, until it receives the exit command, the user requests an operation on the text string each time.

Operations are defined as follows:

Description and output of the input command
SHIFT-R N Moves all the characters of the expression in a single N rotation to the right.
SHIFT-L N Moves all the characters of the expression in a single N rotation to the left.
EXTEND N adds a new character to the end of the existing N string and sets an asterisk (*) as the default value of the characters.
SHRINK N Deletes N characters from the end of the string. If the string length is less than N, each string will be an empty string.
REVERSE reverses the string.
PUT I C replaces the letter I of the I string with the letters C. Note that the number of places starts with one, and the smaller I will always be equal to the length of the string.
PRINT prints the current string and goes to the next line.
EXIT Stop and finish program

"""


word = input()
print()
y = True
while y:
    command = input()
    try:
        # 1- exit

        if command.upper() == "EXIT":
            y = False

        # 2 - print
        elif command.upper() == "PRINT":
            print(word.strip())

        # 3- REVERSE
        elif "REVERSE" in command.upper():
              word = word[::-1]

        # 4- SHRINK
        elif "SHRINK" in command.upper():
            s = command.find(' ')
            n = int(command[s:].strip())
            nl = len(word)
            if nl-n < 0:
                word = ''
            else:
                word = word[:nl-n]

        # 5- EXTEND
        elif "EXTEND" in command.upper():
            s = command.find(' ')
            n = int(command[s:].strip())
            word = word + n * "*"

        # 6- SHIFT-l
        elif "SHIFT-L" in command.upper():
            def leftrotate(s, d):
                tmp = s[d:] + s[0: d]
                return tmp
            s = command.find(' ')
            n = int(command[s:].strip())
            n = n % (len(word))
            word = leftrotate(word,n)
        # 7- SHIFT-R
        elif "SHIFT-R" in command.upper():
            def leftrotate(s, d):
                tmp = s[d:] + s[0: d]
                return tmp
            s = command.find(' ')
            n = int(command[s:].strip())
            def rightrotate(s, d):
                return leftrotate(s, len(s) - d)
            n = n % (len(word))
            word = rightrotate(word,n)
        # 8- PUT I C
        elif "PUT" in command.upper():
            numbers = []
            command = command[::-1]
            s = command.find(" ")
            LW = command[:s].strip()
            LW = LW[::-1]
            command = command[::-1]
            for s in command.split():
                if s.isdigit():
                    numbers.append(int(s))
            num = (numbers[0])
            x = ''
            class1 = []
            for w in word:
                class1.append(w)
            class1[num-1] = LW
            for t in class1:
                x = x + t
            word = x
    except:
        continue
