# Arch API

This page is an auto-generated Python API documentation, including variables, classes and functions for module Arch




### Functions

#### <img src="images/type_method.svg" style="width:16px;"> CalculatePlacement <small>(baramount, barnumber, bardiameter, size, axis, rotation, offsetstart, offsetend, RebarShape='')</small>

Calculate the placement of the bar from given values.



#### <img src="images/type_method.svg" style="width:16px;"> CustomSpacingPlacement <small>(spacinglist, barnumber, axis, rotation, offsetstart, offsetend)</small>

Calculate placement of the bar from custom spacing list.



#### <img src="images/type_method.svg" style="width:16px;"> QT_TRANSLATE_NOOP <small>(ctxt, txt)</small>





#### <img src="images/type_method.svg" style="width:16px;"> addComponents <small>(objectsList, host)</small>

adds the given object or the objects
    from the given list as components to the given host Object. Use this for
    example to add windows to a wall, or to add walls to a cell or floor.



#### <img src="images/type_method.svg" style="width:16px;"> addSpaceBoundaries <small>(space, subobjects)</small>

adds the given subobjects to the given space



#### <img src="images/type_method.svg" style="width:16px;"> adjust_list_len <small>(lst, newLn, val)</small>

Returns a clone of lst with length newLn, val is appended if required



#### <img src="images/type_method.svg" style="width:16px;"> areSameWallTypes <small>(walls)</small>

Check if a list of walls have the same height, width and alignment.

    Parameters
     
    walls: list of <ArchComponent.Component>

    Returns
     
    bool
        True if the walls have the same height, width and alignment, False if
        otherwise.



#### <img src="images/type_method.svg" style="width:16px;"> check <small>(objectslist, includehidden=False)</small>

checks if the given objects contain only solids



#### <img src="images/type_method.svg" style="width:16px;"> cleanArchSplitter <small>(objects=None)</small>

removes the splitters from the base shapes
    of the given Arch objects or selected Arch objects if objects is None



#### <img src="images/type_method.svg" style="width:16px;"> cloneComponent <small>(obj)</small>

Creates a clone of an object as an undefined component



#### <img src="images/type_method.svg" style="width:16px;"> closeHole <small>(shape)</small>

closes a hole in an open shape



#### <img src="images/type_method.svg" style="width:16px;"> closeViewer <small>(name)</small>

Close temporary viewers



#### <img src="images/type_method.svg" style="width:16px;"> convertFloors <small>(floor=None)</small>

convert the given Floor or Building (or all Arch Floors from the active document if none is given) into BuildingParts



#### <img src="images/type_method.svg" style="width:16px;"> copyProperties <small>(obj1, obj2)</small>

Copies properties values from obj1 to obj2,
    when that property exists in both objects



#### <img src="images/type_method.svg" style="width:16px;"> createMeshView <small>(obj, direction=Vector (0.0, 0.0, -1.0), outeronly=False, largestonly=False)</small>

creates a flat shape that is the
    projection of the given mesh object in the given direction (default = on the XY plane). If
    outeronly is True, only the outer contour is taken into consideration, discarding the inner
    holes. If largestonly is True, only the largest segment of the given mesh will be used.



#### <img src="images/type_method.svg" style="width:16px;"> cutComponentwithPlane <small>(archObject, cutPlane, sideFace)</small>

cut object from a plan define by a face, Behind = 0 , front = 1



#### <img src="images/type_method.svg" style="width:16px;"> download <small>(url, force=False)</small>

downloads a file from the given URL and saves it in the
    macro path. Returns the path to the saved file. If force is True, the file will be
    downloaded again evn if it already exists.



#### <img src="images/type_method.svg" style="width:16px;"> face_from_points <small>(ptLst)</small>





#### <img src="images/type_method.svg" style="width:16px;"> find_inters <small>(edge1, edge2, infinite1=True, infinite2=True)</small>

Future wrapper for DraftGeomUtils.findIntersection. The function now
    contains a modified copy of getLineIntersections from that function.



#### <img src="images/type_method.svg" style="width:16px;"> getAllChildren <small>(objectlist)</small>

returns all the children of all the object sin the list



#### <img src="images/type_method.svg" style="width:16px;"> getCameraData <small>(floatlist)</small>

reconstructs a valid camera data string from stored values



#### <img src="images/type_method.svg" style="width:16px;"> getCoinSVG <small>(cutplane, objs, cameradata=None, linewidth=0.2, singleface=False, facecolor=None)</small>

Returns an SVG fragment generated from a coin view



#### <img src="images/type_method.svg" style="width:16px;"> getCutShapes <small>(objs, cutplane, onlySolids, clip, joinArch, showHidden, groupSshapesByObject=False)</small>

returns a list of shapes (visible, hidden, cut lines...)
    obtained from performing a series of booleans against the given cut plane



#### <img src="images/type_method.svg" style="width:16px;"> getCutVolume <small>(cutplane, shapes, clip=False, depth=None)</small>

returns a cut face and a cut volume
    from the given shapes and the given cutting plane. If clip is True, the cutvolume will
    also cut off everything outside the cutplane projection. If depth is non-zero, geometry
    further than this distance will be clipped off



#### <img src="images/type_method.svg" style="width:16px;"> getDXF <small>(obj)</small>

Return a DXF representation from a TechDraw/Drawing view.



#### <img src="images/type_method.svg" style="width:16px;"> getDefaultColor <small>(objectType)</small>

returns a color value for the given object
    type (Wall, Structure, Window, WindowGlass)



#### <img src="images/type_method.svg" style="width:16px;"> getDocumentMaterials <small>()</small>

returns all the arch materials of the document



#### <img src="images/type_method.svg" style="width:16px;"> getExtrusionData <small>(shape, sortmethod='area')</small>

