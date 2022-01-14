# The FreeCAD source code/zh-cn
[FreeCAD的源代码](https://github.com/FreeCAD/FreeCAD)通过Git管理，是公开的，是开放的，是可获得的，声明于[LGPL许可协议](https://en.wikipedia.org/wiki/GNU_Lesser_General_Public_License)之下。任何人都可以复制、下载、阅读、分析、分发和改动。如果你改了代码，还想看到它被吸收进官方代码里，我们要给你提个醒，你的改动需要被FreeCAD开发者认可。所以，聪明的做法是，先到[论坛](http://forum.freecadweb.org)上去发帖，跟大家讨论一下，说说你的初衷和想法。免得到头来，出乎你的意料，你的改动被拒绝。

如果你有兴趣，深入探索FreeCAD源代码，下面就是一些提醒，一点信息，帮助你走上正轨。

-   FreeCAD代码主要采用**C++**编程，但是重度依赖**Python**。FreeCAD的功能里，非常大的部分都提供相应的Python包装。FreeCAD的核心哲学之一，就是对任何C++开发的新属性，都要给出Python接口。为此，FreeCAD通篇都重度使用CPython（Python自己提供的C界面工具），特别是[PyCXX](http://cxx.sourceforge.net/)。FreeCAD代码里也提供了很多模版和定制工具，便于你包装相应的Python封装。FreeCAD一些更高层的部分，完全是用Python写的代码。


<div class="mw-translate-fuzzy">

-   FreeCAD的源代码完全**跨平台**，我们一直很小心，保证让大家在最广泛的平台上和配置上都能使用此应用，避免让用户感觉不爽。因此，如果一个所需组件的新版本不能跨平台，不能广泛而容易地在所有平台上使用，那会是我们的错，我们将尽可能地避免这样的情况放生。同时，保证向后兼容性（用旧版本的FreeCAD也能打开新版本所创建的文件）也有重要的优先级。


</div>

-   FreeCAD的几乎所有功能都分成了两部分，称为**App**和**Gui**。在源代码文件结构中，处处体见着这种分割。App包含所有的功能性东西，它们需要在纯控制台模式（无用户图形界面）运行。既然FreeCAD可以编译后，在没有用户图形界面的情况下运行，App里的代码就得独立于任何GUI相关库。Gui包含那些App功能的外围的代码，在GUI模式运行。


<div class="mw-translate-fuzzy">

-   FreeCAD的大多数功能都通过**模块**来实现。不含模块的FreeCAD只是一个容器，是一个只能打开和保存文件的窗口。所有的几何工具和工作台都实现在模块里。模块有的是C++写的，有的是Python，或者融合两个世界的菁华，用C++和Python制成混合动力的模块。其中实体性和关键性的功能通过C++编程，而终端工具用Python打造，从而更便于FreeCAD的用户扩展和适配。每个模块用于GUI模式时，通常会在FreeCAD接口中，定义并创建一个**工作台**，一般用同样的名字。但是并不强制要求模块包含一个工作台。


</div>


<div class="mw-translate-fuzzy">

-   FreeCAD的模块常常**依赖于其他模块**。大多数使用实体几何的模块依赖于**Part**模块。它是FreeCAD最基础的模块，用OpenCasCade实现了大部分接口。虽然其它模块也可以直接调用OpenCasCade的功能，它们通常不那么做，而是调用Part提供的更高层次的函数。


</div>

-   模块总是从Python**初始化**。即使它们完全是C++写的，它们总是至少包含一小段Python/CPython的结构。


<div class="mw-translate-fuzzy">

-   FreeCAD使用**其他开源库**，堪称求贤若渴。Python和Qt，用在核心和几乎所有模块中。除了它们，还有两个重度使用的库，也几乎到处可见。它们是[OpenCasCade Technology](https://en.wikipedia.org/wiki/Open_Cascade_Technology)和[Coin3D](http://www.coin3d.org/)。FreeCAD创建和管理所有的实体几何，采用了OpenCasCade；而管理3D视图，采用了coin3D。OpenCasCade主要用在App世界，而coin3D更多用于Gui世界。要用FreeCAD做任何几何相关的工作，都需要基本理解OpenCascade，这是基础。特别的模块当然采用特别的库。除了要求这些库在所有平台上都容易获得，通常没有什么其他限制。所以可以想见，一个全副武装的FreeCAD，它的依赖库列表，那将是相当庞大的阵容。


</div>


<div class="mw-translate-fuzzy">

-   FreeCAD的**文档对象**，就是FreeCAD文档中包含的所有对象。在GUI界面，它们出现在Tree View中；在Python控制台，它们可以通过FreeCAD.ActiveDocument.Objects()调用。对几何数据，文档对象可以有，也可以没有；在3D视图中，文档对象可以显示，也可以什么也不显示。文档对象总是被划分为App和Gui两部分。在控制台模式时，就不加载Gui那部分；标准的几何对象，比如Part或Part Design里的那些，有其对应的App中定义的几何体，基于OpenCasCade。而其对应的Gui（通常也被称为\"View Provider\"），负责创建那个几何体的coin3D外观，用来插入coin3D的主场景图，实现3D观看。


</div>

-   源代码的基本文件夹结构如下：
    -   **App**：包含FreeCAD的控制台模式应用。它定义了基本结构，它也为文档对象定义基础类。这些类被各个模块继承，用于创建各自的类。
    -   **Base**：包含FreeCAD里到处都用得到的核心功能性东西：3D向量，单位，矩阵，位置，等等。
    -   **Gui**：包含FreeCAD在GUI模式下的应用。它定义3D视图，也包含很多工具和函数，被工作台调用，用来与接口和3D视图互动。它为视图提供者定义基础类。
    -   **Doc**：包含一个文件，从这个wiki生成的Qt帮助文件，是一个大全。
    -   **Mod**：包含所有的模块。它们本身又进一步分割为App和Gui（除了python模块，它们并不总是清晰地遵从那条约定）。


<div class="mw-translate-fuzzy">

### 相关的东西

-   [源代码管理](Source_code_management/zh-cn.md)
-   [发烧友中心里面又很多文档](Power_users_hub/zh-cn.md)，它们关于模块，关于OpenCasCade，关于Coin3D，主要是写给Python程序员。虽然如此，因为功能性都是相通的，这些页面对C++程序员也有助益。


</div>

[<img src="images/Property.png" style="width:16px"> Developer Documentation](Category_Developer_Documentation.md)

---
[documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > The FreeCAD source code/zh-cn
