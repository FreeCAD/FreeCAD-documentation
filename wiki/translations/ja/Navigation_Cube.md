# Navigation Cube/ja






{{TOCright}}

The navigational cube control, or **navigation cube**, is a user interface graphic aid for reorienting the 3D view. By default, it is visible and resides in the upper right corner of the 3D display. If you are looking at the standard 3D view, it looks like the following:

![](images/FreeCAD-v0-18-NavCube_Axonometric.png )

ナビゲーションキューブは、次の部分で構成されています。

-   Directional Arrows
-   Main Navigation Cube
-   Mini-cube Menu


<div class="mw-translate-fuzzy">

Hovering the mouse pointer over a feature of the navigational cube turns the feature light blue; clicking will reorient the 3D view as indicated by the feature. (Note: As of this writing, the pointer does not register perfectly with some navigational cube features. If a feature you are trying to select does not turn light blue, move the mouse until you find a spot which causes the feature to turn blue.) In the example below, the 3D view has been rotated by a [mouse gesture](Mouse_Model.md) to a \"non-standard\" orientation. The pointer is over a corner (indicated by the blue color); clicking will reorient the 3D view to a standard axonometric view with that corner facing you.


</div>

![](images/FreeCAD-v0-18-NavCube_SelectCorner.png )

## Directional Arrows 

6つの方向矢印があります。4つの三角矢印、上、下、左、右に1つずつ。 2つの湾曲した矢印。1つは上の矢印の両側にあります。

三角形の矢印をクリックすると、3Dビューが矢印の方向に垂直な線を中心に45度回転します。 湾曲した矢印をクリックして、3Dビューを真っ直ぐな線を中心に回転させます。 \<！ - 注：回転軸が正しく定義されていません。 それぞれが2つの平面の交点ですが、それらをどのように記述するのか私は理解できません - \>

## プライマリナビゲーションキューブ

メインナビゲーションキューブ（このセクションでは \"nav cube\"）は、3Dビューの主要部分にある実際のオブジェクトの向きを追跡します。 メイン3Dビューの向きを変える操作は、ナビゲーションキューブの向きも変えます。

The nav cube is essentially a 3D view of a cube with its three main component types (faces, edges, and corners) enhanced so they may be easily clicked with the pointer. Clicking on a particular component will set the 3D view to have that component centered and facing you. The nav cube is somewhat \"squashed\", as if the feature farthest from you were larger than the feature directly facing you. This allows the features adjacent to the feature facing you to be seen and consequently selected. For example, in a \"normal\" view of a regular cube, when one face is facing you, you can also see the four edges of that face and the four corners of that face. In the \"squashed\" nav cube, you can also see features representing each of the adjacent faces, the four edges connecting the corners of the face facing you with the opposite face, and the corners of opposite face. This allows you to select any of the possible standard views except the opposite face and its edges (21 out of 26 possible views):

-   The face facing you (does nothing, since that is the current view)
-   The four edges of the current face
-   The four corners of the current face
-   The four adjacent faces
-   The four edges leading to the opposite face
-   The four corners of the opposite face

Not possible:

-   The opposite face
-   The edges of the opposite face

Note: As of this writing (v 0.18), there are some problems with the nav cube; not all features are currently selectable. In particular, edges are not selectable, nor are the four corners of the immediately facing face.

### 顔の選択

顔をクリックすると、その特定の顔があなたの方を向くように3Dビューの向きが変わります。 正面から見ると、上記のように他の選択点が利用可能である。 4つの隣接する面を表す4つの細い棒が外側の端にあります。 それらをクリックすると、隣接する面に対応するビューが選択されます。 対応する軸測角ビューを設定するために使用できる4つの丸い角があります。 現在機能していない内側のエッジとコーナーのセットもあります。

### エッジ選択

残念ながら、エッジ選択は現在機能していません。 境界線を選択しようとすると、その背後にある面が選択されます。 端をクリックした場合は、端が自分の方を向くように端を中央に配置する必要があります。

### コーナー選択

角の1つをクリックすると、その角から見たときに不等角投影図が表示されます。 上記のように、現在面があなたに直接面しているとき、その面の角は選択できません。

## Mini-cube Menu 

ナビゲーションキューブの右下隅には小さなキューブがあります。 この立方体をクリックすると、ビューのタイプを変更するために使用できるメニューが表示されます（直交図、遠近法、等角図）。 そして、「ズームしてフィット」を実行します。


<div class="mw-translate-fuzzy">

## ナビゲーションキューブの表示を移動する

メインナビゲーションキューブ内の任意の場所でマウスを押してドラッグすると、ナビゲーションキューブ制御構造全体を3D表示内の別の場所に移動できます。 この記事の執筆時点（0.18）では、マウスポインタがメインナビゲーションキューブの端を越えて移動するまで構造は開始されません。


</div>

## Configuration

The navigation cube is configurable, including adjusting its size: **Edit → Preferences... → Display → Navigation → Navigation cube** <small>(v0.19)</small> .

For more advanced configuration, refer to the [CubeMenu](Interface_Customization#CubeMenu.md) [external workbench](External_workbenches.md).


<div class="mw-translate-fuzzy">


{{docnav|Mouse Model|Document structure}}


</div>




[Category:User Documentation](Category:User_Documentation.md)