If a shape has been extruded, returns the base face, and extrusion vector.

    Determines if a shape appears to have been extruded from some base face, and
    extruded at the normal from that base face. IE: it looks like a cuboid.
    https://en.wikipedia.org/wiki/Cuboid#Rectangular_cuboid

    If this is the case, returns what appears to be the base face, and the vector
    used to make that extrusion.

    The base face is determined based on the sortmethod parameter, which can either
    be:

    "area" = Of the faces with the smallest area, the one with the lowest z coordinate.
    "z" = The face with the lowest z coordinate.
    a 3D vector = the face which center is closest to the given 3D point

    Parameters
     
    shape: <Part.Shape>
        Shape to examine.
    sortmethod: {"area", "z"}
        Which sorting algorithm to use to determine the base face.

    Returns
     
    Extrusion data: list
        Two item list containing the base face, and the vector used to create the
        extrusion. In that order.
    Failure: None
        Returns None if the object does not appear to be an extrusion.



#### <img src="images/type_method.svg" style="width:16px;"> getFillForObject <small>(o, defaultFill, source)</small>

returns a color tuple from an object's material



#### <img src="images/type_method.svg" style="width:16px;"> getHost <small>(obj, strict=True)</small>

returns the host of the current object. If strict is true (default),
    the host can only be an object of a higher level than the given one, or in other words, if a wall
    is contained in another wall which is part of a floor, the floor is returned instead of the parent wall



#### <img src="images/type_method.svg" style="width:16px;"> getLengthOfRebar <small>(rebar)</small>

Calculates the length of the rebar.



#### <img src="images/type_method.svg" style="width:16px;"> getMaterialContainer <small>()</small>

returns a group object to put materials in



#### <img src="images/type_method.svg" style="width:16px;"> getPlanWithLine <small>(line)</small>

Function to make a plane along Normal plan



#### <img src="images/type_method.svg" style="width:16px;"> getSVG <small>(source, renderMode='Wireframe', allOn=False, showHidden=False, scale=1, rotation=0, linewidth=1, lineColor=(0.0, 0.0, 0.0), fontsize=1, showFill=False, fillColor=(1.0, 1.0, 1.0), techdraw=False, fillSpaces=False, cutlinewidth=0, joinArch=False)</small>

Return an SVG fragment from an Arch SectionPlane or BuildingPart.

    allOn
        If it is `True`, all cut objects are shown, regardless of if they are
        visible or not.

    renderMode
        Can be `'Wireframe'` (default) or `'Solid'` to use the Arch solid
        renderer.

    showHidden
        If it is `True`, the hidden geometry above the section plane
        is shown in dashed line.

    showFill
        If it is `True`, the cut areas get filled with a pattern.

    lineColor
        Color of lines for the `renderMode` is `'Wireframe'`.

    fillColor
        If `showFill` is `True` and `renderMode` is `'Wireframe'`,
        the cut areas are filled with `fillColor`.

    fillSpaces
        If `True`, shows space objects as filled surfaces.



#### <img src="images/type_method.svg" style="width:16px;"> getSectionData <small>(source)</small>

Returns some common data from section planes and building parts



#### <img src="images/type_method.svg" style="width:16px;"> getShapeFromMesh <small>(mesh, fast=True, tolerance=0.001, flat=False, cut=True)</small>





#### <img src="images/type_method.svg" style="width:16px;"> getStringList <small>(objects)</small>

returns a string defining a list
    of objects



#### <img src="images/type_method.svg" style="width:16px;"> hide <small>(obj)</small>





#### <img src="images/type_method.svg" style="width:16px;"> isOriented <small>(obj, plane)</small>

determines if an annotation is facing the cutplane or not



#### <img src="images/type_method.svg" style="width:16px;"> joinWalls <small>(walls, delete=False)</small>

Join the given list of walls into one sketch-based wall.

    Take the first wall in the list, and adds on the other walls in the list.
    Return the modified first wall.

    Setting delete to True, will delete the other walls. Only join walls
    if the walls have the same width, height and alignment.

    Parameters
     
    walls: list of <Part::FeaturePython>
        List containing the walls to add to the first wall in the list. Walls must
        be based off a base object.
    delete: bool, optional
        If True, deletes the other walls in the list.

    Returns
     
    <Part::FeaturePython>



#### <img src="images/type_method.svg" style="width:16px;"> looksLikeDraft <small>(o)</small>

Does this object look like a Draft shape? (flat, no solid, etc)



#### <img src="images/type_method.svg" style="width:16px;"> makeAxis <small>(num=5, size=1000, name='Axes')</small>

makes an Axis set
    based on the given number of axes and interval distances



#### <img src="images/type_method.svg" style="width:16px;"> makeAxisSystem <small>(axes, name='Axis System')</small>

makes a system from the given list of axes



#### <img src="images/type_method.svg" style="width:16px;"> makeBuilding <small>(objectslist=None, baseobj=None, name='Building')</small>

overwrites ArchBuilding.makeBuilding



#### <img src="images/type_method.svg" style="width:16px;"> makeBuildingPart <small>(objectslist=None, baseobj=None, name='BuildingPart')</small>

creates a buildingPart including the
    objects from the given list.



#### <img src="images/type_method.svg" style="width:16px;"> makeComponent <small>(baseobj=None, name='Component', delete=False)</small>

creates an undefined, non-parametric Arch
    component from the given base object



#### <img src="images/type_method.svg" style="width:16px;"> makeCompoundFromSelected <small>(objects=None)</small>

Creates a new compound object from the given
    subobjects (faces, edges) or from the selection if objects is None



#### <img src="images/type_method.svg" style="width:16px;"> makeCurtainWall <small>(baseobj=None, name='Curtain Wall')</small>

Creates a curtain wall in the active document



#### <img src="images/type_method.svg" style="width:16px;"> makeEquipment <small>(baseobj=None, placement=None, name='Equipment')</small>

creates an equipment object from the given base object.



#### <img src="images/type_method.svg" style="width:16px;"> makeFace <small>(wires, method=2, cleanup=False)</small>

makes a face from a list of wires, finding which ones are holes



#### <img src="images/type_method.svg" style="width:16px;"> makeFence <small>(section, post, path)</small>





#### <img src="images/type_method.svg" style="width:16px;"> makeFloor <small>(objectslist=None, baseobj=None, name='Floor')</small>

overwrites ArchFloor.makeFloor



#### <img src="images/type_method.svg" style="width:16px;"> makeFrame <small>(baseobj, profile, name='Frame')</small>

