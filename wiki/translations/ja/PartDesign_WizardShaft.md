# PartDesign WizardShaft/ja
---
- GuiCommand:/jp   Name:PartDesign_WizardShaft   Workbenches:[パートデザイン](PartDesign_Workbench/jp.md), Complete---


</div>


<div class="mw-translate-fuzzy">

## イントロダクション

このツールを使うと値のテーブルからシャフトを作成し、その力とモーメントを解析することができます。


</div>


<div class="mw-translate-fuzzy">

FreeCADのPythonコンソールに

 Gui.runCommand('PartDesign_WizardShaft')

と入力するとウィザイードが起動します。ウィザードは起動するとデフォルトのテーブル、対応するシャフト部品、力/モーメントのグラフを表示します。


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/WizardShaft_Part.jpg  style="width:800px;">


</div>

ウィンドウの上部にはテーブルが表示されます。テーブルはシャフトの区分と対応する数値の振られた列で構成されます。シャフトの区分は長さと直径によって特徴づけられています。メインウィンドウには二つのタブが表示されます。一つにはシャフト部品そのもの（回転形状）が上記の画像のように表示されます。もう一つのタブにはテーブルで定義された負荷に対するせん断応力とモーメントのグラフが表示されます。

<img alt="" src=images/shaftwizard1.jpg  style="width:800px;"> 

------------------------------------------------------------------------


<div class="mw-translate-fuzzy">

## 必須

シャフト設計ウィザードはせん断応力と曲げモーメントのグラフを作成、表示するためにnumpyパッケージとpyxplotプログラムを使用しています。

## パラメーター

シャフトの各区分には以下のパラメーターが定義可能です。

-   区分の長さ
-   区分の直径
-   負荷のタイプ。メニューをスクロールして適切な項目ををクリックする必要があることに注意してください。そうしないと選択されません！
    -   None: 負荷なし
    -   Fixed: シャフトの末端を固定（例えば他の部品に溶接されている場合）。この負荷タイプは最初の区分、または最後の区分にのみ定義できます。
    -   Static: シャフト区分に静荷重あり
-   シャフトの区分にかける負荷
-   区分の中で負荷がかける位置。位置は区分左端からの距離で定義されます。

（この他にも行、負荷タイプがありますがまだ機能が実装されていません）


</div>

## Parameters

For each shaft segment, the following parameters can be defined

-   Length of the segment
-   Diameter of the segment
-   Load type. Note that you have to click on the desired entry in the menu after scrolling to it, otherwise it will not be selected!
    -   None: No load
    -   Fixed: The end of the shaft is fixed (e.g. welded to another part). This load type can only be defined for the first or last segment.
    -   Static: There is a static load on this shaft segment
-   Load on the shaft segment
-   Location where the load is applied to the segment. The location is counted from the left-hand edge of the segment

(Other rows and load types exist but no functionality has been implemented yet)

## メニュー

新しいシャフトの区分を追加するにはテーブルの右側の何もない領域で右クリックして\"Add column\"を選択します。

## 制限事項

-   同じ直径のシャフト区分を隣接して配置することはできません。

## 計画中の機能

-   テーブルによるシャフトの辺の面取りと丸め込み
-   以前に作成したシャフトウィザード部品の認識とそれによるテーブル値の初期化
-   シャフトの圧力計算
-   シャフトにかかる負荷の可視化（FEMモジュールと同じ機能が使用可能）
-   ドキュメントオブジェクトとして負荷を定義（FEMモジュールと同じ機能が使用可能）
-   物性データベース
-   Y方向と同様にZ方向への負荷を許可（負荷をドキュメントオブジェクトとして定義する必要があります。そうしないとテーブルが非常に長くなってしまいます）








{{PartDesign Tools navi

}}

---
[documentation index](../README.md) > [PartDesign](PartDesign_Workbench.md) > PartDesign WizardShaft/ja
