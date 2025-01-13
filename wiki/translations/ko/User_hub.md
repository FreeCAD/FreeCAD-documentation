# <img alt="" src=images/User_hub.png  style="width:64px;"> User hub/ko



여기는 FreeCAD 를 처음 사용하는 데 필요한 도움말의 요약 또는 종합 한 것 입니다.


<div class="mw-translate-fuzzy">

FreeCAD 는 계속 개발하고 있는 상태라서, 오래 된 또는 누락 된 것이 있을 수 있습니다. 필요한 정보를 찾을 수 없다면, 망설일 필요없이 [FreeCAD forum](https://forum.freecadweb.org) 에서 요청하시기 바랍니다.


</div>


<div class="mw-translate-fuzzy">

FreeCAD 에 기여하고 싶다면, [기부](donate.md), 와 [FreeCAD 돕기](Help_FreeCAD/ko.md) 페이지에 기여하는 여러가지 방법들을 읽어 보시기 바랍니다. 이 위키를 편집하고 싶다면, 여러분의 위키 계정, 문서 편집이 가능한 등급으로 설정 등 두 가지를 [포럼](https://forum.freecadweb.org/viewtopic.php?f=21&t=6830)에 들어가서 관리자에게 PM(개인간 메시지)으로 요청하고, [위키 페이지](WikiPages/ko.md) 에서 지켜야 할 규칙을 읽어 보세요.


</div>

몇 년 전에 FreeCAD가 어떻게 시작되었는지 알고 싶으면 [ 연혁](History.md) 페이지를 방문하세요.



## FreeCAD 사용에 관한 내용 



## 소개

-   [FreeCAD에 대해](About_FreeCAD/ko.md): 프리캐드에 대해 전반적으로 살펴보기
-   [설치하기](Installing.md): 프리캐드를 [윈도우에 설치하기](Installing_on_Windows/ko.md), [Linux](Install_on_Linux.md) 나 [Mac](Install_on_Mac.md) 에 설치하는 방법
-   [도움말 파일 설치](Installing_Helpfile.md): 위키를 근거로 만들어진 오프라인 도움말이 있는데, 그것을 설치하는 방법입니다.
-   [추가 기능 설치](Installing_additional_components/ko.md):프리캐드와 함께 사용 되도록 제작된 타사의 도구를 추가하는 방법.
-   [시작하기](Getting_started/ko.md): 사용할 수 있는 도구들에 대한 요약 정보
-   [자주하는 질문](Frequently_asked_questions/ko.md)
-   [자습서](Tutorials/ko.md) 에서 프리캐드의 여러가지 내용들을 다루고 있습니다.



#### 다른 프로그램의 파일을 들여오는 방법 ? 

-   [해결방법들](Workarounds/ko.md)
-   [Fusion360 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_Fusion360/ko.md)
-   [OnShape 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_OnShape/ko.md)
-   [SolidWorks 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_SolidWorks/ko.md)
-   [Revit 에서 프리캐드로 전환하기](Migrating_to_FreeCAD_from_Revit/ko.md)
-   [FreeCAD BIM migration guide](https://yorik.uncreated.net/blog/2020-010-freecad-bim-guide)
-   [프리캐드와 BIM 프로그램들의 호환성](BIM_application_compatibility_table/ko.md)



### 기본적인 사용방법들 

-   [프리캐드 화면](Interface/ko.md): FreeCAD 의 인터페이스는 그래픽 형식으로 된 [3D 보기](3D_view/ko.md), [트리 보기](Tree_view/ko.md), [속성 편집기](Property_editor/ko.md), [작업 공간](Task_panel/ko.md), [파이썬 콘솔](Python_console/ko.md) 등으로 구성되어 있습니다.
-   [Mouse navigation](Mouse_navigation/ko.md): 마우스나 트랙볼을 이용하여 \'3D 보기\'에서 탐색하는 여러가지 방법들.
-   [Selection methods](Selection_methods/ko.md): 대상물을 선택하는 여러가지 방법들이 있습니다.
-   [Objects naming](Object_name/ko.md): FreeCAD 속 한 대상물은 몇 가지의 명칭을 갖고 있는데, 시스템 내부에서 부여하는 읽기만 가능한 고유한 명칭 `Name` 과 사용자가 편집 할 수 있는 명칭 `Label` 등이 있습니다.
-   [Preferences Editor](Preferences_Editor/ko.md): 기본 시스템이나 각각의 작업대 등에 대해서 편집할 수 있는 속성을 수정할 때 사용 합니다.
-   [File formats](Import_Export/ko.md): 프리캐드로 읽거나 쓸 수 있는 여러가지 파일 형식이 있습니다.



### 작업대

[작업대는](Workbenches/ko.md) 특정 작업용 도구를 모아 놓은 것 입니다. 아래는 프리캐드라는 작업장을 여러분의 컴퓨터에 설치 할 때 함께 제공되는 작업대들 입니다:

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [표준기반 도구](Std_Base/ko.md). 는 모든 작업대에서 공통적으로 제공되는 명령어들과 도구들 입니다.

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> [조립 작업대에서는](Assembly_Workbench/ko.md) 부품들을 조립합니다 <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:32px;"> [BIM 작업대에서는](BIM_Workbench/ko.md) 건축 요소들로 작업하고 [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) 모델을 만들 수 있습니다. 이는 Arch 작업대와 {{VersionMinus|0.21}}에서 사용 가능한 이전 외부 BIM 작업대를 결합합니다.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> [CAM 작업대는](CAM_Workbench/ko.md) G-Code 명령을 생성하는 데 사용됩니다. 이 작업대는 {{VersionMinus|0.21}}에서는 \"Path 작업대\"라고 불렸습니다.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [설계도 작업대에는](Draft_Workbench/ko.md) 2D용 도구들이 있고 기본적인 수준의 3D 작업은 할 수 있습니다.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [FEM 작업대는](FEM_Workbench/ko.md) 유한요소 해석 수행을 지원 합니다.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [검사 작업대](Inspection_Workbench/ko.md) 는 형상물 확인시 사용 할 도구를 제공하기 위해 만들어 졌습니다. 아직은 개발초기 단계에 있습니다.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> The [Material Workbench](Material_Workbench.md) handles the FreeCAD material system. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [격자망 작업대에서는](Mesh_Workbench/ko.md) 삼각형 격자망으로 된 형상물 작업을 할 수 있습니다.

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;"> [OpenSCAD 작업대](OpenSCAD_Workbench/ko.md) 는 OpenSCAD 내부와 상호작용 이나 [constructive solid geometry](Constructive_solid_geometry/ko.md) (CSG) 기본형 모델의 수정 기록의 복구 등을 위한 것입니다.

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [부품 작업대에서는](Part_Workbench/ko.md) 기초 도형 개체 불러오기와 중첩영역 가감처리(=boolean, 집합연산)등의 작업을 할 수 있습니다.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [부품설계 작업대에서는](PartDesign_Workbench/ko.md) 스케치로부터 부품을 설계합니다.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [점 작업대에서는](Points_Workbench/ko.md) 점구름 작업을 합니다.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [역설계 작업대는](Reverse_Engineering_Workbench/ko.md) 모양/솔리드/메시를 파라메트릭 FreeCAD 호환 기능으로 변환하는 특정 도구를 제공하기 위한 것입니다.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [로봇 작업대는](Robot_Workbench.md) 로봇의 움직임을 연구하기 위한 작업대입니다. 현재 유지 관리되지 않습니다.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [스케치 작업대에서는](Sketcher_Workbench/ko.md) 형상 구속이 있는 스케치를 합니다.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [스프레드시트 작업대에서는](Spreadsheet_Workbench/ko.md) 스프레드시트 데이터를 생성하고 조작한다.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [표면 작업대는](Surface_Workbench/ko.md) 표면을 생성하고 수정하는 도구를 제공합니다. 이는 [Part Builder의](Part_Builder.md) 가장자리로부터 면 생성 옵션과 유사합니다.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [기술도면 작업대에서는](TechDraw_Workbench/ko.md) 3D모델을 기술도면화 하는 작업을 합니다.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.



### 매크로

[매크로](Macros.md) 는 단순한 또는 복잡하지만 프리캐드의 기본 시스템에 없는 기능을 하기 위해 [파이썬](Python.md) 으로 작성한 작은 코드 조각 입니다.

고급 사용자는 더 많은 기능으로 FreeCAD를 향상시키기 위해 다양한 [매크로를](macro.md) 작성했습니다.

FreeCAD 0.17부터 [애드온 관리자를](Std_AddonMgr.md) 사용하여 많은 매크로를 설치할 수 있습니다. 수동 설치에 대해서는 [매크로 설치 방법을](How_to_install_macros.md) 참조하세요.



## 외부 작업대 

많은 매크로나 기능을 함께 개발하여 도구 모음과 메뉴로 구성하면 새로운 작업대가 될 수 있습니다.

[외부 작업대는](External_workbenches.md) 기본 FreeCAD 시스템의 일부가 아닌 기능 모음으로, 일반적으로 숙련된 사용자가 개발하고 특정 요구 사항을 대상으로 합니다.

버젼 FreeCAD 0.17 부터는, [Addon Manager](Std_AddonMgr.md) 를 이용하여 여러가지 작업대 설치할 수 있게 되었습니다. 손수 설치 하는 방법에 관해서는 [작업대 추가 하는 방법](How_to_install_additional_workbenches.md) 을 읽어 보세요.



## 참조

-   [Commands Reference](List_of_Commands.md): 프리캐드에서 사용하는 명령어들 전체의 목록 입니다.



## 온라인 도움말 

이것은 공식 프리캐드 온라인 도움말 입니다. 도움말의 전체적인 체계를 재 작업 하는 중에 있다는 것을 이해해 주시기 바랍니다. 그것은 프리캐드 패키지의 이진수 파일과 함께 배포될 .CHM 파일을 생성 하는 데 사용 될 것 입니다. 현재 온라인 도움말에는 이 위키의 가장 완전한 섹션 중 일부가 요약되어 있습니다.

-   \[\[Online_Help_Toc/ko\|온라인 도움말

목차]]



## 기타사항

-   [Power users hub](Power_users_hub.md) 는 좀 더 고급수준의 프리캐드 사용 방법을 알아 보는 곳 입니다.
-   The [FreeCAD Community Portal](FreeCAD_Community_Portal.md) 는 프리캐드에 관한 커뮤니티 회원들이 만든 프로젝트들의 목록이 있습니다.
-   프리캐드에서 사용되는 용어나 문장이 이해하기 어렵나요? [용어집](Glossary/ko.md) 페이지를 찾아 보세요.



---
⏵ [documentation index](../README.md) > [Hubs](Category_Hubs.md) > User hub/ko
