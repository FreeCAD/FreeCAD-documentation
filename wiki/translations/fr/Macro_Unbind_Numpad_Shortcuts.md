# Macro Unbind Numpad Shortcuts/fr

 {{Macro/fr
|Name=Macro Unbind Numpad Shortcuts
|Icon=Macro_Unbind_Numpad_Shortcuts.png
|Description=redéfinit les commandes de vue standard des touches numériques à Ctrl + chiffre, afin qu'elles ne fassent pas tourner la vue par accident lors de la saisie de nombres.
|Author=DeepSOIC
|Version=1.0
|Date=2018-04-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/1e/Macro_Unbind_Numpad_Shortcuts.png ToolBar Icon]
}}

## Description

Lors de la saisie de nombres, et que la zone de saisie du numéro n\'est pas correctement mise au point, FreeCAD réagira aux chiffres en changeant de vue standard. Cette macro est un moyen rapide de relier les raccourcis à Ctrl + numéro. Cela n\'aide pas beaucoup à entrer des nombres, mais au moins la vue ne tournera pas comme une folle.

Voir le thread sur forum [How to turn off (disable) Numpad navigation?](https://forum.freecadweb.org/viewtopic.php?f=3&t=26667)

## Utilisation

1\. Copiez-collez le code de la macro dans la console Python de FreeCAD.

2\. Appuyez deux fois sur Entrée (pour vous assurer que tout est exécuté).

3\. Redémarrez FreeCAD pour que les modifications prennent effet.

## Script

ToolBar Icon ![](images/Macro_Unbind_Numpad_Shortcuts.png )

**Macro\_Unbind\_Numpad\_Shortcuts.FCMacro**


{{MacroCode|code=
preset = [
    ("Std_ViewAxo"   , "Ctrl+0"),
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

