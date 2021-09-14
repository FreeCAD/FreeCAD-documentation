# Draft API/ja




<div class="mw-translate-fuzzy">

これらの関数はDraftモジュールの一部であり、Draftモジュールをインポートすることでスクリプト、マクロ、Pythonインタプリタから使用することができます。


</div>

These functions are part of the [Draft Workbench](Draft_Workbench.md) and can be used in [macros](macros.md) and from the [Python](Python.md) console once the `Draft` module has been imported.

例: 
```python
import FreeCAD, Draft

myrect = Draft.makeRectangle(4, 3)
mydistance = FreeCAD.Vector(2, 2, 0)
Draft.move(myrect, mydistance)
```


{{APIFunction/jp|cut|FreeCAD.Object, FreeCAD.Object|与えられた2つのオブジェクトの差分から作成されたカットオブジェクトを返します。元のオブジェクトは非表示になります。|新しく作成されたオブジェクト}}


{{APIFunction/jp|extrude|FreeCAD.Object, Vector|与えられたオブジェクトをベクトルによって指定された方向に押し出します。元のオブジェクトは非表示になります。|新しく作成されたオブジェクト}}


{{APIFunction/jp|formatObject|FreeCAD.Object, [FreeCAD.Object]|与えられたターゲットオブジェクトに対してDraftツールバーに現在設定されているプロパティ（線の色と太さ）を適用します。ただし二番目のオブジェクトが与えられている場合はそのプロパティをコピーします。またコンストラクションボタンが押されている場合はオブジェクトをコンストラクショングループに配置します。|なし}}


{{APIFunction/jp|fuse|FreeCAD.Object, FreeCAD.Object|
与えられた2つのオブジェクトの結合から作成されたオブジェクトを返します。もしオブジェクトが同一平面上にある場合は特殊なDraftワイヤーが使用され、そうでない場合は最終的なオブジェクトは標準的なPartの結合物になります。|新しく作成されたオブジェクト}}


{{APIFunction/jp|getDraftPath|[string]|Draftモジュールが実行されているユーザーまたはシステムパスを返します。サブパス、またはファイル名が与えられた場合はDraftモザユール内部のサブパスのフルパスが返されます。|ファイルパス}}


{{APIFunction/jp|getGroupContents|list|グループに対して与えられたリストを再帰的にスキャンします。グループが見つかった場合、その内容がリストに追加されます。|FreeCADオブジェクトのリスト}}


{{APIFunction/jp|getRealName|string|オブジェクト名から末尾の数字を取り除きます。|取り除いた後のオブジェクト名}}


{{APIFunction/jp|getSelection| |現在のFreeCADで選択物を返します。|現在のFreeCADで選択物}}


{{APIFunction/jp|makeCircle|radius, [placement], [facemode], [startangle], [endangle]|与えられた半径（radius）の円オブジェクトを作成します。位置（placement）が指定された場合にはそれが使用されます。facemodeがFalseの場合には円はワイヤーフレームで表示されます。それ以外の場合は面として表示されます。startangleとendangleが（単位、°で）与えられた場合はそれが使用されオブジェクトは円弧となって表示されます。|新しく作成されたオブジェクト.}}


{{APIFunction/jp|makeDimension|Vector, Vector, [Vector] または FreeCAD.Object, int, int, [Vector]|一つ目と二つ目のベクトル間の距離を測る寸法オブジェクトを作成します。三番目のベクトルが与えられた場合にはそこを通る寸法線が付与されます。Draftツールバーの現在の線の色と幅が使用されます。2つのベクトルの代わりにFreeCADオブジェクトと二つの整数（、さらにオプションで寸法線が通過するベクトル）を渡すことも可能です。その場合には寸法はオブジェクトに関連付けられ与えられた二つの数字で表される二頂点の間の距離が計測されます。|新しく作成されたオブジェクト.}}


{{APIFunction/jp|makeLine|Vector, Vector|与えられた二つのベクトル間に引かれた線を作成します。Draftツールバーの現在の線の色と幅が使用されます。|新しく作成されたオブジェクト.}}


