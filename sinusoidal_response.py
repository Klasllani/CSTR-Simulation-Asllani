import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_sinusoidal_response(V, F, k, frequency=0.05, amplitude=1.0, duration=100):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create transfer function
    num = [K]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    
    # Calculate frequency response
    w, mag, phase = signal.bode(system)
    
    # Create time vector and input
    t = np.linspace(0, duration, 1000)
    u = amplitude * np.sin(2 * np.pi * frequency * t)
    
    # Simulate system response
    t, response, _ = signal.lsim(system, u, t)
    
    # Calculate theoretical gain and phase at input frequency
    input_freq_rad = 2 * np.pi * frequency
    _, mag_at_freq, phase_at_freq = signal.bode(system, w=[input_freq_rad])
    
    # Create plot with improved styling
    plt.figure(figsize=(12, 8))
    
    # Plot input signal
    plt.subplot(3, 1, 1)
    plt.plot(t, u, 'g-', linewidth=2)
    plt.title('Sinusoidal Input (Inlet Concentration Ca₀)', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Input Amplitude [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Plot system response
    plt.subplot(3, 1, 2)
    plt.plot(t, response, 'b-', linewidth=2)
    plt.title('CSTR Response (Exit Concentration of A)', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Concentration [mol/m³]', fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Plot both signals together (to show phase shift)
    plt.subplot(3, 1, 3)
    plt.plot(t, u, 'g-', linewidth=1.5, label='Input Ca₀')
    plt.plot(t, response / np.max(response) * amplitude, 'b-', linewidth=1.5, 
             label='Normalized Response')  # Normalize for comparison
    
    # Annotate phase shift and amplitude ratio
    plt.annotate(f'Phase Shift: {phase_at_freq[0]:.1f}°\nAmplitude Ratio: {mag_at_freq[0]:.3f}',
                 xy=(duration/4, 0), 
                 xytext=(duration/4, -0.8),
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.title('Input vs. Response Comparison', fontsize=12)
    plt.xlabel('Time [s]', fontsize=10)
    plt.ylabel('Normalized Amplitude', fontsize=10)
    plt.legend(fontsize=9)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simulate_sinusoidal_response(1.0, 0.5, 0.1)
