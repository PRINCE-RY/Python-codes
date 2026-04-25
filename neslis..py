if __name__ == '__main__':
    names = []
    scores = []
    unique_scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
        unique_scores.add(score)
        
    records = [[name, record] for name, record in zip(names, scores)]
    records.sort(key=lambda x: x[0])
    sortered_scores = sorted(unique_scores)
    
    for name_and_score in records:
        if name_and_score[1] == sortered_scores[1]:
            print(name_and_score[0])
        else:
            continue
