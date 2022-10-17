# Macro Unbind Numpad Shortcuts/it
<div class="mw-translate-fuzzy">


{{Macro/it
|Name=Macro Unbind Numpad Shortcuts
|Translate=Annulla collegamenti al tastierino numerico
|Icon=Macro_Unbind_Numpad_Shortcuts.png
|Description=Riassocia i comandi di visualizzazione standard dai tasti numerici a Ctrl + digit, in modo che non ruotino la vista per errore durante l'immissione dei numeri.
|Author=DeepSOIC
|Version=1.0
|Date=2018-04-22
|FCVersion=Tutte
|Download=[https   *//www.freecadweb.org/wiki/images/1/1e/Macro_Unbind_Numpad_Shortcuts.png ToolBar Icon]
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Description 

Quando si immettono i numeri e la casella di immissione del numero non è correttamente focalizzata, FreeCAD reagisce alle cifre cambiando le viste standard. Questa macro è un modo rapido per reindirizzare le scorciatoie a Ctrl + numero. Non aiuta molto con l\'inserimento dei numeri, ma almeno la vista non cambia.


</div>

Vedere nel forum la discussione [Come disattivare (disabilitare) la navigazione dal tastierino numerico?](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=26667)

## Utilizzo

1\. Fare copia-incolla del codice della macro nella console Python di FreeCAD.

2\. Premere invio due volte (per assicurarsi che tutto sia eseguito).

3\. Riavviare FreeCAD affinché le modifiche abbiano effetto.

## Script

ToolBar Icon ![](images/Macro_Unbind_Numpad_Shortcuts.png )

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
for (cmd, shortcut) in preset   *
    App.ParamGet("User parameter   *BaseApp/Preferences/Shortcut").SetString(cmd, shortcut)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Unbind Numpad Shortcuts/it
