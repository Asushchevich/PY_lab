# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
print("3.6")
ospf_route = 'O 10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
rezult = """ 
Protocol: 		OSPF
Prefix: 		10.0.24.0/24
AD/Metrix: 		110/41
Next-Hop: 		10.0.13.3
Last update: 	3d18h
Outbound: 		Interface: FastEthernet0/0 """
print(rezult)