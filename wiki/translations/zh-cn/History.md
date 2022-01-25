# History/zh-cn
\_\_FORCETOC\_\_


<div class="mw-translate-fuzzy">

## 发展历史

<img alt="Early FreeCAD version unknown" src=images/Screenshot_mesh.jpg  style="width:300px;"> <img alt="FreeCAD version 0.7 from 2009" src=images/Part_BooleanOperations.png  style="width:300px;">


</div>


<div class="mw-translate-fuzzy">

FreeCAD的发展历史可以从2001年1月讲起。那时[Jürgen Riegel开始为Cas](User_Jriegel.md).CADE项目工作。这个项目是一个商用软件开发框架。它包括一个[几何建模内核](Glossary/zh-cn#Geometric_modeling_kernel.md)（或者叫CAD内核）。这个内核在2000年发布于一个开源协议之下，并更名为[开放的小瀑布](Glossary#Open_CASCADE.md)(缩写CAS.CADE的原意：为计算机辅助设计和工程服务的计算机辅助软件)。这就使得开发一个开源的3D CAD软件成为可能，因为非得自己从头开始编织CAD内核将会耗费巨大的工作量。


</div>

用Jürgen自己的话来说：


{{Quote|text=''我在2001年1月开启的FreeCAD项目，当时称为GOM(图形对象建模者)，想法就是利用Qt、Python和Cas.CADE来实现。Cas.CADE是我在戴姆勒的项目上用到的一个商用CAD内核。Cas.CADE不久前开源了，所以貌似时机刚刚好，尝试进入当时还是空白的开源CAD领域。我在一个叫做QSpect的项目里有两年经验，最终变成了它的主软件设计师。这个项目使用OpenCascade，关于3D和CAD程序，我学到了很多。我也收到Catia V5的影响，尤其是它非常特别的用户和程序界面。2002年3月，在OpenCascade项目里，我注册了FreeCAD这个软件。我不大懂名字的事情，没法想出比FreeCAD更好的名字了。在2003年四月，我在QSpect项目里的同事Werner Meyer，他换到了一个叫Imetric的公司。与Imetric的接触很有收获，因为他们正在为自己的3D传感器寻找一个新的3D软件平台。2005年，Imetric把它大部分的Mesh模块捐赠给FreeCAD和开源社区，并将FreeCAD作为他们的传感器系统软件的基础。从那时起，Werner Meyer是FreeCAD非常活跃的开发者。2005年，经过一年的挣扎，我决定脱离OpenCascade的文档框架，改为由自己实现。所以，最终，我们只用了OpenCascade的CAD内核，而没有采用其余框架。2007年是另一个有趣的里程碑。我们接上了QT4，然后，接上了LGPL。那时我们做了很多工作，主要是Werner。"

|sign=[Jürgen Riegel](User:Jriegel/zh-cn.md)|source=''[http://forum.freecadweb.org/viewtopic.php?f=8&t=295 谁站在FreeCAD背后?]
"}}


<div class="mw-translate-fuzzy">

这个项目2003年在[OpenCascade论坛](http://www.opencascade.org/org/forum)上发布给公众。我们再看看Jürgen的话：


</div>


<div class="mw-translate-fuzzy">


{{Quote|text=''大家好，我叫Juergen Riegel，今天我想发布一个OpenCasCade项目，FreeCAD。它是基于OpenCasCade、QT和Python的开源CAx RAD。它的功能实现了一些关键概念，比如录制宏，工作台。它有作为服务器运行的能力，还可以作为能动态装载的应用的扩展。它被设计成了不局限于某个系统平台。尽管它处于早期阶段，对用户和开发者都还不可用——计划于2003年底向用户发布第一版——我想要在设计上和方向上得到一些反馈（所以把它发布出来）。GUI近乎完成了，现在我和我的合作开发者Werner Mayer，已经开始加入第一个CAD功能。FreeCAD可以看作是一个通用目的的机械CAD系统，但是它的第一批受众，我想，将是CAx的开发者，他们需要为自己的工程找到一个地基。''
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http://www.opencascade.org/org/forum/thread_6572/?forum=11 发布FreeCAD项目]''}}


</div>

### Werner Mayer 

Werner Mayer joined the project as soon as it was announced as an open source project (prior to the announcement the project was a private project of Jürgen). See this forum post from Werner in German: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>


<div class="mw-translate-fuzzy">

渐渐地，这个项目获得了关注，社区里有新的关键贡献者加入进来。


</div>

-   **Linux beginning**


{{Quote|text=''A fun fact is that he wanted to have an open-source CAD software mainly for Linux because at that time there existed actually nothing for this platform. However, from the beginning on we exclusively developed on Windows for the next 1.5 years. Then a Czech guy made a contribution to make the code of the core build on Linux: https://github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Half a year later I continued the Linux build: https://github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**Q:** Could you share how that first 1.5 years went? Were you meeting in person or online?


{{Quote|text=''Well, at that time we were colleagues (until 2005) so we could discuss things face to face. After that time we still had some personal meetings but discussed most things by email or phone.''}}


{{Quote|text=''As third core developer Yorik joined around end of 2007 but it took another 3 or 4 years until the community and number of contributors started to grow significantly.''}}

**Q:** Did you divide the tasks or work on competing implementations?


{{Quote|text=''Yes. Jürgen was designing and implementing most of the application and document logic and I was doing the basics of the GUI.''}}


{{Quote|text=''However, this wasn't a gradual process but we have experimented with many things at the beginning. For example, in the initial version we used OCC's document framework OCAF and its viewer but after a year or two we got into a dead end because documentation about OCC was very poor and we couldn't get it to work to extend OCAF with our own feature types. So, we decided to only use OCC's modeling capacities but develop our own application/document framework.''}}

**Q:** At the time did you think FreeCAD would be where it is today?


{{Quote|text=''We didn't know but we hoped. Of course we couldn't anticipate how exactly FreeCAD will look today.<br>The most important design decisions were to make it available on all major platforms and make the whole SW as accessible as possible, i.e. to impose all important functions to Python so that (power) users are able to extend FreeCAD with own functions. This way we hoped to get a broad audience.''}}

(See this forum post from Werner [Re: FreeCAD History](https://forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))


<div class="mw-translate-fuzzy">

[Yorik van Havre](User_Yorik.md)2008年加入了这个项目，开始工作于[绘图模块](Draft_Workbench/zh-cn.md)。在那之前，用户没法通过[用户图形界面创建两维几何体](Glossary/zh-cn#GUI.md)。这个模块完全采用Python开发，而不是C++，后者是FreeCAD采用的核心编程语言。这就证明了Python集成的成功，它可以用来扩展FreeCAD的能力或定制FreeCAD。Yorik除了制图模块，还致力于扩展FreeCAD的文档，并成了FreeCAD实际意义上的艺术总监，因为他为FreeCAD的用户图形界面创作出很多图标，[定义了它的风格](Artwork/zh-cn.md)。


</div>

FreeCAD的0.7版在2009年4月发布。它第一次包含了绘图模块。零件模块提供了一个简单的[CSG建设性实体几何元素工作流程](Glossary/zh-cn#Constructive_Solid_Geometry.md)，先创建基础形状，然后通过零件菜单，对他们做布尔运算。它也有一些扩展，可以实现2D轮廓和倒角操作。

····2009年7月发布的0.8版中，可以看到制图模块的更多功能，包括新的尺寸工具。零件模块有了新的工具条，还有新的工具：旋转和交并。

到2009年底，FreeCAD被Debian仓库接纳，作为一个Debian包。2010年FreeCAD被加入到了Ubuntu10.04仓库中。


<div class="mw-translate-fuzzy">

2010年7月发布的0.10版引入了[草图模块](Sketcher_Workbench/zh-cn.md)。它创建2D几何体的基础是草图解算器，一个基于约束的解算器。第一版的功能仅限于创建长方形和线。


</div>

In early 2011, taking the opportunity given by the [Launchpad](https://launchpad.net) online platform, the [FreeCAD Maintainers team](https://launchpad.net/~freecad-maintainers) was created to provide fresh stable releases along with daily build packages of FreeCAD to users of the Ubuntu operating system.

Version 0.11 as released in May 2011 and introduced the new Part Design workbench which included tools such as Pad, Pocket, Fillet and Chamfer. The Draft workbench received enhancements and new tools, like BSpline. The Robot workbench featured more GUI tools.

Version 0.12 was released in January 2012 and featured a more complete Sketcher workbench. It included a totally rewritten solver, FreeGCS. It was the result of months of work by the main FreeCAD developers along with newcomers logari81 (who programmed the solver) and mrlukeparry. More tools were added to the PartDesign workbench.

### Enlargement of core developer team 

In April 2019 the team of core developers was expanded: Jürgen, Werner and Yorik were joined by Abdullah, Bernd, sliptonic and WandererFan

## Interesting Posts on the forum 

-   about PartDesignNext and other design decisions: <https://forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   about Forum history: <https://forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   about Project history: <https://forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   about Code history: <https://forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW: initial code checkin was on March 18th in 2002 (may be the birthday?)
-   about Project to be OpenSource: <https://forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   about The release commit history: <https://forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   about Who is behind FreeCAD: <http://forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   about FEM history: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   about FEM mesher history: <https://forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>

## Release history 

#### Overview

  Version   Release name   Release date     Release notes                                         Release commit                                                                            Release branch
       
  0.20      ?              in development   [Release notes 0.20](Release_notes_0.20.md)   [head master](https://github.com/FreeCAD/FreeCAD/commits/master)                          
  0.19      \-             2021-03-20       [Release notes 0.19](Release_notes_0.19.md)   [release commit 0.19](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)   [branch bugfixes 0.19](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-19)
  0.18      \-             2019-03-12       [Release notes 0.18](Release_notes_0.18.md)   [release commit 0.18](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [branch bugfixes 0.18](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17      Roland         2018-04-06       [Release notes 0.17](Release_notes_0.17.md)   [release commit 0.17](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [branch bugfixes 0.17](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16      \-             2016-04-18       [Release notes 0.16](Release_notes_0.16.md)   [release commit 0.16](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [branch bugfixes 0.16](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15      \-             2015-04-08       [Release notes 0.15](Release_notes_0.15.md)   [release commit 0.15](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [branch bugfixes 0.15](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14      \-             2014-07-01       [Release notes 0.14](Release_notes_0.14.md)   [release commit 0.14](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [branch bugfixes 0.14](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13      \-             2013-01-29       [Release notes 0.13](Release_notes_0.13.md)   [release commit 0.13](https://github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [branch bugfixes 0.13](https://github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
  0.12      \-             2011-12-20       [Release notes 0.12](Release_notes_0.12.md)                                                                                             
  0.11      \-             2011-05-03       [Release notes 0.11](Release_notes_0.11.md)                                                                                             
  0.10      \-             2010-07-24                                                                                                                                                       
  0.9       \-             2010-01-16                                                                                                                                                       
  0.8       \-             2009-07-10                                                                                                                                                       
  0.7       \-             2009-04-24                                                                                                                                                       
  0.6       \-             2007-02-27                                                                                                                                                       
  0.5       \-             2006-10-05                                                                                                                                                       
  0.4       \-             2006-01-15                                                                                                                                                       
  0.3       \-             2005-10-31                                                                                                                                                       
  0.2       \-             2005-08-09                                                                                                                                                       
  0.1       \-             2003-01-27                                                                                                                                                       
  0.0.1     \-             2002-10-29       Initial Upload of a version                                                                                                                     

#### Legend

  Color   Version Type
   
          Future release
          Latest preview version
          **Latest version**
          Older version, still supported
          Old version
          

## External Links 

-   [SourceForge Files section](http://sourceforge.net/projects/free-cad/files/)
-   [SourceForge Old Files section](http://sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Announcing FreeCAD Project](http://www.opencascade.org/org/forum/thread_6572/?forum=11) on the OpenCascade forum



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > History/zh-cn
