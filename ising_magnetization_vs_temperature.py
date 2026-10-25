import numpy as np
import matplotlib.pyplot as plt
from ising import metropolis_sweep

np.random.seed(42)

L = 40
temperatures = np.linspace(1.0, 4.0, 25)
mean_magnetizations = []

for temperature in temperatures:
    # An ordered start equilibrates efficiently at low temperature.
    spins = np.ones((L, L), dtype=int)

    # Equilibrate the lattice before measuring.
    for sweep in range(300):
        metropolis_sweep(spins, temperature)

    measurements = []
    for sweep in range(500):
        metropolis_sweep(spins, temperature)
        measurements.append(abs(np.mean(spins)))

    mean_magnetizations.append(np.mean(measurements))


plt.figure(figsize=(7, 5))
plt.plot(
    temperatures,
    mean_magnetizations,
    "o-",
    color="#6D1E35",
    markerfacecolor="#F2C14E",
    markeredgecolor="#6D1E35",
    label="Simulation",
)
plt.axvline(2.269, color="black", linestyle="--", label=r"$T_c \approx 2.269$")
plt.xlabel("Temperature, T")
plt.ylabel(r"Mean magnetization, $\langle |M| \rangle$")
plt.title("Magnetization of the 2D Ising Model")
plt.ylim(0, 1.05)
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()
plt.savefig("ising_magnetization_vs_temperature.png", dpi=180)
