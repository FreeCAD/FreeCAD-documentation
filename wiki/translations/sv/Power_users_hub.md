# <img alt="" src=images/Power_user_hub.png  style="width:64px;"> Power users hub/sv

------------------------------------------------------------------------




<div class="mw-translate-fuzzy">

Detta är platsen att komma till om du vill ha en djupare insikt i FreeCAD. Här kan du lära dig om hur du anpassar FreeCAD för dina behov.


</div>


<div class="mw-translate-fuzzy">

En av FreeCADs bästa egenskaper är att du kan skripta och utöka den extremt mycket utan att behöva kompilera något eller röra källkoden. All skriptning görs i [python](http://sv.wikipedia.org/wiki/Python_(programspråk)), ett mycket kraftfullt men enkelt programmeringsspråk. Med enkla pythonskript så har du total åtkomst till alla FreeCADs delar. Du kan till exempel:

-   **Skapa och ändra geometri**: Finns det något sorts specialobjekt som du behöver men som inte finns i FreeCADs standardinstallation? Du kan lätt skapa en ny objekttyp, antingen från scratch eller genom att förändra en existerande typ.
-   **Skapa anpassade verktyg och kommandon**: För tillfället så har FreeCAD redn en extensiv funktionalitet, men det finns ännu inte så många smidiga verktyg och kommandon för slutanvändaren än. Men det är redan lätt att skapa ditt eget verktygsset.
-   **Förändra gränssnittet**: FreeCADs användargränssnitt är för tillfället fortfarande mycket enkelt. Men allt finns där för dig för att utöka den för dina behov. Du kan till exempel, skapa verktygslådor att lägga dina egna verktyg i, Skapa specialpaneler för att interagera med dina verktyg, etc.
-   **Förändra scenrepresentationen**: FreeCAD har separata processer för uppbyggnad och beräkning av geometrin och visa den geometrin på din skärm. Du har full åtkomst till det sätt som sceninnehållet visas på skärmen, så därför kan du förändra den representationen, interagera med den , eller lägga till alla sorters specialbeteenden och skärmwidgetar, som information, dragare, ankare eller temporära föremål.


</div>


<div class="mw-translate-fuzzy">

Dessa sidor är i ett tidigt utvecklingsstadie. Om du inte kan hitta den information du letar efter, eller har hittat användbar information på något ställe sim vi inte har länkat till, var då snäll och lämna en kommentar på [pratsidan](Talk_Power_users_hub.md), eller varför inte att du själv lägger till innehåll här!


</div>

## Anpassa FreeCAD 


<div class="mw-translate-fuzzy">

-   [Gränssnittsanpassning](Interface_Customization/sv.md): Startar med början: Verktygslådor och genvägar
-   [Arbeta med makron](Macros/sv.md): Spela in ofta repeterade uppgifter eller pythonkod


</div>

## Skriptning i FreeCAD 

### General


<div class="mw-translate-fuzzy">

**Allmänt**

-   [Introduktion till python](Introduction_to_Python/sv.md) - Se även andra pythonövningar i slutet på denna sida
-   [FreeCAD skriptgrunder](FreeCAD_Scripting_Basics/sv.md): grunderna\...

-   [Nät skript](Mesh_Scripting/sv.md): Hur man interagerar med [Nät modulen](Mesh_Workbench/sv.md)
-   [Gränssnittskommandon](Gui_Command/sv.md) : Lägga till anpassade kommandon till gränssnittet
-   Använda blandade [Enheter](Units/sv.md) i FreeCAD


</div>

### Modules

The functionality of FreeCAD is separated in Modules which deal with special data types and applications. FreeCAD has built-in modules and Extension Modules (plug-ins). Once plugin modules are installed, they become availible to you as easily as the built-in modules. The modules described below are the default modules, includeed in every FreeCAD installation.

-   The [Builtin modules](Builtin_modules.md) are the principal FreeCAD modules. They contain tools for manipulating general FreeCAD configurations, documents and their contents.
-   [Workbench creation](Workbench_creation.md) shows you how to create your own workbench

#### Working with Meshes 


<div class="mw-translate-fuzzy">

\"\"Arbeta med nät\"\"

-   [Nät skript](Mesh_Scripting/sv.md) Hur man interagerar med [Nätmodulen](Mesh_Workbench/sv.md)


</div>

#### Working with Parts 


<div class="mw-translate-fuzzy">

**Använda OpenCasCade**

-   [Del Modulen](Part_Workbench/sv.md): Hur OpenCasCade verktyg och strukturer används i FreeCAD
-   [Topologiska dataskript](Topological_data_scripting/sv.md): Hur man interagerar med Del Modulen
-   [pythonOCC](pythonOCC/sv.md): Hur man släpper fri hela OpenCasCade kraften
-   [Nät till Del](Mesh_to_Part/sv.md): konvertering mellan objekttyper


</div>

#### Accessing the Coin scenegraph 


<div class="mw-translate-fuzzy">

**Komma åt Coin scengrafen**

-   [Coin/Inventor scengrafen](Scenegraph/sv.md): Hur FreeCADs scenrepresentation fungerar
-   [Pivy](Pivy/sv.md): Hur man kommer åt och ändrar scengrafen


</div>

### Controlling the Qt interface 


<div class="mw-translate-fuzzy">

**Kontrollera Qt gränssnittet**

-   [PySide](PySide/sv.md): Hur man kommer åt gränssnittet, och förändrar dess innehåll
-   [Använda FreeCADs gränssnitt](Embedding_FreeCADGui/sv.md) i en annan Qt applikation med PyQt


</div>


<div class="mw-translate-fuzzy">

**Arbeta med parametriska objekt**

-   [Skriptade objekt](Scripted_objects/sv.md): Hur man gör 100% python-skriptade objekt i FreeCAD
-   [Ritningsmodulen](Drawing_Workbench/sv.md): Automatisera 3D-till-2D processen


</div>

-   [Scripted objects](Scripted_objects.md): how to make 100% Python-scripted objects.
    -   [Scripted objects with attachment](Scripted_objects_with_attachment.md): how to make scripted objects attachable to other objects.
    -   [Scripted objects saving attributes](Scripted_objects_saving_attributes.md): how to save and restore attributes of the proxy class with `__getstate__` and `__setstate__`.
    -   [Scripted objects migration](Scripted_objects_migration.md): how to migrate old scripted objects to a new class.

### Examples


<div class="mw-translate-fuzzy">

**Exempel**

-   [Kodbitar](Code_snippets/sv.md) en samling med FreeCAD python kod som du kan använda som ingredienser i dina skript\...
-   [Linjeritningsfunktionen](Line_drawing_function/sv.md): Hur man bygger ett enkelt verktyg att rita linjer med
-   [Skapa dialoger](Dialog_creation/sv.md): Hur man konstruerar dialoger med Qt designer, och använder dem i FreeCAD
-   [Bädda in FreeCAD](Embedding_FreeCAD/sv.md): Hur man importerar FreeCAD som en pythonmodul i andra applikationer
-   [Skissmodulen](Draft_Workbench/sv.md) adderar grundläggande 2D rintningsfunktioner till FreeCAD. Den är helt och hållet skriven i python, så den kan vara ett bra exempel om du vill skriva dina egna moduler.
-   [FreeCAD\'s vektorbibliotek](FreeCAD_vector_math_library/sv.md) : Några praktiska funktioner för att manipulera FreeCAD vektorer. Detta bibliotek är även inkluderat i Skissmodulen.


</div>

## API funktioner 


<div class="mw-translate-fuzzy">

Den kompletta API beskrivningen hittas [här](:<img src="images/Property.png" style="width:16px"> API/sv.md). Notera att den kan vara ofullständig, eftersom vi fortfarande inte har hittat ett sätt att automatiskt inkludera den på denna wiki. För mer rättvisande information, titta i modulerna direkt från FreeCAD.


</div>

Related: [Exposing C++ to Python](Exposing_C%2B%2B_to_Python.md)

## Avancerade ändringar 


<div class="mw-translate-fuzzy">

-   [Uppstart och konfiguration](Start_up_and_Configuration/sv.md): Uppstart och kommandoradsalternativ
-   [Installera på Windows](Installing_on_Windows/sv.md): Använda Windows installeraren
-   [Kompilera FreeCAD på Windows](Compile_on_Windows/sv.md) och [Kompilera FreeCAD på Linux](Compile_on_Linux/sv.md)
-   [Branding](Branding/sv.md): Enkla modifieringar som du kan göra i källkoden för att förändra vissa delar i FreeCAD
-   [Extra pythonmuduler](Extra_python_modules/sv.md) : Utöka FreeCAD\'s pythontolk med dessa kraftfulla moduler!


</div>

## Python övningar 

Dessa är bra allmänna övningar, inte specifika för FreeCAD, som kan vara intressanta för dig om du är helt ny på python.


<div class="mw-translate-fuzzy">

**Python**

-   [Officiell pythonövning](http://docs.python.org/tut/tut.html) En mycket komplett övning för att upptäcka python
-   [pythonövning för icke-programmerare](http://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python) - en excellent wikibok
-   [Python för nybörjare](http://npt.cc.rsu.ru/user/wanderer/ODP/Python_for_Newbies.htm) - en stor övning som täcker allt det grundläggande


</div>


<div class="mw-translate-fuzzy">

**PyQt** - Hur man skapar och hanterar FreeCAD\'s Qt användargränssnitt från python

-   [Grundläggande PyQt övning](http://www.cs.usfca.edu/~afedosov/qttut/) : en enkel och kort linux-baserad övning som kommer att förklara hur man arbetar med PyQt och Qt Designer
-   [Första programmen i PyQt4](http://zetcode.com/tutorials/pyqt4/firstprograms/) : En plattform-agnostisk övning som visar innanmätet i python + qt
-   [programmera Qt applikationer i python](http://vizzzion.org/?id=pyqt) : En djupare övning som täcker hela processen i arbetet med qt och python.


</div>

The following two references are PyQt specific (not PySide) but may offer some information of use:

-   [Basic PyQt tutorial](http://www.cs.usfca.edu/~afedosov/qttut/) : A simple and short linux-based tutorial that will explain how to work with PyQt and Qt Designer
-   [Programming Qt applications in python](http://vizzzion.org/?id=pyqt) : A more in-depth tutorial covering all the process of working with qt and python


<div class="mw-translate-fuzzy">

*Pivy*\' - Hur man interagerar med FreeCAD\'s 3D scener

-   [Grundläggande Pivy övning](http://pivy.coin3d.org/documentation/pycon) : En mycket simpel övning från den officiella Pivy siten
-   [Introduktion av Pivy i studiersturbe](http://www.google.com.br/url?sa=U&start=3&q=http://studierstube.icg.tu-graz.ac.at/doc/pdf/PivyStudierstubeTutorial.pdf&ei=XyC1Sc2wOeCKmQem_eHnBQ&usg=AFQjCNEYhb-0DcUc6OxFVijAe1epBb-4aA) : Ett dokument som egentligen inte är en övning men som på ett bra sätt illustrerar hur Pivy fungerar


</div>

## Grupprojekt


<div class="mw-translate-fuzzy">

På [Grupportalen](free-cad:Community_Portal/sv.md), så kan du hitta andra FreeCAD-baserade projekt som körs av FreeCADs användargrupp. Om du startar ett nytt FreeCAD projekt, ta och lista det där! Vi har också en sida med saker som du kan göra om du skulle vilja [Hjälpa FreeCAD](Help_FreeCAD/sv.md).


</div>

-   [Scientific literature](Scientific_literature.md): articles that reference or use the FreeCAD system in different ways.


{{Powerdocnavi

}}

[<img src="images/Property.png" style="width:16px"> Hubs](Category_Hubs.md)

---
[documentation index](../README.md) > [Hubs](Category_Hubs.md) > Power users hub/sv
