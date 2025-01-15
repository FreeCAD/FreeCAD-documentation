# Manual:Installing/zh-cn
{{Manual:TOC}}


<div class="mw-translate-fuzzy">

FreeCAD 使用 [LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License) 许可证；无论您是商业用途还是非商业用途，您都可以根据自己的需求下载、安装、分发和使用 FreeCAD。您不受任何条款或限制的约束，您使用 FreeCAD 生成的文件完全属于您自己。唯一真正禁止的事情就是声称您自己编写了 FreeCAD！


</div>


<div class="mw-translate-fuzzy">

FreeCAD 在 Windows、Mac OS 和 Linux 上表现相同。然而，安装 FreeCAD 的方式因平台而异。在 Windows 和 Mac 上，FreeCAD 社区提供了预编译的软件包（安装程序），可以直接下载；而在 Linux 上，FreeCAD 的源代码可供 Linux 发行版维护人员使用，他们负责将 FreeCAD 打包为适用于特定发行的版本。因此，在 Linux 上，通常可以直接从软件管理器应用程序安装 FreeCAD。


</div>


<div class="mw-translate-fuzzy">

适用于 Windows 和 Mac OS 的官方 FreeCAD 下载页面是 <https://github.com/FreeCAD/FreeCAD/releases>


</div>

**FreeCAD 版本**


<div class="mw-translate-fuzzy">