{{APIFunction/jp|makeRectangle|length, width, [placement], [facemode]|X方向にlength、Y方向にheightの大きさの長方形オブジェクトを作成します。位置（placement）が指定された場合にはそれが使用されます。facemodeがFalseの場合には円はワイヤーフレームで表示されます。それ以外の場合は面として表示されます。Draftツールバーの現在の線の色と幅が使用されます。|新しく作成されたオブジェクト.}}


{{APIFunction/jp|makeText|string または list, [Vector], [screenmode]|
テキストオブジェクトを作成します。ベクトルが与えられている場合にはその点に文字列またはリストで与えられた複数の文字列が一行に一文字列ずつ配置されます。Draftツールバーの現在の色とユーザー設定で指定されたテキストの高さ、フォントが使用されます。screenmodeがTrueの場合、テキストは常にビュー方向を向き、そうでない場合はXY平面上に配置されます。|新しく作成されたオブジェクト.}}


{{APIFunction/jp|makeWire|list または Part.Wire, [closed], [placement], [facemode]|与えられたベクトルのリストまたは与えられたワイヤーからワイヤーオブジェクトを作成します。closedがTrue、または最初と最後の点が一致している場合はワイヤーが閉じます。facemodeがTrue（またはワイヤーが閉じている）の場合にはワイヤーは塗りつぶされた状態で表示されます。 Draftツールバーの現在の線の色と幅が使用されます。|新しく作成されたオブジェクト.}}


{{APIFunction/jp|move|FreeCAD.Object または list, Vector, [copymode]|与えられたオブジェクトまたは与えられたリストに入っているオブジェクトを与えられたベクトルによって表される方向と距離に移動させます。copymodeがTrueの場合、実際のオブジェクトは動かされず、代わりにコピーが作成されます。|オブジェクト（copymodeがTrueの場合はオブジェクトのコピー）}}


{{APIFunction/jp|precision| |Draftのユーザー設定から精度の値を返します|整数}}


{{APIFunction/jp|rotate|FreeCAD.Object または list, angle, [center], [axis] ,[copymode]|
与えられたオブジェクトまたは与えられたリストに入っているオブジェクトを与えられた角度だけ回転させます。centerが与えられている場合にはaxisを回転軸として使用してcenterを中心に回転させます。axisが省略されている場合にはZ軸垂直方向の周りに回転させます。copymodeがTrueの場合、実際のオブジェクトは動かされず、代わりにコピーが作成されます。|オブジェクト（またはそのコピー）}}


{{APIFunction/jp|scale|FreeCAD.Object または list, vector, [center], [copymode]|
与えられたオブジェクトまたは与えられたリストに入っているオブジェクトを与えられたベクトルで（X、Y、Z方向に）定義される拡大縮小率で拡大縮小します。centerが与えられている場合にはその周りに拡大縮小します。copymodeがTrueの場合、実際のオブジェクトは動かされず、代わりにコピーが作成されます。|オブジェクト（またはそのコピー）}}


{{APIFunction/jp|select|FreeCAD.Object|全ての選択を解除し、渡されたオブジェクトのみを選択します。|なし}}


{{APIFunction/jp|shapify|FreeCAD.Object|パラメトリックな形状オブジェクトを非パラメトリックなものに変換します。|新しいオブジェクト}}


{{APIFunction/jp|draftify|FreeCAD.Object または list|与えられたオブジェクトまたは与えられたリストの各オブジェクトをDraftのパラメトリックワイヤーに変えます。|なし}}


{{APIFunction/jp|getSVG|FreeCAD.Object, [linemodifier], [textmodifier], [(u,v)]|
与えられたオブジェクトのSVG表現を作成します。linemodifier属性はライン幅の（パーセント単位の）拡大縮小率で、textmodifierはテキストサイズ用です。またオプションで投影面を定義するベクトルのタプルを指定できますが、指定しない場合はジオメトリーはXY平面に投影されます。|与えられたオブジェクトのSVG表現が入った文字列}}


 




[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
