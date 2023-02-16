class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here

    def area(self):
        return self.a * self.b / 2

    def is_right_triangle(self):
        return pow(self.c, 2) == pow(self.a, 2) + pow(self.b, 2)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
triangle = RightTriangle(input_c, input_a, input_b)

if triangle.is_right_triangle():
    print(triangle.area())
else:
    print('Not right')
