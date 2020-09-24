number = input('enter your phone number: ')
def world(phone):
    if len(phone) != 12:
         return False 
    for be in range(0, 3):
        if not phone[be].isdecimal():
            return False 
    if phone[3] != '-':
        return False 
    for be in range(4, 7):
        if not phone[be].isdecimal():
            return False 
    if phone[7] != '-':
        return False 
    for be in range(8, 12):
        if not phone[be].isdecimal():
            return False 
    return True 
print(world(number))

 




# print(world('415-555-4242'))                                                                                                                                                                                                                                                                    