creates a frame object from a base sketch (or any other object
    containing wires) and a profile object (an extrudable 2D object containing faces or closed wires)



#### <img src="images/type_method.svg" style="width:16px;"> makeGrid <small>(name='Grid')</small>

makes a grid object



#### <img src="images/type_method.svg" style="width:16px;"> makeIfcSpreadsheet <small>(archobj=None)</small>





#### <img src="images/type_method.svg" style="width:16px;"> makeMaterial <small>(name='Material', color=None, transparency=None)</small>

makes an Material object



#### <img src="images/type_method.svg" style="width:16px;"> makeMultiMaterial <small>(name='MultiMaterial')</small>

makes an Material object



#### <img src="images/type_method.svg" style="width:16px;"> makePanel <small>(baseobj=None, length=0, width=0, thickness=0, placement=None, name='Panel')</small>

creates a
    panel element based on the given profile object and the given
    extrusion thickness. If no base object is given, you can also specify
    length and width for a simple cubic object.



#### <img src="images/type_method.svg" style="width:16px;"> makePanelCut <small>(panel, name='PanelView')</small>

Creates a 2D view of the given panel
    in the 3D space, positioned at the origin.



#### <img src="images/type_method.svg" style="width:16px;"> makePanelSheet <small>(panels=[], name='PanelSheet')</small>

Creates a sheet with the given panel cuts
    in the 3D space, positioned at the origin.



#### <img src="images/type_method.svg" style="width:16px;"> makePanelView <small>(panel, page=None, name='PanelView')</small>

Creates a Drawing view of the given panel
    in the given or active Page object (a new page will be created if none exists).



#### <img src="images/type_method.svg" style="width:16px;"> makePipe <small>(baseobj=None, diameter=0, length=0, placement=None, name='Pipe')</small>

creates an pipe object from the given base object



#### <img src="images/type_method.svg" style="width:16px;"> makePipeConnector <small>(pipes, radius=0, name='Connector')</small>

creates a connector between the given pipes



#### <img src="images/type_method.svg" style="width:16px;"> makePrecast <small>(precasttype=None, length=0, width=0, height=0, slabtype='', chamfer=0, dentlength=0, dentwidth=0, dentheight=0, dents=[], base=0, holenumber=0, holemajor=0, holeminor=0, holespacing=0, groovenumber=0, groovedepth=0, grooveheight=0, groovespacing=0, risernumber=0, downlength=0, riser=0, tread=0)</small>

Creates one of the precast objects in the current document



#### <img src="images/type_method.svg" style="width:16px;"> makeProfile <small>(profile=[0, 'REC', 'REC100x100', 'R', 100, 100])</small>

returns a shape  with the face defined by the profile data



#### <img src="images/type_method.svg" style="width:16px;"> makeProject <small>(sites=None, name='Project')</small>

Create an Arch project.

    If sites are provided, add them as children of the new project.

    Parameters
     
    sites: list of <Part::FeaturePython>, optional
        Sites to add as children of the project. Ultimately this could be
        anything, however.
    name: str, optional
        The label for the project.

    Returns
     
    <Part::FeaturePython>
        The created project.



#### <img src="images/type_method.svg" style="width:16px;"> makeRailing <small>(stairs)</small>

simple make Railing function testing



#### <img src="images/type_method.svg" style="width:16px;"> makeRebar <small>(baseobj=None, sketch=None, diameter=None, amount=1, offset=None, name='Rebar')</small>

adds a Reinforcement Bar object
    to the given structural object, using the given sketch as profile.



#### <img src="images/type_method.svg" style="width:16px;"> makeReference <small>(filepath=None, partname=None, name='External Reference')</small>

Creates an Arch Reference object



#### <img src="images/type_method.svg" style="width:16px;"> makeRoof <small>(baseobj=None, facenr=0, angles=[45.0], run=[250.0], idrel=[-1], thickness=[50.0], overhang=[100.0], name='Roof')</small>

Makes a roof based on
    a closed wire or an object.

    You can provide a list of angles, run, idrel, thickness, overhang for
    each edge in the wire to define the roof shape. The default for angle is
    45 and the list is automatically completed to match the number of edges
    in the wire.

    If the base object is a solid the roof uses its shape.



#### <img src="images/type_method.svg" style="width:16px;"> makeSectionPlane <small>(objectslist=None, name='Section')</small>

Creates a Section plane objects including the
    given objects. If no object is given, the whole document will be considered.



#### <img src="images/type_method.svg" style="width:16px;"> makeSectionView <small>(section, name='View')</small>

