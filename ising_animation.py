import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
from ising import metropolis_sweep


# Simulation parameters.
L = 100
temperature = 1.6
number_of_sweeps = 500
# Random initial configuration.
spins = np.random.choice([-1, 1], size=(L, L))

def main():

    # Maroon represents -1; gold represents +1.
    cmu_colors = ListedColormap(["#6D1E35", "#F2C14E"])


    # update function for the animation
    def update(frame):
       metropolis_sweep(spins, temperature)
       image.set_data(spins)
       magnetization = abs(np.mean(spins))
       title.set_text(
           "Two-Dimensional Ising Model\n"
           f"Sweep {frame + 1}   T = {temperature:.2f}   "
           f"|M| = {magnetization:.2f}"
       )
       return image, title

    fig, ax = plt.subplots(figsize=(6, 6))
    image = ax.imshow(spins, cmap=cmu_colors, vmin=-1, vmax=1)

    ax.set_xticks([])
    ax.set_yticks([])

    # A single two-line title avoids overlapping text.
    title = ax.set_title("Two-Dimensional Ising Model\nSweep 0", pad=10)

    # Keep this variable alive until the plot window is closed.
    animation = FuncAnimation(
        fig,
        update,
        frames=number_of_sweeps,
        interval=40,
        blit=False,
        cache_frame_data=False,
        repeat=False,
    )

    plt.tight_layout()
    plt.show()




if __name__ == "__main__":
    main()
