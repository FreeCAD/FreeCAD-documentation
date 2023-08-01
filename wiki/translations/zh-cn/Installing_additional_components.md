# Installing additional components/zh-cn
<div class="mw-translate-fuzzy">





</div>




# Introduction


<div class="mw-translate-fuzzy">

## 选择你操作系统

FreeCAD 是一个真正的跨平台应用程序，基于世界知名的 [Qt](http://en.wikipedia.org/wiki/Qt_(framework)) 框架之上。这意味着 FreeCAD 外观和行为与在 Windows, Linux 和 Mac 上是一致的。然而，安装过程在每个操作系统上是有所不同的。在下面选择你的操作系统以获得更多细节关于如何安装 FreeCAD。

    
   ![ alt=\'Windows\' \| link= Install on Windows](images/Windows.png )   ![ alt=\'Linux\' \| link= Install on Linux](images/Linux.png )   ![ alt=\'Mac\' \| link= Install on Mac](images/Mac.png )
                           [在 Windows 上安装](Install_on_Windows/zh-cn.md)                                                [在 Linux 上安装](Install_on_Linux/zh-cn.md)                                          [在 Mac 上安装](Install_on_Mac/zh-cn.md)
    


</div>

# Help files 

See [Installing Helpfile](Installing_Helpfile.md).

# External workbenches 


<div class="mw-translate-fuzzy">

除了默认捆绑在 FreeCAD 的 [工作台](workbenches/zh-cn.md) 以外，还有由社区成员制作的一堆很有用额外工作台和模块在网络持续增长。几个进行中的成果是收集它们和令它们方便地展示给你。下面是它们的列表。


</div>


<div class="mw-translate-fuzzy">

## FreeCAD支持的外部软件

FreeCAD支持大量开包即用的外部软件。这就意味着：您只需简单地安装想用的软件，在下次重新开启FreeCAD后便可自动在其中使用此软件了。此过程中无需对其进行重新编译。本节的目标便是提供所有此类软件包的列表，同时给出在FreeCAD中使用这些软件的有关信息以及它们的获取方式。


</div>

FreeCAD supports several third party software packages out of the box. In many cases all you need to do is install the software, and when FreeCAD is restarted it will automatically find and be able to use it. This section aims to provide a list of such software packages, together with some information about where they are used in FreeCAD and where they can be downloaded.

## Support


<div class="mw-translate-fuzzy">

### GitPython

一种用于与Git仓库进行交互的python库。FreeCAD中的此功能在还处于开发状态中。[插件管理器可利用此库从Git仓库中导入各种扩展插件](Std_AddonMgr.md)。此项目托管在GitHub中的 <https://github.com/gitpython-developers/GitPython> 。


</div>

[GitPython](https://github.com/gitpython-developers/GitPython) is a library to interact with Git repositories. The [Addon Manager](Std_AddonMgr.md) can use this library. GitPython is included in the FreeCAD installers for Windows and Mac.


<div class="mw-translate-fuzzy">

### GraphViz

GraphViz是一款开源的图形可视化（graph visualization）软件。在FreeCAD中可通过**Tools → Dependency Graph...**来令它生成依赖图。它的主页位于 <https://www.graphviz.org>


</div>

[GraphViz](https://www.graphviz.org) is an open source graph visualization software. It is used by the [Std DependencyGraph](Std_DependencyGraph.md) tool.


<div class="mw-translate-fuzzy">

### OpenCAMLib

一种提供计算机辅助制造（computer aided manufacturing (CAM)）算法的开源库。在FreeCAD中的[路径工作台（Path Workbench）会用到它](Path_Workbench.md)。OpenCAMLib的首页位于 <http://www.anderswallin.net/CAM/> 。


</div>

[OpenCAMLib](http://www.anderswallin.net/CAM) is an open source library of computer aided manufacturing (CAM) algorithms. It is used in the [Path Workbench](Path_Workbench.md). See the [OpenCamLib](OpenCamLib.md) page for installation instructions.


<div class="mw-translate-fuzzy">

### OpenSCAD

此程序化3D实体CAD建模工具是另一种基于结构实体几何（Constructive Solid Geometry (CSG)）的CAD软件。这意味着：它不能处理网格，而是专用于操作实体几何图形。在FreeCAD中，可通过在**File → Import**与**File → Export**菜单中选择**OpenSCAD CSG format**或**OpenSCAD format**文件类型来导入、导出OpenSCAD所创建的文件。您可以从 <https://www.openscad.org> 处搞到OpenSCAD。


</div>

[OpenSCAD](https://www.openscad.org) is a solid 3D modeller. The [OpenSCAD Workbench](OpenSCAD_Workbench.md) depends on this software and the [Mesh Workbench](Mesh_Workbench.md) uses it for its Boolean tools. It is also required for the import of SCAD files with the [Std Import](Std_Import.md) tool.

## File formats 

All software in this section will be used by the [Std Import](Std_Import.md) or [Std Export](Std_Export.md) tools.


<div class="mw-translate-fuzzy">

### CAD Exchanger 

此为一种用于交换CAD中所用各种文件格式的专用闭源应用程序。您可以用它把专有闭源的格式转换为FreeCAD可访问的格式。本工具的主页为 <https://cadexchanger.com/> ，在此，您可以下载该软件的评估版或购买该软件的使用许可。


</div>

[CADExchanger](https://cadexchanger.com) is a commercial application for exchanging various CAD file formats. There is an [external workbench](https://github.com/yorikvanhavre/CADExchanger) to use this application in FreeCAD.


<div class="mw-translate-fuzzy">

### DXF Importer 

FreeCAD中有一个以C++编写的DXF原生导入、导出工具。 此导入器当前还未实现DXF格式的所有特性。如果您用到了那些还没有实现的特性，可通过在**Edit → Preferences → Import-Export**中选择**Use legacy python importer**选项来开启基于python的旧版导入/导出工具。您还可以通过**Allow FreeCAD to automatically download and update the DXF libaries**选项令FreeCAD自动从 <https://github.com/yorikvanhavre/Draft-dxf-importer> 下载所需文件，或自己手动下载。被选中的导入 / 导出工具用于实现**File → Import** 或 **File → Export**中**AutoDesk DXF 2D**文件格式的导入导出工作。（译注：简而言之，原生导入导出器有新旧两种，旧版以python编写，功能完整但速度较慢；新版由C++编写，速度快但功能还未完整实现。）


</div>

FreeCAD has a native importer and exporter for DXF files, programmed in C++. Currently they do not implement all features of the DXF format. For those features the legacy Python importer and exporter are still available. These require the [Draft-dxf-importer](https://github.com/yorikvanhavre/Draft-dxf-importer) Python library. See the [FreeCAD and DXF Import](FreeCAD_and_DXF_Import.md) page for more information.

### DWG converters 

FreeCAD cannot directly read and write DWG files. To convert DXF files to DWG files, and vice-versa, FreeCAD relies on external converters. There is built-in support for the following DWG converters:

-   [LibreDWG](https://www.gnu.org/software/libredwg) (open-source, lacks support for some DWG entities).
-   [ODA File Converter](https://www.opendesign.com/guestfiles/oda_file_converter) (free, but not open-source).
-   [QCAD pro](https://qcad.org/en/qcad-command-line-tools#dwg2dwg) (commercial). <small>(v0.20)</small> 

See [Import Export Preferences](Import_Export_Preferences#DWG.md) and [FreeCAD and DWG Import](FreeCAD_and_DWG_Import.md) for more information.


<div class="mw-translate-fuzzy">

### ifcOpenShell

IfcOpenShell是一种用来处理建筑设计所用Industry Foundation Classes (IFC)文件格式的库。可在[建筑工作台（Arch Workbench）中通过](Arch_Workbench.md)**Arch → Utilities → Ifc Explorer**来访问它。ifcOpenShell的主页位于 <http://ifcopenshell.org> 。


</div>

[IfcOpenShell](http://ifcopenshell.org) is a library for working with the Industry Foundation Classes (IFC) file format used in architectural design. The library is also used by the [Arch IfcExplorer](Arch_IfcExplorer.md) ({{VersionMinus|0.18}}) and [BIM IfcExplorer](BIM_IfcExplorer.md) tools. IfcOpenShell is included in the FreeCAD installers for Windows and Mac.

### IfcJson

[IfcJson](https://github.com/buildingSMART/ifcJSON) is a library required for exporting to the IFCJSON file format. IFCJSON is a new IFC format that is not yet supported by many applications.


<div class="mw-translate-fuzzy">

### pycollada

Pycollada，又名`python-collada`，是一款用来读写COLLADA文档（一种用于交换3D场景与元素的标准）的Python库。如果您安装了pycollada，就可以通过在**File → Import**与 **File → Export**命令中选择COLLADA文件类型，以COLLADA导入/导出场景。此项目托管于GitHub中的 <https://pycollada.github.io/> ，您可以从 <https://github.com/pycollada/pycollada/releases/> 下载其发行版。


</div>

[Pycollada](https://github.com/pycollada/pycollada/releases), also known as python-collada, is a Python library to read and write Collada (DAE) files. Pycollada is included in the FreeCAD installers for Windows and Mac.

## Rendering

### LuxCoreRender

[LuxCoreRender](https://www.luxcorerender.org) is a render engine, reboot of the [LuxRender](LuxRender.md) project. Officially it is not supported by the [Raytracing Workbench](Raytracing_Workbench.md), but it might be worth to give it a try. It is officially supported by the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-render), intended as a future replacement of the Raytracing Workbench. See the [LuxCoreRender](LuxCoreRender.md) page for more information and installation instructions.

### LuxRender

[LuxRender](https://luxcorerender.org/history/) is one of the two render engines supported by the [Raytracing Workbench](Raytracing_Workbench.md). In 2013 the project has been rebooted becoming [LuxCoreRender](LuxCoreRender.md), with a major code rewriting and compatibility breaking changes. Officially the Raytracing Workbench only supports the abandoned [LuxRender](LuxRender.md) (latest version is 1.6, 2017-12-28), while the new [Render Workbench](https://github.com/FreeCAD/FreeCAD-render) (intended as a future replacement of the Raytracing Workbench) supports instead LuxCoreRender and has dropped the support for LuxRender. Anyway, even if officially not supported, [LuxCoreRender](LuxCoreRender.md) may work with the Raytracing Workbench, it might be worth to give it a try. See the [LuxRender](LuxRender.md) page for more information and installation instructions, and the [LuxCoreRender](LuxCoreRender.md) if you want to try a more modern software.


<div class="mw-translate-fuzzy">

### POVRay

POVRay是一款人所共知的光线追踪器，借助它可渲染出照片级的图像。它在FreeCAD[光线追踪工作台（Raytracing Workbench）目前所支持的两种光追器中坐有一席](Raytracing_Workbench.md)。可以从 <https://www.povray.org> 下载到POVRay。


</div>

[POV-Ray](https://www.povray.org) is a well-known ray-tracer which can render photo-realistic images. It is one of two render engines currently supported by the [Raytracing Workbench](Raytracing_Workbench.md). See the [POV-Ray](POV-Ray.md) page for more information and installation instructions.

## Finite element 


<div class="mw-translate-fuzzy">

### CalculiX

CalculiX是两种有限元包的组合套件：

-   CalculiX CrunchiX, 或`calculix-ccx`为一种有限元求解器（FEM solver）。
-   CalculiX GraphiX, 或`calculix-cgx`为一种显示求解器计算结果的GUI前端。


</div>

[CalculiX](http://calculix.de) is a suite of two finite element packages: CalculiX CrunchiX, a FEM solver, and CalculiX GraphiX, a GUI frontend. Only the solver is supported by FreeCAD. It is used by the [Solver CalculiX](FEM_SolverCalculiX.md) tool.


<div class="mw-translate-fuzzy">

### Gmsh

一种3D有限元网格自动生成器。可在FreeCAD的[有限元工作台（FEM workbench）中](FEM_Workbench.md)，通过**Mesh → FEM mesh from shape by gmsh**来使用它。gmsh的主页位于 <http://www.geuz.org/gmsh>


</div>

[Gmsh](http://gmsh.info) is an automatic finite element mesh generator. it is used by the [FEM MeshGmshFromShape](FEM_MeshGmshFromShape.md) and [Mesh FromPartShape](Mesh_FromPartShape.md) tools.


<div class="mw-translate-fuzzy">

### Elmer

Elmer是一种多物理模拟软件，开源于2005年。在FreeCAD中，可通过**Solve->Solver Elmer**令[有限元工作台（FEM Workbench）调用Elmer的网格与求解](FEM_Workbench.md)（Grid and Solver）模块。Elmer项目的主页位于 <https://www.elmerfem.org> ，可从GitHub中的 <https://github.com/ElmerCSC/elmerfem/releases> 处下载。


</div>

[Elmer](https://www.csc.fi/web/elmer) is a multi-physics simulation software, which was open sourced in 2005. In FreeCAD its Grid and Solver modules are used by the [FEM SolverElmer](FEM_SolverElmer.md) tool.


<div class="mw-translate-fuzzy">

### FEniCS

FEniCS是一种解偏微分方程（partial differential equations (PDEs)）的计算平台，广泛应用于解决有限元（FEM）问题。自然而然，[有限元工作台（FEM Workbench）也不例外](FEM_Workbench.md)。在FreeCAD里，可通过在**File → Import**与**File → Export**中选择**FEM mesh fenics**文件格式来导入或导出FEniCS网格。FEniCS的主页位于 <https://fenicsproject.org> 。


</div>

[FEniCS](https://fenicsproject.org) is a computing platform to solve partial differential equations (PDEs), which are widely used when solving FEM problems. It is used by the [FEM workbench](FEM_Workbench.md)


<div class="mw-translate-fuzzy">

### Z88

Z88是另一种FEM程序，内含网格生成器、求解器与转换器，用于FreeCAD的[有限元工作台中](FEM_Workbench.md)。可通过**Solve-Solver Z88**来访问它。Z88发布了多种包，皆为闭源免费使用。而Z88OS则是发布于开源许可证之下，这正是FreeCAD所梦寐以求的。Z88的首页为 <https://en.z88.de/> 。Z88OS也托管于GitHub上： <https://github.com/LSCAD/Z88OS> ，如有需要，您可以自行编译。


</div>

[Z88](https://en.z88.de) is another FEM program, containing a mesher, a solver and converters. It is used by the [FEM SolverZ88](FEM_SolverZ88.md) tool. FreeCAD requires the open source Z88OS package.


<div class="mw-translate-fuzzy">

### OpenFOAM

一种用来实现场运算与处理（Field Operation and Manipulation (FOAM)）的库，在计算流体力学（Computational Fluid Dynamics (CFD)）仿真中会用到它。正因如此，FreeCAD中的[有限元工作台便会用到OpenFOAM](FEM_Workbench.md)。您可以通过**Model → Fluid constraints**子菜单来访问它。此项目位于 <https://openfoam.org> 。


</div>

[OpenFOAM](https://openfoam.org) is a large collection of libraries for computational fluid dynamics (CFD) simulations. OpenFOAM is used by the [Cfd](Cfd_Workbench.md) and [CfdOF](https://github.com/jaheyns/CfdOF) [external workbenches](external_workbenches.md).


<div class="mw-translate-fuzzy">

## 相关页面

-   [第三方库](Third_Party_Libraries.md)


</div>

-   [Import Export](Import_Export.md)
-   [Import Export Preferences](Import_Export_Preferences.md)
-   [Third Party Libraries](Third_Party_Libraries.md)


<div class="mw-translate-fuzzy">





</div>



---
⏵ [documentation index](../README.md) > Installing additional components/zh-cn
