import math

class arm_data:
    theta2a = None
    theta2b = None
    theta3 = None
    theta2 = None 
    theta4 = None
    theta1 = None
    d = None
    cos_theta2 = None
    sin_theta2 = None
    elbow = None
    angles = None 

class robot_arm:
    def __init__(self):
        self.data = arm_data()
    def ik_solutions(self,x, y, L1, L2):
        def hypot(a, b):
            return (a * a + b * b) ** 0.5

        self.data.d = hypot(x, y)
        if self.data.d > L1 + L2 or self.data.d < abs(L1 - L2):
            return None  # Unreachable

        self.data.cos_theta2 = (x * x + y * y - L1 * L1 - L2 * L2) / (2 * L1 * L2)
        self.data.sin_theta2 = math.sqrt(1 - self.data.cos_theta2 * self.data.cos_theta2)

        self.data.theta2a = math.atan2(self.data.sin_theta2, self.data.cos_theta2)
        self.data.theta2b = math.atan2(-self.data.sin_theta2, self.data.cos_theta2)


        def compute(theta2):
            self.data.theta3 = math.atan2(L2 * math.sin(theta2), L1 + L2 * math.cos(theta2))
            self.data.theta4 = math.atan2(y, x)
            self.data.theta1 = self.data.theta4 - self.data.theta3

            self.data.elbow = [L1 * math.cos(self.data.theta1), L1 * math.sin(self.data.theta1)]
            self.data.angles = [theta2, self.data.theta1, self.data.theta3, self.data.theta4]
            return self.data.elbow, self.data.angles

        return compute(self.data.theta2a), compute(self.data.theta2b)
    @staticmethod
    def remap(value, from_min, from_max, to_min, to_max):
        return to_min + (to_max - to_min) * (value - from_min) / (from_max - from_min)