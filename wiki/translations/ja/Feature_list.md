# Feature list/ja
<div class="mw-translate-fuzzy">

以下はFreeCADに実装されている多くの機能のリストです。ただし機能が多いため全てが記載されているわけではありません。もし将来的な計画について知りたいのであれば[開発ロードマップを見てください](Development_roadmap.md)。機能を概観したいのであれば[スクリーンショットを見るとよいでしょう](Screenshots.md)。


</div>


{{TOCright}}



## リリースノート


<div class="mw-translate-fuzzy">

-   [リリース 0.11](Release_notes_0.11.md)
-   [Release 0.11](Release_notes_0.11.md) - March 2011
-   [Release 0.12](Release_notes_0.12.md) - December 2011
-   [Release 0.13](Release_notes_0.13.md) - January 2013
-   [Release 0.14](Release_notes_0.14.md) - March 2014
-   [Release 0.15](Release_notes_0.15.md) - March 2015
-   [Release 0.16](Release_notes_0.16.md) - April 2016
-   [Release 0.17](Release_notes_0.17.md) - April 2018


</div>



## 一般的な機能

### 基本アプリケーション

<img alt="" src=images/Freecad09-thumbnail.jpg  style="width:300px;">


<div class="mw-translate-fuzzy">

-   複雑な形状タイプに対して複雑な3D操作を可能にする完全な[Open CASCADE Technology](http://en.wikipedia.org/wiki/Open_CASCADE)ベースの *ジオメトリカーネル* ![](images/Feature1.jpg ) brep、nurbsカーブやサーフェス、幅広い幾何エンティティ、ブール演算やフィレット、STEPやIGESフォーマットの組み込みサポートなどの概念をネイティブにサポートしています
-   ![](images/Feature3.jpg ) A full **parametric model**. All FreeCAD objects are natively parametric, which means their shape can be based on [properties](Property.md) or even depend on other objects, all changes being recalculated on demand, and recorded by the undo/redo stack. New object types can be added easily, that can even be [fully programmed in Python](Scripted_objects.md)
-   ![](images/Feature4.jpg ) A **modular architecture** that allow plugins (workbenches) to add functionality to the core application. Those extensions can be as complex as whole new applications programmed in C++ or as simple as [Python scripts](Power_users_hub.md) or self-recorded [macros](macros.md). You have complete access from the **Python** built-in interpreter, macros or external scripts to almost any part of FreeCAD, being [geometry creation and transformation](Topological_data_scripting.md), the 2D or 3D representation of that geometry ([scenegraph](scenegraph.md)) or even the [FreeCAD interface](PySide.md) 
-   ![](images/Feature5.jpg ) Import/export to **standard formats** such as [STEP](http://en.wikipedia.org/wiki/ISO_10303), [IGES](http://en.wikipedia.org/wiki/IGES), [OBJ](http://en.wikipedia.org/wiki/Obj), [STL](http://en.wikipedia.org/wiki/STL_%28file_format%29), [DXF](http://en.wikipedia.org/wiki/Dxf), [SVG](http://en.wikipedia.org/wiki/Svg), [STL](http://en.wikipedia.org/wiki/STL_(file_format)), [DAE](http://en.wikipedia.org/wiki/COLLADA), [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) or [OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html), [NASTRAN](http://en.wikipedia.org/wiki/NASTRAN), [VRML](http://en.wikipedia.org/wiki/VRML) in addition to FreeCAD\'s native [Fcstd file format](Fcstd_file_format.md). The level of compatibility between FreeCAD and a given file format can vary, since it depends on the module that implements it.
-   ![](images/Feature7.jpg ) A [Sketcher](Sketcher_Workbench.md) with constraint-solver, allowing to sketch geometry-constrained 2D shapes. The sketcher currently allows you to build several types of constrained geometry, and use them as a base to build other objects throughout FreeCAD.
-   ![](images/Feature9.jpg ) A [Robot simulation](Robot_Workbench.md) workbench that allows to study robot movements. The robot workbench already has an extended graphical interface allowing GUI-only workflow.
-   ![](images/Feature8.jpg ) A comfortable new workbench for creating [traditional drawing sheets](TechDraw_Workbench.md) with options like detail view, cross sections, dimensioning and others, that permit to put 2D views of your 3D models on a sheet. This workbench then produces ready-to-export SVG or PDF sheets. There exist still the older [Drawing Workbench](Drawing_Workbench.md) with its sparse Gui-commands but a powerful Python functionality.
-   ![](images/Feature-raytracing.jpg ) A [Rendering](Raytracing_Workbench.md) workbench that can export 3D objects for rendering with external renderers. Currently only supports [povray](http://en.wikipedia.org/wiki/POV-Ray) and [LuxRender](http://en.wikipedia.org/wiki/LuxRender), but is expected to be extended to other renderers in the future.
-   ![](images/Feature-arch.jpg ) An [Architecture](Arch_Workbench.md) workbench that allows [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)-like workflow, with [IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes) compatibility.
-   ![](images/Feature-CAM.jpg ) [Path Workbench](Path_Workbench.md) dedicated to mechanical machining like milling (CAM), and is able to output, display and adjust [G code](http://en.wikipedia.org/wiki/G-code).
-   数式ベースのモデルを駆動したり、モデルからデータを取得するには、 ![](images/Feature_spreadsheet.png ) [Integrated Spreadsheetと](Spreadsheet_Workbench.md)[expression parser](Expressions.md) を使用します。


</div>




<div class="mw-translate-fuzzy">

### ドキュメント構造


</div>


<div class="mw-translate-fuzzy">

-   **FreeCADはマルチプラットフォームです**。WIndows、Linux、Mac OSXで完全に同じように動作します。


</div>


<div class="mw-translate-fuzzy">

-   **FreeCADは完全なGUIアプリケーションです**。FreeCADは完全なグラフィカルユーザーインターフェースを持っています。このグラフィカルユーザーインターフェースはよく知られる[Qt](http://www.qtsoftware.com/)フレームワークを基盤にしており、3Dビューワーは[Open Inventor](http://en.wikipedia.org/wiki/Open_Inventor)を元に作成されています。これによって高速な3Dシーン描画が可能になり、シーンのグラフィック表現の取り扱いが非常に容易になっています。


</div>


<div class="mw-translate-fuzzy">

-   **FreeCADはコマンドラインアプリケーションとしても動作します**。この場合にはメモリーの消費量を低くすることができます。コマンドラインモードでのFreeCADはインターフェイス無しで実行されますが、全てのジオメトリツールを使用することができます。これによって例えば他のアプリケーション用のデータを作成するためのサーバーとしてFreeCADを使用することが可能になります。


</div>


<div class="mw-translate-fuzzy">

-   **FreeCADは[Pythonモジュールとしてインポートすることができます](Embedding_FreeCAD/jp.md)**。pythonスクリプトを実行できる他のアプリケーション内部、あるいはpythonコンソールへインポート可能です。コンソールモードの場合と同様、FreeCADのインターフェイス部分を使用することはできませんが、全てのジオメトリツールを使用することができます。


</div>


<div class="mw-translate-fuzzy">

-   **ワークベンチというコンセプト**: FreeCADのインターフェイスではツールは[ワークベンチによってグループ分けされます](workbenches.md)。これによってある作業を行うために必要なツールだけを表示し、作業スペースを整頓された使いやすい状態に保ち、アプリケーションの読み込みを高速にすることができます。


</div>


<div class="mw-translate-fuzzy">

-   **組み込みの[スクリプトフレームワーク](Scripting/ja.md)**: FreeCADには[Python](http://www.python.org/)インタープリターが組み込まれています。またアプリケーション、インターフェイス、ジオメトリー、3Dビューワー上のジオメトリー表現のほとんど全てを網羅したAPIを兼ね備えています。インタープリターは1つのコマンドから複雑なスクリプトまで実行でき、実質的には全モジュールを完全にPythonでプログラムすることさえ可能です。


</div>


<div class="mw-translate-fuzzy">

-   **パラメーター連想ドキュメントオブジェクト**: FreeCADドキュメント上のオブジェクトは全てパラメーターによって定義することが可能です。このパラメーターは動的に変更することが可能でいつでも再計算を行えます。オブジェクトの間の関連付けを保持することも可能なので一つのオブジェクトを変更するとそれに依存したオブジェクトも変更されます。


</div>


<div class="mw-translate-fuzzy">

-   *\'パラメトリックプリミティブ作成\'*（ボックス、球、円柱など）


</div>


<div class="mw-translate-fuzzy">

-   **プリミティブの作成**（直方体、球、円筒など）、**オフセット** (trivial or after Jung/Shin/Choi)、**ブーリアン演算** (加算, 切断、交差)


</div>


<div class="mw-translate-fuzzy">

-   **[1](https://ja.wikipedia.org/wiki/Constructive_Solid_Geometry)**（和集合、差、交差）


</div>


<div class="mw-translate-fuzzy">

-   Graphical creation of **planar geometry** like lines, wires, rectangles, b-splines, circular or elliptic arcs in any plane of the 3D space


</div>


<div class="mw-translate-fuzzy">

-   Modeling with straight or revolution **extrusions**, **sections** and **fillets**.


</div>


<div class="mw-translate-fuzzy">

-   Topological components like **vertices, edges, wires** and **planes** (also via Python scripting).


</div>


<div class="mw-translate-fuzzy">

-   **Testing and repairing** tools for meshes: solid test, non-two-manifolds test, self-intersection test, hole filling and uniform orientation.


</div>


<div class="mw-translate-fuzzy">

-   **Annotations** like texts or dimensions


</div>


<div class="mw-translate-fuzzy">

**アンドゥ/リドゥフレームワーク**: アンドゥスタックにアスセスすることで全ての操作をアンドゥ/リドゥ可能です。一度に複数のステップをアンドゥすることができます。


</div>


<div class="mw-translate-fuzzy">

-   **トランザクションマネージメント**: アンドゥ/リドゥスタックは一つのアクションではなくドキュメントのトランザクションを保持します。これによって各ツールは何をアンドゥまたはリドゥするかを正確に定義することができます。


</div>


<div class="mw-translate-fuzzy">

-   **Built-in [scripting](Scripting.md) framework**: FreeCAD features a built-in [Python](http://www.python.org/) interpreter, and an API that covers almost any part of the application, the interface, the geometry and the representation of this geometry in the 3D viewer. The interpreter can run single commands up to complex scripts, in fact entire modules can even be programmed completely in Python.


</div>


<div class="mw-translate-fuzzy">

-   **組み込みのPythonコンソール**には構文ハイライト機能、自動補完機能、クラスブラウザーが備わっています。Pythonコマンドは直接FreeCADに発行され、結果は直ちに返されます。これによってスクリプト作成者は動的に機能をテストすることができ、モジュールの中身を調べてFreeCADの内部構造を簡単に学ぶことができます。


</div>


<div class="mw-translate-fuzzy">

-   **コンソール上でのユーザー操作のミラーリング**: ユーザーがFreeCADのインターフェイスを介して行った操作はPythonのコードによって実行できます。このPythonのコードはコンソール上に表示したり、マクロとして記録することができます。


</div>


<div class="mw-translate-fuzzy">

-   **完全なマクロ記録と編集**: ユーザーがインターフェイスを操作するとPythonコマンドが発行され、必要な場合はそれを記録、編集して後で再現するために保存することができます。


</div>


<div class="mw-translate-fuzzy">

-   **（ZIPベースの）複合ドキュメント保存フォーマット**: FreeCADドキュメントは.[fcstd拡張子で保存できます](File_Format_FCStd/ja.md)。これにはジオメトリー、スクリプト、サムネイルアイコンといったさまざまな種類の情報を保存することができます。


</div>


<div class="mw-translate-fuzzy">

**完全にカスタマイズ/スクリプト化可能なグラフィカルユーザーインターフェース**。 [Qt](http://www.qtsoftware.com)ベースのFreeCADのインターフェイスに対してはPythonインタープリターを介した完全なアクセスが可能です。FreeCAD自体がワークベンチに提供する単純な機能だけではなく、Qtフレームワーク全体にアクセスできます。これによってウィジットとツールバーに対して作成、追加、ドッキング、削除といった任意のGUI操作を行うことができます。


</div>


<div class="mw-translate-fuzzy">

-   **サムネイラー** (今のところLinuxシステムのみ): GnomeのNautilusを始めとしたほとんどのファイルマネージャーアプリケーションでFreeCAD ドキュメントのアイコン上にファイルの内容を表示します。


</div>


<div class="mw-translate-fuzzy">

-   **モジュール化されたMSIインストーラー**によってWindowsシステム上への柔軟なインストールが可能です。Ubuntuシステム用のパッケージも整備されています。


</div>

## Extra Workbenches 


<div class="mw-translate-fuzzy">

## Extra Workbenches 

Power users have created various custom [external workbenches](external_workbenches.md).


</div>


<div class="mw-translate-fuzzy">


{{docnav/ja|About FreeCAD/ja|Install on Windows/ja}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Feature list/ja
