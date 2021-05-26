with open('mouse_log.txt', 'r') as f:
    a =f.readlines()
    
    for line in a:
        if 'Press' in line:
            p = line.split('"')
            print('Press',"'"+p[1].replace('Key.','').replace("'","")+"'")
        elif 'KeyUp' in line:
            k = line.split('"')
            print('KeyUp',"'"+k[1].replace('Key.','')+"'")
        elif 'scrollh' in line:
            s = line.split(',')
            print('Scroll', s[0],s[1],s[3].replace('\n',''))
        elif 'Button' in line:
            c = line.split(',')
            print('Click', c[0],c[1],c[2].replace('Button.',''))