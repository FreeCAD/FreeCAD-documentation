# Third Party Libraries/ja
{{TOCright}}


<div class="mw-translate-fuzzy">

### 概要

これらはFreeCADプロジェクト内で変更されていないライブラリです。それらは基本的にはダイナミックリンクライブラリ（\*.so または \*.dll）としてそのまま使用されています。必要な変更またはラッパークラスが必要なときには、存在する場合、ラッパーのコードまたは変更したライブラリのコードはFreeCADの基本パッケージに移動する必要があります。 使用するライブラリは:


</div>

The dependencies need to be installed in the system before proceeding with compilation; see [compile on Linux](Compile_on_Linux.md), [compile on Windows](Compile_on_Windows.md), and [compile on MacOS](Compile_on_MacOS.md) for more information.


<div class="mw-translate-fuzzy">

[LibPackを使用する代わりに](#LibPack.md)、自分ですべてのものをダウンロードおよびインストールすることを検討してください。


</div>




<div class="mw-translate-fuzzy">

### リンク


</div>


<div class="mw-translate-fuzzy">

  ライブラリ名   必要なバージョン   取得するためのリンク
    
  Python         \>= 2.5.x          <http://www.python.org/>
  OpenCasCade    \>= 5.2            <http://www.opencascade.org>
  Qt             \>= 4.1.x          <http://www.qtsoftware.com>
  Coin3D         \>= 2.x            <http://www.coin3d.org>
  ODE            \>= 0.10.x         <http://www.ode.org>
  SoQt           \>= 1.2            <http://www.coin3d.org>
  Xerces-C++     \>= 2.7.x \< 3.0   <http://xml.apache.org/xerces-c/>
  GTS            \>= 0.7.x          <http://gts.sourceforge.net/>
  Zlib           \>= 1.x.x          <http://www.zlib.net/>
  Boost          \>= 1.33.x         <http://www.boost.org/>
  Eigen3         \>= 3.0.1          <http://eigen.tuxfamily.org/index.php?title=Main_Page>

  : リンク表


</div>




<div class="mw-translate-fuzzy">

### 詳細


</div>


<div class="mw-translate-fuzzy">

#### Python

**バージョン:** 2.5 以上


</div>


<div class="mw-translate-fuzzy">

**ライセンス:** Python 2.5 ライセンス


</div>


**Python 2 became obsolete in 2019. Further development of FreeCAD will use exclusively Python 3; compatibility with Python 2 won't be tested, so old workbenches and macros that use this version will have to be updated or they may stop working. Please post on the [https://forum.freecadweb.org/ FreeCAD forum] if you encounter problems with Python 3.**

Python is a popular all-purpose scripting language that is widely used in Linux and open source software. In FreeCAD, Python is used during compilation and also at runtime in different ways. It is used

-   to write test scripts to test for different conditions, such as memory leaks, to ensure functionality of the software after changes, for post build checks, and test coverage tests,
-   to write [macros](macros.md) and macro recording,
-   to implement application logic for standard packages,
-   to implement auxiliary tools such as the [Addon Manager](Std_AddonMgr.md),
-   to implement entire workbenches like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md),
-   to dynamically load packages,
-   to implement rules for design (knowledge engineering),
-   to do fancy Internet interactions like work groups and PDM


<div class="mw-translate-fuzzy">

Pythonについては、http://www.python.org/ のソースコードまたはバイナリを利用する、もしくはhttp://www.activestate.com/ のActiveState Pythonを利用することができますが、ActiveStateからデバッグライブラリを取得するのは少し難しいです。


</div>

Python was chosen as the scripting language for FreeCAD for different reasons:

-   It is more object oriented than Perl and Tcl.
-   The code is more readable than Perl and Visual Basic.
-   It is easier to embed in another application, unlike, say, Java.

In summary, Python is well documented, and it\'s easy to embed and extend in a C++ application. It is also well tested and has strong support from the open source community. Read more about Python and browse the official documentation at [Python.org](http://www.python.org).




<div class="mw-translate-fuzzy">

#### Boost


</div>


<div class="mw-translate-fuzzy">

**バージョン:** 1.33.x


</div>

**ライセンス:** Boost Software License - Version 1.0


<div class="mw-translate-fuzzy">

Boost C++ライブラリは、同業者の評論の対象になるような、C++の機能を拡張したオープンソースのライブラリの機能の集まりです。ライブラリは、Boostがオープンとクローズ両方のソースのプロジェクトで使用できるように、Boost Software Licenseの下でライセンスされています。Boostの創設者の多くは、C + +の標準化委員会の上にいて、いくつかのBoostライブラリは、C++0xの技術研究報告1に組み込むために受理されています。


</div>

