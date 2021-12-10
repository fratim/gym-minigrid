from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class DividedEnv(MiniGridEnv):
    """
    Environment with a divider with tunnel in the middle
    """

    def __init__(self, size):
        super().__init__(
            grid_size=size,
            max_steps=10*size*size
        )

    def _gen_grid(self, width, height):
        # Create an empty grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, width, height)

        # Place a goal in the bottom-right corner
        self.put_obj(Goal(), width - 2, height - 2)

        # Create a vertical splitting wall
        splitIdx = int(width/2)
        self.grid.vert_wall(splitIdx, 0)

        # Place the agent at a random position and orientation
        # on the left side of the splitting wall
        self.place_agent(size=(splitIdx, height))

        # Place a door in the wall
        doorIdx = int(width/2)
        self.put_obj(Door('yellow', is_locked=False), splitIdx, doorIdx)

        self.mission = "get to the goal"

class DividedEnv5x5(DividedEnv):
    def __init__(self):
        super().__init__(size=5)

class DividedEnv6x6(DividedEnv):
    def __init__(self):
        super().__init__(size=6)

class DividedEnv7x7(DividedEnv):
    def __init__(self):
        super().__init__(size=7)

class DividedEnv8x8(DividedEnv):
    def __init__(self):
        super().__init__(size=8)

class DividedEnv16x16(DividedEnv):
    def __init__(self):
        super().__init__(size=16)

register(
    id='MiniGrid-Divided-5x5-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5'
)

register(
    id='MiniGrid-Divided-6x6-v0',
    entry_point='gym_minigrid.envs:DividedEnv6x6'
)

register(
    id='MiniGrid-Divided-7x7-v0',
    entry_point='gym_minigrid.envs:DividedEnv7x7'
)

register(
    id='MiniGrid-Divided-8x8-v0',
    entry_point='gym_minigrid.envs:DividedEnv8x8'
)

register(
    id='MiniGrid-Divided-16x16-v0',
    entry_point='gym_minigrid.envs:DividedEnv16x16'
)
