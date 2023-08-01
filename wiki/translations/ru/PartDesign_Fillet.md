---
- GuiCommand:
   Name/ru: Скругление
   Name: PartDesign_Fillet
   MenuLocation: PartDesign - Apply a dress-up feature - Скругление
   Workbenches: [PartDesign](PartDesign_Workbench/ru.md)
   SeeAlso: [Фаска](PartDesign_Chamfer/ru.md), [Скругление](Part_Fillet/ru.md)
---

# PartDesign Fillet/ru


</div>

## Описание

The <img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> **PartDesign Fillet** tool creates fillets (rounds) on the selected edges of an object. It adds a **Fillet** object to the document with its corresponding representation in the [Tree view](Tree_view.md).

## Применение

### Добавление скругления 

1.  Optionally [activate](PartDesign_Body#Active_status.md) the Body to fillet.
2.  There are several ways to select edges to fillet:
    -   Select one or more edges of the Body individually.
    -   Select one or more faces of the Body to select all their edges.
    -   Select a feature (usually the last feature) of the Body to select all its edges. <small>(v0.20)</small> 
3.  For a chain of tangentially connected edges only a single edge needs to be selected, the fillet will propagate along the chain.
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_Fillet.svg" width=16px> [Fillet](PartDesign_Fillet.md)** button.
    -   Select the **Part Design → Apply a dress-up feature → <img src="images/PartDesign_Fillet.svg" width=16px> Fillet** option from the menu.
5.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
6.  The **Fillet parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.

### Редактирование скругления 

1.  Do one of the following:
    -   Double-click the Fillet object in the [Tree view](Tree_view.md)
    -   Right-click the Fillet object in the [Tree view](Tree_view.md) and select **Edit Fillet** from the context menu.
2.  The **Fillet parameters** [task panel](Task_panel.md) opens.See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.

## Параметры

-   To add edges do one of the following:
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following:
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu. <small>(v0.20)</small> 
-   To remove edges do one of the following:
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Set the **Radius** of the fillet.
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons. <small>(v0.20)</small> 

## Примечания

-   PartDesign Fillet should not be confused with [Part Fillet](Part_Fillet.md). Unless you know what you are doing, [Part Fillet](Part_Fillet.md) should not be used on a PartDesign Body. See [Part and PartDesign](Part_and_PartDesign.md).
-   Fillets cannot completely consume the adjacent faces.

## Свойства

See also: [Property editor](Property_editor.md).

A PartDesign Fillet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Данные


{{Properties_Title|Основные}}

-    **Base|LinkSub**: Link to the selected edges and faces of the parent feature. Can be a link to only the parent feature if **Use All Edges** is `True`.

-    **Support Transform|Bool**: If `True` the filleted shape of the additive/subtractive parent feature will be used when the fillet object is included in a [pattern](PartDesign_Workbench#Transformation_tools.md), else only the shape of the fillet itself will be used. The default is `False`.

-    **Add Sub Shape|PartShape|hidden**
    

-    **Base Feature|Link|hidden**: Link to the parent feature.

-    **_ Body|LinkHidden|hidden**: Link to the parent body.


{{Properties_Title|Fillet}}

-    **Radius|QuantityConstraint**: The fillet radius. The default is {{value|1 mm}}.

-    **Use All Edges|Bool**: If `True` all edges of the feature are filleted, and the edges specified by **Base** are ignored. The default is `False`.


{{Properties_Title|Part Design}}

-    **Refine|Bool**: If `True` redundant edges are removed from the result of the operation. The default value is determined by the **Automatically refine model after sketch-based operation** preference. See [PartDesign Preferences](PartDesign_Preferences#General.md).

## Известные проблемы 

Fillets, chamfers, and other features that operate on solid bodies depend on the underlying [OpenCASCADE](OpenCASCADE.md) Technology (OCCT) kernel that FreeCAD uses. The OCCT kernel occasionally has difficulty handling coincident sharp edges, where two faces meet. If this is the case FreeCAD may crash without an explanation.

If run from the terminal, FreeCAD may output a log like this after a crash:


{{code|lang=text|code=
#1  0x7fff63d660ba in BRep_Tool::Curve(TopoDS_Edge const&, TopLoc_Location&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x2a
#2  0x7fff63d69546 in BRep_Tool::Curve(TopoDS_Edge const&, double&, double&) from /usr/lib/x86_64-linux-gnu/libTKBRep.so.7+0x46
#3  0x7fff71f4fef5 in ChFi3d_Builder::PerformIntersectionAtEnd(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x3b05
#4  0x7fff71f58307 in ChFi3d_Builder::PerformOneCorner(int, bool) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x1097
#5  0x7fff71ef6218 in ChFi3d_Builder::PerformFilletOnVertex(int) from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x4e8
#6  0x7fff71ef71d1 in ChFi3d_Builder::Compute() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0xe31
#7  0x7fff720ad7c3 in BRepFilletAPI_MakeChamfer::Build() from /usr/lib/x86_64-linux-gnu/libTKFillet.so.7+0x33
#8  0x7fff723be48e in PartDesign::Chamfer::execute() from /usr/lib/freecad-daily/lib/_PartDesign.so+0x60e
...
}}

This output references functions from OCCT libraries. If this type of crash occurs, the problem may need to be reported and solved in OCCT rather than in FreeCAD.

See the forum threads for more information:

-   [Bug Chamfer bigger than 2mm crashes freecad](https://forum.freecadweb.org/viewtopic.php?p=263818#p263818)
-   [Segfault when using part design fillet](https://forum.freecadweb.org/viewtopic.php?p=264827#p264827)

### Topological naming 

Edge numbers are not completely stable, therefore it is advisable that you finish the main design work of your solid body before applying features like fillets and chamfers, otherwise edges could change names and filleted edges would likely become invalid. When the **Use All Edges** property (<small>(v0.20)</small> ) is `True` there is some protection from this. Because in such cases all the edges of the base object are used and there is no dependence on individual edge names.

Read more in [topological naming problem](Topological_naming_problem.md).





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/ru
