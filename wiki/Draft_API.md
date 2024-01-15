# Draft API

Provide the Draft Workbench public programming interface.

The Draft module offers tools to create and manipulate 2D objects.
The functions in this file must be usable without requiring the
graphical user interface.
These functions can be used as the backend for the graphical commands
defined in `DraftTools.py`.




### Functions

#### <img src="images/Arrow-right.svg" style="width:16px;"> apply_current_style <small>(objs)</small>

Apply the current style to one or more objects.

    Parameters
     
    objs: a single object or an iterable with objects.



#### <img src="images/Arrow-right.svg" style="width:16px;"> argb_to_rgba <small>(color)</small>

Change byte order of a 4 byte color int from ARGB (Qt) to RGBA (FreeCAD).

    Alpha in both integers is always 255.
    Alpha in color properties, although ignored, is always zero however.

    Usage:

        qt_int = self.form.ShapeColor.property("color").rgba() # Note: returns ARGB int
        qt_int = self.form.ShapeColor.property("color").rgb()  # Note: returns ARGB int
        fc_int = argb_to_rgba(qt_int)

        FreeCAD.ParamGet("User parameter:BaseApp/Preferences/View")            .SetUnsigned("DefaultShapeColor", fc_int)

        obj.ViewObject.ShapeColor = fc_int & 0xFFFFFF00

    Related:

        getRgbF() returns an RGBA tuple. 4 floats in the range 0.0 - 1.0. Alpha is always 1.
        Alpha should be set to zero or removed before using the tuple to change a color property:

        obj.ViewObject.ShapeColor = self.form.ShapeColor.property("color").getRgbF()[:3]



#### <img src="images/Arrow-right.svg" style="width:16px;"> array <small>(objectslist, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None)</small>

This function creates an array of independent objects.
    Use make_array() to create a parametric array object.

    Creates an array of the given objects (that can be an object or a list
    of objects).

    In case of rectangular array, xnum of iterations in the x direction
    at xvector distance between iterations, and same for y and z directions
    with yvector and ynum and zvector and znum.

    In case of polar array, center is a vector, totalangle is the angle
    to cover (in degrees) and totalnum is the number of objects, including
    the original.

    Use
     
    array(objectslist, xvector, yvector, xnum, ynum) for rectangular array

    array(objectslist, xvector, yvector, zvector, xnum, ynum, znum) for rectangular array

    array(objectslist, center, totalangle, totalnum) for polar array



#### <img src="images/Arrow-right.svg" style="width:16px;"> autogroup <small>(obj)</small>

Add a given object to the defined Draft autogroup, if applicable.

    This function only works if the graphical interface is available.
    It checks that the `App.draftToolBar` class is available,
    which contains the group to use to automatically store
    new created objects.

    Originally, it worked with standard groups (`App::DocumentObjectGroup`),
    and Arch Workbench containers like `'Site'`, `'Building'`, `'Floor'`,
    and `'BuildingPart'`.

    Now it works with Draft Layers.

    Parameters
     
    obj: App::DocumentObject
        Any type of object that will be stored in the group.



#### <img src="images/Arrow-right.svg" style="width:16px;"> clone <small>(obj, delta=None, forcedraft=False)</small>

clone(obj,[delta,forcedraft])

    Makes a clone of the given object(s).
    The clone is an exact, linked copy of the given object. If the original
    object changes, the final object changes too.

    Parameters
     
    obj :

    delta : Base.Vector
        Delta Vector to move the clone from the original position.

    forcedraft : bool
        If forcedraft is True, the resulting object is a Draft clone
        even if the input object is an Arch object.



#### <img src="images/Arrow-right.svg" style="width:16px;"> compareObjects <small>(obj1, obj2)</small>

Print the differences between 2 objects.

    The two objects are compared through their `TypeId` attribute,
    or by using the `get_type` function.

    If they are the same type their properties are compared
    looking for differences.

    Neither `Shape` nor `Label` attributes are compared.

    Parameters
     
    obj1 : App::DocumentObject
        Any type of scripted object.
    obj2 : App::DocumentObject
        Any type of scripted object.



#### <img src="images/Arrow-right.svg" style="width:16px;"> compare_objects <small>(obj1, obj2)</small>

Print the differences between 2 objects.

    The two objects are compared through their `TypeId` attribute,
    or by using the `get_type` function.

    If they are the same type their properties are compared
    looking for differences.

    Neither `Shape` nor `Label` attributes are compared.

    Parameters
     
    obj1 : App::DocumentObject
        Any type of scripted object.
    obj2 : App::DocumentObject
        Any type of scripted object.



#### <img src="images/Arrow-right.svg" style="width:16px;"> convertDraftTexts <small>(textslist=[])</small>

Convert Text. DEPRECATED. Use 'convert_draft_texts'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> convert_draft_texts <small>(textslist=None)</small>

Convert the given Annotation to a Draft text.

    In the past, the `Draft Text` object didn't exist; text objects
    were of type `App::Annotation`. This function was introduced
    to convert those older objects to a `Draft Text` scripted object.

    This function was already present at splitting time during v0.19.

    Parameters
     
    textslist: list of objects, optional
        It defaults to `None`.
        A list containing `App::Annotation` objects or a single of these
        objects.
        If it is `None` it will convert all objects in the current document.



#### <img src="images/Arrow-right.svg" style="width:16px;"> copyMovedEdges <small>(arguments)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> copyRotatedEdges <small>(arguments)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> copyScaledEdges <small>(arguments)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> copy_moved_edges <small>(arguments)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> copy_rotated_edges <small>(arguments)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> copy_scaled_edges <small>(arguments)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> cut <small>(object1, object2)</small>

Return a cut object made from the difference of the 2 given objects.

    Parameters
     
    object1: Part::Feature
        Any object with a `Part::TopoShape`.

    object2: Part::Feature
        Any object with a `Part::TopoShape`.

    Returns
     
    Part::Cut
        The resulting cut object.

    None
        If there is a problem and the new object can't be created.



#### <img src="images/Arrow-right.svg" style="width:16px;"> dimDash <small>(p1, p2)</small>

Return a SoSeparator with a line used to make dimension dashes.

    It is used by `dim_symbol` to create line end symbols
    like `'Tick-2'`, `'DimOvershoot'`, and `'ExtOvershoot'` dashes.

    Parameters
     
    p1: tuple of three floats or Base::Vector3
        A point to define a line vertex.

    p2: tuple of three floats or Base::Vector3
        A point to define a line vertex.

    Returns
     
    Coin.SoSeparator
        A Coin object with a `SoLineSet` created from `p1` and `p2`
        as vertices.



#### <img src="images/Arrow-right.svg" style="width:16px;"> dimSymbol <small>(symbol=None, invert=False)</small>

Return the specified dimension symbol.

    Parameters
     
    symbol: int, optional
        It defaults to `None`, in which it gets the value from the parameter
        database, `get_param("dimsymbol")`.

        A numerical value defines different markers
         * 0, `SoSphere`
         * 1, `SoSeparator` with a `SoLineSet`, a circle (in fact a 24 sided polygon)
         * 2, `SoSeparator` with a `soCone`
         * 3, `SoSeparator` with a `SoFaceSet`
         * 4, `SoSeparator` with a `SoLineSet`, calling `dim_dash`
         * Otherwise, `SoSphere`

    invert: bool, optional
        It defaults to `False`.
        If it is `True` and `symbol=2`, the cone will be rotated
        -90 degrees around the Z axis, otherwise the rotation is positive,
        +90 degrees.

    Returns
     
    Coin.SoNode
        A `Coin.SoSphere`, or `Coin.SoSeparator` (circle, cone, face, line)
        that will be used as a dimension symbol.



#### <img src="images/Arrow-right.svg" style="width:16px;"> dim_dash <small>(p1, p2)</small>

Return a SoSeparator with a line used to make dimension dashes.

    It is used by `dim_symbol` to create line end symbols
    like `'Tick-2'`, `'DimOvershoot'`, and `'ExtOvershoot'` dashes.

    Parameters
     
    p1: tuple of three floats or Base::Vector3
        A point to define a line vertex.

    p2: tuple of three floats or Base::Vector3
        A point to define a line vertex.

    Returns
     
    Coin.SoSeparator
        A Coin object with a `SoLineSet` created from `p1` and `p2`
        as vertices.



#### <img src="images/Arrow-right.svg" style="width:16px;"> dim_symbol <small>(symbol=None, invert=False)</small>

Return the specified dimension symbol.

    Parameters
     
    symbol: int, optional
        It defaults to `None`, in which it gets the value from the parameter
        database, `get_param("dimsymbol")`.

        A numerical value defines different markers
         * 0, `SoSphere`
         * 1, `SoSeparator` with a `SoLineSet`, a circle (in fact a 24 sided polygon)
         * 2, `SoSeparator` with a `soCone`
         * 3, `SoSeparator` with a `SoFaceSet`
         * 4, `SoSeparator` with a `SoLineSet`, calling `dim_dash`
         * Otherwise, `SoSphere`

    invert: bool, optional
        It defaults to `False`.
        If it is `True` and `symbol=2`, the cone will be rotated
        -90 degrees around the Z axis, otherwise the rotation is positive,
        +90 degrees.

    Returns
     
    Coin.SoNode
        A `Coin.SoSphere`, or `Coin.SoSeparator` (circle, cone, face, line)
        that will be used as a dimension symbol.



#### <img src="images/Arrow-right.svg" style="width:16px;"> downgrade <small>(objects, delete=False, force=None)</small>

Downgrade the given objects.

    This is a counterpart to `upgrade`.

    Parameters
     
    objects: Part::Feature or list
        A single object to downgrade or a list
        containing various such objects.

    delete: bool, optional
        It defaults to `False`.
        If it is `True`, the old objects are deleted, and only the resulting
        object is kept.

    force: str, optional
        It defaults to `None`.
        Its value can be used to force a certain method of downgrading.
        It can be any of: `'explode'`, `'shapify'`, `'subtr'`, `'splitFaces'`,
        `'cut2'`, `'getWire'`, `'splitWires'`, or `'splitCompounds'`.

    Returns
     
    tuple
        A tuple containing two lists, a list of new objects
        and a list of objects to be deleted.

    None
        If there is a problem it will return `None`.

    See Also
     
    upgrade



#### <img src="images/Arrow-right.svg" style="width:16px;"> draftify <small>(objectslist, makeblock=False, delete=True)</small>

draftify(objectslist,[makeblock],[delete])

    Turn each object of the given list (objectslist can also be a single
    object) into a Draft parametric wire.

    TODO: support more objects

    Parameters
     
    objectslist :

    makeblock : bool
        If makeblock is True, multiple objects will be grouped in a block.

    delete : bool
        If delete = False, old objects are not deleted



#### <img src="images/Arrow-right.svg" style="width:16px;"> extrude <small>(obj, vector, solid=False)</small>

extrude(object, vector, [solid])

    Create a Part::Extrusion object from a given object.

    Parameters
     
    obj :

    vector : Base.Vector
        The extrusion direction and module.

    solid : bool
        TODO: describe.



#### <img src="images/Arrow-right.svg" style="width:16px;"> filterObjectsForModifiers <small>(objects, isCopied=False)</small>





#### <img src="images/Arrow-right.svg" style="width:16px;"> filter_objects_for_modifiers <small>(objects, isCopied=False)</small>





#### <img src="images/Arrow-right.svg" style="width:16px;"> formatObject <small>(target, origin=None)</small>

Apply visual properties to an object.

    This function only works if the graphical interface is available.

    If origin is `None` and target is not an annotation, the DefaultDrawStyle
    and DefaultDisplayMode preferences are applied. Else, the properties of
    origin are applied to target.

    If construction mode is active target is then placed in the construction
    group and the `constr` color is applied to its applicable color properties:
    TextColor, PointColor, LineColor, and ShapeColor.

    Parameters
     
    target: App::DocumentObject

    origin: App::DocumentObject, optional
        Defaults to `None`.
        If construction mode is not active, its visual properties are assigned
        to `target`, with the exception of `BoundingBox`, `Proxy`, `RootNode`
        and `Visibility`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> format_object <small>(target, origin=None)</small>

Apply visual properties to an object.

    This function only works if the graphical interface is available.

    If origin is `None` and target is not an annotation, the DefaultDrawStyle
    and DefaultDisplayMode preferences are applied. Else, the properties of
    origin are applied to target.

    If construction mode is active target is then placed in the construction
    group and the `constr` color is applied to its applicable color properties:
    TextColor, PointColor, LineColor, and ShapeColor.

    Parameters
     
    target: App::DocumentObject

    origin: App::DocumentObject, optional
        Defaults to `None`.
        If construction mode is not active, its visual properties are assigned
        to `target`, with the exception of `BoundingBox`, `Proxy`, `RootNode`
        and `Visibility`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> fuse <small>(object1, object2)</small>

fuse(oject1, object2)

    Returns an object made from the union of the 2 given objects.
    If the objects are coplanar, a special Draft Wire is used, otherwise we use
    a standard Part fuse.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get3DView <small>()</small>

