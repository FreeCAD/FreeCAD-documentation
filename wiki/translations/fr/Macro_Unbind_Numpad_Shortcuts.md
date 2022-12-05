# Macro Unbind Numpad Shortcuts/fr
{{Macro/fr
|Name=Macro Unbind Numpad Shortcuts
|Icon=Macro_Unbind_Numpad_Shortcuts.png
|Description=Lorsque vous saisissez des chiffres et que la zone de saisie n'est pas correctement mise au point, FreeCAD réagit aux chiffres en changeant de vue standard. Cette macro est un moyen rapide de relier les raccourcis à Ctrl+numéro. Cela n'aide pas beaucoup à la saisie de chiffres, mais au moins la vue ne tournera pas comme une folle.
|Author=DeepSOIC
|Version=2.0
|Date=2022-04-13
|FCVersion=0.20
|Download=[https://www.freecadweb.org/wiki/images/1/1e/Macro_Unbind_Numpad_Shortcuts.png Icône de la barre d'outils]
}}

## Description

Lors de la saisie de nombres, et que la zone de saisie du numéro n\'est pas correctement mise au point, FreeCAD réagira aux chiffres en changeant de vue standard. Cette macro est un moyen rapide de relier les raccourcis à Ctrl + numéro. Cela n\'aide pas beaucoup à entrer des nombres, mais au moins la vue ne tournera pas comme une folle.

Voir le thread sur forum [How to turn off (disable) Numpad navigation?](https://forum.freecadweb.org/viewtopic.php?f=3&t=26667)

## Utilisation

1\. Copiez-collez le code de la macro dans la console Python de FreeCAD.

2\. Appuyez deux fois sur Entrée (pour vous assurer que tout est exécuté).

3\. Redémarrez FreeCAD pour que les modifications prennent effet.

## Script

Icône de la barre d\'outils ![](images/Macro_Unbind_Numpad_Shortcuts.png )

**Macro_Unbind_Numpad_Shortcuts.FCMacro**


{{MacroCode|code=
preset = [
    ("Std_ViewIsometric"   , "Ctrl+0"),
    ("Std_ViewFront" , "Ctrl+1"),
    ("Std_ViewTop"   , "Ctrl+2"),
    ("Std_ViewRight" , "Ctrl+3"),
    ("Std_ViewRear"  , "Ctrl+4"),
    ("Std_ViewBottom", "Ctrl+5"),
    ("Std_ViewLeft"  , "Ctrl+6"),
]
for (cmd, shortcut) in preset:
    App.ParamGet("User parameter:BaseApp/Preferences/Shortcut").SetString(cmd, shortcut)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Unbind Numpad Shortcuts/fr
