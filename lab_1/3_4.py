# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


print("3.4")
command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'
command1 = command1.strip().split()
command2 = command2.strip().split()
vlan1 = command1[-1].split(',')
vlan2 = command2[-1].split(',')
vlan1 = set(vlan1)
vlan2 = set(vlan2)
print(list(vlan1 & vlan2))
