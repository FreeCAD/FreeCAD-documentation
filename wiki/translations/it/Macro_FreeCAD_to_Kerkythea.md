# Macro FreeCAD to Kerkythea/it
{{Macro/it
|Name=FC to Kerkythea
|Icon=Macro_FreeCAD_to_Kerkythea.png
|Translate=FC in Kerkythea
|Description=Esporta un modello FreeCAD in Kerkythea
|Author=marmni
|Version=1.0
|Date=2015-05-30
|FCVersion=0.17 and above
|Download=[https://www.freecadweb.org/wiki/images/8/8c/Macro_FreeCAD_to_Kerkythea.png ToolBar Icon]
}}

## Descrizione

Macro per esportare il proprio modello nel programma di raytracing [Kerkythea](http://www.kerkythea.net/cms/).


<div class="mw-translate-fuzzy">

## Uso

La macro è disponibile nel seguente repository github: [FreeCAD to Kerkythea-Exporter](https://github.com/marmni/FreeCAD-Kerkythea)


</div>

E\' praticamente auto-esplicativa. Al momento ci sono problemi per esportare le luci e la posizione della telecamera.

## Link

La pagina di discussione: [Kerkythea Rendering System](http://forum.freecadweb.org/viewtopic.php?t=8861)

## Script

Macro ExportToKerkythea.py

ToolBar Icon ![](images/Macro_FreeCAD_to_Kerkythea.png )

**Macro ExportToKerkythea.py**


{{MacroCode|code=
# -*- coding: utf8 -*-
#**************************************************************************************
#*                                                                                    *
#*   Kerkythea exporter                                                               *
#*   Copyright (c) 2014,2015                                                          *
#*   marmni <marmni@onet.eu>                                                          *
#*                                                                                    *
#*   This program is free software; you can redistribute it and/or modify             *
#*   it under the terms of the GNU Lesser General Public License (LGPL)               *
#*   as published by the Free Software Foundation; either version 2 of                *
#*   the License, or (at your option) any later version.                              *
#*   for detail see the LICENCE text file.                                            *
#*                                                                                    *
#*   This program is distributed in the hope that it will be useful,                  *
#*   but WITHOUT ANY WARRANTY; without even the implied warranty of                   *
#*   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                    *
#*   GNU Library General Public License for more details.                             *
#*                                                                                    *
#*   You should have received a copy of the GNU Library General Public                *
#*   License along with this program; if not, write to the Free Software              *
#*   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307             *
#*   USA                                                                              *
#*                                                                                    *
#**************************************************************************************

#**************************************************************************************
#*                                                                                    *
#*                                 BASED ON                                           *
#*                                                                                    *
#* IOANNIS PANTAZOPOULOS                                                              *
#*                                                                                    *
#* Sample code exporting basic Kerkythea XML file.                                    *
#*                                                                                    *
#* Version v1.0                                                                       *
#*                                                                                    *
#**************************************************************************************

__title__="Kerkythea exporter"
__author__ = "marmni <marmni@onet.eu>"
__url__ = ["http://www.freecadweb.org"]


import FreeCAD, FreeCADGui
import re
import random
import __builtin__
import Mesh
from PySide import QtCore, QtGui
import sys
import os


##############################################
#
##############################################
class point3D:
    def __init__(self, point):
        self.x = "%.4f" % (point[0] * 0.001)
        self.y = "%.4f" % (point[1] * 0.001)
        self.z = "%.4f" % (point[2] * 0.001)

    def __str__(self):
        return '<P xyz="{0} {1} {2}"/>'.format(self.x, self.y, self.z)

    #def __eq__(self, other):
        #if self.x == other.x and self.y == other.y and self.z == other.z:
            #return True
        #else:
            #return False 


##############################################
#
##############################################
class indexListPoint3D:
    def __init__(self, point):
        self.i = point[0]
        self.j = point[1]
        self.k = point[2]

    def __str__(self):
        return '<F ijk="{0} {1} {2}"/>'.format(self.i, self.j, self.k)


##############################################
#
##############################################
class Material:
    def __init__(self):
        self.diffuse = None  # Texture()
        self.shininess = 1000.0
        self.ior = 2.0

    def write(self, file):
        file.write('''<Object Identifier="Whitted Material" Label="Whitted Material" Name="" Type="Material">\n''')

        self.diffuse.write(file, "Diffuse")
        self.diffuse.write(file, "Translucent")
        self.diffuse.write(file, "Specular")
        self.diffuse.write(file, "Transmitted")

        file.write('''<Parameter Name="Shininess" Type="Real" Value="{shininess}"/>
<Parameter Name="Transmitted Shininess" Type="Real" Value="{shininess}"/>
<Parameter Name="Index of Refraction" Type="Real" Value="{ior}"/>
</Object>\n'''.format(shininess=self.shininess, ior=self.ior))


##############################################
#
##############################################
class Texture:
    def __init__(self, color):
        self.color = color
        
    def getColorSTR(self):
        return '{0} {1} {2}'.format(self.color[0], self.color[1], self.color[2])

    def toGrayscale(self):
        RGB = 0.299 * self.color[0] + 0.587 * self.color[1] + 0.114 * self.color[2]
        self.color = [RGB, RGB, RGB]

    def write(self, file, identifier):
        file.write('''<Object Identifier="./{identifier}/Constant Texture" Label="Constant Texture" Name="" Type="Texture">
<Parameter Name="Color" Type="RGB" Value="{color}"/>
</Object>\n'''.format(identifier=identifier, color=self.getColorSTR()))


##############################################
#
##############################################
class Model:
    def __init__(self):
        self.vertexList = []
        self.normalList = []
        self.indexList = []
        
        self.name = self.wygenerujID(5, 5)
        self.material = Material()
        
    def addFace(self, face):
        mesh = self.meshFace(face)
        for pp in mesh.Facets:
            num = len(self.vertexList)
            for kk in pp.Points:
                self.vertexList.append(point3D(kk))
            self.indexList.append(indexListPoint3D([num, num + 1, num + 2]))
        
    def meshFace(self, shape):
        faces = []
        triangles = shape.tessellate(1) # the number represents the precision of the tessellation
        for tri in triangles[1]:
            face = []
            for i in range(3):
                vindex = tri[i]
                face.append(triangles[0][vindex])
            faces.append(face)
        m = Mesh.Mesh(faces)
        #Mesh.show(m)
        return m
        
    def wygenerujID(self, ll, lc):
        ''' generate random model name '''
        numerID = ""

        for i in range(ll):
            numerID += random.choice('abcdefghij')
        numerID += "_"
        for i in range(lc):
            numerID += str(random.randrange(0, 99, 1))
        
        return numerID

    def write(self, file):
        file.write('''
<Object Identifier="./Models/{name}" Label="Default Model" Name="{name}" Type="Model"> 
<Object Identifier="Triangular Mesh" Label="Triangular Mesh" Name="" Type="Surface">
<Parameter Name="Vertex List" Type="Point3D List" Value="{pointListSize}">\n'''.format(name=self.name, pointListSize=len(self.vertexList)))

        for i in self.vertexList:
            file.write('{0}\n'.format(i))

        file.write('''</Parameter>
<Parameter Name="Normal List" Type="Point3D List" Value="{pointListSize}">\n'''.format(pointListSize=len(self.vertexList)))
        file.write('<P xyz="0 0 -1"/>\n' * len(self.vertexList))
        file.write('''</Parameter>
<Parameter Name="Index List" Type="Triangle Index List" Value="{indexListSize}">\n'''.format(indexListSize=len(self.indexList)))

        for i in self.indexList:
            file.write('{0}\n'.format(i))

        file.write('''</Parameter>\n</Object>\n''')

        self.material.write(file)
        
        file.write('</Object>\n')


##############################################
#
##############################################
class Camera:
    def __init__(self):
        self.name = "Camera_1"
        self.f_number = "Pinhole"
        self.resolution = "1024x768"
        self.focusDistance = "1"
        self.lensSamples = "3"
        self.blades = "3"
        self.diaphragm = "Circular"
        self.projection = "Planar"

    def addParameter(self, name, pType, value):
        return '<Parameter Name="{0}" Type="{1}" Value="{2}"/>\n'.format(name, pType, value)
        
    def write(self, file):
        cam = FreeCADGui.ActiveDocument.ActiveView.getCameraNode()
        camValues = cam.position.getValue()
        
        x = "%.4f" % (30 * .0254)
        y = "%.4f" % (30 * .0254)
        z = "%.4f" % (30 * .0254)
        
        file.write('<Object Identifier="./Cameras/{0}" Label="Pinhole Camera" Name="{0}" Type="Camera">\n'.format(self.name))
        file.write(self.addParameter("Resolution", "String", self.resolution))
        file.write(self.addParameter("Frame", "Transform", "-0.609474 0.471636 -0.63726 {0} 0.792806 0.362576 -0.489895 {1} 2.70762e-06 -0.803802 -0.594897 {2}".format(x, y, z)))
        file.write(self.addParameter("Focus Distance", "Real", self.focusDistance))
        file.write(self.addParameter("f-number", "String", self.f_number))
        file.write(self.addParameter("Lens Samples", "Integer",self.lensSamples ))
        file.write(self.addParameter("Blades", "Integer", self.blades))
        file.write(self.addParameter("Diaphragm", "String", self.diaphragm))
        file.write(self.addParameter("Projection", "String", self.projection))
        file.write('</Object>\n')


##############################################
#
##############################################
class exportTokerkythea:
    def __init__(self):
        self.models = []
        self.cameras = []
        modelsMultiColors = False

    def write(self, file, name):
        file = __builtin__.open(file, "w")
        #
        self.writeHeader(file, name)
        
        if self.modelsMultiColors:
            for i, j in self.models.items():
                file.write('<Object Identifier="./Models/{0}" Label="Default Model" Name="{0}" Type="Model">\n'.format(i))
                for k in j:
                    k.write(file)
                file.write('</Object>\n')
        else:
            for i in self.models.values():
                i.write(file)
        # CAMERA
        activeCamera = self.cameras[0][0].name
        for i in self.cameras:
            i[0].write(file)
            if i[1]:
                activeCamera = i[0].name
        #
        file.write('<Parameter Name="./Cameras/Active" Type="String" Value="{0}"/>\n'.format(activeCamera))

        self.writeFooter(file, name)

    def writeHeader(self, file, name):
        file.write('''<Root Label="Kernel" Name="" Type="Kernel">
<Object Identifier="./Ray Tracers/Metropolis Light Transport" Label="Metropolis Light Transport" Name="Metropolis Light Transport" Type="Ray Tracer">
</Object>
<Object Identifier="./Environments/Octree Environment" Label="Octree Environment" Name="Octree Environment" Type="Environment">
</Object>
<Object Identifier="./Filters/Simple Tone Mapping" Label="Simple Tone Mapping" Name="" Type="Filter">
</Object>
<Object Identifier="./Scenes/{0}" Label="Default Scene" Name="{0}" Type="Scene">\n
'''.format(name))

    def writeFooter(self, file, name):
        file.write('''</Object>
<Parameter Name="Mip Mapping" Type="Boolean" Value="1"/>
<Parameter Name="./Interfaces/Active" Type="String" Value="Null Interface"/>
<Parameter Name="./Modellers/Active" Type="String" Value="XML Modeller"/>
<Parameter Name="./Image Handlers/Active" Type="String" Value="Free Image Support"/>
<Parameter Name="./Ray Tracers/Active" Type="String" Value="Metropolis Light Transport"/>
<Parameter Name="./Irradiance Estimators/Active" Type="String" Value="Null Irradiance Estimator"/>
<Parameter Name="./Direct Light Estimators/Active" Type="String" Value="Null Direct Light Estimator"/>
<Parameter Name="./Environments/Active" Type="String" Value="Octree Environment"/>
<Parameter Name="./Filters/Active" Type="String" Value="Simple Tone Mapping"/>
<Parameter Name="./Scenes/Active" Type="String" Value="{0}"/>
<Parameter Name="./Libraries/Active" Type="String" Value="Material Librarian"/>
</Root>'''.format(name))


##############################################
#
##############################################

class exportKerkytheaDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)

        self.setWindowTitle(u'Export to Kerkythea v1.1')
        self.setFixedSize(500, 550)

        #
        self.buttonAccept = QtGui.QPushButton('Accept')
        #
        tab = QtGui.QTabWidget()
        tab.addTab(self.addGeneralPage(), u'General')
        tab.addTab(self.addLightsPage(), u'Light')
        tab.addTab(self.addCmerasPage(), u'Camera')
        #
        lay = QtGui.QVBoxLayout(self)
        lay.addWidget(tab)
        lay.addWidget(self.buttonAccept)

    def changePathF(self):
        path = QtGui.QFileDialog().getSaveFileName(self, u"Save as", os.path.expanduser("~"), "*.xml")
        
        fileName = path[0]
        if not fileName == "":
            if not fileName.endswith('xml'):
                fileName = fileName + '.xml'
            self.filePath.setText(fileName)
            
    def addGeneralPage(self):
        self.filePath = QtGui.QLineEdit(os.path.join(os.path.expanduser("~"), 'Unnamed.xml'))
        self.filePath.setReadOnly(True)

        changePath = QtGui.QPushButton('...')
        changePath.setFixedWidth(30)
        self.connect(changePath, QtCore.SIGNAL("clicked ()"), self.changePathF)

        generalBox = QtGui.QGroupBox(u'General')
        generalBoxLay = QtGui.QGridLayout(generalBox)
        generalBoxLay.addWidget(QtGui.QLabel(u'Path           '), 0, 0, 1, 1)
        generalBoxLay.addWidget(self.filePath, 0, 1, 1, 2)
        generalBoxLay.addWidget(changePath, 0, 3, 1, 1)

        generalBoxLay.setColumnStretch(1, 10)
        #
        self.exportObjects_All = QtGui.QRadioButton(u'All visible objects')
        self.exportObjects_All.setChecked(True)
        self.exportObjects_Selected = QtGui.QRadioButton(u'All selected objects')
        self.exportObjects_SelectedFaces = QtGui.QRadioButton(u'All selected faces')
        self.exportObjects_SelectedFaces.setDisabled(True)
        
        exportObjectsBox = QtGui.QGroupBox(u'Export objects')
        exportObjectsBoxLay = QtGui.QVBoxLayout(exportObjectsBox)
        exportObjectsBoxLay.addWidget(self.exportObjects_All)
        exportObjectsBoxLay.addWidget(self.exportObjects_Selected)
        exportObjectsBoxLay.addWidget(self.exportObjects_SelectedFaces)
        #
        self.exportObjectsAs_YES = QtGui.QRadioButton(u'Yes')
        self.exportObjectsAs_YES.setChecked(True)
        self.exportObjectsAs_NO = QtGui.QRadioButton(u'No')
        
        exportObjectsAsBox = QtGui.QGroupBox(u'Group models by color')
        exportObjectsAsBoxLay = QtGui.QVBoxLayout(exportObjectsAsBox)
        exportObjectsAsBoxLay.addWidget(self.exportObjectsAs_YES)
        exportObjectsAsBoxLay.addWidget(self.exportObjectsAs_NO)
        #
        self.exportObjectColor_MulCol = QtGui.QRadioButton(u'Multi colors')
        self.exportObjectColor_Gray = QtGui.QRadioButton(u'Grayscale')
        self.exportObjectColor_SinCol = QtGui.QRadioButton(u'Single color (random)')
        self.exportObjectColor_SinCol.setChecked(True)

        self.exportObjectColorBox = QtGui.QGroupBox(u'Colors')
        self.exportObjectColorBox.setDisabled(True)
        exportObjectColorBoxLay = QtGui.QVBoxLayout(self.exportObjectColorBox)
        exportObjectColorBoxLay.addWidget(self.exportObjectColor_MulCol)
        exportObjectColorBoxLay.addWidget(self.exportObjectColor_Gray)
        exportObjectColorBoxLay.addWidget(self.exportObjectColor_SinCol)
        #####
        widget = QtGui.QWidget()
        
        lay = QtGui.QGridLayout(widget)
        lay.addWidget(generalBox, 0, 0, 1, 4)
        lay.addWidget(exportObjectsBox, 1, 0, 1, 4)
        lay.addWidget(exportObjectsAsBox, 2, 0, 1, 2)
        lay.addWidget(self.exportObjectColorBox, 2, 2, 1, 2)
        
        lay.setRowStretch(10, 10)
        #lay.setColumnStretch(10, 10)
        return widget
        
    def addLightsPage(self):
        widget = QtGui.QWidget()
        
        return widget
        
    def addCmerasPage(self):
        self.resolution = QtGui.QComboBox()
        self.resolution.addItems(['200x200', '320x200', '320x240', '500x500', '512x384', '640x480', '768x576', '800x600', '1024x768', '1280x1024', '1600x1200', '2048x1536', '2816x2112'])
        self.resolution.setCurrentIndex(self.resolution.findText('1024x768'))

        self.cameraName = QtGui.QLineEdit(u'Camera 1')

        filmBox = QtGui.QGroupBox(u'General')
        filmBoxLay = QtGui.QGridLayout(filmBox)
        filmBoxLay.addWidget(QtGui.QLabel(u'Camera name'), 0, 0, 1, 1)
        filmBoxLay.addWidget(self.cameraName, 0, 1, 1, 1)
        filmBoxLay.addWidget(QtGui.QLabel(u'Resolution'), 1, 0, 1, 1)
        filmBoxLay.addWidget(self.resolution, 1, 1, 1, 1)

        filmBoxLay.setHorizontalSpacing(50)
        #
        self.fNumber = QtGui.QComboBox()
        self.fNumber.addItems(['1', '1.4', '2', '2.8', '4', '5.6', '8', '16', '22', 'Pinhole'])
        self.fNumber.setCurrentIndex(self.fNumber.findText('Pinhole'))

        self.focusDistance = QtGui.QDoubleSpinBox()
        self.focusDistance.setValue(1.0)
        self.focusDistance.setRange(0.0, 1000.0)

        self.lensSamples = QtGui.QSpinBox()
        self.lensSamples.setValue(3)
        self.lensSamples.setRange(0, 1000)

        lensBox = QtGui.QGroupBox(u'Lens')
        lensBoxLay = QtGui.QGridLayout(lensBox)
        lensBoxLay.addWidget(QtGui.QLabel(u'f-number'), 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        lensBoxLay.addWidget(self.fNumber, 1, 0, 1, 1)
        lensBoxLay.addWidget(QtGui.QLabel(u'Focus Distance'), 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        lensBoxLay.addWidget(self.focusDistance, 1, 1, 1, 1)
        lensBoxLay.addWidget(QtGui.QLabel(u'Lens Samples'), 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        lensBoxLay.addWidget(self.lensSamples, 1, 2, 1, 1)

        lensBoxLay.setHorizontalSpacing(50)
        #
        self.projection = QtGui.QComboBox()
        self.projection.addItems(['Planar', 'Cylindrical', 'Spherical', 'Parallel'])
        self.projection.setCurrentIndex(self.projection.findText('Planar'))

        self.diaphragm = QtGui.QComboBox()
        self.diaphragm.addItems(['Circular', 'Polygonal'])
        self.diaphragm.setCurrentIndex(self.diaphragm.findText('Circular'))
        
        self.blades = QtGui.QSpinBox()
        self.blades.setValue(3)
        self.blades.setRange(3, 1000)

        geometryBox = QtGui.QGroupBox(u'Geometry')
        geometryBoxLay = QtGui.QGridLayout(geometryBox)
        geometryBoxLay.addWidget(QtGui.QLabel(u'Projection'), 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        geometryBoxLay.addWidget(self.projection, 1, 0, 1, 1)
        geometryBoxLay.addWidget(QtGui.QLabel(u'Diaphragm'), 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        geometryBoxLay.addWidget(self.diaphragm, 1, 1, 1, 1)
        geometryBoxLay.addWidget(QtGui.QLabel(u'Blades'), 0, 2, 1, 1, QtCore.Qt.AlignHCenter)
        geometryBoxLay.addWidget(self.blades, 1, 2, 1, 1)

        geometryBoxLay.setHorizontalSpacing(50)
        #
        #####
        widget = QtGui.QWidget()
        lay = QtGui.QVBoxLayout(widget)
        lay.addWidget(filmBox)
        lay.addWidget(lensBox)
        lay.addWidget(geometryBox)
        lay.addStretch(10)

        return widget
        


class exportKerkythea(exportKerkytheaDialog):
    def __init__(self, parent=None):
        exportKerkytheaDialog.__init__(self, parent)

        self.connect(self.buttonAccept, QtCore.SIGNAL("clicked ()"), self.acceptw)
        self.connect(self.exportObjectsAs_YES, QtCore.SIGNAL("clicked ()"), self.setColors)
        self.connect(self.exportObjectsAs_NO, QtCore.SIGNAL("clicked ()"), self.setColors)

    def setColors(self):
        if self.exportObjectsAs_YES.isChecked():
            self.exportObjectColor_SinCol.setChecked(True)
            self.exportObjectColorBox.setDisabled(True)
        else:
            self.exportObjectColorBox.setDisabled(False)

    def acceptw(self):
        if self.exportObjects_All.isChecked():
            projectObjects = [i for i in FreeCAD.ActiveDocument.Objects if i.ViewObject.Visibility]
        elif self.exportObjects_Selected.isChecked():
            projectObjects = []
            for i in FreeCADGui.Selection.getSelection():
                if i.ViewObject.Visibility and i not in projectObjects:
                    projectObjects.append(i)
        #

        projectModels = {}
        for i in projectObjects:  # objects in document
            try:
                objectColors = i.ViewObject.DiffuseColor
                shape = i.Shape.Faces
            except:
                continue
                
            for j in range(len(i.Shape.Faces)):  # object faces
                # get face color
                if len(objectColors) == len(i.Shape.Faces):
                    modelType = objectColors[j]
                else:
                    modelType = objectColors[0]
                #
                if self.exportObjectsAs_YES.isChecked():
                    modelID = str(modelType)
                else:
                    modelID = i.Label
                #
                if self.exportObjectColor_SinCol.isChecked():
                    modelsMultiColors = False

                    if not modelID in projectModels:
                        model = Model()
                        if self.exportObjectsAs_NO.isChecked():
                            model.name = modelID
                        model.material.diffuse = Texture(modelType)
                        projectModels[modelID] = model
                    else:
                        model = projectModels[modelID]
                else:
                    modelsMultiColors = True

                    if not modelID in projectModels:
                        projectModels[modelID] = []

                    model = Model()
                    model.name = 'Face {0}'.format(j)
                    model.material.diffuse = Texture(modelType)
                    if self.exportObjectColor_Gray.isChecked():
                        model.material.diffuse.toGrayscale()
                    projectModels[modelID].append(model)
                   
#                   model = Model()
#                   model.material.diffuse = Texture(modelType)
#                   projectModels[i.Label].append(model)
                #
                model.addFace(i.Shape.Faces[j])

        exporter = exportTokerkythea()
        exporter.modelsMultiColors = modelsMultiColors
        exporter.models = projectModels
        # CAMERA
        camera = Camera()
        camera.name = self.cameraName.text()
        camera.f_number = self.fNumber.currentText()
        camera.resolution = self.resolution.currentText()
        camera.focusDistance = self.focusDistance.value()
        camera.lensSamples = self.lensSamples.value()
        camera.blades = self.blades.value()
        camera.diaphragm = self.diaphragm.currentText()
        camera.projection = self.projection.currentText()
        
        exporter.cameras.append([camera, True])
        #
        exporter.write(self.filePath.text(), FreeCAD.ActiveDocument.Label)

        self.close()

exportKerkythea().exec_()

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Macro FreeCAD to Kerkythea/it
