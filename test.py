with open('mouse_log.txt', 'r') as f:
    a =f.readlines()
    
    for line in a:
        if 'Press' in line:
            p = line.split('"')
            print("'"+p[1].replace('Key.','').replace("'","")+"'")
        elif 'KeyUp' in line:
            k = line.split('"')
            print("'"+k[1].replace('Key.','').replace("'","")+"'")
        elif 'scrollh' in line:
            s = line.split(',')
            print(s[3].replace('\n',''),s[0],s[1]) # s[3].replace('\n',''),x=s[0],y=s[1]
        elif 'Button' in line:
            c = line.split(',')
            print(c[0],c[1],c[2].replace('Button.','')) # x=c[0],y=c[1],button=c[2].replace('Button.','')