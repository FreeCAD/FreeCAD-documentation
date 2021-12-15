# Macro Shake Sketch/fr
{{Macro/fr
|Name=Macro Shake Sketch
|Icon=Macro_Shake_Sketch.png
|Description=Secoue une esquisse afin de découvrir ses parties non contraintes. Entrez en mode édition pour une esquisse et lancez la macro. La macro ajoute un bruit aléatoire sur tous les points de l'esquisse. L'esquisse est ensuite résolue, les parties contraintes conservent leur position, les parties libres se déplacent {{ColoredText|#ff0000|#ffff00|(Mais faites attention en travaillant sur une copie de votre fichier car la macro "démonte tout" pour afficher et vous devrez recommencer).}} Installation par le gestionnaire d'addons ne fonctionne pas, voir la page wiki macro pour les instructions.
|Author=Gaël Ecorchard, heda
|Version=1.2
|Date=2021-10-22
|FCVersion=Toutes
|Download=[https://www.freecadweb.org/wiki/images/4/4a/Macro_Shake_Sketch.png Icône de la barre d'outils]
}}

## Description

Secoue une esquisse pour révéler ses parties non-contraintes. Entrez en mode édition d\'une esquisse et lancez la macro. Cette macro ajoute un bruit aléatoire dans tous les points de l\'esquisse. Les contraintes de l\'esquisse sont alors résolues, les parties contraintes gardent leur position et les parties libres bougent.

**Mais attention travaillez sur une copie de votre fichier car la macro \"démantèle tout\" pour la visualisation et vous risquez de tout recommencer.**

## Installation

Visible dans le gestionnaire d\'addons, mais l\'installation ne fonctionne pas. Pour le moment, la seule option est d\'installer manuellement, mais vous devez prendre le code de \"view source\" de ce wiki. Le code complet est là, mais il ne s\'affiche pas sur le wiki.

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
# Author: Gaël Ecorchard v1.0 & v1.1
# Author: heda v1.2
# Version:
# - 1.2: 2021-10-22
#       * made macro runnable for current versions of fc
#       * added Part.LineSegment
#       * added start info & result dialogue
#       * hides constraints during shake
#       * added simple debug printing
# - 1.1: 2014-10-31
#       * correct import for Part
# - 1.0: 2014-08
#       * first release

# Amplitude of the point displacements.
# The standard deviation of the Gaussian noise is the largest sketch dimension
# multiplied by this factor.
__version__ = '1.2'
displacement_amplitude = 0.1
debug_print = False
title = 'Sketch Shaker Macro (ver: {})'.format(__version__)

# End of configuration.

from random import gauss

from PySide.QtGui import QMessageBox

import FreeCADGui as Gui
from FreeCAD import Base
import Part

print('Running {}'.format(title))

# For each sketch geometry type, map a list of points to move.
g_geom_points = {
    Base.Vector: [1],
    Part.Line: [1, 2],  # first point, last point
    Part.LineSegment: [1, 2],  # first point, last point
    Part.Circle: [0, 3],  # curve, center
    Part.ArcOfCircle: [1, 2, 3],  # first point, last point, center
} # moves bsplines and conics via lines and circles, no op for Part.Points


def dprint(msg, *args):
    if debug_print:
        if args:
            print(msg.format(*args))
        else:
            print(msg)

class BoundingBox:
    xmin = xmax = ymin = ymax = None

    def enlarge_x(self, x):
        if self.xmin is None:
            self.xmin = self.xmax = x
        elif self.xmin > x:
            self.xmin = x
        elif self.xmax < x:
            self.xmax = x

    def enlarge_y(self, y):
        if self.ymin is None:
            self.ymin = self.ymax = y
        elif self.ymin > y:
            self.ymin = y
        elif self.ymax < y:
            self.ymax = y

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
        elif isinstance(geom, (Part.Line, Part.LineSegment)):
            bbox.enlarge_line(geom)
        elif isinstance(geom, Part.Circle):
            bbox.enlarge_circle(geom)
        elif isinstance(geom, Part.ArcOfCircle):
            bbox.enlarge_arc_of_circle(geom)
    if None in (bbox.xmin, bbox.ymin):
        dprint('sketch bbox not found')
        return 0, 0
    else:
        dprint('sketch bbox found')
        return bbox.xmax - bbox.xmin, bbox.ymax - bbox.ymin


def add_noise(point, sigma):
    """Add a Gaussian noise with standard deviation sigma"""
    dprint('  x0:{:>9.3f}  y0:{:>9.3f}', point.x, point.y)
    point.x = gauss(point.x, sigma)
    point.y = gauss(point.y, sigma)
    dprint('  xt:{:>9.3f}  yt:{:>9.3f}', point.x, point.y)


def move_points(sketch, geom_index, sigma):
    point_indexes = g_geom_points.get(type(sketch.Geometry[i]), [])
    # Direct access to sketch.Geometry[index] does not work. This would,
    # however prevent repeated recompute.
    # not checked validity of comment for v1.2
    moved = False
    for point_index in point_indexes:
        dprint('---- geo idx [{:>3} ] -- pt idx [{:>3} ] ----',
               geom_index, point_index)
        point = sketch.getPoint(geom_index, point_index)
        add_noise(point, sigma)
        try:
            sketch.movePoint(geom_index, point_index, point)
        except ValueError as e:
            dprint(repr(e))
        new_pos = sketch.getPoint(geom_index, point_index)
        test = point.isEqual(new_pos, 0)
        dprint('  did it move? {}', test)
        if test: moved = True
    return moved

def toggle_constraints(sketch, toggle):
    for cid in toggle:
        sketch.toggleVirtualSpace(cid)
    

view_provider = Gui.activeDocument().getInEdit()

shake_it = False
if not view_provider:
    msg = 'A sketch needs to be in edit to be shaken.'
    print(msg)
    _ = QMessageBox.information(None, title, msg)
else:
    sketch = view_provider.Object
    if sketch.TypeId == 'Sketcher::SketchObject':
        sketch.recompute() # ensure update
        to_virtual = [cid for cid, cts in enumerate(sketch.Constraints)
                      if cts.InVirtualSpace]
        sketch_span = get_sketch_dims(sketch)
        sigma = max(sketch_span) * displacement_amplitude
        dprint('sketch span: dx:{:>9.3f} dy:{:>9.3f}', *sketch_span)
        dprint('sigma for gauss-dist: {:.3f}', sigma)
        toggle_constraints(sketch, to_virtual)
        msg = ('Shake sketch will deform the loose parts of the sketch.\n'
               'The deformation cannot be undone.\n'
               'If that is not desired, click Cancel,\n'
               'and run the macro on a copy of the sketch.\n\n'
               'Visibility of constraints has been toggled.\n'
               'Visibility of constraints is restored'
               ' after shaking the sketch.')
        reply = QMessageBox.information(None, title, msg,
                                        QMessageBox.Ok | QMessageBox.Cancel,
                                        QMessageBox.Ok)
        shake_it = reply == QMessageBox.Ok
        
        if not shake_it:
            toggle_constraints(sketch, to_virtual)

if shake_it:
    nbr_moves = 0
    for i in range(sketch.GeometryCount):
        did_move = move_points(sketch, i, sigma)
        if did_move:
            nbr_moves += 1

    msg = 'Did {} moves. Sketch has a total of {} geometry entities.\n\n'
    msg = msg.format(nbr_moves, sketch.GeometryCount)
    open_verts = sketch.OpenVertices
    if open_verts:
        if len(open_verts) == 1:
            ov, form = 'one', 'vertex'
        else:
            ov, form = len(open_verts), 'vertices'
        msg += 'Sketch has {} open {}.'.format(ov, form)
        msg += ('\nA sketch with open vertices'
                ' cannot be used to create a solid.')
    else:
        msg += 'Sketch is free from open vertices.'

    msg += ('\n\nMenu: "Sketch/Validate Sketch..." can be used\n'
            'for additional info about sketch status.')_ = QMessageBox.information(None, title, msg)
    toggle_constraints(sketch, to_virtual)
        
print('Macro finished.')
```

---
[documentation index](../README.md) > Macro Shake Sketch/fr
