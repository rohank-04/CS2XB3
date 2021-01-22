def are_valid_groups(n,g):

    curr = False
    for student in n:
        curr = False
        for group in g:
            for groupMember in group:
                if student == groupMember:
                    curr = True
                    break
            if curr == True:
                break
            
        if curr == False:
            return False
    return True
