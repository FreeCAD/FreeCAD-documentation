# History/pt
\_\_FORCETOC\_\_


<div class="mw-translate-fuzzy">

História


</div>

### How it all started 

FreeCAD began in January 2001 when [Jürgen Riegel](User_Jriegel.md) started working on the Cas.CADE project. Cas.CADE was a commercial software development framework that included a [geometric modeling kernel](Glossary#Geometric_modeling_kernel.md) (or CAD kernel)   * it was released under an open source license in 2000 and renamed [OpenCASCADE](OpenCASCADE.md). This made the realization of an open source 3D CAD program possible, as having to program a CAD kernel from scratch would have required a huge amount of work.

In Jürgen\'s own words   *


{{Quote|text=''The FreeCAD project was started by me in January 2001, as a so called GOM (Graphical Object Modeler), with the idea to use Qt, Python and Cas.CADE, an commercial CAD-Kernel that time I used in Daimler's projects. Cas.CADE gone open source shortly before, so the time seemed right to try a move in the, at that time, empty space of open source CAD. I had a two year experience with OpenCascade in a project called QSpect in which, at the end, I was the main software designer. I learned a lot about 3D and CAD programming. I also was influenced by Catia V5 and its very special user and programming interface… In March 17 2002, within the OpenCascade Project, I registered the software as FreeCAD. I couldn't think of a better name, I'm very bad on names… In April 2003, Werner Meyer, one of the colleges in the QSpect project, switched to a company called Imetric. The contact to Imetric resulted very promising since they searched for a new 3D software platform for their 3D sensors. In 2005, Imetric donated most of its Mesh Module to FreeCAD and the Open Source community, and since then they used FreeCAD as basis for their sensor system software. Since that time, Werner Meyer is a very active developer of FreeCAD. In 2005, after one year of struggle, I decided to rip of the OpenCascade document framework and replace it with an own implementation. So, at the end, we only use the CAD kernel of OpenCascade and not the rest of its Framework. 2007 was another interesting milestone. We switched to QT4 and, therefore, to the LGPL. At that time we did much work, mainly Werner''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[http   *//forum.freecadweb.org/viewtopic.php?f=8&t=295 Who is behind FreeCad?]''}}

The project was announced to the general public on the [OpenCascade Forum](https   *//dev.opencascade.org/forums) in 2003   *


{{Quote|text=''Hi together, my name is Juergen Riegel and today I want announce an OpenCasCade project, FreeCAD. It is an Open Source CAx RAD based on OpenCasCade, QT and Python. It features some key concepts like Macro Recording, Workbenches, ability to run as a server and as a dynamically loadable applications' extension, and it is designed to be platform independent… Although it is in an early stage and not usable for users nor developers—the first user release is planned for the end of 2003—, I would like to get some feedback on the direction and design of FreeCAD. The GUI is nearly finished and now we, my co-developer Werner Mayer and me, have started adding the first CAD functions. FreeCAD can be seen as a general purpose mechanical CAD system, but its first audience, I think, will be CAx developers which need groundwork for own development''.
|sign=[Jürgen Riegel](User_Jriegel.md)|source=''[https   *//dev.opencascade.org/content/announcing-freecad-project Announcing FreeCAD Project on Sun, 08/17/2003 - 19   *23]''}}

### Werner Mayer 

Werner Mayer joined the project as soon as it was announced as an open source project (prior to the announcement the project was a private project of Jürgen). See this forum post from Werner in German   * <https   *//forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>

Over time the project gained traction and saw the addition of new key contributors in the community.

-   **Linux beginning**


{{Quote|text=''A fun fact is that he wanted to have an open-source CAD software mainly for Linux because at that time there existed actually nothing for this platform. However, from the beginning on we exclusively developed on Windows for the next 1.5 years. Then a Czech guy made a contribution to make the code of the core build on Linux   * https   *//github.com/berndhahnebach/All_FreeCAD/commit/9fd2e27c95ba3dc84778d92e2564cd094793ce2f#diff-480477e89f9b6ddafb30c4383dcdd705''}}


{{Quote|text=''Half a year later I continued the Linux build   * https   *//github.com/berndhahnebach/All_FreeCAD/commit/35b962d7d751dd80f7c7781df60f93bc9a3da992''}}

**Q   *** Could you share how that first 1.5 years went? Were you meeting in person or online?


{{Quote|text=''Well, at that time we were colleagues (until 2005) so we could discuss things face to face. After that time we still had some personal meetings but discussed most things by email or phone.''}}


{{Quote|text=''As third core developer Yorik joined around end of 2007 but it took another 3 or 4 years until the community and number of contributors started to grow significantly.''}}

**Q   *** Did you divide the tasks or work on competing implementations?


{{Quote|text=''Yes. Jürgen was designing and implementing most of the application and document logic and I was doing the basics of the GUI.''}}


{{Quote|text=''However, this wasn't a gradual process but we have experimented with many things at the beginning. For example, in the initial version we used OCC's document framework OCAF and its viewer but after a year or two we got into a dead end because documentation about OCC was very poor and we couldn't get it to work to extend OCAF with our own feature types. So, we decided to only use OCC's modeling capacities but develop our own application/document framework.''}}

**Q   *** At the time did you think FreeCAD would be where it is today?


{{Quote|text=''We didn't know but we hoped. Of course we couldn't anticipate how exactly FreeCAD will look today.<br>The most important design decisions were to make it available on all major platforms and make the whole SW as accessible as possible, i.e. to impose all important functions to Python so that (power) users are able to extend FreeCAD with own functions. This way we hoped to get a broad audience.''}}

(See this forum post from Werner [Re   * FreeCAD History](https   *//forum.freecadweb.org/viewtopic.php?f=8&t=47703#p411612))

### Yorik joins the project 

[Yorik van Havre](User_Yorik.md) joined the project in 2008 and started work on the [Draft Module](Draft_Workbench.md). Before that point, there was no way to create 2D geometry through the [GUI](Glossary#GUI.md). This module was programmed entirely in Python rather than in C++ (the core programming language used in FreeCAD). The new Draft workbench proved that Python integration was a success and could be used to extend or customize FreeCAD\'s capabilities. In addition to his work on the Draft module, Yorik worked on expanding the FreeCAD documentation, and became FreeCAD\'s *de facto* \"Art director\", creating many icons for FreeCAD\'s GUI and [defining its style](Artwork.md).

Version 0.7 of FreeCAD released in April 2009 was the first to include the Draft module. The Part module provided a simple [CSG](Glossary#Constructive_Solid_Geometry.md) workflow with creation of primitive shapes and boolean operations accessible through the Part menu. Extrusion of 2D profiles and filleting was also possible.

Version 0.8 released in July 2009 saw some more work in the Draft module, including a new Dimension tool. The Part module benefited from a new toolbar along with new tools, Revolve and Section.

By the end of 2009, FreeCAD was accepted as a Debian package in the Debian repositories. FreeCAD was added to the Ubuntu 10.04 repositories in 2010.

### The project goes on 

Version 0.10 was released in July 2010 and introduced the [Sketcher Workbench](Sketcher_Workbench.md), based on Sketchsolve, a constraint-based solver to create 2D geometry. The first version was limited to creation of rectangles and lines.

In early 2011, taking the opportunity given by the [Launchpad](https   *//launchpad.net) online platform, the [FreeCAD Maintainers team](https   *//launchpad.net/~freecad-maintainers) was created to provide fresh stable releases along with daily build packages of FreeCAD to users of the Ubuntu operating system.

Version 0.11 as released in May 2011 and introduced the new Part Design workbench which included tools such as Pad, Pocket, Fillet and Chamfer. The Draft workbench received enhancements and new tools, like BSpline. The Robot workbench featured more GUI tools.

Version 0.12 was released in January 2012 and featured a more complete Sketcher workbench. It included a totally rewritten solver, FreeGCS. It was the result of months of work by the main FreeCAD developers along with newcomers logari81 (who programmed the solver) and mrlukeparry. More tools were added to the PartDesign workbench.

### Enlargement of core developer team 

In April 2019 the team of core developers was expanded   * Jürgen, Werner and Yorik were joined by Abdullah, Bernd, sliptonic and WandererFan

## Interesting Posts on the forum 

-   about PartDesignNext and other design decisions   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=34923&start=130#p297074>
-   about Forum history   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=7448&start=200#p287106>
-   about Project history   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=47703>
-   about Code history   * <https   *//forum.freecadweb.org/viewtopic.php?f=10&t=46733&start=10#p405068> BTW   * initial code checkin was on March 18th in 2002 (may be the birthday?)
-   about Project to be OpenSource   * <https   *//forum.freecadweb.org/viewtopic.php?f=13&t=40235&start=10#p342330>
-   about The release commit history   * <https   *//forum.freecadweb.org/viewtopic.php?f=8&t=23695#p184940>
-   about Who is behind FreeCAD   * <http   *//forum.freecadweb.org/viewtopic.php?f=8&t=295>
-   about FEM history   * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=48646#p416389>
-   about FEM mesher history   * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=48733#p417627>

## Release history 

#### Overview

  Version   Release name   Release date     Release notes                                         Release commit                                                                            Release branch
       
  1.0       \-             in development   [Release notes 1.0](Release_notes_1.0.md)     [head master](https   *//github.com/FreeCAD/FreeCAD/commits/master)                          
  0.20      \-             2022-06-14       [Release notes 0.20](Release_notes_0.20.md)   [release commit 0.20](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-20)   [branch bugfixes 0.20](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-20)
  0.19      \-             2021-03-20       [Release notes 0.19](Release_notes_0.19.md)   [release commit 0.19](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-19)   [branch bugfixes 0.19](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-19)
  0.18      \-             2019-03-12       [Release notes 0.18](Release_notes_0.18.md)   [release commit 0.18](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-18)   [branch bugfixes 0.18](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-18)
  0.17      Roland         2018-04-06       [Release notes 0.17](Release_notes_0.17.md)   [release commit 0.17](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-17)   [branch bugfixes 0.17](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-17)
  0.16      \-             2016-04-18       [Release notes 0.16](Release_notes_0.16.md)   [release commit 0.16](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-16)   [branch bugfixes 0.16](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-16)
  0.15      \-             2015-04-08       [Release notes 0.15](Release_notes_0.15.md)   [release commit 0.15](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-15)   [branch bugfixes 0.15](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-15)
  0.14      \-             2014-07-01       [Release notes 0.14](Release_notes_0.14.md)   [release commit 0.14](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-14)   [branch bugfixes 0.14](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-14)
  0.13      \-             2013-01-29       [Release notes 0.13](Release_notes_0.13.md)   [release commit 0.13](https   *//github.com/FreeCAD/FreeCAD/commits/releases/FreeCAD-0-13)   [branch bugfixes 0.13](https   *//github.com/FreeCAD/FreeCAD/tree/releases/FreeCAD-0-13)
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

-   [SourceForge Files section](http   *//sourceforge.net/projects/free-cad/files/)
-   [SourceForge Old Files section](http   *//sourceforge.net/projects/free-cad/files/OldFiles/)
-   [Announcing FreeCAD Project](http   *//www.opencascade.org/org/forum/thread_6572/?forum=11) on the OpenCascade forum

[Category   *News](Category_News.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > History/pt
