


{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

[Pivy](http://pivy.coin3d.org/)はFreeCADで使われている3Dレンダリングライブラリである[Coin3d](http://www.coin3d.org)用のPythonのバインディングライブラリです。実行中のPythonインタプリタにインポートするとFreeCADの3DビューアーなどのCoin3d[シーングラフと直に対話処理を行ったり](Scenegraph/jp.md)、新しい3Dビューアーを作成することさえできます。Pivyは標準のFreeCADインストールに同梱されています。


</div>

When imported in a running Python interpreter, Pivy allows us to communicate directly with any running Coin [scenegraph](Scenegraph.md), such as the [3D view](3D_view.md), or even to create new ones. Pivy is not required to compile FreeCAD, but it is required at runtime when running Python-based workbenches that create shapes on screen, like [Draft](Draft_Workbench.md) and [Arch](Arch_Workbench.md). Because of this, Pivy is normally installed when installing a distribution of FreeCAD.


<div class="mw-translate-fuzzy">

Coinライブラリはいくつかに分割されています。Coin自体はシーングラフの操作を担い、Windowsといった複数のGUIシステム用のパッケージがありますが私たちの場合はQt用になります。これらの分割されたモジュールもシステム上に存在する場合にはPivyから利用することができます。Coinモジュールは常駐していて自由に利用することができます。既にFreeCADによって行われているので3D表示をどのインターフェイスに紐付けするのか気にする必要はありません。私たちがやらなければならないのは以下のコマンドを実行することだけです：


</div>


```python
from pivy import coin
```


<div class="mw-translate-fuzzy">

## シーングラフへのアクセスと変更


</div>


<div class="mw-translate-fuzzy">

典型的なCoinシーンがどの様に構成されているかは[シーングラフページで見ました](Scenegraph/jp.md)。FreeCADの3Dビューに表示されているものは全てCoinシーングラフであり、同じやり方で構成されています。ルートのノードが一つあり、画面上のオブジェクトは全てその子ノードです。


</div>

FreeCADでは3Dビューシーングラフのルートノードに簡単にアクセスすることができます：


```python
sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
print(sg)
```

こうするとルートノードが返されます。


```python
<pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
```

シーンの直下の子ノードを調べることもできます。


```python
for node in sg.getChildren():
    print(node)
```


<div class="mw-translate-fuzzy">

SoSeparatorsやSoGroupsといったこれらノードは自身の子ノードを持ちます。利用可能なCoinオブジェクトの全リストは[Coin公式ドキュメント](http://doc.coin3d.org/Coin/classes.html)にあります。


</div>

今度はシーングラフに何か追加してみましょう。すてきな赤い立方体を追加してみることにしましょう：


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```


<div class="mw-translate-fuzzy">

（すてきな）赤い立方体ができました。以下を試してみてください：


</div>


```python
col.rgb = (1, 1, 0)
```


<div class="mw-translate-fuzzy">

わかったでしょうか？実行中であっても全てのものに対してアクセスと変更を行うことができるのです。再計算や再描画は必要ありません。Coinが全て面倒を見てくれます。物体のシーングラフへの追加、プロパティの変更、物体の非表示、一時的なオブジェクトの表示、何でもできます。もちろん3Dビューに関係したことだけですが。この表示はFreeCADがファイルを開いた時とオブジェクトが必要とした時に再計算されます。従って既存のFreeCADオブジェクトの外見を変更した場合、その変更はオブジェクトが再計算されるかファイルを再度開いた瞬間に失われます。


</div>


<div class="mw-translate-fuzzy">

スクリプトでシーングラフを操作する場合の鍵となるのは必要な際に追加したノードの特定のプロパティにアクセスできるということなのです。例えば立方体を動かしたいとしましょう。自作のノードにSoTranslationノードを追加することになるでしょう。ちょうどこんな具合です：


</div>


```python
col = coin.SoBaseColor()
col.rgb = (1, 0, 0)
trans = coin.SoTranslation()
trans.translation.setValue([0, 0, 0])
cub = coin.SoCube()
myCustomNode = coin.SoSeparator()
myCustomNode.addChild(col)
myCustomNode.addChild(trans)
myCustomNode.addChild(cub)
sg.addChild(myCustomNode)
```


<div class="mw-translate-fuzzy">

OpenInventorのシーングラフではその順番が重要であるということを思い出してください。ノードは以降のノードに影響を与えます。color red、cube、color yellow、sphere とすれば赤い立方体と黄色い球が表示されます。もし今、既存の自作ノードに移動を追加すると移動は立方体の後になり、立方体に影響を与えません。上記のように作成時に挿入しておけば次のようにできます：


</div>


```python
trans.translation.setValue([2, 0, 0])
```


<div class="mw-translate-fuzzy">

こうすると立方体が2単位分、右に移動します。 最後に何かを取り除くには次のようにします：


</div>


```python
sg.removeChild(myCustomNode)
```

[top](#top.md)


<div class="mw-translate-fuzzy">

## コールバック機能の使用


</div>


<div class="mw-translate-fuzzy">

[コールバック機能](http://en.wikipedia.org/wiki/Callback_%28computer_science%29)とはCoinライブラリの様な現在使用しているライブラリがコールバック、つまり現在実行中のPythonオブジェクトから特定の関数を呼び出すことを可能にするシステムのことです。これは非常に便利です。これを使うとシーンで何か特定のイベントが起きた場合にCoinからあなたへ通知することができるのです。Coinでは色々なものを監視することができます。マウスの位置、マウスボタンのクリック、キーボードのキーが押されたかどうか、まだまだ他にもあります。


</div>

FreeCADではそういったコールバックを簡単に使うための機能があります：


```python
from pivy import coin

class ButtonTest:
    def __init__(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getMouseClick) 

    def getMouseClick(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == coin.SoMouseButtonEvent.DOWN:
            print("Alert!!! A mouse button has been improperly clicked!!!")
            self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)

ButtonTest()
```


<div class="mw-translate-fuzzy">

コールバックが起きた時にもオブジェクトは実行され続けなければならないのでコールバックはオブジェクトで初期化されなけれればなりません。 利用可能なイベントとパラメータの[全リストまたは](Code_snippets#Observing_mouse_events_in_the_3D_viewer_via_Python.md)[Coin公式ドキュメント](http://doc.coin3d.org/Coin/classes.html)を参照してください。


</div>

[top](#top.md)


<div class="mw-translate-fuzzy">

## ドキュメント


</div>


<div class="mw-translate-fuzzy">

残念ながらPivy自体にはちゃんとしたドキュメントがまだありません。しかしPivyはCoinと正確に対応するのでC++スタイルをPythonスタイルに読み替えれば（例えばSoFile::getClassTypeId()はPivyではSoFile.getClassId()となるでしょう）Coinドキュメントをリファレンスとして安全に使用できます。


</div>

In C++:


```python
SoFile::getClassTypeId()
```

In Pivy:


```python
SoFile.getClassId()
```

-   [Coin3D](https://github.com/coin3d) homepage.
-   [Pivy](https://github.com/coin3d/pivy) homepage.
-   [Coin3D wiki](https://github.com/coin3d/coin/wiki), at GitHub.
-   [Coin3D wiki documentation](https://github.com/coin3d/coin/wiki/Documentation), at GitHub.
-   [Coin3D Documentation](https://coin3d.github.io/Coin/html/), latest automatically generated Doxygen documentation.

### Older

These links provide reference documentation for Coin v3.x. The differences with v4.x are minimal, so they may still be useful.

-   [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
-   [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
-   [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.

[top](#top.md)


{{Powerdocnavi

}} 

[Category:Developer Documentation{{\#translation:}}](Category:Developer_Documentation.md) [Category:Python Code{{\#translation:}}](Category:Python_Code.md)
