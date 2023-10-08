import numpy as np
import matplotlib.pyplot as plt

# Dados de exemplo
x = np.array([9.156, 14.722, 24.955, 33.573, 46.858, 54.399, 63.016])
y = np.array([1.387, 1.151, 0.688, 0.349, -0.341, -0.655, -1.177])

# Realize um ajuste linear usando a função polyfit do NumPy
coefficients = np.polyfit(x, y, 1)
slope, intercept = coefficients

# Crie uma linha de tendência com os coeficientes obtidos
line_of_best_fit = slope * x + intercept

# Imprima a função da reta
print(f"A função da reta é: y = {slope}x + {intercept}")

# Crie um gráfico de dispersão
plt.scatter(x, y, label='Dados de exemplo')

# Plote a linha de tendência
plt.plot(x, line_of_best_fit, label='Linha de tendência', color='red')

# Adicione rótulos e uma legenda
plt.xlabel('Tempo em microsegundos')
plt.ylabel('Ln(V/Volt)')
plt.legend()

# Mostre o gráfico
plt.show()
