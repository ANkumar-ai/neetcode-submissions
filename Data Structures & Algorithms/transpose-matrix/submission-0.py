class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:


        # [[row[0][0],row[1][0]],[row[0][1],row[1][1]],[row[0][2],row[1][2]]]

            matr=[]

            for j in range(len(matrix[0])):

                mat=[]

                for i in range(len(matrix)):

                    mat.append(matrix[i][j])

                matr.append(mat)

            return matr

                






        