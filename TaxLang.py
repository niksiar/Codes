""" TaxLang

In Taxpayer City, people speak Taxlang, which includes the letters T, A, X, M, and N. Because the city dates back to 1717 BC, blocks corresponding to its characters are engraved on the cave walls to write a phrase. More precisely, this language is read from left to right and includes blocks with a length of 5 and a height of 3, and each block corresponds exactly to one of the letters of this language, which you can easily discover the correspondence between by looking at the sample inputs.

Note: Look at the pattern of the stars (*)

- Sample Entry:

*****
oo*oo
oo*oo

Sample Output:

T

- Sample Entry:

oo*oo
o***o
*ooo*

Sample Output:

A

- Sample Entry:

*ooo*
oo*oo
*ooo*

Sample Output:

X

- Sample Entry:

*****oo*oo*ooo***o**oo*oo*ooo*
oo*ooo***ooo*oo*o*o*o***o*o*o*
oo*oo*ooo**ooo**ooo**ooo**ooo*

Sample Output:

TAXMAN
Code:
"""

line1 = input()
line2 = input()
line3 = input()
myclass = []
for x in range(0,len(line1),5):
    l1 = line1[x]
    l2 = line2[x]
    l3 = line3[x]
    if l1 == "*" and l2 == "*":
        try:
            if line1[x+1] == '*':
                # print("M")
                myclass.append("M")
            else:
                # print("N")
                myclass.append("N")
        except:
            continue
    if l1 == "*":
        try:
            if line1[x+2] == "*":
                # print("T")
                myclass.append("T")
        except:
            continue
    if l1 == "o":
        # print("A")
        myclass.append("A")
    if l1 == "*" and l2 == "o" and l3 == "*":
        # print("X")
        myclass.append("X")
# print(myclass)
for n in myclass:
    print(n,end='')

