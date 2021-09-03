 {{Macro/it
|Name=Macro Toggle Drawstyle
|Translate=Stile di disegno
|Description=Cambia lo Stile di disegno dell'oggetto selezionato.
|Author=Piffpoof
|Version=2.0
|Date=2020-02-02
|FCVersion= >=0.17
|Download=[https://www.freecadweb.org/wiki/images/0/0b/Macro_Toggle_Drawstyle.png ToolBar Icon]
|SeeAlso=[Macro Toggle Drawstyle Optimized](Macro_Toggle_Drawstyle_Optimized/it.md) <img src="images/Macro_Toggle_Drawstyle_Optimized.png" width=24px> per tutte le lingue
}}

## Descrizione

Quando si lavora con FreeCAD ci sono momenti in cui si desidera modificare rapidamente lo stile di disegno dell\'oggetto su cui si sta lavorando. Questo è possibile attraverso il menu a tendina Stile di disegno in cui è possibile selezionare qualsiasi tipo. Questa macro rende disponibili 2 degli stili come pulsante in una barra degli strumenti su cui l\'utente può cliccare per passare da uno stile all\'altro. L\'utente può modificare il codice della macro per selezionare i 2 stili che desidera alternare. Questo non aggiunge delle funzionalità mancanti nel menu a discesa dello Stile, ma ne migliora la praticità.

## Installazione

L\'installazione si realizza copiando i due codici nella appropriata directory delle Macro e invocandole dal menu Macro. È utile aggiungerle entrambe a una barra in modo da renderle facilmente disponibili.

-   vedere la pagina [Come installare le macro](How_to_install_macros/it.md)
-   vedere la pagina [Personalizzare la barra degli strumenti](Customize_Toolbars/it.md)

## Uso

Selezionare un oggetto, quindi fare clic sul pulsante della barra degli strumenti associata, o richiamarle dal menu Macro. Lo stile dell\'oggetto selezionato si alterna tra i due Stili specificati nel codice della macro (vedere il codice sottostante). **Note**: La definizione degli stili è elencata nel codice. Modificando il codice (che è documentato nel codice della macro) l\'utente può selezionare i 2 stili che desidere avere alternabili.

## Interfaccia utente 

L\'oggetto selezionato viene ridisegnato nello stile specificato nella macro.

Script ottimizzato per tutte le lingue, su uno oggetto selezionato o tutti gli oggetti [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=40#p146239) (Sun Nov 27, 2016 6:49 pm)

## Script

ToolBar icon ![](images/Macro_Toggle_Drawstyle.png )

**Macro Toggle Drawstyle.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
#
#
#           Macro: Toggle Draw Style
#
# This macros allows the user to switch between different Drawstyles by clicking on
# the button of a Macro in a toolbar.
#
# initial code:     triplus
# macro-isation:    piffpoof
#
# This macro switches (or toggles) between 2 selected styles from the Drawstyle menu.
# As written the macro toggles between "WireFrame" and "As is".
# Immediately below this text is a list of the legal values for the Drawstyle menu.
# The first 2 lines of executable code are of the form "DrawstyleA = " followed by
# the 2nd line which is of the form "DrawstyleB = ".
# These 2 lines specify which of the Drawstyle values the macro will toggle between.
# Drawstyle "As is" is the system default and so is specified as the first drawstyle.
# The second line specifies which drawstyle will be toggled to and from.
# Any of the legal values may be used, so if, for example, it is desired to toggle between
# the Shaded and Points drawstyles, then the 2 lines of code would be modified to be:
#
# drawstyleA = "Shaded"
# drawstyleB = "Points"
#
# but remember that the hash signs ('#') are not to be present on the executable lines.
#
###Legal Values for Drawstyle###
#
# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"
#
################################

# triplus @ 2016, 2020
# Toggle global display mode
# ==============================

# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"

styleA = 0
styleB = 3

# ==============================

from PySide import QtGui
import FreeCADGui as Gui

mw = Gui.getMainWindow()


act = {
    0: mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs"),
    1: mw.findChild(QtGui.QAction, "Std_DrawStyleFlatLines"),
    2: mw.findChild(QtGui.QAction, "Std_DrawStyleShaded"),
    3: mw.findChild(QtGui.QAction, "Std_DrawStyleWireframe"),
    4: mw.findChild(QtGui.QAction, "Std_DrawStylePoints"),
    5: mw.findChild(QtGui.QAction, "Std_DrawStyleHiddenLine"),
    6: mw.findChild(QtGui.QAction, "Std_DrawStyleNoShading"),
}


actionA = act[styleA]
actionB = act[styleB]


if actionA.isChecked():
    actionB.trigger()
else:
    actionA.trigger()

}}

## Vincolo

La discussione sul foro [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336)




