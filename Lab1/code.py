def are_valid_groups(n,g):

    empty = []

    for student in n:
        if student in empty:
            return False
        else:
            empty += [student]

    curr = False
    for student in n:
        curr = False
        for group in g:
            if ((len(group) != 3) and (len(group) != 2)):
                # Group size is not 2 or 3
                return False
            for groupMember in group:
                if student == groupMember:
                    curr = True
                    break
            if curr == True:
                break
            
        if curr == False:
            return False
    return True




# n = [1,2,3,4,5,6]
# g = [[1,2],[3,4],[5,6,7,9]]
# print(are_valid_groups(n,g))