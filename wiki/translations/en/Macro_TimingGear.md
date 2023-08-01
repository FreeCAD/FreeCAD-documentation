# Macro TimingGear/en
{{Macro
|Name=TimingGear
|Description=This macro creates GT2/GT3/GT5 timing gears.
|Author=eaguirre, galou
|Download=[https://github.com/FreeCAD/FreeCAD-macros/blob/master/ObjectCreation/TimingGear.FCMacro download here]
|Date=2019-12-29
|Version=1.5.0
|FCVersion=0.18.5
}}

## Description

This macro creates GT2/GT3/GT5 timing gears to be used with [timing belts](https://en.wikipedia.org/wiki/Timing_belt_(camshaft)). It uses operations of the [PartDesign Workbench](PartDesign_Workbench.md).

The purpose of timing gears is to allow the camshaft and crankshaft to turn the timing chain. The crankshaft turns to move pistons up and down inside the cylinders. The camshaft turns to allow intake and exhaust valves on the cylinders to open and close. These components are important for proper engine timing.

Timing gears are connected to a timing belt or timing chain.

<img alt="" src=images/TimingGear_usage.png  style="width:600px;"> 
*Above: Example of usage of 2 timing pulleys created with the TimingGear macro. Both pulleys were modified to add more features. The GT2 pulleys drive the Z axis of a 3 axis CNC machine.*

## Usage

+++
| ![](images/Macro_TimingGear_dialog.png ) | 1.  Start the macro in a FreeCAD document. Remember that at the moment of installation you can create a button in the Macros toolbar to start it.                                                                                                                        |
|                                                                | 2.  In the dialog window that opens choose the parameters for the GTx timing gear:                                                                                                                                                                                       |
|                                                                |     -   Select the *type of gear*: GT2/GT3/GT5, every GTx gear has a x mm pitch.                                                                                                                                                                                         |
|                                                                |     -   Specify the *tooth count*, it is the number of teeth for the gear it takes a value between 5 and 360.                                                                                                                                                            |
|                                                                |     -   Specify the *gear height*, the height of the gear in mm.                                                                                                                                                                                                         |
|                                                                |     -   Optionally you can *add a shaft*, this option creates a circular or hexagonal hole in the center of the gear used to insert a shaft, leadscrew or similar part, if it\'s your case select between circle/hexagon and specify the diameter of the bore in mm.     |
|                                                                |     -   Also optionally you can add a *base* disc and a *top* disc, with this option you can create a pair of discs at the inferior and superior faces of the gear, it\'s useful for creating pulleys, if it\'s your case insert the height and the diameter both in mm. |
|                                                                | 3.  Click on the create button and wait for the body to be created.                                                                                                                                                                                                      |
|                                                                | 4.  Once the body is finished you can use the [PartDesign Workbench](PartDesign_Workbench.md) to add features to the gear, for example an extra disc and/or a pair of holes to locate the set screws.                                                            |
+++

## Notes

-   If you need to create a double head GTx pulley you can create 2 pulleys with the same parameters and then join them with a boolean operation.
-   The pitch of the timing belts (distance from tooth center to tooth center of consecutive teeth) is specified in types. GT2 has a pitch of 2 mm, GT3 of 3 mm, GT5 of 5 mm etc..

## Useful formulas 

-    **addendum diameter**= **pitch diameter** + 2 \* **module**

-    **belt length**= 2 \* **axle base** + **belt tooth pitch** : 2 \* **(teeth 1 + 2)** + **belt tooth pitch²** : 4 \* pi² \* **axle base** \* **(teeth 1 - 2)²**

-    **axle base**= **belt length** : 4 - **belt tooth pitch** : 8 \* **(teeth 1+2)** + ¼ \* sqrt \[**belt length** - ½ \* **belt tooth pitch** \* **(teeth 1+2)²** - 2 \* **belt tooth pitch²** \* **(teeth 1+2)²** : pi²\]

## Links

-   Forum thread: [GT2, GT3 and GT5 Timing Gear Creator](https://forum.freecadweb.org/viewtopic.php?f=22&t=35899).
-   You can also create timing gears with the [FCGear TimingGear](FCGear_TimingGear.md) command from the external [FCGear Workbench](FCGear_Workbench.md).

## Script

ToolBar Icon ![](images/TimingGear_icon.png )

**Macro_TimingGear.FCMacro**


{{MacroCode|code=
# -*- coding: utf-8 -*-
"""Macro GT2/GT3/GT5 Timing Gear Creator for FreeCAD."""
#
# 
#                         Copyright (c) 2019 - Emilio Aguirre
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLEFOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# 
# TimingGear.png courtesy of Wikipedia
# (https://en.wikipedia.org/wiki/Key_%28engineering%29).
#
# Changelog
# 
# - v 1.5:
#   - Fix position of base.
# - v 1.4:
#   - Fixing bugs related to size of top and base
#   - Adding code to keep dialog upfront main window (thanks mario52 !)
# - v 1.3:
#   - Adding key for shaft hub
#   - Fixing issue with top
#   - Fixing issue with shaft (now values are in diameter)

__Name__ = 'GT2/GT3/GT5 Timing Gear Creator'
__Comment__ = 'GT2/GT3/GT5 Gear Creator Macro (any gear size from 5 to 360 teeth)'
__Author__ = 'eaguirre,galou'
__Version__ = '1.5.0'
__Date__ = '2019-12-29'
__License__ = 'LGPL-2.0-or-later'
__Web__ = 'http://www.emilioaguirre.com'
__Wiki__ = 'https://wiki.freecadweb.org/Macro_TimingGear'
__Icon__ = 'TimingGear.png'
__Help__ = 'Click on the TimingGear button/macro, and enter the required data in the dialog window.'
__Status__ = ''
__Requires__ = 'FreeCAD ?.??'
__Communication__ = 'info_at_emilioaguirre.com,https://github.com/FreeCAD/FreeCAD-macros/issues://forum.freecadweb.org/viewtopic.php?t=35899'
__Files__ = 'TimingGear.png'

# TODO: Fix segfault when clicking a second time on "Create".

import math

from PySide import QtCore
from PySide import QtGui

import FreeCAD as app
import FreeCADGui as gui
import Part  # From FreeCAD.
import ProfileLib.RegularPolygon  # From FreeCAD.
from FreeCAD import Base

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _tr(context, text, disambig=None):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _tr(context, text, disambig=None):
        return QtGui.QApplication.translate(context, text, disambig)


def _circle_intersect_vline(x, r):
    y = math.sqrt(r*r - x*x)
    return y


def _polar(angle_deg, radius, pt):
    """Convert from polar to Cartesian.

    Convert from polar coordinates (theta, radius) to cartesian
    coordinates. The result is added to the given vector pt
    """
    p = app.Vector(0, 0, 0)
    p[0] = pt[0] + radius * math.cos(math.radians(angle_deg))
    p[1] = pt[1] + radius * math.sin(math.radians(angle_deg))
    return p


def _bisector_vector(v1, v2, m):
    """Get the vector between two vectors."""
    return (v1 + v2).normalize() * m


# 
# QT Window Class
# 
class TimingGearWindow(object):

    def __init__(self, main_window):
        self.with_shaft = True
        self.circular_shaft = True  # Hexagonal if False.
        self.shaft_diameter = 5.0
        self.gear_height = 6.0
        self.base_height = 1.0
        self.base_diameter = 6.37
        self.top_height = 1.0
        self.top_diameter = 6.37
        self.with_base = False
        self.with_top = False
        self.max_shaft_diameter = 100.0
        self.tooth_count = 20
        self.with_key = False
        self.key_b = 2
        self.key_h = 2
        self.t1 = 1.2
        self.t2 = 1

        # UI Definition
        win_width = 300.0
        win_height = 340.0
        self.window = main_window
        main_window.setObjectName(_fromUtf8('GT2/GT3/GT5 Timing Gear'))
        main_window.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        main_window.resize(win_width, win_height)
        self.central_wdgt = QtGui.QWidget(MainWindow)

        # UI Elements
        self.type_lbl = QtGui.QLabel(self.central_wdgt)
        self.type_lbl.setGeometry(QtCore.QRect(win_width*0.05, win_height*0.01, 150, 16))

        self.type_combo = QtGui.QComboBox(self.central_wdgt)
        self.type_combo.addItems(['GT2', 'GT3', 'GT5'])
        self.type_combo.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.01, 95, 20))
        self.type_combo.currentIndexChanged.connect(self._on_gt_type_change)

        self.tooth_count_lbl = QtGui.QLabel(self.central_wdgt)
        self.tooth_count_lbl.setGeometry(QtCore.QRect(win_width*0.05, win_height*0.08, 150, 16))

        self.tooth_count_spin = QtGui.QSpinBox(self.central_wdgt)
        self.tooth_count_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.08, 100, 22))
        self.tooth_count_spin.setMinimum(5)
        self.tooth_count_spin.setMaximum(360)
        self.tooth_count_spin.setSingleStep(1)
        self.tooth_count_spin.setValue(self.tooth_count)
        self.tooth_count_spin.valueChanged.connect(self._on_num_teeth_changed)

        self.range_lbl = QtGui.QLabel(self.central_wdgt)
        self.range_lbl.setGeometry(QtCore.QRect(win_width*0.80, win_height*0.08, 150, 16))

        self.gear_height_lbl = QtGui.QLabel(self.central_wdgt)
        self.gear_height_lbl.setGeometry(QtCore.QRect(win_width*0.05, win_height*0.16, 150, 16))

        self.gear_height_spin = QtGui.QDoubleSpinBox(self.central_wdgt)
        self.gear_height_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.16, 100, 22))
        self.gear_height_spin.setMinimum(0.01)
        self.gear_height_spin.setMaximum(100.0)
        self.gear_height_spin.setSingleStep(0.01)
        self.gear_height_spin.setValue(self.gear_height)
        self.gear_height_spin.valueChanged.connect(self._on_hgearear_valuechanged)

        self.gear_height_mm_lbl = QtGui.QLabel(self.central_wdgt)
        self.gear_height_mm_lbl.setGeometry(QtCore.QRect(win_width*0.80, win_height*0.16, 32, 16))

        # Shaft Information
        self.with_shaft_check = QtGui.QCheckBox('With shaft', self.central_wdgt)
        self.with_shaft_check.setGeometry(QtCore.QRect(win_width*0.05, win_height*0.25, 200, 25))
        self.with_shaft_check.setChecked(self.with_shaft)
        self.with_shaft_check.clicked.connect(self._on_checkShaft_clicked)

        self.shaft_diam_spin = QtGui.QDoubleSpinBox(self.central_wdgt)
        self.shaft_diam_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.25, 100, 22))
        self.shaft_diam_spin.setMinimum(0.01)
        self.shaft_diam_spin.setMaximum(100.0)
        self.shaft_diam_spin.setSingleStep(0.01)
        self.shaft_diam_spin.setValue(self.shaft_diameter)
        self.shaft_diam_spin.valueChanged.connect(self._on_diameter_shaft_valuechanged)

        self.shaft_diam_mm_lbl = QtGui.QLabel(self.central_wdgt)
        self.shaft_diam_mm_lbl.setGeometry(QtCore.QRect(win_width*0.8, win_height*0.25, 32, 16))

        self.circular_shaft_radio = QtGui.QRadioButton('Circle', self.central_wdgt)
        self.circular_shaft_radio.move(win_width*0.25, win_height*0.33)
        self.circular_shaft_radio.setChecked(self.circular_shaft)
        self.circular_shaft_radio.clicked.connect(self._on_radioCircle_clicked)

        self.checkKeyHub = QtGui.QCheckBox('Key hub', self.central_wdgt)
        self.checkKeyHub.setGeometry(QtCore.QRect(win_width*0.55, win_height*0.33, 200, 25))
        self.checkKeyHub.setChecked(self.with_key)
        self.checkKeyHub.clicked.connect(self._on_checkKeyHub_clicked)
        self.checkKeyHub.hide()

        self.hexagonal_shaft_radio = QtGui.QRadioButton('Hexagon', self.central_wdgt)
        self.hexagonal_shaft_radio.move(win_width*0.25, win_height*0.38)
        self.hexagonal_shaft_radio.setChecked(not self.circular_shaft)
        self.hexagonal_shaft_radio.clicked.connect(self._on_radioHex_clicked)

        # Base information
        self.checkBase = QtGui.QCheckBox('Add base', self.central_wdgt)
        self.checkBase.move(win_width*0.05, win_height*0.45)
        self.checkBase.setChecked(self.with_base)
        self.checkBase.clicked.connect(self._on_checkBase_clicked)

        self.base_height_lbl = QtGui.QLabel(self.central_wdgt)
        self.base_height_lbl.setGeometry(QtCore.QRect(win_width*0.4, win_height*0.45, 32, 16))
        self.base_height_lbl.hide()

        self.base_height_spin = QtGui.QDoubleSpinBox(self.central_wdgt)
        self.base_height_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.45, 100, 22))
        self.base_height_spin.setMinimum(0.01)
        self.base_height_spin.setMaximum(100.0)
        self.base_height_spin.setSingleStep(0.5)
        self.base_height_spin.setValue(self.base_height)
        self.base_height_spin.valueChanged.connect(self._on_height_base_valuechanged)
        self.base_height_spin.hide()

        self.base_height_mm_lbl = QtGui.QLabel(self.central_wdgt)
        self.base_height_mm_lbl.setGeometry(QtCore.QRect(win_width*0.8, win_height*0.45, 32, 16))
        self.base_height_mm_lbl.hide()

        self.base_diam_lbl = QtGui.QLabel(self.central_wdgt)
        self.base_diam_lbl.setGeometry(QtCore.QRect(win_width*0.4, win_height*0.54, 32, 16))
        self.base_diam_lbl.hide()

        self.base_diam_spin = QtGui.QDoubleSpinBox(self.central_wdgt)
        self.base_diam_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.54, 100, 22))
        self.base_diam_spin.setMinimum(self.shaft_diameter)
        self.base_diam_spin.setMaximum(500.0)
        self.base_diam_spin.setSingleStep(0.5)
        self.base_diam_spin.setValue(self.base_diameter)
        self.base_diam_spin.valueChanged.connect(self._on_diameter_base_valuechanged)
        self.base_diam_spin.hide()

        self.base_diam_mm_lbl = QtGui.QLabel(self.central_wdgt)
        self.base_diam_mm_lbl.setGeometry(QtCore.QRect(win_width*0.8, win_height*0.54, 32, 16))
        self.base_diam_mm_lbl.hide()

        # Top information
        self.top_check = QtGui.QCheckBox('Add top', self.central_wdgt)
        self.top_check.move(win_width*0.05, win_height*0.63)
        self.top_check.setChecked(self.with_base)
        self.top_check.clicked.connect(self._on_checkTop_clicked)

        self.top_height_lbl = QtGui.QLabel(self.central_wdgt)
        self.top_height_lbl.setGeometry(QtCore.QRect(win_width*0.4, win_height*0.63, 32, 16))
        self.top_height_lbl.hide()

        self.top_height_spin = QtGui.QDoubleSpinBox(self.central_wdgt)
        self.top_height_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.63, 100, 22))
        self.top_height_spin.setMinimum(0.01)
        self.top_height_spin.setMaximum(100.0)
        self.top_height_spin.setSingleStep(0.5)
        self.top_height_spin.setValue(self.base_height)
        self.top_height_spin.valueChanged.connect(self._on_height_top_valuechanged)
        self.top_height_spin.hide()

        self.top_height_mm_lbl = QtGui.QLabel(self.central_wdgt)
        self.top_height_mm_lbl.setGeometry(QtCore.QRect(win_width*0.8, win_height*0.63, 32, 16))
        self.top_height_mm_lbl.hide()

        self.top_diam_lbl = QtGui.QLabel(self.central_wdgt)
        self.top_diam_lbl.setGeometry(QtCore.QRect(win_width*0.4, win_height*0.72, 32, 16))
        self.top_diam_lbl.hide()

        self.top_diam_spin = QtGui.QDoubleSpinBox(self.central_wdgt)
        self.top_diam_spin.setGeometry(QtCore.QRect(win_width*0.45, win_height*0.72, 100, 22))
        self.top_diam_spin.setMinimum(self.shaft_diameter)
        self.top_diam_spin.setMaximum(500.0)
        self.top_diam_spin.setSingleStep(0.5)
        self.top_diam_spin.setValue(self.top_diameter)
        self.top_diam_spin.valueChanged.connect(self._on_diameter_top_valuechanged)
        self.top_diam_spin.hide()

        self.top_diam_mm_lbl = QtGui.QLabel(self.central_wdgt)
        self.top_diam_mm_lbl.setGeometry(QtCore.QRect(win_width*0.8, win_height*0.72, 32, 16))
        self.top_diam_mm_lbl.hide()

        self.create_btn = QtGui.QPushButton(self.central_wdgt)
        self.create_btn.setGeometry(QtCore.QRect(win_width*0.65, win_height*0.81, 80, 28))
        self.create_btn.clicked.connect(self._on_create_clicked)

        self.close_btn = QtGui.QPushButton(self.central_wdgt)
        self.close_btn.setGeometry(QtCore.QRect(win_width*0.2, win_height*0.81, 80, 28))
        self.close_btn.clicked.connect(self._on_close_clicked)

        # Set UI elements to window
        MainWindow.setCentralWidget(self.central_wdgt)

        # Set strings to UI
        self.retranslateUi(MainWindow)

        # 
        #  Key Size Chart Standard Metric Keys/Keyways Engineering
        #  TODO: add a reference
        # 
        self.metric_keys = [
            {'over': 6, 'upto': 8, 'b': 2, 'h': 2, 't1': 1.2, 't2': 1, 'r': 0.08},
            {'over': 8, 'upto': 10, 'b': 3, 'h': 3, 't1': 1.8, 't2': 1.4, 'r': 0.08},
            {'over': 10, 'upto': 12, 'b': 4, 'h': 4, 't1': 2.5, 't2': 1.8, 'r': 0.08},
            {'over': 12, 'upto': 17, 'b': 5, 'h': 5, 't1': 3, 't2': 2.3, 'r': 0.16},
            {'over': 17, 'upto': 22, 'b': 6, 'h': 6, 't1': 3.5, 't2': 2.8, 'r': 0.16},
            {'over': 22, 'upto': 30, 'b': 8, 'h': 7, 't1': 4, 't2': 3.3, 'r': 0.16},
            {'over': 30, 'upto': 38, 'b': 10, 'h': 8, 't1': 5, 't2': 3.3, 'r': 0.25},
            {'over': 38, 'upto': 44, 'b': 12, 'h': 8, 't1': 5, 't2': 3.3, 'r': 0.25},
            {'over': 44, 'upto': 50, 'b': 14, 'h': 9, 't1': 5.5, 't2': 3.8, 'r': 0.25},
            {'over': 50, 'upto': 58, 'b': 16, 'h': 10, 't1': 6, 't2': 4.3, 'r': 0.25},
            {'over': 58, 'upto': 65, 'b': 18, 'h': 11, 't1': 7, 't2': 4.4, 'r': 0.25},
            {'over': 65, 'upto': 75, 'b': 20, 'h': 12, 't1': 7.5, 't2': 4.9, 'r': 0.40},
            {'over': 75, 'upto': 85, 'b': 22, 'h': 14, 't1': 9, 't2': 5.4, 'r': 0.40},
            {'over': 85, 'upto': 95, 'b': 25, 'h': 14, 't1': 9, 't2': 5.4, 'r': 0.40},
            {'over': 95, 'upto': 110, 'b': 28, 'h': 16, 't1': 10, 't2': 6.4, 'r': 0.40},
            {'over': 110, 'upto': 130, 'b': 32, 'h': 18, 't1': 11, 't2': 7.4, 'r': 0.40},
            {'over': 130, 'upto': 150, 'b': 36, 'h': 20, 't1': 12, 't2': 8.4, 'r': 0.70},
            {'over': 150, 'upto': 170, 'b': 40, 'h': 22, 't1': 13, 't2': 9.4, 'r': 0.70},
            {'over': 170, 'upto': 200, 'b': 45, 'h': 25, 't1': 15, 't2': 10.4, 'r': 0.70},
            {'over': 200, 'upto': 230, 'b': 50, 'h': 28, 't1': 17, 't2': 11.4, 'r': 0.70},
        ]

        # 
        # Gear Data
        # pitch - distance between two teeth
        # u     - pitch differential. The radial distance between pitch diameter
        #          and pulley outer diameter is called pitch differential.
        # h     - Tooth height
        # H     - Belt height
        # r0    - Inner circle radius
        # r1    - Side circle radius that define the side of a tooth
        # rs    - Small circle radius that define the corner of a tooth
        # offset- Offset of the side circle center
        # name  - Gear name
        # group - Type of Gear
        # TODO: add a reference
        # 

        # GT2 Gear Data
        self.gt2 = {'pitch': 2.0,
                    'u': 0.254,
                    'h': 0.75,
                    'H': 1.38,
                    'r0': 0.555,
                    'r1': 1.0,
                    'rs': 0.15,
                    'offset': 0.40,
                    'name': 'GT2',
                    'group': 'GT'
                    }
        # GT3 Gear Data
        self.gt3 = {'pitch': 3.0,
                    'u': 0.381,
                    'h': 1.14,
                    'H': 2.40,
                    'r0': 0.85,
                    'r1': 1.52,
                    'rs': 0.25,
                    'offset': 0.61,
                    'name': 'GT3',
                    'group': 'GT'
                    }
        # GT5 Gear Data
        self.gt5 = {'pitch': 5.0,
                    'u': 0.5715,
                    'h': 1.93,
                    'H': 3.81,
                    'r0': 1.44,
                    'r1': 2.57,
                    'rs': 0.416,
                    'offset': 1.03,
                    'name': 'GT5',
                    'group': 'GT'
                    }

    def _gt_tooth(self, step, data):
        """Calculate the coordinates of the GT tooth vertices.

        Calculate the coordinates of the GT tooth vertices (the teeth of the
        gear, not the teeth of the timing belt). This calculates the right size
        of the previous tooth and the left side of the next tooth
        """
        up = app.Vector(0, 0, 1)
        zero = app.Vector(0, 0, 0)

        r = (data['dr0'] - data['h']) + data['r0']
        cm = _polar(step, r - data['r0'], zero)
        pt = _polar(step, data['dr0'], zero)
        ptn = pt.cross(up).normalize()
        ptd = app.Vector(pt).normalize() * -1

        pr = pt + (ptn * data['offset'])
        pl = pt + (ptn * -data['offset'])
        a = data['r1']/2
        b = a * math.sqrt(3)

        cl = pr + (ptn * -b) + (ptd * a)
        cl0 = pr + (ptn * -(data['r1']+data['rs']))
        cl1 = pr + (ptn * -data['r1']) + (ptd * data['rs'])
        ecl = cl0 + (ptd * data['rs'])
        cl2 = ecl + _bisector_vector(cl0 - ecl, cl1 - ecl, data['rs'])
        cl3 = pr + _bisector_vector(cl - pr, cl1 - pr, data['r1'])

        cr = pl + (ptn * b) + (ptd * a)
        cr0 = pl + (ptn * (data['r1']+data['rs']))
        cr1 = pl + (ptn * data['r1']) + (ptd * data['rs'])
        ecr = cr0 + (ptd * data['rs'])
        cr2 = ecr + _bisector_vector(cr0 - ecr, cr1 - ecr, data['rs'])
        cr3 = pl + _bisector_vector(cr - pl, cr1 - pl, data['r1'])
        return [cr0, cr2, cr1, cr1, cr3, cr, cr, cm, cl, cl, cl3, cl1, cl1, cl2, cl0]

    def create_gear(self, sketch_gear, data):
        """Create the geometry of the gear.

        Create the geometry of the gear. Each tooth is a sequence of arcs
        (3 points non coincidental vertices).
        """
        tooth_count = data['tooth_count']
        angle = 360.0 / tooth_count
        gear = []
        for idx in range(tooth_count):
            step = angle * idx
            t = None
            if data['group'] == 'GT':
                t = self._gt_tooth(step, data)
            else:
                raise Exception('Invalid group {}'.format(data['group']))
            if len(gear) > 0:
                sketch_gear.addGeometry(Part.LineSegment(gear[-1], t[0]))
            gear.extend(t)
            for i in range(0, len(t) - 1, 3):
                sketch_gear.addGeometry(Part.ArcOfCircle(t[i], t[i+1], t[i+2]))
        sketch_gear.addGeometry(Part.LineSegment(gear[-1], gear[0]))

    def create_key(self, r, z):
        y2 = r + self.t2
        yb = _circle_intersect_vline(-self.key_b/2, r)
        pt = _polar(90, yb, app.Vector(0, 0, z))
        c1 = _polar(180, self.key_b/2, pt)
        c4 = _polar(0, self.key_b, c1)
        pt = _polar(90, y2, app.Vector(0, 0, z))
        c2 = _polar(180, self.key_b/2, pt)
        c3 = _polar(0, self.key_b, c2)
        c5 = _polar(270, r, app.Vector(0, 0, z))
        return [c1, c2, c3, c4, c5]

    def create(self, data):
        """Create the FreeCAD elements inside a new document."""
        progress_bar = Base.ProgressIndicator()
        progress_bar.start('Creating  gear...', 0)

        doc = app.newDocument(data['name'])
        doc_gui = gui.activeDocument()

        gear = doc.addObject('PartDesign::Body', 'Gear')

        sketch_gear = gear.newObject('Sketcher::SketchObject', 'SketchGear')
        sketch_gear.ViewObject.hide()
        sketch_gear.Support = (gear.Origin.OriginFeatures[3], [''])  # The XY Plane.
        sketch_gear.MapMode = 'FlatFace'
        sketch_gear.AttachmentOffset = app.Placement(
            app.Vector(0, 0, 0),
            app.Rotation(0, 0, 0, 1))

        self.create_gear(sketch_gear, data)

        r = self.shaft_diameter / 2
        if self.with_shaft:
            if self.circular_shaft:
                if self.with_key:
                    c = self.create_key(r, 0)
                    key_lst = []
                    key_lst.append(Part.LineSegment(c[0], c[1]))
                    key_lst.append(Part.LineSegment(c[1], c[2]))
                    key_lst.append(Part.LineSegment(c[2], c[3]))
                    sketch_gear.addGeometry(key_lst, False)
                    sketch_gear.addGeometry(Part.ArcOfCircle(c[3], c[4], c[0]))
                else:
                    sketch_gear.addGeometry(Part.Circle(app.Vector(0, 0, 0),
                                                        app.Vector(0, 0, 1),
                                                        r))
            else:
                ProfileLib.RegularPolygon.makeRegularPolygon(
                    sketch_gear, 6, app.Vector(0, 0, 0),
                    app.Vector(r, 0, 0), False)

        pad = gear.newObject('PartDesign::Pad', 'Pad')
        pad.Profile = sketch_gear
        pad.Length = self.gear_height

        # Add base to the Gear
        if self.with_base:
            sketch_base = gear.newObject('Sketcher::SketchObject', 'SketchBase')
            sketch_base.ViewObject.hide()
            sketch_base.Support = (gear.Origin.OriginFeatures[3], [''])  # The XY Plane.
            sketch_base.MapMode = 'FlatFace'
            sketch_base.AttachmentOffset = app.Placement(
                app.Vector(0, 0, -self.base_height),
                app.Rotation(0, 0, 0, 1))

            sketch_base.addGeometry(Part.Circle(
                app.Vector(0, 0, 0),
                app.Vector(0, 0, 1),
                self.base_diameter))
            if self.with_shaft:
                if self.circular_shaft:
                    if self.with_key:
                        c = self.create_key(r, -self.base_height)
                        key_lst = []
                        key_lst.append(Part.LineSegment(c[0], c[1]))
                        key_lst.append(Part.LineSegment(c[1], c[2]))
                        key_lst.append(Part.LineSegment(c[2], c[3]))
                        sketch_base.addGeometry(key_lst, False)
                        sketch_base.addGeometry(Part.ArcOfCircle(c[3], c[4], c[0]))
                    else:
                        sketch_base.addGeometry(Part.Circle(app.Vector(0, 0, 0),
                                                            app.Vector(0, 0, 1),
                                                            r))
                else:
                    ProfileLib.RegularPolygon.makeRegularPolygon(
                        sketch_base, 6, app.Vector(0, 0, -self.base_height),
                        app.Vector(self.shaft_diameter/2, 0, 0), False)

            pad_base = gear.newObject('PartDesign::Pad', 'PadBase')
            pad_base.Profile = sketch_base
            pad_base.Length = self.base_height

        # Add Top to the Gear
        if self.with_top:
            sketch_top = gear.newObject('Sketcher::SketchObject', 'SketchTop')
            sketch_top.Support = (gear.Origin.OriginFeatures[3], [''])  # The XY Plane.
            sketch_top.MapMode = 'FlatFace'
            sketch_top.AttachmentOffset = app.Placement(
                app.Vector(0, 0, self.gear_height),
                app.Rotation(0, 0, 0, 1))

            sketch_top.addGeometry(Part.Circle(app.Vector(0, 0, 0),
                                               app.Vector(0, 0, 1),
                                               self.top_diameter))
            if self.with_shaft:
                if self.circular_shaft:
                    if self.with_key:
                        c = self.create_key(r, 0)
                        key_lst = []
                        key_lst.append(Part.LineSegment(c[0], c[1]))
                        key_lst.append(Part.LineSegment(c[1], c[2]))
                        key_lst.append(Part.LineSegment(c[2], c[3]))
                        sketch_top.addGeometry(key_lst, False)
                        sketch_top.addGeometry(Part.ArcOfCircle(c[3], c[4], c[0]))
                    else:
                        sketch_top.addGeometry(Part.Circle(
                            app.Vector(0, 0, 0),
                            app.Vector(0, 0, 1),
                            r))
                else:
                    ProfileLib.RegularPolygon.makeRegularPolygon(
                        sketch_top, 6, app.Vector(0, 0, 0),
                        app.Vector(r, 0, 0), False)

            pad_top = gear.newObject('PartDesign::Pad', 'PadTop')
            pad_top.Profile = sketch_top
            pad_top.Length = self.top_height

        doc.recompute()
        gui.SendMsgToActiveView('ViewFit')
        progress_bar.stop()

    def retranslateUi(self, window):
        """Set the UI text."""
        window.setWindowTitle(_tr('TimingGear', 'GT2/GT3/GT5 Gear Creator'))
        self.create_btn.setText(_tr('TimingGear', 'Create'))
        self.close_btn.setText(_tr('TimingGear', 'Close'))
        self.tooth_count_lbl.setText(_tr('TimingGear', 'Tooth count:'))
        self.gear_height_lbl.setText(_tr('TimingGear', 'Gear height:'))
        self.type_lbl.setText(_tr('TimingGear', 'Type of gear:'))
        self.gear_height_mm_lbl.setText(_tr('TimingGear', 'mm'))
        self.shaft_diam_mm_lbl.setText(_tr('TimingGear', 'mm'))
        self.base_height_mm_lbl.setText(_tr('TimingGear', 'mm'))
        self.base_diam_mm_lbl.setText(_tr('TimingGear', 'mm'))
        self.top_height_mm_lbl.setText(_tr('TimingGear', 'mm'))
        self.top_diam_mm_lbl.setText(_tr('TimingGear', 'mm'))
        self.range_lbl.setText(_tr('TimingGear', '(5 ~ 360)'))
        self.with_shaft_check.setText(_tr('TimingGear', 'Add shaft\n(Diameter)'))
        self.hexagonal_shaft_radio.setText(_tr('TimingGear', 'Hexagon'))
        self.base_height_lbl.setText(_tr('TimingGear', 'H:'))
        self.base_diam_lbl.setText(_tr('TimingGear', 'D:'))
        self.top_height_lbl.setText(_tr('TimingGear', 'H:'))
        self.top_diam_lbl.setText(_tr('TimingGear', 'D:'))
        self.checkKeyHub.setText(_tr('TimingGear', 'Add key hub'))

    def _update_max_shaft_diameter(self):
        info = None
        gear_type = str(self.type_combo.currentText())
        if gear_type == 'GT2':
            info = dict(self.gt2)
        elif gear_type == 'GT3':
            info = dict(self.gt3)
        else:
            info = dict(self.gt5)

        self.max_shaft_diameter = ((self.tooth_count * info['pitch']) / math.pi) / 2
        self.shaft_diam_spin.setMaximum(self.max_shaft_diameter)
        self.with_shaft_check.setText(_tr('TimingGear',
                                          'Add shaft\n(max '
                                          + '{0:.2f}'.format(self.max_shaft_diameter)
                                          + ' mm)'))
        self.base_diam_spin.setValue(self.max_shaft_diameter)
        self.top_diam_spin.setValue(self.max_shaft_diameter)

    def update_key_hub(self):
        if self.shaft_diameter < 6:
            self.with_key = False
            return

        found = False
        for k in self.metric_keys:
            if k['over'] <= self.shaft_diameter < k['upto']:
                self.key_b = k['b']
                self.key_h = k['h']
                self.t1 = k['t1']
                self.t2 = k['t2']
                self.checkKeyHub.setText(_tr('TimingGear',
                                                'Add key hub\n(b: {} h: {})'.format(
                                                    self.key_b, self.key_h)))
                found = True
                break

        if not found:
            msg = 'Could not find valid key values for shaft radius: {}'.format(shaft_diameter)
            self._error_dialog(msg)
            self.with_key = False
            self.checkKeyHub.setText(_tr('TimingGear', 'Add key hub'))

    # 
    #         UI widgets callbacks
    # 
    def _on_gt_type_change(self, idx):
        # app.Console.PrintMessage('Current index %d selection changed %s\n' % (idx,self.type_combo.currentText()))
        self._update_max_shaft_diameter()

    def _on_num_teeth_changed(self, value):
        # app.Console.PrintMessage('%s Number of Teeths\n' % value)
        self.tooth_count = value
        self._update_max_shaft_diameter()

    def _error_dialog(self, msg):
        diag = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                                 'Error in macro TimingGear',
                                 msg)
        diag.setWindowModality(QtCore.Qt.ApplicationModal)
        diag.exec_()

    def _on_create_clicked(self):
        if 5 <= self.tooth_count <= 360:
            gear_type = str(self.type_combo.currentText())
            app.Console.PrintMessage('Creating Gear {}\n'.format(gear_type))
            if gear_type == 'GT2':
                data = dict(self.gt2)
            elif gear_type == 'GT3':
                data = dict(self.gt3)
            else:
                data = dict(self.gt5)
            data['tooth_count'] = self.tooth_count
            data['d'] = (data['tooth_count'] * data['pitch']) / math.pi
            data['d0'] = data['d'] - (2 * data['u'])
            data['dr0'] = data['d0'] / 2
            app.Console.PrintMessage('pitch {}\n'.format(data['pitch']))
            app.Console.PrintMessage('tooth_count {}\n'.format(data['tooth_count']))
            app.Console.PrintMessage('u {}\n'.format(data['u']))
            app.Console.PrintMessage('d {}\n'.format(data['d']))
            app.Console.PrintMessage('d0 {}\n'.format(data['d0']))
            app.Console.PrintMessage('dr0 {}\n'.format(data['dr0']))
            self.create(data)
        else:
            msg = 'The number of teeth should be between 5 and 360!'
            self._error_dialog(msg)

    def _on_close_clicked(self):
        # app.Console.PrintMessage('Exit Gear Generator\n')
        self.window.close()

    def _on_hgearear_valuechanged(self, value):
        # app.Console.PrintMessage(str(value)+ ' height gear\n')
        self.gear_height = value

    def _on_radioCircle_clicked(self):
        self.circular_shaft = True
        if self.shaft_diameter >= 6 and self.circular_shaft:
            self.checkKeyHub.show()
            self.update_key_hub()

    def _on_radioHex_clicked(self):
        self.circular_shaft = False
        self.checkKeyHub.setChecked(False)
        self.checkKeyHub.hide()

    def _on_diameter_shaft_valuechanged(self, value):
        # app.Console.PrintMessage(str(value) + ' Shaft radius\n')
        if value <= self.max_shaft_diameter:
            self.shaft_diameter = value
            self.base_diam_spin.setMinimum(self.shaft_diameter)
            if self.base_diameter < self.shaft_diameter:
                self.base_diameter = self.shaft_diameter

            self.top_diam_spin.setMinimum(self.shaft_diameter)
            if self.top_diameter < self.shaft_diameter:
                self.top_diameter = self.shaft_diameter

            if self.shaft_diameter >= 6 and self.circular_shaft:
                self.checkKeyHub.show()
                self.update_key_hub()
            else:
                self.checkKeyHub.hide()
        else:
            self.shaft_diameter = self.max_shaft_diameter
            msg = 'The shaft radius should be less than: {}'.format(
                self.max_shaft_diameter)
            self._error_dialog(msg)

    def _on_height_base_valuechanged(self, value):
        # app.Console.PrintMessage(str(value) + ' Height base\n')
        self.base_height = value

    def _on_diameter_base_valuechanged(self, value):
        # app.Console.PrintMessage(str(value) + ' Radius base\n')
        self.base_diameter = value

    def _on_height_top_valuechanged(self, value):
        # app.Console.PrintMessage(str(value) + ' Height top\n')
        self.top_height = value

    def _on_diameter_top_valuechanged(self, value):
        # app.Console.PrintMessage(str(value) + ' Radius top\n')
        self.top_diameter = value

    def _on_checkShaft_clicked(self):
        self.with_shaft = not self.with_shaft
        if self.with_shaft:
            self.circular_shaft_radio.show()
            self.hexagonal_shaft_radio.show()
            self.shaft_diam_spin.show()
            self.shaft_diam_mm_lbl.show()
            if self.shaft_diameter >= 6 and self.circular_shaft:
                self.checkKeyHub.show()
        else:
            self.circular_shaft_radio.hide()
            self.hexagonal_shaft_radio.hide()
            self.shaft_diam_spin.hide()
            self.shaft_diam_mm_lbl.hide()
            self.checkKeyHub.setChecked(False)
            self.checkKeyHub.hide()

    def _on_checkKeyHub_clicked(self):
        self.with_key = not self.with_key
        if self.with_key:
            self.update_key_hub()

    def _on_checkBase_clicked(self):
        self.with_base = not self.with_base
        if self.with_base:
            self.base_height_spin.show()
            self.base_diam_spin.show()
            self.base_height_lbl.show()
            self.base_diam_lbl.show()
            self.base_height_mm_lbl.show()
            self.base_diam_mm_lbl.show()
        else:
            self.base_height_spin.hide()
            self.base_diam_spin.hide()
            self.base_height_lbl.hide()
            self.base_diam_lbl.hide()
            self.base_height_mm_lbl.hide()
            self.base_diam_mm_lbl.hide()

    def _on_checkTop_clicked(self):
        self.with_top = not self.with_top
        if self.with_top:
            self.top_height_spin.show()
            self.top_diam_spin.show()
            self.top_height_lbl.show()
            self.top_diam_lbl.show()
            self.top_height_mm_lbl.show()
            self.top_diam_mm_lbl.show()
        else:
            self.top_height_spin.hide()
            self.top_diam_spin.hide()
            self.top_height_lbl.hide()
            self.top_diam_lbl.hide()
            self.top_height_mm_lbl.hide()
            self.top_diam_mm_lbl.hide()


# 
# Create and display the main window
# 
MainWindow = QtGui.QMainWindow()
ui = TimingGearWindow(MainWindow)
MainWindow.show()
}}



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro TimingGear/en
