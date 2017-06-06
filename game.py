import random

import canvasTest
import Galaxy
import Settlement


class Game:
    current_time = 0

    def __init__(self):


        self.initial_setup()

    @classmethod
    def initial_setup(cls):
        cls.galaxy = Galaxy.Galaxy()
        cls.current_system = cls.galaxy.systems[0]

    @classmethod
    def update(cls, dt):
        cls.current_time += dt

    @classmethod
    def set_current_system(cls, name):
        system_index = cls.galaxy.systemNames.index(name)
        cls.current_system = cls.galaxy.systems[system_index]



game = Game()
app = canvasTest.SpaceGame(game)
app.mainloop()