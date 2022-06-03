---
- GuiCommand   */ro
   Name   *Path Fixture
   Workbenches   *[Path](Path_Workbench.md)
   MenuLocation   *Path → Partial Commands → Fixture
   Shortcut   ***P** **F**
   SeeAlso   *
---

# Path Fixture/ro


</div>

## Descriere

Acest instrument stabilește dispozitivul de decalare a lucrării de la controlerul CNC al mașinii.


<div class="mw-translate-fuzzy">

Target Work Offset Coordinates în mod tipic incude   * Fixtures G53 to G59. Codul G-Code este simplu Fixture (G53, G54, etc\...). Coordinatele offset fixtures reprezintă   *

-   G53 -\> Sistemul de coordonate al mașinii.
-   G54 -\> Scratchpad coordinate system.
-   G55 to G59.9 -\> Sistemele de coordonate care să permită compensările de lucru, legate de comutatoarele Homing localizate pe mașina CNC, să fie utilizate.


</div>


<div class="mw-translate-fuzzy">

Fixarea G59 este utilizată pentru a extinde dispozitivele disponibile. Gradul de extindere implementat este specific mașinii CNC, iar această comandă permite prevederea pentru G59.1 până la G59.9.


</div>

## Utilizare


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/Path_Fixture.png" width=16px> [Fixture](Path_Fixture.md)
**
2.  Selectați Work Offset Fixture dorit din meniul contextual/drop-menu.


</div>

## Proprietăți

-    **Fixture**   * Setați punctul curent de fixare

-    **Active**   * Definește dacă comanda este activă sau nu când este inserată într-un compound

## Notes

## Limitations

## Scripting


<div class="mw-translate-fuzzy">





</div>


{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Fixture/ro