Return the current 3D view.

    Returns
     
    Gui::View3DInventor
        Return the current `ActiveView` in the active document or `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getCloneBase <small>(obj, strict=False, recursive=True)</small>

Return the object cloned by this object, if any.

    Parameters
     
    obj: App::DocumentObject
        Any type of object.

    strict: bool, optional
        It defaults to `False`.
        If it is `True`, and this object is not a clone,
        this function will return `False`.

    recursive: bool, optional
        It defaults to `True`
        If it is `True`, it call recursively to itself to
        get base object and if it is `False` then it just
        return base object, not call recursively to find
        base object.

    Returns
     
    App::DocumentObject
        It `obj` is a `Draft Clone`, it will return the first object
        that is in its `Objects` property.

        If `obj` has a `CloneOf` property, it will search iteratively
        inside the object pointed to by this property.

    obj
        If `obj` is not a `Draft Clone`, nor it has a `CloneOf` property,
        it will return the same `obj`, as long as `strict` is `False`.

    False
        It will return `False` if `obj` is not a clone,
        and `strict` is `True`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getDXF <small>(obj, direction=None)</small>

Return DXF string of the object. DEPRECATED. Use 'get_dxf'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getGroupContents <small>(objectslist, walls=False, addgroups=False, spaces=False, noarchchild=False)</small>

Return a list of objects from groups. DEPRECATED.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getGroupNames <small>()</small>

Return a list of group names. DEPRECATED.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getMovableChildren <small>(objectslist, recursive=True)</small>

Return a list of objects with child objects. DEPRECATED.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getObjectsOfType <small>(objects, typ)</small>

Return only the objects that match the type in the list of objects.

    Parameters
     
    objects : list of App::DocumentObject
        A list of objects which will be tested.

    typ : str
        A string that indicates a type. This should be one of the types
        that can be returned by `get_type`.

    Returns
     
    list of objects
        Only the objects that match `typ` will be added to the output list.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getParam <small>(param, default=None)</small>

Return a parameter value from the current parameter database.

    The parameter database is located in the tree
    ::
        'User parameter:BaseApp/Preferences/Mod/Draft'

    In the case that `param` is `'linewidth'` or `'color'` it will get
    the values from the View parameters
    ::
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

    Parameters
     
    param : str
        A string that indicates a parameter in the parameter database.

    default : optional
        It indicates the default value of the given parameter.
        It defaults to `None`, in which case it will use a specific
        value depending on the type of parameter determined
        with `get_param_type`.

    Returns
     
    int, or str, or float, or bool
        Depending on `param` and its type, by returning `ParameterGrp.GetInt`,
        `ParameterGrp.GetString`, `ParameterGrp.GetFloat`,
        `ParameterGrp.GetBool`, or `ParameterGrp.GetUnsinged`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getParamType <small>(param)</small>

Return the type of the parameter entered.

    Parameters
     
    param : str
        A string that indicates a parameter in the parameter database.

    Returns
     
    str or None
        The returned string could be `'int'`, `'string'`, `'float'`,
        `'bool'`, `'unsigned'`, depending on the parameter.
        It returns `None` for unhandled situations.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getRealName <small>(name)</small>

Strip the trailing numbers from a string to get only the letters.

    Parameters
     
    name : str
        A string that may have a number at the end, `Line001`.

    Returns
     
    str
        A string without the numbers at the end, `Line`.
        The returned string cannot be empty; it will have
        at least one letter.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getSVG <small>(obj, scale=1, linewidth=0.35, fontsize=12, fillstyle='shape color', direction=None, linestyle=None, color=None, linespacing=None, techdraw=False, rotation=0, fillSpaces=False, override=True)</small>

Return SVG string of the object. DEPRECATED. Use 'get_svg'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getSelection <small>(gui=0)</small>

Return the current selected objects.

    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.

    It wraps around `Gui.Selection.getSelection`

    Parameters
     
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.

    Returns
     
    list of App::DocumentObject
        Returns a list of objects in the current selection.
        It can be an empty list if no object is selected.

        If the interface is not available, it returns `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getSelectionEx <small>(gui=0)</small>

Return the current selected objects together with their subelements.

    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.

    It wraps around `Gui.Selection.getSelectionEx`

    Parameters
     
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.

    Returns
     
    list of Gui::SelectionObject
        Returns a list of `Gui::SelectionObject` in the current selection.
        It can be an empty list if no object is selected.

        If the interface is not available, it returns `None`.

    Selection objects
     
    One `Gui::SelectionObject` has attributes that indicate which specific
    subelements, that is, vertices, wires, and faces, were selected.
    This can be useful to operate on the subelements themselves.
    If `G` is a `Gui::SelectionObject`
     * `G.Object` is the selected object
     * `G.ObjectName` is the name of the selected object
     * `G.HasSubObjects` is `True` if there are subelements in the selection
     * `G.SubObjects` is a tuple of the subelements' shapes
     * `G.SubElementNames` is a tuple of the subelements' names

    `SubObjects` and `SubElementNames` should be empty tuples
    if `HasSubObjects` is `False`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getType <small>(obj)</small>

Return a string indicating the type of the given object.

    Parameters
     
    obj : App::DocumentObject
        Any type of scripted object created with Draft,
        or any other workbench.

    Returns
     
    str
        If `obj` has a `Proxy`, it will return the value of `obj.Proxy.Type`.

        * If `obj` is a `Part.Shape`, returns `'Shape'`

        * If `obj` has a `TypeId`, returns `obj.TypeId`

        In other cases, it will return `'Unknown'`,
        or `None` if `obj` is `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_3d_view <small>()</small>

Return the current 3D view.

    Returns
     
    Gui::View3DInventor
        Return the current `ActiveView` in the active document or `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_bbox <small>(obj, debug=False)</small>

Return a BoundBox from any object that has a Coin RootNode.

    Normally the bounding box of an object can be taken
    from its `Part::TopoShape`.
    ::
        >>> print(obj.Shape.BoundBox)

    However, for objects without a `Shape`, such as those
    derived from `App::FeaturePython` like `Draft Text` and `Draft Dimension`,
    the bounding box can be calculated from the `RootNode` of the viewprovider.

    Parameters
     
    obj: App::DocumentObject
        Any object that has a `ViewObject.RootNode`.

    Returns
     
    Base::BoundBox
        It returns a `BoundBox` object which has information like
        minimum and maximum values of X, Y, and Z, as well as bounding box
        center.

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_clone_base <small>(obj, strict=False, recursive=True)</small>

Return the object cloned by this object, if any.

    Parameters
     
    obj: App::DocumentObject
        Any type of object.

    strict: bool, optional
        It defaults to `False`.
        If it is `True`, and this object is not a clone,
        this function will return `False`.

    recursive: bool, optional
        It defaults to `True`
        If it is `True`, it call recursively to itself to
        get base object and if it is `False` then it just
        return base object, not call recursively to find
        base object.

    Returns
     
    App::DocumentObject
        It `obj` is a `Draft Clone`, it will return the first object
        that is in its `Objects` property.

        If `obj` has a `CloneOf` property, it will search iteratively
        inside the object pointed to by this property.

    obj
        If `obj` is not a `Draft Clone`, nor it has a `CloneOf` property,
        it will return the same `obj`, as long as `strict` is `False`.

    False
        It will return `False` if `obj` is not a clone,
        and `strict` is `True`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_diffuse_color <small>(objs)</small>

Get a (cumulative) diffuse color from one or more objects.

    If all tuples in the result are identical a list with a single tuple is
    returned. In theory all faces of an object can be set to the same diffuse
    color that is different from its shape color, but that seems rare. The
    function does not take that into account.

    Parameters
     
    objs: a single object or an iterable with objects.

    Returns
     
    list of tuples
        The list will be empty if no valid object is found.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_dxf <small>(obj, direction=None)</small>

Return a DXF entity from the given object.

    If direction is given, the object is projected in 2D.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_group_contents <small>(objectslist, walls=False, addgroups=False, spaces=False, noarchchild=False)</small>

Return a list of objects from expanding the input groups.

    The function accepts any type of object, although it is most useful
    with "groups", as it is meant to unpack the objects inside these groups.

    Parameters
     
    objectslist: list
        If any object in the list is considered a group, see the `is_group`
        function, its contents (`obj.Group`) are extracted and added to the
        output list.

        Single items that aren't groups are added to the output list
        as is.

    walls: bool, optional
        It defaults to `False`.
        If it is `True`, Wall and Structure objects (Arch Workbench)
        are treated as groups; they are scanned for Window, Door,
        and Rebar objects, and these are added to the output list.

    addgroups: bool, optional
        It defaults to `False`.
        If it is `True`, the group itself is kept as part of the output list.

    spaces: bool, optional
        It defaults to `False`.
        If it is `True`, Arch Spaces are added to the output list even
        when addgroups is False (their contents are always added).

    noarchchild: bool, optional
        It defaults to `False`.
        If it is `True`, the objects inside Building and BuildingParts
        (Arch Workbench) aren't added to the output list.

    Returns
     
    list
        The list of objects from each group present in `objectslist`,
        plus any other individual object given in `objectslist`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_group_names <small>(doc=None)</small>

Return a list of names of existing groups in the document.

    Parameters
     
    doc: App::Document, optional
        It defaults to `None`.
        A document on which to search group names.
        It if is `None` it will search the current document.

    Returns
     
    list of str
        A list of names of objects that are considered groups.
        See the is_group function.

        Otherwise returns an empty list.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_movable_children <small>(objectslist, recursive=True, _donelist=[])</small>

Return a list of objects with child objects that move with a host.

    Builds a list of objects with all child objects (`obj.OutList`)
    that have their `MoveWithHost` attribute set to `True`.
    This function is mostly useful for Arch Workbench objects.

    Parameters
     
    objectslist: list of App::DocumentObject
        A single scripted object or list of objects.

    recursive: bool, optional
        It defaults to `True`, in which case the function
        is called recursively to also extract the children of children
        objects.
        Otherwise, only direct children of the input objects
        are added to the output list.

    _donelist: list
        List of object names. Used internally to prevent an endless loop.

    Returns
     
    list
        List of children objects that have their `MoveWithHost` attribute
        set to `True`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_objects_of_type <small>(objects, typ)</small>

Return only the objects that match the type in the list of objects.

    Parameters
     
    objects : list of App::DocumentObject
        A list of objects which will be tested.

    typ : str
        A string that indicates a type. This should be one of the types
        that can be returned by `get_type`.

    Returns
     
    list of objects
        Only the objects that match `typ` will be added to the output list.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_param <small>(param, default=None)</small>

Return a parameter value from the current parameter database.

    The parameter database is located in the tree
    ::
        'User parameter:BaseApp/Preferences/Mod/Draft'

    In the case that `param` is `'linewidth'` or `'color'` it will get
    the values from the View parameters
    ::
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

    Parameters
     
    param : str
        A string that indicates a parameter in the parameter database.

    default : optional
        It indicates the default value of the given parameter.
        It defaults to `None`, in which case it will use a specific
        value depending on the type of parameter determined
        with `get_param_type`.

    Returns
     
    int, or str, or float, or bool
        Depending on `param` and its type, by returning `ParameterGrp.GetInt`,
        `ParameterGrp.GetString`, `ParameterGrp.GetFloat`,
        `ParameterGrp.GetBool`, or `ParameterGrp.GetUnsinged`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_param_type <small>(param)</small>

Return the type of the parameter entered.

    Parameters
     
    param : str
        A string that indicates a parameter in the parameter database.

    Returns
     
    str or None
        The returned string could be `'int'`, `'string'`, `'float'`,
        `'bool'`, `'unsigned'`, depending on the parameter.
        It returns `None` for unhandled situations.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_real_name <small>(name)</small>

Strip the trailing numbers from a string to get only the letters.

    Parameters
     
    name : str
        A string that may have a number at the end, `Line001`.

    Returns
     
    str
        A string without the numbers at the end, `Line`.
        The returned string cannot be empty; it will have
        at least one letter.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_rgb <small>(color, testbw=True)</small>

Return an RRGGBB value #000000 from a FreeCAD color.

    Parameters
     
    color : list or tuple with RGB values
        The values must be in the 0.0-1.0 range.
    testwb : bool (default = True)
        Pure white will be converted into pure black.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_rgba_tuple <small>(color, typ=1.0)</small>

Return an RGBA tuple.

    Parameters
     
    color: int
        RGBA integer.
    typ: any float (default = 1.0) or int (use 255)
        If float the values in the returned tuple are in the 0.0-1.0 range.
        Else the values are in the 0-255 range.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_selection <small>(gui=0)</small>

