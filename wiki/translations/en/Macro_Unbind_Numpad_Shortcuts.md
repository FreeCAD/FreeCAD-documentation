 {{Macro
|Name=Macro Unbind Numpad Shortcuts
|Icon=Macro_Unbind_Numpad_Shortcuts.png
|Description=When entering numbers, and the number input box is not properly focused, FreeCAD will react to digits by switching standard views. This macro is a quick way to re-bind the shortcuts to Ctrl+number. Doesn't help very much with entering numbers, but at least the view won't spin like crazy.
|Author=DeepSOIC
|Version=1.0
|Date=2018-04-22
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/1e/Macro_Unbind_Numpad_Shortcuts.png ToolBar Icon]
}}

## Description

When entering numbers, and the number input box is not properly focused, FreeCAD will react to digits by switching standard views. This macro is a quick way to re-bind the shortcuts to Ctrl+number. Doesn\'t help very much with entering numbers, but at least the view won\'t spin like crazy.

See forum thread [How to turn off (disable) Numpad navigation?](https://forum.freecadweb.org/viewtopic.php?f=3&t=26667)

## How to use: 

1\. Copy-paste macro code to Py console of FreeCAD.

2\. Press enter twice (to make sure everything is executed).

3\. Restart FreeCAD for the changes to take effect.

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

