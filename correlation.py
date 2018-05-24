### Correlation and Regression Lines - A Quick Recap #1
# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem

physics_scores = [15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
history_scores = [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

mean_physics = sum(physics_scores)/len(physics_scores)
mean_history = sum(history_scores)/len(history_scores)

cov = 0
for i in range(len(physics_scores)):
    a = physics_scores[i] - mean_physics
    b = history_scores[i] - mean_history
    cov += a*b

s1 = 0
for o in range(len(physics_scores)):
    a = (physics_scores[o] - mean_physics)**2
    s1 += a

s2 = 0
for y in range(len(physics_scores)):
    f = (history_scores[y] - mean_history)**2
    s2 += f

var = (s1*s2)**(1/2)

r = cov / var

print(round(r, 3))