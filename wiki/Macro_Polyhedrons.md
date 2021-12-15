# Macro Polyhedrons
{{Macro
|Name=Macro Polyhedrons
|Icon=Dodecahedron.svg
|Description=This macro creates parametric polyhedrons: tetrahedron, hexahedron, octahedron, dodecahedron, icosahedron, icosahedron_truncated<br/>Parameters radius and side can be adjusted.
|Author=Eddy Verlinden, Genk, Belgium
|Version=01.02
|Date=2020-01-10
|FCVersion=All
|Download=ToolBar icon [https://www.freecadweb.org/wiki/images/a/a4/Dodecahedron.svg Icon ToolBar]
|SeeAlso=<img src=images/Pyramidicon.svg style="width:Macro Pyramid](Macro_Pyramid.md) [24px">
}}

## Description

This macro creates parametric polyhedrons: tetrahedron, hexahedron, octahedron, dodecahedron, icosahedron, icosahedron\_truncated, and geodesic spheres at several levels

## Notes

-   If you\'re also interested in pyramids, then you can use <img alt="" src=images/Pyramidicon.svg  style="width:24px;"> [Pyramid macro](Macro_Pyramid.md).
-   You can also make use of the the external workbench [Pyramids\_and\_Polyhedrons](https://github.com/eddyverl/FreeCad-Pyramids-and-Polyhedrons) (github link) that contains the same functions.

![](images/Polyhedrons.png )

## Installation

-   Use the <img alt="" src=images/Std_AddonMgr.svg  style="width:24px;"> [Addon Manager](Std_AddonMgr.md) to install the macro via 
**Tools → Addon Manager → Macros tab**
-   Choose `polyhedrons.py`
-   Press **Install**

## Usage

-   Once installed, open **Macro → Macros**.
-   Click on `polyhedrons.py` and then click on the {{button|Execute}} button.
-   In a popup you can select the type of polyhedron, and you can set the size of the radius or the length of the sides.
-   Press **OK**

Note: You can always adjust the radius or the size, just like with normal parts.

-   More info at [Pyramids\_and\_Polyhedrons](https://github.com/eddyverl/FreeCad-Pyramids-and-Polyhedrons) (github README)

## Related

The forum discussion [Macros for pyramids and polyhedrons](https://forum.freecadweb.org/viewtopic.php?f=22&t=40485&p=344116&hilit=Eddyverl#p344116)

## Script



ToolBar Icon <img alt="" src=images/Dodecahedron.svg  style="width:36px;">

**polyhedrons.py**


{{MacroCode|code=
# ***************************************************************************
# *   Copyright (c) 2019  Eddy Verlinden , Genk Belgium   (eddyverl)        *   
# *                                                                         *
# *   This file is part of the FreeCAD CAx development system.              *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   FreeCAD is distributed in the hope that it will be useful,            *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Lesser General Public License for more details.                   *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with FreeCAD; if not, write to the Free Software        *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************



__Title__   = "Macro_Polyhedrons"
__Author__  = "Eddy Verlinden"
__Version__ = "01.04"
__Date__    = "2020-02-25"
__Comment__ = "This macro creates parametric polyhedrons."


# version 1.04 (2020-02-25)
# correction : value of the side of icosahedron-truncated 

# ver 01.03 (2020-01-15) :
# => added geodesic spheres
# => some additions to the dialog

# ver 01.02 (2020-01-10) 
#  => first release

import FreeCAD,FreeCADGui
import Part
import math
import sys, time
from PySide import QtGui, QtCore
from FreeCAD import Base


def horizontal_regular_polygon_vertexes(sidescount,radius,z, startangle = 0):
    vertexes = []
    if radius != 0 :
        for i in range(0,sidescount+1):
            angle = 2 * math.pi * i / sidescount + math.pi + startangle
            vertex = (radius * math.cos(angle), radius * math.sin(angle), z)
            vertexes.append(vertex)
    else:
        vertex = (0,0,z)
        vertexes.append(vertex)
    return vertexes

       
# ===========================================================================    
    
class Tetrahedron:
        # == basics ==
        #R = z / 4 * sqrt(6)
        #ro = z / 12 * sqrt(6)    -->   ro = R / 3
        #z = 4 * R / sqrt(6)
        #h = z / 3 * sqrt(6) = 4 * R / sqrt(6) /3 * sqrt(6) = 4 * R / 3  = ro + R 
        #radius at level = z / 2 / cos(30) = (4 * R / sqrt(6)) / 2 / sqrt(3) * 2 = 4 * R / (sqrt(6) * sqrt(3))= 4 * R / (3 * sqrt(2)
        
    radiusvalue = 0  
      
    def __init__(self, obj, radius=5):
        obj.addProperty("App::PropertyLength","Radius","Tetrahedron","Radius of the tetrahedron").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Tetrahedron","Sidelength of the tetrahedron")
        obj.Proxy = self

        
    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = radius * 4 / math.sqrt(6)
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * math.sqrt(6) / 4)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            
        faces = []        
        vertexes_bottom = horizontal_regular_polygon_vertexes(3,4*radius/3/math.sqrt(2),- radius / 3)
        vertexes_top    = horizontal_regular_polygon_vertexes(1,0,radius)
        
        for i in range(3):
            vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_top[0],vertexes_bottom[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        polygon_bottom=Part.makePolygon(vertexes_bottom)
        
        faces.append(Part.Face(polygon_bottom))
        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid
        



# ===========================================================================    

class Hexahedron: 
 
    radiusvalue = 0  def __init__(self, obj, radius=5):
        obj.addProperty("App::PropertyLength","Radius","Hexahedron","Radius of the hexahedron").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Hexahedron","Sidelength of the hexahedron")
        obj.Proxy = self

    def execute(self, obj):
            
        radius = float(obj.Radius) 
        if (radius != self.radiusvalue):
            side = radius * 2 / math.sqrt(3)
            obj.Side = side
            self.radiusvalue = radius
        else:
            self.radiusvalue = obj.Side / 2 * math.sqrt(3)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            side = obj.Side       
             
        faces = []
        vertexes_bottom = horizontal_regular_polygon_vertexes(4,math.sqrt(side ** 2 / 2),- side/2, math.pi/4)
        vertexes_top    = horizontal_regular_polygon_vertexes(4,math.sqrt(side ** 2 / 2), side/2, math.pi/4)

        for i in range(4):
            vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_top[i+1],vertexes_top[i],vertexes_bottom[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        polygon_bottom=Part.makePolygon(vertexes_bottom)
        faces.append(Part.Face(polygon_bottom))
        
        polygon_top=Part.makePolygon(vertexes_top)
        faces.append(Part.Face(polygon_top))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid        
        
# ===========================================================================    

class Octahedron: 
    # Z = R * sqrt(2)   
    radiusvalue = 0  def __init__(self, obj, radius=5):
        obj.addProperty("App::PropertyLength","Radius","Octahedron","Radius of the octahedron").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Octahedron","Sidelength of the octahedron")
        obj.Proxy = self
  
    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = radius * math.sqrt(2)
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side / math.sqrt(2))
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue 

        faces = []
        vertexes_middle = horizontal_regular_polygon_vertexes(4,radius,0)
        vertexes_bottom = horizontal_regular_polygon_vertexes(1,0,-radius)
        vertexes_top    = horizontal_regular_polygon_vertexes(1,0,radius)

        for i in range(4):
            vertexes_side=[vertexes_middle[i],vertexes_middle[i+1],vertexes_top[0],vertexes_middle[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(4):
            vertexes_side=[vertexes_middle[i],vertexes_middle[i+1],vertexes_bottom[0],vertexes_middle[i]]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid



# ===========================================================================    
    
class Dodecahedron:radiusvalue = 0  
   
    def __init__(self, obj, radius=5):
        obj.addProperty("App::PropertyLength","Radius","Dodecahedron","Radius of the dodecahedron").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Dodecahedron","Sidelength of the dodecahedron")
        obj.Proxy = self
    

    def execute (self,obj):
        
        angleribs = 121.717474411
        anglefaces = 116.565051177

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = 4 * radius /  (math.sqrt(3) * ( 1 + math.sqrt(5)))
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * (math.sqrt(3) * ( 1 + math.sqrt(5))) / 4)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            
        faces = []
        z = 4 * radius /  (math.sqrt(3) * ( 1 + math.sqrt(5)))
        r = z/2 * math.sqrt((25 + (11 * math.sqrt(5)))/10)
        # int sphere r is height / 2

        h2 = z * math.sin(angleribs/180 * math.pi)

        #height of the side-tips
        radius1 = z / 2 / math.sin(36 * math.pi / 180)
        h5h = (radius1 + radius1 * math.cos(36 * math.pi / 180))   * math.sin(anglefaces * math.pi / 180) #height of the tops

        radius2 = radius1 - z * math.cos(angleribs * math.pi / 180 )

        r=(h2 + h5h)/2  # XXX to make it fit!




        vertexes_bottom = horizontal_regular_polygon_vertexes(5,radius1,-r)
        vertexes_low = horizontal_regular_polygon_vertexes(5,radius2, -r + h2)
        vertexes_high = horizontal_regular_polygon_vertexes(5,radius2, -r + h5h,  math.pi/5)
        vertexes_top = horizontal_regular_polygon_vertexes(5,radius1, r, math.pi/5)

        polygon_bottom = Part.makePolygon(vertexes_bottom)
        face_bottom = Part.Face(polygon_bottom)
        faces.append(face_bottom)

        polygon_top = Part.makePolygon(vertexes_top)
        face_top = Part.Face(polygon_top)
        faces.append(face_top)

        for i in range(5):
            vertexes_side=[vertexes_bottom[i],vertexes_bottom[i+1],vertexes_low[i+1],vertexes_high[i],vertexes_low[i], vertexes_bottom[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            #vertexes_side=[vertexes_top[i],vertexes_top[i+1],vertexes_high[i+1],vertexes_high2[i], vertexes_high[i],vertexes_top[i] ]
            vertexes_side=[vertexes_top[i],vertexes_top[i+1],vertexes_high[i+1],vertexes_low[i+1],vertexes_high[i],vertexes_top[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid


# ===========================================================================    

class Icosahedron:radiusvalue = 0  

    def __init__(self, obj, radius=5):
        obj.addProperty("App::PropertyLength","Radius","Icosahedron","Radius of the icosahedron").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Icosahedron","Sidelength of the icosahedron")
        obj.Proxy = self


    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * math.sqrt(10 + 2 * math.sqrt(5)) / 4)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            

        z = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
        anglefaces = 138.189685104
        r = z/12 * math.sqrt(3) * (3 + math.sqrt(5))


        #radius of a pentagon with the same side
        radius2 = z / math.sin(36 * math.pi/180)/2
        #height of radius2 in the sphere

        angle = math.acos(radius2/radius)
        height = radius * math.sin(angle)

        faces = []

        vertex_bottom = (0,0,-radius)
        vertexes_low = horizontal_regular_polygon_vertexes(5,radius2, -height)
        vertexes_high = horizontal_regular_polygon_vertexes(5,radius2, height, math.pi/5)
        vertex_top = (0,0,radius)


        for i in range(5):
            vertexes_side=[vertex_bottom,vertexes_low[i],vertexes_low[i+1], vertex_bottom]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertexes_side=[vertexes_low[i],vertexes_low[i+1],vertexes_high[i],vertexes_low[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))
            vertexes_side=[vertexes_high[i],vertexes_high[i+1],vertexes_low[i+1],vertexes_high[i] ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertexes_side=[vertex_top,vertexes_high[i],vertexes_high[i+1],vertex_top ]
            polygon_side=Part.makePolygon(vertexes_side)
            faces.append(Part.Face(polygon_side))

        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid
   


# ===========================================================================    

class Icosahedron_truncated:radiusvalue = 0  

    def __init__(self, obj, radius=5):
        obj.addProperty("App::PropertyLength","Radius","Icosahedron_truncated","Radius (of the base-icosahedron)").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Icosahedron_truncated","Sidelength of the truncated icosahedron")
        obj.Proxy = self

    def execute (self,obj):

        radius = float(obj.Radius)
        if (radius != self.radiusvalue):
            obj.Side = 4*radius / math.sqrt(10 + 2 * math.sqrt(5)) / 3
            self.radiusvalue = radius
        else:
            self.radiusvalue = float(obj.Side * math.sqrt(10 + 2 * math.sqrt(5)) / 4) * 3
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            
        z = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
        anglefaces = 138.189685104
        r = z/12 * math.sqrt(3) * (3 + math.sqrt(5))

        #radius of a pentagon with the same side
        radius2 = z / math.sin(36 * math.pi/180)/2

        #height of radius2 in the sphere
        angle = math.acos(radius2/radius)
        height = radius * math.sin(angle)

        faces = []

        vertex_bottom = (0,0,-radius)
        vertexes_low = horizontal_regular_polygon_vertexes(5,radius2, -height)
        vertexes_high = horizontal_regular_polygon_vertexes(5,radius2, height,  -math.pi/5)
        vertex_top = (0,0,radius)

        vertexes_bottom = []
        vertexes_top = []

        for i in range(6):
            new_vertex = ((vertex_bottom[0]+vertexes_low[i][0])/3 , (vertex_bottom[1]+vertexes_low[i][1])/3 , vertex_bottom[2]-(vertex_bottom[2]-vertexes_low[i][2])/3)
            vertexes_bottom.append(new_vertex)
        polygon_side=Part.makePolygon(vertexes_bottom)
        faces.append(Part.Face(polygon_side))

        for i in range(6):
            new_vertex = ((vertex_top[0]+vertexes_high[i][0])/3 , (vertex_top[1]+vertexes_high[i][1])/3 , vertex_top[2]-(vertex_top[2]-vertexes_high[i][2])/3)
            vertexes_top.append(new_vertex)
        polygon_side=Part.makePolygon(vertexes_top)
        faces.append(Part.Face(polygon_side))

        pg6_bottom = []
        for i in range(5):
            vertex1=vertexes_bottom[i]
            vertex2=vertexes_bottom[i+1]
            vertex3=(vertexes_bottom[i+1][0] + (vertexes_low[i+1][0] - vertexes_bottom[i+1][0])/2, vertexes_bottom[i+1][1] + (vertexes_low[i+1][1] - vertexes_bottom[i+1][1])/2, (vertexes_low[i+1][2] + vertexes_bottom[i+1][2])/2)
            vertex4=((vertexes_low[i+1][0]*2 +vertexes_low[i][0])/3, (vertexes_low[i+1][1]*2 +vertexes_low[i][1])/3, -height)
            vertex5=((vertexes_low[i+1][0]+vertexes_low[i][0]*2)/3, (vertexes_low[i+1][1] +vertexes_low[i][1]*2)/3, -height)
            vertex6=(vertexes_bottom[i][0] + (vertexes_low[i][0] - vertexes_bottom[i][0])/2, vertexes_bottom[i][1] + (vertexes_low[i][1] - vertexes_bottom[i][1])/2, (vertexes_low[i][2] + vertexes_bottom[i][2])/2)
            vertexes = [vertex1,vertex2,vertex3,vertex4,vertex5,vertex6,vertex1]
            pg6_bottom.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        pg6_top = []
        for i in range(5):
            vertex1=vertexes_top[i]
            vertex2=vertexes_top[i+1]
            vertex3=(vertexes_top[i+1][0] + (vertexes_high[i+1][0] - vertexes_top[i+1][0])/2, vertexes_top[i+1][1] + (vertexes_high[i+1][1] - vertexes_top[i+1][1])/2, (vertexes_high[i+1][2] + vertexes_top[i+1][2])/2)
            vertex4=((vertexes_high[i+1][0]*2 +vertexes_high[i][0])/3, (vertexes_high[i+1][1]*2 +vertexes_high[i][1])/3, height)
            vertex5=((vertexes_high[i+1][0]+vertexes_high[i][0]*2)/3, (vertexes_high[i+1][1] +vertexes_high[i][1]*2)/3, height)
            vertex6=(vertexes_top[i][0] + (vertexes_high[i][0] - vertexes_top[i][0])/2, vertexes_top[i][1] + (vertexes_high[i][1] - vertexes_top[i][1])/2, (vertexes_high[i][2] + vertexes_top[i][2])/2)
            vertexes = [vertex1,vertex2,vertex3,vertex4, vertex5,vertex6,vertex1]
            pg6_top.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        pg6_low = []
        for i in range(5):
            vertex1 = pg6_bottom[i][3]
            vertex2 = pg6_bottom[i][4]
            vertex3 = ((vertexes_low[i][0]*2 + vertexes_high[i+1][0])/3,(vertexes_low[i][1]*2 + vertexes_high[i+1][1])/3, (vertexes_low[i][2]*2 + vertexes_high[i+1][2])/3)
            vertex4 = ((vertexes_low[i][0] + vertexes_high[i+1][0]*2)/3,(vertexes_low[i][1] + vertexes_high[i+1][1]*2)/3, (vertexes_low[i][2] + vertexes_high[i+1][2]*2)/3)
            vertex5 = ((vertexes_low[i+1][0] + vertexes_high[i+1][0]*2)/3,(vertexes_low[i+1][1] + vertexes_high[i+1][1]*2)/3, (vertexes_low[i+1][2] + vertexes_high[i+1][2]*2)/3)
            vertex6 = ((vertexes_low[i+1][0]*2 + vertexes_high[i+1][0])/3,(vertexes_low[i+1][1]*2 + vertexes_high[i+1][1])/3, (vertexes_low[i+1][2]*2 + vertexes_high[i+1][2])/3)
            vertexes = [vertex1,vertex2,vertex3,vertex4, vertex5,vertex6,vertex1]
            pg6_low.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        pg6_high = []
        for i in range(5):
            vertex1 = pg6_top[i][3]
            vertex2 = pg6_top[i][4]
            vertex3 = pg6_low[i-1][4]
            vertex4 = pg6_low[i-1][5]
            vertex5 = pg6_low[i][2]
            vertex6 = pg6_low[i][3]
            vertexes = [vertex1,vertex2, vertex3, vertex4,vertex5,vertex6 ,vertex1]
            pg6_high.append(vertexes)
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertex1 = pg6_top[i][4]
            vertex2 = pg6_top[i][5]
            vertex3 = pg6_high[i-1][6]
            vertex4 = pg6_high[i-1][5]
            vertex5 = pg6_low[i-1][4]
            vertexes = [vertex1,vertex2, vertex3,vertex4,vertex5,vertex1]
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))

        for i in range(5):
            vertex1 = pg6_bottom[i][4]
            vertex2 = pg6_bottom[i][5]
            vertex3 = pg6_low[i-1][6]
            vertex4 = pg6_low[i-1][5]
            vertex5 = pg6_high[i][4]
            vertexes = [vertex1,vertex2, vertex3,vertex4,vertex5, vertex1]
            polygon_side=Part.makePolygon(vertexes)
            faces.append(Part.Face(polygon_side))


        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid



# ===========================================================================    

def geodesic_radius2side(radius, div):
    # approximative experience values! Not all sides are equal!
    dictsides = {"2":618.034, "3":412.41, "4":312.87,"5":245.09,"6":205.91,"7":173.53,"8":152.96,"9":135.96,"10":121.55}
    div = int(round(div))
    if div < 0:
        return 0
    if div == 1:
        return radius * 4 / math.sqrt(10 + 2 * math.sqrt(5))
    elif div <= 10:
        factor = dictsides[str(div)]
        return radius * factor / 1000

def geodesic_side2radius(side, div):
    # approximative experience values!  Not all sides are equal!
    dictsides = {"2":618.034, "3":412.41, "4":312.87,"5":245.09,"6":205.91,"7":173.53,"8":152.96,"9":135.96,"10":121.55}
    div = int(round(div))
    if div < 0:
        return 0
    if div == 1:
        return side / 4 * math.sqrt(10 + 2 * math.sqrt(5))
    elif div <= 10:
        factor = dictsides[str(div)]
        return side * 1000 / factor


# =========================================================================== 

class Geodesic_sphere:radiusvalue = 0  
    divided_by = 2


    def __init__(self, obj, radius=5, div=2):
        obj.addProperty("App::PropertyLength","Radius","Geodesic","Radius of the sphere").Radius=radius
        obj.addProperty("App::PropertyLength","Side","Geodesic","Sidelength of the triangles (approximative!)")
        obj.addProperty("App::PropertyInteger","DividedBy","Geodesic","The sides of the icosahedron are divided in x").DividedBy = div

        obj.Proxy = self
def geodesic_divide_triangles(self,vertex1, vertex2, vertex3, faces):
        
        vector1 = (Base.Vector(vertex2) - Base.Vector(vertex1)) / self.divided_by
        vector2 = (Base.Vector(vertex3) - Base.Vector(vertex2)) / self.divided_by

        icosaPt={}
        
        icosaPt[str(1)] = Base.Vector(vertex1) 
          
        for level in range(self.divided_by):
            l1 = level + 1
            icosaPt[str(l1*10+1)] = icosaPt[str(1)]+ vector1 * (l1)

            for pt in range(level+1):
                icosaPt[str(l1*10+2+pt)] = icosaPt[str(l1*10+1)] + vector2 *(pt+1)
                    
        
        for level in range(self.divided_by):

            for point in range(level+1):
                vertex1x = icosaPt[str(level*10+1+point)].normalize().multiply(self.radiusvalue)
                vertex2x = icosaPt[str(level*10+11+point)].normalize().multiply(self.radiusvalue)
                vertex3x = icosaPt[str(level*10+12+point)].normalize().multiply(self.radiusvalue)
                polygon = Part.makePolygon([vertex1x,vertex2x,vertex3x, vertex1x])
                faces.append(Part.Face(polygon))

            for point in range(level):
                vertex1x = icosaPt[str(level*10+1+point)].normalize().multiply(self.radiusvalue)
                vertex2x = icosaPt[str(level*10+2+point)].normalize().multiply(self.radiusvalue)
                vertex3x = icosaPt[str(level*10+12+point)].normalize().multiply(self.radiusvalue)
                polygon = Part.makePolygon([vertex1x,vertex2x,vertex3x, vertex1x])
                faces.append(Part.Face(polygon))
      
        return faces

         

    def execute (self,obj):

        obj.DividedBy = int(round(obj.DividedBy))
        if obj.DividedBy <= 0:
            obj.DividedBy = 1
                    
            
        radius = float(obj.Radius)
        if radius != self.radiusvalue or obj.DividedBy != self.divided_by:
            self.divided_by = obj.DividedBy
            obj.Side = geodesic_radius2side(radius, self.divided_by)
            self.radiusvalue = radius
        else:
            self.radiusvalue = geodesic_side2radius(obj.Side,self.divided_by)
            obj.Radius = self.radiusvalue
            radius = self.radiusvalue
            
        self.divided_by = obj.DividedBy   

        z = 4*radius / math.sqrt(10 + 2 * math.sqrt(5))
        anglefaces = 138.189685104
        r = z/12 * math.sqrt(3) * (3 + math.sqrt(5))


        #radius of a pentagram with the same side
        radius2 = z / math.sin(36 * math.pi/180)/2
        
        #height of radius2 in the sphere
        angle = math.acos(radius2/radius)
        height = radius * math.sin(angle)

        faces = []

        vertex_bottom = (0,0,-radius)
        vertexes_low = horizontal_regular_polygon_vertexes(5,radius2, -height)
        vertexes_high = horizontal_regular_polygon_vertexes(5,radius2, height, math.pi/5)
        vertex_top = (0,0,radius)
        
        for i in range(5):
            faces = self.geodesic_divide_triangles(vertex_bottom,vertexes_low[i+1],vertexes_low[i],faces)

        
        for i in range(5):
            faces = self.geodesic_divide_triangles(vertexes_high[i],vertexes_low[i+1],vertexes_low[i],faces)
            faces = self.geodesic_divide_triangles(vertexes_low[i+1],vertexes_high[i+1],vertexes_high[i],faces)

        for i in range(5):
            faces = self.geodesic_divide_triangles(vertex_top,vertexes_high[i],vertexes_high[i+1],faces)

        
        shell = Part.makeShell(faces)
        solid = Part.makeSolid(shell)
        obj.Shape = solid        
 

# =========================================================================== 

class ViewProviderBox:obj_name = "polyhedron"def __init__(self, obj, obj_name):
        self.obj_name = obj_name
        obj.Proxy = self

    def attach(self, obj):
        return

    def updateData(self, fp, prop):
        return

    def getDisplayModes(self,obj):
        return "As Is"
        
    def getDefaultDisplayMode(self):
        return "As Is"

    def setDisplayMode(self,mode):
        return "As Is"

    def onChanged(self, vobj, prop):
        pass
        
    def getIcon(self):
        return """
        /* XPM */
        static char * xpm[] = {
"32 32 9 1",
"   c None",
".  c #010050",
"+  c #000641",
"@  c #04036A",
"#  c #00019A",
"$  c #272687",
"%  c #3E3EA2",
"&  c #4C4BBF",
"*  c #6466FC",
"                                ",
"                                ",
"                                ",
"              @###@$%           ",
"           @#####@&**&          ",
"         @#####@&******%        ",
"       @#####@%*********%       ",
"      @###@@$%***********&      ",
"     +@@$****%*************     ",
"     &********&************&    ",
"     *********%************$+   ",
"     *********&************+.   ",
"    %**********%***********+.+  ",
"    &**********%**********%..+  ",
"    &***********&*********+..   ",
"    &***********%&********+..   ",
"    ***********&@#@@$$%&&*+..   ",
"    ***********@#########+..+   ",
"    **********$##########...+   ",
"    +********%###########...+   ",
"    ++$*****&############...+   ",
"    +..+&***@############...    ",
"     +..++*$#############..+    ",
"      +...+@#############..     ",
"       +...+@############.+     ",
"         ...+@##########@       ",
"          +..+@#######@         ",
"           +..+@####@           ",
"            ++++.@.             ",
"                                ",
"                                ",
"                                "};
        """
        
    def __getstate__(self):
        return None

    def __setstate__(self,state):
        return None
        
        
# ===========================================================================  

def msgbox(s):
    msg = QtGui.QMessageBox()
    msg.setIcon(QtGui.QMessageBox.Information)
    msg.setText(s)
    msg.setWindowTitle("Message")
    msg.setStandardButtons(QtGui.QMessageBox.Ok )
    retval = msg.exec_()


# =========================================================================== 



class polyhedron_dialog(QtGui.QWidget):polyhedronname = ""

    def __init__(self):
        super(polyhedron_dialog, self).__init__()

        self.initUI()

    def initUI(self):
        grid = QtGui.QGridLayout()

        button = QtGui.QPushButton('Cancel')
        button.setStyleSheet("color:blue")
        grid.addWidget(button, 10, 3)
        button.clicked.connect(self.cancel_method)
        button2 = QtGui.QPushButton('OK')
        button2.setStyleSheet("color:blue")
        grid.addWidget(button2, 10, 5)
        button2.clicked.connect(self.slot_method)

        self.listBox = QtGui.QListWidget(self)
        grid.addWidget(self.listBox, 0, 3)
        self.listBox.addItem("tetrahedron")
        self.listBox.addItem("hexahedron")
        self.listBox.addItem("octahedron")
        self.listBox.addItem("dodecahedron")
        self.listBox.addItem("icosahedron")
        self.listBox.addItem("icosahedron-truncated")
        self.listBox.addItem("geodesic-sphere")
        self.listBox.itemClicked.connect(self.listwidgetclicked)

        grid.addWidget(QtGui.QLabel('radius :'), 3, 2)
        self.radius = QtGui.QLineEdit("5")
        self.radius.setStyleSheet("background : white; font-weight:bold; padding-left:10px")
        grid.addWidget(self.radius,3,3)

        grid.addWidget(QtGui.QLabel('or sidelength:'), 3, 4)
        self.side = QtGui.QLineEdit()
        self.side.setStyleSheet("background : white; font-weight:bold; padding-left:10px")
        grid.addWidget(self.side, 3,5)

        self.warning = QtGui.QLineEdit()
        self.warning.setStyleSheet("color : red")
        grid.addWidget(self.warning, 5,3)


        self.setLayout(grid)
        self.move(500, 350)
        self.setWindowTitle('Polyhedrons as FreeCad-Part')
        self.show()def listwidgetclicked(self, item):
        self.polyhedronname = format(item.text())
        self.warning.clear()


    def slot_method(self):
        if self.listBox.selectedItems() == []:
            self.warning.setText("Select a type!")
            return


        if (str(self.radius.text()))== "":
            radius = 0
        else:
            radius = float(str(self.radius.text()))

        if (str(self.side.text()))== "":
            side = 0
        else:
            side = float(str(self.side.text()))

        if radius == 0 and side == 0 :
            self.warning.setText("INPUT ERROR! No radius nor side!")
            return    
            
        if radius != 0 and side != 0 :
            self.warning.setText("INPUT ERROR! Only One value allowed!")
            return
        else :   
            if FreeCAD.ActiveDocument == None:
                FreeCAD.newDocument() 
                      
            obj=FreeCAD.ActiveDocument.addObject("Part::FeaturePython",self.listBox.currentItem().text())

            if self.listBox.currentItem().text() == "tetrahedron":
                if radius==0:
                    radius = side / 4 * math.sqrt(6)
                Tetrahedron(obj, radius)
            elif self.listBox.currentItem().text() == "hexahedron":
                if radius == 0:
                    radius = side * 2 / math.sqrt(3)
                Hexahedron(obj, radius)
            elif self.listBox.currentItem().text() == "octahedron":
                if radius == 0:
                    radius = side / math.sqrt(2)
                Octahedron(obj, radius)
            elif self.listBox.currentItem().text() == "dodecahedron":
                if radius == 0:
                    radius = side / 4 *  math.sqrt(3) * (1 + math.sqrt(5))
                Dodecahedron(obj, radius)
            elif self.listBox.currentItem().text() == "icosahedron":
                if radius == 0:
                    radius = side / 4 * math.sqrt(10 + 2 * math.sqrt(5))
                Icosahedron(obj, radius)
            elif self.listBox.currentItem().text() == "icosahedron-truncated":
                if radius == 0:
                    radius = side / 4 * math.sqrt(10 + 2 * math.sqrt(5)) * 3
                Icosahedron_truncated(obj,radius)
            elif self.listBox.currentItem().text() == "geodesic-sphere":
                if radius == 0:
                    radius = side / 2 * math.sqrt(10 + 2 * math.sqrt(5))
                Geodesic_sphere(obj,radius)  
                                  
            obj.ViewObject.Proxy=0
            ViewProviderBox(obj.ViewObject, self.listBox.item)
            FreeCAD.ActiveDocument.recompute()
            FreeCADGui.SendMsgToActiveView("ViewFit")                

        self.close()

    def cancel_method(self):
        self.close()


mainaction = polyhedron_dialog()


}}

---
[documentation index](../README.md) > Macro Polyhedrons