OBSOLETE
    makeSectionView(section) : Creates a Drawing view of the given Section Plane
    in the active Page object (a new page will be created if none exists



#### <img src="images/type_method.svg" style="width:16px;"> makeSite <small>(objectslist=None, baseobj=None, name='Site')</small>

makeBuilding(objectslist): creates a site including the
    objects from the given list.



#### <img src="images/type_method.svg" style="width:16px;"> makeSolarDiagram <small>(longitude, latitude, scale=1, complete=False, tz=None)</small>

returns a solar diagram as a pivy node. If complete is
    True, the 12 months are drawn. Tz is the timezone related to
    UTC (ex: -3 = UTC-3)



#### <img src="images/type_method.svg" style="width:16px;"> makeSpace <small>(objects=None, baseobj=None, name='Space')</small>

Creates a space object from the given objects. Objects can be one
    document object, in which case it becomes the base shape of the space object, or a list of
    selection objects as got from getSelectionEx(), or a list of tuples (object, subobjectname)



#### <img src="images/type_method.svg" style="width:16px;"> makeStairs <small>(baseobj=None, length=None, width=None, height=None, steps=None, name='Stairs')</small>

creates a Stairs
    objects with given attributes.



#### <img src="images/type_method.svg" style="width:16px;"> makeStructuralSystem <small>(objects=[], axes=[], name='StructuralSystem')</small>

makes a structural system
    based on the given objects and axes



#### <img src="images/type_method.svg" style="width:16px;"> makeStructure <small>(baseobj=None, length=None, width=None, height=None, name='Structure')</small>

creates a
    structure element based on the given profile object and the given
    extrusion height. If no base object is given, you can also specify
    length and width for a cubic object.



#### <img src="images/type_method.svg" style="width:16px;"> makeTruss <small>(baseobj=None, name='Truss')</small>

Creates a space object from the given object (a line)



#### <img src="images/type_method.svg" style="width:16px;"> makeWall <small>(baseobj=None, height=None, length=None, width=None, align=None, face=None, name=None)</small>

Create a wall based on a given object, and returns the generated wall.

    TODO: It is unclear what defines which units this function uses.

    Parameters
     
    baseobj: <Part::PartFeature>, optional
        The base object with which to build the wall. This can be a sketch, a
        draft object, a face, or a solid. It can also be left as None.
    height: float, optional
        The height of the wall.
    length: float, optional
        The length of the wall. Not used if the wall is based off an object.
        Will use Arch default if left empty.
    width: float, optional
        The width of the wall. Not used if the base object is a face.  Will use
        Arch default if left empty.
    align: str, optional
        Either "Center", "Left", or "Right". Effects the alignment of the wall
        on its baseline.
    face: int, optional
        The index number of a face on the given baseobj, to base the wall on.
    name: str, optional
        The name to give to the created wall.

    Returns
     
    <Part::FeaturePython>
        Returns the generated wall.

    Notes
     
    Creates a new <Part::FeaturePython> object, and turns it into a parametric wall
    object. This <Part::FeaturePython> object does not yet have any shape.

    The wall then uses the baseobj.Shape as the basis to extrude out a wall shape,
    giving the new <Part::FeaturePython> object a shape.

    It then hides the original baseobj.



#### <img src="images/type_method.svg" style="width:16px;"> makeWindRose <small>(epwfile, scale=1, sectors=24)</small>

returns a wind rose diagram as a pivy node



#### <img src="images/type_method.svg" style="width:16px;"> makeWindow <small>(baseobj=None, width=None, height=None, parts=None, name=None)</small>

creates a window based on the
    given base 2D object (sketch or draft).



#### <img src="images/type_method.svg" style="width:16px;"> makeWindowPreset <small>(windowtype, width, height, h1, h2, h3, w1, w2, o1, o2, placement=None)</small>

makes a
    window object based on the given data. windowtype must be one of the names
    defined in Arch.WindowPresets



#### <img src="images/type_method.svg" style="width:16px;"> mergeCells <small>(objectslist)</small>

merges the objects in the given list
    into one. All objects must be of the same type and based on the Cell
    object (cells, floors, buildings, or sites).



#### <img src="images/type_method.svg" style="width:16px;"> mergeShapes <small>(w1, w2)</small>

Not currently implemented.

    Return a Shape built on two walls that share same properties and have a
    coincident endpoint.



#### <img src="images/type_method.svg" style="width:16px;"> meshToShape <small>(obj, mark=True, fast=True, tol=0.001, flat=False, cut=True)</small>

turns a mesh into a shape, joining coplanar facets. If
    mark is True (default), non-solid objects will be marked in red. Fast uses a faster algorithm by
    building a shell from the facets then removing splitter, tol is the tolerance used when converting
    mesh segments to wires, flat will force the wires to be perfectly planar, to be sure they can be
    turned into faces, but this might leave gaps in the final shell. If cut is true, holes in faces are
    made by subtraction (default)



#### <img src="images/type_method.svg" style="width:16px;"> placeAlongEdge <small>(p1, p2, horizontal=False)</small>

returns a Placement positioned at p1, with Z axis oriented towards p2.
    If horizontal is True, then the X axis is oriented towards p2, not the Z axis



#### <img src="images/type_method.svg" style="width:16px;"> printMessage <small>(message)</small>





#### <img src="images/type_method.svg" style="width:16px;"> printWarning <small>(message)</small>





#### <img src="images/type_method.svg" style="width:16px;"> projectToVector <small>(shape, vector)</small>

projects the given shape on the given
    vector



#### <img src="images/type_method.svg" style="width:16px;"> pruneIncluded <small>(objectslist, strict=False)</small>

removes from a list of Arch objects, those that are subcomponents of
    another shape-based object, leaving only the top-level shapes. If strict is True, the object
    is removed only if the parent is also part of the selection.



#### <img src="images/type_method.svg" style="width:16px;"> readPresets <small>()</small>





#### <img src="images/type_method.svg" style="width:16px;"> rebuildArchShape <small>(objects=None)</small>

takes the faces from the base shape of the given (or selected
    if objects is None) Arch objects, and tries to rebuild a valid solid from them.



#### <img src="images/type_method.svg" style="width:16px;"> recolorize <small>(attr)</small>

Recolorizes an object or a [documentname,objectname] list
    This basically calls the Proxy.colorize(obj) methods of objects that
    have one.



#### <img src="images/type_method.svg" style="width:16px;"> removeComponents <small>(objectsList, host=None)</small>

removes the given component or
    the components from the given list from their parents. If a host object is
    specified, this function will try adding the components as holes to the host
    object instead.



#### <img src="images/type_method.svg" style="width:16px;"> removeCurves <small>(shape, dae=False, tolerance=5)</small>

replaces curved faces in a shape
    with faceted segments. If dae is True, DAE triangulation options are used



#### <img src="images/type_method.svg" style="width:16px;"> removeShape <small>(objs, mark=True)</small>

takes an arch object (wall or structure) built on a cubic shape, and removes
    the inner shape, keeping its length, width and height as parameters. If mark is True, objects that cannot
    be processed by this function will become red.



#### <img src="images/type_method.svg" style="width:16px;"> removeSpaceBoundaries <small>(space, objects)</small>

removes the given objects from the given spaces boundaries



#### <img src="images/type_method.svg" style="width:16px;"> setAsSubcomponent <small>(obj)</small>

Sets the given object properly to become a subcomponent (addition, subtraction)
    of an Arch component



#### <img src="images/type_method.svg" style="width:16px;"> splitMesh <small>(obj, mark=True)</small>

splits the given mesh object into separated components.
    If mark is False, nothing else is done. If True (default), non-manifold components
    will be painted in red.



#### <img src="images/type_method.svg" style="width:16px;"> strprocessOfCustomSpacing <small>(span_string)</small>

This function take input
    in specific syntax and return output in the form of list. For eg.
    Input: "3@100+2@200+3@100"
    Output: [100, 100, 100, 200, 200, 100, 100, 100]



#### <img src="images/type_method.svg" style="width:16px;"> survey <small>(callback=False)</small>

starts survey mode, where you can click edges and faces to get their lengths or area.
    Clicking on no object (on an empty area) resets the count.



#### <img src="images/type_method.svg" style="width:16px;"> toNode <small>(shape)</small>

builds a linear pivy node from a shape



#### <img src="images/type_method.svg" style="width:16px;"> toggleIfcBrepFlag <small>(obj)</small>

toggles the IFC brep flag of the given object, forcing it
    to be exported as brep geometry or not.



#### <img src="images/type_method.svg" style="width:16px;"> translate <small>(ctxt, txt)</small>





#### <img src="images/type_method.svg" style="width:16px;"> update_svg_cache <small>(source, renderMode, showHidden, showFill, fillSpaces, joinArch, allOn, objs)</small>

Returns None or cached SVG, clears shape cache if required



#### <img src="images/Type_enum.svg" style="width:16px;"> ANGLETOLERANCE

Convert a string or number to a floating point number, if possible.



#### <img src="images/Type_enum.svg" style="width:16px;"> AllowedHosts

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> ArchGrid <small>(obj)</small>

The Grid object



#### <img src="images/Type_enum.svg" style="width:16px;"> ArchGridTaskPanel <small>(obj)</small>

A TaskPanel for the Arch Grid



#### <img src="images/Type_enum.svg" style="width:16px;"> ArchReference <small>(obj)</small>

The Arch Reference object



#### <img src="images/Type_enum.svg" style="width:16px;"> ArchReferenceCommand <small>()</small>

the Arch Reference command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> ArchReferenceTaskPanel <small>(obj)</small>

The editmode TaskPanel for Reference objects



#### <img src="images/Type_enum.svg" style="width:16px;"> ArchScheduleTaskPanel <small>(obj=None)</small>

The editmode TaskPanel for Schedules



#### <img src="images/Type_enum.svg" style="width:16px;"> Arch_Profile <small>()</small>

The FreeCAD Arch_Profile command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> AxisSystemTaskPanel <small>(obj)</small>

A TaskPanel for all the section plane object



#### <img src="images/Type_enum.svg" style="width:16px;"> BuildingPart <small>(obj)</small>

The BuildingPart object



#### <img src="images/Type_enum.svg" style="width:16px;"> BuildingTypes

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> COMPASS_POINTER_LENGTH

int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4



#### <img src="images/Type_enum.svg" style="width:16px;"> COMPASS_POINTER_WIDTH

int([x]) -> integer
int(x, base=10) -> integer

Convert a number or string to an integer, or return 0 if no arguments
are given.  If x is a number, return x.__int__().  For floating point
numbers, this truncates towards zero.

If x is not a number or if base is given, then x must be a string,
bytes, or bytearray instance representing an integer literal in the
given base.  The literal can be preceded by '+' or '-' and be surrounded
by whitespace.  The base defaults to 10.  Valid bases are 0 and 2-36.
Base 0 means to interpret the base from the string as an integer literal.
>>> int('0b100', base=0)
4



#### <img src="images/Type_enum.svg" style="width:16px;"> Categories

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandArchCurtainWall <small>()</small>

the Arch Curtain Wall command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandArchGrid <small>()</small>

the Arch Grid command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandArchSchedule <small>()</small>

the Arch Schedule command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandArchTruss <small>()</small>

the Arch Truss command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandBuildingPart <small>()</small>

the Arch BuildingPart command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandNest <small>()</small>

the Arch Panel command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandPanel <small>()</small>

the Arch Panel command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandPanelCut <small>()</small>

the Arch Panel Cut command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandPanelSheet <small>()</small>

the Arch Panel Sheet command definition



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandStructuralSystem <small>()</small>

The Arch Structural System command definition.



#### <img src="images/Type_enum.svg" style="width:16px;"> CommandStructuresFromSelection <small>()</small>

The Arch Structures from selection command definition.



#### <img src="images/Type_enum.svg" style="width:16px;"> Compass <small>()</small>





#### <img src="images/Type_enum.svg" style="width:16px;"> ConditioningTypes

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> CurtainWall <small>(obj)</small>

The curtain wall object



#### <img src="images/Type_enum.svg" style="width:16px;"> EAST

Base.Vector class.

This class represents a 3D float vector.
Useful to represent points in the 3D space.

The following constructors are supported:

Vector(x=0, y=0, z=0)
x : float
y : float
z : float

Vector(vector)
Copy constructor.
vector : Base.Vector

Vector(seq)
Define from a sequence of float.
seq : sequence of float.



#### <img src="images/Type_enum.svg" style="width:16px;"> ISRENDERING

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



#### <img src="images/Type_enum.svg" style="width:16px;"> NestTaskPanel <small>(obj=None)</small>

The TaskPanel for Arch Nest command



#### <img src="images/Type_enum.svg" style="width:16px;"> PanelCut <small>(obj)</small>

A flat, 2D view of an Arch Panel



#### <img src="images/Type_enum.svg" style="width:16px;"> PanelSheet <small>(obj)</small>

A collection of Panel cuts under a sheet



#### <img src="images/Type_enum.svg" style="width:16px;"> PanelView <small>(obj)</small>

A Drawing view for Arch Panels



#### <img src="images/Type_enum.svg" style="width:16px;"> Presets

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> ProfileTaskPanel <small>(obj)</small>

The editmode TaskPanel for Profile objects



#### <img src="images/Type_enum.svg" style="width:16px;"> SectionPlaneTaskPanel <small>()</small>

A TaskPanel for all the section plane object



#### <img src="images/Type_enum.svg" style="width:16px;"> SheetTaskPanel <small>(obj)</small>





#### <img src="images/Type_enum.svg" style="width:16px;"> SpaceTaskPanel <small>()</small>

A modified version of the Arch component task panel



#### <img src="images/Type_enum.svg" style="width:16px;"> SpaceTypes

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> StructSelectionObserver <small>(callback)</small>





#### <img src="images/Type_enum.svg" style="width:16px;"> StructureTaskPanel <small>(obj)</small>





#### <img src="images/Type_enum.svg" style="width:16px;"> SurveyTaskPanel <small>()</small>

A task panel for the survey tool



#### <img src="images/Type_enum.svg" style="width:16px;"> Truss <small>(obj)</small>

The truss object



#### <img src="images/Type_enum.svg" style="width:16px;"> [Vector](Vector_API.md)

Base.Vector class.

This class represents a 3D float vector.
Useful to represent points in the 3D space.

The following constructors are supported:

Vector(x=0, y=0, z=0)
x : float
y : float
z : float

Vector(vector)
Copy constructor.
vector : Base.Vector

Vector(seq)
Define from a sequence of float.
seq : sequence of float.



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderArchGrid <small>(vobj)</small>

A View Provider for the Arch Grid



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderArchReference <small>(vobj)</small>

A View Provider for the Arch Reference object



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderBuildingPart <small>(vobj)</small>

A View Provider for the BuildingPart object



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderCurtainWall <small>(vobj)</small>

A View Provider for the CurtainWall object



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderPanelCut <small>(vobj)</small>

a view provider for the panel cut object



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderPanelSheet <small>(vobj)</small>

a view provider for the panel sheet object



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderProfile <small>(vobj)</small>

General view provider for Profile classes



#### <img src="images/Type_enum.svg" style="width:16px;"> ViewProviderTruss <small>(vobj)</small>

A View Provider for the Truss object



#### <img src="images/Type_enum.svg" style="width:16px;"> WindowOpeningModes

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> WindowPartTypes

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> WindowPresets

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> pre

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> print_function





#### <img src="images/Type_enum.svg" style="width:16px;"> profilefiles

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/Type_enum.svg" style="width:16px;"> rodmodes

Built-in immutable sequence.

If no argument is given, the constructor returns an empty tuple.
If iterable is specified the tuple is initialized from iterable's items.

If the argument is a tuple, the return value is the same object.



#### <img src="images/Type_enum.svg" style="width:16px;"> unicode

str(object='') -> str
str(bytes_or_buffer[, encoding[, errors]]) -> str

Create a new string object from the given object. If encoding or
errors is specified, then the object must expose a data buffer
that will be decoded using the given encoding and error handler.
Otherwise, returns the result of object.__str__() (if defined)
or repr(object).
encoding defaults to sys.getdefaultencoding().
errors defaults to 'strict'.



#### <img src="images/Type_enum.svg" style="width:16px;"> verbose

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



#### <img src="images/Type_enum.svg" style="width:16px;"> zeroMM

Quantity
defined by a value and a unit.

The following constructors are supported:
Quantity() -- empty constructor
Quantity(Value) -- empty constructor
Quantity(Value,Unit) -- empty constructor
Quantity(Quantity) -- copy constructor
Quantity(string) -- arbitrary mixture of numbers and chars defining a Quantity



### Modules

#### <img src="images/type_module.svg" style="width:16px;"> ArchCommands





#### <img src="images/type_module.svg" style="width:16px;"> ArchComponent

This module provides the base Arch component class, that is shared
by all of the Arch BIM objects.

Examples
 
TODO put examples here.



#### <img src="images/type_module.svg" style="width:16px;"> ArchFloor

This module provides tools to build Floor objects. Floors are used to group
different Arch objects situated at a same level.

The _Floor object and this module as a whole is now obsolete. It has been
superseded by the use of the BuildingPart class, set to the "Building Storey"
IfcType.



#### <img src="images/type_module.svg" style="width:16px;"> ArchIFC

This modules sets up and manages the IFC-related properties, types
and attributes of Arch/BIM objects.



#### <img src="images/type_module.svg" style="width:16px;"> ArchIFCView

View providers and UI elements for the Ifc classes.



#### <img src="images/type_module.svg" style="width:16px;"> ArchPipe





#### <img src="images/type_module.svg" style="width:16px;"> ArchProfile





#### <img src="images/type_module.svg" style="width:16px;"> ArchWindowPresets





#### <img src="images/type_module.svg" style="width:16px;"> [Draft](Draft_API.md)

Provide the Draft Workbench public programming interface.

The Draft module offers tools to create and manipulate 2D objects.
The functions in this file must be usable without requiring the
graphical user interface.
These functions can be used as the backend for the graphical commands
defined in `DraftTools.py`.



#### <img src="images/type_module.svg" style="width:16px;"> DraftGeomUtils

Define geometry functions for manipulating shapes in the Draft Workbench.

These functions are used by different object creation functions
of the Draft Workbench, both in `Draft.py` and `DraftTools.py`.
They operate on the internal shapes (`Part::TopoShape`) of different objects
and on their subelements, that is, vertices, edges, and faces.



#### <img src="images/type_module.svg" style="width:16px;"> DraftVecUtils

Provide vector math utilities used in the Draft workbench.

Vector math utilities used primarily in the Draft workbench
but which can also be used in other workbenches and in macros.



#### <img src="images/type_module.svg" style="width:16px;"> [FreeCAD](FreeCAD_API.md)

The functions in the FreeCAD module allow working with documents.
The FreeCAD instance provides a list of references of documents which
can be addressed by a string. Hence the document name must be unique.

The document has the read-only attribute FileName which points to the
file the document should be stored to.



#### <img src="images/type_module.svg" style="width:16px;"> [Part](Part_API.md)

This is a module working with shapes.



#### <img src="images/type_module.svg" style="width:16px;"> Units

The Unit API



#### <img src="images/type_module.svg" style="width:16px;"> csv

CSV parsing and writing.

This module provides classes that assist in the reading and writing
of Comma Separated Value (CSV) files, and implements the interface
described by PEP 305.  Although many CSV files are simple to parse,
the format is not formally defined by a stable specification and
is subtle enough that parsing lines of a CSV file with something
like line.split(",") is bound to fail.  The module supports three
basic APIs: reading, writing, and registration of dialects.


DIALECT REGISTRATION:

Readers and writers support a dialect argument, which is a convenient
handle on a group of settings.  When the dialect argument is a string,
it identifies one of the dialects previously registered with the module.
If it is a class or instance, the attributes of the argument are used as
the settings for the reader or writer:

    class excel:
        delimiter = ','
        quotechar = '"'
        escapechar = None
        doublequote = True
        skipinitialspace = False
        lineterminator = '\r\n'
        quoting = QUOTE_MINIMAL

SETTINGS:

    * quotechar - specifies a one-character string to use as the
        quoting character.  It defaults to '"'.
    * delimiter - specifies a one-character string to use as the
        field separator.  It defaults to ','.
    * skipinitialspace - specifies how to interpret spaces which
        immediately follow a delimiter.  It defaults to False, which
        means that spaces immediately following a delimiter is part
        of the following field.
    * lineterminator -  specifies the character sequence which should
        terminate rows.
    * quoting - controls when quotes should be generated by the writer.
        It can take on any of the following module constants:

        csv.QUOTE_MINIMAL means only when required, for example, when a
            field contains either the quotechar or the delimiter
        csv.QUOTE_ALL means that quotes are always placed around fields.
        csv.QUOTE_NONNUMERIC means that quotes are always placed around
            fields which do not parse as integers or floating point
            numbers.
        csv.QUOTE_NONE means that quotes are never placed around fields.
    * escapechar - specifies a one-character string used to escape
        the delimiter when quoting is set to QUOTE_NONE.
    * doublequote - controls the handling of quotes inside fields.  When
        True, two consecutive quotes are interpreted as one during read,
        and when writing, each quote character embedded in the data is
        written as two quotes



#### <img src="images/type_module.svg" style="width:16px;"> datetime

Fast implementation of the datetime type.



#### <img src="images/type_module.svg" style="width:16px;"> math

This module provides access to the mathematical functions
defined by the C standard.



#### <img src="images/type_module.svg" style="width:16px;"> os

OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\r' or '\n' or '\r\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).



