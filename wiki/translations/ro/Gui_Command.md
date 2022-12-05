# Gui Command/ro
{{TOCright}}


<div class="mw-translate-fuzzy">

GuiCommand este una dintre cele mai importante funcții ale FreeCAD în principalul punct de interacțiune al utilizatorului. De fiecare dată când utilizatorul selectează un element de meniu sau apasă butonul unei bare de instrumente pe care îl activează a GuiCommand. Unele dintre atributele unui GuiCommand sunt:

-   Definește un nume
-   Conține o pictogramă
-   Definește domeniul de aplicare pentru o anulare / refacere
-   Are o pagină de ajutor
-   Deschide și controlează dialogurile
-   Înregistrare macro
-   si asa mai departe\...


</div>

## Naming


<div class="mw-translate-fuzzy">

### Nominalizare

The GuiCommand is named in a certain way: *ModuleName_CommandName* e.g \"Base_Open\" this is the Open Gui Command in the Base system. The GuiCommand in a certain module is named with the module name in front e.g. \"Part_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

If the docu is not finished use [Template:UnfinishedDocu](Template_UnfinishedDocu.md)


</div>

## Help page 


<div class="mw-translate-fuzzy">

### Pagina Help 

Fiecare GuiCommand trebuie să aibă o pagină de ajutor. Pagina de ajutor este găzduită pe FreeCAD docu wiki. Articolul are același nume ca și GuiCommand, de ex. [Draft ShapeString](Draft_ShapeString.md).


</div>


<div class="mw-translate-fuzzy">

To create your own help pages you can use the template: [GuiCommand model](GuiCommand_model.md)


</div>


<div class="mw-translate-fuzzy">

Exemplu:

-   [Draft ShapeString](Draft_ShapeString.md)
-   [Draft Line](Draft_Line.md)


</div>


<div class="mw-translate-fuzzy">

### Iconițe

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


</div>

<img alt="" src=images/Tango-Palette.png  style="width:400px;">


<div class="mw-translate-fuzzy">

Every GuiCommand has to have an icon. We use the [Tango icon set](http://tango.freedesktop.org/Tango_Desktop_Project) and its guidelines. On the right side you see the tango color palette.


</div>


<div class="mw-translate-fuzzy">

Preferable all Icons are drafted with SVG with e.g. [Inkscape](http://inkscape.org). This makes it easier to apply changes and derive additional Icons in the same application space.


</div>


<div class="mw-translate-fuzzy">

**icons color coding chart**


</div>

<img alt="" src=images/Colorchart.png  style="width:200px;">

Încercăm cât mai mult posibil să respectăm această diagramă, astfel încât culoarea icoanelor are un sens direct.



---
![](images/Right_arrow.png) [documentation index](../README.md) > Gui Command/ro
