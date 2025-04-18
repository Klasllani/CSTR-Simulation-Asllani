# Simple simulation of a first order Continuous Stirred Tank Reactor (CSTR)
- Includes response to various types of input concentation stimuli (step changes, ramp inputs, sinusoidal inputs, etc.)
- Supports user-defined reactor parameters for flexible simulation configurations
- Uses control library’s TransferFunction class to model system dynamics
- Incorporation of PID controller to maintain exit concentration set point 
- Uses Ziegler-Nichols heuristic tuning method 

<br>

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

Ensure all required Python libraries are installed (numpy, matplotlib, scipy, control) and cd to the project directory.

<br>

### 2. Running
**Execute the simulation** using the main script:
 ```sh
python3 main.py
   ```
+ This command works for **Unix-based** operating systems (Linux, macOS, etc.)
+ For Windows: use python instead of python3

<br>

To change system parameters, the following is an example:
 ```sh
python3 main.py --V 2.0 --F 0.8 --k 0.15 --Ku 3.0 --Tu 15.0 --c_ref 0.9 --pulse_start 25
   ```

**FYI**: If the user doesn’t provide any specific system inputs when running the script, the default parameters defined in the argparse setup will be used. They are defined below, in the next section.

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

## Maximizing Conversion (X<sub>a</sub>):
When running the simulation with default parameters, an astute user will notice lackluster conversion of A to B. 

#### To increase X<sub>a</sub>, refer to **above formula section**, and you can see that:
+ Increasing reactor volume, increases residence time and thus conversion
+ Decreasing flow rate, increases residence time and thus conversion
+ Increasing the reaction rate constant, increases conversion. In the real world, this can be done in several ways, depending on the process:
  - Changing temperature (look at the Arrhenius equation)
  - Introducing a castalyst to lower activation energy (again, Arrhenius equation)
  - pH Control (for acid/base reactions, enzyme catalysis, fermentation, etc.)
  - Pressure effects (Le Chatelier's principle)
+ Adjust PID control parameters
  - Set c_ref to a lower value to lower set point exit concentration of A
  - Increasing ultimate gain (Ku) for stronger control response, adjusting ultimate period (Tu) to match the system’s dynamics
  - Consider cascade control using temperature as secondary controlled variable and/or feed-forward control to handle inlet concentration disturbances
+ Miscellaneous enhancements such as upgrading the impeller/agitator or altering reactor geometry 

<br>

#### Overall Reference:
Coughanower, D. R.; Koppel, L. B. *Process Systems Analysis and Control*; McGraw-Hill Chemical Engineering Series, McGraw-Hill Companies: New York, 1964; pp 123–124.
