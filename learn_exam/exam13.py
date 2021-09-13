import sys
#create commend dictionary
command={'reset':'reset what','reset board':'board fault','board add':'where to add',
        'board delete':'no board at all','reboot backplane':'impossible',
        'backplane abort':'install first'}
keyl = list(command.keys()) #dict key is hashable,transform to unhashable
while True:
    try:
        n = input().strip().split()
        if len(n) < 1 or len(n) > 2:
            print("unknown command")
        elif len(n) == 1:
            if n[0] in keyl[0]:
                print(command[keyl[0]])
            else:
                print("unknown command")