#### <img src="images/type_module.svg" style="width:16px;"> patharray

Provides the object code for the PathArray object.

The copies will be placed along a path like a polyline, spline, or bezier
curve, and along the selected subelements.

To Do
 
The `'PathSubelements'` property must be changed in type, as it does not need
to be an `App::PropertyLinkSubList`.
A `LinkSubList` is to select multiple subelements (edges) from multiple
objects. However, since we need to select a `'Path Object'` already,
which is a single object, the subelements that we can choose must belong
to this `'Path Object'` only.

Therefore, the correct property that must be used is `App::PropertyLinkSub`.
Then in the property editor we will be unable to select more than one object
thus preventing errors of the subelements not matching the `'PathObject'`.

In fact, both `'PathObject'` and `'PathSubelements'`
could be handled with a single `App::PropertyLinkSub` property,
as this property can be used to select a single object,
or a single object with its subelements.

In the future, we could migrate the properties, or outright break
compatibility with older objects by changing both properties
`'PathObject'` and `'PathSubelements'`.

An alternative to this would be to use a single `App::PropertyLinkSubList`.
This would allow us to build PathArrays on multiple objects and multiple
subelements (edges) of those objects at the same time. However, to do this,
the logic in `execute` would have to be changed to account for multiple
objects. Therefore, the first solution is simpler, that is, using
a single property of type `App::PropertyLinkSub`.



