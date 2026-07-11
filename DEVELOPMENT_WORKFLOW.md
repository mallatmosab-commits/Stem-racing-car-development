# My Racing Car Development Journal: From Concept to Nationals

Developing this car wasn't just about drawing shapes; it was an iterative cycle of trial, error, and refinement. Whether I was looking at a flow visualization in ANSYS or debating a structural trade-off for the wheels, every decision was aimed at finding that perfect balance between drag, downforce, and pure speed.

Here is how I navigated the development process.

## 1. The Body: Searching for Efficiency
My approach to the body was simple: cut the drag without losing stability. I treated the AR-M01 as my "ground truth" and evolved it through six iterations before arriving at the final configuration.

- **The Early Iterations (AR-M01 – M03):** My initial focus was cleaning up the airflow. I realized early on that the CO2 holder was a major source of turbulence. By smoothing the halo area and slimming down the sidepods in M03, I managed to get the airflow much "cleaner" before it even reached the rear of the car.
- **The Fine-Tuning (AR-M04 – M06):** Once the main body was stable, I started obsessing over the rear floor and the wake. Adding the rear floor walls in M04 was a calculated trade-off—it added a tiny bit of drag, but the control it gave me over the rear-end airflow was well worth it. By the time I reached the tapered rear design of M06, I finally felt the car’s drag coefficient drop to where it needed to be.
- **Final Choice (AR-M07):** This was the "Nationals" spec. It represents everything I learned: a tapered rear, optimized wheel wake, and a chassis that meets all the weight and regulation requirements while still being slippery through the air.

## 2. Wing Development: Managing the Air
The wings were a constant battle between downforce and parasitic drag.

- **Rear Wing:** I tested a few configurations, but it came down to a simple truth: the downward-pointing wings just created too much instability. I settled on an upward-curved design (RW-M03) because it gave me the best balance—keeping the car glued to the track without acting like a parachute.
- **Front Wing:** The biggest hurdle here was the front wheels. They kept creating a massive high-pressure zone that ruined the inlet flow. I went through several ramp designs before the FW-M03 really clicked for the regional level. When the 2025 regulations hit, I had to pivot to the FW-M04, which sacrificed a little bit of complexity for better structural integrity under the stricter rules.

## 3. Wheel R&D: Strength vs. Inertia
The wheels were perhaps the most technical part of the build. I didn't just want them to roll; I needed them to have a low moment of inertia and zero structural wobble.

- **The Design Logic:** I leaned into nylon powder manufacturing, which allowed for internal hollowing to save weight.
- **Aero Covers:** I’m a firm believer in covering the spokes. By isolating the wheel cover from the rotating rim, I cut down on the internal turbulence that kills efficiency at high speeds.
- **Structural Integrity:** Using FEA (Von Mises stress analysis) was a game-changer. It allowed me to push the material thickness to the absolute limit—light enough to accelerate fast, but stiff enough to hold up through a high-speed run.

## My Integrated Workflow
Looking back, my process became almost second nature. It wasn't just about moving from A to B; it was a continuous loop of:

1. **Modeling:** Getting the geometry into Fusion 360.
2. **Simulation:** Pushing that model through ANSYS and obsessing over the pressure contours and pathlines.
3. **Analysis:** Asking myself, "Where is the airflow separating? Can I shave mass here without losing structural rigidity?"
4. **Refinement:** Tweaking the CAD and starting the cycle again.

This workflow wasn't just a list of steps—it was how I justified every change I made. By the time I reached the final design, I had the data to back up exactly why the car performed the way it did.
