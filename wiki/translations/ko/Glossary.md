# Glossary/ko
이 페이지에는 프리캐드에서 사용하는 기본적인 용어의 설명이 있습니다.

첫 문자 찾기:{{CompactTOC|center=yes}}

## 0-9


{{gloss}}


{{term|3D view|content=3D view ([3D 보기](3D_view/ko.md))}}


{{defn|defn= 3D 보기는 프리캐드 [인터페이스](Interface/ko.md)의 구성요 소입니다. 이것은 모형의 3차원 표현을 보여 줍니다.}}


{{glossend}}

## A


{{gloss}}


{{term|Arc (호)}}


{{defn|defn=원의 일부분.}}


{{term|App}}


{{defn|defn=프리캐드 프로그램의 내부 수준 The FreeCAD App layer.}}


{{term|Arch|content=Arch ([건축 작업대(Arch Workbench)](Arch_Workbench/ko.md))}}


{{defn|defn=이전의 건축 작업대(Architectural Workbench) 의 약어입니다. 이 작업대는 [BIM 작업대](BIM_Workbench/ko.md)(<small>(v1.0)</small> )로 대체되었습니다.}}


{{term|Assembly|content=Assembly([조립품](Assembly/ko.md))}}


{{defn|no=1|defn=서로에 대해 정의된 위치가 있는 [부품(Part)](#Part.md)의 집합입니다.}}


{{defn|no=2|defn=조립품 생성을 용이하게 하는 것을 목표로 하는 [작업대(workbench)](#Workbench.md)입니다. FreeCAD에는 현재 이러한 작업대가 내장되어 있지 않지만 여러 [외부 조립 작업대](External_workbenches/ko.md)가 있습니다.}}


{{term|Axes(축들)}}


{{defn|defn= [축(Axis)](#Axis.md)의 복수형}}


{{term|Axis (축)}}


{{defn|defn=작업 공간의 원점을 통과하는 가상의 선입니다. 3개의 법선축이 있습니다. X, Y, Z라는 고전적인 이름이 있습니다. X는 좌우입니다. Y는 위아래입니다. Z는 페이지/화면 안팎을 나타냅니다.}}


{{glossend}}

## B


{{gloss}}


{{term|Backtrace}}


{{defn|defn=Output from a debugging program that displays the series of instructions FreeCAD followed before a problem occurred.}}


{{term|Bezier Curve|content=[http://en.wikipedia.org/wiki/B%C3%A9zier_curve Bezier Curve]}}


{{defn|defn=A type of parametric curve.}}


{{term|BIM|content=[BIM (BIM 작업대)](BIM_Workbench/ko.md)}}


{{defn|defn= [https://en.wikipedia.org/wiki/Building_information_modeling Building Information Modelling]의 약자입니다. [BIM 작업대](BIM_Workbench/ko.md) 는 프리캐드에서 BIM 작업흐름을 제공합니다.}}


{{term|Blueprint}}


{{defn|defn=Old term used for [drawing](#Drawing.md), and coined for its original [http://en.wikipedia.org/wiki/Blueprint reproduction process].}}


{{term|Body ([몸통](Body/ko.md))}}


{{defn|defn=일련의 작업([스케치(sketches)](#Sketch.md), 구성 기하요소 및 [도형특징(features)](#Feature.md))을 그룹화하여 하나의 연속된 고체를 생성하는 [부품설계(PartDesing)](PartDesign_Workbench/ko.md) [작업대(workbench)](#Workbench.md)에서 사용되는 컨테이너 유형입니다. (FreeCAD V0.17에 도입되었습니다.)}}


{{term|Boolean Logic (부울 논리)}}


{{defn|defn=A method of data manipulation by using of the operands: And, Or, Not.}}


{{term|Boolean Operation (부울 연산)}}


{{defn|defn=A method of manipulating objects by using Boolean Logic. In FreeCAD, the Boolean Operations are: Union ([Fuse](#Fuse.md)), Difference ([Cut](#Cut.md)), Intersection, and Section.}}


{{term|Boolean OPerations check}}


{{defn|defn=See [BOPcheck](#BOPcheck.md).}}


{{term|BOPcheck}}


{{defn|defn=A setting that allows the Check Geometry tools in the Part WB and OpenSCAD WB to also check geometry made from [Boolean logic](#Boolean_Logic.md). The default Check Geometry setting for BOPcheck is "false" (or off). The user can enable BOPcheck to provide more accuracy when running the Check Geometry tool but this comes at the expense of longer Check Geometry processing times. Beginning with FreeCAD 0.19, the BOPcheck setting is most easily enabled from the Settings portion of the Check Geometry widget.}}


{{term|brep}}


{{defn|defn=Native file format for [Open CASCADE](#Open_CASCADE.md) and shared by a few applications. FreeCAD can save in *.brep format.}}


{{term|B-rep (경계 표현)}}


{{defn|defn=경계 표현(B-rep)은 [http://en.wikipedia.org/wiki/B-rep boundary representation]을 나타냅니다. 이는 FreeCAD가 지원하는 두 가지 유형의 3D 모델 중 하나입니다(다른 하나는 [메시(mesh)](#Mesh.md)입니다).}}


{{term|B-spline (B-조절곡선)}}


{{defn|defn=A type of parametric curve. See [http://en.wikipedia.org/wiki/B-spline B-spline]}}


{{glossend}}

## C


{{gloss}}


{{term|Callout}}


{{defn|defn=String of text connected to a line pointing to an object in a [drawing](#Drawing.md).}}


{{term|Chamfer (모따기)}}


{{defn|defn=날카로움을 없애기 위해 모서리를 비스듬히 잘라내는 것. 경사진 가장자리.}}


{{term|Clipping Plane (절단 평면)}}


{{defn|defn=절단 평면은 3D 보기에서 모형을 잘라내는 데 사용됩니다. 이는 시각적 보조 도구일 뿐 실제로 모형을 자르지는 않습니다.}}


{{term|Clone (복제본)}}


{{defn|defn=원본의 매개변수 제어 가능 상태가 유지되는 복사본입니다. 원본 개체가 변경되면 복제본도 변경되어 원본 개체에 대한 수정 사항을 똑같이 표시합니다.}}


{{term|Coin}}


{{defn|defn=Also called [https://www.coin3d.org Coin3D]. Third-party software library used for 3D representation by FreeCAD.}}


{{term|COLLADA}}


{{defn|defn=An interchange file format for [mesh](#Mesh.md) models. File extension is *.dae.}}


{{term|Command|content=[Command (명령)](Command/ko.md)}}


{{defn|defn=도구 모음 버튼을 누르거나 키보드 단축키를 입력하거나 Python 콘솔에 입력할 때 [GUI](#GUI.md)에서 호출되는 작업입니다.}}


{{term|Compound (복합)}}


{{defn|defn=Groups objects together without fusing them like a [boolean union](#Boolean_Operation.md) would.}}


{{term|CompSolid (복합체)}}


{{defn|defn=Set of [solids](#Solid.md) connected by their [faces](#Face.md). CompSolids are needed in [FEM](#FEM.md), where more than one material is used in one FEM-mesh.}}


{{term|Constraint (구속)}}


{{defn|defn=[ 스케치 (Sketch)](#Sketch.md)에서 기본 요소 간의 기하학적 관계에 대한 제약 조건입니다. 구속에 숫자 값이 있는 경우 치수 구속이라고 합니다(예: 거리 구속에는 두 점을 연결하는 가상의 선의 길이라는 숫자 값이 있습니다). 숫자 값이 없는 구속 조건(예: 수평 구속)은 기하학적 구속이라고도 합니다.}}


{{term|Constructive Solid Geometry|content=[http://en.wikipedia.org/wiki/Constructive_solid_geometry Constructive Solid Geometry]}}


{{defn|defn=A solid modeling method for creating shapes by using [boolean operations](#Boolean_Operation.md) on [primitives](#Primitive.md).}}


{{term|Coordinate (좌표)}}


{{defn|defn=A number which defines the position of an object in space in reference to a [http://en.wikipedia.org/wiki/Cartesian_coordinate_system coordinate system].}}


{{term|Coplanar (동일 평면)}}


{{defn|defn=Existing on the same plane.}}


{{term|CSG}}


{{defn|defn=Short for [Constructive Solid Geometry](#Constructive_Solid_Geometry.md).}}


{{term|Cut (자르기)}}


{{defn|defn=형상 간에 [ 부울 차이 (boolean difference)](#Boolean_Operation.md)를 적용합니다.}}


{{glossend}}

## D


{{gloss}}


{{term|DAG}}


{{defn|defn=See [Directed Acyclic Graph.](#Directed_Acyclic_Graph.md)}}


{{term|Degrees Of Freedom (자유도)}}


{{defn|defn=The number of ways geometry in a [Sketch](#Sketch.md) may vary. 예를 들어 하나의 점으로만 구성된 스케치가 있고 이 점에 [구속 (Constraint)](#Constraint.md)이 적용되지 않은 경우, 이 점은 수직과 수평 모두 자유롭게 움직일 수 있으므로 두 개의 [자유도(DOF)](#DOF.md)를 가집니다.
마찬가지로 구속이 없는 단일 원으로만 구성된 스케치는 원이 수직 및 수평으로 움직일 수 있고 반경이 정의되지 않았기 때문에 [자유도](#DOF.md)가 3입니다. [자유도](#DOF.md)가 더 이상 남아 있지 않을 때까지 스케치를 제한하는 것이 좋습니다. 이 경우 [(완전히 구속Fully Constrained)](#Fully_Constrained.md)되었다고 합니다.}}


{{term|Dependency Graph}}


{{defn|defn=A third-party graphing tool used to show how objects in a FreeCAD model use or are related to one another. For more information, refer to the [Dependency Graph](Std_DependencyGraph.md) Wiki page.}}


{{term|Difference}}


{{defn|no=1|defn=The result of, or remainder of, a subtraction.}}


{{defn|no=2|defn=A [Boolean Operation](#Boolean_operation.md) in the [Part](Part_Workbench.md) [workbench](#Workbench.md) which is used to subtract one geometry from another; it results in a [Cut](#Cut.md).}}


{{term|Directed Acyclic Graph}}

(abbreviated as \"DAG\") {{defn|defn=A type of [Dependency Graph](#Dependency_Graph.md) where the relationship of objects flows in a generally linear direction from start to end with no circular dependencies. When following a DAG there is no flow from one object A to any other objects and then back to that same object A again. In FreeCAD, a graph of the model must always be a DAG.}} {{term|DOF (자유도)}} {{defn|defn=[자유도(Degrees Of Freedom)의 약어](#Degrees_Of_Freedom.md)}} {{term|Draft|content=[Draft](Draft_Workbench.md)}} {{defn|no=1|defn=A FreeCAD [workbench](#Workbench.md) used primarily for 2 dimensional work.}} {{defn|no=2|defn=A relief angle on a mold to allow removal of the finished product. See [PartDesign Draft](PartDesign_Draft.md).}} {{term|Drawing}} {{defn|defn=Describes a representation of geometry through the use of two-dimensional views. Also called plan or [blueprint](#Blueprint.md).}} {{glossend}}

## E


{{gloss}}


{{term|Edge (모서리)}}


{{defn|no=1|defn=A segment joining two [vertices](#Vertices.md). This segment can be a straight line or a curve. The CAD kernel defines it as: One-dimensional shape corresponding to a curve and bounded by a vertex at each extremity. A closed circle has therefore only one vertex, where it starts and ends. See [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 "Open CASCADE Technology, Profile: Defining the Topology"].}}


{{defn|no=2|defn=The joining line between two faces. It can be curved or straight.}}


{{term|Element (요소)}}


{{defn|defn=An item of Sketcher geometry such as a point, a line segment, an arc, a circle, etc.}}


{{term|Expression (표현식)}}


{{defn|no=1|defn=A general term used in mathematics and programming.}}


{{defn|no=2|defn=In FreeCAD [expressions](Expressions.md) are used to compute values. They can reference and drive object properties. They are used in [spreadsheets](Spreadsheet_Workbench.md) and to control parametric models.}}


{{term|Extrude (돌출)}}


{{defn|defn=A general term for extending a 2D object into 3D along 1 direction. See also [Pad](#Pad.md).}}


{{glossend}}

## F


{{gloss}}


{{term|Face (면)}}


{{defn|defn=2차원 위상 구조입니다. 예를 들어, 직육면체에는 6개의 면이 있습니다. 면은 FreeCAD에서 면이 하나인 구의 경우처럼 곡면이 될 수 있습니다.  CAD 커널은 이를 다음과 같이 정의합니다: 닫힌 [철사(wire)](#Wire.md)로 둘러싸인 표면의 일부. [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 Profile: Defining the Topology]을 참조.}}


{{term|Facet (면)}}


{{defn|defn=Often used to describe planar faces on a [mesh](#Mesh.md).}}


{{term|FC}}


{{defn|defn=Short for FreeCAD.}}


{{term|FCStd}}


{{defn|defn=FreeCAD native file format. File extension *.fcstd, *.FCStd}}


{{term|Feature ([도형특징](PartDesign_Feature/ko.md))}}


{{defn|defn=[부품설계(Part Design)](PartDesign_Workbench/ko.md) [작업대(workbench)](#Workbench.md) 작업흐름에서 3D 부품의 기하학적 특징이 만들어지는 각 단계입니다.  예를 들면 [깔판(Pad)](#Pad.md), [오목 파기(Pocket)](#Pocket.md), [회전 홈파기(Groove)](#Groove.md), [모깎기(Fillet)](#Fillet.md), 등이 있습니다. [부품설계](PartDesign_Workbench/ko.md) [작업대(workbench)](#Workbench.md)에서 모델을 생성할 때 각 도형특징은 마지막 도형특징의 형상을 취하고 무언가를 추가하거나 제거합니다.  따라서 "오목 파기(Pocket)" 도형특징은 오목하게 판 구멍 자체뿐 아니라 그것을 포함하는 전체 부품을 의미합니다.}}


{{term|FEM|content=[FEM (유한요소법)](FEM_Workbench/ko.md)}}


{{defn|defn=[https://en.wikipedia.org/wiki/Finite_element_method Finite Element Method], a [workbench](#Workbench.md) used to solve engineering and mathematical physics problems associated with parts, assemblies and structures.}}


{{term|Fillet (모깎기)}}


{{defn|defn=A rounded relief or cut at an edge added for a finished appearance and to break sharp edges. See [Part Fillet](Part_Fillet.md) and [PartDesign Fillet](PartDesign_Fillet.md).}}


{{term|Fork}}


{{defn|defn=See [Forked Model](#Forked_Model.md).}}


{{term|Forked Model}}


{{defn|defn=A modeling method, usually accidental and incorrect in FreeCAD, that creates two or more versions of a model from a previous item. (Not to be confused with intentional operations like Array, Clone, Polar Pattern, etc.)}}


{{term|Frenet}}


{{defn|defn=When Sweeping a profile along a 3D path, the Frenet parameter controls the orientation of the profile as it travels along the path. If Frenet is true, the profiles are oriented using the Frenet Frame (tangent, binormal, normal) of the path. If Frenet is false the profile's rotation is not restricted. [https://en.wikipedia.org/wiki/Differentiable_curve#Frenet_frame Frenet frame]}}


{{term|Freetype|content=[http://www.freetype.org FreeType]}}


{{defn|defn=A freely available software library used to extract information from font definition files.}}


{{term|Frustum|content=[http://en.wikipedia.org/wiki/Frustum Frustum] (각뿔대)}}


{{defn|defn=절단하는 두 개의 평행한 평면 사이에 있는 고체 부분입니다. 컴퓨터 그래픽에서 화면에 표시되는 3차원 영역인 [http://en.wikipedia.org/wiki/Viewing_frustum "viewing frustum"]을 설명하는 데 사용됩니다.}}


{{term|Fully Constrained (완전 구속)}}


{{defn|defn=[스케치 작업대](#Sketcher.md)에서 스케치에 [자유도](#Degrees_Of_Freedom.md)가 없으면 스케치는 적용된 구속조건에 의해 "완전히 [구속](#Constraint.md)"되었다고 합니다.}}


{{term|Fuse (융합)}}


{{defn|defn=FreeCAD에서 형상의 [부울 결합(boolean union)](#Boolean_Operation.md)을 나타내기 위해 일반적으로 사용되는 용어입니다.}}


{{glossend}}

## G


{{gloss}}


{{term|GDB or gdb}}


{{defn|defn=[https://www.gnu.org/software/gdb/ '''G'''NU Project '''D'''e'''B'''ugger], a debugging program used on Unix and other 'nix operating systems in order to get a [backtrace](#Backtrace.md). "gdb" (without the quotation marks) is also the first part of the command used to start the GDB program itself. An example of how to use GDB with FreeCAD is in [http://forum.freecadweb.org/viewtopic.php?t=7052#p56918 this forum post]}}


{{term|Geometric modeling kernel}}


{{defn|defn=Also called CAD kernel. A set of complex software libraries responsible for the creation of 3D shapes. All operations on objects (extrude, boolean operations, chamfer, fillet) rely on the geometric modeling kernel.}}


{{term|Git}}


{{defn|defn=[http://en.wikipedia.org/wiki/Distributed_revision_control Distributed revision control system] used by FreeCAD to host and manage its code base.}}


{{term|[Group (모둠)](Std_Group/ko.md)}}


{{defn|defn=[나무 보기](#Tree_view.md)에서 요소들을 구조화하는 데 사용됩니다..}}


{{term|GUI}}


{{defn|defn='''G'''raphical '''U'''ser '''I'''nterface. Allows users to interact with FreeCAD through graphical icons and the mouse pointer.}}


{{glossend}}

## H


{{gloss}}


{{term|Half_Space|content=[http://en.wikipedia.org/wiki/Half-space_%28geometry%29 Half Space]}}


{{defn|defn=When a plane completely divides a 3D Euclidian space, the plane forms two half spaces.}}


{{glossend}}

## I


{{gloss}}


{{term|IGES}}


{{defn|defn=A file format for the exchange of product data models. Files extensions are *.iges, *.igs. See also [STEP](#STEP.md).}}


{{term|Intersection|content=[http://en.wikipedia.org/wiki/Intersection Intersection] (교차)}}


{{defn|defn=두 개 이상의 기하학적 개체에서 모두에게 공통되는 부분입니다. 예를 들어 두 선의 교차는 점입니다.}}


{{glossend}}

## J


{{gloss}}


{{term|JT}}


{{defn|defn=A proprietary 3D data format developed by Siemens PLM Software. FreeCAD has no support for JT at this time.}}


{{glossend}}

## K


{{gloss}}


{{term|Kernel}}


{{defn|defn=See [Geometric modeling kernel](#Geometric_modeling_kernel.md).}}


{{term|KML}}


{{defn|defn=Keyhole Markup Language - an XML-based geospatial 3D data definition file used by Google Earth. FreeCAD has no support for KML at this time.}}


{{glossend}}

## L


{{gloss}}


{{term|Label (표지)}}


{{defn|no=1|defn=개체의 사용자 정의 속성으로, [나무 보기(Tree view)](#Tree_view.md)를 사람이 더 쉽게 이해할 수 있도록 하는 데 사용됩니다.}}


{{defn|no=2|defn=A string of descriptive text added to a drawing (see [Draft Label](Draft_Label.md)).}}


{{defn|defn=Contrast with [Name](#Name.md).}}


{{term|Line (선)}}


{{defn|defn=대부분 [선분(line segment)](#Line_Segment.md)의 동의어로 사용됩니다. 스케치 작업대에서는 무한 직선 경로라는 정확한 의미로 사용되기도 합니다.}}


{{term|Line Segment (선분)}}


{{defn|defn=두 [점(points)](#Point.md)}}

사이의 직선 경로입니다. {{term|Lock (잠금)}} {{defn|defn=[잠금 구속](Sketcher_ConstrainLock/ko.md)}} {{term|Loft|content=[http://en.wikipedia.org/wiki/Loft_%283D%29 Loft]}} {{defn|defn=A topological form created by linking consecutive profiles with a surface. Similar to the process used to make fabric covered aeroplanes or boats. Also the FreeCAD function for creating such a form.}} {{glossend}}

## M


{{gloss}}


{{term|Macro}}


{{defn|defn=A saved sequence of FreeCAD instructions, often written by end users.}}


{{term|Manifold (다양체)}}


{{defn|defn=완벽하게 밀폐되어 부피를 형성하는 [형상](#Shape.md)을 말합니다. 이를 잘 설명하는 친숙한 동의어는 "수밀"입니다. 고체를 생성하려면, a [shell](#Shell.md) must be manifold.}}


{{term|Mantis}}


{{defn|defn=[Bug tracking system](#Tracker.md) used by the FreeCAD project.}}


{{term|Mesh}}


{{defn|defn=Type of object that can be imported or created by FreeCAD. See [http://en.wikipedia.org/wiki/Polygon_mesh Polygon mesh] for more details.}}


{{term|Model (모형)}}


{{defn|defn=3D 모형 이라고도 합니다. 3차원 [부품(part)](#Part.md)이나 [조립품(assembly)](#Assembly.md)을 컴퓨터로 표현한 것입니다.}}


{{term|MultiTransform|content=[MultiTransform](PartDesign_MultiTransform.md)}}


{{defn|defn=Stands for multiple transformation. A [feature](#Feature.md) from the [PartDesign](PartDesign_Workbench.md) [workbench](#Workbench.md) that applies a series of chained transformations (linear and circular pattern, mirrored) to selected features.}}


{{glossend}}

## N


{{gloss}}


{{term|Name (이름)}}


{{defn|defn=FreeCAD 문서 개체에 대한 고유 식별자입니다. 프로그램에서 한 번 할당된 이름은 쉽게 변경할 수 없습니다. [표지(Label)](#Label.md)와 대조됩니다.}}


{{term|Non-manifold (비다양체)}}


{{defn|defn=Non-manifold topology, also called zero-thickness, is two distinct solid bodies connected at a theoretical vertex or edge. It is an unsupported type of shape (not always detected by FreeCAD) that should be avoided, as it can cause trouble with further steps and export.}}


{{term|Null Shape}}


{{defn|defn=A [Shape](#Shape.md) property that has not been initialized by a program/macro. Usually an error condition.}}


{{glossend}}

## O


{{gloss}}


{{term|OCC}}


{{defn|defn=Acronym for [Open CASCADE](#Open_CASCADE.md). Prior to being open sourced, it used to be named CAS.CADE (abbreviated from Computer Aided Software for Computer Aided Design and Engineering).}}


{{term|OCE}}


{{defn|defn='''O'''pen CASCADE '''C'''ommunity '''E'''dition. It provides patches, improvements and experiments contributed by users over the official [Open CASCADE](#Open_CASCADE.md) library. FreeCAD is known to work on either OCC or OCE.}}


{{term|OCCT}}


{{defn|defn=Open CASCADE Technology. See [OCC](#OCC.md).}}


{{term|Open CASCADE|content=[http://www.opencascade.org Open CASCADE]}}


{{defn|defn=The [geometric modeling kernel](#Geometric_modeling_kernel.md) (software library) underlying FreeCAD. Also called [OCC](#OCC.md) or [OCCT](#OCCT.md) (for Open CASCADE Technology). See also [OCE](#OCE.md).}}


{{term|OpenSCAD|content=[http://www.openscad.org/ OpenSCAD]}}


{{defn|no=1|defn=Name of a script-only based CAD program.}}


{{defn|no=2|defn=A [workbench](#Workbench.md) in FreeCAD. The [OpenSCAD](OpenSCAD_Workbench.md) [workbench](#Workbench.md) provides an interface for import/export of *.scad and *.csg models, as well as a some utility tools.}}


{{term|Origin (원점)}}


{{defn|defn=좌표계의 중심입니다. 모든 것은 여기서부터 양 또는 음의 방향으로 나갑니다. 지구를 '원점'으로 보는 우리의 우주관도 마찬가지입니다.}}


{{term|Orthographic (평행 투상)}}


{{defn|defn=See [http://en.wikipedia.org/wiki/Orthographic_projection Orthographic projection] and [http://en.wikipedia.org/wiki/Multiview_orthographic_projection Multiview orthographic projection].}}


{{glossend}}

## P


{{gloss}}


{{term|Pad (깔판)}}


{{defn|defn=[스케치(Sketch)](#Sketch.md)의 평면에 수직인 방향으로 스케치를 신장시킨 것입니다. [돌출(Extrude)](#Extrude.md)도 참조하세요.}}


{{term|Part (부품)}}


{{defn|no=1|defn=A FreeCAD [workbench](#Workbench.md) primarily used for a [http://en.wikipedia.org/wiki/Constructive_solid_geometry Constructive Solid Geometry] workflow. See [부품 작업대(Part Workbench)](Part_Workbench/ko.md).}}


{{defn|no=2|defn=A FreeCAD Python module, directly interfacing with [OCC](#OCC.md). See [Part scripting](Part_scripting.md).}}


{{defn|no=3|defn=A container which groups any type of FreeCAD object and has a [placement](#Placement.md). See [Std Part](Std_Part.md).}}


{{defn|no=4|defn=A unibody solid. The lowest level component in an assembly.}}


{{term|PartDesignNext}}


{{defn|defn=Nickname used over the forums to distinguish the [PartDesign](PartDesign_Workbench.md) [workbench](#Workbench.md) in the FreeCAD 0.17 release version from the one in v0.16 and earlier, because of the vast changes introduced.}}


{{term|PD}}


{{defn|defn=Abbreviation of [PartDesign](PartDesign_Workbench.md), a FreeCAD [workbench](#Workbench.md).}}


{{term|PDN}}


{{defn|defn=Abbreviation of [PartDesignNext](#PartDesignNext.md).}}


{{term|Perspective (원근법)}}


{{defn|defn=[http://en.wikipedia.org/wiki/Graphical_projection#Perspective Perspective projection]}}


{{term|Pivy|content=[http://pypi.python.org/pypi/Pivy Pivy]}}


{{defn|defn=A software library that allows Python to use Coin.}}


{{term|Placement (배치)}}


{{defn|defn=공간에서 개체의 좌표와 방향을 정의하는 속성 집합입니다. [배치](Placement/ko.md)를 참고하세요.}}


{{term|Planar (평면적)}}


{{defn|defn=모든 요소가 같은 평면에 놓여 있는 기하학적 구조를 말합니다.}}


{{term|Plane (평면)}}


{{defn|no=1|defn=무한히 멀리 확장되는 평평한 2차원 표면입니다.}}


{{defn|no=2|defn=[부품(Part)](Part_Workbench/ko.md) [작업대(workbench)](#Workbench.md)에서 생성된 기초적인 2차원 객체 .}}


{{term|Plot}}


{{defn|no=1|defn=An outdated synonym for a technical drawing made by a pen plotter. See [https://en.wikipedia.org/wiki/Plotter Plotter]}}


{{defn|no=2|defn=Short for plot plan. See [https://en.wikipedia.org/wiki/Site_plan Site plan]}}


{{defn|no=3|defn=Graphical representation of data. See [https://en.wikipedia.org/wiki/Plot_(graphics) Plot (graphics)]}}


{{term|Pocket (오목 자리)}}


{{defn|defn=[스케치](#Sketch.md)를 기반으로 고체에서 재료를 제거하는 [도형특징(feature)](#Feature.md)입니다.}}


{{term|Point (점)}}


{{defn|defn=3D 작업 공간에서 단일 영역을 참조하는 데 사용되는 항목입니다. "점"은 치수가 없습니다.그렇지만 우리가 보는 화면에는 치수가 있으며, 일반적으로 "점"으로만 표시되어 위치를 확인할 수 있습니다. [꼭지점(Vertex)](#Vertex.md)도 참조하세요.}}


{{term|Polygon mesh}}


{{defn|defn=See [http://en.wikipedia.org/wiki/Polygonal_mesh Polygonal_mesh]}}


{{term|Polyline (꺾은선)}}


{{defn|defn=여러 가지 길이와 방향을 가진 선분들을 차례로 이은 선입니다.}}


{{term|POV-Ray (POV-광선)}}


{{defn|defn=[http://en.wikipedia.org/wiki/POV-Ray POV-Ray]}}


{{term|PPA}}


{{defn|defn=An acronym that stands for '''P'''ersonal '''P'''ackage '''A'''rchive. It's a type of software repository exclusive to the Ubuntu Linux operating system. The FreeCAD project offers the latest release as well as development versions through two PPA repositories. Updates are managed by the host system's update manager.}}


{{term|Primitive (기본 도형)}}


{{defn|defn=모형 제작에 사용되는 기본 형상입니다. 일부 2D 기본 요소에는 점, 선, 다각형, 원, 타원, spiral, helix 이 있습니다. 3D 기본 요소에는 상자, 원통, 원뿔, 원환체, 구, 타원체, 각기둥이 있습니다.}}


{{term|PySide|content=[https://wiki.qt.io/PySide PySide]}}


{{defn|defn=A freely available software library that allows Python to use QT.}}


{{term|Python|content=[http://www.python.org Python]}}


{{defn|defn=A programming language used in the development of FreeCAD as well as in user-written [macros](#Macro.md) or scripts.}}


{{glossend}}

## Q


{{gloss}}


{{term|Qt|content=[https://www.qt.io/developers/ Qt]}}


{{defn|defn=A cross-platform application and user interface framework.}}


{{glossend}}

## R


{{gloss}}


{{term|Raytracing (광선추적)}}


{{defn|defn=[http://en.wikipedia.org/wiki/Ray_tracing_%28graphics%29 Ray tracing]}}


{{term|Revolve (공전)}}


{{defn|defn=A tool in the [Part](Part_Workbench.md) [workbench](#Workbench.md). See [Part Revolve](Part_Revolve.md).}}


{{term|Robot (로봇)}}


{{defn|defn=[http://en.wikipedia.org/wiki/Industrial_robot Industrial robot]}}


{{term|Rotate (회전)}}


{{defn|defn=개체를 축으로 회전시켜 공간에서 방향을 변경하는 동작입니다.}}


{{glossend}}

## S


{{gloss}}


{{term|Section (단면)}}


{{defn|defn=[http://en.wikipedia.org/wiki/Cross_section_%28geometry%29 Cross section (geometry)]}}


{{term|Self Intersection (자기교차)}}


{{defn|defn=곡선이 자기 자신을 가로지르는 조건입니다(예: '8','&'). 이는 기하학적 커널 알고리즘을 혼란스럽게 하고 일반적으로 오류 조건을 생성합니다.}}


{{term|Shape (형상)}}


{{defn|defn=FreeCAD에서 ([meshes](#Mesh.md)를 제외한) 도형의 대부분의 요소를 설명하기 위해 사용되는 일반적인 용어입니다.}}


{{term|Shell (껍질)}}


{{defn|defn=두 개 이상의 연속된 [면(face)](#Face.md)으로 이루어진 형상입니다. [다양체](#Manifold.md) (enclosed) 껍질은 [고체](#Solid.md)로 전환될 수 있습니다..}}


{{term|Sketch (스케치)}}


{{defn|defn=평면 또는 [면(Face)](#Face.md)에 고정된 개체의 구속된 2D 그림입니다. FreeCAD에서 스케치는 항상 3D 공간의 어딘가에 있는 2차원 개체입니다.}}


{{term|Sketcher|content=[Sketcher](Sketcher_Workbench.md) (스케치 작업대)}}


{{defn|defn=A [workbench](#Workbench.md) used to create 2D geometry by use of [elements](#Element.md) and [constraints](#Constraint.md).}}


{{term|Sketcher Solver}}


{{defn|defn=The internal FreeCAD mechanism that calculates inter-dependencies and effects of adding, deleting, and modifying geometry and associated constraints in each Sketch. Sketcher Solver also calculates the arrangement of all geometry in each Sketch so it can be displayed correctly.}}


{{term|Smooth Line}}


{{defn|defn=In a Drawing, a line indicating a change between tangent surfaces, as in the transition from a flat surface to a fillet. Also "tangent edge". See [Drawing View](Drawing_View#Modify_an_existing_view.md)}}


{{term|Solid (고체)}}


{{defn|defn=[Shells](#Shell.md)로 둘러싸인 3D 공간의 일부입니다. 고체에는 질량이 있는 개체와 관련된 부피 및 기타 속성이 있습니다.}}


{{term|Solver}}


{{defn|defn=See [Sketcher Solver](#Sketcher_Solver.md).}}


{{term|Stable}}


{{defn|defn=A nickname for the last general release version of the FreeCAD software. This is typically the version available from sources other than the FreeCAD project. Compare with [Unstable](#Unstable.md).}}


{{term|STL}}


{{defn|defn=''STereoLithography'', also known as ''Standard Tessellation Language.'' A [mesh](#Mesh.md) file format defining only the surface of a 3D object. File extensions is *.stl}}


{{term|STEP}}


{{defn|defn=An ISO standard (ISO 10303) for the exchange of 3D data and product manufacturing information. It replaces [IGES](#IGES.md). File extensions are *.step, *.stp.}}


{{term|SVG}}


{{defn|defn=[https://en.wikipedia.org/wiki/Scalable_Vector_Graphics Scalable Vector Graphics]. A vector graphics file format.}}


{{term|Sweep (쓸기)}}


{{defn|defn=하나 이상의 2D 단면을 궤적(경로)을 따라 쓸어서 생성된 3D 형상입니다. 생성된 형상뿐만 아니라 도구를 정의하는 데 일반적으로 사용됩니다. See [http://en.wikipedia.org/wiki/Solid_modeling#Sweeping Solid modeling]}}


{{glossend}}

## T


{{gloss}}


{{term|Task panel (작업판)}}


{{defn|defn=A [https://en.wikipedia.org/wiki/Panel_(computer_software) control panel] in FreeCAD that displays content specific to the task at hand. It can show available tools in the active [workbench](#Workbench.md) or prompt for values and options while a [command](#Command.md) is active.}}


{{term|Tasks tab}}


{{defn|defn=See [Task panel](#Task_panel.md).}}


{{term|Tessellation (쪽매 붙임)}}


{{defn|defn=쪽매붙임(tessellation)은 쪽매(tile)이라고 하는 하나 이상의 기하학적 형상을  겹치지 않고 빈틈 없이 표면을 붙이는 것입니다. FreeCAD에서는 3D 보기에 기하학적 형상을 표시하는 데 필요합니다. 기본 설정에서 도형의 치수를 기준으로 쪽매붙임을 설정하면 계산 시간을 절약하면서 둥근 표면을 더 매끄럽게 볼 수 있습니다. [Preferences Editor](Preferences_Editor.md)를 참고하세요.}}


{{term|Thickness (두께)}}


{{defn|no=1|defn=A measure of how thick a shape is.}}


{{defn|no=2|defn=A [Part](Part_Workbench.md) [workbench](#Workbench.md) tool to hollow out a solid and leave a defined uniform thickness.}}


{{term|Toggle (전환)}}


{{defn|defn=True 또는 False, Off와 On 등 두 가지 옵션 간에 변경할 수 있는 설정입니다.}}


{{term|Topological Naming (위상적 이름 짓기)}}


{{defn|defn=모서리 또는 면이 생성되면 영구적인 이름이 할당되는 체계입니다. 내부적으로 FreeCAD는 고체의 모서리와 면에 번호를 부여하여 식별합니다: 모서리1, 모서리2, 면1, 면2 등입니다. 문제는 이러한 ID가 다소 무작위로 적용되며 모형에 모서리와 면의 양을 변경하는 작업이 수행된 후에 이 이름이 변경된다는 것입니다. 예를 들어, 모형을 수정하면 면2에 연결된 항목이 나중에 다른 면(이름이 바뀌어 새로운 면2가 된)에 잘못 연결되어 사용자가 원하지 않는 결과를 초래할 수 있습니다. FreeCAD 0.20 릴리스에서는 토폴로지 명명 기능이 아직 구현되지 않았으므로 개체를 수정하여 모서리 또는 면의 수가 변경되면 해당 개체의 모서리 또는 면의 이름도 변경될 수 있습니다.}}


{{term|Torus (원환체)}}


{{defn|defn=기본 입체 도형의 하나}}


{{term|Tracker (추적기)}}


{{defn|defn=Short for bug tracker, the online software application used to keep track of reported bugs or feature requests. See also [Mantis](#Mantis.md).}}


{{term|Tree view|content=[Tree View (나무 보기)](Tree_view/ko.md)}}


{{defn|defn=나무 보기는 FreeCAD [인터페이스](interface/ko.md)의 구성 요소입니다. 이는 별도의 [GUI](#GUI.md) 요소로 표시되거나 [Combo View](Combo_View.md)의 일부로 표시될 수 있습니다. 여기에는 문서 구조의 표현이 포함됩니다.}}


{{glossend}}

## U


{{gloss}}


{{term|Union (결합)}}


{{defn|defn=A [Part](Part_Workbench.md) [workbench](#Workbench.md) tool that performs a [Boolean operation](#Boolean_Operation.md) on selected shapes.}}


{{term|Unstable}}


{{defn|defn=A nickname for a very recent version of the FreeCAD software. This version will contain many changes recently implemented by the developers. It does not typically fail or produce wrong results, but it has not completed testing.}}


{{term|Upgrade|content=[Upgrade](Draft_Upgrade.md)}}


{{defn|defn=A [Draft](Draft_Workbench.md) [workbench](#Workbench.md) tool.}}


{{glossend}}

## V


{{gloss}}


{{term|Vector (향량)}}


{{defn|defn=방향이 있는 크기입니다. 종종 2차원 또는 3차원의 화살표로 표현됩니다. For example, "fifty paces north", "9.8 m/s^2 down", and "(3,5,6) units in the x, y, z, direction, respectively" are all vectors. FreeCAD에서는 정렬된 쌍(x, y) 또는 정렬된 삼항(x, y, z)으로 표시되는 경우가 가장 많습니다.}}


{{term|Vertex (꼭지점)}}


{{defn|defn=공간에 홀로 있는 [점](#Point.md) 또는 [모서리들](#Edge.md)이 만나는 [형상](#shape.md)의 구석 입니다. 개방형 캐스케이드 기술(open Cascade Technology)은 이를 기하학의 한 점에 해당하는 0차원 [형상](#shape.md)으로 정의합니다. [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 OCCT 프로필: 토폴로지 정의]를 참조하세요.}}


{{term|Vertices (꼭지점들)}}


{{defn|defn=[꼭지점(Vertex)](#Vertex.md)의 복수형}}


{{term|Viewprovider}}


{{defn|defn=General interface for all visual stuff in FreeCAD. A ViewProvider generates and handles all around visualizing and presenting objects from the FreeCAD [App layer](#App.md) to the user. This class and its descendents have to be implemented for any object type in order to show them in the [3D view](#3D_view.md) and [Tree view](#Tree_view.md).}}


{{glossend}}

## W


<div class="mw-translate-fuzzy">


{{gloss}}


{{term|WB}}


{{defn|defn= [Workbench](#Workbench.md)의 줄임말.}}


{{term|Wire (철사)}}


{{defn|no=1|defn=[꼭지점들](#Vertex.md)로 연결된 일련의 [모서리들](#Edge.md) 입니다. Wire(철사)라는 용어는 주로 [https://dev.opencascade.org/doc/overview/html/occt__tutorial.html#OCCT_TUTORIAL_SUB2_3 Open Cascade Technology]에서 이러한 의미로 사용되므로 이 OCT를 사용하는FreeCAD 에서도 같은 의미로 사용됩니다.}}


{{defn|no=2|defn=매개변수로 제어 가능한 철사를 만드는 [설계제도(Draft)](Draft_Workbench/ko.md) [작업대(workbench)](#Workbench.md)의 명령어 입니다.}}


{{term|Workbench (작업대)}}


{{defn|defn=모듈이라고도 하는 각 작업대는 특정 작업 전용 도구 세트를 그룹화합니다.}}


{{glossend}}


</div>

## X


{{gloss}}


{{term|X}}


{{defn|defn=일반적으로 2D 또는 3D X [축(axis)](#Axis.md)을 나타냅니다.}}


{{glossend}}

## Y


{{gloss}}


{{term|Y}}


{{defn|defn=일반적으로 2D 또는 3D Y [축(axis)](#Axis.md)을 나타냅니다.}}


{{glossend}}

## Z


{{gloss}}


{{term|Z}}


{{defn|defn=일반적으로 3D Z [축(axis)](#Axis.md)을 나타냅니다.}}


{{glossend}}



---
⏵ [documentation index](../README.md) > [Wiki](Category_Wiki.md) > [Glossary](Category_Glossary.md) > Glossary/ko
