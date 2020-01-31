char = raw_input("Enter String : ")


def stringAlternative(char):
    temp = ""
    for i in range(len(char)):
        if (i % 2) == 0:
            temp = temp + char[i]
    print(temp)


stringAlternative(char)