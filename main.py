import argparse
import step_response
import ramp_response
import sinusoidal_response
import pid_control
import rectangular_pulse_response
import impulse_response
import random_noise_response

def main():
    parser = argparse.ArgumentParser(description="CSTR Simulation with User Parameters")
    parser.add_argument('--V', type=float, default=1.0, help='Reactor volume (m³)')
    parser.add_argument('--F', type=float, default=0.5, help='Volumetric flow rate (m³/s)')
    parser.add_argument('--k', type=float, default=0.1, help='Reaction rate constant (1/s)')
    parser.add_argument('--pulse_start', type=float, default=20, help='Rectangular pulse start time (s)')
    parser.add_argument('--pulse_end', type=float, default=40, help='Rectangular pulse end time (s)')
    parser.add_argument('--noise_mean', type=float, default=0, help='Mean of random noise')
    parser.add_argument('--noise_std', type=float, default=1, help='Standard deviation of random noise')
    parser.add_argument('--Ku', type=float, default=2.0, help='Ultimate gain for PID control')
    parser.add_argument('--Tu', type=float, default=10.0, help='Ultimate period for PID control (s)')
    parser.add_argument('--c_ref', type=float, default=0.8, help='Reference concentration for PID control')
    args = parser.parse_args()
    
    print("Running CSTR Simulation...")
    
    print("Simulating Step Response...")
    step_response.simulate_step_response(args.V, args.F, args.k)
    
    print("Simulating Ramp Response...")
    ramp_response.simulate_ramp_response(args.V, args.F, args.k)
    
    print("Simulating Sinusoidal Response...")
    sinusoidal_response.simulate_sinusoidal_response(args.V, args.F, args.k)
    
    print("Simulating PID Control...")
    pid_control.simulate_pid_control(args.V, args.F, args.k, args.Ku, args.Tu, args.c_ref)
    
    print("Simulating Rectangular Pulse Response...")
    rectangular_pulse_response.simulate_rectangular_pulse_response(args.V, args.F, args.k, args.pulse_start, args.pulse_end)
    
    print("Simulating Impulse Response...")
    impulse_response.simulate_impulse_response(args.V, args.F, args.k)
    
    print("Simulating Random Noise Response...")
    random_noise_response.simulate_random_noise_response(args.V, args.F, args.k, args.noise_mean, args.noise_std)

if __name__ == "__main__":
    main()
