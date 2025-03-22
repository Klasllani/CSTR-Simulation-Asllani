import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_random_noise_response(V, F, k, noise_mean, noise_std):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create transfer function
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    # Create time vector and random noise input
    t = np.linspace(0, 100, 1000)
    np.random.seed(0)  # For reproducibility
    u = np.random.normal(noise_mean, noise_std, len(t))
    
    # Simulate system response
    t, response, _ = signal.lsim(system, U=u, T=t)
    
    # Calculate moving average for clearer trend visualization
    window_size = 50
    ma_response = np.convolve(response, np.ones(window_size)/window_size, mode='valid')
    ma_t = t[window_size-1:]
    
    # Create plot with improved styling
    plt.figure(figsize=(12, 9))
    
    # Input noise plot
    plt.subplot(3, 1, 1)
    plt.plot(t, u, 'g-', linewidth=1, alpha=0.7)
    plt.title('Random Noise Input (Variations in Inlet Concentration Ca₀)', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Input Noise [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # System response plot
    plt.subplot(3, 1, 2)
    plt.plot(t, response, 'b-', linewidth=1)
    plt.title('CSTR Response (Concentration of A)', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Concentration [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Moving average for trend analysis
    plt.subplot(3, 1, 3)
    plt.plot(ma_t, ma_response, 'r-', linewidth=2, label=f'Moving Average (window={window_size})')
    plt.title('Filtered Response (Moving Average)', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Smoothed Concentration [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(fontsize=10)
    
    # Add statistics
    plt.figtext(0.02, 0.01, 
                f'Input Statistics:\nMean = {np.mean(u):.4f}\nStd Dev = {np.std(u):.4f}\n\n'
                f'Output Statistics:\nMean = {np.mean(response):.4f}\nStd Dev = {np.std(response):.4f}\n'
                f'Response/Input Std Ratio = {np.std(response)/np.std(u):.4f}',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.15)  # Make room for text
    plt.show()

if __name__ == "__main__":
    simulate_random_noise_response(1.0, 0.5, 0.1, 0, 1)