您在上述引用页面和您所使用的发行版软件管理器中找到的官方 FreeCAD 发布版本是稳定版本。然而，FreeCAD 的开发非常迅速！几乎每天都会添加新功能和修复错误。由于稳定版本发布之间的时间通常较长，您可能有兴趣尝试更先进的 FreeCAD 版本。这些开发版本或预发布版本会不时地上传到上述的 [下载页面](https://github.com/FreeCAD/FreeCAD/releases)，或者，如果您使用的是 Ubuntu 或 Fedora，FreeCAD 社区还维护着 [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily)（个人软件包存档）和 [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) 的 \'daily builds\'（每日构建），这些版本会定期更新，包含最新的更改。


</div>


<div class="mw-translate-fuzzy">

如果您在虚拟机中安装 FreeCAD，请注意由于大多数虚拟机对 [OpenGL](https://en.wikipedia.org/wiki/OpenGL) 的支持限制，性能可能会很差（在某些情况下甚至无法使用）。


</div>



### 在 Windows 上安装 


<div class="mw-translate-fuzzy">

1.  从 [download page](https://github.com/FreeCAD/FreeCAD/releases) 下载与您的 Windows 版本（32位或64位）对应的安装程序（.exe）包。FreeCAD 的安装程序应适用于从 Windows 7 开始的任何版本。
2.  双击下载的安装程序。
3.  接受 LGPL 许可的条款，这将是您可以放心点击 \"accept\" 按钮而不阅读文本的少数情况之一。没有隐藏条款: ![](images/Freecad-windows-install-01.jpg )
4.  您可以保留默认路径，或者根据需要进行更改: ![](images/Freecad-windows-install-02.jpg )
5.  除非您计划进行一些高级的 Python 编程，否则无需设置 PYTHONPATH 变量。如果决定要改，您可能已经了解它的用途: ![](images/Freecad-windows-install-03.jpg )
6.  在安装过程中，还会安装一些捆绑在安装程序中的其他组件: ![](images/Freecad-windows-install-04.jpg )
7.  完成，FreeCAD 已安装。您可以在开始菜单中找到它: ![](images/Freecad-windows-install-05.jpg )


</div>

**安装开发版本**


<div class="mw-translate-fuzzy">

打包 FreeCAD 并创建安装程序需要一些时间和投入，因此通常提供开发（也称为预发布）版本作为 .zip（或 .7z）存档文件。这些不需要安装，只需解压缩它们，并通过双击其中的 FreeCAD.exe 文件来启动 FreeCAD。这还允许您将稳定版本和"不稳定"版本同时保存在同一台计算机上。


</div>



### 在 Linux 上安装 


<div class="mw-translate-fuzzy">

在大多数现代 Linux 发行版（如 Ubuntu、Fedora、openSUSE、Debian、Mint、Elementary 等）上，可以通过点击按钮直接从发行版提供的软件管理应用程序进行安装 FreeCAD（它的外观可能与下面的图示不同，每个发行版使用自己的工具）。


</div>


<div class="mw-translate-fuzzy">

1.  打开软件管理器并搜索 \"freecad\"：
    <img alt="" src=images/Freecad-linux-install-01.jpg  style="width:800px;">
2.  单击 \"安装\" 按钮，这样就安装了 FreeCAD。别忘了随后给它评分！
    <img alt="" src=images/Freecad-linux-install-02.jpg  style="width:800px;">


</div>

**其他方式**


<div class="mw-translate-fuzzy">

使用 Linux 的一大乐趣在于定制软件的多种可能性，所以不要限制自己。在 Ubuntu 及其衍生版上，还可以从由 FreeCAD 社区维护的 [PPA](https://launchpad.net/~freecad-maintainers) 安装 FreeCAD（包含稳定版和开发版）。在 Fedora 上，可以从 [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) 安装最新的 FreeCAD 开发版本。由于这是开源软件，您还可以轻松地 [自己编译 FreeCAD](Compiling.md)。


</div>



### 在 Mac OS 上安装 

在 Mac OSX 上安装 FreeCAD 现在和其他平台一样简单。 但是，由于社区中拥有 Mac 的人数较少，因此可用的软件包有时会落后于其他平台的版本。


<div class="mw-translate-fuzzy">

1.  从 [下载页面](https://github.com/FreeCAD/FreeCAD/releases)下载与您的版本相对应的压缩包。
2.  打开"下载"文件夹，并展开下载的 zip 文件：![](images/Freecad-mac-01.jpg )
3.  将 zip 文件内的 FreeCAD 应用程序拖动到"应用程序"文件夹中：![](images/Freecad-mac-02.jpg )
4.  完成，FreeCAD 已安装！![](images/Freecad-mac-03.jpg )
5.  如果系统因为应用程序不来自 App Store 而阻止 FreeCAD 的启动，您需要在系统设置中启用它：![](images/Freecad-mac-04.jpg )


</div>



### 卸载


<div class="mw-translate-fuzzy">

希望您不需要卸载 FreeCAD，但了解如何卸载也没错。在 Windows 和 Linux 上，卸载 FreeCAD 非常简单。在 Windows 上，使用控制面板中的标准"卸载软件"选项；在 Linux 上，使用您用于安装的软件管理器进行卸载。在 Mac OS 上，只需从应用程序文件夹中将其删除即可。


</div>



### 设置基本偏好选项


<div class="mw-translate-fuzzy">

一旦安装了 FreeCAD，您可能想要打开它并更改一些偏好设置。在 FreeCAD 中，偏好设置位于菜单 **编辑 → 偏好设置** 下。下面列出了一些您可能希望更改的基本设置；您可以浏览偏好设置页面，看是否还有其他您想要更改的内容。


</div>

#### General category, General tab 

![](images/FreeCAD_022_GeneralGen.png )

1.  **Language**: By default, FreeCAD will select your operating system\'s language, but you have the option to change it. Thanks to the dedication of many contributors, FreeCAD is available in a wide array of languages.
2.  **Units**: This setting allows you to choose the default units system for your projects.

#### General category, Document tab 

![](images/FreeCAD_022_GeneralDoc.png )

1.  **Create a new document at startup**: FreeCAD will automatically open a new document each time the program starts.
2.  **Storage options**: Configure settings here to help you recover your work in the event of a crash.
3.  **\'Authoring and license**\': In this area, you can determine the settings for new files. To facilitate sharing, consider starting with a more permissive, copyleft license like Creative Commons.

#### Display category, Navigation tab 

![](images/FreeCAD_022_DisplayNav.png )

1.  **Zoom at cursor**: When enabled, zoom actions center on the mouse cursor. If disabled, zoom focuses on the center of the view.
2.  **Invert zoom**: This option reverses the zoom direction in relation to mouse movement.

#### Workbenches tab 

![](images/FreeCAD_022_WBMenu.png )

Although FreeCAD typically opens to the start page, this setting lets you bypass it. You can start directly in your preferred workbench. Additionally, you can customize which workbenches are displayed in the selector menu.

#### Import-Export tab 

![](images/FreeCAD_022_ImportExport.png )

Here, define basic parameters for importing and exporting in various formats.



### 安装其他内容


<div class="mw-translate-fuzzy">

随着 FreeCAD 项目和其社区的快速发展，以及其易于扩展的特性，社区成员和其他爱好者开始在互联网上推出各种外部贡献和附加项目。这些外部项目中的大部分是工作台或宏，可以通过 FreeCAD 菜单 "Tools" 下的 [附加组件管理器](Std_AddonMgr.md) 直接安装。附加组件管理器将允许您安装许多有趣的组件，例如：


</div>

![](images/FreeCAD_022_AddonsMenu.png )


<div class="mw-translate-fuzzy">

1.  [部件库](https://github.com/FreeCAD/FreeCAD-library)，包含由 FreeCAD 用户创建的各种有用模型，或模型的一部分，可以自由在您的项目中使用。该库可以直接从您的 FreeCAD 安装中使用和访问。
2.  [Additional workbenches](https://github.com/FreeCAD/FreeCAD-addons)，扩展了 FreeCAD 的功能，用于特定任务，例如为您的模型的部分或区域添加动画效果，如板金折叠或 BIM。关于每个附加工作台及其包含的工具的更多解释可以在附加组件管理器上的各个附加组件页面中找到，您可以通过点击相应链接访问它们。
3.  一组 [宏](https://github.com/FreeCAD/FreeCAD-macros)，这些宏也可以在 [FreeCAD 维基](Macros_recipes.md) 上找到，并提供了关于如何使用它们的文档。


</div>


<div class="mw-translate-fuzzy">

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">


</div>

**延伸阅读**

-   [更多下载选项](Download.md)
-   [FreeCAD PPA（适用于 Ubuntu）](https://launchpad.net/~freecad-maintainers)
-   [FreeCAD 附加组件 PPA（适用于 Ubuntu）](https://launchpad.net/freecad-extras)
-   [自行编译 FreeCAD](Compiling.md)
-   [FreeCAD 翻译](https://crowdin.com/project/freecad)
-   [FreeCAD GitHub 页面](https://github.com/FreeCAD)
-   [FreeCAD 附加组件管理器](Std_AddonMgr.md)



---
⏵ [documentation index](../README.md) > [Poweruser Documentation](Category_Poweruser%20Documentation.md) > [Tutorials](Category_Tutorials.md) > Manual:Installing/zh-cn
