import numpy as np

def f(x, y):
    return 0.5 * np.sin(x + y)

def inverse_transform_sampling():
    # Генерация равномерно распределенных случайных величин U1 и U2
    u1 = np.random.uniform(0, 1)
    u2 = np.random.uniform(0, 1)

    # Обратная функция распределения
    x = np.arcsin(2 * u1 - 1)
    y = np.arcsin(2 * u2 - 1)

    return x, y

# Генерация 1000 двумерных случайных величин
num_samples = 1000
samples = []
for _ in range(num_samples):
    x, y = inverse_transform_sampling()
    samples.append((x, y))

# Визуализация сгенерированных значений
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg')

x_samples = [sample[0] for sample in samples]
y_samples = [sample[1] for sample in samples]

plt.scatter(x_samples, y_samples, s=5)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Generated Samples')
plt.show()