Return the current selected objects.

    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.

    It wraps around `Gui.Selection.getSelection`

    Parameters
     
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.

    Returns
     
    list of App::DocumentObject
        Returns a list of objects in the current selection.
        It can be an empty list if no object is selected.

        If the interface is not available, it returns `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_selection_ex <small>(gui=0)</small>

Return the current selected objects together with their subelements.

    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.

    It wraps around `Gui.Selection.getSelectionEx`

    Parameters
     
    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.

    Returns
     
    list of Gui::SelectionObject
        Returns a list of `Gui::SelectionObject` in the current selection.
        It can be an empty list if no object is selected.

        If the interface is not available, it returns `None`.

    Selection objects
     
    One `Gui::SelectionObject` has attributes that indicate which specific
    subelements, that is, vertices, wires, and faces, were selected.
    This can be useful to operate on the subelements themselves.
    If `G` is a `Gui::SelectionObject`
     * `G.Object` is the selected object
     * `G.ObjectName` is the name of the selected object
     * `G.HasSubObjects` is `True` if there are subelements in the selection
     * `G.SubObjects` is a tuple of the subelements' shapes
     * `G.SubElementNames` is a tuple of the subelements' names

    `SubObjects` and `SubElementNames` should be empty tuples
    if `HasSubObjects` is `False`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_svg <small>(obj, scale=1, linewidth=0.35, fontsize=12, fillstyle='shape color', direction=None, linestyle=None, color=None, linespacing=None, techdraw=False, rotation=0, fillspaces=False, override=True)</small>

Return a string containing an SVG representation of the object.

    Paramaeters
     
    scale: float, optional
        It defaults to 1.
        It allows scaling line widths down, so they are resolution-independent.

    linewidth: float, optional
        It defaults to 0.35.

    fontsize: float, optional
        It defaults to 12, which is interpreted as `pt` unit (points).
        It is used if the given object contains any text.

    fillstyle: str, optional
        It defaults to 'shape color'.

    direction: Base::Vector3, optional
        It defaults to `None`.
        It is an arbitrary projection vector or a `WorkingPlane.PlaneBase`
        instance.

    linestyle: optional
        It defaults to `None`.

    color: optional
        It defaults to `None`.

    linespacing: float, optional
        It defaults to `None`.

    techdraw: bool, optional
        It defaults to `False`.
        If it is `True`, it sets some options for generating SVG strings
        for displaying inside TechDraw.

    rotation: float, optional
        It defaults to 0.

    fillspaces: bool, optional
        It defaults to `False`.

    override: bool, optional
        It defaults to `True`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_type <small>(obj)</small>

Return a string indicating the type of the given object.

    Parameters
     
    obj : App::DocumentObject
        Any type of scripted object created with Draft,
        or any other workbench.

    Returns
     
    str
        If `obj` has a `Proxy`, it will return the value of `obj.Proxy.Type`.

        * If `obj` is a `Part.Shape`, returns `'Shape'`

        * If `obj` has a `TypeId`, returns `obj.TypeId`

        In other cases, it will return `'Unknown'`,
        or `None` if `obj` is `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> get_windows <small>(obj)</small>

Return the windows and rebars inside a host.

    Parameters
     
    obj: App::DocumentObject
        A scripted object of type `'Wall'` or `'Structure'`
        (Arch Workbench).
        This will be searched for objects of type `'Window'` and `'Rebar'`,
        and clones of them, and the found elements will be added
        to the output list.

        The function will search recursively all elements under `obj.OutList`,
        in case the windows and rebars are nested under other walls
        and structures.

    Returns
     
    list
        A list of all found windows and rebars in `obj`.
        If `obj` is itself a `'Window'` or a `'Rebar'`, or a clone of them,
        it will return the same `obj` element.



#### <img src="images/Arrow-right.svg" style="width:16px;"> getrgb <small>(color, testbw=True)</small>

Return an RRGGBB value #000000 from a FreeCAD color.

    Parameters
     
    color : list or tuple with RGB values
        The values must be in the 0.0-1.0 range.
    testwb : bool (default = True)
        Pure white will be converted into pure black.



#### <img src="images/Arrow-right.svg" style="width:16px;"> heal <small>(objlist=None, delete=True, reparent=True)</small>

heal([objlist],[delete],[reparent])

    Recreate Draft objects that are damaged, for example if created from an
    earlier version. If ran without arguments, all the objects in the document
    will be healed if they are damaged.

    Parameters
     
    objlist : list

    delete : Base.Vector or list of Base.Vector
        If delete is True, the damaged objects are deleted (default).

    reparent : bool
        If reparent is True (default), new objects go at the very same place
        in the tree than their original.



#### <img src="images/Arrow-right.svg" style="width:16px;"> isClone <small>(obj, objtype=None, recursive=False)</small>

Return True if the given object is a clone of a certain type.

    A clone is of type `'Clone'`, and has a reference
    to the original object inside its `Objects` attribute,
    which is an `'App::PropertyLinkListGlobal'`.

    The `Objects` attribute can point to another `'Clone'` object.
    If `recursive` is `True`, the function will be called recursively
    to further test this clone, until the type of the original object
    can be compared to `objtype`.

    Parameters
     
    obj : App::DocumentObject
        The clone object that will be tested for a certain type.

    objtype : str or list of str
        A type string such as one obtained from `get_type`.
        Or a list of such types.

    recursive : bool, optional
        It defaults to `False`.
        If it is `True`, this same function will be called recursively
        with `obj.Object[0]` as input.

        This option only works if `obj.Object[0]` is of type `'Clone'`,
        that is, if `obj` is a clone of a clone.

    Returns
     
    bool
        Returns `True` if `obj` is of type `'Clone'`,
        and `obj.Object[0]` is of type `objtype`.

        If `objtype` is a list, then `obj.Objects[0]`
        will be tested against each of the elements in the list,
        and it will return `True` if at least one element matches the type.

        If `obj` isn't of type `'Clone'` but has the `CloneOf` attribute,
        it will also return `True`.

        It returns `False` otherwise, for example,
        if `obj` is not even a clone.



#### <img src="images/Arrow-right.svg" style="width:16px;"> isClosedEdge <small>(edge_index, object)</small>





#### <img src="images/Arrow-right.svg" style="width:16px;"> is_clone <small>(obj, objtype=None, recursive=False)</small>

Return True if the given object is a clone of a certain type.

    A clone is of type `'Clone'`, and has a reference
    to the original object inside its `Objects` attribute,
    which is an `'App::PropertyLinkListGlobal'`.

    The `Objects` attribute can point to another `'Clone'` object.
    If `recursive` is `True`, the function will be called recursively
    to further test this clone, until the type of the original object
    can be compared to `objtype`.

    Parameters
     
    obj : App::DocumentObject
        The clone object that will be tested for a certain type.

    objtype : str or list of str
        A type string such as one obtained from `get_type`.
        Or a list of such types.

    recursive : bool, optional
        It defaults to `False`.
        If it is `True`, this same function will be called recursively
        with `obj.Object[0]` as input.

        This option only works if `obj.Object[0]` is of type `'Clone'`,
        that is, if `obj` is a clone of a clone.

    Returns
     
    bool
        Returns `True` if `obj` is of type `'Clone'`,
        and `obj.Object[0]` is of type `objtype`.

        If `objtype` is a list, then `obj.Objects[0]`
        will be tested against each of the elements in the list,
        and it will return `True` if at least one element matches the type.

        If `obj` isn't of type `'Clone'` but has the `CloneOf` attribute,
        it will also return `True`.

        It returns `False` otherwise, for example,
        if `obj` is not even a clone.



#### <img src="images/Arrow-right.svg" style="width:16px;"> is_closed_edge <small>(edge_index, object)</small>





#### <img src="images/Arrow-right.svg" style="width:16px;"> is_group <small>(obj)</small>

Return True if the given object is considered a group.

    Parameters
     
    obj : App::DocumentObject
        The object to check.

    Returns
     
    bool
        Returns `True` if `obj` is considered a group:

        The object is derived from `App::DocumentObjectGroup` but not
        a `'LayerContainer'`.

        Or the object is of the type `'Project'`, `'Site'`, `'Building'`,
        `'Floor'`, `'BuildingPart'` or `'Space'` from the Arch Workbench.
        Note that `'Floor'` and `'Building'` are obsolete types.

        Otherwise returns `False`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> joinTwoWires <small>(wire1, wire2)</small>

join_two_wires(object, object): joins two wires if they share a common
    point as a start or an end.



#### <img src="images/Arrow-right.svg" style="width:16px;"> joinWires <small>(wires, joinAttempts=0)</small>

join_wires(objects): merges a set of wires where possible, if any of those
    wires have a coincident start and end point



#### <img src="images/Arrow-right.svg" style="width:16px;"> join_two_wires <small>(wire1, wire2)</small>

joins two wires if they share a common
    point as a start or an end.



#### <img src="images/Arrow-right.svg" style="width:16px;"> join_wires <small>(wires, joinAttempts=0)</small>

merges a set of wires where possible, if any of those
    wires have a coincident start and end point



#### <img src="images/Arrow-right.svg" style="width:16px;"> loadSvgPatterns <small>()</small>

Load the default Draft SVG patterns and user defined patterns.

    The SVG patterns are added as a dictionary to the `App.svgpatterns`
    attribute.



#### <img src="images/Arrow-right.svg" style="width:16px;"> loadTexture <small>(filename, size=None, gui=0)</small>

Return a Coin.SoSFImage to use as a texture for a 2D plane.

    This function only works if the graphical interface is available
    as the visual properties that can be applied to a shape
    are attributes of the view provider (`obj.ViewObject`).

    Parameters
     
    filename: str
        A path to a pixel image file (PNG) that can be used as a texture
        on the face of an object.

    size: tuple of two int, or a single int, optional
        It defaults to `None`.
        If a tuple is given, the two values define the width and height
        in pixels to which the loaded image will be scaled.
        If it is a single value, it is used for both dimensions.

        If it is `None`, the size will be determined from the `QImage`
        created from `filename`.

        CURRENTLY the input `size` parameter IS NOT USED.
        It always uses the `QImage` to determine this information.

    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.

    Returns
     
    coin.SoSFImage
        An image object with the appropriate size, number of components
        (grayscale, grayscale and transparency, color,
        color and transparency), and byte data.

        It returns `None` if the interface is not available,
        or if there is a problem creating the image.



#### <img src="images/Arrow-right.svg" style="width:16px;"> load_svg_patterns <small>()</small>

Load the default Draft SVG patterns and user defined patterns.

    The SVG patterns are added as a dictionary to the `App.svgpatterns`
    attribute.



#### <img src="images/Arrow-right.svg" style="width:16px;"> load_texture <small>(filename, size=None, gui=0)</small>

Return a Coin.SoSFImage to use as a texture for a 2D plane.

    This function only works if the graphical interface is available
    as the visual properties that can be applied to a shape
    are attributes of the view provider (`obj.ViewObject`).

    Parameters
     
    filename: str
        A path to a pixel image file (PNG) that can be used as a texture
        on the face of an object.

    size: tuple of two int, or a single int, optional
        It defaults to `None`.
        If a tuple is given, the two values define the width and height
        in pixels to which the loaded image will be scaled.
        If it is a single value, it is used for both dimensions.

        If it is `None`, the size will be determined from the `QImage`
        created from `filename`.

        CURRENTLY the input `size` parameter IS NOT USED.
        It always uses the `QImage` to determine this information.

    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.

    Returns
     
    coin.SoSFImage
        An image object with the appropriate size, number of components
        (grayscale, grayscale and transparency, color,
        color and transparency), and byte data.

        It returns `None` if the interface is not available,
        or if there is a problem creating the image.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeAngularDimension <small>(center, angles, p3, normal=None)</small>

Create an angle dimension. DEPRECATED. Use 'make_angular_dimension'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeArray <small>(baseobject, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, name='Array', use_link=False)</small>

Create an Array. DEPRECATED. Use 'make_array'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeBSpline <small>(pointslist, closed=False, placement=None, face=None, support=None)</small>

make_bspline(pointslist, [closed], [placement])

    Creates a B-Spline object from the given list of vectors.

    Parameters
     
    pointlist : [Base.Vector]
        List of points to create the polyline.
        Instead of a pointslist, you can also pass a Part Wire.
        TODO: Change the name so!

    closed : bool
        If closed is True or first and last points are identical,
        the created BSpline will be closed.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeBezCurve <small>(pointslist, closed=False, placement=None, face=None, support=None, degree=None)</small>

make_bezcurve(pointslist, [closed], [placement])

    Creates a Bezier Curve object from the given list of vectors.

    Parameters
     
    pointlist : [Base.Vector]
        List of points to create the polyline.
        Instead of a pointslist, you can also pass a Part Wire.
        TODO: Change the name so!

    closed : bool
        If closed is True or first and last points are identical,
        the created BSpline will be closed.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe

    degree : int
        Degree of the BezCurve



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeBlock <small>(objectslist)</small>

make_block(objectslist)

    Creates a Draft Block from the given objects.

    Parameters
     
    objectlist : list
        Major radius of the ellipse.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeCircle <small>(radius, placement=None, face=None, startangle=None, endangle=None, support=None)</small>

make_circle(radius, [placement, face, startangle, endangle])
    or make_circle(edge,[face]):

    Creates a circle object with given parameters.

    If startangle and endangle are provided and not equal, the object will show
    an arc instead of a full circle.

    Parameters
     
    radius : the radius of the circle.

    placement :
        If placement is given, it is used.

    face : Bool
        If face is False, the circle is shown as a wireframe,
        otherwise as a face.

    startangle : start angle of the circle (in degrees)
        Recalculated if not in the -360 to 360 range.

    endangle : end angle of the circle (in degrees)
        Recalculated if not in the -360 to 360 range.

    edge : edge.Curve must be a 'Part.Circle'
        The circle is created from the given edge.

    support :
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeCopy <small>(obj, force=None, reparent=False, simple_copy=False)</small>

make_copy(object, [force], [reparent], [simple_copy])

    Make an exact copy of an object and return it.

    Parameters
     
    obj :
        Object to copy.

    force :
        Obsolete, not used anymore.

    reparent :
        Group the new object in the same group of the old one.

    simple_copy :
        Create a simple copy of the object (a new non parametric
        Part::Feature with the same Shape as the given object).



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeDimension <small>(p1, p2, p3=None, p4=None)</small>

Create a dimension. DEPRECATED. Use 'make_dimension'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeEllipse <small>(majradius, minradius, placement=None, face=None, support=None)</small>

make_ellipse(majradius, minradius, [placement], [face], [support])

    Makes an ellipse with the given major and minor radius, and optionally
    a placement.

    Parameters
     
    majradius :
        Major radius of the ellipse.

    minradius :
        Minor radius of the ellipse.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeFacebinder <small>(selectionset, name='Facebinder')</small>

