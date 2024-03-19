import numpy as np
import matplotlib.pyplot as plt

def pendulum_motion(theta0, length, g, time):
    omega0 = 0
    dt = 0.01
    theta = theta0
    omega = omega0
    theta_list = []
    time_list = []
    for t in np.arange(0, time, dt):
        alpha = -(g/length) * np.sin(theta)
        omega += alpha * dt
        theta += omega * dt
        theta_list.append(theta)
        time_list.append(t)
    return time_list, theta_list

length = 1.0
g = 9.8
theta0 = np.pi/4
time = 10

time_list, theta_list = pendulum_motion(theta0, length, g, time)
plt.plot(time_list, theta_list)
plt.xlabel('Time (s)')
plt.ylabel('Angle (rad)')
plt.title('Pendulum Motion Simulation')
plt.show()
