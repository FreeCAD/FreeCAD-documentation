# Macro clone explicit
{{Macro
|Name=Macro Clone explicit
|Icon=Macro_clone_explicit.png
|Description=Creates a copy of each selected object and sets its properties to an expression linking to the original object, making it an explicit and editable clone.
|Author=Raph82
|Version=0.1
|Date=2018-12-15
|FCVersion=18 and after
|Download=[https://www.freecadweb.org/wiki/images/a/ab/Macro_clone_explicit.png ToolBar Icon]
|SeeAlso=[Expressions](Expressions.md)
}}

## Description

This macro creates a copy of each selected object and sets its properties to an [expression](Expressions.md) linked to the original object, making it an explicit and editable clone.

This clone is a copy of the original object, as in the **Edit → Duplicate selection** command, but its properties are defined by expressions.

### How does this \'explicit and editable clone\' differ from a Clone object? 

\'Explicit\' because all of the original object properties are visible. In a Clone object of a Cube, can you see its Height for example? When you use an expression for a Clone object, can you easily access its parent properties?

\'Editable\' because, contrary to a Clone object, you can edit the expression of any property. So it is possible to have the object only clone certain properties of its parent, while you modify the others.

## Usage

1.  Select at least one object.

2.  
    **Macro → Macros...**
    

3.  Select the **clone_explicit.FCMacro** from the list.

4.  Press the **Execute** button.

## Script

ToolBar Icon ![](images/Macro_clone_explicit.png )

 **Macro_clone_explicit.FCMacro**


{{MacroCode|code=
__Title__ = "clone_explicit"
__Author__ = "Raph82"
__URL__     = "http://www.freecadweb.org/index-fr.html"
__Version__ = "0.1"
__Date__    = "2018-12-15" #YYYY-MM-DD
__Comment__ = "This macro creates a copy of the selected objects and sets their properties to an expression linking to the original object, making it an explicit and editable clone"
__Web__ = "http://www.freecadweb.org/"
__Wiki__ = "http://www.freecadweb.org/wiki/index.php?title=Macro_clone_explicit"
__Icon__  = "/usr/lib/freecad/Mod/plugins/icons/Macro_clone_explicit.png"
__IconW__  = "C:/Users/User Name/AppData/Roaming/FreeCAD/Macro_clone_explicit.png"
__Help__ = "Select at least one object and run the macro to make explicit and editable clone(s)"
__Status__ = "dev"
__Requires__ = "All FreeCAD"
__Communication__ = "http://www.freecadweb.org/wiki/index.php?title=User:raph82"

#IMPORTS:
import sys

##################################################
def set_expression(obj, property_to_set, expression):
    """"""
    try:
        print type(obj)
        obj.setExpression(property_to_set, expression)
#    except 'Base.FreeCADError':
    except Exception as detail:
        print detail
        print type(detail)
        if detail['swhat'] == 'Property not found':
            App.Console.PrintMessage('Object "{obj}" has no property "{prop}"\r\n'.format(obj=obj.Name, prop=property_to_set))
        else:
            raise

##################################################
def clone_explicit(mode):
    """Copy the selected objects and sets their properties to an expression, making it an explicit and editable clone.

     This clone is called "explicit and editable" because the link with its parent is visible and can be changed in the object properties.

     The link to the original object can be either "direct" or "transient", depending on the mode argument:
     - a direct clone has expressions pointing to its parent: clone.Length = parent.Length
     - a transient clone has expressions pointing to its ancestor. Say parent.Length = Box001.Length. With a transient clone, clone.Length = Box001.Length, whereas with a direct clone, clone.Length = parent.Length.
       This indirect link to Box001 (via the parent object) could be severed, accidentally or not, depending on what relationship you're looking for.

     If you're lost, try with a direct clone first."""

    App.Console.PrintMessage("Start of clone_explicit macro"+"\r\n")

    #Current selection check:
    sel = FreeCADGui.Selection.getSelection()

    App.Console.PrintMessage(str(len(sel))+" object(s) selected\r\n")
    if len(sel) != 0:
        for i in range(len(sel)):
            obj=sel[i]

            #copying current object:
            App.Console.PrintMessage('Copying "'+obj.Label+'" ('+obj.Name+')\r\n')
            obj_copy=App.ActiveDocument.copyObject(obj, False) #https://www.freecadweb.org/api/d8/d3e/classApp_1_1Document.html#a08f1d7d90f4a7276a02918fb6445a04a
            App.Console.PrintMessage('"'+obj_copy.Label+'" ('+obj_copy.Name+') created\r\n')

            if mode == 'direct':
                #defining expressions pointing to the original object:
                set_expression(obj_copy, 'Placement.Base.x',          obj.Name+u'.Placement.Base.x')
                set_expression(obj_copy, 'Placement.Base.y',          obj.Name+u'.Placement.Base.y')
                set_expression(obj_copy, 'Placement.Base.z',          obj.Name+u'.Placement.Base.z')
                set_expression(obj_copy, 'Placement.Rotation.Angle',  obj.Name+u'.Placement.Rotation.Angle')
                set_expression(obj_copy, 'Placement.Rotation.Axis.x', obj.Name+u'.Placement.Rotation.Axis.x')
                set_expression(obj_copy, 'Placement.Rotation.Axis.y', obj.Name+u'.Placement.Rotation.Axis.y')
                set_expression(obj_copy, 'Placement.Rotation.Axis.z', obj.Name+u'.Placement.Rotation.Axis.z')
                set_expression(obj_copy, 'Length',                    obj.Name+u'.Length')
                set_expression(obj_copy, 'Width',                     obj.Name+u'.Width')
                set_expression(obj_copy, 'Height',                    obj.Name+u'.Height')

            elif mode == 'transient':
                #defining expressions pointing to the utmost original object:
                define_transient_expression(obj, obj_copy, 'Placement.Base.x')
                define_transient_expression(obj, obj_copy, 'Placement.Base.y')
                define_transient_expression(obj, obj_copy, 'Placement.Base.z')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Angle')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Axis.x')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Axis.y')
                define_transient_expression(obj, obj_copy, 'Placement.Rotation.Axis.z')
                define_transient_expression(obj, obj_copy, 'Length')
                define_transient_expression(obj, obj_copy, 'Width')
                define_transient_expression(obj, obj_copy, 'Height')
            else:
                App.Console.PrintError('Programming error: mode value not recognized.\r\n')

            App.Console.PrintMessage('('+obj_copy.Label+'" ('+obj_copy.Name+') expressions set\r\n')

        FreeCAD.ActiveDocument.recompute()
        App.Console.PrintMessage('End of clone_explicit macro\r\n')

    else:
        App.Console.PrintError('Select at least one object first\r\n')

    sel = ""
    obj = ""
    obj_copy = ""

##################################################
def find_expression(source_object, property_to_define):
    """"""

    for var_tuple in source_object.ExpressionEngine: #https://forum.freecadweb.org/viewtopic.php?f=22&t=21950
        # .ExpressionEngine returns tuple like [('Placement.Base.z', 'Length')], see https://docs.python.org/2.7/tutorial/datastructures.html#tuples-and-sequences
        App.Console.PrintMessage('var_tuple[0]='+var_tuple[0]+'\r\n')
        if var_tuple[0] == property_to_define:
           return var_tuple[1]

##################################################
def define_transient_expression(source_object, target_object, property_to_define):
    """"""
    expressions = source_object.ExpressionEngine #https://forum.freecadweb.org/viewtopic.php?f=22&t=21950
    # returns tuple like [('Placement.Base.z', 'Length')], see https://docs.python.org/2.7/tutorial/datastructures.html#tuples-and-sequences

    expression = find_expression(source_object, property_to_define)
    if expression != None:
#        App.Console.PrintMessage("target_object.Name="+target_object.Name+"\r\n")
#        App.Console.PrintMessage("property_to_define="+property_to_define+"\r\n")
#        App.Console.PrintMessage("expressions[property_to_define]="+expressions[property_to_define]+"\r\n")

        set_expression(target_object, property_to_define, expression)
    else:
        set_expression(target_object, property_to_define, source_object.Name+'.'+property_to_define)

    expressions = ""

##################################################
clone_explicit('direct')
#clone_explicit('transient')
}}