make_facebinder(selectionset, [name])

    Creates a Facebinder object from a selection set.

    Parameters
     
    selectionset :
        Only faces will be added.

    name : string (default = "Facebinder")
        Name of the created object



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeLabel <small>(targetpoint=None, target=None, direction=None, distance=None, labeltype=None, placement=None)</small>

Create a Label. DEPRECATED. Use 'make_label'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeLayer <small>(name=None, linecolor=None, drawstyle=None, shapecolor=None, transparency=None)</small>

Create a Layer. DEPRECATED. Use 'make_layer'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeLine <small>(first_param, last_param=None)</small>

makeLine(first_param, p2)

    Creates a line from 2 points or from a given object.

    Parameters
     
    first_param :
        Base.Vector -> First point of the line (if p2 is None)
        Part.LineSegment -> Line is created from the given Linesegment
        Shape -> Line is created from the give Shape

    last_param : Base.Vector
        Second point of the line, if not set the function evaluates
        the first_param to look for a Part.LineSegment or a Shape



#### <img src="images/Arrow-right.svg" style="width:16px;"> makePathArray <small>(baseobject, pathobject, count, xlate=None, align=False, pathobjsubs=[], use_link=False)</small>

Create PathArray. DEPRECATED. Use 'make_path_array'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makePoint <small>(X=0, Y=0, Z=0, color=None, name='Point', point_size=5)</small>

make_point(x, y, z, [color(r, g, b), point_size]) or
        make_point(Vector, color(r, g, b), point_size])

    Creates a Draft Point in the current document.

    Parameters
     
    X :
        float -> X coordinate of the point
        Base.Vector -> Ignore Y and Z coordinates and create the point
            from the vector.

    Y : float
        Y coordinate of the point

    Z : float
        Z coordinate of the point

    color : (R, G, B)
        Point color as RGB
        example to create a colored point:
        make_point(0, 0, 0, (1, 0, 0)) # color = red
        example to change the color, make sure values are floats:
        p1.ViewObject.PointColor = (0.0, 0.0, 1.0)



#### <img src="images/Arrow-right.svg" style="width:16px;"> makePointArray <small>(base, ptlst)</small>

Create PointArray. DEPRECATED. Use 'make_point_array'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makePolygon <small>(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)</small>

makePolgon(edges,[radius],[inscribed],[placement],[face])

    Creates a polygon object with the given number of edges and radius.

    Parameters
     
    edges : int
        Number of edges of the polygon.

    radius :
        Radius of the control circle.

    inscribed : bool
        Defines is the polygon is inscribed or not into the control circle.

    placement : Base.Placement
        If placement is given, it is used.

    face : bool
        If face is True, the resulting shape is displayed as a face,
        otherwise as a wireframe.

    support :
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeRectangle <small>(length, height=0, placement=None, face=None, support=None)</small>

make_rectangle(length, width, [placement], [face])

    Creates a Rectangle object with length in X direction and height in Y
    direction.

    Parameters
     
    length, height : dimensions of the rectangle

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    Rectangles can also be constructed by giving them a list of four vertices
    as first argument: make_rectangle(list_of_vertices, face=...)
    but you are responsible to check yourself that these 4 vertices are ordered
    and actually form a rectangle, otherwise the result might be wrong. Placement
    is ignored when constructing a rectangle this way (face argument is kept).



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeShape2DView <small>(baseobj, projectionVector=None, facenumbers=[])</small>

make_shape2dview(object, [projectionVector], [facenumbers])

    Add a 2D shape to the document, which is a 2D projection of the given object.

    Parameters
     
    object :
        TODO: Describe

    projectionVector : Base.Vector
        Custom vector for the projection

    facenumbers : [] TODO: Describe
        A list of face numbers to be considered in individual faces mode.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeShapeString <small>(String, FontFile, Size=100, Tracking=0)</small>

ShapeString(Text,FontFile,[Height],[Track])

    Turns a text string into a Compound Shape

    Parameters
     
    majradius :
        Major radius of the ellipse.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeSketch <small>(objects_list, autoconstraints=False, addTo=None, delete=False, name='Sketch', radiusPrecision=-1, tol=0.001)</small>

make_sketch(objects_list, [autoconstraints], [addTo], [delete],
                   [name], [radiusPrecision], [tol])

    Makes a Sketch objects_list with the given Draft objects.

    Parameters
     
    objects_list: can be single or list of objects of Draft type objects,
        Part::Feature, Part.Shape, or mix of them.

    autoconstraints(False): if True, constraints will be automatically added to
        wire nodes, rectangles and circles.

    addTo(None) : if set to an existing sketch, geometry will be added to it
        instead of creating a new one.

    delete(False): if True, the original object will be deleted.
        If set to a string 'all' the object and all its linked object will be
        deleted.

    name('Sketch'): the name for the new sketch object.

    radiusPrecision(-1): If <0, disable radius constraint. If =0, add individual
        radius constraint. If >0, the radius will be rounded according to this
        precision, and 'Equal' constraint will be added to curve with equal
        radius within precision.

    tol(1e-3): Tolerance used to check if the shapes are planar and coplanar.
        Consider change to tol=-1 for a more accurate analysis.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeText <small>(stringlist, point=Vector (0.0, 0.0, 0.0), screen=False)</small>

Create Text. DEPRECATED. Use 'make_text'.



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeWire <small>(pointslist, closed=False, placement=None, face=None, support=None, bs2wire=False)</small>

make_wire(pointslist, [closed], [placement])

    Creates a Wire object from the given list of vectors.  If face is
    true (and wire is closed), the wire will appear filled. Instead of
    a pointslist, you can also pass a Part Wire.

    Parameters
     
    pointslist : [Base.Vector]
        List of points to create the polyline

    closed : bool
        If closed is True or first and last points are identical,
        the created polyline will be closed.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe

    bs2wire : bool
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> makeWorkingPlaneProxy <small>(placement)</small>

make_working_plane_proxy(placement)

    Creates a Working Plane proxy object in the current document.

    Parameters
     
    placement : Base.Placement
        specify the p.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_angular_dimension <small>(center=Vector (0.0, 0.0, 0.0), angles=None, dim_line=Vector (10.0, 10.0, 0.0), normal=None)</small>

