# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("3.7")
MAC = 'AAAA:BBBB:CCCC'
MAC = MAC.replace(":","")
MAC = int(MAC, 16)
MAC = bin(MAC)
print(MAC)