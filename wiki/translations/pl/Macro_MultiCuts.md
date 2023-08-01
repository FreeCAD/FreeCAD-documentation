# Macro MultiCuts/pl
{{Macro/pl
|Name=Macro multiCuts
|Name/pl=Macro multiCuts
|Icon=multiCuts.png
|Description=Makro poprawia hierarchię cięć logicznych poprzez automatyczne etykietowanie i używanie kopii dla cięć.
|Author=Dprojects
|Date=2022-08-15
|Version=1.0
}}

## Opis

![](images/MultiCuts_test.gif )

## Skrypt


{{MacroCode|code=

__Title__="multiCuts"
__Author__ = "Dprojects"
__Version__ = "1.0"
__Date__    = "2022-08-15"
__Comment__ = ""
__Web__ = "https://github.com/dprojects/Woodworking"
__Wiki__ = "https://wiki.freecadweb.org/Macro_multiCuts"
__Icon__  = "multiCuts.png"
__IconW__  = "multiCuts.png"
__Help__ = "select base object and next objects to cut the base"
__Status__ = "stable"
__Requires__ = "freecad 0.20.29177"
__Communication__ = "http://www.freecadweb.org/wiki/index.php?title=User:Dprojects"

# ####################################################################
#
# This macro allows to create multi bool cut operation at 
# selected objects. First selected object should be the base 
# element and all other selected will cut the base. The copies will 
# be created for cut, so the objects tree not change. Also there is 
# automatic labeling for better cut hierarchy look. This macro has 
# been created for special request 
# https://forum.freecadweb.org/viewtopic.php?f=31&t=70941 
# but is also available at Woodworking workbench.
#
# Certified platform:
# 
# OS: Ubuntu 22.04 LTS (XFCE/xubuntu)
# Word size of FreeCAD: 64-bit
# Version: 0.20.29177 (Git) AppImage
# Build type: Release
# Branch: (HEAD detached at 0.20)
# Hash: 68e337670e227889217652ddac593c93b5e8dc94
# Python 3.9.13, Qt 5.12.9, Coin 4.0.0, Vtk 9.1.0, OCC 7.5.3
# Locale: English/United States (en_US)
# Installed mods: 
#  * Woodworking 0.20.29177
#
# https://github.com/dprojects/Woodworking
#
# MIT License
# 
# Copyright (c) 2022 Darek L github.com/dprojects
# 
# Permission is hereby granted, free of charge, to any 
# person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the 
# Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish, distribute, 
# sublicense, and/or sell copies of the Software, and to permit 
# persons to whom the Software is furnished to do so, subject 
# to the following conditions:
# 
# The above copyright notice and this permission notice shall 
# be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER 
# DEALINGS IN THE SOFTWARE.
# 
# ####################################################################

import FreeCAD, FreeCADGui


def multiCuts(iObjects):

    cuts = []i = 0
    for o in iObjects:
        
        i = i + 1
        
        if i == 1:
            base = o
            baseName = str(base.Name)
            baseLabel = str(base.Label)
            continue

        copy = FreeCAD.ActiveDocument.copyObject(o)
        copy.Label = "copy, " + o.Label
        
        cutName = baseName + str(i-1)
        cut = FreeCAD.ActiveDocument.addObject("Part::Cut", cutName)
        cut.Base = base
        cut.Tool = copy
        cut.Label = "Cut " + str(i-1) + ", " + baseLabel
        
        FreeCAD.activeDocument().recompute()
        
        base = cut
        cuts.append(cut)
        
    cut.Label = "Cut, " + baseLabel

    return cuts

# ####################################################################
# main
# ####################################################################

multiCuts(FreeCADGui.Selection.getSelection())
FreeCADGui.Selection.clearSelection()

# ####################################################################

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro MultiCuts/pl
