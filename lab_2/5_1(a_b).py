# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
while True:
    IP = input()
    isIpCorrect = True
    if len(IP.split(".")) != 4:
        isIpCorrect = False

    ipArray = IP.split(".")
    for number in ipArray:
        if int(number) not in range(0, 255):
            isNumbersCorrect = False
            break
    if isIpCorrect:
        if IP == "255.255.255.255":
            print("local broadcast")
        if IP == "0.0.0.0":
            print("unassigned")
        firstNum = IP.split(".")[0]
        if 223 < int(firstNum) < 239:
            print("multicast")
        if int(firstNum) < 224:
            print("unicast")
        break
    else:
        print("Incorrect IPv4 address")