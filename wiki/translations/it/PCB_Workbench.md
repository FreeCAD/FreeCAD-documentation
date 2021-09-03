

## Introduzione


{{TOCright}}

[Circuito stampato](https://it.wikipedia.org/wiki/Circuito_stampato) Ambiente per FreeCAD (PCB)

Ambiente per circuiti stampati flessibile per FreeCAD (PCB)

Il modulo permette di importare/creare schede PCB in FreeCAD. Portata del modulo:

-   supporto per molti livelli diversi,
-   possibilità di scegliere colori, trasparenza e nomi per ogni layer,
-   il modulo permette di importare modelli IGES/STP con colori,
-   possibile mostrare fori/vie indipendenti.

## Riferimenti

-   Autore: marmni
-   Pagina principale: <https://sourceforge.net/projects/eaglepcb2freecad/>
-   Codice sorgente su github: <https://github.com/marmni/FreeCAD-PCB>

## Strumenti

Per una descrizione dettagliata dell\'uso del ambiente si veda **index.pdf** nel codice sorgente o [manuale](https://raw.githubusercontent.com/marmni/FreeCAD-PCB/master/index.pdf)

Barra degli strumenti

![](images/PCB-menu-orizz.png )

Menu a discesa

![](images/PCB-export-BOM.png ) ![](images/PCB-export-hole.png ) ![](images/PCB-create-new.png ) ![](images/PCB-explode.png ) ![](images/PCB-bounding-box.png )

## Installazione

### Installazione automatica 

Questo ambiente può essere installato dal [Addon Manager](Std_AddonMgr/it.md).

### Da GitHub 

**Prerequisiti**

FreeCAD-PCB richiede FreeCAD nella versione 0.18 o superiore e Python versione 2.7 o superiore.

**Istruzioni per l\'installazione di Linux** (Da GitHub)

Decomprimere il file zip scaricato e copiare la cartella estratta nella directory dove è installato FreeCAD (sottocartella Mod).

Example:

-   FreeCAD path:

~/Programs/FreeCAD

-   So copy mod to folder

~/Programs/FreeCAD/Mod

-   You can also copy files to folder

~/.FreeCAD/Mod .

-   Next change read/write permission to 777. Please don\'t forget about parameter -R!

Example:

chmod 777 -R PCB

**Istruzioni per l\'installazione di Windows** (Da GitHub)

Decomprimere il file zip scaricato e copiare la cartella estratta nella direzione in cui è installato FreeCAD (sottocartella Mod).

Example:

-   FreeCAD path:

C:/Program Files/FreeCAD-0.18

-   So copy mod to folder

C:/Program Files/FreeCAD-0.18/Mod

-   Next change read/write permission for all users. Click right button on folder PCB and choose Properties →

Security → Edit → Users and mark all checkboxes under \'Allow\' option.

**Istruzioni per l\'installazione di MacOS** (Da GitHub)

## Riferimento a FreeCAD-PCB Ambiente 

-   Wiki del Ambiente: [Ambienti esterni](https://wiki.freecadweb.org/External_workbenches)
-   Wiki di FreeCAD: [Pagina principale Wiki](https://wiki.freecadweb.org/Main_Page)
-   Forum di FreeCAD: [EaglePCB importer for FreeCAD](http://forum.freecadweb.org/viewtopic.php?f=9&t=5107)
-   Tutorial:
-   Video: [EaglePCB\_2\_FreeCAD - FreeCAD odczyt plików brd z programu Eagle](https://www.youtube.com/watch?v=81NsljRJx8c&feature=youtu.be)
-   Archivio: [PCB biblioteca](https://github.com/marmni/FreeCAD-PCB-library)
-   Segnalazione di bug: Si prega di segnalare i bug a <https://github.com/marmni/FreeCAD-PCB/issues>

## Altri riferimento utili 

-   [EaglePCB su sourceforge](https://sourceforge.net/projects/eaglepcb2freecad/)
-   [Ricette macro](Macros_recipes/it.md)
-   [Scaricare FreeCAD](Download/it.md)
-   [Portale della comunità FreeCAD](FreeCAD_Community_Portal/it.md)



[Category:Sandbox{{\#translation:}}](Category:Sandbox.md) [Category:User Documentation{{\#translation:}}](Category:User_Documentation.md) [Category:Addons{{\#translation:}}](Category:Addons.md) [Category:External Workbenches{{\#translation:}}](Category:External_Workbenches.md)
