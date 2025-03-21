# Simple simulation of a first order Continuous Stirred Tank Reactor (CSTR)
- Includes response to various types of input concentation stimuli (step changes, ramp inputs, sinusoidal inputs, etc.)
- Incorporation of PID controller to maintain exit concentration set point 
- Laplace transformation used for transfer function to simulate the closed-loop response of the reactor
- Uses Ziegler-Nichols heuristic tuning method

## System Description
A liquid stream of **A** enters the reactor at a volumetric flow rate **F** , decomposing according to the irreversible chemical reaction **A→B**, at a rate of **r=k*C<sub>a</sub>**

The reactor is modeled with a time constant **𝜏** and a gain **K**. The purpose of the control system is to maintain the concentration of **B** leaving the reactor at a desired value despite variations in the inlet concentration **C<sub>a</sub><sub>0</sub>**

  
#### Reactor Formulas:
V $\frac{dc}{dt}$ = F*C<sub>a</sub><sub>0</sub> - (F+kv)*C<sub>a</sub>

, and

𝜏 $\frac{dc}{dt}$ + C<sub>a</sub> = K*C<sub>a</sub><sub>0</sub> 

where:
- 𝜏 = $\frac{V}{F+kV}$
- K = $\frac{1}{kV/F}$

## Running the Simulation

### 1. Preliminaries

**Ensure** all required Python packages are installed:
```sh
pip install numpy matplotlib scipy control
   ```

**Navigate** to the project directory:
 ```sh
cd [project-directory]
   ```
### 2. Running
**Execute the simulation** using the main script:
 ```sh
python main.py
   ```

To change system parameters, the following is an example:
 ```sh
python main.py --V 2.0 --F 0.8 --k 0.15 --Ku 3.0 --Tu 15.0 --c_ref 0.9 --pulse_start 25
   ```

**FYI**: If the user doesn’t provide any specific system inputs when running the script, the default parameters defined in the argparse setup will be used. The are defined in the next section.

### Default Parameters:

* **--V**: Reactor volume (m³), default=1.0
* **--F**: Volumetric flow rate (m³/s), default=0.5
* **--k**: Reaction rate constant (1/s), default=0.1
* **--Ku**: Ultimate gain for PID control, default=2.0
* **--Tu**: Ultimate period for PID control (s), default=10.0
* **--c_ref**: Reference concentration for PID control, default=0.8
* **--pulse_start**: Rectangular pulse start time (s), default=20
* **--pulse_end**: Rectangular pulse end time (s), default=40
* **--noise_mean**: Mean of random noise, default=0
* **--noise_std**: Standard deviation of random noise, default=1

##
#### Reference
Coughanower, D. R.; Koppel, L. B. *Process Systems Analysis and Control*; McGraw-Hill Chemical Engineering Series, McGraw-Hill Companies: New York, 1964; pp 123–124.

<br>
