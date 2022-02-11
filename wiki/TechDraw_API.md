# TechDraw API

This is a module for making drawings



#### <img src="images/type_method.svg" style="width:16px;"> edgeWalker

[wires] = edgeWalker(edgePile,inclBiggest) -- Planar graph traversal finds wires in edge pile.



#### <img src="images/type_method.svg" style="width:16px;"> findCentroid

vector = findCentroid(shape,direction): finds geometric centroid of shape looking in direction.



#### <img src="images/type_method.svg" style="width:16px;"> findOuterWire

wire = findOuterWire(edgeList) -- Planar graph traversal finds OuterWire in edge pile.



#### <img src="images/type_method.svg" style="width:16px;"> findShapeOutline

wire = findShapeOutline(shape,scale,direction) -- Project shape in direction and find outer wire of result.



#### <img src="images/type_method.svg" style="width:16px;"> makeDistanceDim

makeDistanceDim(DrawViewPart, dimType, fromPoint, toPoint) -- draw a Length dimension between fromPoint to toPoint.  FromPoint and toPoint are unscaled 2d View points. dimType is one of ['Distance', 'DistanceX', 'DistanceY'.



#### <img src="images/type_method.svg" style="width:16px;"> makeDistanceDim3d

makeDistanceDim(DrawViewPart, dimType, 3dFromPoint, 3dToPoint) -- draw a Length dimension between fromPoint to toPoint.  FromPoint and toPoint are unscaled 3d model points. dimType is one of ['Distance', 'DistanceX', 'DistanceY'.



#### <img src="images/type_method.svg" style="width:16px;"> makeExtentDim

makeExtentDim(DrawViewPart, [edges], direction) -- draw horizontal or vertical extent dimension for edges (or all of DrawViewPart if edge list is empty. direction:  0 - Horizontal, 1 - Vertical.



#### <img src="images/type_method.svg" style="width:16px;"> makeGeomHatch

makeGeomHatch(face, [patScale], [patName], [patFile]) -- draw a geom hatch on a given face, using optionally the given scale (default 1) and a given pattern name (ex. Diamond) and .pat file (the default pattern name and/or .pat files set in preferences are used if none are given). Returns a Part compound shape.



#### <img src="images/type_method.svg" style="width:16px;"> project

[visiblyG0,visiblyG1,hiddenG0,hiddenG1] = project(TopoShape[,App.Vector Direction, string type])
 -- Project a shape and return the visible/invisible parts of it.



#### <img src="images/type_method.svg" style="width:16px;"> projectEx

[V,V1,VN,VO,VI,H,H1,HN,HO,HI] = projectEx(TopoShape[,App.Vector Direction, string type])
 -- Project a shape and return the all parts of it.



#### <img src="images/type_method.svg" style="width:16px;"> projectToDXF

string = projectToDXF(TopoShape[,App.Vector Direction, string type])
 -- Project a shape and return the DXF representation as string.



#### <img src="images/type_method.svg" style="width:16px;"> projectToSVG

string = projectToSVG(TopoShape[, App.Vector direction, string type, float tolerance, dict vStyle, dict v0Style, dict v1Style, dict hStyle, dict h0Style, dict h1Style])
 -- Project a shape and return the SVG representation as string.



#### <img src="images/type_method.svg" style="width:16px;"> removeSvgTags

string = removeSvgTags(string) -- Removes the opening and closing svg tags
and other metatags from a svg code, making it embeddable



#### <img src="images/type_method.svg" style="width:16px;"> viewPartAsDxf

string = viewPartAsDxf(DrawViewPart) -- Return the edges of a DrawViewPart in Dxf format.



#### <img src="images/type_method.svg" style="width:16px;"> viewPartAsSvg

string = viewPartAsSvg(DrawViewPart) -- Return the edges of a DrawViewPart in Svg format.



#### <img src="images/type_method.svg" style="width:16px;"> writeDXFPage

writeDXFPage(page,filename): Exports a DrawPage to a DXF file.



#### <img src="images/type_method.svg" style="width:16px;"> writeDXFView

writeDXFView(view,filename): Exports a DrawViewPart to a DXF file.









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw API