#### <img src="images/type_module.svg" style="width:16px;"> re

Support for regular expressions (RE).

This module provides regular expression matching operations similar to
those found in Perl.  It supports both 8-bit and Unicode strings; both
the pattern and the strings being processed can contain null bytes and
characters outside the US ASCII range.

Regular expressions can contain both special and ordinary characters.
Most ordinary characters, like "A", "a", or "0", are the simplest
regular expressions; they simply match themselves.  You can
concatenate ordinary characters, so last matches the string 'last'.

The special characters are:
    "."      Matches any character except a newline.
    "^"      Matches the start of the string.
    "$"      Matches the end of the string or just before the newline at
             the end of the string.
    "*"      Matches 0 or more (greedy) repetitions of the preceding RE.
             Greedy means that it will match as many repetitions as possible.
    "+"      Matches 1 or more (greedy) repetitions of the preceding RE.
    "?"      Matches 0 or 1 (greedy) of the preceding RE.
    *?,+?,?? Non-greedy versions of the previous three special characters.
    {m,n}    Matches from m to n repetitions of the preceding RE.
    {m,n}?   Non-greedy version of the above.
    "\\"     Either escapes special characters or signals a special sequence.
    []       Indicates a set of characters.
             A "^" as the first character indicates a complementing set.
    "|"      A|B, creates an RE that will match either A or B.
    (...)    Matches the RE inside the parentheses.
             The contents can be retrieved or matched later in the string.
    (?aiLmsux) The letters set the corresponding flags defined below.
    (?:...)  Non-grouping version of regular parentheses.
    (?P<name>...) The substring matched by the group is accessible by name.
    (?P=name)     Matches the text matched earlier by the group named name.
    (?#...)  A comment; ignored.
    (?=...)  Matches if ... matches next, but doesn't consume the string.
    (?!...)  Matches if ... doesn't match next.
    (?<=...) Matches if preceded by ... (must be fixed length).
    (?<!...) Matches if not preceded by ... (must be fixed length).
    (?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                       the (optional) no pattern otherwise.

The special sequences consist of "\\" and a character from the list
below.  If the ordinary character is not on the list, then the
resulting RE will match the second character.
    \number  Matches the contents of the group of the same number.
    \A       Matches only at the start of the string.
    \Z       Matches only at the end of the string.
    \b       Matches the empty string, but only at the start or end of a word.
    \B       Matches the empty string, but not at the start or end of a word.
    \d       Matches any decimal digit; equivalent to the set [0-9] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode digits.
    \D       Matches any non-digit character; equivalent to [^\d].
    \s       Matches any whitespace character; equivalent to [ \t\n\r\f\v] in
             bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the whole
             range of Unicode whitespace characters.
    \S       Matches any non-whitespace character; equivalent to [^\s].
    \w       Matches any alphanumeric character; equivalent to [a-zA-Z0-9_]
             in bytes patterns or string patterns with the ASCII flag.
             In string patterns without the ASCII flag, it will match the
             range of Unicode alphanumeric characters (letters plus digits
             plus underscore).
             With LOCALE, it will match the set [0-9_] plus characters defined
             as letters for the current locale.
    \W       Matches the complement of \w.
    \\       Matches a literal backslash.

This module exports the following functions:
    match     Match a regular expression pattern to the beginning of a string.
    fullmatch Match a regular expression pattern to all of a string.
    search    Search a string for the presence of a pattern.
    sub       Substitute occurrences of a pattern found in a string.
    subn      Same as sub, but also return the number of substitutions made.
    split     Split a string by the occurrences of a pattern.
    findall   Find all occurrences of a pattern in a string.
    finditer  Return an iterator yielding a Match object for each match.
    compile   Compile a pattern into a Pattern object.
    purge     Clear the regular expression cache.
    escape    Backslash all non-alphanumerics in a string.

Each function other than purge and escape can take an optional 'flags' argument
consisting of one or more of the following module constants, joined by "|".
A, L, and U are mutually exclusive.
    A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
                   match the corresponding ASCII character categories
                   (rather than the whole Unicode categories, which is the
                   default).
                   For bytes patterns, this flag is the only available
                   behaviour and needn't be specified.
    I  IGNORECASE  Perform case-insensitive matching.
    L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
    M  MULTILINE   "^" matches the beginning of lines (after a newline)
                   as well as the string.
                   "$" matches the end of lines (before a newline) as well
                   as the end of the string.
    S  DOTALL      "." matches any character at all, including the newline.
    X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
    U  UNICODE     For compatibility only. Ignored for string patterns (it
                   is the default), and forbidden for bytes patterns.

This module also defines an exception 'error'.



#### <img src="images/type_module.svg" style="width:16px;"> six

Utilities for writing code that runs on Python 2 and 3



#### <img src="images/type_module.svg" style="width:16px;"> tempfile

Temporary files.

This module provides generic, low- and high-level interfaces for
creating temporary files and directories.  All of the interfaces
provided by this module can be used without fear of race conditions
except for 'mktemp'.  'mktemp' is subject to race conditions and
should not be used; it is provided for backward compatibility only.

The default path names are returned as str.  If you supply bytes as
input, all return values will be in bytes.  Ex:

    >>> tempfile.mkstemp()
    (4, '/tmp/tmptpu9nin8')
    >>> tempfile.mkdtemp(suffix=b'')
    b'/tmp/tmppbi8f0hy'

This module also provides some data items to the user:

  TMP_MAX  - maximum number of names that will be tried before
             giving up.
  tempdir  - If this is set to a string before the first use of
             any routine from this module, it will be considered as
             another candidate location to store temporary files.



#### <img src="images/type_module.svg" style="width:16px;"> time

This module provides various functions to manipulate time values.

There are two standard representations of time.  One is the number
of seconds since the Epoch, in UTC (a.k.a. GMT).  It may be an integer
or a floating point number (to represent fractions of seconds).
The Epoch is system-defined; on Unix, it is generally January 1st, 1970.
The actual value can be retrieved by calling gmtime(0).

The other representation is a tuple of 9 integers giving local time.
The tuple items are:
  year (including century, e.g. 1998)
  month (1-12)
  day (1-31)
  hours (0-23)
  minutes (0-59)
  seconds (0-59)
  weekday (0-6, Monday is 0)
  Julian day (day in the year, 1-366)
  DST (Daylight Savings Time) flag (-1, 0 or 1)
If the DST flag is 0, the time is given in the regular time zone;
if it is 1, the time is given in the DST time zone;
if it is -1, mktime() should guess based on the date and time.



#### <img src="images/type_module.svg" style="width:16px;"> uuid

UUID objects (universally unique identifiers) according to RFC 4122.

This module provides immutable UUID objects (class UUID) and the functions
uuid1(), uuid3(), uuid4(), uuid5() for generating version 1, 3, 4, and 5
UUIDs as specified in RFC 4122.

If all you want is a unique ID, you should probably call uuid1() or uuid4().
Note that uuid1() may compromise privacy since it creates a UUID containing
the computer's network address.  uuid4() creates a random UUID.

Typical usage:

    >>> import uuid

    # make a UUID based on the host ID and current time
    >>> uuid.uuid1()    # doctest: +SKIP
    UUID('a8098c1a-f86e-11da-bd1a-00112444be1e')

    # make a UUID using an MD5 hash of a namespace UUID and a name
    >>> uuid.uuid3(uuid.NAMESPACE_DNS, 'python.org')
    UUID('6fa459ea-ee8a-3ca4-894e-db77e160355e')

    # make a random UUID
    >>> uuid.uuid4()    # doctest: +SKIP
    UUID('16fd2706-8baf-433b-82eb-8c7fada847da')

    # make a UUID using a SHA-1 hash of a namespace UUID and a name
    >>> uuid.uuid5(uuid.NAMESPACE_DNS, 'python.org')
    UUID('886313e1-3b8a-5372-9b90-0c9aee199e5d')

    # make a UUID from a string of hex digits (braces and hyphens ignored)
    >>> x = uuid.UUID('{00010203-0405-0607-0809-0a0b0c0d0e0f}')

    # convert a UUID to a string of hex digits in standard form
    >>> str(x)
    '00010203-0405-0607-0809-0a0b0c0d0e0f'

    # get the raw 16 bytes of the UUID
    >>> x.bytes
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f'

    # make a UUID from a 16-byte string
    >>> uuid.UUID(bytes=x.bytes)
    UUID('00010203-0405-0607-0809-0a0b0c0d0e0f')



#### <img src="images/type_module.svg" style="width:16px;"> zipfile

Read and write ZIP files.

XXX references to utf-8 need further investigation.









---
![](images/Right_arrow.png) [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Arch](Arch_Workbench.md) > Arch API
