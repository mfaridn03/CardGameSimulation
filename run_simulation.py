from game import Game
from __players import PlayerA, PlayerB, PlayerC, PlayerN

if __name__ == "__main__":
    g = Game([PlayerA(), PlayerB(), PlayerC(), PlayerN()])
    g.play()
