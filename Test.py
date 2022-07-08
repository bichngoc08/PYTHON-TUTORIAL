import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(18, 6))
z = np.linspace(-3, 3, 100)


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


y0 = -np.log(1 - sigmoid(z))  # Trường hợp ground truth = 0
y1 = -np.log(sigmoid(z))  # Trường hợp ground truth = 1

# Hàm mất mát nếu ground truth = 1
ax[0].plot(z, y1)
ax[0].set_xlabel('z')
ax[0].set_ylabel('L(y, yhat)')
ax[0].set_title('y=1')

# Hàm mất mát nếu ground truth = 0
ax[1].plot(z, y0)
ax[1].set_xlabel('z')
ax[1].set_ylabel('L(y, yhat)')
ax[1].set_title('y=0')

plt.show()
