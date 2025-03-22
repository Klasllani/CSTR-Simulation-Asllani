import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_ramp_response(V, F, k):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create transfer function
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    # Create time vector and input
    t = np.linspace(0, 100, 1000)
    u = t / 100  # Normalize to have a slower ramp
    
    # Simulate system response
    t, response, _ = signal.lsim(system, U=u, T=t)
    
    # Calculate analytical steady-state error for ramp input
    steady_state_error = tau * u[-1]
    
    # Create plot with improved styling
    plt.figure(figsize=(10, 6))
    plt.plot(t, response, 'b-', linewidth=2, label='Concentration of A')
    plt.plot(t, u, 'g--', linewidth=2, label='Normalized Ramp Input (Ca₀)')
    
    # Add steady-state error visualization
    plt.plot([t[-1], t[-1]], [response[-1], u[-1]], 'r-', linewidth=2)
    plt.annotate(f'Steady State Error = {steady_state_error:.3f}', 
                 xy=(t[-1], (response[-1] + u[-1])/2),
                 xytext=(t[-1] - 30, (response[-1] + u[-1])/2),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    plt.title('CSTR Ramp Response', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Normalized Concentration [mol/m³]', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_ramp_response(1.0, 0.5, 0.1)