Due to their popularity and stability, many Boost libraries have been accepted for incorporation into the C++11 standard, and more are planned for inclusion in subsequent C++ standards.


<div class="mw-translate-fuzzy">

効率性と柔軟性を確保するために、Boostはテンプレートを多用します。 BoostはC++言語でのジェネリックプログラミングやメタプログラミングに広範な仕事や研究の源となっています。


</div>




<div class="mw-translate-fuzzy">

#### OpenCasCade


</div>


<div class="mw-translate-fuzzy">

**バージョン:** 5.2 以上


</div>


<div class="mw-translate-fuzzy">

**ライセンス:** 6.7.0以降は、追加の例外を除いて、GNU劣等一般公衆利用許諾契約書（LGPL）バージョン2.1によって管理されています。 [https://www.opencascade.com/content/licensing以前のバージョンでは、わずかに異なるライセンスが使用されていました。https://www.opencascade.com/content/occt-public-license](https://www.opencascade.com/content/licensing以前のバージョンでは、わずかに異なるライセンスが使用されていました。https://www.opencascade.com/content/occt-public-license)


</div>


<div class="mw-translate-fuzzy">

OCCは、フル機能を備えたCADカーネルです。もともと、それはフランスの Matia Datavision氏がStrim（スタイラー）とユークリッド量子アプリケーション用に開発し、後にオープンソース化されました。それは本当に巨大なライブラリで、オープンソースプロジェクトでは実装が困難、もしくは不可能と思われるいくつかのパッケージを提供されたことで、フリーのCADアプリケーションを可能にした初めてのライブラリです。:

-   完全STEP準拠のジオメトリカーネル
-   トポロジデータモデルと、それらを操作ために必要なすべての機能（切り取り、結合、押し出し、などなど\...）
-   STEP、IGES、VRML等の標準インポート/エクスポートプロセッサ
-   選択をサポートしている3Dと2Dのビューア
-   ドキュメントの外部リンクの保存と復元、設計履歴（パラメトリックモデリング）の再計算をサポートしたドキュメントやプロジェクトデータ構造と、拡張パッケージとして動的に新しいデータ型をロードする機能


</div>

OCCT is a big and complex set of C++ libraries that provide functionality required by a CAD application:

-   A complete STEP compliant geometry kernel.
-   A topological data model and needed functions to work with shapes (cut, fuse, extrude, and many others).
-   Standard import and export processors for files like STEP, IGES, VRML.
-   A 2D and 3D viewer with selection support.
-   A document and project data structure with support for save and restore, external linking of documents, recalculation of design history (parametric modeling) and a facility to load new data types as an extension package dynamically.

There are two main versions of OpenCASCADE in existence in different Linux distributions. One is distributed by the original developers; it is known as OCCT, and is packaged under the names `occ` or `occt`. The other version is the \"community edition\", abbreviated OCE, and is normally found with the `oce` name. FreeCAD can compile against either version, however, since 2016 FreeCAD recommends compiling against the official OCCT libraries rather than the OCE ones. The reason is that the community edition lacks important bug fixes and functions that make using FreeCAD better.


<div class="mw-translate-fuzzy">

OpenCasCadeの詳細は、OpenCasCadeページまたはhttp://www.opencascade.orgを見てください。


</div>




<div class="mw-translate-fuzzy">

#### Qt


</div>


<div class="mw-translate-fuzzy">

**バージョン:** 4.1.x 以上


</div>


<div class="mw-translate-fuzzy">

**ライセンス:** GPL v2.0/v3.0 もしくは 商用 (バージョン 4.5からはLGPL v2.1)


</div>


<div class="mw-translate-fuzzy">

Qtのについて多くのことを伝える必要がないと思います。それは、オープンソースプロジェクトの中で最も頻繁に使用されるGUIツールキットの一つです。Qtを使用する最も重要な理由は、Qt Designerと全体のダイアログボックスを（XML）リソースとしてロードし、特殊なウィジェットを組み込む実現性です。CAXのアプリケーションでは、ユーザーとの対話やダイアログボックスがコードの大部分を占めていて、新しい機能を持つFreeCADを簡単に拡張するために、優れたダイアログデザイナーがとても重要です。さらに詳しい情報や、とても良いオンラインドキュメントは、http://www.qtsoftware.comで見つけることができます。


</div>

Further information about Qt libraries and their programming documentation are available at [Qt Documentation](https://doc.qt.io/?hsCtaTracking=f641fd1a-772b-4957-964b-dad954b8d702%7C46c97dac-f1f6-49b3-ae46-8070fc35ea13).

#### Shiboken2 and Pyside2 

Shiboken is the Python binding generator that Qt for Python uses to create the PySide module, in other words, it is the system that is used to expose the Qt C++ API to the Python language.

The original Shiboken and PySide packages were meant to be used with Python 2 and Qt4; since these two versions are considered obsolete in 2019, please use Shiboken2 and PySide2, which work with Python 3 and Qt5. New development of FreeCAD is done with Python 3 and Qt5, so compatibility with Python 2 and Qt4 is not guaranteed after FreeCAD 0.18.

Read more about Shiboken and Pyside on [Qt for Python](https://wiki.qt.io/Qt_for_Python/Shiboken).




<div class="mw-translate-fuzzy">

#### Coin3D


</div>


<div class="mw-translate-fuzzy">

**バージョン:** 2.0 以上


</div>


<div class="mw-translate-fuzzy">

**ライセンス:** GPL v2.0 もしくは商用


</div>


<div class="mw-translate-fuzzy">

Coinは、C + +アプリケーションプログラミングインターフェースを備えた高レベル3Dグラフィックスライブラリです。Coinは、科学的·工学的な視覚化アプリケーションのほとんどすべての種類に適したリアルタイムグラフィックスをレンダリングするためにシーングラフデータ構造を使用しています。


</div>


<div class="mw-translate-fuzzy">

Coinは業界標準の瞬時レンダリングライブラリOpenGL上に構築されており、高い水準のプリミティブの抽象化が追加されており、3Dインタラクティビティを提供し、プログラマの利便性と生産性を向上し、アプリケーションプログラマに対して手間がかかっている多くの高速描画用の最適化機能をわかりやすく提供しています。


</div>


<div class="mw-translate-fuzzy">

CoinはSGI Open InventorのAPIに基づいています。それに精通していない人にとって、Open Inventorは科学的·工学的コミュニティにおける3Dビジュアライゼーションとビジュアルシミュレーションソフトウェアのデファクトスタンダードのグラフィックスライブラリになって久しいです。Coinは世界中の大規模なエンジニアリングアプリケーションの数千の主要なビルディングブロックとして貢献していることから、その成熟度は10年以上の期間にわたって価値が証明されました。


</div>


<div class="mw-translate-fuzzy">

OpenCasCadeビューア（AISおよびGraphics3D）には、特に大規模なエンジニアリングレンダリングでは限界があり、パフォーマンスのボトルネックがあるため、FreeCADではOpenInventorを3Dビューアとして使用します。 テクスチャやボリュームレンダリングのような他のものは、実際にはサポートされていません。


</div>


<div class="mw-translate-fuzzy">

Coinは、さまざまなプラットフォーム：任意のUNIX / Linux/ \* BSDのプラットフォーム、すべてのMicrosoft Windowsオペレーティングシステム、およびMac OS Xに移植可能です


</div>




<div class="mw-translate-fuzzy">

#### SoQt


</div>

**バージョン:** 1.2.0 以上


<div class="mw-translate-fuzzy">

**ライセンス:** GPL v2.0 または 商用


</div>


<div class="mw-translate-fuzzy">

SoQtはQt GUIツールキットを繋ぐ発明です。残念ながら、それはLGPLではないので、私たちはFreeCADの基本コードから取り外し、ライブラリとしてリンクする必要があります。それはCoinのような同様のライセンスモデルを採用しています。そして、あなたは、Qtのバージョンを使用してコンパイルする必要があります。


</div>

SoQt is no longer used in FreeCAD, it was replaced by Quarter which is a more recent Qt binding.

#### Quarter

**Version:** 1.0 or higher

**License:** BSD 3-clause license

Quarter is a newer Coin3D binding to the Qt toolkit. A version of it is included in the source code of FreeCAD so it is compiled together with it.

#### Pivy

**Version:** 0.6.3 or higher

**License:** BSD 3-clause license

[Pivy](Pivy.md) is a library that wraps the Coin3d library for use in [Python](Python.md). It is not needed to build FreeCAD or to start it, but it is needed as a runtime dependency by the [Draft Workbench](Draft_Workbench.md), and by other workbenches that use it internally, like [Arch](Arch_Workbench.md) and [BIM](BIM_Workbench.md).

If you are not going to use these workbenches, you won\'t need Pivy.

### Ply

**Version:** 3.11 or higher

**License:** BSD 3-clause license

Ply is the Python-Lex-Yacc parser. It is used as a runtime dependency by the [OpenSCAD Workbench](OpenSCAD_Workbench.md). If you don\'t use this workbench, you may not need this package.

For more information see [Ply homepage](https://www.dabeaz.com/ply/)




<div class="mw-translate-fuzzy">

#### Xerces-C++ 


</div>


<div class="mw-translate-fuzzy">

**バージョン:** 2.7.0 以上


</div>

**ライセンス** Apache Software License Version 2.0


<div class="mw-translate-fuzzy">

Xerces-C++は、C++の移植可能なサブセットとして書かれた検証用XMLパーサです。Xerces-C++を使うと、あなたのアプリケーションにXMLの読み書き機能を追加することが簡単になります。共有ライブラリは、XML文書を解析、生成、操作、検証するために提供されています。


</div>


<div class="mw-translate-fuzzy">

パーサはFreeCADの中のパラメータを保存および復元するために使用されます。


</div>

### Eigen3

**Version:** 3.0 or higher

**License:** Starting from the 3.1.1 version, it is licensed under the [Mozilla Public License 2.0](http://www.mozilla.org/MPL/2.0). Earlier versions were licensed under the [GNU Lesser General Public License 3](https://www.gnu.org/licenses/lgpl-3.0.en.html).

Eigen is a C++ template library for linear algebra: matrices, vectors, numerical solvers, and related algorithms.

If you just want to use Eigen, you can use the header files right away. There is no binary library to link to, and no configured header file. Eigen is a pure template library defined in the headers.

Eigen is used in FreeCAD for many vector operations in 3D space. To learn more, visit [Eigen homepage](http://eigen.tuxfamily.org/index.php?title=Main_Page).

### Zipios++

**Version:** 0.1.5 or higher

**License:** GNU Lesser General Public License 2.1

Zipios++ is a C++ library for reading and writing `.zip` files. Access to individual entries is provided through standard C++ iostreams. A simple read-only virtual file system that mounts regular directories and `.zip` files is also provided. The structure and public interface of Zipios++ are loosely based on the `java.util.zip` package of Java.

FreeCAD\'s native file format `.FCstd` is in reality a `.zip` file that stores and compresses other types of data within it, such as BREP and XML files. Therefore, Zipios++ is used to save and open compressed archives, including FreeCAD files.

A copy of Zipios++ is included in the source code of FreeCAD so it is compiled together with it. If you want to use an external Zipios++ library, provided by your operating system, you may set -DFREECAD_USE_EXTERNAL_ZIPIOS=ON with `cmake`.

Zipios++ uses the Zlib library to perform the actual decompression of files.


<div class="mw-translate-fuzzy">

#### Zlib


</div>


<div class="mw-translate-fuzzy">

**バージョン:** 1.x.x


</div>


<div class="mw-translate-fuzzy">

**ライセンス:** zlib License


</div>


<div class="mw-translate-fuzzy">

zlibは自由で、汎用で、合法的に邪魔されない\--これは、どの特許も侵害していない\-- 実質的にどんなハードウェアやOSでも利用できるロスレスのデータ圧縮ライブラリです。 zlibのデータフォーマットはプラットフォーム間で互換性があります。　Unixのcompress(1)やGIFイメージフォーマット等のLZW圧縮法とは異なり、zlibで使用されている圧縮方法は、基本的にデータを膨らますことはありません。(LZWはひどい場合は２倍や３倍のファイルサイズになります。zlibのメモリ使用量は、入力データとは独立しており、圧縮時に必要に応じて減らすことができます。


</div>

A copy of this library is included in the source code of FreeCAD so it is compiled together with it.

### libarea

**Version:** 0.0.20140514-1 or higher

**License:** BSD 3-clause license

Libarea is a software library to compute profile and pocket operations which are used in computer aided manufacturing (CAM) software. It was created by Dan Heeks for his HeeksCNC project.

A copy of the library is included with the source code of the [Path Workbench](Path_Workbench.md), so it is compiled together with it.


<div class="mw-translate-fuzzy">

### LibPack

LibPackは上記のすべてのライブラリを一緒に梱包した便利なパッケージです。現在、Windowsプラットフォームでは[ダウンロードページから利用可能です](Download.md)！あなたがLinuxで作業していれば、LibPackを必要としません。代わりにお使いのLinuxディストリビューションのパッケージリポジトリを利用するべきです。


</div>

If you\'re working under Linux, you don\'t need the LibPack, as you can get the dependencies from your distribution\'s repositories as mentioned in the [compile on Linux](Compile_on_Linux.md) page.

### FreeCAD 12.1.2 

See the announcement in the forum: [New libpacks for Windows with Qt5.12, OCC7.3 and Python 3.6 by apeltauer](https://forum.freecadweb.org/viewtopic.php?f=4&t=35789)

It includes among other things: Boost 1.67, Coin3D 4.0.0a, Eigen3, Open CASCADE Technology 7.3.0, Python 3.6.8, PySide2, Qt 5.12.1, Salome SMESH, Shiboken2, vtk7, Xerces-C, Zipios++, zlib 1.2.11


<div class="mw-translate-fuzzy">


{{docnav|Compiling (Speeding up)|Third Party Tools}}


</div>



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Third Party Libraries/ja
