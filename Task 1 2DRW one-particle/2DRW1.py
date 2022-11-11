def rw2d(Nstep):
    """
    A simulation for 2D random walk for a single particle.
    Nstep = the number of steps each particle takes
    """

    Nstep=int(Nstep)
    rng = np.random.default_rng()

    # Individual steps in x and y
    angles = 
    x_list = # a 1D array of dimensions Nstep
    y_list = # a 1D array of dimensions Nstep
    
    # x,y trajectories of the particle
    x_traj = # a 1D array of size Nstep using cumulative sum
    y_traj = # a 1D array of size Nstep using cumulative sum
    
    #plotting
    fig, ax1 = plt.subplots(1)
    ax1.plot(0, 0, 'go')  #highlight the initial position
    ax1.plot(x_traj[-1], y_traj[-1], 'ro')  #highlight the final position
    ax1.plot(x_traj, y_traj, 'k-') #particle trajectory
    ax1.set_aspect('equal', 'box')
    plt.show()
        
rw2d(Nstep=1e4)