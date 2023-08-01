# Part Revolve/cs
---
- GuiCommand:/cs   Name:Part Revolve   Name/cs:Díl Obtáčení   MenuLocation:Díl -> Obtáčení   Workbenches:[[Part_Workbench/cs   Díl]], Kompletace|SeeAlso:---


</div>

## Description


<div class="mw-translate-fuzzy">

Obtáčí vybraný objekt kolem zadané osy. Pro obtáčení jsou povoleny následující typy, výsledky obtáčení jsou uvedeny ve druhém sloupci:


</div>


<div class="mw-translate-fuzzy">

  Vstupní tvar   Výstupní tvar
   
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

## Notes

-   [App Link](App_Link.md) objects linked to the appropriate object types can also be used as shapes and to specify the axis. <small>(v0.20)</small> 
-   If the object to revolve intersects the rotation axis the operation will fail in most cases.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Revolve/cs
