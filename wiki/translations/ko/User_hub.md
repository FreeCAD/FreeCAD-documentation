# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/ko



여기는 FreeCAD 를 처음 사용하는 데 필요한 도움말의 요약 또는 종합 한 것 입니다.

FreeCAD 는 계속 개발하고 있는 상태라서, 오래 된 또는 누락 된 것이 있을 수 있습니다. 필요한 정보를 찾을 수 없다면, 망설일 필요없이 [FreeCAD forum](https://forum.freecadweb.org) 에서 요청하시기 바랍니다.

FreeCAD 에 기여하고 싶다면, [기부](donate.md), 와 [Help FreeCAD](Help_FreeCAD.md) 페이지에 기여하는 여러가지 방법들을 읽어 보시기 바랍니다. 이 위키를 편집하고 싶다면, 여러분의 위키 계정, 문서 편집이 가능한 등급으로 설정 등 두 가지를 [포럼](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830)에 들어가서 관리자에게 PM(개인간 메시지)으로 요청하고, [위키 페이지](WikiPages.md) 에서 지켜야 할 규칙을 읽어 보세요.

몇 년 전에 FreeCAD가 어떻게 시작되었는지 알고 싶으면 [ 연혁](History.md) 페이지를 방문하세요.



## FreeCAD 사용에 관한 내용 



### 기본 사항 

-   [프리캐드의 개요](About_FreeCAD/ko.md): 프리캐드에 대해 전반적으로 살펴보기
-   [설치하기](Installing.md): 프리캐드를 [Windows](Install_on_Windows.md), [Linux](Install_on_Linux.md) 나 [Mac](Install_on_Mac.md) 에 설치하는 방법
-   [도움말 파일 설치](Installing_Helpfile.md): 위키를 근거로 만들어진 오프라인 도움말이 있는데, 그것을 설치하는 방법입니다.
-   [추가 기능 설치](Installing_additional_components/ko.md):프리캐드와 함께 사용 되도록 제작된 타사의 도구를 추가하는 방법.
-   [Getting started](Getting_started.md): 사용할 수 있는 도구들에 대한 요약 정보
-   [FAQ](Frequently_asked_questions.md): 자주 문의되는 내용들
-   [자습용 교재](Tutorials/ko.md) 에서 프리캐드의 여러가지 내용들을 다루고 있습니다.



#### 다른 프로그램의 파일을 들여오는 방법 ? 

-   [해결방법들](Workarounds/ko.md)
-   [Fusion360 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_Fusion360/ko.md)
-   [OnShape 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_OnShape/ko.md)
-   [SolidWorks 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_SolidWorks/ko.md)
-   [Revit 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_Revit/ko.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [프리캐드와 BIM 프로그램들의 호환성](BIM_application_compatibility_table/ko.md)



### 기본적인 사용방법들 

-   [프리캐드 화면](Interface/ko.md): FreeCAD 의 인터페이스는 그래픽 형식으로 된 [3D 보기](3D_view/ko.md), [트리 보기](Tree_view/ko.md), [특성 편집기](Property_editor/ko.md), [작업 공간](Task_panel/ko.md), [파이썬 콘솔](Python_console/ko.md) 등으로 구성되어 있습니다.
-   [Mouse navigation](Mouse_navigation/ko.md): 마우스나 트랙볼을 이용하여 \'3D 보기\'에서 탐색하는 여러가지 방법들.
-   [Selection methods](Selection_methods/ko.md): 이 어플 속에서 대상물을 선택하는 여러가지 방법들이 있습니다.
-   [Objects naming](Object_name/ko.md): FreeCAD 속 한 대상물은 몇 가지의 명칭을 갖고 있는데, 시스템 내부에서 부여하는 읽기만 가능한 고유한 명칭 `Name` 과 사용자가 편집 할 수 있는 명칭 `Label` 등이 있습니다.
-   [Preferences Editor](Preferences_Editor/ko.md): 기본 시스템이나 각각의 작업환경 등에 대해서 편집할 수 있는 속성을 수정할 때 사용 합니다.
-   [File formats](Import_Export/ko.md): 프리캐드로 읽거나 쓸 수 있는 여러가지 파일 형식이 있습니다.



### 분야별 작업환경 

[작업환경들](Workbenches.md) 은 전문분야 작업용 도구를 모아 놓은 것 입니다. 프리캐드를 설치 할 때 배포되며 기본 수준의 작업환경 입니다:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [Standard tools](Std_Base.md). 는 모든 작업환경에서 공통적으로 제공되는 명령어들과 도구들 입니다.

-   <img alt="" src=images/Workbench_Arch.svg  style="width:32px;"> [건축 작업환경](Arch_Workbench/ko.md) 는 건축 요소들에 관한 작업환경 입니다.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [설계도 작업환경](Draft_Workbench/ko.md) 에는 2D용 도구들이 있고 기본적인 수준의 3D 작업은 할 수 있습니다.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> The [FEM 작업환경](FEM_Workbench/ko.md) 은 유한요소 해석 수행을 지원 합니다.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [검사 작업환경](Inspection_Workbench/ko.md) 는 형상물 확인시 사용 할 도구를 제공하기 위해 만들어 졌습니다. 아직은 개발초기 단계에 있습니다.

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> The [격자망 작업환경](Mesh_Workbench/ko.md) 은 삼각형 격자망으로 된 형상물 작업환경 입니다.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> The [OpenSCAD 작업환경](OpenSCAD_Workbench.md) 은 OpenSCAD 내부와 상호작용 이나 [constructive solid geometry](Constructive_solid_geometry/ko.md) (CSG) 기본형 모델의 수정 기록의 복구 등을 위한 것입니다.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [기본형 개체 도구](Part_Module/ko.md) 는 프로그램에서 기본형 개체 불러오기와 중첩영역 가감처리(=boolean, 집합연산)등의 작업 도구입니다.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> The [상세 부분 설계 작업환경](PartDesign_Workbench/ko.md) 건물 한 부분에 관한 스케치를 형상물로 만들기 위한 환경 입니다.

-   <img alt="" src=images/Workbench_Path.svg  style="width:32px;"> The [CNC 작업환경](Path_Workbench/ko.md) 은 CNC 장비로 작동 시킬 작업을 G-code 로 작성할 때 사용합니다.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> The [Points Workbench](Points_Workbench.md) for working with point clouds.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> The [Reverse Engineering Workbench](Reverse_Engineering_Workbench.md) is intended to provide specific tools to convert shapes/solids/meshes into parametric FreeCAD-compatible features.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> The [Robot Workbench](Robot_Workbench.md) for studying robot movements. Currently unmaintained.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> The [Sketcher Workbench](Sketcher_Workbench.md) for working with geometry-constrained sketches.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> The [Spreadsheet Workbench](Spreadsheet_Workbench.md) for creating and manipulating spreadsheet data.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> The [Surface Workbench](Surface_Workbench.md) provides tools to create and modify surfaces. It is similar to the [Part Builder](Part_Builder.md) Face from edges option.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> The [TechDraw Workbench](TechDraw_Workbench.md) for producing technical drawings from 3D models.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.



### 매크로

[매크로](Macros.md) 는 단순한 또는 복잡하지만 프리캐드의 기본 시스템에 없는, 기능을 하도록 [파이썬](Python.md) 으로 작성한 단편 규모의 코드 입니다.

Power users have written various [macros](macros.md) to enhance FreeCAD with more capabilities.

Since FreeCAD 0.17, many macros can be installed using the [Addon Manager](Std_AddonMgr.md). For a list of the macros refer to the [Macros recipes](Macros_recipes.md) page. For manual installation see [How to install macros](How_to_install_macros.md).



### 남 다른 작업환경 만들기 

When many macros or functions are developed together, and are organized in toolbars and menus, they can become a new workbench.

[External workbenches](External_workbenches.md) are collections of functions that are not part of the base FreeCAD system, usually developed by experienced users, and targeting a particular need.

버젼 FreeCAD 0.17 부터는, [Addon Manager](Std_AddonMgr.md) 를 이용하여 여러가지 작업환경들을 설치할 수 있게 되었습니다. 손수 설치 하는 방법에 관해서는 [작업환경을 추가 하는 방법](How_to_install_additional_workbenches.md) 을 읽어 보세요.



## 참조

-   [Commands Reference](List_of_Commands.md): 프리캐드에서 사용하는 명령어들 전체의 목록 입니다.



## 온라인 도움말 

이것은 공개 된 프리캐드 도움말 입니다. 도움말의 전체적인 체계를 재 작업 하는 중에 있다는 것을 이해해 주시기 바랍니다. 그것은 프리캐드 패키지의 이진수 파일과 함께 배포될 .CHM 파일을 생성 하는 데 사용 될 것 입니다. 그 때가 되면 이 위키에서 가장 완성도 높은 몇 가지 부문에 대한 결과물이 온라인 도움말에 있을 것입니다.

-   \[\[Online_Help_Toc/ko\|온라인 도움말 시스템 -

목차]]



## 기타사항

-   [Power users hub](Power_users_hub.md) 는 좀 더 고급수준의 프리캐드 사용 방법을 알아 보는 곳 입니다.
-   The [FreeCAD Community Portal](FreeCAD_Community_Portal.md) 는 프리캐드에 관한 커뮤니티 회원들이 만든 프로젝트들의 목록이 있습니다.
-   프리캐드에서 사용되는 용어나 문장이 이해하기 어렵나요? [용어 설명](Glossary/ko.md) 페이지를 이용해 보세요.



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/ko
