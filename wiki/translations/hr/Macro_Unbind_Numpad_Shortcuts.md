# Macro Unbind Numpad Shortcuts/hr
<div class="mw-translate-fuzzy">


{{Macro/hr
|Name=Macro Unbind Numpad Shortcuts
|Translate=Makro Razdvoji Numpad prečace
|Icon=Macro_Unbind_Numpad_Shortcuts.png
|Description=rebinds standard view commands from digit keys to Ctrl+digit, so that they don't spin the view by accident when entering numbers.
|Author=DeepSOIC
|Version=1.0
|Date=2018-04-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/1e/Macro_Unbind_Numpad_Shortcuts.png ToolBar Icon]
}}


</div>

## Description


<div class="mw-translate-fuzzy">

## Opis

Kada unosite brojeve, a okvir za unos broja nije pravilno fokusiran, FreeCAD će reagirati na znamenke prebacivanjem standardnih prikaza. Ova je makronaredba brz način ponovnog vezanja prečaca do Ctrl+broja. Ne pomaže mnogo s unosom brojeva, ali barem pogled neće zavrtjeti kao lud.


</div>

Pogledajte nit na forumu [How to turn off (disable) Numpad navigation?](https://forum.freecadweb.org/viewtopic.php?f=3&t=26667)

## Kako koristiti: 

1\. Copy-paste makro kod na Py konzolu FreeCAD-a.

2\. Dvaput pritisnite enter (kako biste provjerili je li sve izvršeno).

3\. Ponovno pokrenite FreeCAD kako bi promjene stupile na snagu.

## Skripta

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
for (cmd, shortcut) in preset:
    App.ParamGet("User parameter:BaseApp/Preferences/Shortcut").SetString(cmd, shortcut)
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Unbind Numpad Shortcuts/hr
