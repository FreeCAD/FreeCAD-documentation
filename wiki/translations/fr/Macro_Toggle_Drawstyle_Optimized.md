# Macro Toggle Drawstyle Optimized/fr
{{Macro/fr
|Name=Macro Toggle Drawstyle Optimized
|Description=Script optimisé pour toutes les langues et pour les objets sélectionnés ou tous les objets.<br/>Lorsque vous travaillez avec FreeCAD, vous pouvez parfois changer rapidement le style de dessin de l'objet avec lequel vous travaillez. Ceci est disponible via le menu déroulant Drawstyle où n'importe quel style Drawstyle peut être sélectionné. Cette macro rend disponibles 2 des styles de dessin sous forme de bouton cliquable sur une barre d'outils sur laquelle l'utilisateur peut cliquer pour basculer entre les deux styles de dessin.<br/>
|Author=Piffpoof , triplus  
|Version=2.0
|Date=2020-29-01
|FCVersion=0.17 and above
|Download=[https   *//www.freecadweb.org/wiki/images/8/8c/Macro_Toggle_Drawstyle_Optimized.png ToolBar Icon]
|SeeAlso=[Macro Toggle Drawstyle](Macro_Toggle_Drawstyle/fr.md) <img src="images/Macro_Toggle_Drawstyle.png" width=24px>
}}

## Description

Script optimisé pour toutes les langues, pour les objets sélectionnés ou tous les objets.

Trois macros sont disponibles   *

-   Combinaison qui bascule le mode d\'affichage global lorsque rien n\'est sélectionné et/ou bascule le mode d\'affichage des objets sélectionnés si des objets sont sélectionnés. Lorsque les objets sont sélectionnés, le mode d\'affichage global est automatiquement défini sur Tel quel   * [Macro\_Toggle\_Drawstyle\_Optimized.FCMacro](#Script.md) <img alt="" src=images/Macro_Toggle_Drawstyle_Optimized.png  style="width   *24px;">
-   Basculer le mode d\'affichage global   * [Macro\_Toggle\_Drawstyle\_Optimized\_2.FCMacro](#Script_2.md) <img alt="" src=images/Macro_Toggle_Drawstyle_Optimized_2.png  style="width   *24px;">
-   Basculer le mode d\'affichage du ou des objets sélectionnés (modifications visibles uniquement dans le mode d\'affichage général tel quel (situé dans la barre d\'outils Afficher))   * [Macro\_Toggle\_Drawstyle\_Optimized\_3.FCMacro](#Script_3.md) <img alt="" src=images/Macro_Toggle_Drawstyle_Optimized_3.png  style="width   *24px;">

Lorsque vous travaillez avec FreeCAD, vous pouvez parfois changer rapidement le style de dessin de l\'objet avec lequel vous travaillez. Ceci est disponible via le menu déroulant Drawstyle où n\'importe quel style Drawstyle peut être sélectionné. Cette macro rend disponibles 2 des styles de dessin sous forme de bouton cliquable sur une barre d\'outils sur laquelle l\'utilisateur peut cliquer pour basculer entre les deux styles de dessin.

## Installation

L'installation consiste à copier les deux codes dans le répertoire Macro approprié et à l'appeler à partir du menu Macro. Il est de loin préférable de l\'ajouter à la barre d\'outils pour être plus facilement disponible.

-   voir [Comment installer des macros](How_to_install_macros/fr.md) pour plus d\'informations sur l\'installation de ce code de macro
-   voir [Personnaliser les barres d\'outils](Customize_Toolbars/fr.md) pour plus d\'informations sur l\'installation en tant que bouton dans une barre d\'outils

## Utilisation

Sélectionnez un objet, puis cliquez sur le bouton de la barre d\'outils associé ou appelez-le dans le menu Macro. Le style de dessin de l\'objet sélectionné basculera entre les deux styles de dessin spécifiés dans le code de macro (voir la liste de codes ci-dessous).

## Script

Combinaison qui bascule le mode d\'affichage global lorsque rien n\'est sélectionné et/ou bascule le mode d\'affichage des objets sélectionnés si des objets sont sélectionnés. Lorsque les objets sont sélectionnés, le mode d\'affichage global est automatiquement défini tel quel   *

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
    0   * mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs"),
    1   * mw.findChild(QtGui.QAction, "Std_DrawStyleFlatLines"),
    2   * mw.findChild(QtGui.QAction, "Std_DrawStyleShaded"),
    3   * mw.findChild(QtGui.QAction, "Std_DrawStyleWireframe"),
    4   * mw.findChild(QtGui.QAction, "Std_DrawStylePoints"),
    5   * mw.findChild(QtGui.QAction, "Std_DrawStyleHiddenLine"),
    6   * mw.findChild(QtGui.QAction, "Std_DrawStyleNoShading"),
}


default = act[0]
actionA = act[globalA]
actionB = act[globalB]


if sel   *
    obj = []
    default.trigger()
    for s in sel   *
        if s.Object.TypeId == "App   *   *Link"   *
            if s.Object.LinkedObject not in obj   *
                obj.append(s.Object.LinkedObject)
        elif s.Object not in obj   *
            obj.append(s.Object)
        else   *
            pass

    for o in obj   *
        if o.ViewObject.DisplayMode == objectA   *
            o.ViewObject.DisplayMode = objectB
        else   *
            o.ViewObject.DisplayMode = objectA
else   *
    if actionA.isChecked()   *
        actionB.trigger()
    else   *
        actionA.trigger()

}}

## Script 2 

Basculer le mode d\'affichage global   *

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
    0   * mw.findChild(QtGui.QAction, "Std_DrawStyleAsIs"),
    1   * mw.findChild(QtGui.QAction, "Std_DrawStyleFlatLines"),
    2   * mw.findChild(QtGui.QAction, "Std_DrawStyleShaded"),
    3   * mw.findChild(QtGui.QAction, "Std_DrawStyleWireframe"),
    4   * mw.findChild(QtGui.QAction, "Std_DrawStylePoints"),
    5   * mw.findChild(QtGui.QAction, "Std_DrawStyleHiddenLine"),
    6   * mw.findChild(QtGui.QAction, "Std_DrawStyleNoShading"),
}


actionA = act[styleA]
actionB = act[styleB]


if actionA.isChecked()   *
    actionB.trigger()
else   *
    actionA.trigger()
}}

## Script 3 

Basculer le mode d\'affichage du ou des objets sélectionnés (les modifications ne sont visibles qu\'en mode d\'affichage global tel quel (situé dans la barre d\'outils Afficher))   *

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


for s in sel   *
    if s.Object.TypeId == "App   *   *Link"   *
        if s.Object.LinkedObject not in obj   *
            obj.append(s.Object.LinkedObject)
    elif s.Object not in obj   *
        obj.append(s.Object)
    else   *
        pass


for o in obj   *
    if o.ViewObject.DisplayMode == styleA   *
        o.ViewObject.DisplayMode = styleB
    else   *
        o.ViewObject.DisplayMode = styleA
}}




## Liens

Le lien sur forum (2016-11-27 ver   *1.0 FC =\< 0.17)   * [Keyboard shortcut, View toolbar - Wireframe](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=40#p146239)

The Forum link (2020-29-01 ver   *2.0 FC =\> 0.17)    * [Keyboard shortcut, View toolbar - Wireframe](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=14336&start=50#p364692)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Toggle Drawstyle Optimized/fr
