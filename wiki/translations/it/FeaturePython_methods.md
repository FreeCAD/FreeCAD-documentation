# FeaturePython methods/it



{{TOCright}}

## Introduzione


<div class="mw-translate-fuzzy">

Questa pagina funge da riferimento per i metodi sovrascrivibili disponibili negli [Oggetti FeaturePython](FeaturePython_Objects/it.md) o [Oggetti creati da script](Scripted_objects/it.md).


</div>

## Riferimento primario 

I metodi seguenti rappresentano circa il 99% dei casi d\'uso che gli utenti esperti possono avere per le classi proxy Python.

+--------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             | Called during document recomputes                                        | Do not call `recompute()` from this method (or any method called from `execute()`) as this causes a nested recompute.                                                                                                                                                                                                                                |
| `execute(self, obj)`              |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                         |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             | Called before a property value is changed                                |                                                                                                                                                                                                                                                                                                                                                                                     |
| `onBeforeChange(self, obj, prop)` |                                                                          | `prop`                                                                                                                                                                                                                                                                                                                                                                                    |
|                                         |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                            |                                                                          | is the name of the property to be changed, not the property object itself. Property changes cannot be cancelled. Previous / next property values are not simultaneously available for comparison.                                                                                                                                                                                                  |
+--------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             | Called after a property is changed                                       |                                                                                                                                                                                                                                                                                                                                                                                     |
| `onChanged(self, obj, prop)`      |                                                                          | `prop`                                                                                                                                                                                                                                                                                                                                                                                    |
|                                         |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                            |                                                                          | is the name of the property to be changed, not the property object itself.                                                                                                                                                                                                                                                                                                                         |
+--------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                             | Called after a document is restored or a FeaturePython object is copied. | Occasionally, references to the FeaturePython object from the class, or the class from the FeaturePython object may be broken, as the class `__init__()` method is not called when the object is reconstructed. Adding `self.Object <nowiki>=</nowiki> obj` or `obj.Proxy <nowiki>=</nowiki> self` often solves these issues. |
| {{Incode|onDocumentRestored(self, obj)}}   |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                         |                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                    |
+--------------------------------------------+--------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

It is not uncommon to encounter a situation where the Python callbacks are not being triggered as they should. Beginners in this area can rest assured that the FeaturePython callback system is not fragile or broken. Invariably when callbacks fail to run it is because a reference is lost or undefined in the underlying code. If, however, callbacks appear to be breaking with no explanation, providing object/proxy references in the `onDocumentRestored()` callback (as noted in the first table above) may alleviate these problems. Until you are comfortable with the callback system, it may be useful to add print statements in each callback to print messages to the console during development.

## Additional methods 

The below methods are for **advanced** usage of Python proxy classes and you won\'t have a need for them most of the time.

-   mustExecute
-   getViewProviderName
-   getSubObject
-   getSubObjects
-   getLinkedObject
-   hasChildElement
-   isElementVisible
-   canLinkProperties
-   allowDuplicateLabel
-   redirectSubName
-   canLoadPartial
-   onBeforeChangeLabel

## Determining available Python methods 

Within the [FeaturePython Template Class](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L161-L351) exists various () calls.

Each of these correspond to an available bound Python method.

For example, imp->execute() [on line 193](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L193) means the execute method is available.

Note, getPyObject() and init() are special-cases and don\'t follow the above heuristic.

## Vedere anche 

-   [FreeCAD GitHub: FeaturePython.h - public API](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L44-L86)
-   [FreeCAD GitHub: FeaturePythonT template class](https://github.com/FreeCAD/FreeCAD/blob/76e74294894bbce46d006e149315c6274d206278/src/App/FeaturePython.h#L167)
-   [FreeCAD Forum Discussion: Scripted Objects Complete Method Reference](https://forum.freecadweb.org/viewtopic.php?f=22&t=49194)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
