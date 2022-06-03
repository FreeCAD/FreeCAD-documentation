# Licence/zh-cn
{{TOCright}}

## FreeCAD 中使用的许可证 

FreeCAD有两种不同的许可, 一个用于应用程序本身, 另一个用于文档：

**[Lesser General Public Licence, version 2 or superior (LGPL2+)](wikipedia_LGPL.md)**用于所有FreeCAD的源代码。所谓源代码，即包含于[官方Git仓库](https   *//github.com/FreeCAD/FreeCAD)里的那些。


<div class="mw-translate-fuzzy">

**[Creative Commons Attribution 3.0 License (CC-BY-3.0)](http   *//creativecommons.org/licenses/by/3.0/)**用于http   *//www.freecadweb.org上的文档。


</div>

FreeCAD中的不同组件可以使用不同的许可，有关其详细信息, 请参阅FreeCAD的[debian版权文件](https   *//github.com/FreeCAD/FreeCAD/blob/master/package/debian/copyright)。

## 许可证的影响

下面，用更友好更容易懂的话，解释LGPL对你意味着什么：

#### 所有用户

任何人都可以下载它，使用它，重新分发它，完全免费，没有任何限制。你的那一份FreeCAD真的是你的，就像你用FreeCAD生产的文件一样。你不会隔一阵就被要求更新FreeCAD，也不用改变你对FreeCAD的用法。使用FreeCAD没有绑定，不会把你绑定在任何形式的合同或义务上。FreeCAD的源代码公开，可供检查，这就可以保证它不会发走你的私人数据，保证它不做此类你并不知情的事情。

#### 专业用户

自由使用FreeCAD吧，不管是私人、商业还是机构，FreeCAD可以用于任何目的。任何版本的FreeCAD，都可以在任何地方，无限次地部署和安装。你也可以修改和调整FreeCAD，来满足你自己的目的，没有任何限制。然而，你却不能让FreeCAD的开发者受到非难。使用FreeCAD过程中，可能造成损害或业务损失。开发者并不对此承担责任。

#### 开源软件开发者

你可以把FreeCAD作为基础，开发你自己的应用，或者你可以简单地扩展它，为它创建新的模块。如果你将FreeCAD嵌入到你自己的应用里，你可以选择GPL或LGPL许可，或者与LGPL兼容的其他许可，使你的工作归为所有权软件，或者不归。如果你开发了一个模块，将用作FreeCAD的一个扩展，单丝它里面并不包含FreeCAD的任何代码，那么你就能选择你想要的任何许可。然而，如果你希望你的模块使用者众，最好还是保持与FreeCAD一致，使用LGPL许可。这样你的代码就更容易被将来的模块引用，甚至被FreeCAD本身吸纳。


<div class="mw-translate-fuzzy">

#### 不开源的开发者

你可以把FreeCAD作为你的应用的基础，并不强迫开源你的应用。LGPL许可其实只要求两件简单的事情：1) 清楚地告知你的用户，你的应用里包含FreeCAD，声明FreeCAD使用LGPL许可；2) 清晰地将你自己的应用与FreeCAD组件区分开。这通常有两种实现形式。或者你动态地链接到FreeCAD组件，这样用户就被允许修改它；或者把FreeCAD源代码，还有你带来的修改，让你的用户可以获得。你将从FreeCAD开发者那里得到帮助，只要不是单向索取就好。


</div>


<div class="mw-translate-fuzzy">

#### 文件

上面提到的任何许可，都不针对你用FreeCAD制作的模型和文件。后者不受任何约束，不绑定于任何所有权。你的文件就是你的。你可以在FreeCAD里，通过\"File -\> Project Information\"，为你的文件设置所有者，指定你自己的许可协议。


</div>

## 主开发者的声明

我知道，网上讨论*\"正确\"*的开源协议，占用了互联网带宽的很大部分。所以这里我觉得，FreeCAD应该有这个协议。


<div class="mw-translate-fuzzy">

我选择了[LGPL](http   *//en.wikipedia.org/wiki/LGPL)作为这个项目的许可协议，我知道LGPL的利与弊，我将给你解释一下做这个决定的原因。


</div>

FreeCAD是一个库和一个应用的混合体，所以要求GPL协议就显得太强人所难了。它将阻碍给FreeCAD写商用模块的努力，因为它不允许与FreeCAD的基础库建立链接。你可能会问，为什么要提商用模型？那我们看看Linux，它是个好例子。如果GNU C库采用GPL协议，那它就会阻止链接到非GPL的应用，Linux还会那么成功吗？还有，虽然我热爱Linux的自由，我也想使用非常优秀的NVIDIA 3D图形驱动。NVIDIA不想给出这些驱动的代码，我能理解也能接受这一点。我们都需要为公司工作，需要报酬，或者至少是食物。所以当遵守LGPL的规则，让开源软件和非开源软件和谐共处，对我来说并不是什么不好的事情。我希望看到的是，有个人为FreeCAD写了一个Catia的导入/导出处理器，然后把它免费分发，或者是赚一点钱。我不喜欢强迫他给出太多，超出他想给的。那不好，对他和对FreeCAD来说，都不好。

然而这个决定仅为 FreeCAD 的核心系统做出。每个应用模块的作者都可以做出自己的决定。


{{Quote|Jürgen Riegel|15 October 2006}}







[Category   *Developer Documentation](Category_Developer_Documentation.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Developer Documentation](Category_Developer Documentation.md) > Licence/zh-cn
