# FEM MaterialSolid/ro
---
- GuiCommand   *   Name   *FEM MaterialSolid    MenuLocation   *Model → FEM material for solid   |Workbenches   *[Shortcut   *M,M   SeeAlso   *[[FEM_tutorial|FEM tutorial](FEM_Workbench___FEM]].md)---


</div>

## Descriere

Adaugă proprietăți materiale la o piesă.

![](images/FEMMaterialSolidProperties.png ) 
*The FEM material task panel*


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

-   Click pe <img alt="" src=images/FEM_MaterialSolid.png  style="width   *32px;"> sau selctați **Model** → **<img src="images/FEM_MaterialSolid.png" width=32px> FEM material for solid** din meniul principal.
-   Dublu click pe obiectul creat **<img src="images/FEM_MaterialSolid.png" width=32px> SolidMaterial** obiectul

![](images/FEMMaterialProperties.PNG )

-   -   Selectați un material. Pentru analiza mecanică mecanică, **CalculiX-Steel** este o opțiune tipică.
    -   Cu condiția să aplicați materialul întregului obiect, nu selectați entități geometrice (liste de referință goale). Materialul va fi aplicat modelului întreg. Altfel, atribuiți manual materiale pentru anumite piese ale modelului, selectând unele dintre ele pentru fiecare material introdus, dar nu lăsați nici o parte a modelului fără materiale atribuite.
    -   Puteți ajusta proprietățile materialelor, cum ar fi densitatea, modulul de elasticitate Young, coeficientul Poisson etc., cu toate acestea majoritatea materialelor obișnuite sunt deja disponibile în presetări și nu au nevoie de modificări.
    -   Dacă efectuați modificări, puteți salva materialul personalizat.

-   Click pe **Close** pentru a închide dialogul și a crat un obiect **<img src="images/FEM_MaterialSolid.png" width=32px> SolidMaterial
**


</div>

## Notă


<div class="mw-translate-fuzzy">

1.  Pentru Proprietățile mecanice ale materialului utilizați cardul/tabelul \*MATERIAL în CalculiX. Detalii despre proprietățile mecanice ale materialului sunt explicate la adresa <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node216.html>


</div>





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM MaterialSolid/ro
