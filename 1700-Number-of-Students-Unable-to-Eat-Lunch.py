class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        j,i,n=0,0,len(students)
        while (n != i):
            if students[0] == sandwiches[j]:
                j+=1
                students.pop(0)
                i=0
                n = len(students)
            else:
                temp=students.pop(0)
                students.append(temp)
                i+=1
        return len(students)        

        