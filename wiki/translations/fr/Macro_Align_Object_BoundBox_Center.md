# Macro Align Object BoundBox Center/fr
{{Macro/fr
|Name=Macro Align Object BoundBox Center
|Description=Aligne 2 objets (ou plus) par le centre de leurs boîtes englobantes.
|Author=heda
|Version=0.2
|Date=2024-11-10
|FCVersion=
}}

## Description

Cette macro aligne 2 objets (ou plus) par le centre de leurs boîtes englobantes.

![](images/Macro_Align_Object_BoundBox_Center.png )



*Macro Align Object BoundBox Center*



## Utilisation

Sélectionnez et lancez.



## Installation

Par le biais du [gestionnaire des extensions](Std_AddonMgr/fr.md).

## Version

-   v0.2 2024-11-10 : gère maintenant aussi les dessins/textes.
-   v0.1 2024-10-23 : première version.

## Code

**Macro_Align_Object_BoundBox_Center.FCMacro**


{{MacroCode|code=
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ***************************************************************************
# *   Copyright (c) 2024 heda <heda @ freecad forum>                        *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************


__Name__ = 'Macro_Align_Object_BoundBox_Center'
__Comment__ = 'Aligns 2 (or more) objects by bounding box'
__Author__ = 'heda @ fc-forum'
__Version__ = '0.2'
__Date__ = '2024-11-10'
__License__ = 'LGPL-2.0-or-later'
__Web__ = ''
__Wiki__ = 'https://wiki.freecad.org/Macro_Align_Object_BoundBox_Center'
__Icon__ = ''
__Help__ = 'Select and launch.'
__Status__ = 'functional'
__Requires__ = 'tested on FreeCAD v0.21'
__Communication__ = ''
__Files__ = ''


__doc__ = """
select 2 or more objects and run macro.
first object is reference, and all subsequent
selections will get a placement that has the
centre at same location as the reference object.

undo transaction is commented out,
since it moves the object back twice...
"""


import FreeCAD as App
import FreeCADGui as Gui

doc = App.ActiveDocument
sel = Gui.Selection.getSelection()

def getBBox(obj):
    if hasattr(obj, 'Shape'):
        return obj.Shape.BoundBox
    elif hasattr(obj.'ViewObject'):
        return obj.ViewObject.getBoundingBox()
    else:
        return None

if len(sel) > 1:

    ref, *moves = sel
    refbb = getBBox(ref)
    msg_skip = 'could not find bbox for {}, skipping...)'
    if refbb:
        # doc.openTransaction('Bbox align objects')
        moved = list()
        for move in moves:
            movebb = getBBox(move)
            if movebb:
                vec = refbb.Center - movebb.Center
                move.Placement.Base = move.Placement.Base + vec
                moved.append(move)
            else:
                print(msg_skip.format(move.Label))
        doc.recompute()
        # doc.commitTransaction()
        if moved:
            txt = [obj.Label for obj in moved]
            print('moved {} to {}'.format(', '.join(txt), ref.Label))
        else:
            print('could not move any objects')
    else:
        print('could not find bbox for ref-obj, bailing...') 
}}



---
⏵ [documentation index](../README.md) > Macro Align Object BoundBox Center/fr
