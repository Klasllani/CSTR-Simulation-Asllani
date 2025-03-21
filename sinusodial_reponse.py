import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_sinusoidal_response(V, F, k, frequency=0.1, amplitude=1.0, duration=100):
    tau = V / (F + V * k)
    num = [1]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    t = np.linspace(0, duration, 1000)
    u = amplitude * np.sin(2 * np.pi * frequency * t)
    t, response, _ = signal.lsim(system, u, t)
    
    plt.figure(figsize=(10, 6))
    plt.subplot(2, 1, 1)
    plt.plot(t, u)
    plt.title('Sinusoidal Input')
    plt.xlabel('Time [s]')
    plt.ylabel('Input')
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(t, response)
    plt.title('CSTR Sinusoidal Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_sinusoidal_response(1.0, 0.5, 0.1)
