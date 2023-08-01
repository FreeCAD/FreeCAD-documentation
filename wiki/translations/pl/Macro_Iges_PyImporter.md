# Macro Iges PyImporter/pl
{{Macro
|Name=Iges_PyImporter
|Description=Imports an IGES file with entity 128 into FreeCAD.
|Author=heda
|Version=0.2
|Date=2022-03-26
|FCVersion=any
}}

## Description

Standalone import for ascii iges-files with bspline surfaces, entity 128, for example created with FreeShip, which appears to always be incorrectly handled by [OCC](OpenCASCADE.md).

Further info can be found in the {{Incode|docstring}} of the macro.

The macro can be expanded to cover additional entities. Anyone is free to extend, modify and improve the macro, best done by changing it here on the Wiki.

## Usage

Run the macro and select an IGES file.

Options:

-   make shell
-   apply color
-   progress bar

## Install

Through Addon manager.

## Link

Forum: There is no dedicated thread, but this macro has sprung out of this [forum post](https://forum.freecad.org/viewtopic.php?p=582137&sid=3a86de4d61ef810a81861c757e15129c#p582137).

## Version

v0.2 2022-03-26 : first release

## Code

**Macro_Iges_PyImporter.FCMacro**


{{MacroCode|code=
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ***************************************************************************
# *   Copyright (c) 2022 heda <heda @ freecad forum>                        *
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENSE text file.                                 *
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


__Name__ = 'Iges_PyImporter'
__Comment__ = 'Imports an iges file with entity 128 to FreeCAD'
__Author__ = 'heda @ fc-forum'
__Version__ = '0.2'
__Date__ = '2022-03-26'
__License__ = 'LGPL-2.0-or-later'
__Web__ = ''
__Wiki__ = 'https://wiki.freecad.org/Macro_Iges_PyImporter'
__Icon__ = ''
__Help__ = 'Launch macro and select file.'
__Status__ = 'works'
__Requires__ = 'tested on FreeCAD v0.19'
__Communication__ = 'forum'
__Files__ = ''



__doc__ = """
Standalone import for ascii iges-files with bspline surfaces,
entity 128, which appears to always be incorrectly handled by occ.

options:
- make shell [default on] or individual surfaces
  if off, the making of shell is enforced for files with more than 50 surfaces
- apply color [default on] if color is present in the iges-file,
  the parser naivly takes the first and ignores any following color records
- progress bar [default on] see note.

Run macro and select the iges file.
Creation of the surfaces can take a while.
Import is to current document if available, else a new is created.

There are no error or consistency checks, the parser either works or fails.
The only parsed entity is 128 - rational bspline surface,
assumed to be freeform. Parsing ability could be expanded,
specification used is iges5.3.

The importer is tested on:
- one freeship file
- one libIGES file

v0.1 - first version - handled iges files created by freeship.
v0.2 - also handles files made with libIGES (on gh).

note: if the macro has an error, the use of the progress bar makes fc
      freezes in monumental ways, the application has to be killed
      with system commands. If so, switch off the progress bar.
"""


import FreeCAD as App
import FreeCADGui as Gui
import Part
from PySide import QtGui

import re
from pathlib import Path
from collections import namedtuple, Counter

### options
MakeShell = True
ShellLimit = 50
ApplyColor = True
ProgressBar = True

filename, filt = QtGui.QFileDialog.getOpenFileName(filter='*.igs')

if not filename:
    raise UserWarning('Need to select an iges file.')

print('Importing: {}'.format(filename))

class Ticker:
    """better than nothing, does not always show though"""
    tick_count = 0
    pbon = ProgressBar
    if pbon:
        pb = App.Base.ProgressIndicator() 
        pb.start('importing iges', 100)def tick(self, ticks=1):
        if self.pbon:
            for i in range(ticks):
                self.pb.next()
                self.tick_count += 1

    def tick_time(self, prog):
        if isinstance(self.tick_step, int):
            self.tick(self.tick_step)
        else:
            if prog in self.tick_step:
                self.tick()def set_tick_step(self, number):
        self.tot_number = number
        span = 100 - 3 * 4
        if number >= span:
            self.tick_step = tuple(range(0, number, int(number / span) + 1))
        else:
            self.tick_step = int(span / number)
        
    def end(self):
        if self.pbon:
            for i in range(101 - self.tick_count):
                self.tick()
            self.pb.stop()


ticker = Ticker()


iges = Path(filename)
data = iges.read_text().splitlines()

sec_def = re.compile('\W+')
sections = dict(S='', G='', D=list(), P=dict())
DES = namedtuple('DES', 'entity linecount label')
oddeven = color = None

for i, line in enumerate(data):
    sec_col = line[72:]
    section, snbr = sec_def.split(sec_col)
    if section in 'SG':
        sections[section] += line[:72]
    elif section == 'D':
        if oddeven is None:
            oddeven = bool(i % 2)
        if isinstance(oddeven, bool):
            if bool(i % 2) == oddeven:
                row1 = [line[j:j+8] for j in range(0, 80, 8)]
                row2 = [data[i+1][j:j+8] for j in range(0, 80, 8)]
                entitydef = (int(row1[0]), int(row2[3]), row2[-3])
                sections['D'].append(DES(*entitydef))
    elif section == 'P':
        break

lc = i

### header
fields = ' '.join(('f{}'.format(i+1) for i in range(25)))
for oldnew in (('f6 preprocessor', 'f14 unitsflag', 'f23 version')):
    fields = fields.replace(*oldnew.split())
Header = namedtuple('Header', fields)
cheat = sections.get('G').split(',')
cheat[0] += ',' # assume that the parameter delimiter is a comma
if len(cheat) == 26:
    cheat.pop(1) # the freeship file

header = Header(*cheat)

### unit
Units = dict(u1=(25.4, 'inch'),
             u2=(1, 'mm'),
             u3=(1, 'user defined, skip'),
             u4=(25.4 * 12, 'feet'),
             u5=(1, 'miles, skipping'),
             u6=(1000, 'meters'),
             u7=(10000, 'kilometers'),
             u8=(25.4 / 1000, 'milli inch'),
             u9=(1, 'micron, skipping'),
             u10=(10, 'centimeters'),
             u11=(1, 'micro inches, skipping'),
             )

unit, unitname = Units.get('u{}'.format(header.unitsflag))
msg = 'file units: {} / preprocessor: {}'
print(msg.format(unitname, header.preprocessor))

ticker.tick(3)

### color
# naive assumtion that color is first entry
msg = 'color definition found in file'
if 314 in set((desi.entity for desi in sections['D'])):
    des = sections['D'].pop(0)
    code, *rgb, _ = data[lc].split(';')[0].split(',')
    color = tuple(float(c) / 100 for c in (rgb)) + (0.,)
    lc += des.linecount
    print(msg)
else:
    print('no ' + msg)

ticker.tick(3)

entities, skipped = list(), list()
for des in sections['D']:
    if des.entity == 128:
        chunk = ''
        for line in data[lc:lc+des.linecount]:
            chunk += line[:64].strip()
        entities.append(chunk.strip()[:-1])
    else:
        skipped.append(des.entity)
    lc += des.linecount

print('found {} surfaces'.format(len(entities)))
if skipped:
    for entity, count in Counter(skipped).items():
        print('skipped {} records of entity {}'.format(count, entity))
else:
    print('no records skipped during parsing')
print('creating surfaces...')

Gui.updateGui() # flushes prints
ticker.tick(3)
ticker.set_tick_step(len(entities))

MakeShell = MakeShell if len(entities) < ShellLimit + 1 else True
doc = App.ActiveDocument if App.ActiveDocument else App.newDocument(iges.stem)

surfs = list()

### parse iges record and create fc surface
for j, entity in enumerate(entities):
    entity = entity.split(',')
    entity[:10] = [int(i) for i in entity[:10]]
    entity[10:] = [float(i) for i in entity[10:]]
    K1, K2, M1, M2, P1, P2, P3, P4, P5 = entity[1:10]
    N1 = 1 + K1 - M1
    N2 = 1 + K2 - M2
    A = N1 + 2 * M1
    B = N2 + 2 * M2
    C = (1 + K1) * (1 + K2)
    # matrix is K1 + 1 x K2 + 1; u,vuknots = entity[10:10+A+1]
    vknots = entity[11+A:11+A+B+1]
    weights = entity[12+A+B:11+A+B+C+1]
    poles = entity[12+A+B+C:11+A+B+4*C+1]if P3 == 0: # rational
        u0, u1, v0, v1 = entity[12+A+B+4*C:15+A+B+4*C+1]
    else: # polynomial
        passumults = [uknots.count(kn) for kn in sorted(set(uknots))]
    vmults = [vknots.count(kn) for kn in sorted(set(vknots))]if P3 == 0:
        pass
    else:
        uknots = uknots[M1:-M1]
        vknots = vknots[M2:-M2]poles = [App.Vector(*pt) * unit
             for pt in zip(poles[0::3], poles[1::3],poles[2::3])]poles = [poles[i:i+K1+1] for i in range(0, len(poles), K1+1)]
    weights = [weights[i:i+K1+1] for i in range(0, len(weights), K1+1)]
    poles = list(zip(*poles))
    weights = list(zip(*weights))bsurface = Part.BSplineSurface()
    builder = bsurface.buildFromPolesMultsKnots
    builder(poles, umults, vmults, uknots, vknots,
            bool(P4), bool(P5), M1, M2, weights)if MakeShell:
        surfs.append(bsurface.toShape())
    else:
       Part.show(bsurface.toShape(), 'Surface')
       if color and ApplyColor:
           doc.ActiveObject.ViewObject.ShapeColor = color

    ticker.tick_time(j)
    

if MakeShell:
    shell = Part.makeShell(surfs)
    Part.show(shell, iges.stem)
    if color and ApplyColor:
        doc.ActiveObject.ViewObject.ShapeColor = color
    doc.ActiveObject.ViewObject.DisplayMode = 'Shaded'

ticker.tick(3)

doc.recompute()
av = Gui.ActiveDocument.ActiveView
av.viewIsometric()
av.fitAll()
print('... import iges completed')
ticker.end()

# end
}}



---
⏵ [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > Macro Iges PyImporter/pl
