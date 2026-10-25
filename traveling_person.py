import numpy as np
import matplotlib.pyplot as plt


N = 20
cities = np.random.rand(N, 2)


def distance(route):

    path = cities[np.append(route, route[0])]

    return np.sum(
        np.sqrt(np.sum(np.diff(path, axis=0)**2, axis=1))
    )


def accept(delta, T):

    return delta < 0 or np.random.random() < np.exp(-delta/T)


def annealing():

    route = np.random.permutation(N)
    T = 1.0

    for step in range(100000):

        # Propose a new route
        new_route = route.copy()

        i, j = np.random.choice(N, 2, replace=False)
        new_route[i], new_route[j] = new_route[j], new_route[i]

        # Accept or reject
        delta = distance(new_route) - distance(route)

        if accept(delta, T):
            route = new_route

        # Cool down
        T *= 0.999

    return route


route = annealing()


# Plot result
path = cities[np.append(route, route[0])]

plt.plot(path[:, 0], path[:, 1], '-o')
plt.axis('equal')
plt.grid()
plt.show()


