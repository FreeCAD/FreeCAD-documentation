# Macro DeepCopy/it
{{Macro/it
|Name=Macro DeepCopy
|Translate=DeepCopy
|Icon=Macro_DeepCopy.png
|Description=Crea un composto formato da una copia tutte le forme di una parte
|Author=galou_breizh
|Version=1.0
|Date=2018-03-16
|FCVersion=V0.17 e successive
|Download=[https://wiki.freecad.org/images/0/0a/Macro_DeepCopy.png ToolBar Icon]
}}



## Descrizione

Seleziona una parte nell\'albero, esegui la macro e creerai un composto con una copia di tutte le sue forme. La gerarchia delle parti viene persa e tutte le funzionalità speciali dei bambini della parte originale. Per esempio sottoparti, corpi, schizzi, \... andranno persi e la loro forma sarà copiata.


{{Codeextralink|https://raw.githubusercontent.com/FreeCAD/FreeCAD-macros/master/Conversion/DeepCopy.FCMacro}}

## Script

ToolBar Icon ![](images/Macro_DeepCopy.png )

**Macro_DeepCopy.FCMacro**


{{MacroCode|code=
__Name__ = 'Deep Copy'
__Comment__ = 'Takes a part and makes a compound out of it'
__License__ = 'Apache-2.0'
__Web__ = 'https://wiki.freecad.org/Macro_DeepCopy'
__Wiki__ = 'https://wiki.freecad.org/Macro_DeepCopy'
__Icon__ = 'https://wiki.freecad.org/images/0/0a/Macro_DeepCopy.png'
__Help__ = 'Select a part and launch'
__Author__ = 'galou_breizh'
__Version__ = '1.0.0'
__Status__ = 'Stable'
__Requires__ = 'FreeCAD >= v0.17'
__Files__ = 'Macro_DeepCopy.png'

import FreeCAD as app
import FreeCADGui as gui


def deep_copy(doc):
    for sel_object in gui.Selection.getSelectionEx():
        deep_copy_part(doc, sel_object.Object)


def deep_copy_part(doc, part):
    if part.TypeId != 'App::Part':
        # Part is not a part, return.
        return

    copied_subobjects = []
    for o in get_all_subobjects(part):
        copied_subobjects += copy_subobject(doc, o)

    compound = doc.addObject('Part::Compound', 'Copy of ' + part.Label)
    compound.Links = copied_subobjects
    doc.recompute()


def get_all_subobjects(o):
    """Recursively get all subobjects

    Subobjects of objects having a Shape attribute are not included otherwise each
    single feature of the object would be copied. The result is that bodies,
    compounds, and the result of boolean operations will be converted into a
    simple copy of their shape.
    """
    # Depth-first search algorithm.
    discovered = []
    # We do not need an extra copy for stack because OutList is already a copy.
    stack = o.OutList
    while stack:
        v = stack.pop(0)
        if v not in discovered:
            discovered.append(v)
            if not hasattr(v, 'Shape'):
                stack += v.OutList
    return discovered


def copy_subobject(doc, o):
    """Copy the shape of an object

    Some GUI attributes are also copied
    """
    copied_object = []
    if not hasattr(o, 'Shape') or o.Shape.isNull():
        return copied_object
    vo_o = o.ViewObject
    try:
        copy = doc.addObject('Part::Feature', o.Name + '_Shape')
        copy.Shape = o.Shape
        copy.Label = 'Copy of ' + o.Label
        copy.Placement = o.getGlobalPlacement()

        vo_copy = copy.ViewObject
        vo_copy.ShapeColor = vo_o.ShapeColor
        vo_copy.LineColor = vo_o.LineColor
        vo_copy.PointColor = vo_o.PointColor
        vo_copy.DiffuseColor = vo_o.DiffuseColor
        vo_copy.Transparency = vo_o.Transparency
    except AttributeError:
        pass
    else:
        copied_object = [copy]
    return copied_object


if __name__ == '__main__':
    doc = app.activeDocument()
    if doc:
        deep_copy(doc)
    else:
        app.Console.PrintWarning('No active document')

}}

[code on GitHub](https://github.com/FreeCAD/FreeCAD-macros/blob/master/Conversion/DeepCopy.FCMacro)



---
⏵ [documentation index](../README.md) > Macro DeepCopy/it
