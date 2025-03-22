import numpy as np
import matplotlib.pyplot as plt
import control

def simulate_pid_control(V, F, k, Ku, Tu, c_ref):
    # Calculate time constant and gain
    tau = V / (F + V * k)
    K = 1 / (1 + V * k / F)
    
    # Create plant transfer function
    num = [K]
    den = [tau, 1]
    system = control.TransferFunction(num, den)
    
    # Calculate PID parameters using Ziegler-Nichols method
    Kp = 0.6 * Ku
    Ki = 1.2 * Ku / Tu
    Kd = 3 * Ku * Tu / 40
    
    # Create PID controller transfer function
    pid = control.TransferFunction([Kd, Kp, Ki], [1, 0])
    
    # Create closed-loop system
    closed_loop = control.feedback(pid * system, 1)
    
    # Simulate step response
    t, response = control.step_response(closed_loop)
    
    # Scale response to reference concentration
    response = response * c_ref
    
    # Reference line (setpoint)
    reference = np.ones_like(response) * c_ref
    
    # Create plot with improved styling
    plt.figure(figsize=(10, 8))
    
    # System response plot
    plt.subplot(2, 1, 1)
    plt.plot(t, response, 'b-', linewidth=2, label='System Response')
    plt.plot(t, reference, 'r--', linewidth=1.5, label='Reference (Setpoint)')
    plt.title('CSTR Closed-Loop Response with PID Control', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Concentration of Product B [mol/m³]', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Calculate tracking error
    error = reference - response
    
    # Error plot
    plt.subplot(2, 1, 2)
    plt.plot(t, error, 'g-', linewidth=2)
    plt.title('Control Error (Reference - Response)', fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]', fontsize=12)
    plt.ylabel('Error [mol/m³]', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Add system and controller parameters
    plt.figtext(0.02, 0.02, 
                f'System Parameters:\nV = {V} m³\nF = {F} m³/s\nk = {k} 1/s\nτ = {tau:.2f} s\nK = {K:.2f}\n\n'
                f'Controller Parameters (Z-N):\nKp = {Kp:.2f}\nKi = {Ki:.2f}\nKd = {Kd:.2f}',
                bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.tight_layout()
    plt.subplots_adjust(bottom=0.2)  # Make room for text
    plt.show()

if __name__ == "__main__":
    simulate_pid_control(1.0, 0.5, 0.1, 2.0, 10.0, 0.8)
