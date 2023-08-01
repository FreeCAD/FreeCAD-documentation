---
- GuiCommand:
   Name: Rocket Parachute Size Calculator
   Icon: Rocket_Calculator.svg
   MenuLocation: Rocket - Calculators - Parachute Size Calculator
   Workbenches: [Rocket Workbench](Rocket_Workbench.md)
   Version: 0.19
---

# Rocket Parachute Size Calculator/pl

## Description

This calculator determines the parachute size required to achieve the desired descent rate based on the parachute parameters.

The desired descent rate depends on your needs. As a rule of thumb, the main parachute should slow the rocket to approximately $6.1\,m/s\,(20\,f/s)$ while the drone should allow the parachute to descend much faster $18.3\,m/s\,(60\,f/s)$ - $21.3\,m/s\,(70\,f/s)$. The editor has presets for these, with the value for the drogue being in the middle of the range. You can set a custom descent rate to suit your needs.

A key value for determining the descent rate is the coefficient of drag ($C_D$). The exact value of this will depend on a variety of factors including the shape of the parachute. Presets are provided for parachutes cut from a flat piece of material (round, square, hexagonal) such as those provided by many kits, and for a true dome shape. Your parachute manufacturer may provide a better value for this coefficient.

## Usage

![](images/Calc_parachute_size.png )

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_Calculator.svg" width=16px> [Parachute Size Calculator](Rocket_Parachute_Size_Calculator.md)** button.
    -   Select the **Rocket → Calculators → <img src="images/Rocket_Calculator.svg" width=16px> Parachute Size Calculator** option from the menu.
2.  Enter the weight of your rocket and parameters for your parachute.

## Calculation

Parachute size is determined by the mass of the rocket, desired descent rate, and drag characteristics of the parachute. The calculation is a two step process. First the area of the parachute is calculated:

$$A = { 2mg \over { \rho v_T^2 C_D }}$$

where

$$m =$$ the mass of the rocket

$$v_T =$$ desired terminal velocity

$$C_D =$$ drag coefficient of the parachute

$$\rho = 1.22$$ air density, average at sea level in $kg/m^3$ at $15C$

$$g = 9.807$$ acceleration due to gravity in $m/s^2$

The diameter is then calculated from the surface area based on the shape.

For hexagonal parachutes:

$$D = \sqrt{ 2A \over sqrt{3}}$$

For square parachutes, the diameter is the length of each side

$$D = \sqrt{A}$$

For all other parachutes, the shape is assumed to be circular

$$D = \sqrt{ 4A \over \pi }$$

### Units

Calculations are done using metric units, but will display in your preferred units. Values can also be entered using any supported units by including the units with the value (*eg* 5 oz, or 23.2 g)

## References

1.  <http://www.rocketmime.com/rockets/descent.html>
2.  <https://descentratecalculator.onlinetesting.net/>
3.  <https://www.math.net/area-of-a-hexagon>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External Workbenches.md) > Rocket Parachute Size Calculator/pl
