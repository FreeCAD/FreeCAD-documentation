 {{Macro/it
|Name=Macro ObjectInfo
|Translate=Info oggetto
|Description=Fornisce informazioni sull'oggetto selezionato
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09|FCVersion=Until 0.17 '''and PyQt4'''
|Download=Questa non è una macro ma un WorkBench, decomprime il file .zip e incolla la directory completa nella directory degli utenti Mod [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|SeeAlso=<img src=images/Arch_Survey.svg style="width:Arch Survey|24px"> [Arch Survey](Arch_Survey/it.md)
}}

## Descrizione

Questa estensione fornisce il volume, la superfice e altre utili informazioni sull\'oggetto selezionato.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">

## Installazione

In Linux, creare la cartella \"Mod\" in .FreeCAD, nella propria Home. Poi, all\'interno di \"Mod\", creare la cartella \"Info\" in cui estrarre l\'archivio. In Windows, creare la cartella \"Info\" in C:\\Program Files\\FreeCAD0.xx\\Mod.


<div class="mw-translate-fuzzy">

## Utilizzo

Quindi avviare FreeCAD, aprire il file STEP e passare al workbench \"Info\" con il workbench switcher o andando al menu Visualizza → Workbench. Ora seleziona il tuo solido e fai clic sull\'icona \"Info\"; la barra delle applicazioni a sinistra mostrerà alcune informazioni sul modello, inclusi il volume, l\'area della superficie, il centro di massa e il momento della intertia.


</div>

## Codice


{{MacroCode|code=
import webbrowser 

##########
# WorkBenche
# Code used to download the zip file from FreeCAD
##########

FreeCAD.Console.PrintMessage("\n" + "You must download the Info.zip file in the author github KeithSloan/FreeCAD_Infosite" + "\n")
FreeCAD.Console.PrintMessage("http://keithsloan.dynu.com/Keith&Jenny/" + "\n")
webbrowser.open("https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip")

}}

## Legame

Si tratta di un modulo creato da un utente di FreeCAD ottenibile presso <http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

Dal Forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)




