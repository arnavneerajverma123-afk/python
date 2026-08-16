def cube(no_):
   return no_**3
def by_three(no_):
    if no_%3==0:
        return cube(no_)
    else:
        return False
print(by_three(9))
print(by_three(4))