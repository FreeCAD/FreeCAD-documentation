---
- GuiCommand:
   Name:FCGear TimingGear
   MenuLocation:FCGear → Create a Timing gear
   Workbenches:[FCGear](FCGear_Workbench.md)
   Shortcut:None
   Version:v0.16
   SeeAlso:
---

# FCGear TimingGear/pl

## Opis

Celem kół zębatych rozrządu jest umożliwienie wałowi rozrządu i wału korbowego obracanie łańcucha rozrządu. Wał korbowy obraca się, aby poruszać tłokami w górę i w dół wewnątrz cylindrów. Wałek rozrządu obraca się, aby umożliwić otwieranie i zamykanie zaworów wlotowych i wylotowych w cylindrach. Te elementy są ważne dla prawidłowego sterowania rozrządem silnika.

Timing gears are connected to a timing belt or timing chain.

![](images/Timing-Gear_example.png ) 
*Above: Timing gear*

## Usage

1.  Switch to the <img alt="" src=images/FCGear_workbench_icon.svg  style="width:22px;"> [FCGear Workbench](FCGear_Workbench.md).
2.  Invoke the command several way:
    -   Press the <img alt="" src=images/FCGear_TimingGear.svg  style="width:22px;"> [Create a Timing gear](FCGear_TimingGear.md) button in the tool bar.
    -   Using the **Gear Menu → Timing gear**.
3.  Change the gear parameter to the required conditions (see **Properties → Data** below).

## Properties

### Data


{{Properties_Title|Base}}

-    **Placement**: [Placement](Placement.md) is the location and orientation of an object in space.

-    **Label**: User name of the object in the [Tree view](Tree_view.md).


{{Properties_Title|computed}}

-    **h**: Radial height of teeth (not changeable, is calculated automatically).

-    **offset**: X-Offset of second arc mid-point (not changeable, is calculated automatically).

-    **pitch**: Pitch of gear (not changeable, is calculated automatically).

-    **r0**: Radius of first arc (not changeable, is calculated automatically).

-    **r1**: Radius of second arc (not changeable, is calculated automatically).

-    **rs**: Radius of third arc (not changeable, is calculated automatically).

-    **u**: Radial difference between pitch ... diameter and head of gear (not changeable, is calculated automatically).


{{Properties_Title|gear_parameter}}

-    **height**: Default is 5,00 mm. Value of the gear width.

-    **teeth**: Default is 20. Number of teeth.

-    **type**: Default is gt2. Type of timing gear -- profile pitch for timing belts (see also the information in **Notes**).

### View

The parameter descriptions of the **View** tab will be found in [Property editor](Property_editor.md), further below at **Example of the properties of a PartDesign object**.

## Notes

-    **type**: The pitch of the timing belts (distance from tooth centre to tooth centre of consecutive teeth) is specified in types. GT2 has a pitch of 2 mm, GT3 of 3 mm, GT5 of 5 mm etc..

## Limitations

Limitations are not known yet.

## Useful formulas 

-    **addendum diameter**= **pitch diameter** + 2 \* **module**

-    **belt length**= 2 \* **axle base** + **belt tooth pitch** : 2 \* **(teeth 1 + 2)** + **belt tooth pitch²** : 4 \* pi² \* **axle base** \* **(teeth 1 - 2)²**

-    **axle base**= **belt length** : 4 - **belt tooth pitch** : 8 \* **(teeth 1+2)** + ¼ \* sqrt \[**belt length** - ½ \* **belt tooth pitch** \* **(teeth 1+2)²** - 2 \* **belt tooth pitch²** \* **(teeth 1+2)²** : pi²\]




_ _ _

---
[documentation index](../README.md) > [Addons](Category_Addons.md) > FCGear TimingGear/pl
