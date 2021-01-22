
def are_valid_groups(n,g):

    curr = False
    for student in n:
        curr = False
        for group in g:
            for groupMember in group:
                if student == groupMember:
                    curr = True
                    break
            
        if curr == False:
            return False
    return True








n = [1,2,3,4,5,8]
g = [[1,2],[3,4],[5,6]]

print(are_valid_groups(n,g))