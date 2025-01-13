# Macro Convert 021
{{Macro
|Name=Convert_021
|Description=Converts a FreeCAD file saved with a post-0.21 version back to 0.21 format.
|Author=yorik
|Version=0.1
|Date=2024-03-13
|FCVersion=any
}}

## Description

This macro opens a file dialog to allow to choose a FreeCAD file and converts it to 0.21 format (replace AttachmentSupport property to Support). A new file with extension .021.FCStd is created so the original file is not modified.

## Usage

Run the macro and select a FCStd file when the dialog pops up.

## Install

Through Addon manager.

## Code

 **Macro_Convert_021.FCMacro**

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    # ***************************************************************************
    # *                                                                         *
    # *   Copyright (c) 2024 Yorik van Havre <yorik@uncreated.net>              *
    # *                      Florian Foinant-Willig <ffw@2f2v.fr>               *
    # *                                                                         *
    # *   This program is free software; you can redistribute it and/or modify  *
    # *   it under the terms of the GNU General Public License (GPL)            *
    # *   as published by the Free Software Foundation; either version 3 of     *
    # *   the License, or (at your option) any later version.                   *
    # *   for detail see the LICENCE text file.                                 *
    # *                                                                         *
    # *   This program is distributed in the hope that it will be useful,       *
    # *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
    # *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
    # *   GNU General Public License for more details.                          *
    # *                                                                         *
    # *   You should have received a copy of the GNU Library General Public     *
    # *   License along with this program; if not, write to the Free Software   *
    # *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
    # *   USA                                                                   *
    # *                                                                         *
    # ***************************************************************************

    """This macro opens a file dialog to allow to choose a FreeCAD file
    and converts it to 0.21 format (replace AttachmentSupport property to Support).
    A new file with extension .021.FCStd is created so the original file is not modified"""
    import os
    import zipfile
    from PySide import QtGui

    filenames = QtGui.QFileDialog.getOpenFileNames(None,
                                                 "Open FreeCAD file",
                                                 None,
                                                 "FreeCAD Files (*.FCStd *.fcstd)")
    for filename in filenames[0]:
        print("Processing", filename, "...")
        spl = os.path.splitext(filename)
        filename021 = spl[0] + ".021" + spl[1]
        with zipfile.ZipFile(filename) as inzip, zipfile.ZipFile(filename021, "w") as outzip:
            for inzipinfo in inzip.infolist():
                with inzip.open(inzipinfo) as infile:
                    if inzipinfo.filename == "Document.xml":
                        content = infile.read()
                        content = content.replace(b"AttachmentSupport", b"Support")
                        outzip.writestr(inzipinfo, content)
                    else:
                        outzip.writestr(inzipinfo, infile.read())
        print(filename021, "successfully written")

    print ("All done!")



---
⏵ [documentation index](../README.md) > Macro Convert 021
