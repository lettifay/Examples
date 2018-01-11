# Tower of Hanio problem

def Hanoi(n,src_loc,tmp_loc,dst_loc):
    if n == 1:
        print src_loc,'->',dst_loc
    else:
        Hanoi(n-1,src_loc,dst_loc,tmp_loc)
        Hanoi(1,src_loc,tmp_loc,dst_loc)
        Hanoi(n-1,tmp_loc,src_loc,dst_loc)

# Main        
Hanoi(3,'A','B','C')

# output:
'''
A -> C
A -> B
C -> B
A -> C
B -> A
B -> C
A -> C
'''
