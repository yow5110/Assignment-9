# Week 11 Task 1

In this assignment we will implement a 2D random walk model on a square lattice for one particle with proper vectorization. 

For every step in 2D, you'll make a choice between up, down, left, and right = [1,0], [0,-1], [-1,0], [0,1]. You may be tempted to write 

x_list = rng.choice([-1,1])

y_list = rng.choice([-1,1])

and stitch them together to form your steps, but then you'll run into diagonal steps like [1,1] every once in a while, which is not a valid move, so we have to find another way. One way is to generate a random array of *angles* (0,80,180,270 degrees) all at once and then convert them into x and y components using array operations. A template following this approach is provided, but feel free to use any other time-efficient approach you prefer. 

You can use for loops for prototyping and vectorize things later. Ideally, the final code would not need any for loop. Your Task 1 code will need to be fast enough in preparation of the the multi-particle simulation for 1000 particles and 10000 steps in the next two Tasks. 

At the end, a plotting section is provided to show the trajectory of the particle and its starting / ending points in green / red. A sample image is attached.

