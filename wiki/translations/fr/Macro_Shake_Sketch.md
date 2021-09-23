# Macro Shake Sketch/fr



{{Macro/fr
|Name=Macro Shake Sketch
|Icon=Macro_Shake_Sketch.png
|Description=Secoue une esquisse pour révéler ses parties non-contraintes {{ColoredText|#ff0000|#ffff00|(But be careful working on a copy of your file because the macro "dismantles all" to display and you may start over).}}
|Author=Gaël Ecorchard
|Version=1.1
|Date=2014-10-31
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/4/4a/Macro_Shake_Sketch.png ToolBar Icon]
}}

## Description

Secoue une esquisse pour révéler ses parties non-contraintes. Entrez en mode édition d\'une esquisse et lancez la macro. Cette macro ajoute un bruit aléatoire dans tous les points de l\'esquisse. Les contraintes de l\'esquisse sont alors résolues, les parties contraintes gardent leur position et les parties libres bougent.

**Mais attention travaillez sur une copie de votre fichier car la macro \"démantèle tout\" pour la visualisation et vous risquez de tout recommencer.**

## Script

Icône de la barre d\'outils ![](images/Macro_Shake_Sketch.png )

**Macro Shake\_Sketch.py**


```python
# -*- coding: utf-8 -*-

# FreeCAD macro to shake a sketch in order to discover its unconstrained parts.
#
# A Gaussian noise is introduced in all sketch points and the sketch is then
# solved.
# Beware that the sketch can look different because some constraints have
# several solutions. In this case, just undo.
#
# This file is released under the MIT License.
# Author: Gaël Ecorchard
# Version:
# - 1.1, 2014-10-31
#     * correct import for Part
# - 1.0, 2014-08, first release.

# Amplitude of the point displacements.
# The standard deviation of the Gaussian noise is the largest sketch dimension
# multiplied by this factor.
displacement_amplitude = 0.1

# End of configuration.

from random import gauss

import FreeCADGui as Gui
from FreeCAD import Base
import Part

# For each sketch geometry type, map a list of points to move.
g_geom_points = {
    Base.Vector: [1],
    Part.Line: [1, 2],  # first point, last point
    Part.Circle: [0, 3],  # curve, center
    Part.ArcOfCircle: [1, 2, 3],  # first point, last point, center
}


class BoundingBox(object):
    xmin = None
    xmax = None
    ymin = None
    ymax = None

    def enlarge_x(self, x):
        if self.xmin is None:
            self.xmin = x
            self.xmax = x
            return
        if self.xmin > x:
            self.xmin = x
            return
        if self.xmax < x:
            self.xmax = x
            return

    def enlarge_y(self, y):
        if self.ymin is None:
            self.ymin = y
            self.ymax = y
            return
        if self.ymin > y:
            self.ymin = y
            return
        if self.ymax < y:
            self.ymax = y
            return

    def enlarge_point(self, point):
        self.enlarge_x(point.x)
        self.enlarge_y(point.y)

    def enlarge_line(self, line):
        self.enlarge_x(line.StartPoint.x)
        self.enlarge_x(line.EndPoint.x)
        self.enlarge_y(line.StartPoint.y)
        self.enlarge_y(line.EndPoint.y)

    def enlarge_circle(self, circle):
        self.enlarge_x(circle.Center.x - circle.Radius)
        self.enlarge_x(circle.Center.x + circle.Radius)
        self.enlarge_y(circle.Center.y - circle.Radius)
        self.enlarge_y(circle.Center.y + circle.Radius)

    def enlarge_arc_of_circle(self, arc):
        # TODO: correctly compute the arc extrema (cf. toShape().BoundBox)
        self.enlarge_x(arc.Center.x)
        self.enlarge_y(arc.Center.y)


def get_sketch_dims(sketch):
    bbox = BoundingBox()
    for geom in sketch.Geometry:
        if isinstance(geom, Base.Vector):
            bbox.enlarge_point(geom)
        elif isinstance(geom, Part.Line):
            bbox.enlarge_line(geom)
        elif isinstance(geom, Part.Circle):
            bbox.enlarge_circle(geom)
        elif isinstance(geom, Part.ArcOfCircle):
            bbox.enlarge_arc_of_circle(geom)
    if (bbox.xmin is not None) and (bbox.ymin is not None):
        return bbox.xmax - bbox.xmin, bbox.ymax - bbox.ymin
    else:
        return 0, 0


def add_noise(point, sigma):
    """Add a Gaussian noise with standard deviation sigma"""
    point.x = gauss(point.x, sigma)
    point.y = gauss(point.y, sigma)


def move_points(sketch, geom_index, sigma):
    point_indexes = g_geom_points[type(sketch.Geometry[i])]
    # Direct access to sketch.Geometry[index] does not work. This would,
    # however prevent repeated recompute.
    for point_index in point_indexes:
        point = sketch.getPoint(geom_index, point_index)
        add_noise(point, sigma)
        sketch.movePoint(geom_index, point_index, point)

view_provider = Gui.activeDocument().getInEdit()

# Don't know how to exit from a macro.
do_move = True
if not view_provider:
    do_move = False

if do_move:
    sketch = view_provider.Object

    if sketch.TypeId != 'Sketcher::SketchObject':
        do_move = False

if do_move:
    sigma = max(get_sketch_dims(sketch)) * displacement_amplitude

    for i in range(len((sketch.Geometry))):
        move_points(sketch, i, sigma)
```




