---
- GuiCommand:/ro
   Name:Part Revolve
   Name/ro:Part Revolve
   MenuLocation:Part → Revolve
   Workbenches:[Part](Part_Workbench/ro.md), Complete
   SeeAlso:
---


</div>


<div class="mw-translate-fuzzy">

Se rotește obiectul selectat în jurul unei axe date. Următoarele tipuri de forme sunt permise și conduc la formele de ieșire listate ([See Notes for exceptions](#Notes.md)):


</div>

  Input shape   Output shape
  ------------- ----------------------------
  Vertex        Edge
  Edge          Face
  Wire          Shell
  Face          Solid
  Shell         Compound solid (Compsolid)


<div class="mw-translate-fuzzy">

Solidele sau solidele compuse nu sunt permise ca forme de intrare. Compuși normali nu sunt permise în acest moment. Viitoarele versiuni vor verifica forma actuală tip de obiecte compuse.


</div>

![](images/Dialog-revolve.png )


<div class="mw-translate-fuzzy">

Argumentul Unghi specifică cât de departe trebuie să se rotească obiectul. coordonatele direcționează originea axei de rotație, în raport cu originea a sistemului de coordonate.


</div>


<div class="mw-translate-fuzzy">

If you select a user defined axis, the numbers define the direction of the revolving axis with respect to the coordinate system: If the Z coordinate is 0 and the Y and X coordinate are non-zero, then the axis will lie in the X-Y-plane. Its angle is such that its tangent is the ratio of the given X and Y coordinates.


</div>

### Note

-   Dacă versiunea dvs. de FreeCAD are o casetă de selectare pentru dialogul Solid în dialogul Revolve, puteți face Solids din filamente și muchii închise.
-   Dacă Revolve este efectuată utilizând o axă care intersectează fața pentru a se roti și doriți să creați un solid, rezultatul poate fi nevalid. Acest lucru se poate întâmpla din diferite motive, auto-intersecție, direcție etc.





  
