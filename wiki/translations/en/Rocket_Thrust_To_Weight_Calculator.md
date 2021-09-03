---
- GuiCommand:
   Name:Rocket Thrust To Weight Calculator
   Icon:Rocket_Calculator.svg
   MenuLocation:Rocket → Calculators → Thrust To Weight Calculator
   Workbenches:[Rocket Workbench](Rocket_Workbench.md)
   Version:0.19
---

## Description

This simple calculator determines the minimum average thrust required to maintain a 5:1 thrust to weight ratio.

## Usage

![](images/Calc_thrust_to_weight.png )

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_Calculator.svg" width=16px> [Thrust To Weight Calculator](Rocket_Thrust_To_Weight_Calculator.md)** button.
    -   Select the **Rocket → Calculators → <img src="images/Rocket_Calculator.svg" width=16px> Thrust To Weight Calculator** option from the menu.
2.  Enter the weight of your rocket.

## Calculation

Thrust to weight is calculated using the following formula:

$$T_{min} = 5mg$$

where

$$T_{min} =$$ recommended minimum average thrust
$$m =$$ mass of the rocket
$$g = 9.807\, m/s^2$$, acceleration due to gravity

### Units

Calculations are done using metric units, but will display in your preferred units. Values can also be entered using any supported units by including the units with the value (*eg* 5 oz, or 23.2 g)







[Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
