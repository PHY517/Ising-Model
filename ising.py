import numpy as np

def metropolis_sweep(spins, temperature):
    """Perform one Metropolis sweep of the lattice."""
    L = spins.shape[0]

    for i in range(L):
     for j in range(L):
        # Sum the four neighbors using periodic boundaries.
        neighbors = (
            spins[(i + 1) % L, j]
            + spins[(i - 1) % L, j]
            + spins[i, (j + 1) % L]
            + spins[i, (j - 1) % L]
        )

        delta_E = 2 * spins[i, j] * neighbors

        # Metropolis acceptance rule, with J = k_B = 1.
        if delta_E <= 0 or np.random.random() < np.exp(-delta_E / temperature):
            spins[i, j] *= -1
     


