# Macros/zh-cn
{{TOCright}}

## 简介


<div class="mw-translate-fuzzy">

宏是一种在FreeCAD中生成一系列复杂动作的简便方式。您可以借助此功能方便地将多个动作记录下来，将其保存在所取名下，在需要的时候反复执行。由于宏是一系列[Python命令](Python.md)，所以可以对它们进行编辑，并创建出非常复杂的脚本。


</div>


<div class="mw-translate-fuzzy">

Python脚本通常以`.py`作为扩展名，而FreeCAD中的宏则以`.FCMacro`作为扩展名。由经验丰富者所编写的宏的合集可从[macros recipes页面找到](macros_recipes.md)。


</div>


<div class="mw-translate-fuzzy">

参考[Introduction to Python来学习Python编程语言](Introduction_to_Python.md)，再阅读[Python scripting tutorial与](Python_scripting_tutorial.md)[FreeCAD Scripting Basics来学习如何编写宏](FreeCAD_Scripting_Basics.md)。


</div>


<div class="mw-translate-fuzzy">

## 如何工作

在**Edit → Preferences → General → Macro → Show scripts commands in python console**菜单中开启控制台输出。这时，您将看到在FreeCAD中所执行的每个动作（例如按下按钮）的对应Python命令都输出到了控制台中。这些命令都能记录到宏中。制作宏的主要工具为宏工具栏：![](images/Macros_toolbar.jpg )。其中有4个按钮：Record（记录）, stop recording（停止记录）, edit（编辑）以及执行当前的宏（play）。


</div>

Enable the console output in the menu **Edit → Preferences → General → Macro → Show scripts commands in python console**. You will see that in FreeCAD, every action you do, such as pressing a button, outputs a Python command. Those commands are what can be recorded in a macro. The main tool for making macros is the macros toolbar: ![](images/Macros_toolbar.jpg ). On it you have 4 buttons: Record, stop recording, edit and play the current macro.

这个工具使用起来也十分方便：按下记录按钮，系统会让您给宏起个名，接下来让您来执行一些动作。待记录的动作执行完毕后，点击停止记录按钮，之前的动作就会被保存下来。随后即可利用编辑按钮来访问宏对话框。

![](images/Macros.png ) 
*宏对话框, 列举了系统中存在的宏*


<div class="mw-translate-fuzzy">

您可以管理您的宏：删除、编辑、复制、安装，或者从头创建一个新的宏。如果您要编辑一个宏，它便会在编辑器窗口中打开，在此就可以修改其代码。可以用{{button|Addons...}}按钮来安装一个新的宏，它将跳转至[Addon Manager](Std_AddonMgr.md)。


</div>


<div class="mw-translate-fuzzy">

## 示例

按下记录按钮，指定宏的名称，这里设置为\"cylinder 10x10\"，接下来，在[零件工作台中创建一个半径为](Part_Workbench.md)10且高为10的圆柱体。随后按下\"stop recording（停止记录）\"按钮。在编辑宏对话框中，您可以看到刚刚记录的python代码，如有需要就对代码进行调整。要执行编辑器中的宏的时候，只需简单地按下工具栏中的执行按钮即可。您制作的宏将一直存于硬盘，因此，您做的任意更改、或所创的新宏总能在下次开启FreeCAD时继续使用。


</div>

Press the record button, give a name, let\'s say \"cylinder 10x10\", then, in the [Part Workbench](Part_Workbench.md), create a cylinder with radius = 10 and height = 10. Then, press the \"stop recording\" button. In the edit macros dialog, you can see the python code that has been recorded, and, if you want, make alterations to it. To execute your macro, simply press the execute button on the toolbar while your macro is in the editor. You macro is always saved to disk, so any change you make, or any new macro you create, will always be available next time you start FreeCAD.


<div class="mw-translate-fuzzy">

## 自定义

诚然，我们不可能为了使用宏而每次都将其先加载至编辑器中。FreeCAD提供了更便捷的方式令您使用宏，例如为之添加快捷键，或将它加入菜单作为其中的一个选项。只要创建好宏，一切有关的操作都可通过**Tools → Customize**菜单来实现。


</div>

Of course it is not practical to load a macro in the editor in order to use it. FreeCAD provides much better ways to use your macro, such as assigning a keyboard shortcut to it or putting an entry in the menu. Once your macro is created, all this can be done via the **Tools → Customize** menu.

![](images/Macros_config.jpg )


<div class="mw-translate-fuzzy">

借助[自定义工具栏可使您的宏成为像其他FreeCAD标准工具那样的实体工具](Customize_Toolbars.md)。这样，既可将python脚本强大的功能添加至FreeCAD中，又能令您方便地把自己制作的工具加入到界面中。如果您希望了解更多关于[Python脚本的信息](Python.md)，请阅读[Scripting页面](Scripting.md)。


</div>

See [Customize Toolbars](Customize_Toolbars.md) for a more detailed description.


<div class="mw-translate-fuzzy">

## 通过非记录的方式来创建宏

[如何安装宏](How_to_install_macros.md) 您也可以通过不记录GUI动作，而直接复制/粘贴python代码的方式来创建宏。即，简单地创建一个新的宏，对它进行编辑，并粘贴您自己的代码。最后再以保存FreeCAD文档的方式来保存宏。当下一次开启FreeCAD的时候, 此宏将位列宏菜单中的\"Installed Macros\"项下。


</div>

You can also directly copy/paste python code into a macro, without recording GUI action. Simply create a new macro, edit it, and paste your code. You can then save your macro the same way as you save a FreeCAD document. Next time you start FreeCAD, the macro will appear under the \"Installed Macros\" item of the Macro menu.

See [How to install macros](How_to_install_macros.md) for a more detailed description.


<div class="mw-translate-fuzzy">

## 众宏之库

您可以光临[Macros recipes页面来挑选需要的宏](Macros_recipes.md)，并将它添加至FreeCAD中进行安装。


</div>

There are two main places for macros. The first one is the official peer-reviewed macro repository on [GitHub](https://github.com/FreeCAD/FreeCAD-macros). The second one is the [Macros recipes](Macros_recipes.md) page from which you can pick some useful macros to add to your FreeCAD installation. Macros from both repositories can be installed via the [Addon Manager](Std_AddonMgr.md) directly from FreeCAD.


<div class="mw-translate-fuzzy">

## 链接

[安装更多的工作台](Installing_more_workbenches.md)。


</div>

-   [Automatically run macro at startup](Macro_at_Startup.md)
-   [Installing more workbenches](Installing_more_workbenches.md)


<div class="mw-translate-fuzzy">

## 教程

[如何安装其他的工作台](How_to_install_additional_workbenches.md)。


</div>

You can manually install extensions, however, it is much simpler to just use the [Addon Manager](Std_AddonMgr.md).

-   [How to install macros](How_to_install_macros.md)
-   [How to install additional workbenches](How_to_install_additional_workbenches.md)



---
![](images/Button_right.svg) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > [Python Code](Category_Python Code.md) > [Macros](Category_Macros.md) > Macros/zh-cn
