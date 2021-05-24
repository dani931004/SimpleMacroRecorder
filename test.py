with open('mouse_log.txt', 'r') as f:
    a = f.readlines()
    for i in a:
        if 'Button' in i:
            print('Click')
        else:
            print('Scroll')