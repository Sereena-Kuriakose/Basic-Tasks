def group_members(group_data, n):
    for value in group_data:
        if  value ==n:
            return True
    return False
print(group_members([1,2,3,4], 2))