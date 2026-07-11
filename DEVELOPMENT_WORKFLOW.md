# Stem Racing Car Development Workflow

## Overview
This workflow documents the design and aerodynamic development journey for the stem racing car.
It combines the body, wing, and wheel R&D phases into a single process that is easy to follow and use for future documentation.

## Tools and Methods
- 3D CAD modeling (e.g. Fusion 360)
- CFD simulation and contour analysis in ANSYS
- Velocity pathline and pressure contour reviews
- FEA stress analysis for wheel structures
- Iterative design evaluation by drag, lift, stability, and manufacturability

## Body Development Process
1. Baseline design evaluation
   - Start with the first body variant: `AR-M01`
   - Analyze drag, lift, high-pressure regions, and airflow around the CO2 holder
   - Identify airflow separation, pressure concentration, and unnecessary downforce

2. `AR-M02` improvements
   - Smooth the CO2 holder
   - Extend and clean the halo area
   - Result: reduced drag, better airflow stability, and lower resistance

3. `AR-M03` sidepod refinement
   - Slim down sidepods to reduce frontal drag
   - Smooth external airflow and lower high-pressure zones
   - Result: more efficient flow with less wake interference

4. `AR-M04` rear floor control
   - Add rear floor walls for improved rear airflow management
   - Evaluate tradeoffs: better rear control vs. slightly higher drag
   - Decision point: maintain core body shape while refining rear flow

5. `AR-M05` rounded sidepods
   - Use rounded sidepods to reduce local turbulence
   - Optimize the shape for better interaction between car body and air
   - Result: acceptable aerodynamic balance and improved overall package

6. `AR-M06` tapered rear section
   - Reduce rear surface area and create a tapered finish
   - Focus on smoother wake and lower turbulence
   - Outcome: improved straight-line aerodynamic efficiency

7. Final competition body: `AR-M07`
   - Adopt tapered rear design and optimized wheel wake
   - Meet regulations and weight requirements for Nationals class
   - Result: lower drag, reduced lift, and strong performance consistency

## Floor Design and Weight Management
- Test several floor concepts for drag and lift performance
- Evaluate each floor by manufacturability and mass savings
- Select the layout that provides the best aerodynamic value with low weight
- Final choice should balance structural simplicity and airflow advantage

## Wing Development Process
### Rear wing research
1. `RW-M01` baseline
   - Provides lift while keeping drag moderate
   - Identifies airflow behavior and V-shape performance risks
   - Improvement goal: add a curved wing section to reduce lift and drag

2. `RW-M02` angle-of-attack study
   - Compare negative vs positive angle of attack
   - Evaluate drag increase and downforce generation
   - Improvement goal: refine wing curvature for more stable airflow

3. `RW-M03` chosen design
   - Upward-pointing wing delivered the best aerodynamic balance
   - Downward-pointing wing created more drag and lift instability
   - Final wing selected for effective downforce with acceptable drag

### Front wing evolution
1. `FW-M01` baseline
   - High-pressure area around the front wheels
   - Flow blockage caused turbulence and reduced aerodynamic efficiency
   - Improvement goal: add a ramp section and better inlet shaping

2. `FW-M02` airflow redirection
   - Reduced drag by improving flow guidance
   - Pressure contours still indicated wheel-area interference
   - Improvement goal: lower stagnation and satisfy technical regulations

3. `FW-M03` Regional design
   - Best balance of lift and drag for the regulations
   - Improved front profile and airflow around the wheel area
   - Chosen as the most successful concept for regional competition

4. `FW-M03.1` V-shaped front wing test
   - Inspired by more advanced race-car geometry
   - Produced more directed airflow and better rear-end balance
   - Used as a design investigation rather than the final wing

5. `FW-M04` Nationals design
   - Compliant with updated 2025 regulations
   - Maintained low drag while increasing structural support
   - Final design chosen for stronger performance under stricter rules

## Wheel R&D and Structural Optimization
### Objectives
- Low moment of inertia for faster acceleration and braking
- Low deformation to keep tire contact stable
- Low rotational energy to improve efficiency
- Improved stability and consistent traction

### Wheel system design
- Use lightweight materials such as nylon powder with internal hollowing
- Central airfoil support to guide airflow around the wheel area
- Integrated tether-line guide to improve launch stability and reduce lateral movement

### Wheel cover strategy
- Fully enclose spokes to reduce drag and internal turbulence
- Keep the wheel cover separate from the rotating rim to avoid inertia penalties
- Result: smaller wake, higher efficiency, and improved straight-line stability

### Spoke and bearing placement
- Spread spoke positions to equalize load and improve durability
- Center bearing placement precisely inside the wheel structure to reduce imbalance
- Select bearing sizes that support wheel stiffness while minimizing added mass

### Structural testing and selection
- Use Von Mises stress predictions to keep material stress below yield limits
- Perform FEA on wheel structures under expected loading
- Choose design thickness and geometry based on strength, deformation, and inertia tradeoffs

### Selected wheel concept
- Compare designs A, B, and C for deformation and rotational energy
- Choose the design that delivers the lowest drag and acceptable stiffness
- Confirm that the final design is stable, lightweight, and regulation-ready

## Integrated Development Flow
1. Define target performance metrics
2. Model body, floor, wing, and wheels in CAD
3. Simulate body and wing aerodynamics in ANSYS
4. Analyze pressure contours, velocity pathlines, drag, and lift
5. Adjust geometry and repeat simulations
6. Test wheel structure with FEA and optimize spoke/cover design
7. Select the best combination for regional and nationals rules
8. Document final choices and explain the reasoning for each subsystem
