\_\_NOTOC\_\_ 


<div class="mw-translate-fuzzy">

## はじめに

これは[FreeCAD](http://www.freecadweb.org)のドキュメントwikiです。マニュアルを参照するには、ユーザーハブを探索する方法と、マニュアルを参照する方法の2つの方法があります。 FreeCADのユーザーと開発者のコ​​ミュニティによって作成された作業です。情報が間違っているか見つからない場合は、[help FreeCAD](help_FreeCAD.md)！

# FreeCAD


<div class="main-menu">


{{Languages-top| {{en|Main Page}} {{cn|Main Page/cn}} {{de|Main Page/de}} {{es|Main Page/es}} {{fr|Main Page/fr}} {{it|Main Page/it}} {{pl|Main Page/pl}} {{ru|Main Page/ru}}  {{tr|Main Page/tr}} }}

パラメトリック3D-CADモデラー


</div>


<div class="main-toolbox">


{{screenshot|Rim_bling.png|a screenshot showing version 0.12}}

Loading latest commits\...


{{mantisbox}}


{{booksbox}}

Loading facebook widget\...


</div>


<div class="main-content">

**FreeCAD**は[CAD](http://en.wikipedia.org/wiki/CAD)、MCAD、[CAx](http://en.wikipedia.org/wiki/CAx)、[CAE](http://en.wikipedia.org/wiki/Computer-aided_engineering)、[PLM](http://en.wikipedia.org/wiki/Product_Lifecycle_Management)などのための汎用の[フィーチャーベース・パラメトリック3Dモデラー](http://en.wikipedia.org/wiki/Parametric_feature_based_modeler)で、[機械工学](http://en.wikipedia.org/wiki/Mechanical_engineering)や[製品設計](http://en.wikipedia.org/wiki/Product_design)だけでなく、建築やそれ以外のエンジニアリング専門分野などエンジニアリングの幅広い分野での利用に向いています。100%の[オープンソース](http://en.wikipedia.org/wiki/Open_source)であり、高度にモジュール化されているため非常に高度な拡張、カスタマイズが可能です。

FreeCADは強力なジオメトリーカーネルである[OpenCasCade](http://en.wikipedia.org/wiki/Open_CASCADE)をその基盤とし、[Coin3D](http://en.wikipedia.org/wiki/Coin3D)ライブラリによる[OpenInventor](http://en.wikipedia.org/wiki/Open_Inventor)に準拠した3Dシーン表現モデルと幅広い[Python](http://en.wikipedia.org/wiki/Python_(programming_language)) APIをその特徴としています。インターフェイスは[Qt](http://en.wikipedia.org/wiki/Qt_(framework))によって作成されています。FreeCADはWindows、Mac OSX、Linuxのプラットフォーム上で完全に同じ様に動作します。

![](images/Right_arrow.png ) [詳細はこちらから\...](About_FreeCAD/jp.md)

## 主な特徴

-   ![](images/Feature1.jpg )

完全な[OpenCASCADE-Technology](http://en.wikipedia.org/wiki/Open_CASCADE)ベースの**ジオメトリーカーネル**によって複雑な形状に対して複雑な3D操作が可能です。またBREP、NURBS、ブーリアン演算、フィレットといった概念をネィティブでサポートしています。

-   ![](images/Feature6.jpg ) **モジュールアーキテクチャ**によってコアアプリケーションに機能追加するためのプラグイン（モジュール）を使用することが可能です。全く新しいアプリケーションと同じくらい複雑なものから、[Pythonスクリプトや自己記録](Scripting/jp.md)[マクロと同じくらいシンプルなものまでさまざまな拡張機能を作成できます](macros/jp.md)。
-   ![](images/Feature3.jpg ) 完全な**パラメトリックモデル**によって任意のパラメトリック駆動カスタムオブジェクト型を使用可能です。これらのオブジェクト型を[Pythonで完全にプログラムすることも可能です](Scripted_objects/jp.md)。
-   ![](images/Feature4.jpg ) **Python**の組み込みインタープリタ、マクロ、外部スクリプトからFreeCADのほとんどの部分に完全にアクセス可能です。[ジオメトリーの作成と変換](Topological_data_scripting/jp.md)、ジオメトリーの2D・3D表現（[シーングラフ](scenegraph/jp.md)）、[FreeCADのインターフェイスにさえアクセスすることが可能です](PyQt/jp.md)。
-   ![](images/Feature5.jpg ) FreeCADネイティブの[Fcstdファイルフォーマットに加え](Fcstd_file_format/jp.md)、[STEP](http://en.wikipedia.org/wiki/ISO_10303)、[IGES](http://en.wikipedia.org/wiki/IGES)、[OBJ](http://en.wikipedia.org/wiki/Obj)、[DXF](http://en.wikipedia.org/wiki/Dxf)、[SVG](http://en.wikipedia.org/wiki/Svg)、[STL](http://en.wikipedia.org/wiki/STL_(file_format))、[DAE](http://en.wikipedia.org/wiki/COLLADA)、[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)、[OFF](http://people.sc.fsu.edu/~jburkardt/data/off/off.html)といった**標準的なフォーマット**のインポート/エクスポートが可能です。
-   ![](images/Feature7.jpg ) 拘束ソルバーを持った[スケッチャーによってジオメトリー拘束された](Sketcher_Workbench/jp.md)2D形状のスケッチが可能です。現在、スケッチャーでは複数の拘束ジオメトリー型を作成し、それらをFreeCADで他のオブジェクトを作成する際の土台として使うことができます。
-   ![](images/Feature9.jpg ) ロボットの動作を研究するための[ロボットシミュレーションモジュールを使用可能です](Robot_Workbench/jp.md)。ロボットモジュールには既にGUIだけでのワークフローを可能にする拡張グラフィカルインターフェイスが備わっています。

## 開発中

-   ![](images/Feature8.jpg ) 3Dモデルの2Dビューをシート上に配置することを可能にする[ドローイングシートモジュール](Drawing_Workbench/jp.md)。さらにこのモジュールはエクスポート用のSVG、PDFシートを作成します。このモジュールはまだ未完成ですが既に強力なPythonの機能を提供しています。
-   ![](images/Feature-raytracing.jpg ) 外部レンダラを使ったレンダリング用の3Dモジュールエクスポートを可能にする[レンダリングモジュール](Raytracing_Workbench.md)。現在サポートされているのは[POV-Ray](http://en.wikipedia.org/wiki/POV-Ray)だけですが将来的には他のレンダラにも拡張される予定です。
-   ![](images/Feature-arch.jpg ) [BIM](http://en.wikipedia.org/wiki/Building_Information_Modeling)ライクなワークフローを可能にする[IFC](http://en.wikipedia.org/wiki/Industry_Foundation_Classes)と互換性のある[建築モジュール](Arch_Module/jp.md)。Archモジュールの作成については[このコミュニティ](http://forum.freecadweb.org/viewtopic.php?f=10&t=821)によって激しい議論が行われています。
-   ![](images/Feature-assembly.jpg ) 複数の形状、複数ドキュメント、複数ファイル、複数の関連物での作業を可能にする[アセンブリモジュール](Assembly_project/jp.md)。

## マニュアル

FreeCADマニュアルはFreeCADの使用についての最先端のドキュメントを提供するためにコミュニティの努力のもと常に作業が行われており、既に複数の言語で利用可能です。まだマニュアルには多くの情報が欠けています。遠慮せずに参加と[貢献を行ってください](Help_FreeCAD/jp.md)！

+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| -   ![](images/Flag-en.jpg ) [Table of contents](Online_Help_Toc.md)       | -   ![](images/Flag-fr.jpg ) [Table des matières](Online_Help_Toc/fr.md)   | -   ![](images/Flag-pt.jpg ) [Tabela de conteúdos](Online_Help_Toc/pt.md) |
| -   ![](images/Flag-cn.jpg ) [目录](Online_Help_Toc/cn.md)                 | -   ![](images/Flag-it.jpg ) [Indice dei contenuti](Online_Help_Toc/it.md) | -   ![](images/Flag-ru.jpg ) [Содержание](Online_Help_Toc/ru.md)          |
| -   ![](images/Flag-de.jpg ) [Inhaltsverzeichnis](Online_Help_Toc/de.md)   | -   ![](images/Flag-jp.jpg ) [目次](Online_Help_Toc/jp.md)                 | -   ![](images/Flag-tr.jpg ) [İçindekiler](Online_Help_Toc/tr.md)         |
| -   ![](images/Flag-es.jpg ) [Índice de contenidos](Online_Help_Toc/es.md) | -   ![](images/Flag-pl.jpg ) [Spis Treści](Online_Help_Toc/pl.md)          |                                                                                             |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+

## 参加しよう

### 参加方法

もしあなたが私たちを手助けすることに興味があるなら、FreeCADプロジェクトにはやらなければならないことがたくさんあります。C++、Pythonプログラマのためのプログラミング作業もありますが、もしコーディングできなくてもやれることはたくさんあります。ドキュメントの執筆、初心者の手助け、アプリケーションとドキュメントの翻訳、あなたの好みのオペレーティングシステム用の最新のFreeCADリリースのパッケージング、あるいはたんにあなたの周りにいる人たちがFreeCADを見つける手助けをしてくれるだけでもかまいません。[FreeCADを援助するというページにもっと詳しい説明があります](help_FreeCAD/jp.md)。

### ソースコード

FreeCADはcMakeまたはautotoolsを使ってコンパイルすることができます。Gitのリンクはgit://free-cad.git.sourceforge.net/gitroot/free-cad/free-cadで、[Windows](CompileOnWindows/jp.md)、[Unix/Linux](CompileOnUnix/jp.md)、[MacOSXでのビルド手順も用意されています](CompileOnMac/jp.md)。

### 開発について

何が計画されているかについては[開発ロードマップをチェックしてください](Development_roadmap.md)。次のリリースに向けた作業の進捗についてはMantisのページである[変更履歴](http://www.freecadweb.org/tracker/changelog_page.php)と[ロードマップ](http://www.freecadweb.org/tracker/roadmap_page.php)を、またFreeCADのコードベースについてのさらに詳しい情報については[プロジェクトの統計](http://www.ohloh.net/p/freecad)を見てください。開発に関わるコミュニケーションは全て[フォーラム](http://forum.freecadweb.org/)で行われているので、もし参加したいのであれば必ず訪れてください。

### どこでもFreeCADをフォローしよう！

<img alt="" src=images/Twitter.png ) ![](images/Facebook.png ) ![](images/Youtube.png ) ![](images/Googleplus.png  style="width:24px;">


</div>

\_\_NOTOC\_\_

This is the documentation wiki of [FreeCAD](http://www.freecadweb.org). The information contained here is what forms the offline documentation shipped with FreeCAD itself. You have two main ways to browse through the documentation: by exploring user hubs, or by following the manual. It is a work in progress, written by the community of users and developers of FreeCAD. If you find information that is wrong or missing, please [help](Help_FreeCAD.md)!


</div>


<div class="mw-translate-fuzzy">

## ユーザーハブ


</div>


<div class="mw-translate-fuzzy">

<img alt="Crystal_Clear_app_display.png" src=images/Crystal_Clear_app_display.png  style="width:64px;"> [Users hub](User_hub.md): このページには、FreeCADユーザ全員に便利なドキュメントが含まれています：すべてのワークベンチの一覧、FreeCADアプリケーションのインストール方法と使用方法、チュートリアル、および必要なものについての詳細な説明が含まれています。





<img alt="" src=images/Crystal_Clear_app_terminal.png  style="width:64px;"> [Power users hub](Power_users_hub.md): このページには、上級ユーザーやPythonスクリプトの作成に興味のある人のためのドキュメントが集められています。また、マクロのリポジトリ、それらをインストールして使用する方法、およびあなたの特定のニーズに合わせてFreeCADをカスタマイズする方法の詳細もご覧いただけます。 
 <img alt="" src=images/Crystal_Clear_app_tutorials.png  style="width:64px;"> [Developers hub](Developer_hub.md): このセクションでは、FreeCADを自分でコンパイルする方法、FreeCADのソースコードがどのように構造化されているか、どのようにナビゲートするか、新しいワークベンチを開発する方法、FreeCADを独自のアプリケーションに埋め込む方法について説明します。 



</div>

## マニュアル 


<div class="mw-translate-fuzzy">

<img alt="" src=images/Crystal_Clear_manual.png  style="width:64px;"> [The FreeCAD manual](Manual:Introduction.md) は、このwikiに含まれる情報を表現するもう一つのより線形な方法です。 それは本のように読まれるように作られ、上のハブから他の多くのページにあなたを穏やかに紹介します。 [ebook versions](https://www.gitbook.com/book/yorikvanhavre/a-freecad-manual/details) も利用できます。また、[a couple of translations in pdf format](https://www.freecadweb.org/manual/) 
 FreeCADマニュアルはFreeCADの使用についての最先端のドキュメントを提供するためにコミュニティの努力のもと常に作業が行われており、既に複数の言語で利用可能です。まだマニュアルには多くの情報が欠けています。遠慮せずに参加と[貢献を行ってください](Help_FreeCAD/jp.md)！

+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+
| -   ![](images/Flag-en.jpg ) [Table of contents](Online_Help_Toc.md)       | -   ![](images/Flag-fr.jpg ) [Table des matières](Online_Help_Toc/fr.md)   | -   ![](images/Flag-pt.jpg ) [Tabela de conteúdos](Online_Help_Toc/pt.md) |
| -   ![](images/Flag-cn.jpg ) [目录](Online_Help_Toc/cn.md)                 | -   ![](images/Flag-it.jpg ) [Indice dei contenuti](Online_Help_Toc/it.md) | -   ![](images/Flag-ru.jpg ) [Содержание](Online_Help_Toc/ru.md)          |
| -   ![](images/Flag-de.jpg ) [Inhaltsverzeichnis](Online_Help_Toc/de.md)   | -   ![](images/Flag-jp.jpg ) [目次](Online_Help_Toc/jp.md)                 | -   ![](images/Flag-tr.jpg ) [İçindekiler](Online_Help_Toc/tr.md)         |
| -   ![](images/Flag-es.jpg ) [Índice de contenidos](Online_Help_Toc/es.md) | -   ![](images/Flag-pl.jpg ) [Spis Treści](Online_Help_Toc/pl.md)          |                                                                                             |
+----------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------+


</div>

## 目次

次の表は、FreeCADアプリケーションに同梱されているオフラインドキュメントのバックボーンを構成するこのwikiのすべての記事を示しています。 すでにいくつかの言語で利用可能です：

+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
| -   ![](images/Flag-en.jpg ) [Table of contents](Online_Help_Toc.md)       | -   ![](images/Flag-fr.jpg ) [Table des matières](Online_Help_Toc/fr.md) | -   ![](images/Flag-pt.jpg ) [Tabela de conteúdos](Online_Help_Toc/pt.md) pt |
| -   ![](images/Flag-bg.jpg ) [Съдържание](Online_Help_Toc/bg.md)           | -   ![](images/Flag-hr.jpg ) [Sadržaj](Online_Help_Toc/hr.md)            | -   ![](images/Flag-pt-br.jpg ) [Índice](Online_Help_Toc/pt-br.md) pt-br  |
| -   ![](images/Flag-cn.jpg‎ ) [目錄](Online_Help_Toc/zh.md) zh            | -   ![](images/Flag-id.jpg ) [Daftar isi](Online_Help_Toc/id.md)         | -   ![](images/Flag-ro.jpg ) [Cuprins](Online_Help_Toc/ro.md)                |
| -   ![](images/Flag-cn.jpg ) [目录](Online_Help_Toc/zh-cn.md) zh-cn        | -   ![](images/Flag-it.jpg ) [Sommario](Online_Help_Toc/it.md)           | -   ![](images/Flag-ru.jpg ) [Содержание](Online_Help_Toc/ru.md)             |
| -   ![](images/Flag-cn.jpg‎ ) [目錄](Online_Help_Toc/zh-tw.md) zh-tw      | -   ![](images/Flag-jp.jpg ) [目次](Online_Help_Toc/ja.md) ja            | -   ![](images/Flag-sv.jpg ) [Innehallsforteckning](Online_Help_Toc/sv.md)   |
| -   ![](images/Flag-cs.jpg ) [Obsah](Online_Help_Toc/cs.md)                | -   ![](images/Flag-ko.jpg ) [온라인 도움말](Online_Help_Toc/ko.md)      | -   ![](images/Flag-tr.jpg ) [İçindekiler](Online_Help_Toc/tr.md)            |
| -   ![](images/Flag-de.jpg ) [Inhaltsverzeichnis](Online_Help_Toc/de.md)   | -   ![](images/Flag-pl.jpg ) [Spis Treści](Online_Help_Toc/pl.md)        | -   ![](images/Flag-uk.jpg ) [Інтернет Допомога](Online_Help_Toc/uk.md)      |
| -   ![](images/Flag-es.jpg ) [Índice de contenidos](Online_Help_Toc/es.md) |                                                                                            |                                                                                                |
+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

## 参加しよう 

### 参加方法 


<div class="mw-translate-fuzzy">

もしあなたが私たちを手助けすることに興味があるなら、FreeCADプロジェクトにはやらなければならないことがたくさんあります。C++、Pythonプログラマのためのプログラミング作業もありますが、もしコーディングできなくてもやれることはたくさんあります。ドキュメントの執筆、初心者の手助け、アプリケーションとドキュメントの翻訳、あなたの好みのオペレーティングシステム用の最新のFreeCADリリースのパッケージング、あるいはたんにあなたの周りにいる人たちがFreeCADを見つける手助けをしてくれるだけでもかまいません。[FreeCADを援助するというページにもっと詳しい説明があります](help_FreeCAD/jp.md)。


</div>


<div class="mw-translate-fuzzy">

[help FreeCAD](help_FreeCAD.md) ページにすべての詳細が記載されています。 FreeCADは2016年から[Google Summer of Code](Google_Summer_of_Code.md) にも参加しています。 [Contributors hubページは](Contributors_hub.md)、FreeCADプロジェクトを支援し、貢献するための可能な方法を収集するためのもう一つの取り組みです。


</div>

### ソースコード 


<div class="mw-translate-fuzzy">

FreeCADはcMakeまたはautotoolsを使ってコンパイルすることができます。Gitのリンクはgit://free-cad.git.sourceforge.net/gitroot/free-cad/free-cadで、[Windows](CompileOnWindows/jp.md)、[Unix/Linux](CompileOnUnix/jp.md)、[MacOSXでのビルド手順も用意されています](CompileOnMac/jp.md)。


</div>

### 開発について 


<div class="mw-translate-fuzzy">

何が計画されているかについては[開発ロードマップをチェックしてください](Development_roadmap.md)。次のリリースに向けた作業の進捗についてはMantisのページである[変更履歴](http://www.freecadweb.org/tracker/changelog_page.php)と[ロードマップ](http://www.freecadweb.org/tracker/roadmap_page.php)を、またFreeCADのコードベースについてのさらに詳しい情報については[プロジェクトの統計](http://www.ohloh.net/p/freecad)を見てください。開発に関わるコミュニケーションは全て[フォーラム](http://forum.freecadweb.org/)で行われているので、もし参加したいのであれば必ず訪れてください。


</div>




[Category:Documentation{{\#translation:}}](Category:Documentation.md)
