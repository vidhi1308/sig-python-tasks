print("name - VIDHI SHARMA  roll no - 1900300100242")
class circle:
    def __init__(self, radius):
        self.r = radius

    def getArea(self):
        return 3.14 * self.r * self.r
    def getCircumference(self):
        return 2 * 3.14 * self.r
    pass

rad=int(input("Enter radius = "))
c=circle(rad)
print("Area =", c.getArea())
print("Circumference =", c.getCircumference())