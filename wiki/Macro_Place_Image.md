# Macro Place Image
{{Macro
|Name=Macro Place Image
|Description=Creates an ImagePlane and aligns it to an existing Draft Rectangle.
|Author=heda
|Version=0.1
|Date=2023-01-30
}}

## Description

Creates an [ImagePlane](Image_CreateImagePlane.md) and aligns it to an existing [Draft Rectangle](Draft_Rectangle.md).

## Usage

Select a Draft Rectangle, run the macro. See \_\_doc\_\_ for limitation.

## Install

Through the [Addon manager](Std_AddonMgr.md).

## Link

Forum: No dedicated thread, but sprung out of [forum post](https://forum.freecadweb.org/viewtopic.php?f=22&t=75606&).

## Version

v0.1 2023-01-30 : first release

## Script

 **Macro_Place_Image.FCMacro**


{{MacroCode|code=
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ***************************************************************************
# *   Copyright (c) 2023 heda <heda @ freecad forum>                        *
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


__Name__ = 'Place_Image'
__Comment__ = 'Aligns ImagePlane to existing draft rectangle'
__Author__ = 'heda @ fc-forum'
__Version__ = '0.1'
__Date__ = '2023-01-30'
__License__ = 'LGPL-2.0-or-later'
__Web__ = ''
__Wiki__ = 'https://wiki.freecadweb.org/Macro_Place_Image'
__Icon__ = ''
__Help__ = 'Select rectangle, run macro and image is placed.'
__Status__ = 'Stable'
__Requires__ = 'tested on FreeCAD v0.20'
__Communication__ = 'forum'
__Files__ = ''


__doc__ = """
Works as intended on XY-plane.
When out of XY-plane, not so much.
Feel free to improve the placement logic.
"""


from pathlib import Path as pyPath
from PySide.QtGui import QMessageBox, QFileDialog

import Draft
import FreeCAD as App
import FreeCADGui as Gui

doc = App.ActiveDocument
sel = Gui.Selection.getSelection()
rect = None

def message(msg):
    QMessageBox.information(None, __Name__, msg)

if sel:
    sel, *_ = sel
    if hasattr(sel, 'Proxy') and isinstance(sel.Proxy, Draft.Rectangle):
        rect = sel
    else:
        message('Sorry, selected object needs to be a draft rectangle.')
else:
    message('No selection, select a draft rectangle.')

if rect:
    rname = rect.Name
    picformats = '*.png *.bmp *.jpg *.jpeg'
    pic, _ = QFileDialog.getOpenFileName(None, 'Select Image',
                                         '', f'Images ({picformats})')
    if pic:
        picname = pyPath(pic).stem.replace(' ', '_')
        imp = doc.addObject('Image::ImagePlane', picname)
        imp.ImageFile = pic

        imp.setExpression('XSize', f'{rname}.Length')
        imp.setExpression('YSize', f'{rname}.Height')
        imp.setExpression('.Placement.Base.x',
                          f'{rname}.Placement.Base.x + XSize / 2')
        imp.setExpression('.Placement.Base.y',
                          f'{rname}.Placement.Base.y + YSize / 2')
        imp.setExpression('.Placement.Base.z',
                          f'{rname}.Placement.Base.z - 0.1 mm')
        imp.setExpression('.Placement.Rotation.Angle',
                          f'{rname}.Placement.Rotation.Angle')
        imp.setExpression('.Placement.Rotation.Axis',
                          f'{rname}.Placement.Rotation.Axis')

        rect.ViewObject.Visibility = False
        rect.setExpression('.Label2',  f'<<{picname}>>')
        doc.recompute()
        print('placed image successfully')
}}



---
⏵ [documentation index](../README.md) > Macro Place Image
