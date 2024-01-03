import random
import math

def f(x, y):
    return (1/2) * math.sin(x + y)

def monte_carlo_mean(num_samples):
    sum_values = 0
    res = []

    for _ in range(num_samples):
        x = random.uniform(0, math.pi / 2)  # Генерация случайного значения x от 0 до pi
        y = random.uniform(0, math.pi / 2)  # Генерация случайного значения y от 0 до pi
        z = random.uniform(0, 1)
        if f(x, y) > z:
            sum_values += f(x, y)
            res.append(f(x, y))

    mean = sum(res) / len(res)
    return mean

num_samples = 10000000
mean = monte_carlo_mean(num_samples)
print("Математическое ожидание:", round(mean, 8))