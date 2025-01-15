---
 GuiCommand:
   Name: Rocket Ejection Charge Calculator
   Icon: Rocket_Calculator.svg
   MenuLocation: Rocket , Calculators , Ejection Charge Calculator
   Workbenches: Rocket_Workbench
   Version: 0.19
---

# Rocket Ejection Charge Calculator/en

## Description


**This calculator only gives an estimate of the amount of powder required. Too much or too little may result in a failed recovery or damage to your rocket<br>'''ALWAYS''' ground test your rocket before flying**

Ejection occurs when the chamber containing the recovery system is pressurized with sufficient force to eject the recovery system from the chamber. The force required can vary according to a number of factors:

  - diameter and volume of the body tube

  - mass of the nose and recovery system

  - ejection method, for example piston systems require less pressure

  - presence of shear pins used to prevent drag separation

  - fit of the recovery system in the body tube

As such, this calculator will only give you a starting estimate. Too little powder will result in a failed ejection and a failed recovery. Too much powder may result in damage to the rocket or recovery system, which may also result in a failed recovery. It is **ALWAYS** necessary to do a ground test before flying your rocket.

When calculating the volume of the body tube, it is rarely necessary to include the full length. For example, the shoulder of the nose or electronics bay may consume some volume. Adjust your length specification accordingly.

There are some rules of thumb that can be applied based on years of experience from multiple rocket builders. Of primary concern here is the force applied to the ejectable portion, typically the nose cone or electronics bay. Ejection forces at this interface should be between 150 and 200 lbf (\~667 to 890 N). The pressure required can then be calculated based on the volume of the chamber. This pressure will be less for larger diameters and more for smaller diameters. There are presets in the calculator to set these forces (low and high settings in the combobox).

Ground testing should start at the low end of the recommended range to prevent damage to your rocket. Increase the amount as required to ensure safe recovery.

## Usage

![](images/Calc_ejection_charge.png )

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Rocket_Calculator.svg" width=16px> [Ejection Charge Calculator](Rocket_Ejection_Charge_Calculator.md)** button.
    -   Select the **Rocket → Calculators → <img src="images/Rocket_Calculator.svg" width=16px> Ejection Charge Calculator** option from the menu.
2.  Enter the weight of your rocket and parameters for your parachute.

## Calculation

Pressure is set by desired force, or force can be set by specifying the desired pressure. This is based on the force applied to the area at the end of the volume to be pressurized.

$$P = \cfrac{F}{\pi {\left ( \cfrac{D}{2} \right )}^2}$$

where

$$F =$$ desired force
$$D =$$ body tube diameter

Once the desired pressure is known, the amount of black powder can be calculated using

$$m = \cfrac{ PV }{ R_{c}Tg }$$

where

$$P =$$ the pressure calculated in the previous equation
$$V =$$ the volume of the chamber to be pressurized
$$R_{c} = 12.1579\, \frac{m}{K}$$, combustion gas constant for FFFFg black powder
$$T = 1739\, K$$, combustion gas temperature
$$g = 9.807\, \frac{m}{s^2}$$, acceleration due to gravity

### Units

Calculations are done using metric units, but will display in your preferred units. Values can also be entered using any supported units by including the units with the value (*eg* 5 oz, or 23.2 g)

## References

1.  <http://vernk.com/EjectionChargeSizing.htm>
2.  <https://www.insanerocketry.com/blackpowder.html>
3.  <https://rocketrycalculator.com/rocketry-calculator/bp-estimator>
4.  <http://www.rockethead.net/black_powder_calculator.htm>
5.  <http://hararocketry.org/hara/resources/how-to-size-ejection-charge/>



---
⏵ [documentation index](../README.md) > [Addons](Category_Addons.md) > [External Workbenches](Category_External%20Workbenches.md) > Rocket Ejection Charge Calculator/en
