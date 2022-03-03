# Interface Status
# ================================================================================
# DN                                                 Description           Speed    MTU  
# -------------------------------------------------- --------------------  ------  ------
# topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
# topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
import json

f = open('sample-data.json', 'r')
temp = f.read()

dct = json.loads(temp)
print('Interface Status\n' + 80*'=' + '\nDN' + 49*' ' +'Description          Speed   MTU\n' + 50*'-' + ' ' + 20*'-' + ' ' + 6*'-' + ' ' + 6*'-')
for i in dct["imdata"]:
    print(i["l1PhysIf"]["attributes"]["dn"], end = '')
    if len(str((i["l1PhysIf"]["attributes"]["dn"]))) == 42:
        print(28*' ' + i["l1PhysIf"]["attributes"]["descr"] + ' ' + i["l1PhysIf"]["attributes"]["speed"] + 2*' ' + i["l1PhysIf"]["attributes"]["mtu"])
    else:
        print(29*' ' + i["l1PhysIf"]["attributes"]["descr"] + ' ' + i["l1PhysIf"]["attributes"]["speed"] + 2*' ' + i["l1PhysIf"]["attributes"]["mtu"])
