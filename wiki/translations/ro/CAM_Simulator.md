# CAM Simulator/ro
---
 GuiCommand:   Name: Path Simulator   Workbenches: Path Workbench   Path ---


</div>



## Descriere


<div class="mw-translate-fuzzy">

Acest instrument simulează lucrarea de desen prin scanarea modelelor 3D ale instrumentelor folosite în fiecare operație, de-a lungul căilor de cod G, prin scăderea materialelor din stoc/semifabricat, unde se suprapun stocul și instrumentul, asigurând vizualizarea. de muncă. Acest lucru face posibilă detectarea și izolarea erorilor înainte de a efectua lucrul la o freză/CNC


</div>

![](images/Path-Simulation.gif )

## Usage


<div class="mw-translate-fuzzy">

## Utilizare

1.  Apăsați butonul **<img src="images/Path_Simulator.png" width=16px> [CAM Simulator](Path_Simulator.md)
**
2.  Debifați orice Operații care nu trebuie simulate
3.  Acordați cu finețe setările de viteză și de precizie.
4.  Selectați lucrarea pentru simulare din meniul derulant.
5.  Apăsați butonul Redare sau redați o animație a operațiunilor.
    Apăsați butonul Fast Forward pentru a face acest lucru chiar și pentru traiectorii complicate.
6.  Funcția Pauză și funcționalitatea cu un singur pas sunt furnizate pentru a rezolva anumite tăieturi sau mișcări.
7.  Faceți clic pe butonul Anulare pentru a elimina stocul/semifabricatul creat pentru simulare. Dacă faceți clic pe OK, acest obiect va fi păstrat în lucrarea dvs.


</div>




<div class="mw-translate-fuzzy">

## Proprietăți

1.  Necesită contribuție


</div>


<div class="mw-translate-fuzzy">

-    **Playback Speed**: The speed of the simulation playback, in G-Code lines/second

-    **Accuracy**: The accuracy of the simulation expressed as a percentage indicating the simulations deviation from the Job. For interactive simulation, reducing accuracy to 0.3 works much faster.

-    **Job**: The Job used as the basis of the simulation

-    **Operation List**: The list of Operations selected for inclusion in the simulation.


</div>





{{CAM_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [CAM](CAM_Workbench.md) > CAM Simulator/ro
