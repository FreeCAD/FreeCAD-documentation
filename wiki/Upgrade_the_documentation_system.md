# Upgrade the documentation system
This page is dedicated to the description of the [Google Summer of Code 2019](Google_Summer_of_Code.md) project idea of upgrading the documentation system of FreeCAD.

## Outline

FreeCAD already possesses a vast documentation, written by its users and hosted on this very wiki. On each FreeCAD release, the contents of the wiki get packed into a offline documentation package which is bundled with FreeCAD. When using the \"what\'s this?\" feature, FreeCAD users can quickly get documentation about a specific tool

Additionally, this same documentation also has several translations, hosted on the same wiki and managed by a mediawiki plugin, and also counts on the source code structure and comments, automatically extracted by the [doxygen](https   *//en.wikipedia.org/wiki/Doxygen) tool, and hosted on <https   *//www.freecadweb.org/api/>

However there are several problems   *

-   The bundled offline doc is often incomplete, due to the difficulty (and size) to pack it all
-   Over a year there are significant differences between the online and offline docs
-   Translations are not available offline
-   The doxygen-generated docs are in a bad state, hard to read and use and don\'t explain APIs clearly, and confuse C++ and python
-   The wiki is hard to port and back up
-   [Add-ons](https   *//github.com/FreeCAD/FreeCAD-addons) documentation is not well integrated

Additionally, the mediawiki-based documentation is more and more problematic to maintain and back up, and we are looking at transitioning to a more easily portable and redundant system like git-based wikis.

This project proposes to remedy to the main problems by   *

\- allowing the user to switch between online and offline documentation, and choose between different available languages - extending and bettering the doxygen-generated documentation, with special care for the python API

-   proposing a better Doxygen structure for <https   *//www.freecadweb.org/api/> possibly with interconnection with the wiki

\- working on bettering the current wiki (formatting, linking between pages, navigation, etc) - reimplement the old workbench-defined documentation system, help porting the different addons - adapt the FreeCAD start page to it - adapt the FreeCAD help menu (integrate workbenches and addons help entries) - exploring the different possibilities of git-based documentation, analyzing specially their user-friendliness and ease of edition, and possibilities of maintaining large translations easily and automatically (for ex. connecting with translation platforms) and propose migration workflows

## Details

-   Get familiar with FreeCAD and the contents of the wiki
-   Successfully compile FreeCAD (you\'ll be working in C++) and the Doxygen docs
-   Understand how Doxygen works and specifically how it treats C++ and Python differently
-   Work on the FreeCAD C++ source code (modify the whats\'this and documentation system, work on the Help menu)
-   Work on the in-source code documentation
-   Work on the wiki documentation
-   Explore and document available open-source documentation systems

## Expected Outcome 

-   A better documentation system inside FreeCAD
-   Documentation. Like all open-source projects, it is of uttermost importance to document a lot everything you do. This allows for other people to take on and extend your work more easily.
-   Proposals of migration to a better documentation system that would still keep FreeCAD users happy and eager to write and translate

## Project Properties 

### Skills

-   Programming language   * C++, but understanding some Python will be necessary
-   Readiness to work with documentation, reasonably good english writing skills

### Difficulty

Medium

### Additional Information 

-   Potential mentors   * [Yorik](http   *//forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)

[Category   *Google Summer of Code](Category_Google_Summer_of_Code.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > Upgrade the documentation system
