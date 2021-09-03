


{{Macro/it
|Name=GuiResetToolbars
|Name/it=Gui Reset Tool bars
|Description=Questa macro ripristina la posizione delle barre degli strumenti. Esegui la macro in un workbench che ha una barra degli strumenti mancante.
|Author=PROTORS
|Download=[https://wiki.freecadweb.org/images/f/f8/GuiResetToolbars.svg ToolBar Icon]
|Date=2020-04-21
|Version=1.0.0
|FCVersion= 0.18.4 e piu
|SeeAlso=[https://github.com/protors/ResetToolbars/ Github repository]
}}

## Descrizione

Questa macro ripristina la posizione delle barre degli strumenti.

## Usare

Esegui la macro in un workbench che ha una barra degli strumenti mancante.

## Script

ToolBar Icon ![](images/GuiResetToolbars.svg )

**GuiResetToolbars.FCMacro**


{{MacroCode|code=
# Reset Toolbars position
# Author: Milos Petrasinovic <mpetrasinovic@protors.co>
# PROTORS, Belgrade, Serbia
# info@protors.co
# 
# --------------------
#
# Copyright (C) 2020 PROTORS <info@protors.co>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#  
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#  
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# --------------------

__Name__ = 'GuiResetToolbars'
__Comment__ = 'Reset Toolbars position'
__Author__ = 'PROTORS'
__Version__ = '1.0.0'
__Date__ = '2020-04-21'
__License__ = 'LGPL-3.0-or-later'
__Web__ = "https://github.com/protors/ResetToolbars/"
__Wiki__ = 'https://wiki.freecadweb.org/Macro_GuiResetToolbars'
__Icon__ = 'GuiResetToolbars.svg'
__Help__ = 'Run the macro within a workbench that has missing toolbar(s)'
__Status__ = 'stable'
__Requires__ = 'Freecad >= 0.18.4'
__Communication__ = 'https://github.com/protors/ResetToolbars/issues/'
__Files__ = 'GuiResetToolbars.svg'

import FreeCADGui as gui
from PySide import QtGui, QtCore # FreeCAD's special PySide!

mw = gui.getMainWindow()
tb = mw.findChildren(QtGui.QToolBar)
for i in tb:
    mw.addToolBar(QtCore.Qt.TopToolBarArea, i)
}}

## Link

La discussione sul forum [Reset toolbar position](https://forum.freecadweb.org/viewtopic.php?f=3&t=45452&p=390034#p389404)