Create an angular dimension from the given center and angles.

    Parameters
     
    center: Base::Vector3, optional
        It defaults to the origin `Vector(0, 0, 0)`.
        Center of the dimension line, which is a circular arc.

    angles: list of two floats, optional
        It defaults to `[0, 90]`.
        It is a list of two angles, given in degrees, that determine
        the aperture of the dimension line, that is, of the circular arc.
        It is drawn counter-clockwise.
        ::
            angles = [0 90]
            angles = [330 60]  # the arc crosses the X axis
            angles = [-30 60]  # same angle

    dim_line: Base::Vector3, optional
        It defaults to `Vector(10, 10, 0)`.
        This is a point through which the extension of the dimension line
        will pass. This defines the radius of the dimension line,
        the circular arc.

    normal: Base::Vector3, optional
        It defaults to `None`, in which case the axis of the current working
        plane is used.

    Returns
     
    App::FeaturePython
        A scripted object of type `'AngularDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_arc_3points <small>(points, placement=None, face=False, support=None, map_mode='Deactivated', primitive=False)</small>

Draw a circular arc defined by three points in the circumference.

    Parameters
     
    points: list of Base::Vector3
        A list that must be three points.

    placement: Base::Placement, optional
        It defaults to `None`.
        It is a placement, comprised of a `Base` (`Base::Vector3`),
        and a `Rotation` (`Base::Rotation`).
        If it exists it moves the center of the new object to the point
        indicated by `placement.Base`, while `placement.Rotation`
        is ignored so that the arc keeps the same orientation
        with which it was created.

        If both `support` and `placement` are given,
        `placement.Base` is used for the `AttachmentOffset.Base`,
        and again `placement.Rotation` is ignored.

    face: bool, optional
        It defaults to `False`.
        If it is `True` it will create a face in the closed arc.
        Otherwise only the circumference edge will be shown.

    support: App::PropertyLinkSubList, optional
        It defaults to `None`.
        It is a list containing tuples to define the attachment
        of the new object.

        A tuple in the list needs two elements;
        the first is an external object, and the second is another tuple
        with the names of sub-elements on that external object
        likes vertices or faces.
        ::
            support = [(obj, ("Face1"))]
            support = [(obj, ("Vertex1", "Vertex5", "Vertex8"))]

        This parameter sets the `Support` property but it only really affects
        the position of the new object when the `map_mode`
        is set to other than `'Deactivated'`.

    map_mode: str, optional
        It defaults to `'Deactivated'`.
        It defines the type of `'MapMode'` of the new object.
        This parameter only works when a `support` is also provided.

        Example: place the new object on a face or another object.
        ::
            support = [(obj, ("Face1"))]
            map_mode = 'FlatFace'

        Example: place the new object on a plane created by three vertices
        of an object.
        ::
            support = [(obj, ("Vertex1", "Vertex5", "Vertex8"))]
            map_mode = 'ThreePointsPlane'

    primitive: bool, optional
        It defaults to `False`. If it is `True`, it will create a Part
        primitive instead of a Draft object.
        In this case, `placement`, `face`, `support`, and `map_mode`
        are ignored.

    Returns
     
    Part::Part2DObject or Part::Feature
        The new arc object.
        Normally it returns a parametric Draft object (`Part::Part2DObject`).
        If `primitive` is `True`, it returns a basic `Part::Feature`.

    None
        Returns `None` if there is a problem and the object cannot be created.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_array <small>(base_object, arg1, arg2, arg3, arg4=None, arg5=None, arg6=None, use_link=True)</small>

Create a Draft Array of the given object.

    Rectangular array
     
    make_array(object, xvector, yvector, xnum, ynum)
    make_array(object, xvector, yvector, zvector, xnum, ynum, znum)

    xnum of iterations in the x direction
    at xvector distance between iterations, same for y direction
    with yvector and ynum, same for z direction with zvector and znum.

    Polar array
     
    make_array(object, center, totalangle, totalnum) for polar array, or

    center is a vector, totalangle is the angle to cover (in degrees)
    and totalnum is the number of objects, including the original.

    Circular array
     
    make_array(object, rdistance, tdistance, axis, center, ncircles, symmetry)

    In case of a circular array, rdistance is the distance of the
    circles, tdistance is the distance within circles, axis the rotation-axis,
    center the center of rotation, ncircles the number of circles
    and symmetry the number of symmetry-axis of the distribution.

    To Do
     
    The `Array` class currently handles three types of arrays,
    orthogonal, polar, and circular. In the future, probably they should be
    split in separate classes so that they are easier to manage.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_bezcurve <small>(pointslist, closed=False, placement=None, face=None, support=None, degree=None)</small>

make_bezcurve(pointslist, [closed], [placement])

    Creates a Bezier Curve object from the given list of vectors.

    Parameters
     
    pointlist : [Base.Vector]
        List of points to create the polyline.
        Instead of a pointslist, you can also pass a Part Wire.
        TODO: Change the name so!

    closed : bool
        If closed is True or first and last points are identical,
        the created BSpline will be closed.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe

    degree : int
        Degree of the BezCurve



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_block <small>(objectslist)</small>

make_block(objectslist)

    Creates a Draft Block from the given objects.

    Parameters
     
    objectlist : list
        Major radius of the ellipse.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_bspline <small>(pointslist, closed=False, placement=None, face=None, support=None)</small>

make_bspline(pointslist, [closed], [placement])

    Creates a B-Spline object from the given list of vectors.

    Parameters
     
    pointlist : [Base.Vector]
        List of points to create the polyline.
        Instead of a pointslist, you can also pass a Part Wire.
        TODO: Change the name so!

    closed : bool
        If closed is True or first and last points are identical,
        the created BSpline will be closed.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_circle <small>(radius, placement=None, face=None, startangle=None, endangle=None, support=None)</small>

make_circle(radius, [placement, face, startangle, endangle])
    or 

    Creates a circle object with given parameters.

    If startangle and endangle are provided and not equal, the object will show
    an arc instead of a full circle.

    Parameters
     
    radius : the radius of the circle.

    placement :
        If placement is given, it is used.

    face : Bool
        If face is False, the circle is shown as a wireframe,
        otherwise as a face.

    startangle : start angle of the circle (in degrees)
        Recalculated if not in the -360 to 360 range.

    endangle : end angle of the circle (in degrees)
        Recalculated if not in the -360 to 360 range.

    edge : edge.Curve must be a 'Part.Circle'
        The circle is created from the given edge.

    support :
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_circular_array <small>(base_object, r_distance=100, tan_distance=50, number=3, symmetry=1, axis=Vector (0.0, 0.0, 1.0), center=Vector (0.0, 0.0, 0.0), use_link=True)</small>

Create a circular array from the given object.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    r_distance: float, optional
        It defaults to `100`.
        Radial distance to the next ring of circular arrays.

    tan_distance: float, optional
        It defaults to `50`.
        The tangential distance between two elements located
        in the same circular ring.
        The tangential distance together with the radial distance
        determine how many copies are created.

    number: int, optional
        It defaults to 3.
        The number of layers or rings of repeated objects.
        The original object stays at the center, and is counted
        as a layer itself. So, if you want at least one layer of circular
        copies, this number must be at least 2.

    symmetry: int, optional
        It defaults to 1.
        It indicates how many lines of symmetry the entire circular pattern
        has. That is, with 1, the array is symmetric only after a full
        360 degrees rotation.

        When it is 2, the array is symmetric at 0 and 180 degrees.
        When it is 3, the array is symmetric at 0, 120, and 240 degrees.
        When it is 4, the array is symmetric at 0, 90, 180, and 270 degrees.
        Et cetera.

    axis: Base::Vector3, optional
        It defaults to `App.Vector(0, 0, 1)` or the `+Z` axis.
        The unit vector indicating the axis of rotation.

    center: Base::Vector3, optional
        It defaults to `App.Vector(0, 0, 0)` or the global origin.
        The point through which the `axis` passes to define
        the axis of rotation.

    use_link: bool, optional
        It defaults to `True`.
        If it is `True` the produced copies are not `Part::TopoShape` copies,
        but rather `App::Link` objects.
        The Links repeat the shape of the original `base_object` exactly,
        and therefore the resulting array is more memory efficient.

        Also, when `use_link` is `True`, the `Fuse` property
        of the resulting array does not work; the array doesn't
        contain separate shapes, it only has the original shape repeated
        many times, so there is nothing to fuse together.

        If `use_link` is `False` the original shape is copied many times.
        In this case the `Fuse` property is able to fuse
        all copies into a single object, if they touch each other.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.

    See Also
     
    make_ortho_array, make_polar_array, make_path_array, make_point_array



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_clone <small>(obj, delta=None, forcedraft=False)</small>

clone(obj,[delta,forcedraft])

    Makes a clone of the given object(s).
    The clone is an exact, linked copy of the given object. If the original
    object changes, the final object changes too.

    Parameters
     
    obj :

    delta : Base.Vector
        Delta Vector to move the clone from the original position.

    forcedraft : bool
        If forcedraft is True, the resulting object is a Draft clone
        even if the input object is an Arch object.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_copy <small>(obj, force=None, reparent=False, simple_copy=False)</small>

make_copy(object, [force], [reparent], [simple_copy])

    Make an exact copy of an object and return it.

    Parameters
     
    obj :
        Object to copy.

    force :
        Obsolete, not used anymore.

    reparent :
        Group the new object in the same group of the old one.

    simple_copy :
        Create a simple copy of the object (a new non parametric
        Part::Feature with the same Shape as the given object).



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_dimension <small>(p1, p2, p3=None, p4=None)</small>

Create one of three types of dimension objects.

    In all dimensions the p3 parameter defines a point through which
    the dimension line will go through.

    The current line width and color will be used.

    Linear dimension
     
    - (p1, p2, p3): a simple linear dimension from p1 to p2

    - (object, i1, i2, p3): creates a linked dimension to the provided
      object (edge), measuring the distance between its vertices
      indexed i1 and i2

    Circular dimension
     
    - (arc, i1, mode, p3): creates a linked dimension to the given arc
      object, i1 is the index of the arc edge that will be measured;
      mode is either "radius" or "diameter".



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_ellipse <small>(majradius, minradius, placement=None, face=None, support=None)</small>

make_ellipse(majradius, minradius, [placement], [face], [support])

    Makes an ellipse with the given major and minor radius, and optionally
    a placement.

    Parameters
     
    majradius :
        Major radius of the ellipse.

    minradius :
        Minor radius of the ellipse.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_facebinder <small>(selectionset, name='Facebinder')</small>

make_facebinder(selectionset, [name])

    Creates a Facebinder object from a selection set.

    Parameters
     
    selectionset :
        Only faces will be added.

    name : string (default = "Facebinder")
        Name of the created object



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_fillet <small>(objs, radius=100, chamfer=False, delete=False)</small>

Create a fillet between two lines or Part.Edges.

    Parameters
     
    objs: list
        List of two objects of type wire, or edges.

    radius: float, optional
        It defaults to 100. The curvature of the fillet.

    chamfer: bool, optional
        It defaults to `False`. If it is `True` it no longer produces
        a rounded fillet but a chamfer (straight edge)
        with the value of the `radius`.

    delete: bool, optional
        It defaults to `False`. If it is `True` it will delete
        the pair of objects that are used to create the fillet.
        Otherwise, the original objects will still be there.

    Returns
     
    Part::Part2DObjectPython
        The object of Proxy type `'Fillet'`.
        It returns `None` if it fails producing the object.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_hatch <small>(baseobject, filename, pattern, scale, rotation)</small>

Creates and returns a
    hatch object made by applying the given pattern of the given PAT file to the faces of
    the given base object. Given scale and rotation factors are applied to the hatch object.
    The result is a Part-based object created in the active document.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_label <small>(target_point=Vector (0.0, 0.0, 0.0), placement=Vector (30.0, 30.0, 0.0), target_object=None, subelements=None, label_type='Custom', custom_text='Label', direction='Horizontal', distance=-10, points=None)</small>

Create a Label object containing different types of information.

    The current color and text height and font specified in preferences
    are used.

    Parameters
     
    target_point: Base::Vector3, optional
        It defaults to the origin `App.Vector(0, 0, 0)`.
        This is the point which is pointed to by the label's leader line.
        This point can be adorned with a marker like an arrow or circle.

    placement: Base::Placement, Base::Vector3, or Base::Rotation, optional
        It defaults to `App.Vector(30, 30, 0)`.
        If it is provided, it defines the base point of the textual
        label.
        The input could be a full placement, just a vector indicating
        the translation, or just a rotation.

    target_object: Part::Feature or str, optional
        It defaults to `None`.
        If it exists it should be an object which will be used to provide
        information to the label, as long as `label_type` is different
        from `'Custom'`.

        If it is a string, it must be the `Label` of that object.
        Since a `Label` is not guaranteed to be unique in a document,
        it will use the first object found with this `Label`.

    subelements: str, optional
        It defaults to `None`.
        If `subelements` is provided, `target_object` should be provided
        as well, otherwise it is ignored.

        It should be a string indicating a subelement name, either
        `'VertexN'`, `'EdgeN'`, or `'FaceN'` which should exist
        within `target_object`.
        In this case `'N'` is an integer that indicates the specific number
        of vertex, edge, or face in `target_object`.

        Both `target_object` and `subelements` are used to link the label
        to a particular object, or to the particular vertex, edge, or face,
        and get information from them.
        ::
            make_label(..., target_object=App.ActiveDocument.Box)
            make_label(..., target_object="My box", subelements="Face3")

        These two parameters can be can be obtained from the `Gui::Selection`
        module.
        ::
            sel_object = Gui.Selection.getSelectionEx()[0]
            target_object = sel_object.Object
            subelements = sel_object.SubElementNames[0]

    label_type: str, optional
        It defaults to `'Custom'`.
        It indicates the type of information that will be shown in the label.
        See the get_label_types function in label.py for supported types.

        Only `'Custom'` allows you to manually set the text
        by defining `custom_text`. The other types take their information
        from the object included in `target`.

        - `'Position'` will show the base position of the target object,
          or of the indicated `'VertexN'` in `target`.
        - `'Length'` will show the `Length` of the target object's `Shape`,
          or of the indicated `'EdgeN'` in `target`.
        - `'Area'` will show the `Area` of the target object's `Shape`,
          or of the indicated `'FaceN'` in `target`.

    custom_text: str, or list of str, optional
        It defaults to `'Label'`.
        If it is a list, each element in the list represents a new text line.

        It is the text that will be displayed by the label when
        `label_type` is `'Custom'`.

    direction: str, optional
        It defaults to `'Horizontal'`.
        It can be `'Horizontal'`, `'Vertical'`, or `'Custom'`.
        It indicates the direction of the straight segment of the leader line
        that ends up next to the textual label.

        If `'Custom'` is selected, the leader line can be manually drawn
        by specifying the value of `points`.
        Normally, the leader line has only three points, but with `'Custom'`
        you can specify as many points as needed.

    distance: int, float, Base::Quantity, optional
        It defaults to -10.
        It indicates the length of the horizontal or vertical segment
        of the leader line.

        The leader line is composed of two segments, the first segment is
        inclined, while the second segment is either horizontal or vertical
        depending on the value of `direction`.
        ::
            T
            |
            |
            o  L text

        The `oL` segment's length is defined by `distance`
        while the `oT` segment is automatically calculated depending
        on the values of `placement` (L) and `distance` (o).

        This `distance` is oriented, meaning that if it is positive
        the segment will be to the right and above of the textual
        label, depending on if `direction` is `'Horizontal'` or `'Vertical'`,
        respectively.
        If it is negative, the segment will be to the left
        and below of the text.

    points: list of Base::Vector3, optional
        It defaults to `None`.
        It is a list of vectors defining the shape of the leader line;
        the list must have at least two points.
        This argument must be used together with `direction='Custom'`
        to display this custom leader.

        However, notice that if the Label's `StraightDirection` property
        is later changed to `'Horizontal'` or `'Vertical'`,
        the custom point list will be overwritten with a new,
        automatically calculated three-point list.

        For the object to use custom points, `StraightDirection`
        must remain `'Custom'`, and then the `Points` property
        can be overwritten by a suitable list of points.

    Returns
     
    App::FeaturePython
        A scripted object of type `'Label'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_layer <small>(name=None, line_color=None, shape_color=None, line_width=2.0, draw_style='Solid', transparency=0)</small>

Create a Layer object in the active document.

    If a layer container named `'LayerContainer'` does not exist,
    it is created with this name.

    A layer controls the view properties of the objects inside the layer,
    so all parameters except for `name` only apply if the graphical interface
    is up.

    Parameters
     
    name: str, optional
        It is used to set the layer's `Label` (user editable).
        It defaults to `None`, in which case the `Label`
        is set to `'Layer'` or to its translation in the current language.

    line_color: tuple, optional
        It defaults to `None`, in which case it uses the value of the parameter
        `User parameter:BaseApp/Preferences/View/DefaultShapeLineColor`.
        If it is given, it should be a tuple of three
        floating point values from 0.0 to 1.0.

    shape_color: tuple, optional
        It defaults to `None`, in which case it uses the value of the parameter
        `User parameter:BaseApp/Preferences/View/DefaultShapeColor`.
        If it is given, it should be a tuple of three
        floating point values from 0.0 to 1.0.

    line_width: float, optional
        It defaults to 2.0.
        It determines the width of the edges of the objects contained
        in the layer.

    draw_style: str, optional
        It defaults to `'Solid'`.
        It determines the style of the edges of the objects contained
        in the layer.
        If it is given, it should be 'Solid', 'Dashed', 'Dotted',
        or 'Dashdot'.

    transparency: int, optional
        It defaults to 0.
        It should be an integer value from 0 (completely opaque)
        to 100 (completely transparent).

    Return
     
    App::FeaturePython
        A scripted object of type `'Layer'`.
        This object does not have a `Shape` attribute.
        Modifying the view properties of this object will affect the objects
        inside of it.

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_line <small>(first_param, last_param=None)</small>

makeLine(first_param, p2)

    Creates a line from 2 points or from a given object.

    Parameters
     
    first_param :
        Base.Vector -> First point of the line (if p2 is None)
        Part.LineSegment -> Line is created from the given Linesegment
        Shape -> Line is created from the give Shape

    last_param : Base.Vector
        Second point of the line, if not set the function evaluates
        the first_param to look for a Part.LineSegment or a Shape



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_linear_dimension <small>(p1, p2, dim_line=None)</small>

Create a free linear dimension from two main points.

    Parameters
     
    p1: Base::Vector3
        First point of the measurement.

    p2: Base::Vector3
        Second point of the measurement.

    dim_line: Base::Vector3, optional
        It defaults to `None`.
        This is a point through which the extension of the dimension line
        will pass.
        This point controls how close or how far the dimension line is
        positioned from the measured segment that goes from `p1` to `p2`.

        If it is `None`, this point will be calculated from the intermediate
        distance between `p1` and `p2`.

    Returns
     
    App::FeaturePython
        A scripted object of type `'LinearDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_linear_dimension_obj <small>(edge_object, i1=1, i2=2, dim_line=None)</small>

Create a linear dimension from an object.

    Parameters
     
    edge_object: Part::Feature
        The object which has an edge which will be measured.
        It must have a `Part::TopoShape`, and at least one element
        in `Shape.Vertexes`, to be able to measure a distance.

    i1: int, optional
        It defaults to `1`.
        It is the index of the first vertex in `edge_object` from which
        the measurement will be taken.
        The minimum value should be `1`, which will be interpreted
        as `'Vertex1'`.

        If the value is below `1`, it will be set to `1`.

    i2: int, optional
        It defaults to `2`, which will be converted to `'Vertex2'`.
        It is the index of the second vertex in `edge_object` that determines
        the endpoint of the measurement.

        If it is the same value as `i1`, the resulting measurement will be
        made from the origin `(0, 0, 0)` to the vertex indicated by `i1`.

        If the value is below `1`, it will be set to the last vertex
        in `edge_object`.

        Then to measure the first and last, this could be used
        ::
            make_linear_dimension_obj(edge_object, i1=1, i2=-1)

    dim_line: Base::Vector3
        It defaults to `None`.
        This is a point through which the extension of the dimension line
        will pass.
        This point controls how close or how far the dimension line is
        positioned from the measured segment in `edge_object`.

        If it is `None`, this point will be calculated from the intermediate
        distance between the vertices defined by `i1` and `i2`.

    Returns
     
    App::FeaturePython
        A scripted object of type `'LinearDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_ortho_array <small>(base_object, v_x=Vector (10.0, 0.0, 0.0), v_y=Vector (0.0, 10.0, 0.0), v_z=Vector (0.0, 0.0, 10.0), n_x=2, n_y=2, n_z=1, use_link=True)</small>

