# Macro GuiResetToolbars/fr
{{Macro/fr
|Name=GuiResetToolbars
|Name/fr=GuiResetToolbars
|Description=Cette macro réinitialise la position des barres d'outils. Exécutez la macro dans un plan de travail dont la ou les barres d'outils sont manquantes.
|Author=PR-DC
|Download=[https   *//wiki.freecadweb.org/images/f/f8/GuiResetToolbars.svg Icône de la barre d'outils]
|Date=2020-04-21
|Version=1.0.0
|FCVersion= 0.18.4 et plus
|SeeAlso=[https   *//github.com/PR-DC/GuiResetToolbars/ Dépôt Github]
}}

## Description

Cette macro réinitialise la position des barres d\'outils.

## Utilisation

Exécutez la macro dans un plan de travail dont la ou les barres d\'outils sont manquantes.

## Script

Icône de la barre d\'outils ![](images/GuiResetToolbars.svg )

**GuiResetToolbars.FCMacro**


{{MacroCode|code=
# Reset Toolbars position
# Author   * Milos Petrasinovic <mpetrasinovic@pr-dc.com>
# PR-DC, Republic of Serbia
# info@pr-dc.com
# 
# 
#
# Copyright (C) 2020 PR-DC <info@pr-dc.com>
# 
# This program is free software   * you can redistribute it and/or modify
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
# along with this program.  If not, see <https   *//www.gnu.org/licenses/>.
#
# 

__Name__ = 'GuiResetToolbars'
__Comment__ = 'Reset Toolbars position'
__Author__ = 'PR-DC'
__Version__ = '1.0.0'
__Date__ = '2020-04-21'
__License__ = 'LGPL-3.0-or-later'
__Web__ = "https   *//github.com/PR-DC/GuiResetToolbars/"
__Wiki__ = 'https   *//wiki.freecadweb.org/Macro_GuiResetToolbars'
__Icon__ = 'GuiResetToolbars.svg'
__Help__ = 'Run the macro within a workbench that has missing toolbar(s)'
__Status__ = 'stable'
__Requires__ = 'Freecad >= 0.18.4'
__Communication__ = 'https   *//github.com/PR-DC/GuiResetToolbars/issues/'
__Files__ = 'GuiResetToolbars.svg'

import FreeCADGui as gui
from PySide import QtGui, QtCore # FreeCAD's special PySide!

mw = gui.getMainWindow()
tb = mw.findChildren(QtGui.QToolBar)
for i in tb   *
    mw.addToolBar(QtCore.Qt.TopToolBarArea, i)
}}

## Liens

Discussion sur le forum de [Reset toolbar position](https   *//forum.freecadweb.org/viewtopic.php?f=3&t=45452&p=390034#p389404)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro GuiResetToolbars/fr
