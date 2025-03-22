import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_step_response(V, F, k):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create transfer function
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    # Simulate step response
    t, response = signal.step(system)
    
    # Adjust time scale to make the plot more readable
    t = t * 5  # Scale time to see more of the response
    
    # Calculate species A and B concentrations
    # Assuming normalized step input of Ca0 = 1
    Ca = response  # This is actually Ca/Ca0
    Cb = 1 - Ca    # For A→B reaction, Cb = Ca0 - Ca
    
    # Create plot with improved styling
    plt.figure(figsize=(10, 6))
    plt.plot(t, Ca, 'b-', linewidth=2, label='Concentration of A')
    plt.plot(t, Cb, 'r-', linewidth=2, label='Concentration of B')
    plt.title('CSTR Step Response to Inlet Concentration Change', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Normalized Concentration [C/Ca0]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add theoretical steady-state value
    plt.axhline(y=K, color='b', linestyle='--', label=f'Steady State Ca = {K:.2f}')
    plt.axhline(y=1-K, color='r', linestyle='--', label=f'Steady State Cb = {1-K:.2f}')
    
    # Add time constant marker
    idx = np.argmin(np.abs(Ca - K * (1 - 1/np.e) - (1-K)/np.e))
    plt.plot(t[idx], Ca[idx], 'bo')
    plt.annotate(f'τ = {tau:.2f} s', 
                 xy=(t[idx], Ca[idx]), 
                 xytext=(t[idx] + 0.5, Ca[idx] - 0.1),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))
    
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_step_response(1.0, 0.5, 0.1)
