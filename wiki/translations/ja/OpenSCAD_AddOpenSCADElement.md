# OpenSCAD AddOpenSCADElement/ja
---
 GuiCommand:   Name: OpenSCAD_AddOpenSCADElement   Name/ja: OpenSCAD_AddOpenSCADElement   Workbenches: OpenSCAD Module   OpenSCAD|MenuLocation: OpenSCAD -> Add OpenSCAD Element---


</div>

## Description


<div class="mw-translate-fuzzy">

#### 説明

タスクパネルにOpenSCADのコードを入力し、OpenSCADバイナリを実行することでOpenSCADのエレメントを追加します（OpenSCADが必要です）。


</div>

\'as mesh\'が選択されている場合、OpenSCADはメッシュをレンダリングします。

Addが押されるたびにOpenSCADのコードが実行されエレメントがインポートされます。


<div class="mw-translate-fuzzy">

この機能はOpenSCADの出力で表示される以上の文法チェック、エラーは出力しません。 エレメントが見つからない場合はuse\<\>ステートメントやinclude\<\>ステートメントで指定したパスが間違っている可能性があります。

通常の場合と同様、ライブラリはアクセス可能でなければなりません。下記のように書くとサンプルにアクセス可能です。

    include <../examples/example001.scad>;

上記ではOpenSCADアイコンとしても知られる最初のサンプルをインクルードしています。


</div>

Libraries should be accessible as usual, whereas example can be reached as stated below.


```python
include <../examples/example001.scad>;
```


<div class="mw-translate-fuzzy">

would include the first examples also known as the OpenSCAD icon


</div>

## Setup OpenSCAD within FreeCAD 


<div class="mw-translate-fuzzy">

#### Initial set up from within FreeCAD 

-   OpenSCAD needs to be installed on your computer before FreeCAD will have this functionality
    -   install OpenSCAD in the appropriate manner for your operating system. See [the OpenSCAD web site](http://www.openscad.org/) for more information
-   FreeCAD needs to be told where to find the OpenSCAD executable
    -   Switch to the OpenSCAD Workbench Menu -\> View Workbench -\> OpenSCAD
    -   Open the preferences dialog Menu -\> Edit -\> Preferences
    -   Click on \"OpenSCAD\" on the left plane
    -   Click on the button labled \"\...\" in General Settings -\> General OpenSCAD Settings -\> OpenSCAD executable to browser the directory or enter the path (e.g. Ubuntu based Linux distributions /usr/bin/openscad) directly into the line input right to the button
    -   close and restart FreeCAD, a new OpenSCAD icon will appear on the tool bar, and in the OpenSCAD menu, in the FreeCAD OpenSCAD workbench
-   It is also possible to add another optional Parameter which controls the maximum sides of a polygon before it is considered a circle (fn).


</div>

FreeCAD needs to be told where to find the OpenSCAD executable:

-   Switch to the <img alt="" src=images/Workbench_OpenSCAD.svg  style="width:24px;"> [OpenSCAD Workbench](OpenSCAD_Workbench.md) via 
**View → Workbench → OpenSCAD**
-   Open the preferences dialog **Edit → Preferences**
-   Click on \"OpenSCAD\" on the left plane
-   Click on the button labled **...** in **General Settings → General OpenSCAD Settings → OpenSCAD executable** to browse the directory or enter the path (e.g. Ubuntu based Linux distributions `/usr/bin/openscad`) directly into the line input right to the button
-   Close and restart FreeCAD

:   **Result:** A new OpenSCAD icon will appear on the tool bar, and in the OpenSCAD menu, in the FreeCAD OpenSCAD workbench.

Note: It is also possible to add another optional Parameter which controls the maximum sides of a polygon before it is considered a circle (fn).


<div class="mw-translate-fuzzy">

FreeCADバージョン0.14以降、上記の設定が空の場合、FreeCADはOpenSCAD実行可能ファイルを検索します。


</div>





{{OpenSCAD_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [OpenSCAD](OpenSCAD_Workbench.md) > OpenSCAD AddOpenSCADElement/ja
