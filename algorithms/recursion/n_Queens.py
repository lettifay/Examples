import random

def n_Queens(num):
    def conflict(pos,positions):
        n = len(positions)
        for i in range(n):
            if abs(pos - positions[i]) in (0, n - i):
                return True
        return False
    
    def pretty_print(pos_list):
        num = len(pos_list)
        for pos in pos_list:
            print '. '*pos + 'X ' + '. '*(num - pos -1) 
    
    def getPosition(n, positions=[]):
        for pos in range(n):
            if not conflict(pos,positions):
                if n == len(positions) + 1:
                    yield [pos]
                else:
                    for pos_list in getPosition(n, positions + [pos]): #get pos_list from next row
                        yield [pos] + pos_list #give pos_list to former row
                
    solutions = list(getPosition(num))
    print 'number of solutions:',len(solutions)
    print 'one example:'
    pretty_print(random.choice(solutions))

# Main
# n=8 for Eight Queen Problem
n_Queens(8)

#output:

'''
number of solutions: 92
one example:
. . . . X . . . 
. X . . . . . . 
. . . X . . . . 
. . . . . X . . 
. . . . . . . X 
. . X . . . . . 
X . . . . . . . 
. . . . . . X .

'''