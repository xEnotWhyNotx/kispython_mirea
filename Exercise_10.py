class MealyError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Mealy:
    def __init__(self):
        self.state = 'A'

    def exit(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'H':
            self.state = 'E'
            return 11
        if self.state == 'E':
            self.state = 'A'
            return 7
        else:
            raise MealyError('exit')

    def dash(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'F'
            return 3
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'H'
            return 9
        else:
            raise MealyError('dash')

    def cue(self):
        if self.state == 'C':
            self.state = 'C'
            return 4
        if self.state == 'G':
            self.state = 'G'
            return 10
        if self.state == 'D':
            self.state = 'E'
            return 5
        if self.state == 'E':
            self.state = 'F'
            return 6
        else:
            raise MealyError('cue')


def test():
    o = main()
    o.exit()  # 0
    o.dash()  # 1
    o.cue()  # 4
    o.exit()  # 2
    o.cue()  # 5
    try:
        o.dash()  # MealyError
    except MealyError:
        pass
    o.cue()  # 6
    o.dash()  # 8
    o.cue()  # 10
    o.cue()  # 10
    try:
        o.exit()  # MealyError
    except MealyError:
        pass
    o.dash()  # 9
    o.exit()  # 11
    o.exit()  # 7
    o.exit()  # 0
    o.dash()  # 1
    o.dash()  # 3
    o.dash()  # 8

    o = main()
    try:
        o.dash()  # MealyError
    except MealyError:
        pass
    o.exit()  # 0
    o.dash()  # 1
    o.cue()  # 4
    o.cue()  # 4
    o.dash()  # 3
    o.dash()  # 8
    try:
        o.exit()  # MealyError
    except MealyError:
        pass
    o.cue()  # 10
    o.dash()  # 9
    o.exit()  # 11
    o.exit()  # 7
    try:
        o.cue()  # MealyError
    except MealyError:
        pass
    o.exit()  # 0
    try:
        o.cue()  # MealyError
    except MealyError:
        pass
    o.dash()  # 1
    o.cue()  # 4
    o.exit()  # 2
    try:
        o.exit()  # MealyError
    except MealyError:
        pass
    o.cue()  # 5
    o.cue()  # 6


def main():
    return Mealy()


test()
