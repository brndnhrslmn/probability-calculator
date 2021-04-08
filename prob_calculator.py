import copy
import random
# Consider using the modules imported above.


class Hat:

    def __init__(self, **balls) -> None:
        self.contents = []

        # build a list of balls corrsponding to the colours and quantities entered
        for colour, quantity in balls.items():
            for i in range(quantity):
                self.contents.append(colour)

    # a method to draw and remove random balls from the hat
    def draw(self, quantity) -> list:
        draw = []
        if quantity >= len(self.contents):
            return self.contents
        for i in range(quantity):
            draw.append(self.contents.pop(
                random.randrange(len(self.contents))))
        return draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments) -> float:
    M = 0
    N = num_experiments
    flag = False

    # make a backup of the hat
    # call draw() method to draw balls
    # compare drawn balls to expected and record
    for i in range(N):
        backup = copy.deepcopy(hat)
        drawn = backup.draw(num_balls_drawn)
        for colour, quantity in expected_balls.items():
            if drawn.count(colour) < quantity:
                flag = False
                break
            else:
                flag = True

        if flag == True:
            M += 1
    return M/N
