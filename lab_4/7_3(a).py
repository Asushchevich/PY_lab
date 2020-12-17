print('7.3a')


def get_int_vlan_map(file_name: str) -> (dict, dict):
    access = dict()
    trunk = dict()

    with open(file_name, 'r') as f:
        file = f.read().split('!')
        # print(file)
    for i in file:
        if 'Ethernet' in i:
            # print(i)
            if 'access' in i:
                access['Fast' + i.split()[1]] = i[i.index('vlan') + 1:][0]
            elif 'trunk' in i:
                i = i.split()
                trunk['Fast' + i[1]] = i[i.index('vlan') + 1:][0]
            elif 'duplex auto' in i:
                access['Fast' + i.split()[1]] = 1

    return access, trunk


print(get_int_vlan_map('config_sw1.txt'))