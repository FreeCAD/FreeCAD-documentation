# Shape/ko
## 소개

FreeCAD에서 **형상(Shape)**이라는 단어는 일반적으로 [Part TopoShape](Part_TopoShape.md)(`Part::TopoShape` 클래스)를 나타내는 데 사용됩니다. 이것은 요소에 3D 기하학적 및 파라메트릭 표현(큐브, 피라미드, 구, 원통, 융합 등)을 제공하는 개체 유형입니다.

기본적으로 [3D view에](3D_view.md) 표시되는 모든 개체에는 [TopoShape가](Part_TopoShape.md) 있습니다. 단, \"[Meshes](Mesh.md)\"(`Mesh::MeshObject` 클래스)는 예외입니다. .

이 객체 유형에 대한 자세한 내용은 [Part TopoShape를](Part_TopoShape.md) 참조하세요.

![](images/Shape_and_mesh.svg )



*왼쪽: 속성에 의해 정의된 파라메트릭 형상. 오른쪽: 정점과 삼각형 표면으로 정의되는 [mesh](Mesh.md).*



## 용법

Shapes are normally created by internal functions of the [Part Workbench](Part_Workbench.md), and are ultimately defined by the [OpenCASCADE Technology](OpenCASCADE.md) kernel (OCCT).

Once a Shape is created, it can be used and modified by all [workbenches](Workbenches.md) by creating [scripted objects](scripted_objects.md) around that Shape.

Essentially, every object derived from a [Part Feature](Part_Feature.md) (`Part::Feature` class) is expected to hold and manipulate a Shape.

Any OpenCascade Shape has a tesselation mainly to view the Shape on screen. More information about this can be found in this German [forum post](https://forum.freecad.org/viewtopic.php?t=77521&start=10#p674947) and in the [OpenCascad Mesh documentation](https://dev.opencascade.org/doc/overview/html/occt_user_guides__mesh.html).

## Notes

In informal usage, a \"Shape\" may be any geometrical figure that is visible in the [3D view](3D_view.md), and thus its concept may be confused with that of \"[Body](Body.md)\" or \"[Part](Part.md)\".

However, when more precision is required, the distinction must be made.

-   A \"[Body](Body.md)\" is an object derived from a [Part Feature](Part_Feature.md) (`Part::Feature` class), created with the [PartDesign Workbench](PartDesign_Workbench.md).
-   A \"Shape\" is an internal object, embedded within the \"[Body](Body.md)\".
-   A \"[Part](Part.md)\" is used to group several \"[Bodies](Body.md)\" to form an [assembly](assembly.md). A \"Part\" has a collection of \"Shapes\", but doesn\'t have a \"Shape\" of its own.


 {{Document objects navi}}



---
⏵ [documentation index](../README.md) > [Glossary](Category_Glossary.md) > [Part](Category_Part.md) > Shape/ko
