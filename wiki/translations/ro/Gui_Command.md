# Gui Command/ro
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


<div class="mw-translate-fuzzy">

### Nominalizare

The GuiCommand is named in a certain way: *ModuleName\_CommandName* e.g \"Base\_Open\" this is the Open Gui Command in the Base system. The GuiCommand in a certain module is named with the module name in front e.g. \"Part\_Cylinder\".


</div>


<div class="mw-translate-fuzzy">

If the docu is not finished use [Template:UnfinishedDocu](Template:UnfinishedDocu.md)


</div>


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


<div class="mw-translate-fuzzy">

### Cerințe de calitate 

Există o mulțime de GuiCommands (Funcții) în FreeCAD care sunt experimentale sau utilizate în scurt timp pentru punerea în aplicare. Aceste comenzi Gui sunt în mare parte în Atelierele de lucru dedicate cum ar fi Part, Mesh/Plasa sau Cam. Pentru a asigura o bună experiență a utilizatorilor, a fost creat \"Workbench\" \"Complete\". Acest Atelier de lucru include toate GuiCommands care îndeplinesc anumite \"cerințe de calitate \" care sunt descrise aici:


</div>

There are a lot of GuiCommands (tools) in FreeCAD which are experimental or used for a short time to test implementation of new features. These GuiCommands are mostly in the dedicated workbenches like Part, Mesh or Cam. To ensure a good user experience the workbench *Complete* was created. This workbench incorporates all GuiCommands which meet certain quality requirements which are described here:


<div class="mw-translate-fuzzy">

-   Comanda/Funcția trebuie să fie \'\'\' terminat \'\'\'. Nici o lucrare în desfășurare!
-   Trebuie să aibă o \'\'\'pagină de ajutor \'\'\' ca de ex [Draft ShapeString](Draft_ShapeString.md)
    -   Toate câmpurile din [Template: GuiCommand](Template:_GuiCommand.md) trebuie completate
    -   O imagine a dialogurilor pe care comanda le obține în cele din urmă
    -   descrierea detaliată a comenzii și a tuturor parametrilor și setărilor acesteia
    -   Descrierea interfețelor și claselor legate de python cu exemple de cod
-   Configurați o pictogramă și o poziție de meniu corespunzătoare


</div>


<div class="mw-translate-fuzzy">

Sperăm că acest lucru devine adevărat pentru toți GuiCommands din[List of Commands](List_of_Commands.md).


</div>


{{Powerdocnavi

}}

---
[documentation index](../README.md) > Gui Command/ro
