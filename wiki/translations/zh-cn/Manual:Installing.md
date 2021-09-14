# Manual:Installing/zh-cn




<div class="mw-translate-fuzzy">





</div>


{{Manual:TOC}}

FreeCAD 使用[LGPL](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)许可证，您可以按照自己的方式自由下载，安装，重新分发和使用 FreeCAD。无论您用它做何种类型的工作 （商业或非商业），都不受任何条款或限制的约束，用它生成的文件完全属于您。许可证唯一禁止的，就是声称您自己编写了 FreeCAD！

FreeCAD 在 Windows，Mac OS 和 Linux 上行为一致。但是，平台不同，安装方式也略有不同。在 Windows 和 Mac 上，FreeCAD 社区提供预编译的软件包（安装程序），可以下载；而在 Linux上，因为源代码提供给了 Linux 发行版的维护人员，后者负责为其特定发行版打包 FreeCAD，所以在 Linux 上，您通常可以直接通过软件管理器安装 FreeCAD。

适用于 Windows 和 Mac OS 的官方 FreeCAD 下载页面是 <https://github.com/FreeCAD/FreeCAD/releases>

**FreeCAD 版本**

在上面引用的页面，以及在 Linux 发行版的软件管理器中找到的 FreeCAD 正式版本是稳定版本。不过，FreeCAD 的开发速度很快，几乎每一天都会添加新功能和修复错误。在两个稳定版本之间通常要花费很长时间，因此您或许有兴趣尝试更加前沿的 FreeCAD 版本。这些开发版本或预发布版本会不时上传到上面提到的[下载页面](https://github.com/FreeCAD/FreeCAD/releases)，或者，如果您使用的是 Ubuntu 或 Fedora，则可以使用它们的专有渠道：FreeCAD 社区还维护着 [PPA](https://launchpad.net/~freecad-maintainers/+archive/ubuntu/freecad-daily)（个人包档案）和 [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/)（社区项目），或者称为"每日构建"，会定期更新。

如果您在虚拟机中安装 FreeCAD，请注意性能可能很差。由于大多数虚拟机上的 [OpenGL](https://en.wikipedia.org/wiki/OpenGL) 支持限制，某些情况下 FreeCAD 可能无法使用。

### 在 Windows 上安装 

1.  从[下载页面](https://github.com/FreeCAD/FreeCAD/releases)下载与您的 Windows 版本（32位或64位）对应的安装程序包（.exe）。FreeCAD 安装程序应该适用于从Windows 7 开始的任何 Windows 版本。
2.  双击下载的安装程序。
3.  接受 LGPL 许可证的条款。你可以真正地，安全地点击"接受"按钮，而不阅读文本吗？这次是少有的情况：没有隐藏条款。![](images/Freecad-windows-install-01.jpg )
4.  你可以在此处保留默认路径，也可以根据需要进行更改。![](images/Freecad-windows-install-02.jpg )
5.  除非你打算做一些高级的 python 编程，否则不需要设置 PYTHONPATH 变量。如果你要改，说明你可能已经知道这是干什么的了。![](images/Freecad-windows-install-03.jpg )
6.  在安装过程中，还将安装一些附加组件，这些组件捆绑在了安装程序中。![](images/Freecad-windows-install-04.jpg )
7.  FreeCAD 就这样安装好了，可以在开始菜单中找到它。![](images/Freecad-windows-install-05.jpg )

**安装开发版本**

因为打包 FreeCAD 并创建安装程序需要一些时间和奉献精神，通常开发（也称为预发布）版本以.zip（或.7z）压缩文档的形式提供。无需安装，只要解压缩后，双击在里面找到的 FreeCAD.exe 文件，就可以启用 FreeCAD 了。这样你便可以将稳定版本和"不稳定"版本保存在了同一台计算机上。

### 在 Linux 上安装 


<div class="mw-translate-fuzzy">

在大多数现代 Linux 发行版（Ubuntu，Fedora，OpenSUSE，Debian，Mint，Elementary等）上，可以直接在发行版提供的软件管理应用程序中一键安装 FreeCAD（有些方面可能与下面的图片不同，每个发行版使用专有的工具）。


</div>

1.  打开软件管理器，搜索"freecad"；

![](images/Freecad-linux-install-01.jpg )

1.  单击"安装"按钮，等一会 FreeCAD 就安装好了。不要忘记使用以后给个评价！
    ![](images/Freecad-linux-install-02.jpg )

**其他方式**

使用 Linux 的一大乐趣是有多种可能来定制软件，不用束缚自己。在 Ubuntu 及其衍生产品上，FreeCAD 也可以从FreeCAD 社区维护的 [PPA](https://launchpad.net/~freecad-maintainers) 安装（它包含稳定版和开发版）。在 Fedora 上，可以从 [copr](https://copr.fedorainfracloud.org/groups/g/freecad/coprs/) 安装 FreeCAD 的最新开发版本。因为 FreeCAD 是开源软件，也可以[自己轻松编译 FreeCAD](Compiling/zh-cn.md)。

### 在 Mac OS 上安装 

在 Mac OSX 上安装 FreeCAD 现在和其他平台一样简单。 但是，由于社区中拥有 Mac 的人数较少，因此可用的软件包有时会落后于其他平台的几个版本。

1.  从[下载页面](https://github.com/FreeCAD/FreeCAD/releases)下载与您的版本对应的压缩包。
2.  打开"下载"文件夹，然后展开下载的 zip 文件。![](images/Freecad-mac-01.jpg )
3.  将 FreeCAD 应用程序从 zip 内拖到 Applications 文件夹。![](images/Freecad-mac-02.jpg )
4.  就是这样，你安装了FreeCAD！![](images/Freecad-mac-03.jpg )
5.  如果由于对来自 App Store 的应用程序的权限受限，系统阻止 FreeCAD 启动，则需要在系统设置中启用它。![](images/Freecad-mac-04.jpg )

### 卸载

希望您不想卸载 FreeCAD，但知道如何做也无妨。 在 Windows 和 Linux 上，卸载 FreeCAD 非常简单。在Windows 上，使用控制面板中的标准"删除软件"选项; 在 Linux 上，使用您用于安装它的相同软件管理器将其删除。 在 Mac OS 上，只需将其从 Applications 文件夹中删除即可。

### 设置基本首选项

安装 FreeCAD 后，您可能想要打开它并更改一些首选项。 FreeCAD 中的首选项设置位于菜单"编辑 → 首选项"下。下面列出了一些您可能希望更改的基本设置。您可以浏览首选项页面，来查看是否还有其他要更改的内容。

1.  **语言**: （"常规"类别， "常规"选项卡）FreeCAD 将自动选择操作系统的语言，但您可能想要更改它。FreeCAD 几乎完全翻译成了五六种语言，其它语言版本目前只是部分翻译。您可以轻松地[帮助翻译 FreeCAD](https://crowdin.com/project/freecad)。
    ![](images/Freecad-basic-options01.jpg )
2.  **自动加载模块**: （"常规"类别，"常规"选项卡）通常，FreeCAD 将首先显示起始页面。您可以跳过这个并直接在您选择的工作台中开始 FreeCAD 会话，在"启动"下列有"启动后自动加载模块"。 [工作台将在](Workbenches/zh-cn.md)[下一章中详细说明](Manual:The_FreeCAD_Interface/zh-cn.md)。
3.  **在启动时创建新文档**: （"常规"类别，"文档"选项卡）结合上面的自动加载模块选项，如果选中，则启动 FreeCAD 开始工作。
    ![](images/Freecad-basic-options02.jpg )
4.  **存储选项**: （"常规"类别， "文档"选项卡）与任何复杂的应用程序一样，FreeCAD 可能包含导致其偶尔崩溃的错误。在这里，您可以配置选项，以帮助您在崩溃时恢复工作。
5.  **著作和许可**: （"常规"类别，"文档"选项卡）在此处设置所创建的新文件的要用的值。你可以考虑使用像 [Creative Commons](https://creativecommons.org/) 这样友好的 [copyleft](https://en.wikipedia.org/wiki/Copyleft) 许可证，从一开始就使您的文件可以共享。
6.  **重定向内部 python 消息**: （"常规"类别，"输出窗口"选项卡）这两个选项最好总是勾选，因为当运行 python 脚本时出现问题时，它们会让内部 python 解释器的消息显示[报表视图中](Manual:The_FreeCAD_Interface#Report_view/zh-cn.md)。
    ![](images/Freecad-basic-options03.jpg )
7.  **单位**: （"常规"类别，"单位"选项卡）您可以在此处设置要使用的默认单位系统。
    ![](images/Freecad-basic-options04.jpg )
8.  **在光标处缩放**: （"显示"类别，"3D"选项卡）如果设置，缩放操作将聚焦在鼠标指针处。如果未设置，则当前视图的中心是变焦焦点。
9.  **反转缩放**: （"显示"类别，"3D"选项卡）缩放方向与鼠标移动的方向相反。
    ![](images/FreeCAD-v0-18-Preferences-Display.png )

### 安装其他内容

因为 FreeCAD 项目及其社区的快速发展，也因为它易于扩展，社区成员和其他爱好者所做的外部贡献和周边项目在互联网各处出现。这些外部项目中的大多数都是工作台或宏，可以通过菜单"Tools"下的"[插件管理器](AddonManager/zh-cn.md)"轻松安装在 FreeCAD 中。插件管理器允许您安装许多有趣的组件，例如：

1.  [零件库](https://github.com/FreeCAD/FreeCAD-library)，包含 FreeCAD 用户创建的各种有用模型或模型片段，可以在项目中自由使用。你可以在 FreeCAD 安装包中使用和访问该库。
2.  [其他工作台](https://github.com/FreeCAD/FreeCAD-addons)，可以扩展 FreeCAD 的功能，用于某些特定任务，例如将模型的某些部件做成动画，或者用于某些特定领域，例如钣金折叠或 BIM。每个工作台的进一步说明及其包含的工具在每个插件页面上有说明，您可以通过单击插件管理器上的相应链接访问该页面。
3.  [一组宏](https://github.com/FreeCAD/FreeCAD-macros)，也可以[在 FreeCAD 维基上找到](Macros_recipes.md)，还有关于如何使用它们的文档。

<img alt="" src=images/FreeCAD-addon-manager01.jpg  style="width:800px;">

如果您使用的是 Ubuntu 操作系统，上面的一些插件也可作为 [FreeCAD 插件 PPA](https://launchpad.net/freecad-extras) 上的软件包提供。

**延伸阅读**


<div class="mw-translate-fuzzy">

-   [更多下载选项](Download/zh-cn.md)
-   [详细的安装说明](Installing/zh-cn.md)
-   [适用于 Ubuntu 的 FreeCAD PPA](https://launchpad.net/~freecad-maintainers)
-   [用于 Ubuntu 的 FreeCAD 插件 PPA](https://launchpad.net/freecad-extras)
-   [自己编译 FreeCAD](Compiling/zh-cn.md)
-   [翻译 FreeCAD](https://crowdin.com/project/freecad)
-   [FreeCAD github 页面](https://github.com/FreeCAD)
-   [FreeCAD 插件管理器 ](AddonManager/zh-cn.md)


</div>


<div class="mw-translate-fuzzy">





</div>

[Category:Poweruser Documentation](Category:Poweruser_Documentation.md) [Category:Tutorials](Category:Tutorials.md)
