def position_space(l):
    for i in range(0, 5):
        if l[i] == (" "):
            return i    
def convertlist(s):
    l = []
    if len(s) != 5:
        print("enter only five characters")
        exit()
    else:    
        for i in range(5):
            if len(s) == 5:
                l.append(s[i])
        return l
def convertstring(ls):
    s = ' '.join(ls)
    return s
def swap(x,y):
    x,y = y,x
    l = [x,y]
    return l
s1 = convertlist(input())
s2 = convertlist(input())
s3 = convertlist(input())
s4 = convertlist(input())
s5 = convertlist(input())
p1 = p2 = p3 = p4 = p5 =-1
t1 = t2 = t3 = t4 = t5 = 1
k = input("enter key:")
if k == 'Z':
    print ("Quit")
    exit()
i = 1
while k != 'Z':
    while k != '0':
        p1 = position_space(s1)
        p2 = position_space(s2) 
        p3 = position_space(s3)
        p4 = position_space(s4)
        p5 = position_space(s5)
        if (p1==0 or p2==0 or p3==0 or p4==0 or p5==0):
            if k == 'L':
                t1 = 0   
        if (p1==4 or p2==4 or p3==4 or p4==4 or p5==4):
            if k == 'R':
                t2 = 0  
        if k!='A' and k!='B' and k!='L'and k!='R' and k != 'Z':
            print("This puzzle has no configuration.")
            exit()             
        elif p1 != None and p1 >=0:
            if k == 'A':
                t3 = 0
            elif k == 'B':
                l1 = swap(s1[p1],s2[p1])
                s1[p1],s2[p1] = l1[0],l1[1]
            elif k == 'L':
                l1 = swap(s1[p1],s1[p1-1])
                s1[p1],s1[p1-1] = l1[0],l1[1]
            else:
                if k == 'R':
                    if p1==4:
                        t5 = 0
                    else:          
                        l1 = swap(s1[p1], s1[p1+1])
                        s1[p1],s1[p1+1] = l1[0],l1[1]               
        elif p5 != None and p5 >=0:
            if k == 'B':
                t4 = 0
            elif k == 'A':
                l1 = swap(s5[p5],s4[p5])
                s5[p5], s4[p5] = l1[0],l1[1] 
            elif k == 'R':
                if p5==4:
                    t5 = 0
                else:    
                    l1 = swap(s5[p5],s5[p5+1])
                    s5[p5],s5[p5+1] = l1[0], l1[1]
            else:
                if k == 'L':
                    l1 = swap(s5[p5],s5[p5-1])
                    s5[p5],s5[p5-1] = l1[0],l1[1]       
        elif p2 != None and p2 >=0:
            if k == 'A':
                l1 = swap(s2[p2],s1[p2])
                s2[p2],s1[p2] = l1[0],l1[1]
            elif k == 'B':
                l1 = swap(s2[p2],s3[p2])
                s2[p2],s3[p2] = l1[0],l1[1]
            elif k == 'R':
                if p2 == 4:
                    t5 = 0
                else:    
                    l1 = swap(s2[p2],s2[p2+1])
                    s2[p2],s2[p2+1] = l1[0],l1[1]
            else:
                if k == 'L':
                    l1 = swap(s2[p2],s2[p2-1]) 
                    s2[p2],s2[p2-1] = l1[0],l1[1]
        elif p3 != None and p3 >=0:
            if k == 'A':
                l1 = swap(s3[p3],s2[p3])
                s3[p3],s2[p3] = l1[0],l1[1] 
            elif k == 'B':
                l1 = swap(s3[p3],s4[p3])
                s3[p3],s4[p3] = l1[0],l1[1] 
            elif k == 'R':
                if p3 == 4:
                    t5 = 0 
                else:
                    l1 = swap(s3[p3],s3[p3+1])
                    s3[p3],s3[p3+1] = l1[0],l1[1] 
            else:
                if k == 'L':
                    l1 = swap(s3[p3],s3[p3-1]) 
                    s3[p3],s3[p3-1] = l1[0],l1[1] 
        else:
            if p4 != None and p4 >=0:
                if k == 'A':
                    l1 = swap(s4[p4],s3[p4])
                    s4[p4],s3[p4] = l1[0],l1[1] 
                elif k == 'B':
                    l1 = swap(s4[p4],s5[p4])
                    s4[p4],s5[p4] = l1[0],l1[1] 
                elif k == 'R':
                    if p4 == 4:
                        t5=0
                    else:    
                        l1 = swap(s4[p4],s4[p4+1])
                        s4[p4],s4[p4+1] = l1[0],l1[1] 
                else:
                    if k == 'L':
                        l1 = swap(s4[p4],s4[p4-1]) 
                        s4[p4],s4[p4-1] = l1[0],l1[1] 
        k = input("enter key:") 
        if k == 'Z':
            print ("Quit")
            exit()
        if k == '0':
            print("puzzle #",i,":")
            if t1==0 or t2 == 0 or t3 == 0 or t4 == 0 or t5 == 0:
                print("This puzzle has no configuration.")
            else: 
                print (convertstring(s1))
                print (convertstring(s2))
                print (convertstring(s3))
                print (convertstring(s4))
                print (convertstring(s5))
            i = i + 1   
    s1 = convertlist(input())
    s2 = convertlist(input())
    s3 = convertlist(input())
    s4 = convertlist(input())
    s5 = convertlist(input())
    k = input("enter key:")
    if k == 'Z':
       print ("Quit")
       exit()
