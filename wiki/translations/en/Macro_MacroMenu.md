# Macro MacroMenu/en
{{Macro
|Name=Macro MacroMenu
|Icon=Macro_MacroMenu.png
|Description=Adds the macros found in the macros folder to the FreeCAD Macros menu
|Author=Yorik
|Version=1.0
|Date=2014-08-07
|FCVersion=All
|Download=[https://www.freecadweb.org/wiki/images/1/1e/Macro_MacroMenu.png ToolBar Icon]
}}

## Description

This code was part of the [Draft Workbench](Draft_Workbench.md) and has been removed cf [issue #490](http://freecadweb.org/tracker/view.php?id=490).

## Script

ToolBar Icon ![](images/Macro_MacroMenu.png )

**Macro_MacroMenu.FCMacro**


{{MacroCode|code=

import os,FreeCAD,FreeCADGui
 
macrosList = []
macroPath = FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Macro").GetString("MacroPath") 
 
class MacroCommand():
    "A template for macro commands"
    def __init__(self,macroname):
        self.macroname = macroname
 
    def GetResources(self):
        return {'Pixmap'  : 'Draft_Macro',
                'MenuText': self.macroname,
                'ToolTip': 'Executes the '+self.macroname+' macro'}
 
    def Activated(self):
        target = macroPath+os.sep+self.macroname+'.FCMacro'
        if os.path.exists(target): execfile(target)
            
if macroPath and os.path.isdir(macroPath):
    macros = []
    for f in os.listdir(macroPath):
        if ".FCMacro" in f:
            macros.append(f[:-8])
    for m in macros:
        cmd = 'Macro_'+m
        FreeCADGui.addCommand(cmd,MacroCommand(m))
        macrosList.append(cmd)

}}



---
⏵ [documentation index](../README.md) > Macro MacroMenu/en
