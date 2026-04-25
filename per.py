if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    def averageScore (scores): 
        return format(sum(scores)/len(scores),".2f") 
    print(averageScore(student_marks[query_name]))
