---
- GuiCommand:/ro   Name:FEM ConstraintContact   Name/ro:FEM ConstraintContact   MenuLocation:Model → Mechanical Constraints → Constraint contact   |Workbenches:[Shortcut:   SeeAlso:[[FEM_tutorial/ro|FEM tutorial](FEM_Workbench/ro___FEM]].md)---


</div>

## Descriere

Creează o constrângere MEF pentru contactul între două suprafețe.


<div class="mw-translate-fuzzy">

## Cum se folosește 


</div>


<div class="mw-translate-fuzzy">

1.  Click pe <img alt="" src=images/FEM_ConstraintContact.png  style="width:32px;"> sau alegeți **Model** → **Mechanical Constraints** → **<img src="images/FEM_ConstraintContact.png" width=32px> Constraint contact** din meniul de us.
2.  Select the master face.
3.  Select the slave face.
4.  Enter a contact stiffness.
5.  Enter a friction coefficient.


</div>

## Limite


<div class="mw-translate-fuzzy">

1.  Constrângerea de contact poate fi aplicată numai la două fețe.


</div>


<div class="mw-translate-fuzzy">

## Note


</div>

### CalculiX

1.  Rigiditatea contactului trebuie să fie de 10 ori mai moale (modulul Young) decât modulul de a avea un contact dur. Cu cât este mai mare valoarea rigidității de contact, cu atât este mai mare contactul dintre suprafețe.
2.  Fața slave este fața care intră în fața principală și, prin urmare, are mai multe deformări.
3.  Tabelul \*CONTACT PAIR este utilizat pentru modelarea contactului în CalculiX. Constrângerea folosește contactul optimizat cu constrângeri față-în-față și formula de contact este explicată în detaliu aici la <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>

-   Overview for different contact types: <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>

-   Further interesting informations:

-   -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> and following posts !!!

-   -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=20276>

-   -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=21331>

-   -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699> (initial contact topic)

-   A very detailed CalculiX contact example. ([link](http://dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   A very cool example found in the FreeCAD German subforum. ([link](https://forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))





{{FEM Tools navi

}}  
