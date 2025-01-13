---
 GuiCommand:
   Name: PartDesign Fillet
   MenuLocation: Part Design , Apply a dress-up feature , Fillet
   Workbenches: PartDesign_Workbench/ko
   SeeAlso: PartDesign_Chamfer/ko
---

# PartDesign Fillet/ko



## 설명

<img alt="" src=images/PartDesign_Fillet.svg  style="width:24px;"> **부품설계 작업대에서 모깎기** 도구는 개체의 선택된 모서리를 둥글게 깎아냅니다. [트리 뷰에](Tree_view/ko.md) 해당 표현이 있는 문서에 **모깎기** 개체를 추가합니다.



## 용법



### 모깎기 추가 

1.  Optionally [activate](PartDesign_Body#Active_status.md) the Body to fillet.
2.  There are several ways to select edges to fillet:
    -   Select one or more edges of the Body individually.
    -   Select one or more faces of the Body to select all their edges.
    -   Select a feature (usually the last feature) of the Body to select all its edges.
3.  For a chain of tangentially connected edges only a single edge needs to be selected, the fillet will propagate along the chain.
4.  There are several ways to invoke the tool:
    -   Press the **<img src="images/PartDesign_Fillet.svg" width=16px> [Fillet](PartDesign_Fillet.md)** button.
    -   Select the **Part Design → Apply a dress-up feature → <img src="images/PartDesign_Fillet.svg" width=16px> Fillet** option from the menu.
5.  If there is no active Body, and there are two or more Bodies in the document, the **Active Body Required** dialog will open and prompt you to activate one. If there is a single Body it will be activated automatically.
6.  The **Fillet parameters** [task panel](Task_panel.md) opens. See [Options](#Options.md) for more information.
7.  Press the **OK** button to finish.



### 모깎기 편집 

1.  Do one of the following:
    -   Double-click the Fillet object in the [Tree view](Tree_view.md)
    -   Right-click the Fillet object in the [Tree view](Tree_view.md) and select **Edit Fillet** from the context menu.
2.  The **Fillet parameters** [task panel](Task_panel.md) opens.See [Options](#Options.md) for more information.
3.  Press the **OK** button to finish.



## 선택 사항 

-   To add edges do one of the following:
    -   Press the **Add** button to start selecting edges and/or faces in the [3D view](3D_view.md).
    -   To select all remaining edges do the following:
        1.  If required press the **Add** button.
        2.  Use the **Ctrl**+**Shift**+**A** keyboard shortcut, or right-click the list and select **Add all edges** from the context menu.
-   To remove edges do one of the following:
    -   Press the **Remove** button to start deselecting edges and/or faces in the [3D view](3D_view.md). Selected elements are highlighted in purple.
    -   Select one or more elements in the list and press the **Del** key, or right-click the list and select **Remove** from the context menu.
-   Set the **Radius** of the fillet.
-   Check the **Use all edges** checkbox to select all edges of the previous feature. This deactivates the selection list and the related buttons.



## 보충 설명 

-   부품설계 작업대에서의 모깎기를 [부품 작업대에서의 모깎기와](Part_Fillet/ko.md) 혼동하지 마세요. 둘의 차이를 알지 못하는 경우 [부품 작업대의 모깎기를](Part_Fillet/ko.md) 부품설계의 몸통에 사용하면 안 됩니다. [부품과 부품설계를](Part_and_PartDesign.md) 참조하세요.
-   모깎기는 인접한 면을 완전히 소모할 수 없습니다.



## 속성

[속성 편집기도](Property_editor/ko.md) 참조하세요.

A PartDesign Fillet object is derived from a [Part Feature](Part_Feature.md) object and inherits all its properties. It also has the following additional properties:

### Data


{{Properties_Title|Base}}

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



## 알려진 문제 

고체 몸통에서 작동하는 모깎기, 모따기 및 기타 도형특징은 FreeCAD가 사용하는 기본 [OpenCASCADE](OpenCASCADE.md) 기술(OCCT) 커널에 따라 달라집니다. OCCT 커널은 두 면이 만나는 동시에 동시에 날카로운 모서리를 처리하는 데 어려움을 겪는 경우가 있습니다. 이 경우 FreeCAD는 설명 없이 충돌할 수 있습니다.

터미널에서 실행하면 FreeCAD는 충돌 후 다음과 같은 로그를 출력할 수 있습니다.


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

이 출력은 OCCT 라이브러리의 기능을 참조합니다. 이러한 유형의 충돌이 발생하면 FreeCAD가 아닌 OCCT에서 문제를 보고하고 해결해야 할 수도 있습니다.



### 위상 명명(Topological naming) 

Edge numbers are not completely stable, therefore it is advisable that you finish the main design work of your solid body before applying features like fillets and chamfers, otherwise edges could change names and filleted edges would likely become invalid. When the **Use All Edges** property is `True` there is some protection from this. Because in such cases all the edges of the base object are used and there is no dependence on individual edge names.

[위상 명명 문제에](Topological_naming_problem/ko.md) 대해 더 자세히 알아보세요.





{{PartDesign Tools navi

}}



---
⏵ [documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign Fillet/ko
