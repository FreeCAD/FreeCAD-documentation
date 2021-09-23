# Part Revolve/cs
---
- GuiCommand:/cs   Name:Part Revolve   Name/cs:Díl Obtáčení   MenuLocation:Díl -> Obtáčení   Workbenches:[[Part_Workbench/cs   Díl]], Kompletace|SeeAlso:---


</div>


<div class="mw-translate-fuzzy">

Obtáčí vybraný objekt kolem zadané osy. Pro obtáčení jsou povoleny následující typy, výsledky obtáčení jsou uvedeny ve druhém sloupci:


</div>


<div class="mw-translate-fuzzy">

  Vstupní tvar   Výstupní tvar
  -------------- ----------------
  Vrchol         Hrana
  Hrana          Plocha
  Drát           Plášť
  Plocha         Těleso
  Plášť          Složené těleso


</div>


<div class="mw-translate-fuzzy">

Jako vstupní objekty nemohou být použity tělesa nebo složená tělesa. Nemohou být použity ani běžné složeniny. Budoucí verze budou kontrolovat zda vybraný objekt není složený objekt.


</div>

![](images/Dialog-revolve.png )


<div class="mw-translate-fuzzy">

Argument Úhel specifikuje o kolik stupňů má objekt být otočen. Souřadnice posunou počátek osy obtáčení relativně k počátku souřadnicového systému.


</div>


<div class="mw-translate-fuzzy">

Jestli je vybrána uživetelsky definována osa, čísla definují směr obtáčecí osy vzhledem k souřadnicovému systému: Je-li souřadnice Z rovna 0 a souřadnice X a Y jsou nenulové, bude osa ležet v rovině XY. Úhel je takový, že jeho směrnice je poměr zadaných souřadnic X a Y.


</div>

### Notes

-   If your version of FreeCAD has a check box for Solid in the Revolve dialog, you can make Solids from closed Wires and Edges.
-   If Revolve is performed using an axis that intersects the face to rotate, and you want to create a solid, the result might be invalid. This can happen for various reasons, self-intersection, direction, etc.

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/cs