Create an orthogonal array from the given object.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    v_x, v_y, v_z: Base::Vector3, optional
        The vector indicating the vector displacement between two elements
        in the specified orthogonal direction X, Y, Z.

        By default:
        ::
            v_x = App.Vector(10, 0, 0)
            v_y = App.Vector(0, 10, 0)
            v_z = App.Vector(0, 0, 10)

        Given that this is a vectorial displacement
        the next object can appear displaced in one, two or three axes
        at the same time.

        For example
        ::
            v_x = App.Vector(10, 5, 0)

        means that the next element in the X direction will be displaced
        10 mm in X, 5 mm in Y, and 0 mm in Z.

        A traditional "rectangular" array is obtained when
        the displacement vector only has its corresponding component,
        like in the default case.

        If these values are entered as single numbers instead
        of vectors, the single value is expanded into a vector
        of the corresponding direction, and the other components are assumed
        to be zero.

        For example
        ::
            v_x = 15
            v_y = 10
            v_z = 1
        becomes
        ::
            v_x = App.Vector(15, 0, 0)
            v_y = App.Vector(0, 10, 0)
            v_z = App.Vector(0, 0, 1)

    n_x, n_y, n_z: int, optional
        The number of copies in the specified orthogonal direction X, Y, Z.
        This number includes the original object, therefore, it must be
        at least 1.

        The values of `n_x` and `n_y` default to 2,
        while `n_z` defaults to 1.
        This means the array is a planar array by default.

    use_link: bool, optional
        It defaults to `True`.
        If it is `True` the produced copies are not `Part::TopoShape` copies,
        but rather `App::Link` objects.
        The Links repeat the shape of the original `base_object` exactly,
        and therefore the resulting array is more memory efficient.

        Also, when `use_link` is `True`, the `Fuse` property
        of the resulting array does not work; the array doesn't
        contain separate shapes, it only has the original shape repeated
        many times, so there is nothing to fuse together.

        If `use_link` is `False` the original shape is copied many times.
        In this case the `Fuse` property is able to fuse
        all copies into a single object, if they touch each other.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.

    See Also
     
    make_ortho_array2d, make_rect_array, make_rect_array2d, make_polar_array,
    make_circular_array, make_path_array, make_point_array



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_ortho_array2d <small>(base_object, v_x=Vector (10.0, 0.0, 0.0), v_y=Vector (0.0, 10.0, 0.0), n_x=2, n_y=2, use_link=True)</small>

Create a 2D orthogonal array from the given object.

    This works the same as `make_ortho_array`.
    The Z component is ignored so it only considers vector displacements
    in X and Y directions.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    v_x, v_y: Base::Vector3, optional
        Vectorial displacement of elements
        in the corresponding X and Y directions.
        See `make_ortho_array`.

    n_x, n_y: int, optional
        Number of elements
        in the corresponding X and Y directions.
        See `make_ortho_array`.

    use_link: bool, optional
        If it is `True`, create `App::Link` array.
        See `make_ortho_array`.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.

    See Also
     
    make_ortho_array, make_rect_array, make_rect_array2d, make_polar_array,
    make_circular_array, make_path_array, make_point_array



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_path_array <small>(base_object, path_object, count=4, extra=Vector (0.0, 0.0, 0.0), subelements=None, align=False, align_mode='Original', tan_vector=Vector (1.0, 0.0, 0.0), force_vertical=False, vertical_vector=Vector (0.0, 0.0, 1.0), start_offset=0.0, end_offset=0.0, use_link=True)</small>

