---
- GuiCommand:/ru
   Name:Path Fixture
   Name/ru:Path Fixture
   MenuLocation:Path → Supplemental Commands → Крепление
   Workbenches:[Path](Path_Workbench/ru.md)
   Shortcut:**P** **F**
   SeeAlso:
---

# Path Fixture/ru


</div>

## Description

The tool <img alt="" src=images/Path_Fixture.svg  style="width:24px;"> [Fixture](Path_Fixture.md) sets the Work Offset Coordinate Fixture of the machine CNC controller.

Target Work Offset Coordinates typically include: Fixtures G53 to G59. The G-code is simply the Fixture (G53, G54, etc\...). The coordinate offset fixtures represent:

-   G53 → Machine coordinate system.
-   G54 → Scratchpad coordinate system.
-   G55 to G59.9 → Coordinate fixtures allowing work offsets, relative to Homing switches located on the CNC machine, to be used.

The G59 Fixture is used to expand available fixtures. The degree of expansion implemented is CNC machine specific, and this command allows provides for G59.1 to G59.9.

## Usage

1.  Press the **<img src="images/Path_Fixture.svg" width=16px> [Fixture](Path_Fixture.md)** button or use the **P** then **F** keyboard shortcut.
2.  Select the desired Work Offset Fixture from the drop-menu.

## Properties

-    **Fixture**: Sets the current fixture point

-    **Active**: Defines if this command is active or not when inserted into a compound

## Notes

## Limitations

## Scripting


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Fixture/ru
