 {{VeryImportantMessage|Ovi su alati sada uključeni u [Manipulator Workbench](Manipulator_Workbench/hr.md). Instalirajte ovu radnu površinu za najnovija ažuriranja tih alata.}}


<div class="mw-translate-fuzzy">


{{Macro/hr
|Name=Center Faces of Parts
|Translate=Središnja lica dijelova
|Icon=Macro_Center_Align_Objects_with_Faces_or_Edges.png
|Description=Ova makronaredba poravnava objekte preko ograničenja lica ili rubova. Ovi su alati sada uključeni u [https://github.com/easyw/Manipulator Manipulator Workbench]. Instalirajte ovu radnu površinu za najnovija ažuriranja tih alata.
|Author=easyw-fc
|Version=1.5.3
|Date=2017-10-01
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/e/ee/Macro_Center_Align_Objects_with_Faces_or_Edges.svg ToolBar Icon]<br/>[https://www.freecadweb.org/wiki/images/8/8b/Mover-ico.png Mover-ico]<br/>[https://www.freecadweb.org/wiki/images/e/ee/Caliper-ico.png Caliper-ico]
}}


</div>


<div class="mw-translate-fuzzy">

## Opis


</div>


{{Codeextralink|https://raw.githubusercontent.com/easyw/FreeCAD_Macros/master/Align%20Objects/CenterAlignObjectswFacesEdges.py}}

## Alati


<div class="mw-translate-fuzzy">

**Aligner** ![](images/Aligner-ico.png ): skup alata za pomicanje i poravnavanje 3D dijelova


</div>


<div class="mw-translate-fuzzy">

**Mover** ![](images/Mover-ico.png ): skup alata za pomicanje i okretanje 3D dijelova na različitim osima


</div>


<div class="mw-translate-fuzzy">

**Measure** ![](images/Caliper-ico.png ): skup alata za mjerenje 3D dijelova, s nekim mjerama Snap i Radius, Length, Angle.


</div>

Ovi pomoćnici rade s **Part, App :: Part i Body objektima**. Svaki Alat može biti **Plutajući** ili **Usidren lijevo ili desno**.

------------------------------------------------------------------------

## OLD Reference 

Ovaj makronaredba pokriva sljedeća ograničenja:

-   Koncentrično ograničenje među necilindričnim dijelovima;
-   Ograničenje na središnja lica and/or rubove.
-   Radi i sa novim Body i App :: Part kontejnerima, kao i sa STEP hijerarhijom.

![](images/Center-align-faces.png )

![](images/center-align-faces-in-action.gif )

![](images/center-align-Body-objects.gif )

![](images/utube-alignment-tool-tutorial.png )

[Aligning tool video tutorial](https://youtu.be/qzixT157jJU)

![](images/utube-alignment-STEP-models.png )

[Aligning STEP models video tutorial](https://youtu.be/aQcPqhlgHBU)


<div class="mw-translate-fuzzy">

## koristite

Lica ili rubovi ograničavaju se među necilindričnim dijelovima: Samo otvorite FC dokument, pokrenite Macro i odaberite dva ili više Faces/Edges koje želite poravnati. Kliknite na gumb Align i to je to!


</div>

## Skripta

Ikona za vašu alatnu traku<img alt="" src=images/Macro_Center_Align_Objects_with_Faces_or_Edges.png  style="width:50px;">

**CenterAlignObjectswFacesEdges.py**

After downloading the file here
GitHub page
<https://github.com/easyw/FreeCAD_Macros/tree/master/Align%20Objects>
code:
<https://github.com/easyw/FreeCAD_Macros/raw/master/Align%20Objects/CenterAlignObjectswFacesEdges.py>
you need to copy the file to your macro directory.
[How to install macros](How_to_install_macros.md)

## Link

Forum : [Faces or Edges constraint among non cylindrical parts Macro](http://forum.freecadweb.org/viewtopic.php?f=22&t=18655)




