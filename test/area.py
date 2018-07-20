import math

# 计算图形面积 Ywx


class Area:
    def __init__(self, a, b=0):
        self.a = a
        self.b = b
        self.pi = 3.14

    # 三角形
    def triangle_area(self, c):
        """ 海伦公式计算三角形面积 """
        p = (self.a + self.b + c) / 2
        ar = p * (p - self.a) * (p - self.b) * (p - c)
        if ar > 0:
            area = math.sqrt(ar)
            return round(area, 2)
        else:
            return "请输入正确的三条边！"

    # 等边三角形
    def triangle_eq_area(self):
        p = (self.a * 3) / 2
        ar = p * pow((p - self.a), 3)
        if ar > 0:
            area = math.sqrt(ar)
            return round(area, 2)
        else:
            return "请输入正确的三条边！"

    # 计算长方形面积
    def rectangle_area(self):
        area = self.a * self.b
        return area

    # 计算正方形面积
    def square_area(self):
        area = pow(self.a, 2)
        return area

    # 计算菱形面积
    def diamond_area(self):
        area = (self.a * self.b) / 2
        return area

    # 计算圆形面积
    def circular_area(self):
        area = self.pi * pow(self.a, 2)
        return area

    # 计算椭圆面积
    def ellipse_area(self):
        area = self.a * self.b * self.pi
        return area

    # 计算梯形面积
    def trapezoid_area(self, h):
        area = ((self.a + self.b) * h) / 2
        return area


# 实例化面积类
area = Area(3, 4)
print(area.triangle_area(5))

eq_tri = Area(6)
print(eq_tri.triangle_eq_area())

print(area.rectangle_area())

print(area.square_area())

print(area.diamond_area())

print(area.circular_area())

print(area.ellipse_area())

print(area.trapezoid_area(6))
