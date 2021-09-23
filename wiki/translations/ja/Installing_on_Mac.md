# Installing on Mac/ja






<div class="mw-translate-fuzzy">

インストーラーを使って1ステップでFreeCADをMac OS Xにインストールすることができます。


</div>


{{DownloadMacStable}}

and the weekly build can be downloaded from

<img alt="" src=images/Nightly.png  style="width:30px;">[Weekly](https://github.com/FreeCAD/FreeCAD-AppImage/releases/tag/weekly-builds)

You can also use a package manager such as HomeBrew to keep your software updated. Instructions to install HomeBrew can be seen [here](https://brew.sh/). When HomeBrew installed you can simply install FreeCAD 0.18.4 through your bash terminal with


```python
brew install --cask freecad
```

and to use the latest version available (0.19pre) on HomeBrew you may run


```python
brew install freecad
```

If there are any issues with the HomeBrew Cask or Formula you may report them to [here](https://github.com/FreeCAD/homebrew-freecad).

このページではFreeCADインストーラーの使い方と機能を説明しています。またアンインストール方法も記載されています。 インストールが終わると[使い始めることができます](Getting_started/jp.md)！

### 簡単なインストール

FreeCADインストーラーはディスクイメージファイルに収められたインストールパッケージ（.mpkg）として提供されています。

The FreeCAD installer is provided as a app package (.app) enclosed in a disk image file.

最新のインストーラーは[ダウンロードページからダウンロードすることができます](Download.md)。ファイルをダウンロードしたらディスクイメージをマウントして**Install FreeCAD**パッケージを実行してください。

![](images/mac_installer_1.png )

インストールされるパッケージのリストが記載された**Customize Installation**画面をインストーラーが表示します。もし既にこれらのパッケージのどれかがインストールされている場合はチェックボックスを使ってインストール選択を外すことができます。インストールされているかどうかわからない場合は全てのアイテムにチェックをいれたままにしておいてください。

![](images/mac_installer_2.png )

### アンインストール

今のところFreeCADにはアンインストーラーがありません。FreeCADとインストールされた全てのコンポーネントを完全に取り除きたい場合は以下のファイルとフォルダをごみ箱にドラッグしてください。

-   /Applications内：
    -   FreeCAD


<div class="mw-translate-fuzzy">

これで終わりです。


</div>


<div class="mw-translate-fuzzy">


{{docnav/jp|Install on Unix/jp|Getting started/jp}}


</div>