## Options

A mode option was planned. It\'s not yet implemented. It now seems much more complex than initially thought, maybe too complex for me to implement.

The idea is that one might prefer one of two behaviors:

-   the clone keeps mimicking its parent even if the parent properties *expressions* change. It\'s the direct mode,
-   the clone keeps the properties *expressions* the parent had when the clone was created. It\'s the transient mode.

Note the emphasis on the word \"expressions\". An expression is one abstraction layer over a value.

Here\'s an example. Imagine the parent object (the one you select before running the macro), has its Height property set to the expression Object**3**.Height * 2.

-   When run in direct mode:
    -   Clone.Height = Parent.Height,
    -   changes in Object**3**.Height value would affect both the parent and the clone objects,
    -   changes in Parent.Height *expression* would **also** affect both objects:
        -   Parent.Height = Object**4**.Height * 2 and
        -   Clone.Height = Parent.Height still.
-   When run in transient mode:
    -   Clone.Height = Object**3**.Height * 2,
    -   changes in Object**3**.Height value would affect both the parent and the clone objects,
    -   changes in Parent.Height *expression* would **only** affect the parent object:
        -   Parent.Height = Object**4**.Height * 2 and
        -   Clone.Height = Object**3**.Height * 2 still.

 For now, the macro is run with the mode parameter set to direct and no choice is proposed to the user.

## Limitations

-   Works well only with Cubes at the moment. To expand to many types I need to:
    -   find how to identify an object type to deal with its different properties accordingly;
    -   find how to catch the Property not found error.

## Version history 

-   0.1: first public release



---
![](images/Button_right.svg) [documentation index](../README.md) > Macro clone explicit
