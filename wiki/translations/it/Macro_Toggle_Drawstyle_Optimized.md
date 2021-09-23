# Macro Toggle Drawstyle Optimized/it
{{Macro/it
|Name=Macro Toggle Drawstyle Optimized
|Description=Script ottimizzato per tutte le lingue e per gli oggetti selezionati o tutti gli oggetti. <br/> Quando si lavora con FreeCAD ci sono momenti in cui si desidera cambiare rapidamente lo stile di disegno dell'oggetto con cui si sta lavorando. Questo è disponibile attraverso il menu a discesa Drawstyle in cui è possibile selezionare qualsiasi Drawstyle. Questa macro rende disponibili 2 stili di disegno come pulsante selezionabile su una barra degli strumenti su cui l'utente può fare clic per alternare tra i due stili.
|Author=Piffpoof , triplus  
|Version=2.0
|Date=2020-29-01
|FCVersion=0.17 é più alto
|Download=[https://www.freecadweb.org/wiki/images/8/8c/Macro_Toggle_Drawstyle_Optimized.png ToolBar Icon]
|SeeAlso=[Macro Toggle Drawstyle](Macro_Toggle_Drawstyle/it.md) <img src="images/Macro_Toggle_Drawstyle.png" width=24px>
}}

## Descrizione

Script ottimizzato per tutte le lingue e per oggetti selezionati o tutti gli oggetti.

Tre macro sono disponibile:

-   Combinazione che attiva o disattiva la modalità di visualizzazione globale quando non è selezionato nulla e / o attiva la modalità di visualizzazione degli oggetti selezionati se gli oggetti sono selezionati. Quando gli oggetti sono selezionati, la modalità di visualizzazione globale viene automaticamente impostata su Come è: [Macro\_Toggle\_Drawstyle\_Optimized.FCMacro](#Script.md) <img alt="" src=images/Macro_Toggle_Drawstyle_Optimized.png  style="width:24px;">
-   Attiva/disattiva la modalità di visualizzazione globale: [Macro\_Toggle\_Drawstyle\_Optimized\_2.FCMacro](#Script_2.md) <img alt="" src=images/Macro_Toggle_Drawstyle_Optimized_2.png  style="width:24px;">
-   Attiva/disattiva la modalità di visualizzazione degli oggetti selezionati (le modifiche sono visibili solo nella modalità di visualizzazione globale così com\'è (situata sulla barra degli strumenti Visualizza)): [Macro\_Toggle\_Drawstyle\_Optimized\_3.FCMacro](#Script_3.md) <img alt="" src=images/Macro_Toggle_Drawstyle_Optimized_3.png  style="width:24px;">

Quando lavori con FreeCAD ci sono momenti in cui vuoi cambiare rapidamente lo stile di disegno dell\'oggetto con cui stai lavorando. Questo è disponibile attraverso il menu a discesa Drawstyle in cui è possibile selezionare qualsiasi Drawstyle. Questa macro rende disponibili 2 stili di disegno come pulsante selezionabile su una barra degli strumenti su cui l\'utente può fare clic per alternare tra i due stili.

## Installazione

L\'installazione comprende la copia dei due codici nella directory Macro appropriata e il richiamo dal menu Macro. È molto preferibile aggiungerli entrambi a una barra degli strumenti in modo da renderli più facilmente disponibili.

-   vedi [Come installare le macro](How_to_install_macros/it.md) per informazioni su come installare questa macro
-   vedi [Personalizza barre degli strumenti](Customize_Toolbars/it.md) per informazioni su come installare come pulsante su una barra degli strumenti

## Uso

Seleziona un oggetto, quindi fai clic sul pulsante della barra degli strumenti associato o invoca dal menu Macro. Lo stile di disegno dell\'oggetto selezionato passerà tra i due stili di disegno specificati nel codice macro (vedere l\'elenco dei codici di seguito).

## Script

Combinazione che attiva o disattiva la modalità di visualizzazione globale quando non è selezionato nulla e / o attiva la modalità di visualizzazione degli oggetti selezionati se gli oggetti sono selezionati. Quando gli oggetti sono selezionati, la modalità di visualizzazione globale viene automaticamente impostata su Come è:

The icon ToolBar ![](images/Macro_Toggle_Drawstyle_Optimized.png )

**Macro\_Toggle\_Drawstyle\_Optimized.FCMacro**


{{MacroCode|code=
# triplus @ 2016, 2020
# Toggle object/global display mode
# ==============================

# 0 = "As is"
# 1 = "Flat lines"
# 2 = "Shaded
# 3 = "Wireframe"
# 4 = "Points"
# 5 = "Hidden line"
# 6 = "No shading"

globalA = 0
globalB = 3

a = "Flat Lines"
b = "Shaded"
c = "Wireframe"
d = "Points"

objectA = a
objectB = c

# ==============================

from PySide import QtGui
import FreeCADGui as Gui

mw = Gui.getMainWindow()
sel = Gui.Selection.getSelectionEx()


act = {
    0: mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs"),
    1: mw.findChild(QtGui.QAction, "Std_DrawStyleFlatLines"),
    2: mw.findChild(QtGui.QAction, "Std_DrawStyleShaded"),
    3: mw.findChild(QtGui.QAction, "Std_DrawStyleWireframe"),
    4: mw.findChild(QtGui.QAction, "Std_DrawStylePoints"),
    5: mw.findChild(QtGui.QAction, "Std_DrawStyleHiddenLine"),
    6: mw.findChild(QtGui.QAction, "Std_DrawStyleNoShading"),
}


default = act[0]
actionA = act[globalA]
actionB = act[globalB]


if sel:
    obj = []
    default.trigger()
    for s in sel:
        if s.Object.TypeId == "App::Link":
            if s.Object.LinkedObject not in obj:
                obj.append(s.Object.LinkedObject)
        elif s.Object not in obj:
            obj.append(s.Object)
        else:
            pass

    for o in obj:
        if o.ViewObject.DisplayMode == objectA:
            o.ViewObject.DisplayMode = objectB
        else:
            o.ViewObject.DisplayMode = objectA
else:
    if actionA.isChecked():
        actionB.trigger()
    else:
        actionA.trigger()

}}

## Script 2 

Attiva/disattiva modalità di visualizzazione globale:

The icon ToolBar ![](images/Macro_Toggle_Drawstyle_Optimized_2.png )

**Macro\_Toggle\_Drawstyle\_Optimized\_2.FCMacro**


{{MacroCode|code=
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

## Script 3 

Attiva/disattiva la modalità di visualizzazione degli oggetti selezionati (le modifiche sono visibili solo nella modalità di visualizzazione globale così com\'è (situata sulla barra degli strumenti Visualizza)):

The icon ToolBar ![](images/Macro_Toggle_Drawstyle_Optimized_3.png )

**Macro\_Toggle\_Drawstyle\_Optimized\_3.FCMacro**


{{MacroCode|code=
# triplus @ 2016, 2020
# Toggle selected object(s) display mode
# ==============================

a = "Flat Lines"
b = "Shaded"
c = "Wireframe"
d = "Points"

styleA = a
styleB = c

# ==============================

from PySide import QtGui
import FreeCADGui as Gui

obj = []
mw = Gui.getMainWindow()
sel = Gui.Selection.getSelectionEx()
mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs").trigger()


for s in sel:
    if s.Object.TypeId == "App::Link":
        if s.Object.LinkedObject not in obj:
            obj.append(s.Object.LinkedObject)
    elif s.Object not in obj:
        obj.append(s.Object)
    else:
        pass


for o in obj:
    if o.ViewObject.DisplayMode == styleA:
        o.ViewObject.DisplayMode = styleB
    else:
        o.ViewObject.DisplayMode = styleA
}}




## Collegamento

Il vincolo al forum (2016-11-27 ver:1.0 FC =\< 0.17): [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=40#p146239)

Il vincolo al forum (2020-29-01 ver:2.0 FC =\> 0.17) : [Keyboard shortcut, View toolbar - Wireframe](https://forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=50#p364692)

---
[documentation index](../README.md) > Macro Toggle Drawstyle Optimized/it
