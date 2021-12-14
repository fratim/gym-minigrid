from gym_minigrid.minigrid import *
from gym_minigrid.register import register

class DividedEnv(MiniGridEnv):
    """
    Environment with a divider with tunnel in the middle
    """

    def __init__(self, size, random_goals, max_box_strength):

        self.random_goals = random_goals
        self.max_box_strength = max_box_strength

        super().__init__(
            grid_size=size,
            max_steps=10*size*size
        )


    def place_box(self, configuration):
        if self.max_box_strength is not None:
            if configuration and configuration.box_strength is not None:
                box_strength = configuration
            else:
                box_strength = np.random.randint(0, self.max_box_strength)

            self.put_obj(Box(strength=box_strength), int(self.width / 2), int(self.height / 2))

        else:
            # # Place free cell in middle
            doorIdx = int(self.width / 2)
            self.grid.free_cell(doorIdx, doorIdx)
            box_strength = -1

        return box_strength

    def set_up_goal(self, configuration):
        # Place a goal goal
        if configuration and configuration.goal_pos is not None:
            goal_pos = configuration.goal_pos
        else:
            if self.random_goals:
                goal_pos = self.get_possible_location()
            else:
                goal_pos = (self.width - 2, self.height - 2)

        self.put_obj(Goal(), *goal_pos)

        return goal_pos

    def set_up_agent(self, goal_pos, configuration):
        # Place the agent at a random position and orientation
        if configuration and configuration.agent_state is not None:
            assert configuration.agent_dir is not None
            self.place_agent(configuration.agent_pos, configuration.agent_dir)
        else:
            goal_x = goal_pos[0]
            box_width = math.floor((self.width-2)/2)
            box = (box_width, self.height-2)
            if goal_x > (self.width/2):
                top = (1, 1)
            else:
                top = (math.ceil(self.width / 2), 1)
            self.place_agent(top, box)  # place agent at random starting position on the other side of the grid

    def set_up_walls(self):
        # Generate the surrounding walls
        self.grid.wall_rect(0, 0, self.width, self.height)

        # Create a vertical splitting wall
        self.grid.vert_wall(int(self.width / 2), 0)

    def _gen_grid(self, configuration):
        # Create an empty grid
        self.grid = Grid(self.width, self.height)

        # set up walls
        self.set_up_walls()

        # place box or leave middle cell empty
        box_strength = self.place_box(configuration)

        # determine and fix goal position
        goal_pos = self.set_up_goal(configuration)

        # determine and fix agent position
        self.set_up_agent(goal_pos, configuration)

        # create mission statement
        self.mission = f"get to the goal by destroying the box of strength {box_strength}"


## environment without box and with goal in bottom right corner
class DividedEnv5x5(DividedEnv):
    def __init__(self):
        super().__init__(size=5, random_goals=False, max_box_strength=None)

## environment without box and with random goals
class DividedEnv5x5xRandGoals(DividedEnv):
    def __init__(self):
        super().__init__(size=5, random_goals=True, max_box_strength=None)

## environment with box of strength 1 and with goal in bottom right corner
class DividedEnv5x5xBox1(DividedEnv):
    def __init__(self):
        super().__init__(size=5, random_goals=False, max_box_strength=1)

## environment with box of strength 4 and with goal in bottom right corner
class DividedEnv5x5xBox4(DividedEnv):
    def __init__(self):
        super().__init__(size=5, random_goals=False, max_box_strength=4)

## environment with box of strength 1 and with random goals
class DividedEnv5x5xRandGoalsxBox1(DividedEnv):
    def __init__(self):
        super().__init__(size=5, random_goals=True, max_box_strength=1)

## environment with box of strength 4 and with random goals
class DividedEnv5x5xRandGoalsxBox4(DividedEnv):
    def __init__(self):
        super().__init__(size=5, random_goals=True, max_box_strength=4)


register(
    id='MiniGrid-Divided-5x5-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5'
)

register(
    id='MiniGrid-Divided-5x5-RandGoals-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5xRandGoals'
)

register(
    id='MiniGrid-Divided-5x5-Box1-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5xBox1'
)

register(
    id='MiniGrid-Divided-5x5-Box4-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5xBox4'
)

register(
    id='MiniGrid-Divided-5x5-RandGoals-Box1-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5xRandGoalsxBox1'
)

register(
    id='MiniGrid-Divided-5x5-RandGoals-Box4-v0',
    entry_point='gym_minigrid.envs:DividedEnv5x5xRandGoalsxBox4'
)
