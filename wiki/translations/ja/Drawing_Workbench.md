# Drawing Workbench/ja
**Development of the [[Drawing Workbench]] stopped in FreeCAD 0.16, and the new [[TechDraw Workbench]] aiming to replace it was introduced in v0.17. Both workbenches are still provided in v0.17, but the Drawing Workbench may be removed in future releases.**

<img alt="Drawing workbench icon" src=images/Workbench_Drawing.svg  style="width:128px;">

## Introduction

ドローイングモジュールを使うと3D作業物を紙の上に移すことができます。つまりモデルのビューを2Dウィンドウに表示し、図面にそのウィンドウを挿入するということです。例えば枠線、タイトル、ロゴマークが入ったシートに挿入し、最終的にそのシートを印刷することができます。ドローイングモジュールは現在も製作中で多かれ少なかれ技術面でのテスト段階にあります！


{{TOCright}}

<img alt="" src=images/Drawing_extraction.png  style="width:600px;">

## GUIツール

2D図面を作成、設定、エキスポートするためのツールです。

-   <img alt="" src=images/Drawing_New.png  style="width:32px;"> [スケーラブルベクターグラフィックを開く](Drawing_Open_SVG/jp.md): SVGファイルとして保存されている図面を開きます

-   <img alt="" src=images/Drawing_Landscape_A3.png  style="width:32px;"> [A3図面の新規作成](Drawing_Landscape_A3/jp.md): FreeCADのデフォルトのA3テンプレートから新しい図面を作成します

-   <img alt="" src=images/Drawing_View.png  style="width:32px;"> [ビューの挿入](Drawing_View/jp.md): アクティブな図面上に選択されたオブジェクトのビューを挿入します

-   <img alt="" src=images/Drawing_Annotation.png  style="width:32px;"> [Annotation](Drawing_Annotation.md): Adds an annotation to the current drawing sheet

-   <img alt="" src=images/Drawing_Clip.png  style="width:32px;"> [Clip](Drawing_Clip.md): Adds a clip group to the current drawing sheet

-   <img alt="" src=images/Drawing_Openbrowser.png  style="width:32px;"> [Open Browser](Drawing_Openbrowser.md): Opens a preview of the current sheet in the browser

-   <img alt="" src=images/Drawing_Orthoviews.png  style="width:32px;"> [Ortho Views](Drawing_Orthoviews.md): Automatically creates orthographic views of an object on the current drawing sheet

-   <img alt="" src=images/Drawing_Symbol.png  style="width:32px;"> [Symbol](Drawing_Symbol.md): Adds the contents of a SVG file as a symbol on the current drawing sheet

-   <img alt="" src=images/Drawing_DraftView.png  style="width:32px;"> [Draft View](Draft_Drawing.md): Inserts a special Draft view of the selected object in the current drawing sheet

-   <img alt="" src=images/Drawing_SpreadsheetView.png  style="width:32px;"> [Spreadsheet View](Drawing_SpreadsheetView.md): Inserts a view of a selected spreadsheet in the current drawing sheet

-   <img alt="" src=images/Drawing_Save.png  style="width:32px;"> [図面の保存](Drawing_Save/jp.md): 現在の図面をSVGファイルとして保存します

-   [Project Shape](Drawing_ProjectShape.md): Creates a projection of the selected object (Source) in the 3D view.

-    **Note:**the [Draft Drawing](Draft_Drawing.md) tool is used with [Draft objects](Draft_Workbench.md). It has some additional capabilities over the Drawing tools, and supports specific objects like [Draft dimensions](Draft_Dimension.md).

## Workflow

この画像を見るとドローイングモジュールの主要なコンセプトが見て取れます。ドキュメントには図面に引用したい形状オブジェクト（Schenkel）が入っています。さらに\"Page\"が作成されています。ページはテンプレートに基づいてインスタンス化されます。今回のケースでは\"A3_Landscape\"テンプレートです。テンプレートには[SVG](SVG.md) ドキュメントであなたが普段使っているページ枠、ロゴ、標準のプレゼンテーション資料規格を使うことができます。

このページには複数のビューを挿入することができます。各ビューはページ上での位置（X、Yプロパティ）、拡大率（スケールプロパティ）などをはじめとした属性情報を持っています。ページ、ビュー、参照しているオブジェクトが変化するとそのたびにページが再生成され、ページの表示が更新されます。

## スクリプト処理

今のところエンドユーザー用の（GUI）ワークフローは非常に限定されたものしか用意されていません。APIはもっと充実しています。以下ではドローイングモジュールのスクリプト処理用APIをどう使うかの例を挙げていきます。

See the [Drawing API example](Drawing_API_example.md) page for a description of the functions used to create drawing pages and views.

The macro [CartoucheFC](Macro_CartoucheFC.md) allows you to create a custom information box on an A3 landscape page.

## Templates

FreeCAD comes bundled with a set of default templates, but you can find more on the [Drawing templates](Drawing_templates.md) page.

## Extending the Drawing Module 

Some notes on the programming side of the drawing module will be added to the [Drawing Documentation](Drawing_Documentation.md) page. This is to help quickly understand how the drawing module works, enabling programmers to rapidly start programming for it.

## Tutorials

-   [Drawing tutorial](Drawing_tutorial.md)

## External links 

-   [Intro to mechanical drawing on Youtube - by Normal Universe](https://www.youtube.com/watch?v=1Hm5Zyjmjac)





{{Drawing Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Obsolete Workbenches](Category_Obsolete Workbenches.md) > [Drawing](Category_Drawing.md) > Drawing Workbench/ja
