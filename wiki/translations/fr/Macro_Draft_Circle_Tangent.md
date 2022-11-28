# Macro Draft Circle Tangent/fr
{{Macro/fr
|Name=Macro Draft Circle Tangent
|Description=Crée des tangentes aux Draft cercles.
|Author=heda
|Version=0.1
|Date=2022-11-21
|FCVersion=-
}}

## Description

![](images/Macro_Draft_circle_tangent_example.png ) 
*Macro Draft Circle Tangent*

## Utilisation

Sélectionnez et lancez.

## Installation

Par le biais du [Gestionnaire des extensions](Std_AddonMgr/fr.md).

## Version

v0.1 2022-11-21    * première version

## Code

**Macro_Draft_Circle_Tangent.FCMacro**


{{MacroCode|code=
#!/usr/bin/env python3
# -*- coding   * utf-8 -*-

# ***************************************************************************
# *   Copyright (c) 2022 heda <heda @ freecad forum>                        *
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


__Name__ = 'Draft_circle_tangent'
__Comment__ = 'Makes tangents to draft circles.'
__Author__ = 'heda @ fc-forum'
__Version__ = '0.1'
__Date__ = '2022-11-21'
__License__ = 'LGPL-2.0-or-later'
__Web__ = ''
__Wiki__ = 'https   *//wiki.freecadweb.org/Macro_Draft_circle_tangent'
__Icon__ = ''
__Help__ = 'Select and launch.'
__Status__ = 'functional'
__Requires__ = 'tested on FreeCAD v0.20'
__Communication__ = ''
__Files__ = ''


__doc__ = """
makes tangents for draft circles and arcs
a) circle and vertex/point
b) two circles

select before launching macro

for circle and point the tangents are constructed,
as one would do with pen and paper
for circle and circle the angles are calculated,
one can also construct the tangents in a similar way to
circle/point way, i.e. intersections by additional construction circles

note   * tesselation often makes the true tangent not look like a true tangent
this is to not overload rendering for larger projects
one can change the viewsetting deviation for the circle to minimum (0.01)
if one wants to better view the true tangent, if so, better turn that back
to default once viewed - it is easy to foget that this has been done,
and can in larger projects put fc to more or less a complete halt.
"""

from math import sin, cos, pi, atan2, acos, asin

import Draft

doc = App.ActiveDocument
cgroup = doc.addObject('App   *   *DocumentObjectGroup','Construction')
Vector, Placement = App.Vector, App.Placement
RotZero = Placement().Rotation

def get_curve(obj)   *
    return obj.Shape.Edge1.Curve

def point2vector(pt)   *
    return pt.toShape().Point

def get_intersection_points(obj1, obj2)   *
    doc.recompute()
    i1, i2 = get_curve(obj1).intersect(get_curve(obj2))
    return (point2vector(p) for p in (i1, i2))

def add_construction(obj)   *
    _ = cgroup.addObject(obj)

def mk_line(v1, v2, construction=True)   *
    line = Draft.make_line(v1, v2)
    if construction   *
        line.ViewObject.DrawStyle = 'Dashdot'
        add_construction(line)
    return line

def mk_circle(centre, radius)   *
    circle = Draft.make_circle(radius, Placement(centre, RotZero), False)
    circle.ViewObject.DrawStyle = 'Dashed'
    add_construction(circle)
    return circle


## selection logic
SINGLE = False
msg = ('select exactly 2 items, 2 (draft) circles '
        'or 1 (draft) circle and one vertex or (draft) point')
selection = Gui.Selection.getSelection()
if len(selection) == 2   *
    s1, s2 = selection
    r1, r2 = (hasattr(r, 'Radius') for r in selection)
    if r1 and r2   *
        c1s, c2s = s1, s2
    elif not r1 and not r2   *
        raise RunTimeWarning(msg)
    else   *
        SINGLE = True
        circle = s1 if r1 else s2
        sx1, sx2 = Gui.Selection.getSelectionEx()
        sx = sx2 if r1 else sx1
        point, = sx.PickedPoints
    
else   *
    raise RunTimeWarning(msg)

if SINGLE   *

    o = circle.Placement.Base
    op = point - o

    ccircle = mk_circle(o + op/2, op.Length/2)

    v1, v2 = get_intersection_points(circle, ccircle)

    tangent1 = mk_line(point, v1, False)
    tangent2 = mk_line(point, v2, False)


else   *

    # c1 is the larger one
    if c1s.Radius >= c2s.Radius   *
        c1, c2 = c1s, c2s
    else   *
        c1, c2 = c2s, c1s

    c1c, c2c = c1.Placement.Base, c2.Placement.Base

    centerline = mk_line(c1c, c2c)
    cc = c2c - c1c

    # construction circle outer tangent
    c3 = mk_circle(c1c, c1.Radius - c2.Radius)

    phi1 = atan2(cc.y, cc.x) + acos(c3.Radius / cc.Length)
    v1 = Vector(cos(phi1), sin(phi1), 0).normalize()
    line = mk_line(c1c, v1 * c1.Radius + c1c)
    ot1 = mk_line(c1c + v1 * c1.Radius, c2c + v1 * c2.Radius, False)

    phi2 = atan2(cc.y, cc.x) - acos(c3.Radius / cc.Length)
    v2 = Vector(cos(phi2), sin(phi2), 0).normalize()
    line2 = mk_line(c1c, v2 * c1.Radius + c1c)
    ot2 = mk_line(c1c + v2 * c1.Radius, c2c + v2 * c2.Radius, False)

    # construction circle inner tangent
    c4 = mk_circle(c2c, c1.Radius + c2.Radius)

    phi1 = atan2(cc.y, cc.x) + asin(c4.Radius / cc.Length) - pi/2
    v1 = Vector(cos(phi1), sin(phi1), 0).normalize()
    line = mk_line(c2c, -v1 * c2.Radius + c2c)
    ot1 = mk_line(c1c + v1 * c1.Radius, c2c - v1 * c2.Radius, False)

    phi2 = atan2(cc.y, cc.x) - asin(c4.Radius / cc.Length) + pi/2
    v2 = Vector(cos(phi2), sin(phi2), 0).normalize()
    line2 = mk_line(c2c, - v2 * c2.Radius + c2c)
    ot2 = mk_line(c1c + v2 * c1.Radius, c2c - v2 * c2.Radius, False)

cgroup.ViewObject.Visibility = False
doc.recompute()

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro Draft Circle Tangent/fr
