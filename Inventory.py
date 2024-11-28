def displayInventory(bag):
    print('Inventory:')
    c=0
    for i,j in bag.items():
        c+=int(j)
        print(str(j)+' '+i)
    print('Total number of items: '+str(c))

bag={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(bag)
