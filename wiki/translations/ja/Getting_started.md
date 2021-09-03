





{{TOCright}}

## 序文


<div class="mw-translate-fuzzy">

FreeCADは、CAD/CAE用のパラメトリックモデリングアプリケーションです。まだ開発の初期段階なので、すぐに作品の製作に使用できると期待しないように。これは主に機械設計用に作られていますが、3Dオブジェクトを精度良くモデル化し、モデリング履歴を制御する必要がある他のすべての用途にも使用できます。


</div>


<div class="mw-translate-fuzzy">

でもFreeCADがどういったもので、またどういった機能が開発されているのか興味がある方は、是非ダウンロードして試してみてください。現時点では既にたくさんの機能が実装されています。しかしユーザーインターフェイスはまだ十分に開発されていません。したがって、もしあなたがPythonを少し知っていれば、比較的に簡単に複雑な形状の作成や修正にすぐに取りかかれますが、Pyhtonを知らなければ、FreeCADが提供する機能はまだほんの僅かであると感じるでしょう。でも待ってください、すぐに改善されますから。 評価後のアイデアや意見は、是非[FreeCADディスカッションフォーラム](http://forum.freecadweb.org/index.php)で私たちと共有しましょう！


</div>


<div class="mw-translate-fuzzy">

Like all open-source projects, the FreeCAD project is not a one-way work delivered to you by its developers. It depends much on its community to grow, gain features, and stabilize (get bugs fixed). So don\'t forget this when using FreeCAD; if you like it, you can directly influence and [help FreeCAD](help_FreeCAD.md)!


</div>

See also:

-   [Migrating to FreeCAD from Fusion360](Migrating_to_FreeCAD_from_Fusion360.md)
-   [Tutorials](Tutorials.md)
-   [Video tutorials](Video_tutorials.md)

## インストール


<div class="mw-translate-fuzzy">

まず初めに（まだ済んでいなければですが）FreeCADをダウンロードしてインストールしてください。[ダウンロードページで現在のバージョンと更新を確認しましょう](Download.md)。インストールパッケージはWindows用（.msi）とUbuntuとDebian用（.deb）、openSUSE（rpm）とMac OSX用を用意しています。 See the [インストール](Installing/jp.md) page for information about how to install FreeCAD.


</div>


<div class="mw-translate-fuzzy">

## FreeCADを試してみる


</div>

<img alt="" src=images/FreeCAD_interface_base_divisions.svg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD_interface.png  style="width:1024px;">

![最初に起動するFreeCADインターフェイスです。[他のスクリーンショットも参照してください](images/screenshots/jp.md)。](Freecad09-empty.jpg )


</div>


<div class="mw-translate-fuzzy">

1.  The 3D view, showing the contents of your document
2.  The tree view, which shows the hierarchy and construction history of all the objects in your document
3.  The [property editor](property_editor.md), which allows you to view and modify properties of the selected objects
4.  The report view (or output window), which is where FreeCAD prints messages, warnings and errors
5.  The Python console, where all the commands executed by FreeCAD are printed, and where you can enter python code
6.  The [workbench selector](Workbenches.md), where you select the active workbench


</div>


<div class="mw-translate-fuzzy">

FreeCADは汎用の3Dモデリングアプリケーションです。機械工学と、専門的なエンジニアリングや建築などの関連分野に重点を置いています。FreeCADは、限られた特定のタスクを実行するためだけではなく、あらゆる種類の3Dアプリケーションを開発するためのプラットフォームとして考えられています。このため、FreeCADのインターフェイスは一連の [ワークベンチに分けられています](Workbenches/jp.md)。ワークベンチでは特定のタスクやタスクグループに必要なツールのみを表示するようにインターフェイスの内容を変更することができます。


</div>


<div class="mw-translate-fuzzy">

つまりFreeCADのインターフェイスは、メニューバーや3Dビュー領域、及びシーンの内容やオブジェクトのプロパティを表示するための幾つかのサイドパネルを持つ、とてもシンプルな容れ物であると言えるでしょう。また、これらのパネルの全ての内容はワークベンチに応じて変更することができます。


</div>

<img alt="" src=images/Start_center_0.18_screenshot.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

<img alt="" src=images/Startcenter.jpg  style="width:1024px;"> For FreeCAD 0.17 see this [start center](Media:Startcenter0.17.jpg.md) screenshot.


</div>


<div class="mw-translate-fuzzy">

初めてFreeCAD起動すると\"一般的な\"ワークベンチ（我々は"完全なワークベンチ"と呼びますが）が表示されます。このワークベンチは、他のワークベンチから最も完成されたツールを集めたものです。FreeCADはかなり若くまだ専門的な作業には使用されていませんから、このワークベンチはFreeCADをより簡単に知るうえでとても役に立つでしょう。基本的には、ジオメトリを作成するために十分なツールは全てこのワークスペースにあります。


</div>

### 3次元空間での操作

FreeCADは2つの異なる[操作モードを持っており](Mouse_Model/jp.md)、ユーザー設定ダイアログまたは3Dビューでの右クリックで変更できます。これらのモードの詳細については[マウスモデルのページを見てください](Mouse_Model/jp.md)。 デフォルトのモード(\"CAD操作モード\")ではコマンドは以下の通りです。


<div class="mw-translate-fuzzy">

FreeCAD has several different [navigation modes](Mouse_Model.md) available, that change the way you use your mouse to interact with the objects in the 3D view and the view itself. One of them is specifically made for [touchpads](Mouse_Model#Touchpad_Navigation.md), where the middle mouse button is not used. The following table describes the default mode, called **CAD Navigation** (You can quickly change the current navigation mode by right-clicking on an empty area of the 3D view):


</div>


<div class="mw-translate-fuzzy">


{{CAD Navigation/jp}}


{{CAD Navigation
|Select_name=Select
|Pan_name=Pan
|Zoom_name=Zoom
|Rotate_view_name=Rotate view<br>First method
|Rotate_view_alt_name=Rotate view<br>Alternate method
|Ctrl=**Ctrl**
|Shift=**Shift**
|Select_text=Press the left mouse button over an object you want to select.

Holding down **Ctrl** allows the selection of multiple objects.
|Pan_text=Hold the middle mouse button, then move the pointer.
|Pan_mode_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Zoom_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor.
|Zoom_mode_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [[spinning]], if this is enabled.

A double click with the middle mouse button sets a new center of rotation.
|Rotate_view_mode_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small> 
|Rotate_view_alt_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method.
}}


</div>

Holding down **Ctrl** allows the selection of multiple objects. \|Pan\_text=Hold the middle mouse button, then move the pointer. \|Pan\_mode\_text=Pan mode: hold the **Ctrl** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small>  \|Zoom\_text=Use the mouse wheel to zoom in and out.

Clicking the middle mouse button re-centers the view on the location of the cursor. \|Zoom\_mode\_text=Zoom mode: hold the **Ctrl** and **Shift** keys, press the right mouse button once, then move the pointer. <small>(v0.17)</small>  \|Rotate\_view\_text=Hold the middle mouse button, then press and hold the left mouse button, then move the pointer.

The cursor location when the middle mouse button is pressed determines the center of rotation. Rotation works like spinning a ball which rotates around its center. If the buttons are released before you stop the mouse motion, the view continues [spinning](spinning.md), if this is enabled.

A double click with the middle mouse button sets a new center of rotation. \|Rotate\_view\_mode\_text=Rotate mode: hold the **Shift** key, press the right mouse button once, then move the pointer. <small>(v0.17)</small>  \|Rotate\_view\_alt\_text=Hold the middle mouse button, then press and hold the right mouse button, then move the pointer.

With this method the middle mouse button may be released after the right mouse button is held pressed.

Users who use the mouse with their right hand may find this method easier than the first method. }}

またViewメニュー、Viewツールバー、数値のショートカット（ **1** **2**など\...）からプリセットのビュー（トップビュー、フロントビューなど）が利用できます。

## First steps with FreeCAD {#first_steps_with_freecad}

FreeCAD\'s focus is to allow you to make high-precision 3D models, to keep tight control over those models (being able to go back into modelling history and change parameters), and eventually to build those models (via 3D printing, CNC machining or even construction worksite). It is therefore very different from some other 3D applications made for other purposes, such as animation film or gaming. Its learning curve can be steep, especially if this is your first contact with 3D modeling. If you are struck at some point, don\'t forget that the friendly community of users on the [FreeCAD forum](http://forum.freecadweb.org/index.php) might be able to get you out in no time.


<div class="mw-translate-fuzzy">

The workbench you will start using in FreeCAD depends on the type of job you need to do: If you are going to work on mechanical models, or more generally any small-scale objects, you\'ll probably want to try the [PartDesign Workbench](PartDesign_Workbench.md). If you will work in 2D, then switch to the [Draft Workbench](Draft_Workbench.md), or the [Sketcher Workbench](Sketcher_Workbench.md) if you need constraints. If you want to do BIM, launch the [Arch Workbench](Arch_Workbench.md). And if you come from the OpenSCAD world, try the [OpenSCAD Workbench](OpenSCAD_Workbench.md). There are also many community-developed [external workbenches](External_workbenches.md) available.


</div>


<div class="mw-translate-fuzzy">

You can switch workbenches at any time, and also [customize](Interface_Customization.md) your favorite workbench to add tools from other workbenches.


</div>

## Working with the PartDesign and Sketcher workbenches {#working_with_the_partdesign_and_sketcher_workbenches}

## ![](images/Workbench_Draft.png ) [2次元の製図](Draft_Module/jp.md) {#workbench_draft.png_2次元の製図}


{{Draft Tools/jp}}

## ![](images/Workbench_Part.png ) [3Dパーツの作成](Part_Module/jp.md) {#workbench_part.png_3dパーツの作成}


{{Part Tools/jp}}

## [2D図面へのエクスポート](Drawing_Module/jp.md)


{{Drawing Tools/jp}}

## [外部レンダラーへのエクスポート](Raytracing_Module/jp.md)


{{Raytracing Tools/jp}}

The [PartDesign Workbench](PartDesign_Workbench.md) is made to build complex objects, starting from simple shapes, and adding or removing pieces (called \"features\"), until you get to your final object. All the features you applied during the modelling process are stored in a separate view called the [tree view](Document_structure.md), which also contains the other objects in your document. You can think of a PartDesign object as a succession of operations, each one applied to the result of the preceding one, forming one big chain. In the tree view, you see your final object, but you can expand it and retrieve all preceding states, and change any of their parameter, which automatically updates the final object.

The PartDesign workbench makes heavy use of another workbench, the [Sketcher Workbench](Sketcher_Workbench.md). The sketcher allows you to draw 2D shapes, which are defined by applying Constraints to the 2D shape. For example, you might draw a rectangle and set the size of a side by applying a length constraint to one of the sides. That side then cannot be resized anymore (unless the constraint is changed).

Those 2D shapes made with the sketcher are used a lot in the PartDesign workbench, for example to create 3D volumes, or to draw areas on the faces of your object that will then be hollowed from its main volume. This is a typical PartDesign workflow:

1.  Create a new sketch
2.  Draw a closed shape (make sure all points are joined)
3.  Close the sketch
4.  Expand the sketch into a 3D solid by using the pad tool
5.  Select one face of the solid
6.  Create a second sketch (this time it will be drawn on the selected face)
7.  Draw a closed shape
8.  Close the sketch
9.  Create a pocket from the second sketch, on the first object

Which gives you an object like this:

<img alt="" src=images/Partdesign_example.jpg  style="width:1024px;">

At any moment, you can select the original sketches and modify them, or change the extrusion parameters of the pad or pocket operations, which will update the final object.

## Working with the Draft and Arch workbenches {#working_with_the_draft_and_arch_workbenches}

The [Draft Workbench](Draft_Workbench.md) and [Arch Workbench](Arch_Workbench.md) behave a bit differently than the other workbenches above, although they follow the same rules, which are common to all of FreeCAD. In short, while the Sketcher and PartDesign are made primarily to design single pieces, Draft and Arch are made to ease your work when working with several, simpler objects.

The [Draft Workbench](Draft_Workbench.md) offers you 2D tools somewhat similar to what you can find in traditional 2D CAD applications such as [AutoCAD](https://en.wikipedia.org/wiki/AutoCAD). However, 2D drafting being far away from the scope of FreeCAD, don\'t expect to find there the full array of tools that these dedicated applications offer. Most of the Draft tools work not only in a 2D plane but also in the full 3D space, and benefit from special helper systems such as [Work planes](Draft_SelectPlane.md) and [object snapping](Draft_Snap.md).

The [Arch Workbench](Arch_Workbench.md) adds [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling) tools to FreeCAD, allowing you to build architectural models with parametric objects. The Arch workbench relies extensively on other modules such as Draft and Sketcher. All the Draft tools are also present in the Arch workbench, and most Arch tools make use of the Draft helper systems.

A typical workflow with Arch and Draft workbenches might be:

1.  Draw a couple of lines with the Draft Line tool
2.  Select each line and press the Wall tool to build a wall on each of them
3.  Join the walls by selecting them and pressing the Arch Add tool
4.  Create a floor object, and move your walls in it from the Tree view
5.  Create a building object, and move your floor in it from the Tree view
6.  Create a window by clicking the Window tool, select a preset in its panel, then click on a face of a wall
7.  Add dimensions by first setting the working plane if necessary, then using the Draft Dimension tool

これはあなたにこれを与える：

<img alt="" src=images/Arch_workflow_example.jpg  style="width:1024px;">


<div class="mw-translate-fuzzy">

[Tutorialsページの詳細](Tutorials.md)。


</div>


<div class="mw-translate-fuzzy">

## [スクリプト](Scripting/jp.md)


</div>

Freecad, as an open source software, offers the possibility to supplement its workbenches with addons.

The [Addon](Addon.md) principle is based on the development of a workbench complement. Any user can develop a function that he or she deems to be missing for her/his own needs or, ultimately, for the community. With the forum, the user can request an opinion, help on the forum. It can share, or not, the object of its development according to copyright rules to define. Free to her/him. To develop, the user has available [scripting](scripting.md) functions.

There are two types of addons:

1.  [Macros](Macros.md): short snippets of Python code that provide a new tool or functionality. Macros usually start as a way to simplify or automate the task of drawing or editing a particular object. If many of these macros are collected inside a directory, the entire directory may be distributed as a new workbench.
2.  [External workbenches](External_workbenches.md): collections of tools programmed in Python or C++ that extend FreeCAD in an important way. If a workbench is sufficiently developed and is well documented, it may be included as one of the base workbenches in FreeCAD. Under [External workbenches](External_workbenches.md), you\'ll find the principle and a list of existing library.

## Scripting


<div class="mw-translate-fuzzy">

最後はFreeCADの最も強力な機能の一つ、[スクリプト環境です](scripting/jp.md) 。統合されたPythonコンソールから（あるいは他の外部のPythonスクリプトからでも）、FreeCADのほとんど全ての機能へアクセスできます。ジオメトリの作成や修正、3Dシーンでのオブジェクトの表示方法の変更、FreeCADインターフェースへのアクセスや変更が可能です。Pythonスクリプトはまた[マクロとしても使用され](macros/jp.md)、カスタムコマンドを簡単に作成することができます。


</div>


<div class="mw-translate-fuzzy">

## 新着情報﻿


</div>


<div class="mw-translate-fuzzy">

-   [Version 0.17 Release notes](Release_notes_0.17.md) : Check what\'s new in the 0.17 release of FreeCAD
-   [Version 0.16 Release notes](Release_notes_0.16.md) : Check what\'s new in the 0.16 release of FreeCAD
-   [Version 0.15 Release notes](Release_notes_0.15.md) : Check what\'s new in the 0.15 release of FreeCAD
-   [Version 0.14 Release notes](Release_notes_0.14.md) : Check what\'s new in the 0.14 release of FreeCAD
-   [Version 0.13 Release notes](Release_notes_013.md) : Check what\'s new in the 0.13 release of FreeCAD
-   [Version 0.12 Release notes](Release_notes_012.md) : Check what\'s new in the 0.12 release of FreeCAD
-   [バージョン0.12リリースノート](Release_notes_012/jp.md) ： FreeCAD リリース 0.12 の新着情報をチェックしてください。
-   [Version 0.11 Release notes](Release_notes_011.md) : Check what\'s new in the 0.11 release of FreeCAD


</div>


<div class="mw-translate-fuzzy">


{{docnav/jp|Install on Mac/jp|Mouse Model/jp}}


</div>




[Category:User\_Documentation/ja](Category:User_Documentation/ja.md)
