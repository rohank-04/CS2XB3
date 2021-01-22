def are_valid_groups(n,g):

    
    for student in n:
        curr = False
       
            for groupMember in group:
                if student == groupMember:
                    curr = True
                    break
            if curr == True:
                break
            
        if curr == False:
            return False
    
