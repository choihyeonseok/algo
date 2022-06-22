while True:
    num = str(input())
    if num == '0':
        break
    else:
        n =[]    
        for i in range(len(num)):
            if num[i] == '1':
                n.append(2)
            elif num[i] == '0':
                n.append(4)
            else :
                n.append(3)
        print(len(num)-1+sum(n)+2)