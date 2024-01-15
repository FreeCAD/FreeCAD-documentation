# Macro Toggle Panels Visibility/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Toggle Panels Visibility
|Translate=Nascondi Pannelli
|Icon=Macro_Toggle_Views_Visibility.png
|Description=Questa macro commuta la visibilità dai vari punti di vista supportati in FreeCAD, permettendo di visualizzare la finestra principale in tutto lo spazio disponibile sullo schermo.
|Author=Piffpoof
|Version=1.0
|Date=2015-01-17|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/d/d0/Macro_Toggle_Views_Visibility.png Toolbar icon]
|SeeAlso=[https://forum.freecadweb.org/viewtopic.php?f=22&t=30450&hilit=Toggle_Panels Toggle_Panels]
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Descrizione

Quando si lavora con FreeCAD, in certi momenti servono molte finestre di supporto aperte, come Combo View, Report, ecc., in altri momenti si desidera nascondere tutte le finestre di supporto in modo che tutto lo spazio disponibile sullo schermo possa essere utilizzato per visualizzare il modello in lavorazione. Questa macro consente di nascondere tutte le finestre di supporto, o di renderle nuovamente visibili, con un solo clic sulla barra degli strumenti.


</div>

## Installation


<div class="mw-translate-fuzzy">

## Installazione

L\'installazione si realizza copiando i due codici nella appropriata directory delle Macro. Dopo sono invocabili dal menu Macro. È molto utile aggiungerle entrambe in una barra degli strumente, in modo da renderle disponibili più facilmente.

-   vedere la pagina [Come installare le macro](How_to_install_macros/it.md)
-   vedere la pagina [Personalizzare la barra degli strumenti](Customize_Toolbars/it.md)


</div>

## Usage


<div class="mw-translate-fuzzy">

## Uso

Fare clic sul pulsante della barra degli strumenti associato, o richiamarle dal menu Macro. Tutte le finestre di supporto quali Console Python, Rapporto e Vista Combinata diventeranno tutte visibili o tutte nascoste.


</div>

## User Interface 


<div class="mw-translate-fuzzy">

## Interfaccia utente 

L\'azione dell\'utente è immediatamente confermata dal fatto che le finestre di supporto appaiono o spariscono.


</div>



## Script

Toolbar icon ![](images/Macro_Toggle_Views_Visibility.png )

**Macro_Toggle_Panels_Visibility.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
# macro to toggle visibility of Report view, Python console, Combo view
from PySide import QtCore, QtGui
mainWindow = FreeCADGui.getMainWindow()
dockWidgets = mainWindow.findChildren(QtGui.QDockWidget)
for dw in dockWidgets:
    if dw.objectName() == "Python console":
        pcWidget = dw
    if dw.objectName() == "Combo View":
        cvWidget = dw
    if dw.objectName() == "Report view":
        rvWidget = dw
     
if pcWidget.isVisible():
    pcWidget.hide()
    cvWidget.hide()
    rvWidget.hide()
else:
    pcWidget.show()
    cvWidget.show()
    rvWidget.show()

}}



---
⏵ [documentation index](../README.md) > Macro Toggle Panels Visibility/it
