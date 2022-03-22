Objective: return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it:
Level: Easy
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasc_triang = []
        for i in range(numRows):
            current_row = []
            for j in range(i+1):
                num = 1
                if j==0 or j==i:
                    current_row.append(num)
                    continue                
                if i>=2:                    
                    num = prev_row[j-1]+prev_row[j]
                current_row.append(num)
            prev_row = current_row
            pasc_triang.append(current_row)
        return pasc_triang
