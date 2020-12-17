# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print('3.5')
vlans = '10,20,30,1,2,100,10,30,3,4,10'
vlansList = list(set((vlans).split(',')))
vlansList.sort()
print(vlansList)