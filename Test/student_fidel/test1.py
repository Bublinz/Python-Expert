# Game inventory
jack = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def number(me):
    print('display Inventory:')
    sum = 0
    for k, v in me.items(): 
        print(str(v)+ ' ' + k)
        sum +=v
        
    print('Total number of inventory: ' + str(sum))
number(jack)
    
