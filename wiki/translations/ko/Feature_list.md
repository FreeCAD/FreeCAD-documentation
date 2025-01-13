# Feature list/ko
이것은 FreeCAD가 구현하는 광범위하지만 완전하지 않은 특징 목록입니다.






## 배포 기록 


<div class="mw-translate-fuzzy">

-   [Release 0.21](Release_notes_0.21.md) - 2023년 8월
-   [Release 0.20](Release_notes_0.20.md) - 2022년 6월
-   [Release 0.19](Release_notes_0.19.md) - 2021년 3월
-   [Release 0.18](Release_notes_0.18.md) - 2019년 3월
-   [배포 0.17](Release_notes_0.17/ko.md) - 2018년 4월
-   [Release 0.16](Release_notes_0.16.md) - 2016년 4월
-   [Release 0.15](Release_notes_0.15.md) - 2015년 3월
-   [Release 0.14](Release_notes_0.14.md) - 2014년 3월
-   [Release 0.13](Release_notes_0.13.md) - 2013년 1월
-   [Release 0.12](Release_notes_0.12.md) - 2011년 12월
-   [Release 0.11](Release_notes_0.11.md) - 2011년 3월


</div>



## 주요 특징 


<div class="mw-translate-fuzzy">

-   ![](images/Feature1.jpg ) A complete [Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE)-based **geometry kernel** allowing complex 3D operations on complex shape types, with native support for concepts like [Boundary Representation](https://en.wikipedia.org/wiki/Boundary_representation) (BREP), [Non-uniform rational basis spline](https://en.wikipedia.org/wiki/Non-uniform_rational_B-spline) (NURBS) curves and surfaces, a wide range of geometric entities, boolean operations and [fillets](https://en.wikipedia.org/wiki/Fillet_(mechanics)), and built-in support of [STEP](https://en.wikipedia.org/wiki/ISO_10303) and [IGES](https://en.wikipedia.org/wiki/IGES) formats 

-   ![](images/Feature3.jpg ) A full **parametric model**. All FreeCAD objects are natively parametric, meaning their shape can be based on [properties](Property.md) or even depend on other objects. All changes are recalculated on demand, and recorded by an undo/redo stack. New object types can be added easily, and can even be [fully programmed in Python](Scripted_objects.md).

-   ![](images/Feature4.jpg ) A **modular architecture** that allows plugin extensions (modules) to add functionality to the core application. An extension can be as complex as a whole new application programmed in C++ or as simple as a [Python script](Power_users_hub.md) or self-recorded [macro](Macros.md). You have complete access to almost any part of FreeCAD from the built-in **Python** interpreter, macros or external scripts, be it [geometry creation and transformation](Topological_data_scripting.md), the 2D or 3D representation of that geometry ([scenegraph](Scenegraph.md)) or even the [FreeCAD interface](PySide.md).

-   ![](images/Feature5.jpg ) Import/export to **standard formats** such as [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) or [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) in addition to FreeCAD\'s native **[FCStd](File_Format_FCStd.md)** file format. The level of compatibility between FreeCAD and a given file format can vary, since it depends on the module that implements it.

-   ![](images/Feature7.jpg ) [스케치 작업대에서는](Sketcher_Workbench/ko.md) 통합된 제약 조건 해결 프로그램을 통해 형상 제약이 있는 2D 형상을 스케치할 수 있습니다. 스케치된 2D 형상은 FreeCAD 전체에서 다른 객체를 제작하기 위한 기반으로 사용될 수 있습니다.

-   ![](images/Feature8.jpg ) [기술도면 작업대에서는](TechDraw_Workbench/ko.md) 기존 3D 모델로부터 상세 보기, 단면 보기, 치수 측정 등의 옵션이 포함된 2D 기술 도면을 작성할 수 있습니다. 그런 다음 즉시 내보낼 수 있는 SVG 또는 PDF 파일을 생성합니다.

-   ![](images/Feature-arch.jpg ) An [Architecture module](Arch_Workbench.md) that allows [Building Information Modeling](http://en.wikipedia.org/wiki/Building_Information_Modeling) (BIM)-like workflow, with [Industry Foundation Classes](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) (IFC) compatibility.

-   ![](images/Feature-CAM.jpg ) A [CAM module](CAM_Workbench.md) dedicated to mechanical machining for [Computer Aided Manufacturing](https://en.wikipedia.org/wiki/Computer-aided_manufacturing) (CAM). Using the Path module you may output, display and adjust the [G code](http://en.wikipedia.org/wiki/G-code) used to control the target machine.

-   ![](images/Feature_spreadsheet.png ) An [Integrated Spreadsheet](Spreadsheet_Workbench.md) and an [expression parser](Expressions.md) which may be used to drive formula-based models and organize model data in a central location.


</div>



## 일반적 특징 

-   **멀티 플랫폼**. FreeCAD는 윈도, 리눅스, 맥OS 그리고 다른 플랫폼에서 똑같은 방식으로 돌아갑니다.

-   **완전한 GUI 애플리케이션**. FreeCAD는 [Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor) 기반의 3D 뷰어와 함께 [Qt](https://www.qt.io/) 프레임워크 기반의 완전한 그래픽 사용자 인터페이스를 갖추고 있습니다.3D 장면의 빠른 렌더링과 매우 접근하기 쉬운 장면 그래프 표현이 가능합니다.

-   **명령줄 응용프로그램으로 실행됩니다**. 명령줄 모드에서 FreeCAD는 인터페이스 없이 모든 형상 도구와 함께 실행됩니다. 이 모드에서는 메모리 사용량이 상대적으로 적으며, 예를 들어 다른 애플리케이션용 콘텐츠를 생성하는 서버로 사용할 수 있습니다.

-   **[Python 모듈](Embedding_FreeCAD.md)**로 가져올 수 있습니다. FreeCAD는 Python 스크립트를 실행할 수 있는 모든 응용 프로그램으로 가져올 수 있습니다. 명령줄 모드에서와 마찬가지로 FreeCAD의 인터페이스 부분은 사용할 수 없지만 모든 형상 도구에 액세스할 수 있습니다.

-   **작업대 개념**. FreeCAD 인터페이스에서 도구는 [작업대별로](Workbenches/ko.md) 그룹화됩니다.이를 통해 특정 작업을 수행하는 데 사용되는 도구만 표시하고 작업 공간을 깔끔하게 유지하고 반응성을 높이며 응용 프로그램을 빠르게 실행할 수 있습니다.

-   **plugin/module framework for late loading of features/data-types**. FreeCAD is divided into a core application with modules and workbenches that are loaded only when needed. Almost all tools and geometry types are stored in workbenches. Workbenches behave like plugins; in addition to delayed loading, individual workbenches can be added to or removed from an existing installation of FreeCAD.

-   **parametric associative document objects**. All objects in a FreeCAD document can be defined by parameters. Those parameters can be modified and recomputed at any time. Since object relationships are maintained, the modification of one object will automatically propagate to any dependent objects.

-   **parametric primitive creation**. Primitive objects such as box, sphere, cylinder, etc. can be created by specifying their geometry constraints.

-   **graphical modification operations**. FreeCAD can perform translation, rotation, scaling, mirroring, offset (either trivial or as described in [Jung/Shin/Choi](https://www.researchgate.net/publication/240754626_Self-intersection_Removal_in_Triangular_Mesh_Offsetting)) or shape conversion, in any plane of the 3D space.

-   **[Constructive solid geometry](Constructive_solid_geometry.md) (boolean operations)**. FreeCAD can do constructive solid geometry operations (union, difference, intersect).

-   **graphical creation of planar geometry**. Lines, wires, rectangles, B-splines, and circular or elliptic arcs can be created graphically in any plane of the 3D space.

-   **modeling with straight or revolved** **extrusions**, **sections** and **fillets**.

-   **꼭지점**, **모서리**, **선** 그리고**평면**과 같은 **위상학적 구성요소**.

-   **테스트 및 수리**. FreeCAD에는 메쉬 테스트(고체 테스트, 비-2다양체 테스트, 자체 교차 테스트)를 위한 도구와 메쉬 수리(구멍 채우기, 균일한 방향)를 위한 도구가 있습니다.

-   **주석**. FreeCAD는 텍스트나 치수에 대한 주석을 삽입할 수 있습니다.

-   **실행 취소/다시 실행 프레임워크**. FreeCAD의 모든 것은 실행 취소/다시 실행이 가능하며 사용자는 실행 취소 스택에 액세스할 수 있습니다. 한 번에 여러 단계를 실행 취소할 수 있습니다.

-   **transaction oriented**. The undo/redo stack stores document transactions, not single actions, allowing each tool to define exactly what must be undone or redone.

-   **built-in [scripting](Scripting.md) framework**. FreeCAD features a built-in [Python](http://www.python.org/) interpreter, with an API that covers almost any part of the application, the interface, the geometry and the representation of this geometry in the 3D viewer. The interpreter can run complex scripts as well as single commands; entire workbenches can be programmed completely in Python.


<div class="mw-translate-fuzzy">

-   **내장 Python 콘솔**. Python 인터프리터에는 구문 강조, 자동 완성 및 클래스 브라우저가 포함된 콘솔이 포함되어 있습니다. Python 명령은 FreeCAD에서 직접 실행할 수 있으며 즉시 결과를 반환하므로 스크립트 작성자는 즉시 기능을 테스트하고 FreeCAD 모듈의 내용을 탐색하며 FreeCAD 내부에 대해 쉽게 배울 수 있습니다.


</div>

-   **사용자 상호작용을 반영합니다**. 사용자가 FreeCAD 인터페이스에서 수행하는 모든 작업은 콘솔에 인쇄되고 매크로에 기록될 수 있는 Python 코드를 실행합니다.

-   **완전한 [macro](Macros.md) 기록 및 편집** 기능을 제공합니다. 사용자가 인터페이스를 조작할 때 실행되는 Python 명령을 기록하고, 필요한 경우 편집하고, 나중에 재현하기 위해 저장할 수 있습니다.

-   **복합(ZIP 기반) 문서 저장 형식**. FreeCAD 문서는 **.[FCStd](File_Format_FCStd.md)** 확장자로 저장됩니다.문서에는 형상, 스크립트 또는 축소판 아이콘과 같은 다양한 유형의 정보가 포함될 수 있습니다. **.FCStd** 파일 자체는 zip 컨테이너입니다. 저장된 FreeCAD 파일은 이미 압축되었습니다.

-   **완전히 사용자 정의 가능/스크립트 가능 그래픽 사용자 인터페이스(GUI)**. FreeCAD의 [Qt](https://www.qt.io) 기반 인터페이스는 Python 인터프리터를 통해 완전히 접근할 수 있습니다. FreeCAD 자체가 작업대에 제공하는 간단한 기능 외에도 전체 Qt 프레임워크에 접근할 수 있습니다. 사용자는 위젯과 도구 모음 생성, 추가, 도킹, 수정 또는 제거와 같은 모든 작업을 GUI에서 수행할 수 있습니다.

-   **썸네일러**. (현재 Linux 시스템에만 해당) FreeCAD 문서 아이콘은 Gnome의 Nautilus와 같은 대부분의 파일 관리자 응용 프로그램에서 파일 내용을 표시합니다.

-   **모듈식 MSI 설치 프로그램**. FreeCAD 설치 프로그램을 사용하면 Windows 시스템에 유연하게 설치할 수 있습니다. Ubuntu 시스템용 패키지도 유지 관리됩니다.



## 외부 작업대 

고급 사용자는 다양한 사용자 정의 [외부 작업대를](External_workbenches/ko.md) 만들었습니다.



---
⏵ [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/ko
