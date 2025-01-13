# Workbenches/ko
[Revit](https://en.wikipedia.org/wiki/Autodesk_Revit) 또는 [CATIA](https://en.wikipedia.org/wiki/CATIA)와 같은 많은 최신 디자인 응용 프로그램과 마찬가지로 FreeCAD는 [작업대](https://en.wikipedia.org/wiki/Workbench)개념을 기초로 하고 있습니다. 작업대는 특정 작업을 위해 특별히 그룹화된 도구 모음로 볼 수 있습니다. 전통적인 가구 작업장에는 나무를 다루는 사람을 위한 작업대가 있고, 금속 조각을 다루는 사람을 위한 작업대가 있고, 나무와 금속 부품들을 함께 조립하는 사람을 위한 세 번째 작업대가 있을 것입니다.

FreeCAD 에서, 같은 개념이 적용됩니다. 하나의 작업대에는 해당 작업에 관련된 도구들이 모여 있습니다.

(프리캐드라는 작업장 안에서 작업물을 가지고) 다른 작업대로 이동하면, 화면에서 이용할 수 있는 도구들이 바뀝니다. 툴바, 명령어 바 등의 여러가지 화면 내용이 새로운 작업대에 따라서 바뀌지만, 작업대상물의 모습은 바뀌지 않습니다. 예를 들면, 제도 작업대에서 2D 형태의 그림으로 시작하고, 부품 작업대로 변경해서 계속 작업을 할 수 있습니다.

때로는 작업대를 \'모듈\'이라고 부르기도 합니다. 그러나 작업대와 모듈은 서로 다른 것입니다. 작업대를 포함하여 FreeCAD의 어떠한 확장 프로그램들은 모두 모듈이지만 작업대는 GUI 구성(도구모음과 메뉴)을 갖춘 특별한 유형의 모듈입니다.



## 내장된 작업대 



### 현재

다음 작업대들은 FreeCAD 설치시 묶음으로 같이 제공됩니다.


<div class="mw-translate-fuzzy">

-   <img alt="" src=images/Freecad.svg  style="width:32px;"> [표준 기반은](Std_Base/ko.md) 작업대가 아니라 모든 작업대에서 사용할 수 있는 \"표준\" 명령들의 모음입니다.


</div>

-   <img alt="" src=images/Workbench_Assembly.svg  style="width:32px;"> [조립 작업대에서는](Assembly_Workbench/ko.md) 부품들을 조립합니다. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_BIM.svg  style="width:24px;"> [BIM 작업대는](BIM_Workbench.md) 건축 요소로 작업하고 [BIM](https://en.wikipedia.org/wiki/Building_information_modeling) 모델을 만들 수 있는[외부 작업대입니다](External_workbenches/ko.md). 건축 작업대와 이전의 외부 BIM 작업대가 결합되었고{{VersionMinus|0.21}}에서 사용가능 합니다.

-   <img alt="" src=images/Workbench_CAM.svg  style="width:32px;"> [CAM 작업대는](CAM_Workbench/ko.md) G-코드 명령어를 만들 때 사용됩니다. 이 작업대는 {{VersionMinus|0.21}}에서 이름은\"Path 작업대\"였습니다.

-   <img alt="" src=images/Workbench_Draft.svg  style="width:32px;"> [설계제도 작업대에는](Draft_Workbench/ko.md) 2D 제도 도구와 기본적인 2D 및 3D CAD 작업도구들이 있습니다.

-   <img alt="" src=images/Workbench_FEM.svg  style="width:32px;"> [FEM 작업대에서는](FEM_Workbench/ko.md) 유한요소 해석을 할 수 있습니다.

-   <img alt="" src=images/Workbench_Inspection.svg  style="width:32px;"> [검사 작업대는](Inspection_Workbench/ko.md) 형상 검사를 위한 특정 도구를 제공하기 위해 만들어졌습니다. 아직은 개발 초기 단계입니다.

-   <img alt="" src=images/Workbench_Material.svg  style="width:32px;"> The [Material Workbench](Material_Workbench.md) handles the FreeCAD material system. <small>(v1.0)</small> 

-   <img alt="" src=images/Workbench_Mesh.svg  style="width:32px;"> [메쉬 작업대에서는](Mesh_Workbench.md) 삼각 메시 작업을 합니다 .

-   <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:32px;">[OpenSCAD 작업대에서는](OpenSCAD_Workbench/ko.md) OpenSCAD와의 상호 운용성 및 [Constructive solid geometry](Constructive_solid_geometry.md)(CSG) 모델 이력을 수리합니다 .

-   <img alt="" src=images/Workbench_Part.svg  style="width:32px;"> [부품 작업대](Part_Workbench/ko.md) 에서는 기하학적 기본도형 및 부울 연산을 사용하여 작업합니다.

-   <img alt="" src=images/Workbench_PartDesign.svg  style="width:32px;"> [부품 설계 작업대에서는](PartDesign_Workbench/ko.md) 스케치로부터 부품을 설계합니다.

-   <img alt="" src=images/Workbench_Points.svg  style="width:32px;"> [점 작업대에서는](Points_Workbench/ko.md) 점구름 작업을 합니다.

-   <img alt="" src=images/Workbench_Reverse_Engineering.svg  style="width:32px;"> [역설계 작업대는](Reverse_Engineering_Workbench/ko.md) 형상/솔리드/메시를 파라메트릭 FreeCAD 호환 기능으로 변환하는 특정 도구를 제공하기 위한 것입니다.

-   <img alt="" src=images/Workbench_Robot.svg  style="width:32px;"> [로봇 작업대](Robot_Workbench/ko.md) 에서는 로봇의 움직임을 다루는데 현재는 관리되지 않고 있습니다.

-   <img alt="" src=images/Workbench_Sketcher.svg  style="width:32px;"> [스케치 작업대에서는](Sketcher_Workbench/ko.md) 형상 구속이 있는 스케치를 합니다.

-   <img alt="" src=images/Workbench_Spreadsheet.svg  style="width:32px;"> [스프레드시트 작업대에서는](Spreadsheet_Workbench/ko.md) 스프레드시트 데이터를 생성하고 조할 수 있습니다.

-   <img alt="" src=images/Workbench_Surface.svg  style="width:32px;"> [표면 작업대는](Surface_Workbench/ko.md) 표면을 생성하고 수정하는 도구를 제공합니다. 이는 [Part Builder의](Part_Builder.md) 가장자리로부터 면 생성 옵션과 유사합니다.

-   <img alt="" src=images/Workbench_TechDraw.svg  style="width:32px;"> [기술도면 작업대](TechDraw_Workbench/ko.md) 에서는 3D모델을 기술도면화 하는 작업을 합니다. 0.20버전 이후 사라진[Drawing Workbench의](Drawing_Workbench.md) 후계자입니다.

-   <img alt="" src=images/Workbench_Test.svg  style="width:32px;"> The [Test Framework Workbench](Testing.md) is for debugging FreeCAD.



### 더 이상 사용되지 않음 

아래 작업대들은 프리캐드 0.21판 이후부터는 더이상 포함되지 않습니다.

-   <img alt="" src=images/Workbench_Start.svg  style="width:32px;"> The [Start Workbench](Start_Workbench.md) allows you to quickly jump to one of the most common workbenches.

-   <img alt="" src=images/Workbench_Web.svg  style="width:32px;"> The [Web Workbench](Web_Workbench.md) provides you with a browser window instead of the [3D view](3D_view.md) within FreeCAD.

The following workbenches are no longer included after version 0.20:

-   <img alt="" src=images/Workbench_Drawing.svg  style="width:32px;"> The [Drawing Workbench](Drawing_Workbench.md) was used for producing technical drawings. The [TechDraw Workbench](TechDraw_Workbench.md) is its more advanced replacement.

-   <img alt="" src=images/Workbench_Image.svg  style="width:32px;"> The [Image Workbench](Image_Workbench.md) was used for working with bitmap images. Its functionality has been integrated in [Std Base](Std_Base.md). See [Std Import](Std_Import.md) and [Std ViewLoadImage](Std_ViewLoadImage.md).

-   <img alt="" src=images/Workbench_Raytracing.svg  style="width:32px;"> The [Raytracing Workbench](Raytracing_Workbench.md) was used for ray-tracing (rendering). The external [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) should be used instead.



## 외부 작업대 

프리캐드의 작업대들은 [python으로](Python.md) 프로그램하기가 쉽습니다. 그래서 많은 사람들이 프리캐드의 주 개발 영역 밖에서도 추가적인 작업대들을 만들어 내고 있습니다.

[외부 작업대](External_workbenches/ko.md) 페이지에는 이 커뮤니티에 알려진 모든 작업대들이 나열되어 있습니다. [애드온 관리자를](Std_AddonMgr.md) 이용해 대부분은 FreeCAD 내에서 쉽게 설치할 수 있습니다.found under menu **Tools → <img src="images/Std_AddonMgr.svg" width=24px> Addon manager**.



---
⏵ [documentation index](../README.md) > [Workbenches](Category_Workbenches.md) > Workbenches/ko
