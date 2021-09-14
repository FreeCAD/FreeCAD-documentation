# PySide/ja




{{TOCright}}


<div class="mw-translate-fuzzy">


<H2>

PySide


</H2>


</div>


<div class="mw-translate-fuzzy">

[PySide](http://en.wikipedia.org/wiki/PySide)はクロスプラットフォームのGUIツールキットQtのPythonバインディングです。 FreeCADはPython内部のすべてのGUI（Graphic User Interface）目的にPySideを使用します。 PySideは、以前にFreeCADによってGUIに使用されていたPyQtパッケージに代わるものです。 PySideはより許容されるライセンスを持っています。 違いの詳細については[PySideとPyQtの違い](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt)を参照してください。


</div>

When you install FreeCAD, you should get both Qt and PySide as part of the package. If you are [compiling](Compiling.md) yourself then you must verify that these two libraries are installed in order for FreeCAD to run correctly. Of course, PySide will only work if Qt is present.

In the past, FreeCAD used PyQt, another Qt binding for Python, but in 2013 ([1dc122dc9a](https://github.com/FreeCAD/FreeCAD/commit/1dc122dc9a)) the project migrated to PySide because it has a more permissible [license](licence.md).

For more information see:

-   [Wikipedia:PySide](http://en.wikipedia.org/wiki/PySide)
-   [Differences Between PySide and PyQt](http://qt-project.org/wiki/Differences_Between_PySide_and_PyQt)

![](images/PySideScreenSnapshot1.jpg ) ![](images/PySideScreenSnapshot2.jpg ) *Examples created with PySide. Left: a simple dialog. Right: a more complex dialog with graphs.*

## PySide in FreeCAD with Qt5 

FreeCAD was developed to be used with Python 2 and Qt4. As these two libraries became obsolete, FreeCAD transitioned to Python 3 and Qt5. In most cases this transition was done without needing to break backwards compatibility.

Normally, the `PySide` module provides support for Qt4, while `PySide2` provides support for Qt5. However, in FreeCAD there is no need to use `PySide2` directly, as a special `PySide` module is included to handle Qt5.

This `PySide` module is located in the `Ext/` directory of an installation of FreeCAD compiled for Qt5. 
```python
/usr/share/freecad/Ext/PySide
```

This module just imports the necessary classes from `PySide2`, and places them in the `PySide` namespace. This means that in most cases the same code can be used with both Qt4 and Qt5, as long as we use the single `PySide` module. 
```python
PySide2.QtCore -> PySide.QtCore
PySide2.QtGui -> PySide.QtGui
PySide2.QtSvg -> PySide.QtSvg
PySide2.QtUiTools -> PySide.QtUiTools
```

The only unusual aspect is that the `PySide2.QtWidgets` classes are placed in the `PySide.QtGui` namespace. 
```python
PySide2.QtWidgets.QCheckBox -> PySide.QtGui.QCheckBox
```

[top](#top.md)

## Examples of PySide use 


<div class="mw-translate-fuzzy">

-   [Beginner PySide Examples](PySide_Beginner_Examples.md) （ Hello World、お知らせ、テキストを入力、番号を入力
-   [Medium PySide Examples](PySide_Medium_Examples.md) （ウィンドウのサイズ変更、ウィジェットの非表示、ポップアップメニュー、マウスの位置、マウスイベント）
-   [Advanced PySide Examples](PySide_Advanced_Examples.md) (ウィジェットなど)


</div>


<div class="mw-translate-fuzzy">

彼らは主題を3つの部分に分け、PySide、PythonそしてFreeCAD内部への露出のレベルによって区別しました。最初のページには概要と背景資料があり、PySideとそのまとめ方について説明していますが、2ページ目と3ページ目は、ほとんどが異なるレベルのコード例です。


</div>


<div class="mw-translate-fuzzy">

その意図は、問題に取り組むユーザがコードを簡単にコピーして自分の作業に貼り付け、必要に応じてそれを修正し、FreeCADによる問題解決に戻ることができるように、関連ページがPySideを実行する単純なPythonコードを提供することです。うまくいけば、彼らはPySideの質問に対する答えを探すためにインターネットを越えて追いかけに行く必要はありません。同時にこのページは、Web上で利用可能なさまざまな包括的なPySideチュートリアルと参照サイトを置き換えることを意図していません。


</div>

[top](#top.md)

## Documentation

There are some differences in handling of widgets in Qt4 (PySide) and Qt5 (PySide2). The programmer should be aware of these incompatibilities, and should consult the official documentation if something doesn\'t seem to work as expected on a given platform. Nevertheless, Qt4 is considered obsolete, so most development should target Qt5 and Python 3.

The PySide documentation refers to the Python-style classes; however, since Qt is originally a C++ library, the same information should be available in the corresponding C++ reference.

-   [Qt Modules](https://doc.qt.io/qtforpython/modules.html) available from PySide2 (Qt5).
-   [All Qt classes by module](https://doc.qt.io/qt-5/modules-cpp.html) in Qt5 for C++.
-   [Qt Modules](https://deptinfo-ensip.univ-poitiers.fr/ENS/pyside-docs/index.html) available from PySide (Qt4).

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation](Category:Developer_Documentation.md) [Category:Python Code](Category:Python_Code.md)
