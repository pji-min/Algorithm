n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)

adjusted_scores = [(score / max_score) * 100 for score in scores]
new_average = sum(adjusted_scores) / n

print(new_average)
