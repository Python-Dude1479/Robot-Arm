import sys
import pico_ik_lib as ik
import servo_lib as sl

ik_solver = ik.robot_arm()
arm = sl.Servo()
arm.add_servo([9, 10])

def parse_coords(msg):
    try:
        x_str, y_str = msg.strip().split(',')
        return float(x_str), float(y_str)
    except Exception as e:
        print("Parse error:", e)
        return None, None

while True:
    line = sys.stdin.readline()
    if line:
        angles = parse_coords(line)
        if angles:
            iks = ik_solver.ik_solutions(angles[0], angles[1], 85, 140)
            sol = iks[1][1][:2]
            t1 = sol[1] * 180 / 3.1415
            t2 = (sol[0] * 180 / 3.1415) + 90
            t2 = ik_solver.remap(t2, 90, -90, 600, 2400)
            arm.write([t1, t2], [True, False])
