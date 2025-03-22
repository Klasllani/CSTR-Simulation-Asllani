import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_impulse_response(V, F, k):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create transfer function
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    # Simulate impulse response
    t, response = signal.impulse(system)
    
    # Scaling time to see more of the response
    t = t * 5
    
    # Find the peak of the response
    peak_idx = np.argmax(response)
    peak_time = t[peak_idx]
    peak_value = response[peak_idx]
    
    # Calculate time when response decays to 36.8% (1/e) of peak
    decay_target = peak_value / np.e
    decay_idx = np.argmin(np.abs(response[peak_idx:] - decay_target)) + peak_idx
    decay_time = t[decay_idx]
    
    # Create plot with improved styling
    plt.figure(figsize=(10, 6))
    plt.plot(t, response, 'b-', linewidth=2)
    
    # Mark the peak
    plt.plot(peak_time, peak_value, 'ro')
    plt.annotate(f'Peak: {peak_value:.4f} at t={peak_time:.2f}s', 
                 xy=(peak_time, peak_value),
                 xytext=(peak_time + 0.5, peak_value),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    # Mark the time constant
    plt.plot(decay_time, decay_target, 'go')
    plt.annotate(f'τ = {tau:.2f} s', 
                 xy=(decay_time, decay_target),
                 xytext=(decay_time + 0.5, decay_target - 0.02),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    # Add theoretical curve
    theoretical_curve = (K/tau) * np.exp(-t/tau)
    plt.plot(t, theoretical_curve, 'r--', linewidth=1, alpha=0.7, 
             label=f'Theoretical: (K/τ)e^(-t/τ)')
    
    plt.title('CSTR Impulse Response', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Concentration of A [mol/m³]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    
    # Add system parameters in the corner
    plt.annotate(f'System Parameters:\nV = {V} m³\nF = {F} m³/s\nk = {k} 1/s\nτ = {tau:.2f} s\nK = {K:.2f}',
                 xy=(0.02, 0.02), xycoords='axes fraction',
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_impulse_response(1.0, 0.5, 0.1)
