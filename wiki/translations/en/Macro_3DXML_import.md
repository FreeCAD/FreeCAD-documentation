# Macro 3DXML import/en
{{Macro
|Name=3DXML_import
|Description=Imports a 3DXML-ascii file to FreeCAD.
|Author=heda
|Version=0.1
|Date=2021-10-03
|FCVersion=-
}}

## Description

This macro imports a 3DXML-ascii file, with options to include edges and/or meshes. There are more types of 3DXML files than the ascii-type, other types cannot be imported with this macro.

The macro has only been tested on one file, the implemented features are limited to what was available in that file. If more test files are made available, the macro possibly could be expanded to cover additional features. Anyone is free to modify and improve the macro, best done by modifying it here on the Wiki. Further info in the {{Incode|docstring}} of the macro.

## Usage

Run macro and select a file.

## Install

Through Addon manager.

## Link

Forum: No dedicated thread, but sprung out of [forum post](https://forum.freecadweb.org/viewtopic.php?f=8&t=28199).

## Version

v0.1 2021-10-03 : first release

## Code

**Macro\_3DXML\_import.FCMacro**


{{MacroCode|code=
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ***************************************************************************
# *   Copyright (c) 2021 heda <heda @ freecad forum>                                      *
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


__Name__ = '3DXML_import'
__Comment__ = 'Imports a 3DXML-ascii file to FreeCAD'
__Author__ = 'heda @ fc-forum'
__Version__ = '0.1'
__Date__ = '2021-10-03'
__License__ = 'LGPL-2.0-or-later'
__Web__ = ''
__Wiki__ = 'https://wiki.freecadweb.org/Macro_3DXML_import'
__Icon__ = ''
__Help__ = 'Launch macro and select file.'
__Status__ = 'Stable'
__Requires__ = 'tested on FreeCAD v0.19'
__Communication__ = 'forum'
__Files__ = ''


__doc__ = """
The 3DXML file format allows for multiple types of representations.
This macro is limited to human readable content in the files,
i.e. the ascii tesselated type of geometry definition.
This type of geometry definition includes polylines as edges of geometry,
and meshes (like stl files).

The macro in current state requires a readable xml-file of type ".3DRep".

Import of edges is by default off, since that is the operation taking the
longest time.

It is recommended to run a mesh analysis after import to for example
remove duplicate points or correct flipped normals.

This macro is created using only one reference file (with only "strips" as
facets), thus it's applicability on other .3DRep files is currently unknown.
If other test files are made available, the macro can be updated.
"""

import FreeCAD as App
import Part, Mesh
from PySide import QtGui
import xml.etree.ElementTree as ET

IMPORT_EDGES, MERGE_EDGES = False, False
IMPORT_MESHES, MERGE_MESHES = True, True

filename, filt = QtGui.QFileDialog.getOpenFileName(filter='*.3DRep')

if not filename:
    raise UserWarning('Need to select a 3DRep file.')

print('Importing: {}'.format(filename))
doc = App.ActiveDocument

tree = ET.parse(filename)
root = tree.getroot()

# get namespaces from xml
ns = dict([node for _, node in
           ET.iterparse(filename, events=['start-ns'])])
if ns.get('') != 'http://www.3ds.com/xsd/3DXML':
    raise UserWarning('did not find expected namespace, file malformed?')
ns.update({'3dx':ns.get('')})


def parse_verts(vertbuffer):
    def floatify(xyz):
        return tuple((float(i) for i in xyz.split()))
    return [floatify(v) for v in vertbuffer.split(',')]

def parse_strips(strips):
    return (tuple(int(i) for i in strip.split())
            for strip in strips.split(','))

def make_mesh(element):
    Faces, VertexBuffer, SurfaceAttributes = list(element)
    Color = Faces.find('.//3dx:Color', ns)
    RGBA = tuple((float(i) for i in tuple(Color.attrib.values())[1:]))
    Face = Faces.find('.//3dx:Face', ns)
    strips = Face.get('strips')
    facets = list()
    if strips:
        Positions, Normals = list(VertexBuffer)
        facetverts = fv = parse_verts(Positions.text)
        for strip in parse_strips(strips):
            facetidx = zip(strip, strip[1:], strip[2:])
            facets += [tuple(fv[i] for i in pidx) for pidx in facetidx]
    else:
        print('face type undefined')
    return Mesh.Mesh(facets), RGBA


for BagRepType in root.findall('3dx:Root/3dx:Rep', ns):
    edges, meshes = list(), list()
    for PolygonalRepType in BagRepType:
        if PolygonalRepType.find('./3dx:Edges', ns):
            if not IMPORT_EDGES:
                continue
            Edges = PolygonalRepType.find('./3dx:Edges', ns)
            for polyline in Edges.findall('./3dx:Polyline', ns):
                verts = parse_verts(polyline.get('vertices'))
                edges.append(Part.makePolygon(verts))
                
        elif PolygonalRepType.find('./3dx:Faces', ns):
            print('  found face element')
            if not IMPORT_MESHES:
                continue
            mesh = make_mesh(PolygonalRepType)
            meshes.append(mesh)

    if edges:
        print('  creating edges')
        edgegroup = doc.addObject('App::DocumentObjectGroup','Edges')
        wires = list()
        if MERGE_EDGES:
            _edges = list()
            for _edge in edges:
                _edges += _edge.Edges
            for swire in Part.sortEdges(_edges):
                wire = Part.Wire(swire)
                obj = doc.addObject('Part::Feature', 'Edge')
                obj.Shape = wire
                wires.append(obj)
        else:
            for edge in edges:
                obj = doc.addObject('Part::Feature', 'Edge')
                obj.Shape = edge
                wires.append(obj)
        edgegroup.addObjects(wires)

    if meshes:
        print('  creating meshes')
        meshgroup = doc.addObject('App::DocumentObjectGroup','Meshes')
        meshobjs = list()
        if MERGE_MESHES:
            mesh_assembled = Mesh.Mesh()
            for mesh, RGBA in meshes:
                mesh_assembled.addMesh(mesh)
            obj = doc.addObject('Mesh::Feature', 'Mesh')
            obj.Mesh = mesh_assembled
            obj.ViewObject.ShapeColor = RGBA
            meshobjs.append(obj)
        else:
            for mesh, RGBA in meshes:
                obj = doc.addObject('Mesh::Feature', 'Mesh')
                obj.Mesh = mesh
                obj.ViewObject.ShapeColor = RGBA
                meshobjs.append(obj)
        meshgroup.addObjects(meshobjs)

doc.recompute()
print('... completed import')

# end
}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Macro 3DXML import/en