Make a Draft PathArray object.

    Distribute copies of a `base_object` along `path_object`
    or `subelements` from `path_object`.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    path_object: Part::Feature or str
        Path object like a polyline, B-Spline, or bezier curve that should
        contain edges.
        Just like `base_object` it can also be `Label`.

    count: int, float, optional
        It defaults to 4.
        Number of copies to create along the `path_object`.
        It must be at least 2.
        If a `float` is provided, it will be truncated by `int(count)`.

    extra: Base.Vector3, optional
        It defaults to `App.Vector(0, 0, 0)`.
        It translates each copy by the value of `extra`.
        This is useful to adjust for the difference between shape centre
        and shape reference point.

    subelements: list or tuple of str, optional
        It defaults to `None`.
        It should be a list of names of edges that must exist in `path_object`.
        Then the path array will be created along these edges only,
        and not the entire `path_object`.
        ::
            subelements = ['Edge1', 'Edge2']

        The edges must be contiguous, meaning that it is not allowed to
        input `'Edge1'` and `'Edge3'` if they do not touch each other.

        A single string value is also allowed.
        ::
            subelements = 'Edge1'

    align: bool, optional
        It defaults to `False`.
        If it is `True` it will align `base_object` to tangent, normal,
        or binormal to the `path_object`, depending on the value
        of `tan_vector`.

    align_mode: str, optional
        It defaults to `'Original'` which is the traditional alignment.
        It can also be `'Frenet'` or `'Tangent'`.

        - Original. It does not calculate curve normal.
          `X` is curve tangent, `Y` is normal parameter, Z is the cross
          product `X` x `Y`.
        - Frenet. It defines a local coordinate system along the path.
          `X` is tangent to curve, `Y` is curve normal, `Z` is curve binormal.
          If normal cannot be computed, for example, in a straight path,
          a default is used.
        - Tangent. It is similar to `'Original'` but includes a pre-rotation
          to align the base object's `X` to the value of `tan_vector`,
          then `X` follows curve tangent.

    tan_vector: Base::Vector3, optional
        It defaults to `App.Vector(1, 0, 0)` or the +X axis.
        It aligns the tangent of the path to this local unit vector
        of the object.

    force_vertical: Base::Vector3, optional
        It defaults to `False`.
        If it is `True`, the value of `vertical_vector`
        will be used when `align_mode` is `'Original'` or `'Tangent'`.

    vertical_vector: Base::Vector3, optional
        It defaults to `App.Vector(0, 0, 1)` or the +Z axis.
        It will force this vector to be the vertical direction
        when `force_vertical` is `True`.

    start_offset: float, optional
        It defaults to 0.0.
        It is the length from the start of the path to the first copy.

    end_offset: float, optional
        It defaults to 0.0.
        It is the length from the end of the path to the last copy.

    use_link: bool, optional
        It defaults to `True`, in which case the copies are `App::Link`
        elements. Otherwise, the copies are shape copies which makes
        the resulting array heavier.

    Returns
     
    Part::FeaturePython
        The scripted object of type `'PathArray'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_path_twisted_array <small>(base_object, path_object, count=15, rot_factor=0.25, use_link=True)</small>

Create a Path twisted array.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_point <small>(X=0, Y=0, Z=0, color=None, name='Point', point_size=5)</small>

make_point(x, y, z, [color(r, g, b), point_size]) or
        make_point(Vector, color(r, g, b), point_size])

    Creates a Draft Point in the current document.

    Parameters
     
    X :
        float -> X coordinate of the point
        Base.Vector -> Ignore Y and Z coordinates and create the point
            from the vector.

    Y : float
        Y coordinate of the point

    Z : float
        Z coordinate of the point

    color : (R, G, B)
        Point color as RGB
        example to create a colored point:
        make_point(0, 0, 0, (1, 0, 0)) # color = red
        example to change the color, make sure values are floats:
        p1.ViewObject.PointColor = (0.0, 0.0, 1.0)



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_point_array <small>(base_object, point_object, extra=None, use_link=True)</small>

Make a Draft PointArray object.

    Create copies of a `base_object` at the points defined by
    a `point_object`.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    point_object: Part::Feature, Sketcher::SketchObject, Mesh::Feature,
                  Points::FeatureCustom or str
        The object must have vertices and/or points.

    extra: Base::Placement, Base::Vector3, or Base::Rotation, optional
        It defaults to `None`.
        If it is provided, it is an additional placement that is applied
        to each copy of the array.
        The input could be a full placement, just a vector indicating
        the additional translation, or just a rotation.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'PointArray'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_polar_array <small>(base_object, number=5, angle=360, center=Vector (0.0, 0.0, 0.0), use_link=True)</small>

Create a polar array from the given object.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    number: int, optional
        It defaults to 5.
        The number of copies produced in the polar pattern.

    angle: float, optional
        It defaults to 360.
        The magnitude in degrees swept by the polar pattern.

    center: Base::Vector3, optional
        It defaults to the origin `App.Vector(0, 0, 0)`.
        The vector indicating the center of rotation of the array.

    use_link: bool, optional
        It defaults to `True`.
        If it is `True` the produced copies are not `Part::TopoShape` copies,
        but rather `App::Link` objects.
        The Links repeat the shape of the original `obj` exactly,
        and therefore the resulting array is more memory efficient.

        Also, when `use_link` is `True`, the `Fuse` property
        of the resulting array does not work; the array doesn't
        contain separate shapes, it only has the original shape repeated
        many times, so there is nothing to fuse together.

        If `use_link` is `False` the original shape is copied many times.
        In this case the `Fuse` property is able to fuse
        all copies into a single object, if they touch each other.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.

    See Also
     
    make_ortho_array, make_circular_array, make_path_array, make_point_array



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_polygon <small>(nfaces, radius=1, inscribed=True, placement=None, face=None, support=None)</small>

makePolgon(edges,[radius],[inscribed],[placement],[face])

    Creates a polygon object with the given number of edges and radius.

    Parameters
     
    edges : int
        Number of edges of the polygon.

    radius :
        Radius of the control circle.

    inscribed : bool
        Defines is the polygon is inscribed or not into the control circle.

    placement : Base.Placement
        If placement is given, it is used.

    face : bool
        If face is True, the resulting shape is displayed as a face,
        otherwise as a wireframe.

    support :
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_radial_dimension_obj <small>(edge_object, index=1, mode='radius', dim_line=None)</small>

Create a radial or diameter dimension from an arc object.

    Parameters
     
    edge_object: Part::Feature
        The object which has a circular edge which will be measured.
        It must have a `Part::TopoShape`, and at least one element
        must be a circular edge in `Shape.Edges` to be able to measure
        its radius.

    index: int, optional
        It defaults to `1`.
        It is the index of the edge in `edge_object` which is going to
        be measured.
        The minimum value should be `1`, which will be interpreted
        as `'Edge1'`. If the value is below `1`, it will be set to `1`.

    mode: str, optional
        It defaults to `'radius'`; the other option is `'diameter'`.
        It determines whether the dimension will be shown as a radius
        or as a diameter.

    dim_line: Base::Vector3, optional
        It defaults to `None`.
        This is a point through which the extension of the dimension line
        will pass. The dimension line will be a radius or diameter
        of the measured arc, extending from the center to the arc itself.

        If it is `None`, this point will be set to one unit to the right
        of the center of the arc, which will create a dimension line that is
        horizontal, that is, parallel to the +X axis.

    Returns
     
    App::FeaturePython
        A scripted object of type `'LinearDimension'`.
        This object does not have a `Shape` attribute, as the text and lines
        are created on screen by Coin (pivy).

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_rect_array <small>(base_object, d_x=10, d_y=10, d_z=10, n_x=2, n_y=2, n_z=1, use_link=True)</small>

Create a rectangular array from the given object.

    This function wraps around `make_ortho_array`
    to produce strictly rectangular arrays, in which
    the displacement vectors `v_x`, `v_y`, and `v_z`
    only have their respective components in X, Y, and Z.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    d_x, d_y, d_z: Base::Vector3, optional
        Displacement of elements in the corresponding X, Y, and Z directions.

    n_x, n_y, n_z: int, optional
        Number of elements in the corresponding X, Y, and Z directions.

    use_link: bool, optional
        If it is `True`, create `App::Link` array.
        See `make_ortho_array`.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.

    See Also
     
    make_ortho_array, make_ortho_array2d, make_rect_array2d, make_polar_array,
    make_circular_array, make_path_array, make_point_array



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_rect_array2d <small>(base_object, d_x=10, d_y=10, n_x=2, n_y=2, use_link=True)</small>

Create a 2D rectangular array from the given object.

    This function wraps around `make_ortho_array`,
    to produce strictly rectangular arrays, in which
    the displacement vectors `v_x` and `v_y`
    only have their respective components in X and Y.
    The Z component is ignored.

    Parameters
     
    base_object: Part::Feature or str
        Any of object that has a `Part::TopoShape` that can be duplicated.
        This means most 2D and 3D objects produced with any workbench.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.

    d_x, d_y: Base::Vector3, optional
        Displacement of elements in the corresponding X and Y directions.

    n_x, n_y: int, optional
        Number of elements in the corresponding X and Y directions.

    use_link: bool, optional
        If it is `True`, create `App::Link` array.
        See `make_ortho_array`.

    Returns
     
    Part::FeaturePython
        A scripted object of type `'Array'`.
        Its `Shape` is a compound of the copies of the original object.

    None
        If there is a problem it will return `None`.

    See Also
     
    make_ortho_array, make_ortho_array2d, make_rect_array, make_polar_array,
    make_circular_array, make_path_array, make_point_array



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_rectangle <small>(length, height=0, placement=None, face=None, support=None)</small>

make_rectangle(length, width, [placement], [face])

    Creates a Rectangle object with length in X direction and height in Y
    direction.

    Parameters
     
    length, height : dimensions of the rectangle

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    Rectangles can also be constructed by giving them a list of four vertices
    as first argument: make_rectangle(list_of_vertices, face=...)
    but you are responsible to check yourself that these 4 vertices are ordered
    and actually form a rectangle, otherwise the result might be wrong. Placement
    is ignored when constructing a rectangle this way (face argument is kept).



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_shape2dview <small>(baseobj, projectionVector=None, facenumbers=[])</small>

make_shape2dview(object, [projectionVector], [facenumbers])

    Add a 2D shape to the document, which is a 2D projection of the given object.

    Parameters
     
    object :
        TODO: Describe

    projectionVector : Base.Vector
        Custom vector for the projection

    facenumbers : [] TODO: Describe
        A list of face numbers to be considered in individual faces mode.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_shapestring <small>(String, FontFile, Size=100, Tracking=0)</small>

ShapeString(Text,FontFile,[Height],[Track])

    Turns a text string into a Compound Shape

    Parameters
     
    majradius :
        Major radius of the ellipse.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_sketch <small>(objects_list, autoconstraints=False, addTo=None, delete=False, name='Sketch', radiusPrecision=-1, tol=0.001)</small>

make_sketch(objects_list, [autoconstraints], [addTo], [delete],
                   [name], [radiusPrecision], [tol])

    Makes a Sketch objects_list with the given Draft objects.

    Parameters
     
    objects_list: can be single or list of objects of Draft type objects,
        Part::Feature, Part.Shape, or mix of them.

    autoconstraints(False): if True, constraints will be automatically added to
        wire nodes, rectangles and circles.

    addTo(None) : if set to an existing sketch, geometry will be added to it
        instead of creating a new one.

    delete(False): if True, the original object will be deleted.
        If set to a string 'all' the object and all its linked object will be
        deleted.

    name('Sketch'): the name for the new sketch object.

    radiusPrecision(-1): If <0, disable radius constraint. If =0, add individual
        radius constraint. If >0, the radius will be rounded according to this
        precision, and 'Equal' constraint will be added to curve with equal
        radius within precision.

    tol(1e-3): Tolerance used to check if the shapes are planar and coplanar.
        Consider change to tol=-1 for a more accurate analysis.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_text <small>(string, placement=None, screen=False, height=None, line_spacing=1)</small>

Create a Text object containing the given list of strings.

    The current color and text height and font specified in preferences
    are used.

    Parameters
     
    string: str, or list of str
        String to display on screen.
        If it is a list, each element in the list represents a new text line.

    placement: Base::Placement, Base::Vector3, or Base::Rotation, optional
        Defaults to `None`.
        If it is provided, it is the placement of the new text.
        The input could be a full placement, just a vector indicating
        the translation, or just a rotation.

    screen: bool or None, optional
        Defaults to `False`.
        If it is `True`, the DisplayMode is set to "Screen".
        If it is `False`, it is set to "World".
        If it is `None`, the DisplayMode depends on the current preferences.

    height: float or None, optional
        Defaults to `None`.
        A height value for the text, in mm.
        If it is `None` or zero, the FontSize depends on the current preferences.

    line_spacing: float or None, optional
        Defaults to 1.
        The line spacing factor.
        If it is `None` or zero, the LineSpacing depends on the current preferences.

    Returns
     
    App::FeaturePython
        A scripted object of type `'Text'`.
        This object does not have a `Shape` attribute, as the text is created
        on screen by Coin (pivy).

    None
        If there is a problem it will return `None`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_wire <small>(pointslist, closed=False, placement=None, face=None, support=None, bs2wire=False)</small>

make_wire(pointslist, [closed], [placement])

    Creates a Wire object from the given list of vectors.  If face is
    true (and wire is closed), the wire will appear filled. Instead of
    a pointslist, you can also pass a Part Wire.

    Parameters
     
    pointslist : [Base.Vector]
        List of points to create the polyline

    closed : bool
        If closed is True or first and last points are identical,
        the created polyline will be closed.

    placement : Base.Placement
        If a placement is given, it is used.

    face : Bool
        If face is False, the rectangle is shown as a wireframe,
        otherwise as a face.

    support :
        TODO: Describe

    bs2wire : bool
        TODO: Describe



#### <img src="images/Arrow-right.svg" style="width:16px;"> make_workingplaneproxy <small>(placement)</small>

make_working_plane_proxy(placement)

    Creates a Working Plane proxy object in the current document.

    Parameters
     
    placement : Base.Placement
        specify the p.



#### <img src="images/Arrow-right.svg" style="width:16px;"> mirror <small>(objlist, p1, p2)</small>

Create a mirror object from the provided list and line.

    It creates a `Part::Mirroring` object from the given `objlist` using
    a plane that is defined by the two given points `p1` and `p2`,
    and the Draft working plane normal.

    Parameters
     
    objlist: single object or a list of objects
        A single object or a list of objects.

    p1: Base::Vector3
        Point 1 of the mirror plane. It is also used as the `Placement.Base`
        of the resulting object.

    p2: Base::Vector3
        Point 2 of the mirror plane.

    Returns
     
    None
        If the operation fails.

    list
        List of `Part::Mirroring` objects, or a single one
        depending on the input `objlist`.

    To Do
     
    Implement a mirror tool specific to the workbench that does not
    just use `Part::Mirroring`. It should create a derived object,
    that is, it should work similar to `Draft.offset`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> move <small>(objectslist, vector, copy=False)</small>

move(objects,vector,[copy])

    Move the objects contained in objects (that can be an object or a
    list of objects) in the direction and distance indicated by the given
    vector.

    Parameters
     
    objectslist : list

    vector : Base.Vector
        Delta Vector to move the clone from the original position.

    copy : bool
        If copy is True, the actual objects are not moved, but copies
        are created instead.

    Return
     
    The objects (or their copies) are returned.



#### <img src="images/Arrow-right.svg" style="width:16px;"> moveEdge <small>(object, edge_index, vector)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> moveVertex <small>(object, vertex_index, vector)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> move_edge <small>(object, edge_index, vector)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> move_vertex <small>(object, vertex_index, vector)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> offset <small>(obj, delta, copy=False, bind=False, sym=False, occ=False)</small>

offset(object,delta,[copymode],[bind])

    Offset the given wire by applying the given delta Vector to its first
    vertex.

    Parameters
     
    obj :

    delta : Base.Vector or list of Base.Vector
        If offsetting a BSpline, the delta must not be a Vector but a list
        of Vectors, one for each node of the spline.

    copy : bool
        If copymode is True, another object is created, otherwise the same
        object gets offsetted.

    copy : bool
        If bind is True, and provided the wire is open, the original
        and the offset wires will be bound by their endpoints, forming a face.

    sym : bool
        if sym is True, bind must be true too, and the offset is made on both
        sides, the total width being the given delta length.



#### <img src="images/Arrow-right.svg" style="width:16px;"> precision <small>()</small>

Return the precision value from the parameter database.

    It is the number of decimal places that a float will have.
    Example
    ::
        precision=6, 0.123456
        precision=5, 0.12345
        precision=4, 0.1234

    Due to floating point operations there may be rounding errors.
    Therefore, this precision number is used to round up values
    so that all operations are consistent.
    By default the precision is 6 decimal places.

    Returns
     
    int
        params.get_param("precision")



#### <img src="images/Arrow-right.svg" style="width:16px;"> printShape <small>(shape)</small>

Print detailed information of a topological shape.

    Parameters
     
    shape : Part::TopoShape
        Any topological shape in an object, usually obtained from `obj.Shape`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> print_shape <small>(shape)</small>

Print detailed information of a topological shape.

    Parameters
     
    shape : Part::TopoShape
        Any topological shape in an object, usually obtained from `obj.Shape`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> removeHidden <small>(objectslist)</small>

Return only the visible objects in the list.

    This function only works if the graphical interface is available
    as the `Visibility` attribute is a property of the view provider
    (`obj.ViewObject`).

    Parameters
     
    objectslist: list of App::DocumentObject
        List of any type of object.

    Returns
     
    list
        Return a copy of the input list without those objects
        for which `obj.ViewObject.Visibility` is `False`.

        If the graphical interface is not loaded
        the returned list is just a copy of the input list.



#### <img src="images/Arrow-right.svg" style="width:16px;"> remove_hidden <small>(objectslist)</small>

Return only the visible objects in the list.

    This function only works if the graphical interface is available
    as the `Visibility` attribute is a property of the view provider
    (`obj.ViewObject`).

    Parameters
     
    objectslist: list of App::DocumentObject
        List of any type of object.

    Returns
     
    list
        Return a copy of the input list without those objects
        for which `obj.ViewObject.Visibility` is `False`.

        If the graphical interface is not loaded
        the returned list is just a copy of the input list.



#### <img src="images/Arrow-right.svg" style="width:16px;"> rgba_to_argb <small>(color)</small>

Change byte order of a 4 byte color int from RGBA (FreeCAD) to ARGB (Qt).



#### <img src="images/Arrow-right.svg" style="width:16px;"> rotate <small>(objectslist, angle, center=Vector (0.0, 0.0, 0.0), axis=Vector (0.0, 0.0, 1.0), copy=False)</small>

rotate(objects,angle,[center,axis,copy])

    Rotates the objects contained in objects (that can be a list of objects
    or an object) of the given angle (in degrees) around the center, using
    axis as a rotation axis.

    Parameters
     
    objectslist : list

    angle : rotation angle (in degrees)

    center : Base.Vector

    axis : Base.Vector
        If axis is omitted, the rotation will be around the vertical Z axis.

    copy : bool
        If copy is True, the actual objects are not moved, but copies
        are created instead.

    Return
     
    The objects (or their copies) are returned.



#### <img src="images/Arrow-right.svg" style="width:16px;"> rotateEdge <small>(object, edge_index, angle, center, axis)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> rotateVertex <small>(object, vertex_index, angle, center, axis)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> rotate_edge <small>(object, edge_index, angle, center, axis)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> rotate_vertex <small>(object, vertex_index, angle, center, axis)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> scale <small>(objectslist, scale=Vector (1.0, 1.0, 1.0), center=Vector (0.0, 0.0, 0.0), copy=False)</small>

scale(objects, scale, [center], copy)

    Scales the objects contained in objects (that can be a list of objects or
    an object) of the given  around given center.

    Parameters
     
    objectlist : list

     Base.Vector
        Scale factors defined by a given vector (in X, Y, Z directions).

    objectlist : Base.Vector
        Center of the scale operation.

    copy : bool
        If copy is True, the actual objects are not scaled, but copies
        are created instead.

    Return
     
    The objects (or their copies) are returned.



#### <img src="images/Arrow-right.svg" style="width:16px;"> scaleEdge <small>(obj, edge_index, scale, center)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> scaleVertex <small>(obj, vertex_index, scale, center)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> scale_edge <small>(obj, edge_index, scale, center)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> scale_vertex <small>(obj, vertex_index, scale, center)</small>

Needed for SubObjects modifiers.
    Implemented by Dion Moult during 0.19 dev cycle (works only with Draft Wire).



#### <img src="images/Arrow-right.svg" style="width:16px;"> select <small>(objs=None, gui=0)</small>

Unselects everything and selects only the given list of objects.

    This function only works if the graphical interface is available
    as the selection module only works on the 3D view.

    Parameters
     
    objs: list of App::DocumentObject, optional
        It defaults to `None`.
        Any type of scripted object.
        It may be a list of objects or a single object.

    gui: bool, optional
        It defaults to the value of `App.GuiUp`, which is `True`
        when the interface exists, and `False` otherwise.

        This value can be set to `False` to simulate
        when the interface is not available.



#### <img src="images/Arrow-right.svg" style="width:16px;"> setParam <small>(param, value)</small>

Set a Draft parameter with the given value.

    The parameter database is located in the tree
    ::
        'User parameter:BaseApp/Preferences/Mod/Draft'

    In the case that `param` is `'linewidth'` or `'color'` it will set
    the View parameters
    ::
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

    Parameters
     
    param : str
        A string that indicates a parameter in the parameter database.

    value : int, or str, or float, or bool
        The appropriate value of the parameter.
        Depending on `param` and its type, determined with `get_param_type`,
        it sets the appropriate value by calling `ParameterGrp.SetInt`,
        `ParameterGrp.SetString`, `ParameterGrp.SetFloat`,
        `ParameterGrp.SetBool`, or `ParameterGrp.SetUnsinged`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> set_param <small>(param, value)</small>

Set a Draft parameter with the given value.

    The parameter database is located in the tree
    ::
        'User parameter:BaseApp/Preferences/Mod/Draft'

    In the case that `param` is `'linewidth'` or `'color'` it will set
    the View parameters
    ::
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineWidth'
        'User parameter:BaseApp/Preferences/View/DefaultShapeLineColor'

    Parameters
     
    param : str
        A string that indicates a parameter in the parameter database.

    value : int, or str, or float, or bool
        The appropriate value of the parameter.
        Depending on `param` and its type, determined with `get_param_type`,
        it sets the appropriate value by calling `ParameterGrp.SetInt`,
        `ParameterGrp.SetString`, `ParameterGrp.SetFloat`,
        `ParameterGrp.SetBool`, or `ParameterGrp.SetUnsinged`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> shapify <small>(obj)</small>

Transform a parametric object into a static, non-parametric shape.

    Parameters
     
    obj : App::DocumentObject
        Any type of scripted object.

        This object will be removed, and a non-parametric object
        with the same topological shape (`Part::TopoShape`)
        will be created.

    Returns
     
    Part::Feature
        The new object that takes `obj.Shape` as its own.

        Depending on the contents of the Shape, the resulting object
        will be named `'Face'`, `'Solid'`, `'Compound'`,
        `'Shell'`, `'Wire'`, `'Line'`, `'Circle'`,
        or the name returned by `get_real_name(obj.Name)`.

        If there is a problem with `obj.Shape`, it will return `None`,
        and the original object will not be modified.



#### <img src="images/Arrow-right.svg" style="width:16px;"> split <small>(wire, newPoint, edgeIndex)</small>





#### <img src="images/Arrow-right.svg" style="width:16px;"> string_encode_coin <small>(ustr)</small>

Encode a unicode object to be used as a string in coin.

    Parameters
     
    ustr : str
        A string to be encoded

    Returns
     
    str
        Encoded string. If the coin version is >= 4
        it will encode the string to `'utf-8'`, otherwise
        it will encode it to `'latin-1'`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> stringencodecoin <small>(ustr)</small>

Encode a unicode object to be used as a string in coin.

    Parameters
     
    ustr : str
        A string to be encoded

    Returns
     
    str
        Encoded string. If the coin version is >= 4
        it will encode the string to `'utf-8'`, otherwise
        it will encode it to `'latin-1'`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> svg_patterns <small>()</small>

Return a dictionary with installed SVG patterns.

    Returns
     
    dict
        Returns `App.svgpatterns` if it exists.
        Otherwise it calls `load_svg_patterns` to create it
        before returning it.



#### <img src="images/Arrow-right.svg" style="width:16px;"> svgpatterns <small>()</small>

Return a dictionary with installed SVG patterns.

    Returns
     
    dict
        Returns `App.svgpatterns` if it exists.
        Otherwise it calls `load_svg_patterns` to create it
        before returning it.



#### <img src="images/Arrow-right.svg" style="width:16px;"> tolerance <small>()</small>

Return a tolerance based on the precision() value

    Returns
     
    float
        10 ** -precision()



#### <img src="images/Arrow-right.svg" style="width:16px;"> type_check <small>(args_and_types, name='?')</small>

Check that the arguments are instances of certain types.

    Parameters
     
    args_and_types : list
        A list of tuples. The first element of a tuple is tested as being
        an instance of the second element.
        ::
            args_and_types = [(a, Type), (b, Type2), ...]

        Then
        ::
            isinstance(a, Type)
            isinstance(b, Type2)

        A `Type` can also be a tuple of many types, in which case
        the check is done for any of them.
        ::
            args_and_types = [(a, (Type3, int, float)), ...]

            isinstance(a, (Type3, int, float))

    name : str, optional
        Defaults to `'?'`. The name of the check.

    Raises
     
    TypeError
        If the first element in the tuple is not an instance of the second
        element, it raises `Draft.name`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> typecheck <small>(args_and_types, name='?')</small>

Check that the arguments are instances of certain types.

    Parameters
     
    args_and_types : list
        A list of tuples. The first element of a tuple is tested as being
        an instance of the second element.
        ::
            args_and_types = [(a, Type), (b, Type2), ...]

        Then
        ::
            isinstance(a, Type)
            isinstance(b, Type2)

        A `Type` can also be a tuple of many types, in which case
        the check is done for any of them.
        ::
            args_and_types = [(a, (Type3, int, float)), ...]

            isinstance(a, (Type3, int, float))

    name : str, optional
        Defaults to `'?'`. The name of the check.

    Raises
     
    TypeError
        If the first element in the tuple is not an instance of the second
        element, it raises `Draft.name`.



#### <img src="images/Arrow-right.svg" style="width:16px;"> ungroup <small>(obj)</small>

Remove the object from any group to which it belongs.

    A "group" is any object returned by `get_group_names`.

    Parameters
     
    obj: App::DocumentObject or str
        Any type of object.
        If it is a string, it must be the `Label` of that object.
        Since a label is not guaranteed to be unique in a document,
        it will use the first object found with this label.



#### <img src="images/Arrow-right.svg" style="width:16px;"> upgrade <small>(objects, delete=False, force=None)</small>

Upgrade the given objects.

    This is a counterpart to `downgrade`.

    Parameters
     
    objects: Part::Feature or list
        A single object to upgrade or a list
        containing various such objects.

    delete: bool, optional
        It defaults to `False`.
        If it is `True`, the old objects are deleted, and only the resulting
        object is kept.

    force: str, optional
        It defaults to `None`.
        Its value can be used to force a certain method of upgrading.
        It can be any of: `'makeCompound'`, `'closeGroupWires'`,
        `'makeSolid'`, `'closeWire'`, `'turnToParts'`, `'makeFusion'`,
        `'makeShell'`, `'makeFaces'`, `'draftify'`, `'joinFaces'`,
        `'makeSketchFace'`, `'makeWires'`.

    Returns
     
    tuple
        A tuple containing two lists, a list of new objects
        and a list of objects to be deleted.

    None
        If there is a problem it will return `None`.

    See Also
     
    downgrade



#### <img src="images/BIM_Column.svg" style="width:16px;"> AngularDimension <small>(obj)</small>

The angular dimension object.

    This inherits `DimensionBase` to provide the basic functionality of
    a dimension.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Array <small>(obj)</small>

The Draft Array object.

    To Do
     
    The `Array` class currently handles three types of arrays,
    orthogonal, polar, and circular. In the future, probably they should be
    split in separate classes so that they are easier to manage.



#### <img src="images/BIM_Column.svg" style="width:16px;"> BSpline <small>(obj)</small>

The BSpline object



#### <img src="images/BIM_Column.svg" style="width:16px;"> BezCurve <small>(obj)</small>

The BezCurve object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Block <small>(obj)</small>

The Block object



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Circle](Circle_API.md) <small>(obj)</small>

The Circle object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Clone <small>(obj)</small>

The Clone object



#### <img src="images/BIM_Column.svg" style="width:16px;"> DraftLabel <small>(obj)</small>

The Draft Label object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> DraftLink <small>(obj, tp)</small>

New class to use the App::Link objects in arrays.

    Introduced by realthunder.
    This is subclassed by `draftobjects.array.Array`
    and by `draftobjects.patharray.PathArray`.



#### <img src="images/BIM_Column.svg" style="width:16px;"> DraftObject <small>(obj, tp='Unknown')</small>

The base class for Draft objects.

    Parameters
     
    obj : a base C++ object
        The base object instantiated during creation,
        which commonly may be of types `Part::Part2DObjectPython`,
        `Part::FeaturePython`, or `App::FeaturePython`.

            >>> obj = App.ActiveDocument.addObject('Part::Part2DObjectPython')
            >>> DraftObject(obj)

        This class instance is stored in the `Proxy` attribute
        of the base object.
        ::
            obj.Proxy = self

    tp : str, optional
        It defaults to `'Unknown'`.
        It indicates the type of this scripted object,
        which will be assigned to the Proxy's `Type` attribute.

        This is useful to distinguish different types of scripted objects
        that may be derived from the same C++ class.

    Attributes
     
    Type : str
        It indicates the type of scripted object.
        Normally `Type = tp`.

        All objects have a `TypeId` attribute, but this attribute
        refers to the C++ class only. Using the `Type` attribute
        allows distinguishing among various types of objects
        derived from the same C++ class.

            >>> print(A.TypeId, "->", A.Proxy.Type)
            Part::Part2DObjectPython -> Wire
            >>> print(B.TypeId, "->", B.Proxy.Type)
            Part::Part2DObjectPython -> Circle

    This class attribute is accessible through the `Proxy` object:
    `obj.Proxy.Type`.



#### <img src="images/BIM_Column.svg" style="width:16px;"> DraftText <small>(obj)</small>

The Draft Text object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Ellipse](Ellipse_API.md) <small>(obj)</small>

The Circle object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Facebinder <small>(obj)</small>

The Draft Facebinder object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Fillet <small>(obj)</small>

Proxy class for the Fillet object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Hatch <small>(obj)</small>





#### <img src="images/BIM_Column.svg" style="width:16px;"> Label <small>(obj)</small>

The Draft Label object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Layer <small>(obj)</small>

The Layer object.

    This class is normally used to extend a base `App::FeaturePython` object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> LinearDimension <small>(obj)</small>

The linear dimension object.

    This inherits `DimensionBase` to provide the basic functionality of
    a dimension.

    This linear dimension includes measurements between two vertices,
    but also a radial dimension of a circular edge or arc.



#### <img src="images/BIM_Column.svg" style="width:16px;"> PathArray <small>(obj)</small>

The Draft Path Array object.

    The object distributes copies of an object along a path like a polyline,
    spline, or bezier curve.

    Attributes
     
    Align: bool
        It defaults to `False`.
        It sets whether the object will be specially aligned to the path.

    AlignMode: str
        It defaults to `'Original'`.
        Indicates the type of alignment that will be calculated when
        `Align` is `True`.

        `'Original'` mode is the historic `'Align'` for old (v0.18) documents.
        It is not really the Fernat alignment. It uses the normal parameter
        from `getNormal` (or the default) as a constant, it does not calculate
        curve normal.
        `X` is curve tangent, `Y` is normal parameter, `Z` is the cross product
        `X` x `Y`.

        `'Tangent'` mode is similar to `Original`, but includes a pre-rotation
        (in execute) to align the `Base` object's `X` to `TangentVector`,
        then `X` follows curve tangent, normal input parameter
        is the Z component.

        If `ForceVertical` is `True`, the normal parameter from `getNormal`
        is ignored, and `X` is curve tangent, `Z` is `VerticalVector`,
        and `Y` is the cross product `X` x `Z`.

        `'Frenet'` mode orients the copies to a coordinate system
        along the path.
        `X` is tangent to curve, `Y` is curve normal, `Z` is curve binormal.
        If normal cannot be computed, for example, in a straight line,
        the default is used.

    ForceVertical: bool
        It defaults to `False`.
        If it is `True`, and `AlignMode` is `'Original'` or `'Tangent'`,
        it will use the vector in `VerticalVector` as the `Z` axis.

    StartOffset: float
        It defaults to 0.0.
        It is the length from the start of the path to the first copy.

    EndOffset: float
        It defaults to 0.0.
        It is the length from the end of the path to the last copy.



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Point](Point_API.md) <small>(obj, x=0, y=0, z=0)</small>

The Draft Point object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> PointArray <small>(obj)</small>

The Draft Point Array object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> Polygon <small>(obj)</small>

The Polygon object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Rectangle <small>(obj)</small>

The Rectangle object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Shape2DView <small>(obj)</small>

The Shape2DView object



#### <img src="images/BIM_Column.svg" style="width:16px;"> ShapeString <small>(obj)</small>

The ShapeString object



#### <img src="images/BIM_Column.svg" style="width:16px;"> Text <small>(obj)</small>

The Draft Text object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> ViewProviderDraft <small>(vobj)</small>

The base class for Draft view providers.

    Parameters
     
    vobj : a base C++ view provider
        The view provider of the scripted object (`obj.ViewObject`),
        which commonly may be of types `PartGui::ViewProvider2DObjectPython`,
        `PartGui::ViewProviderPython`, or `Gui::ViewProviderPythonFeature`.

        A basic view provider is instantiated during the creation
        of the base C++ object, for example,
        `Part::Part2DObjectPython`, `Part::FeaturePython`,
        or `App::FeaturePython`.

            >>> obj = App.ActiveDocument.addObject('Part::Part2DObjectPython')
            >>> vobj = obj.ViewObject
            >>> ViewProviderDraft(vobj)

        This view provider class instance is stored in the `Proxy` attribute
        of the base view provider.
        ::
            vobj.Proxy = self

    Attributes
     
    Object : the base C++ object
        The scripted document object that is associated
        with this view provider, which commonly may be of types
        `Part::Part2DObjectPython`, `Part::FeaturePython`,
        or `App::FeaturePython`.

    texture : coin.SoTexture2
        A texture that could be added to this object.

    texcoords : coin.SoTextureCoordinatePlane
        The coordinates defining a plane to use for aligning the texture.

    These class attributes are accessible through the `Proxy` object:
    `vobj.Proxy.Object`, `vobj.Proxy.texture`, etc.



#### <img src="images/BIM_Column.svg" style="width:16px;"> ViewProviderDraftAlt <small>(vobj)</small>

A view provider that doesn't absorb its base object in the tree view.

    The `claimChildren` method is overridden to return an empty list.

    The `doubleClicked` method is defined.

    Only used by the `Shape2DView` object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> ViewProviderDraftLink <small>(vobj)</small>

A view provider for link type object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> ViewProviderDraftPart <small>(vobj)</small>

A view provider that displays a Part icon instead of a Draft icon.

    The `getIcon` method is overridden to provide `Part_3D_object.svg`.

    Only used by the `Block` object.



#### <img src="images/BIM_Column.svg" style="width:16px;"> [Wire](Wire_API.md) <small>(obj)</small>

The Wire object



#### <img src="images/BIM_Column.svg" style="width:16px;"> WorkingPlaneProxy <small>(obj)</small>

The Draft working plane proxy object



#### <img src="images/BIM_Column.svg" style="width:16px;"> arrowtypes

Built-in mutable sequence.

If no argument is given, the constructor creates a new empty list.
The argument must be an iterable if specified.



#### <img src="images/BIM_Column.svg" style="width:16px;"> gui

bool(x) -> bool

Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.



### Modules

#### <img src="images/Applications-python.svg" style="width:16px;"> App

The functions in the FreeCAD module allow working with documents.
The FreeCAD instance provides a list of references of documents which
can be addressed by a string. Hence the document name must be unique.

The document has the read-only attribute FileName which points to the
file the document should be stored to.









---
⏵ [documentation index](../README.md) > [API](Category_API.md) > [Poweruser Documentation](Category_Poweruser Documentation.md) > [Draft](Draft_Workbench.md) > Draft API
