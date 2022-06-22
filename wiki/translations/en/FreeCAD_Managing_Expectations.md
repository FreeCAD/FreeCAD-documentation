# FreeCAD Managing Expectations/en
## Purpose


{{TOCright}}

The purpose of this wiki page is to \'Manage Expectations\' of users using FreeCAD, especially those coming from other proprietary CAD/CAM solutions.

## The Eternal Open Source Conundrum 

I really like/dislike using \[Insert your go-to proprietary program\] but I   *

-   can\'t afford it
-   resent that I need to pay for it
-   don\'t want to be locked in to proprietary format/technology
-   want to own my work
-   want to work on my local machine (not on someone else\'s cloud)
-   really like using FOSS better
-   don\'t want to be involved in a FOSS because I don\'t have   * time, skills the community needs
-   don\'t want to involved in a FOSS because someone else is probably doing that
-   want to complain somewhere about a pathetic attempt at competing with \[Insert your go-to proprietary program\]
-   want to vent about how ugly the UI is to someone/somewhere just because wanna!

### Reflections

How do people conceive the way open source software is created?

#### Hopium

*I hope this open source project can get their act together (self-organize)* .

#### Hand Washing 

*Why can\'t these people self-organize?!? It\'s possible, look at these other successful projects\...*

## What FreeCAD is not 

### Non Parametric 

-   FreeCAD can be used non-parametrically. But the user needs to know how.
-   Blender is the ideal free libre opensource tool for non-parametric design.

### Mesh Modeler 

-   Again, Blender is the more appropriate application for mesh modeling.

## Common Perspectives 

### FreeCAD has not reached v1.0 

### FreeCAD is not stable 

This is true to of any of many CAD applications. FreeCAD suffers from this as well. Although the community works to address catastrophic crashes quickly, users are encouraged to employ a workflow in which they save their work often and utilize the backup features (available in preferences) to recover or roll-back from problematic issues. An important point here to consider is that many users aren\'t always using the most up to date version of FreeCAD and end up complaining of deprecated or already addressed instability problems. FreeCAD also has a very long release cycle and in the past has not backported fixes due to time and 3rd-party dependency complexity. In short, many bugs get fixed in the development version and so users need to make the unorthodox decision of running a development version of FreeCAD instead of the \'stable\'.

### FreeCAD UI is ugly 

-   At its core, this is relegated to \'Eye of the beholder\' (subjective) perspective. FreeCAD has been around a very long time, its dedicated users have grown familiar with the user interface.
-   The topic of changes to UI/UX is very contentious. Changes to the UI/UX require proof of concepts, popularity in the community, and effectiveness to eventually make it in to the mainline FreeCAD code. This takes time and diplomacy.
-   Is it really? Thanks to customization possibilities (as of v0.20) there is an ability to customize the UI (see [Preference Packs](Preference_Packs.md)). At some point very soon, FreeCAD will be provide a comprehensive flexibility to customize its UI, something other CAD packages would not be able to boast.

### Where is my favorite feature? 

## Realities

### OpenCascade Kernel 

OpenCascade (OCC/OCCT) is a core external CAD kernel dependency that FreeCAD is utterly dependent on. There are many open \'upstream\' bugs that the FreeCAD community has identified and track regarding OCC. We track them via the   *

-   [bugtracker](https   *//github.com/FreeCAD/FreeCAD/issues?q=is%3Aopen+is%3Aissue+label%3A%223rd+Party%3A+OCC%22)
-   [forum thread](https   *//forum.freecad.org/viewtopic.php?t=20264) called *OCC Bugs in the Bugtracker*

### Qt

### Volunteers

The reality of having a volunteer based workforce   *

-   Project timelines/goals change due to unforeseen life issues.
-   Goals abandoned due to financial or motivational problems.
-   Incompatible relational attitudes/behaviors that come up during collaborations.
-   Unpaid volunteers

Hence, FreeCAD\'s motto *It\'s done when it\'s done.*

### Organizational Challenges 

As with many opensource projects, FreeCAD has had its organizational challenges. Some of them are listed here in short   *

-   Departure of jriegel (one of the original core developers)
-   The incomplete implementation of PartDesign workbench (incompatibilities with Part WB).
-   Assembly workbench development that had been abandoned several times (Assembly and Assembly2). It now has 3 separate solutions (Assembly2+, Assembly3, Assembly4). There is an intention to unify these 3 active Assembly approaches.

## Relevant Links 

-   [Why the GIMP Team Obviously\* Hates You (\*We Actually Lot you. \*\*mostly)](https   *//www.youtube.com/watch?v=JBmdbipkbrk) Pat David from GIMP team presentation at SCaLE16x California 2016
-   [Earning Your Support Instead of Buying it   * A How-to Guide to Open Source Assistance](https   *//vimeo.com/144089061) by [Ian Turton](https   *//twitter.com/ijturton) at FOSS4G Seoul 2015

## Discussion Threads 

Links to forum thread discussions related to this topic

-   Discussion   * FreeCAD is not ready for 1.0 ([forum thread](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=43461))

[Category   *Common Questions](Category_Common_Questions.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > FreeCAD Managing Expectations/en
