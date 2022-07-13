# FreeCAD Managing Expectations/pl
**While we welcome and encourage community growth and participation, demands, emotional rants and wild claims are generally poorly received as our community is made up of many experienced and passionate supporters of FreeCAD who have heard similar statements many times over. If you find a feature lacking, or something which is annoying for you, we highly encourage you to consider getting engaged with the code itself. FreeCAD is largely developed by a relatively small group of talented people who all have day jobs, families and other interests beyond just programming on-demand. If you have the skills (Python/C++) and motivation to participate, your contributions can help make FreeCAD even better than it is today. You can find tracked bugs/feature requests [https   *//github.com/FreeCAD/FreeCAD/issues here].**


{{TOCright}}

## Przeznaczenie

Ta strona wiki jest przeznaczona dla nowych użytkowników programu FreeCAD odchodzących z innych rozwiązań CAD / CAM.

## Opening statement 

Many hobbyists, freelance designers and small businesses often seek refuge from the high costs and licensing restrictions of commercial software, or perhaps you merely choose FreeCAD because you believe in the philosophy behind [FOSS](https   *//en.wikipedia.org/wiki/FOSS). In either case, WELCOME! There are many users, just like you who have successfully made the transition to FreeCAD for their personal and professional needs. This wiki page is designed to help set you on the path to success and establish some realistic expectations while diving into the *FreeCAD Way*, which is most likely quite a bit different from what you may have grown accustomed to with other popular CAD software.

## Czego mogę się spodziewać? 


<div class="mw-translate-fuzzy">

W swoim rdzeniu FreeCAD jest modelerem parametrycznym. Wykorzystuje koncepcję środowisk pracy, gdzie każde środowisko jest odpowiedzialne za konkretne zadania i funkcje. Jako taki może być używany do wielu celów. Jest aktywnie wykorzystywany w produkcji i dość stabilny. Jednak, jak każdy inny program CAD, FreeCAD nie jest w 100% stabilny.


</div>


<div class="mw-translate-fuzzy">

Pochodząc z innego programu CAD, być może będziesz musiał zmienić swój sposób pracy, użyć obejścia lub makra, ale w wielu przypadkach będziesz w stanie osiągnąć to, czego chcesz. A jeśli potrzebujesz pomocy   * mamy bardzo aktywne i responsywne [forum](https   *//forum.freecad.org/index.php) chętne do pomocy. A wśród członków forum na pewno są (byli) użytkownicy Twojego obecnego programu CAD. Więc nie wahaj się skorzystać z tych zasobów.


</div>

## Jak mogę pomóc? 

Jest wiele sposobów   * możesz dokonać [wpłaty](Donate/pl.md), pomóc w pytaniach na [forum](https   *//forum.freecad.org/index.php), albo napisać dokumentację lub kod. Zobacz [Pomoc FreeCAD](Help_FreeCAD/pl.md).

## Learning resources 

### Official

-   [This Wiki](Main_Page.md)
-   [The Help Forum](https   *//forum.freecadweb.org/viewforum.php?f=3)
-   [Workarounds for known problems](Workarounds.md)

### Un-official 

The following YouTube Channels have reasonably good quality content focused around FreeCAD (it is recommended to ignore any tutorials based on version 0.17 or earlier)   *

-   *MangoJelly Solutions* (several beginner, intermediate and advanced video playlists)
-   *Joko EngineeringHelp* (intermediate/advanced videos)
-   *Brodie Fairhall* (A couple of videos helping Fusion 360 users transition to FreeCAD)
-   And more\...

## Questions and answers 

### \"Can FreeCAD do XYZ?\" 

FreeCAD already has the ability to do the following types of work   *

-   Spline-based parametric modeling using the [Part](Part_Workbench.md), [Part Design](PartDesign_Workbench.md) and [Sketcher](Sketcher_Workbench.md) workbenches
-   [Surface](Surface_Workbench.md)/[Curves](Curves_Workbench.md) modeling using NURBS
-   [Mesh](Mesh_Workbench.md) import/modifications
-   Assembly simulation (3 different approaches, [A2+](A2plus_Workbench.md), [ASM3](Assembly3_Workbench.md), and [ASM4](Assembly4_Workbench.md), are all actively developed)
-   [Architectural](Arch_Workbench.md)/[BIM](BIM_Workbench.md) design\]
-   Mechanical Stress Analysis ([FEM/FEA](FEM_Workbench.md))
-   Computational Fluid Dynamic Analysis ([CFD](Cfd_Workbench.md))
-   [Technical Drawings](TechDraw_Workbench.md)/[Drafting](Draft_Workbench.md)
-   And more [core](Workbenches.md) and [external](External_workbenches.md) workbenches\...

### \"User interface (UI/UX) is ugly, odd, confusing or not like XYZ Software!\" 

FreeCAD allows for [extensive customization](Interface_Customization.md) of the user interface. While we realize the default colors or arrangement of elements may not be pleasing to everyone, we encourage you to tailor it to your own specific needs and work-flows. If you feel you\'ve come up with what could be a popular arrangement/theme/customized toolbars etc. please feel free to look into leveraging the recently added [Preference Pack](Preference_Packs.md) feature and share it with the community. Perhaps your efforts will help someone else in their transition to FreeCAD. FOSS software thrives on all sorts of community contributions and this is a common topic of discussion.

### \"Why doesn\'t this feature work like in XYZ software?\" 

FreeCAD has a development pedigree spanning over [20 years](History.md). Functions and behaviors are heavily reviewed, debated and assessed before they are added or changed. Have an open mind, while it may not be apparent, there is likely a very good rationale behind such things. This isn\'t to say that FreeCAD is perfect, but please consider that what you\'ve grown used to may not be the only or best way to get something done.

### \"I can\'t figure out the workflow of FreeCAD!\" 

FreeCAD has a philosophy to not dictate \'how\' you use it. Rather it provides tools and a wide array of options under which you \'can\' use them. This means two things. First, the software isn\'t going to necessarily \'guide\' or \'steer\' you toward a certain style or workflow. Second, this means you can experiment with the tools and find what works best for you. This doesn\'t mean there aren\'t general [\'best practices\'](Feature_editing.md) to keep in mind while using FreeCAD, but those best practices generally apply to any professional design software when creating stable models.

### \"What the heck is with all these workbenches?\" 

One of the powerful features of FreeCAD is it\'s modularity. This is done by compartmentalizing tool development into workbenches. Once you are familiar with the tools provided they can often work synergistically to create highly complex and advanced models. A great analogy is that FreeCAD is structured similar to a mechanics rolling tool-chest, and each workbench is a drawer of specific tools. You can use these tools to build a car, but it is up to the mechanic to understand how to use them to accomplish their goal.

### \"FreeCAD is fundamentally broken, my models blow-up!\" 

FreeCAD is built around an open-source Geometric Modeling Kernel called \"[OpenCascade Technology](OpenCASCADE.md)\" (or OCC). It is the most feature rich and mature open source modeling kernel available. However it does have bugs, quirks and limitations. One of these is referred to as the [\"Topological Naming Problem\"](Topological_naming_problem.md) (or TNP). Whenever a model is modified, the internal names of faces and edges are changed by the kernel causing undesirable behavior for any model features that reference them. The current development cycle is focused around implementing a naming algorithm designed to mitigate this effect under most circumstances. However, be aware that TNP mitigation is not a replacement for [good modeling practice and techniques](Feature_editing.md).


<div class="mw-translate-fuzzy">

### Kernel OpenCascade 


</div>


<div class="mw-translate-fuzzy">

OpenCascade (OCC/OCCT) jest podstawową zewnętrzną zależnością jądra CAD, od której FreeCAD jest całkowicie zależny. Istnieje wiele otwartych błędów \"upstream\", które społeczność FreeCAD zidentyfikowała i śledzi w odniesieniu do OCC. Śledzimy je poprzez   *

-   [bugtracker](https   *//github.com/FreeCAD/FreeCAD/issues?q=is%3Aopen+is%3Aissue+label%3A%223rd+Party%3A+OCC%22)
-   [wątek na forum](https   *//forum.freecad.org/viewtopic.php?t=20264) o nazwie *OCC Bugs in the Bugtracker*


</div>


<div class="mw-translate-fuzzy">

## Odnośniki internetowe 


</div>

-   [Dyskusja   * FreeCAD nie jest gotowy na 1.0 (wątek na forum)](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=43461)
-   [Why the GIMP Team Obviously\* Hates You (\*We Actually Love You. \*\*Mostly)](https   *//www.youtube.com/watch?v=JBmdbipkbrk) Pat David z prezentacji zespołu GIMP na SCaLE16x California 2016 r.
-   [Earning Your Support Instead of Buying it   * A How-to Guide to Open Source Assistance](https   *//vimeo.com/144089061) autorstwa [Iana Turtona](https   *//twitter.com/ijturton) na FOSS4G Seul 2015

[Category   *Common Questions](Category_Common_Questions.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > FreeCAD Managing Expectations/pl
