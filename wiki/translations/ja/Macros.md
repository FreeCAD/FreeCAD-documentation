# Macros/ja
{{TOCright}}

## Introduction


<div class="mw-translate-fuzzy">

マクロはFreeCADに複雑なアクションを作成するための便利な方法です。簡単にあなたが行う操作を記録したものを名前をつけて保存し、いつでも好きなときに再生することができます。マクロはpythonコマンドで記述されているので、それらを編集して非常に複雑なスクリプトを作成することができます。


</div>

While Python scripts normally have the `.py` extension, FreeCAD macros should have the `.FCMacro` extension. A collection of macros written by experienced users is found in the [macros recipes](Macros_recipes.md) page.

See the [Power users hub](Power_users_hub.md) to learn more about the [Python](Python.md) programming language, and about writing macros. In particular, you should start with these pages:

-   [Introduction to Python](Introduction_to_Python.md)
-   [Python scripting tutorial](Python_scripting_tutorial.md)
-   [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md)


<div class="mw-translate-fuzzy">

### 操作方法

コンソール出力（メニュー Edit -\> Preferences -\> General -\> Macros -\> Show scripts commands in python console）を有効にした場合は、FreeCADでは、ボタンを押すのなどのあなたが行うすべてのアクションがpythonコマンドを出力していることがわかります。 このコマンドはマクロに記録することができるものです。マクロを作成するための主なツールはマクロのツールバーです。![](images/Macros_toolbar.jpg )それには、4つのボタンがあります：「記録」、「記録終了」、「編集」、「マクロの実行」です。


</div>

Enable the console output in the menu **Edit → Preferences → General → Macro → Show scripts commands in python console**. You will see that in FreeCAD, every action you do, such as pressing a button, outputs a Python command. Those commands are what can be recorded in a macro. The main tool for making macros is the macros toolbar: ![](images/Macros_toolbar.jpg ). On it you have 4 buttons: Record, stop recording, edit and play the current macro.


<div class="mw-translate-fuzzy">

それを使用することは非常に簡単です：「記録」ボタンを押すと、マクロに名前を付けるように求められます。その後、いくつかのアクションを実行します。作業が完了したら、「記録終了」ボタンをクリックして、あなたの行ったアクションが保存されます。ここで「編集」ボタンを押すとマクロダイアログを開くことができます。


</div>


<div class="mw-translate-fuzzy">

![](images/Macros.png ) ![](images/Macros.jpg )


</div>


<div class="mw-translate-fuzzy">

マクロダイアログには、あなたのマクロを管理、編集、削除、新規作成ができます。マクロを編集する場合、コードに変更を加えることができるエディタウィンドウが開きます。 新しいマクロは[Addon ManagerにリンクするAddons](Std_AddonMgr.md) \...ボタンを使ってインストールできます。


</div>


<div class="mw-translate-fuzzy">

### 例

「記録」ボタンを押して名前をつけてみましょう。\"cylinder 10×10\"にします。その後、[パートワークベンチで](Part_Workbench/ja.md)、半径= 10、高さ= 10でシリンダを作成します。そして、「記録停止」ボタンを押してください。マクロ編集のダイアログでは、記録されているPythonのコードを見ることができ、必要に応じて変更を加えることができます。マクロを実行する簡単な方法は、マクロをエディタで開きツールバー上の「実行」ボタンを押します。 マクロは常にディスクに保存され、あなたが行ったすべての変更、または新しく作成したマクロはFreeCADを次回起動時も利用できるようになっています。


</div>

Press the record button, give a name, let\'s say \"cylinder 10x10\", then, in the [Part Workbench](Part_Workbench.md), create a cylinder with radius = 10 and height = 10. Then, press the \"stop recording\" button. In the edit macros dialog, you can see the python code that has been recorded, and, if you want, make alterations to it. To execute your macro, simply press the execute button on the toolbar while your macro is in the editor. You macro is always saved to disk, so any change you make, or any new macro you create, will always be available next time you start FreeCAD.


<div class="mw-translate-fuzzy">

### カスタマイズ

もちろん、マクロを使用するたびに、エディタでマクロを開くのは実用的ではありません。 FreeCADは、マクロにキーボードショートカットを割り当てる、メニューのエントリに追加するなど、マクロを使用するためのはるかに優れた方法を提供します。マクロが作成されると、Tools -\> Customize メニューから設定を行うことができます


</div>

Of course it is not practical to load a macro in the editor in order to use it. FreeCAD provides much better ways to use your macro, such as assigning a keyboard shortcut to it or putting an entry in the menu. Once your macro is created, all this can be done via the **Tools → Customize** menu.

![](images/Macros_config.jpg )


<div class="mw-translate-fuzzy">

[Customize Toolbars](Customize_Toolbars.md) この方法であなたのマクロをFreeCADの標準ツールのように使うことができます。これは、FreeCADのpythonスクリプトの力のおかげで、インターフェイスに独自のツールを簡単に追加することができます。Pythonスクリプティングについて詳細をお知りになりたい場合は[Scriptingページを参照してください](Scripting.md)。


</div>

See [Customize Toolbars](Customize_Toolbars.md) for a more detailed description.


<div class="mw-translate-fuzzy">

### 記録せずにマクロを作成する

[How to install macros](How_to_install_macros.md) また、直接GUI操作を記録せずに、マクロにpythonコードをコピー/ペーストすることができます。新しいマクロを作成・編集して、コードを貼り付けます。あなたのマクロはFreeCADの文書を保存するのと同じ方法で保存することができます。FreeCADを次回起動する時には、マクロは「Macro」メニューの\"Installed Macros\"項目の下に表示されます。


</div>

You can also directly copy/paste python code into a macro, without recording GUI action. Simply create a new macro, edit it, and paste your code. You can then save your macro the same way as you save a FreeCAD document. Next time you start FreeCAD, the macro will appear under the \"Installed Macros\" item of the Macro menu.

See [How to install macros](How_to_install_macros.md) for a more detailed description.


<div class="mw-translate-fuzzy">

### マクロリポジトリ

[Macros recipesページには](Macros_recipes.md)、あなたのFreeCADに追加できるいくつかの便利なマクロが紹介されています。


</div>

There are two main places for macros. The first one is the official peer-reviewed macro repository on _ page from which you can pick some useful macros to add to your FreeCAD installation. Macros from both repositories can be installed via the [Addon Manager](Std_AddonMgr.md) directly from FreeCAD.


<div class="mw-translate-fuzzy">

### Links

[Installing more workbenches](Installing_more_workbenches.md)


</div>

-   [Automatically run macro at startup](Macro_at_Startup.md)
-   [Installing more workbenches](Installing_more_workbenches.md)


<div class="mw-translate-fuzzy">

### Tutorials

[How to install additional workbenches](How_to_install_additional_workbenches.md)


</div>

You can manually install extensions, however, it is much simpler to just use the [Addon Manager](Std_AddonMgr.md).

-   [How to install macros](How_to_install_macros.md)
-   [How to install additional workbenches](How_to_install_additional_workbenches.md)


<div class="mw-translate-fuzzy">


{{docnav/ja|Image Workbench/ja|Introduction to Python/ja}}


</div>


{{Powerdocnavi

}}

_ _ _

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Macros/ja
