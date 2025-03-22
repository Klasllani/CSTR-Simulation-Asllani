import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_rectangular_pulse_response(V, F, k, pulse_start, pulse_end):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create transfer function
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    # Create time vector and input
    t = np.linspace(0, 100, 1000)
    u = np.zeros_like(t)
    u[(t >= pulse_start) & (t <= pulse_end)] = 1
    
    # Simulate system response
    t, response, _ = signal.lsim(system, U=u, T=t)
    
    # Find key points in response
    rising_idx = np.argmin(np.abs(t - pulse_start))
    falling_idx = np.argmin(np.abs(t - pulse_end))
    
    # Find time to reach 63.2% of final value (1 time constant)
    target_rise = 0.632 * K
    rise_point = np.argmin(np.abs(response[rising_idx:falling_idx] - target_rise)) + rising_idx
    
    # Create plot with improved styling
    plt.figure(figsize=(10, 8))
    
    # Plot in two subplots for better visibility
    plt.subplot(2, 1, 1)
    plt.plot(t, u, 'g--', linewidth=2, label='Pulse Input (Ca₀)')
    plt.title('Rectangular Pulse Input to CSTR', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Input Value [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    
    plt.subplot(2, 1, 2)
    plt.plot(t, response, 'b-', linewidth=2, label='System Response')
    
    # Mark the time constant
    plt.plot(t[rise_point], response[rise_point], 'ro')
    plt.annotate(f'τ = {tau:.2f} s', 
                 xy=(t[rise_point], response[rise_point]),
                 xytext=(t[rise_point] + 5, response[rise_point] - 0.1),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    # Mark the start and end of the pulse response
    plt.axvline(x=pulse_start, color='r', linestyle='--', alpha=0.5)
    plt.axvline(x=pulse_end, color='r', linestyle='--', alpha=0.5)
    
    plt.title('CSTR Response to Rectangular Pulse', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Concentration of A [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_rectangular_pulse_response(1.0, 0.5, 0.1, 20, 40)
