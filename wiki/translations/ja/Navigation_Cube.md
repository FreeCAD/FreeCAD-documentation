# Navigation Cube/ja
{{TOCright}}

## Introduction

The **Navigation Cube** gives visual information about the camera orientation in the current [3D view](3D_view.md) and can be used to change it. By default it is visible and resides in the upper right corner of the view.

The Navigation Cube was updated in FreeCAD version 0.20 and the rest of this page describes that version. In FreeCAD version 0.19 the main behavior is the same but some features are missing.

![](images/Navigation_Cube_Example.png )


<div class="mw-translate-fuzzy">

ナビゲーションキューブは、次の部分で構成されています。

-   Directional Arrows
-   Main Navigation Cube
-   Mini-cube Menu


</div>

All parts, except the axis indicators, can be clicked.

## Usage

### Main cube 

The main cube has 26 faces: 6 main faces, 12 rectangular edge faces (<small>(v0.20)</small> ), and 8 corner faces. Clicking any of them will reorient the camera so that its direction is perpendicular to the selected face.


<div class="mw-translate-fuzzy">

## Directional Arrows 


</div>


<div class="mw-translate-fuzzy">

6つの方向矢印があります。4つの三角矢印、上、下、左、右に1つずつ。 2つの湾曲した矢印。1つは上の矢印の両側にあります。


</div>

### Reverse view button 

Clicking the round button in the top right corner of the Navigation Cube will rotate the [3D view](3D_view.md) 180 degrees around the vertical axis of the view.


<div class="mw-translate-fuzzy">

## Mini-cube Menu 


</div>


<div class="mw-translate-fuzzy">

ナビゲーションキューブの右下隅には小さなキューブがあります。 この立方体をクリックすると、ビューのタイプを変更するために使用できるメニューが表示されます（直交図、遠近法、等角図）。 そして、「ズームしてフィット」を実行します。


</div>

## Customization

### Move the Navigation Cube 


<div class="mw-translate-fuzzy">

## ナビゲーションキューブの表示を移動する

メインナビゲーションキューブ内の任意の場所でマウスを押してドラッグすると、ナビゲーションキューブ制御構造全体を3D表示内の別の場所に移動できます。 この記事の執筆時点（0.18）では、マウスポインタがメインナビゲーションキューブの端を越えて移動するまで構造は開始されません。


</div>

### Preferences

The Navigation Cube is controlled by several preferences: **Edit → Preferences... → Display → Navigation → Navigation cube**. See [Preferences Editor](Preferences_Editor#Navigation.md).

### Advanced options 

The [CubeMenu](Interface_Customization#CubeMenu.md) external workbench provides easier access to several more advanced customization options.


<div class="mw-translate-fuzzy">


{{docnav|Mouse Model|Document structure}}


</div>



---
![](images/Right_arrow.png) [documentation index](../README.md) > [User Documentation](Category_User Documentation.md) > Navigation Cube/ja
