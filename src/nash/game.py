"""A class for a normal form game"""
import numpy as np

class Game:
    """
    A class for a normal form game.

    Parameters
    ----------

        - A, B: 2 dimensional numpy array representing the payoff matrices for
          non zero sum games.
        - A: 2 dimensional numpy array representing the payoff matrix for a
          zero sum game.
    """
    def __init__(self, *args):
        if len(args) == 2:
            self.payoff_matrices = args
        if len(args) == 1:
            self.payoff_matrices = args[0], -args[0]
        self.zero_sum = np.array_equal(self.payoff_matrices[0],
                                       -self.payoff_matrices[1])

    def obtain_equilibria(self):
        """
        Obtain the Nash equilibria using support enumeration.

        Algorithm implemented here is Algorithm 3.4 of [NN2007]_
        with an aspect of pruning from [SLB2008]_.

        1. For each k in 1...min(size of strategy sets)
        2. For each I,J supports of size k
        3. Prune: check if supports are dominated
        4. Solve indifference conditions and check that have Nash Equilibrium.
        """
        pass