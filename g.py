import numpy as np
import matplotlib.pyplot as plt

data_v = np.array([5.8252, 5.7525, 5.4247, 4.9926, 4.5448, 4.4082, 3.8276, 3.5885, 3.0945, 2.6283, 2.3952, 1.9865, 1.6909, 1.3499, 0.9064, 0.6790, 0.5500, 0.4211, 0.2154, 0.1371])
data_ms = np.array([0.0295, 0.0422, 0.1013, 0.1858, 0.2787, 0.3125, 0.4560, 0.5152, 0.6841, 0.8530, 0.9375, 1.0980, 1.3176, 1.5709, 1.9003, 2.0693, 2.3480, 2.6351, 3.1334, 3.6571])

plt.figure(figsize=(10, 5))

plt.plot(data_ms, data_v, 'bo-', label='V por ms')
plt.title('Valores de Vr pelo tempo(ms)')
plt.xlabel('Tempo (ms)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()

plt.show()


