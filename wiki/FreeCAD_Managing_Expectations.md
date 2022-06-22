# FreeCAD Managing Expectations
## Purpose

This wiki page is intended for new FreeCAD users coming from other CAD/CAM solutions.

## FreeCAD is FreeCAD 

If you are considering FreeCAD as a replacement for another CAD program you may wonder why FreeCAD is different. The simple answer is that FreeCAD just is. It does not aim to emulate product X, Y or Z, it has its own way of doing thing, its own workflows, its own [history](History.md).

Does that mean FreeCAD developers think that FreeCAD is perfect the way it is? No, of course not. There are bugs in FreeCAD that need to be fixed, because we are a FOSS project we can be quite open about this, but also new features that programmers want to introduce. And if you ask for a feature developers may well consider it. But, please, do not expect them to drop what they are currently doing. Or quit their day job for that matter, most of them are volunteers after all. *It\'s done when it\'s done* is the FreeCAD motto.

## What can I expect? 

At its core FreeCAD is parametric modeler. It uses a workbench concept, where each workbench is responsible for specific tasks and functions. As such it can be used for many purposes. It is actively used in production and quite stable. But, like any other CAD program, FreeCAD is not 100% stable.

Coming from another CAD program you may have to change your workflow, or use a workaround or a macro, but in many cases you will be able to achieve what you want. And if you need help   * we have a very active and responsive [forum](https   *//forum.freecad.org/index.php) willing to assist. And among the forum member there are bound to be (former) users of you current CAD program. So do not hesitate to tap into that resource.

### Can FreeCAD be used for 2D drafting? 

### Can FreeCAD be used for non-parametric modeling? 

### Can FreeCAD be used for mesh modeling? 

## How can I contribute? 

There are many ways   * you can make a [donation](Donate.md), help with [forum](https   *//forum.freecad.org/index.php) questions, or write documentation or code. See [Help FreeCAD](Help_FreeCAD.md).

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

## Realities

### OpenCascade Kernel 

OpenCascade (OCC/OCCT) is a core external CAD kernel dependency that FreeCAD is utterly dependent on. There are many open \'upstream\' bugs that the FreeCAD community has identified and track regarding OCC. We track them via the   *

-   [bugtracker](https   *//github.com/FreeCAD/FreeCAD/issues?q=is%3Aopen+is%3Aissue+label%3A%223rd+Party%3A+OCC%22)
-   [forum thread](https   *//forum.freecad.org/viewtopic.php?t=20264) called *OCC Bugs in the Bugtracker*

### Qt

## Links

-   [Discussion   * FreeCAD is not ready for 1.0 (forum thread)](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=43461)
-   [Why the GIMP Team Obviously\* Hates You (\*We Actually Love You. \*\*Mostly)](https   *//www.youtube.com/watch?v=JBmdbipkbrk) Pat David from GIMP team presentation at SCaLE16x California 2016
-   [Earning Your Support Instead of Buying it   * A How-to Guide to Open Source Assistance](https   *//vimeo.com/144089061) by [Ian Turton](https   *//twitter.com/ijturton) at FOSS4G Seoul 2015



[Category   *Common Questions](Category_Common_Questions.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Common Questions](Category_Common Questions.md) > FreeCAD Managing Expectations
