from game import Game
from __players import PlayerA, PlayerB, PlayerC, PlayerD

if __name__ == "__main__":
    g = Game([PlayerA(), PlayerB(), PlayerC(), PlayerD()])
    g.play()
