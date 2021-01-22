def are_valid_groups(N,G):

    for student in N:
        flag = False
        for group in G:
            for Member in group:
                if student == Member:
                    flag= True
                    break
            if flag:
                break
        if not flag:
            return False
    return flag
