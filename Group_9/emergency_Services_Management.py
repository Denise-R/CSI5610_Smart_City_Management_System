"""
Irma Rrushi
Part 6: Emergency Services Management (01 Matrix)
"""
"""
If we think of the city as a grid, where the emergency services are located in cells with value  0 and the other cells are 1. 
The algorithm would find the ETA of the emergency services. Example, if something happens at cell x and  if the shortest distance
is 3 from the nearest 0/emergency service, then the ETA would be let’s say 3 min.
"""

class Solution:
    
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        m = len(mat)                          #get the number of rows
        n = len(mat[0])                       #get the number of columns
        for _ in range(2):                    #repeat twice
            for i in range(m):                #for every cell in the matrix 
                for j in range(n):
                    if mat[i][j] > 0:         #for nonzero cell value
                        left = float('inf')   #initialize the variables left, right, up and down to inf
                        right = float('inf')
                        up = float('inf')
                        down = float('inf')
                        if (j != 0):          # left cell not defined
                            left=mat[i][j-1]
                        if(j !=  n-1):        # right cell not defined
                            right=mat[i][j+1] 
                        if(i != 0):           # up cell not defined
                            up=mat[i-1][j] 
                        if(i != m-1):         # down cell not defined
                            down=mat[i+1][j]
                        mat[i][j] = min(left, right, up, down) + 1     #assign to the cell the minimum between the neighbor cells plus 1
        
        return mat           #return matrix
