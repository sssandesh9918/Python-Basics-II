# Imagine you are creating a Super Mario game. You need to define
# a class to represent Mario. What would it look like? If you aren't
# familiar with SuperMario, use your own favorite video or board game
# to model a player.
class mario:
    def __init__(self,username,coins,score,time):
        self.username=username
        self.coins=coins
        self.score=score
        self.time=time
    def move_forward(self):
        return f'{self.username} has {score self.score}'
    def move_upward(self):
        return f'{self.username} has {score self.score}'
    def jump(self):
        return f'{self.username} has {score self.score}''
    def game_over(self):
        return f'{self.username}, your game is over'
m1=mario('Sandesh','500','422525','1452')
m2=mario('Hari','524','522636','1300')
print(m1.move_forward())
print(m1.move_upward())
print(m2.jump())
print(m1.game_over())
