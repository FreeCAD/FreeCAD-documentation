# Draft ToggleConstructionMode/sv
---
- GuiCommand:   Name: Draft ToggleConstructionMode   Name/sv: Draft ToggleConstructionMode   Workbenches: Draft_Workbench/sv   Draft, Arch_Workbench/sv|MenuLocation: Draft -> Utilities -> Toggle construction mode---


</div>

## Description


<div class="mw-translate-fuzzy">

Konstruktionsläget i Skissmodulen är en enkel inställning som tillåter dig att rita konstruktionsgeometri (vilket är geometri som endast används till att hjälpa dig med att konstruera mer komplexa element) i en speciell grupp, med en speciell färg, så det är lätt att separera dem från resten och stänga av dem när du inte behöver dem.

-   **Konstruktion** knappen i Skisskommandolådan sätter på och stänger av konstruktionsläget
-   När den knappen trycks in, så kommar alla objekt som du sedan ritar att få konstruktionsfärgen och placeras i konstruktionsgruppen
-   Färgen och gruppnamnet kan ändras i [alternativfönstret](Draft_Preferences/sv.md).
-   En tangentbordsgenväg kan tilldelas till knappen för att lätt kunna stänga på/av funktionen från tangentbordet (Verktyg -\> Anpassa -\> Tangentbord -\> Python -\> Toggle Construction Mode)

## Description 

The Draft module features a construction mode, which allows to draw certain objects in a special group, with a defined color, so it is easy to separate them from the other objects and switch it off when you don\'t need it, or delete them after you don\'t need them anymore.


</div>

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Draft_construction_mode_example.jpg  style="width:400px;">


</div>

## Usage

1.  There are several ways to invoke the command:
    -   Press the **<img src="images/Draft_ToggleConstructionMode.svg" width=16px> [Draft ToggleConstructionMode](Draft_ToggleConstructionMode.md)** button in the [Draft Tray](Draft_Tray.md). This button is depressed if Draft construction mode is currently on.
    -   Select the **Utilities → <img src="images/Draft_ToggleConstructionMode.svg" width=16px> Toggle construction mode** option from the menu.
    -   Use the keyboard shortcut: **C** then **M**.
2.  The button in the [Draft Tray](Draft_Tray.md) is updated.

## Notes

-   If Draft construction mode is switched on the active [layer](Draft_Layer.md) is ignored.

## Preferences

-   To change the label of the construction group: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction group name**.
-   To change the color that is used: **Edit → Preferences... → Draft → General settings → Construction Geometry → Construction geometry color**.



---
⏵ [documentation index](../README.md) > [Draft](Draft_Workbench.md) > Draft ToggleConstructionMode/sv
