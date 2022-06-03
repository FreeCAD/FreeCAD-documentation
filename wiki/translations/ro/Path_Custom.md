# Path Custom/ro
---
- GuiCommand   *   Name   *Path Custom   Workbenches   *[[Path Workbench   Path]]|MenuLocation   *Path → Partial Commands → Custom   Shortcut   *   SeeAlso   *---


</div>

## Descriere

Acest instrument introduce un obiect traiectorie care constă din cod G personalizat și codificat manual.

Deoarece comanda G-Code personalizată nu oferă nicio legătură cu un controler de scule, dacă o sculă este utilizată de codul G personalizat, indicele instrumentului trebuie să fie scris împreună cu codul de pornire M, pentru a fi transmis Postprocesorul. Acest lucru asigură că modificările și pornirea instrumentului vor fi generate în mod corespunzător.

De exemplu, pentru a transmite Postprocesorului că instrumentul utilizat în operațiunea G-Cod personalizat are indicele Tool 6 și o viteză a arborelui de 10.000, introduceți următorul cod la începutul operațiunii Custom G Code   *

(T6   * 4mm Endmill)

M6 T6

M3 S10000

Rețineți că ratele de feed vor fi generate în mod corect de către Postprocessor, numai dacă ratele de feed G-Cod personalizat sunt scrise în Unități / secundă.

## Utilizare


<div class="mw-translate-fuzzy">

1.  Apăsați butonul **<img src="images/Path_Custom.png" width=16px> [Custom](Path_Custom.md)
**
2.  Scrieți codul G personalizat cu proprietatea **G Code**

a noului obiect creat. Consulatați pagina [Path scripting](Path_scripting.md) pentru comenzile G-Code acceptae.


</div>

## Proprietăți

-    **G Code**   * Comenzile G Code personalizate pentru a construi calea





{{Path_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Path](Path_Workbench.md) > Path Custom/ro
