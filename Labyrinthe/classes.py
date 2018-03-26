class DK:
    def __init__ (self):
        self.state = 0
        self.pos = [0, 0]
        self.sprites = ['dk_front', 'dk_back', 'dk_left', 'dk_right']

    def move (self, dir, free):
        if dir == 'bot':
            self.state = 0
            if self.pos[1] + 30 < 450 and free:
                self.pos[1] += 30
        elif dir == 'top':
            self.state = 1
            if self.pos[1] - 30 >= 0 and free:
                self.pos[1] -= 30
        elif dir == 'left':
            self.state = 2
            if self.pos[0] - 30 >= 0 and free:
                self.pos[0] -= 30
        elif dir == 'right':
            self.state = 3
            if self.pos[0] + 30 < 450 and free:
                self.pos[0] += 30

    def getState (self):
        return self.sprites[self.state]

    def getPos (self):
        return (self.pos[0], self.pos[1])
