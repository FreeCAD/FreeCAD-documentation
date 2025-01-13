# Macro ObjectInfo/it
{{Macro/it
|Name=Macro ObjectInfo
|Translate=Info oggetto
|Description=Questa WorkBench consente di ottenere informazioni riguardo il volume, superficie, baricentro e momento di inerzia dell'oggetto selezionato. <br><br>Questa non è una macro ma un Ambiente di lavoro (workbench), decomprimere il file .zip e incollare la directory completa nella directory utente Mod [https://github.com/KeithSloan/FreeCAD_Info/archive/master.zip Info]
|Author=keithsloan52
|Version=1.0
|Date=2012-11-09
|FCVersion=Until 0.17 '''and PyQt4'''
|Download=[https://wiki.freecad.org/images/2/29/Macro_ObjectInfo.png ToolBar Icon]
|SeeAlso=[Arch Ispeziona](Arch_Survey/it.md)
}}



## Descrizione

Questo Ambiente permette di conoscere le informazioni sul volume, la superficie, il centro di massa e il momento d\'inerzia dell\'oggetto selezionato.

<img alt="" src=images/ObjectInfoIt.png  style="width:480px;">



## Installazione

In Linux, creare la cartella \"Mod\" in .FreeCAD, nella propria Home. Poi, all\'interno di \"Mod\", creare la cartella \"Info\" in cui estrarre l\'archivio. In Windows, creare la cartella \"Info\" in C:\\Program Files\\FreeCAD0.xx\\Mod.



## Utilizzo

Quindi avviare FreeCAD, aprire il file STEP e passare all\'ambiente \"Info\" tramite l\'ambiente switcher o andando al menu Visualizza → Workbench. Ora selezionare il proprio solido e fare clic sull\'icona \"Info\"; la barra delle applicazioni a sinistra mostrerà alcune informazioni sul modello, inclusi il volume, l\'area della superficie, il centro di massa e il momento di inerzia.



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



## Link

Si tratta di un modulo creato da un utente di FreeCAD ottenibile presso <http://www.sloan-home.co.uk/FreeCAD/Info/Info.html>

Dal Forum [Info Workbench - Help with icons please.](http://forum.freecadweb.org/viewtopic.php?f=10&t=3185)



---
⏵ [documentation index](../README.md) > Macro ObjectInfo/it
