# Python scripting tutorial/ja
<div class="mw-translate-fuzzy">


{{docnav/ja
|[Introduction to Python](Introduction_to_Python/ja.md)
|[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/ja.md)}}


</div>


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Python](http://en.wikipedia.org/wiki/Python_%28programming_language%29)はプログラミング言語で使い方はとても簡単、すぐに修得することができます。オープンソースかつマルチプラットフォームで簡単なシェルスクリプトから非常に複雑なプログラムのプログラミングまでさまざま用途で使用できます。ですがもっとも広く使われている用途はスクリプト言語として使うというものです。これは他のアプリケーションに簡単に組み込むことができるためです。FreeCAD内部でもまさにその様にして使用されています。Pythonコンソール、または自作のスクリプトからFreeCADを操作したり、まだグラフィカルユーザーインターフェイスのツールがない非常に複雑な動作を行わせることもできます。


</div>


<div class="mw-translate-fuzzy">

例えばPythonスクリプトからは次の様な操作を行うことができます；

-   新しいオブジェクトの作成
-   既存のオブジェクトの変更
-   それらのオブジェクトの3D表示の変更
-   FreeCADのインターフェイスの変更


</div>


<div class="mw-translate-fuzzy">

FreeCADではPythonを使う複数の方法が存在します：

-   [FreeCAD Pythonインタープリター](FreeCAD_Scripting_Basics/jp.md)。\"コマンドライン\"スタイルのインターフェイスでシンプルなコマンドを実行することができます。
-   [マクロ](macros/jp.md)。存在しないツールをFreeCADインターフェイスに手軽に追加するのには便利な方法です。
-   外部スクリプト。より複雑なプログラムに使用できます。例えば[ワークベンチ全体といったものです](Workbenches/jp.md)。


</div>


<div class="mw-translate-fuzzy">

このチュートリアルでは入門的なサンプルスクリプトをいくつか作成しますが、このWikiにはこれ以外にもたくさんの利用可能な[Pythonスクリプトについてのドキュメントがあります](Power_users_hub/jp.md)。もしPythonを使うのが初めてでその機能を知りたいのであれば基礎的な[Pyton入門もあります](introduction_to_Python/jp.md)。


</div>

Before proceeding with Python scripting, go to **Edit → Preferences → General → Output window** and check two boxes:

-    **Redirect internal Python output to report view**.

-    **Redirect internal Python errors to report view**.

Then go to **View → Panels** and check:

-    **Report view**.


<div class="mw-translate-fuzzy">

## Pythonのコードを書く

FreeCADでPythonのコードを書く場合には二つの手軽な方法があります：Pythonコンソール（View -\> Views -\> Python consoleメニューから利用可能）、またはマクロエディター（Tools -\> Macros）です。コンソールの場合Pythonコマンドを一つ一つ書いていき、コマンドはリターンキーを押したタイミングで実行されます。一方、マクロでは複数行からできたより複雑なスクリプトを保存できます。このスクリプトはマクロが実行されたタイミングでだけ実行されます。


</div>

There are two ways to write Python code in FreeCAD. In the [Python console](Python_console.md) (select **View → Panels → Python console** from the menu) or in the [Macro editor](Std_DlgMacroExecute.md) (select **Macro → Macros...** from the menu). In the console you write Python commands one by one, executing them by pressing **Enter**, while macros can contain more complex code made up of several lines, executed only when the macro is executed.

![](images/Screenshot_pythoninterpreter.jpg )


<div class="mw-translate-fuzzy">

![The FreeCAD python console](images/Screenshot_pythoninterpreter.jpg )


</div>


<div class="mw-translate-fuzzy">

このチュートリアルでは両方の方法を使うことができます。各行を一行ずつPythonコンソールにコピー/ペーストして各行ごとに**Return**キーを押すか、コード全体を新しいマクロウィンドウにコピー/ペーストしてください。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## FreeCADの調査

さてまずは新しい空のドキュメントを作成しましょう：


</div>

Let\'s start by creating a new empty document:


```python
doc = FreeCAD.newDocument()
```


<div class="mw-translate-fuzzy">

このコマンドをPythonコンソールに入力すると\"FreeCAD.\"と入力した直後に行の残りをすばやく自動補完できるようにウィンドウがポップアップします。さらには自動補完リストの各エントリーにはそれが何を行うものかの説明のツールチップさえ備わっているのです。これを使えば利用可能な関数を簡単に調べることができます。\"newDocument\"を選択する前に他の利用可能なオプションも見ておいてください。


</div>

![](images/Screenshot_classbrowser.jpg )


<div class="mw-translate-fuzzy">

![The autocomplete mechanism of the FreeCAD python console](images/Screenshot_classbrowser.jpg )


</div>


<div class="mw-translate-fuzzy">

さて新しいドキュメントが作成されました。これはツールバーの\"新しいドキュメント\"ボタンを押した場合と同じです。実際はFreeCADのボタンのほとんどは一、二行のPythonコードを実行しているだけに過ぎません。Edit -\> Preferences -\> General -\> Macroにある\"show script commands in python console\"オプションを設定するとよくわかります。こうするとボタンを押した時に実行されるPythonコードが全てコンソールに表示されます。Pythonで操作を再現する方法を学ぶのにとても便利です。


</div>


<div class="mw-translate-fuzzy">

さあ、ドキュメントに戻りましょう。ドキュメントを使って何ができるのかを確認してみましょう。


</div>


```python
doc.
```


<div class="mw-translate-fuzzy">

利用可能なオプションを調べてください。通常、大文字から始まる名前は値が保持されている属性で、小文字から始まる名前は\"処理を行うための\"関数（メソッドとも呼ばれます）です。アンダースコアで始まる名前は通常はモジュールの内部動作のためのもので、気にする必要はありません。それではドキュメントに新しいオブジェクトを追加するためのメソッドの一つを使って見ましょう。


</div>


```python
box = doc.addObject("Part::Box", "myBox")
```


<div class="mw-translate-fuzzy">

何も起きません。なぜでしょう？これはFreeCADが大きな展望に立って作られているからです。いつの日かそれぞれ独立した数百もの複雑なオブジェクトをFreeCADで操作できる時が来るでしょう。どこかを少し変更するだけで大きな影響が現れ、ドキュメント全体を再計算しなければならなくなるかもしれません。それには長い時間がかかることでしょう・・・こういった事情からほとんどのコマンドではシーンが自動的に更新されることはありません。手動で更新を行う必要があるのです：


</div>


```python
doc.recompute()
```


<div class="mw-translate-fuzzy">

見えましたか？作成したボックスが表示されました！FreeCADのオブジェクト追加ボタンの多くは実のところ2つの処理を行います。オブジェクトの追加と再計算です。もし上で説明した\"show script commands in python console\"オプションを有効にしていれば今度はGUIのボタンで球を追加してみてください。二行のPythonコードが順番に実行されるのが見て取れるでしょう。


</div>

さて、作成したボックスの中身を調べてみましょう：


```python
box.
```

すぐにとても興味をそそられるものがいくつか見つかるでしょう。例えばこれです：


```python
box.Height
```

これを使うとボックスの現在の高さを表示できます。変更してみましょう：


```python
box.Height = 5
```


<div class="mw-translate-fuzzy">

マウスでボックスを選択するとプロパティパネルの\"Data\"タブに\"Height\"プロパティが表示されているのがわかるでしょう。ここ（と後で説明する\"View\"タブ）に表示されるFreeCADオブジェクトのプロパティは全てPythonによって直接アクセスすることができます。アクセスは先ほど\"Height\"プロパティでやったように名前で行います。ボックスの別の寸法も変更してみてください。


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## ベクトルと配置

[ベクトル](http://en.wikipedia.org/wiki/Euclidean_vector)は3Dアプリケーションにおいて非常に基礎的な概念です。ベクトルとは3つの数字（x、y、z）のリストで、3D空間ないでの点や位置を表します。ベクトルを使うと加算、減算、投影や[その他](http://en.wikipedia.org/wiki/Vector_space)にも色々なことを行うことができます。FreeCADでは次のようにしてベクトルを使用します：


</div>

[Vectors](https://en.wikipedia.org/wiki/Euclidean_vector) are a very fundamental concept in any 3D application. A vector is a list of 3 numbers (x, y and z), describing a point or position in 3D space. Many things can be done with vectors, such as additions, subtractions, projections and [much more](https://en.wikipedia.org/wiki/Vector_space). In FreeCAD vectors work like this:


```python
myvec = FreeCAD.Vector(2, 0, 0)
myvec.x
myvec.y
othervec = FreeCAD.Vector(0, 3, 0)
sumvec = myvec.add(othervec)
```


<div class="mw-translate-fuzzy">

FreeCADオブジェクトに共通する機能の一つが[配置です](Placement/jp.md)。各オブジェクトはPlacement属性を持ち、そこにはオブジェクトの位置（Base）と方向（Rotation）が保持されています。操作は簡単です。一例として私たちのオブジェクトを動かしてみましょう。


</div>


```python
box.Placement
box.Placement.Base
box.Placement.Base = sumvec
 
otherpla = FreeCAD.Placement()
box.Placement = otherpla
```

さて、さらに進む前にいくつかの重要な概念を理解しておく必要があります。 {{Top}}


<div class="mw-translate-fuzzy">

## AppとGui

FreeCADは最初、ユーザーインターフェイス無しのコマンドラインアプリケーションとして動作するように作成されていました。その結果、ほとんど全ての物が\"幾何\"コンポーネントと\"表示\"コンポーネントに分割されています。コマンドラインモードで動作させている際には幾何部分は存在しますが表示部分は無効化されるています。こうした理由からFreeCADのほとんどのオブジェクトは二つの部分、つまりObjectとViewObjectから構成されています。


</div>

FreeCAD has been designed so that it can also be used without its user interface, as a command-line application. Almost every object in FreeCAD therefore consists of two parts: an `Object`, its \"geometry\" component, and a `ViewObject`, its \"visual\" component. When you work in command-line mode, the geometry part is present, but the visual part is disabled.


<div class="mw-translate-fuzzy">

このコンセプトの説明のために私たちの立方体を見てください。寸法や位置など立方体の幾何プロパティはObjectの中に保持されています。一方、色や線の太さなどの表示プロパティはViewObjecの中に保持されています。そしてそれがプロパティウィンドウの\"Data\"タブと\"View\"タブに対応しているのです。オブジェクトのViewObjecには次のようにしてアクセスすることができます：


</div>


```python
vo = box.ViewObject
```


<div class="mw-translate-fuzzy">

これで\"View\"タブのプロパティを変更することもできるようになりました：


</div>


```python
vo.Transparency = 80
vo.hide()
vo.show()
```


<div class="mw-translate-fuzzy">

FreeCADが起動するとすぐにPythonコンソールは2つの基本モジュールをロードします。FreeCADとFreeCADGuiです（これらにも短縮名のAppとGuiによってアクセスることが可能です）。この二つにはドキュメントとそのオブジェクトを操作するための一般的な機能が保持されています。このコンセプトの説明のためにFreeCADとFreeCADGuiの両方にActiveDocument属性があることを確認してください。これが現在、開かれているドキュメントです。FreeCAD.ActiveDocumentとFreeCADGui.ActiveDocumentは同じオブジェクトではありません。FreeCADドキュメントを￥の二つのコンポーネントであり、異なる属性とメソッドが保持されています。例えばFreeCADGui.ActiveDocument にはActiveViewがありますが、これは現在開かれている3Dビューです。


</div>


{{Top}}

## Modules

The true power of FreeCAD lies in its faithful modules, with their respective workbenches. The FreeCAD base application is more or less an empty container. Without its modules it can do little more than create new, empty documents. Each module not only adds new workbenches to the interface, but also new Python commands and new object types. As a result several different, and even totally incompatible, object types can coexist in the same document. The most important modules in FreeCAD that we\'ll look at in this tutorial are: [Part](Part_Workbench.md), [Mesh](Mesh_Workbench.md), [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md).


<div class="mw-translate-fuzzy">

[Sketcherと](Sketcher_Workbench/ja.md)[Draftは両方とも形状の作成と制御に](Draft_Workbench/ja.md)[Partモジュールを使用しています](Part_Workbench/ja.md)。これらで扱われる形状はBRepですが一方の[Meshは完全に独立し](Mesh_Workbench/ja.md)、独自のオブジェクトを制御します。詳細については下記にあります。


</div>

現在のドキュメントでの利用可能な基底オブジェクト型は次のようにしてチェックすることができます：


```python
doc.supportedTypes()
```


<div class="mw-translate-fuzzy">

さまざまなFreeCADモジュールはFreeCADに独自のオブジェクト型を追加しますがpythonコンソールでは自動的に読み込まれません。これは起動が遅くなることを防ぐためです。モジュールはそれが必要になった時にのみ読み込まれます。例えばPartモジュールの内部を調べたい時は以下のようにします：


</div>


```python
import Part
Part.
```

しかし今はここまでにしておいてPartモジュールについては後で詳しく説明します。 {{Top}}


<div class="mw-translate-fuzzy">

## Mesh


</div>


<div class="mw-translate-fuzzy">

[メッシュ](http://en.wikipedia.org/wiki/Polygon_mesh)は非常に単純な3Dオブジェクトで例えば[Sketchup](http://en.wikipedia.org/wiki/SketchUp)、[Blender](http://en.wikipedia.org/wiki/Blender_%28software%29)、[3D studio Max](http://en.wikipedia.org/wiki/Autodesk_3ds_Max)で使用されています。メッシュは3つの要素でできています。点（頂点とも呼ばれます）、線（エッジとも呼ばれます）、そして面です。FreeCADを含む多くのアプリケーションでは面は点を三つだけ持つことができます。しかし、もちろん同一平面上にある複数の三角形からなるもっと大きな平面を作ることができます


</div>


<div class="mw-translate-fuzzy">

メッシュは非常に単純なのでそれが短所になることもありますが上にあげたような多くのアプリケーションではむしろ利点になります。単純ゆえに一つのドキュメントの中に数百万ものメッシュを持つことが容易にできるからです。しかしFreeCAD内部ではあまり使われず、ほとんどの場合は他のアプリケーションから出力されたメッシュ形式（.stl、.obj）のオブジェクトをインポートする用途に使われます。またFreeCADが誕生した初めの一ヶ月間はメインテストモジュールとして広く使われました。


</div>


<div class="mw-translate-fuzzy">

MeshオブジェクトとFreeCADオブジェクトは別物です。FreeCADオブジェクトをMeshオブジェクトの入れ物と考えるといいでしょう（後で見るようにPartオブジェクトについても同じことが言えます）。FreeCADにメッシュオブジェクトを追加するためにはまず最初にFreeCADオブジェクトとMeshオブジェクトを作成しなければなりません。それが終わったらFreeCADオブジェクトにMeshオブジェクトを追加します：


</div>


```python
import Mesh
mymesh = Mesh.createSphere()
mymesh.Facets
mymesh.Points
 
meshobj = doc.addObject("Mesh::Feature", "MyMesh")
meshobj.Mesh = mymesh
doc.recompute()
```


<div class="mw-translate-fuzzy">

標準的な例です。createSphere()メソッドを使って自動で球を作成していますが、もちろん頂点と面を定義してゼロから自作のメッシュを作成することもできます。


</div>

[Read more about mesh scripting\...](Mesh_Scripting.md) [メッシュのスクリプト処理についてもっと読む・・・](Mesh_Scripting/jp.md) {{Top}}


<div class="mw-translate-fuzzy">

## Part

FreeCAD全体で最も強力なモジュールが[パートモジュールです](Part_Module/jp.md)。これを使うと[BRep](http://en.wikipedia.org/wiki/Boundary_representation)オブジェクトを作成し、操作することができます。メッシュと異なりこのオブジェクトには幅広いコンポーネントが用意されています。すこし説明しておくとBrepとは境界表現（Boundary Representation）を意味します。つまりこのオブジェクトは内部体積を定義する閉じた表面によって定義されるのです。これらの表面は平面から非常に複雑なNURBS面までさまざまに変化します。またこれに体積の概念はこれらの表面に基づきます。


</div>

The [Part](Part_Workbench.md) module is the most powerful module in the whole of FreeCAD. It allows you to create and manipulate [BRep](https://en.wikipedia.org/wiki/Boundary_representation) objects. BREP stands for \"Boundary Representation\". A BREP object is defined by surfaces that enclose and define an inner volume. Unlike meshes, BREP objects can have a wide variety of components from planar faces to very complex NURBS surfaces.


<div class="mw-translate-fuzzy">

Partモジュールは強力な機能を持つ[OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE_Technology)ライブラリをその基盤としています。このライブラリはブーリアン演算、フィレット処理、ロフト処理などの幅広い複雑な操作を簡単にそのオブジェクトに対して行うための機能を提供しています。


</div>

Partモジュールの使い方はMeshモジュールと同じです。FreeCADオブジェクトとPartオブジェクトを作成し、PartオブジェクトをFreeCADオブジェクトに追加します：


```python
import Part
myshape = Part.makeSphere(10)
myshape.Volume
myshape.Area

shapeobj = doc.addObject("Part::Feature", "MyShape")
shapeobj.Shape = myshape
doc.recompute()
```


<div class="mw-translate-fuzzy">

（Meshモジュールと同様に）Partモジュールにも自動でFreeCADオブジェクトを作成して形状を追加するためのシュートカットが存在します。それを使えば上のコードの最後の3行を省略することができます：


</div>


```python
Part.show(myshape)
```


<div class="mw-translate-fuzzy">

Part.show(myshape)

myshapeの中身を調べるとFaces、Edges、Vertexes、Solids、Shellsといったたくさんの興味をそそられる利用可能サブコンポーネントや切り取り（減算）、共通集合（交差）、フューズ（結合）といった幅広い形状操作があることに気がつくでしょう。[幾何データスクリプト処理のページではこれら全てについて詳細に説明を行なっています](Topological_data_scripting/jp.md)。

[パートのスクリプト処理についてもっと読む・・・](Topological_data_scripting/jp.md)


</div>


<div class="mw-translate-fuzzy">

[Read more about part scripting\...](Topological_data_scripting.md)


</div>


{{Top}}


<div class="mw-translate-fuzzy">

## Draft

FreeCADには[Sketcherや](Sketcher_Workbench/ja.md)[Draftといったさらに多くのモジュールが備わっています](Draft_Workbench/ja.md)。これらのモジュールはPartオブジェクトを作成するだけでなくそれにパラメーターを追加していたり、そのPartの形状を制御するための全く新しい手段を持っていることさえあります。上のボックスのサンプルはちょうどパラメトリックオブジェクトの良い例になっています。ボックスを定義するために必要なことは高さや幅といったいくつかのパラメーターを指定することだけです。パラメーターに基いてオブジェクトはPart形状を自動で計算します。FreeCADでは[Pythonを使ってこういったオブジェクトを作成する手段が用意されています](Scripted_objects.md)。


</div>

FreeCAD features many more modules, such as [Sketcher](Sketcher_Workbench.md) and [Draft](Draft_Workbench.md), that also create Part objects. These modules add additional parameters to the objects created, or even implement a whole new way to handle the Part geometry in them. Our box example above is a perfect example of a parametric object. All you need to define the box is to specify the parameters height, width and length. Based on those, the object will automatically calculate its Part shape. FreeCAD allows you to [create such objects in Python](Scripted_objects.md).


<div class="mw-translate-fuzzy">

[Draftモジュールではlines](Draft_Workbench/ja.md)、circlesといったいくつかの2Dパラメトリックオブジェクト型が追加されており（全Partオブジェクトも含まれています）、またDraft製オブジェクトだけでなく、全てのPartオブジェクトに対して使用可能なジェネリック関数もいくつか用意されています。何が利用可能か調べるためには次の様にするだけです：


</div>


```python
import Draft
rec = Draft.makeRectangle(5, 2)
mvec = FreeCAD.Vector(4, 4, 0)
Draft.move(rec, mvec)
Draft.move(box, mvec)
```


{{Top}}


<div class="mw-translate-fuzzy">

## Interface

FreeCADのユーザーインターフェイスは[Qt](http://en.wikipedia.org/wiki/Qt_%28framework%29)によって作られています。Qtは強力なグラフィカルインターフェイスシステムであり、3Dビューの周りに配置されたメニュー、ツールバー、ボタンといった全てのコントロールの描画と制御を行なっています。QtにはPyQtと呼ばれるモジュールが用意されています。これを使うとPythonでFreeCADで採用されているようなQtインターフェイスへアクセスしたり変更を加えることができます。Qtインターフェイスをいじって簡単なダイアログを作成してみることにしましょう：


</div>

The FreeCAD user interface is made with [Qt](https://en.wikipedia.org/wiki/Qt_(software)), a powerful graphical interface system, responsible for drawing and handling all the controls, menus, toolbars and buttons around the [3D view](3D_view.md). Qt provides a module, [PySide](PySide.md), which allows Python to access and modify Qt interfaces such as FreeCAD\'s. Let\'s try to fiddle with the Qt interface and produce a simple dialog:


```python
from PySide import QtGui
QtGui.QMessageBox.information(None, "Apollo program", "Houston, we have a problem")
```


<div class="mw-translate-fuzzy">

ツールバーにFreeCADのアイコンがあるダイアログが表示されます。つまりQtはこの命令がFreeCADアプリケーション内部から発行されたものであることをわかっているのです。従って私たちはFreeCADのインターフェイスのどの部分でも簡単に直接操作することが可能なのです。


</div>


<div class="mw-translate-fuzzy">

Qtは非常に強力なインターフェイスシステムで非常に複雑なことも可能です。またそれだけでなくQt Designerのように簡単に使えるツールもいくつか提供されています。Qt Designerを使えばグラフィカルにダイアログをデザインすることができ、数行のPythonコードを書くだけでそれをFreeCADのインターフェイスに追加することができます。


</div>

[Read more about PySide here\...](PySide.md) [pyqtについてもっと読む・・・](PyQt/ja.md) {{Top}}


<div class="mw-translate-fuzzy">

## マクロ

さて基本的なことについて十分理解できたかと思います。それではPythonスクリプトの保存はどこでできるのでしょうか？またどうやればFreeCADから簡単にそれを起動できるのでしょうか？そのための簡単な仕組みがあり、[マクロと呼ばれています](Macros.md)。マクロはたんなるPythonスクリプトで、ツールバーに追加してマクスクリックするだけで起動することが可能です。FreeCADには簡単なテキストエディター（Macro -\> Macros -\> Create）が用意されており、それを使ってスクリプトを書いたり、ペーストすることができます。それができたらTools -\> Customize -\> Macrosを使ってスクリプトに対してボタンを設定してツールバーに追加することができます。


</div>

Now that you have a good understanding of the basics, where are we going to keep our Python scripts, and how are we going to launch them inside FreeCAD? There is an easy mechanism for that, called [Macros](Macros.md). A macro is a Python script that can be added to a toolbar and launched via a mouse click. FreeCAD provides you with a simple text editor (**Macro → Macros... → Create**) where you can write or paste scripts. Once the script is done, use **Tools → Customize... → Macros** to define a button for it that can be added to toolbars.


<div class="mw-translate-fuzzy">

これでFreeCADのスクリプト処理についてもっと詳細に知る準備ができました。[パワーユーザーハブへ進んでください](Power_users_hub/jp.md)！


</div>


{{Top}}


<div class="mw-translate-fuzzy">


{{docnav/ja
|[Introduction to Python](Introduction_to_Python/ja.md)
|[FreeCAD Scripting Basics](FreeCAD_Scripting_Basics/ja.md)}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > Python scripting tutorial/ja
