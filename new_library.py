


class ArithmeticOperations:

    def __init__(self):
        self.sum_ = 0

    def get_sum(self, num1, num2):
        self.sum_ = num1 + num2
        return self.sum_
    
def TurtleDoodle():
    import turtle as t
    from random import random
    for i in range(100):
        steps = int(random() * 100)
        angle = int(random() * 360)
        t.right(angle)
        t.fd(steps)

