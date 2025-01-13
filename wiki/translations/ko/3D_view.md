# 3D view/ko
## 소개




FreeCAD의 **3D 보기**는 [interface에서](interface.md) 가장 중요한 창을 형성하는 Coin3D [scenegraph의](Scenegraph.md) 인스턴스입니다. Coin3D는 OpenInventor 2.1 장면 설명 표준을 구현하는 라이브러리입니다.

배경색, [마우스 탐색](Mouse_navigation/ko.md) 스타일 및 확대/축소 단계와 같은 보기의 특정 속성은 [기본 설정 편집기에서](Preferences_Editor/ko.md) 구성할 수 있습니다.

<img alt="" src=images/FreeCAD_3D_view.png  style="width:600px;">



*3D 보기는 FreeCAD [설계제도 작업대](interface]]의_구성_요소입니다.기본적으로 좌표축이 있는 작은 위젯과 좌표축이 있는 탐색 입방체가 표시됩니다; 그리드는 [[Draft Workbench/ko.md)를 로드하여 표시하고 구성할 수 있습니다.*

## Context menu 

The options in the context menu of the 3D view depend on the selected object(s) and the currently active workbench. To display this menu optionally select one or more objects and then right-click in the 3D view.

## Details

FreeCAD uses the Quarter library to use Coin3D in a Qt environment.

It is possible to interact directly with the 3D view scenegraph from the [Python console](Python_console.md) by using the Python library Pivy.

For more information see the power user documentation:

-   [Scenegraph](Scenegraph.md), description of Coin3D.
-   [Pivy](Pivy.md), usage of Coin3D from the Python console.
-   [Third party libraries](Third_Party_Libraries.md) used by FreeCAD.
-   [Coin3D](https://grey.colorado.edu/coin3d/index.html) C++ documentation.


{{Interface navi

}}



---
⏵ [documentation index](../README.md) > 3D view/ko
