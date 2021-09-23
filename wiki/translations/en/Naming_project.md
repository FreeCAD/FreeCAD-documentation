# Naming project/en



**
This roadmap is probably obsolete. For more information see [Development roadmap](Development_roadmap.md).<br>
If you are not involved with the development discussed here:<br>
!!! PLEASE DO NOT EDIT OR TRANSLATE !!!
**


{{TOCright}}

This template is the guideline for a FreeCAD development project. It follows the rules of the [Getting Things Done (GTD)](http://en.wikipedia.org/wiki/Getting_Things_Done#Methodology) process. The projects are collected in the [Development roadmap](Development_roadmap.md).

## Purpose and principles 

This is a development and design effort to implement a robust topological naming in FreeCAD.

More details about topological naming in **[Topological naming problem](Topological_naming_problem.md)**.

## Outcome

1.  **Interface** in (Part::TopoShape) to robustly reference (name) shapes and sub-shapes (faces, edges, vertexes) through a string (sub-element name like \"Face1\")
    Here we need a interface to provide Part::TopoShape with all information need to do the Naming, e.g. NewShape, additional information from an algorithm like deleted faces, modeling step (for 2.) and \...
2.  **Association** of modeling steps with the resulting faces/edges.
    In case of a big model the user is lost if he/she has hundreds of fillets or bore hole. So if the faces/edges would know what modeling step it created we could implement a double click on edge/face opens the right feature!
3.  An **algorithm** to keep the naming stable throughout changes in modeling history, like splitting edge/faces and moving vertexes
    ![](images/NamingExample.jpg )
4.  (optional) **memory optimized data structure** to keep only changed faces/edges in each modeling feature.
    This will become important when the models get bigger. Its not efficient to copy most of the shape just through. Would be much more effective to share the unchanged faces/edges between Features and copy only whats changed.

## Brainstorming

A lot was discussed in the [\"Robust References\" Post](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656) of jrheinlaender in the period from June 2012 to May 2016.

### Others

-   [Catia V5 Topology and Generic Naming](http://www.maruf.ca/files/caadoc/CAATopTechArticles/JournalMethodology.htm#Definition) and [Catia V5 Objectives of Generic Naming](http://www.maruf.ca/files/caadoc/CAAMmrTechArticles/CAAMmrGenericNaming.htm#Objectives%20of%20GN)
-   [Topological naming in OCAF (Open CASCADE Application Framework)](https://www.opencascade.com/doc/occt-7.4.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6)

### Literature & Papers 

-   J Kripac, \"A mechanism for persistently naming topological entities in history-based parametric solid models, Symposium on Solid Modeling and Applications 1995, p.21-30\"

:   Describes a method to do the first three points in the List. Would say the is the approach used by Catia and OCC-TNaming. At least the interface looks the same. The paper was nowhere to download. I had to buy it. If someone is interested I can send it via E-Mail.

-   [Dago AGBODAN, David MARCHEIX and Guy PIERRA, \"PERSISTENT NAMING FOR PARAMETRIC MODELS, 2000\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.29.2836&rep=rep1&type=pdf)

:   Interesting approach via shell-graphs, tackles the point four on the list by reusing faces/edges not changed.

-   [Duhwan Mun and Soonhung Han, \"Identification of Topological Entities and Naming Mapping for Parametric CAD Model Exchanges, INTERNATIONAL JOURNAL OF CAD/CAM, 2005, p 69-82\"](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.106.3087&rep=rep1&type=pdf)

:   Very good overview and Examples

-   [Farjana, S.H., Han, S. \"Mechanisms of Persistent Identification of Topological Entities in CAD Systems: A Review\", Alexandria Engineering Journal, Volume 57, Issue 4, December 2018, Pages 2837-2849](https://research-management.mq.edu.au/ws/portalfiles/portal/100931773/Publisher_version_open_access_.pdf)

-   [Assembly Solving for Neutral Re-Imported Product Models Tahir A. Jauhar, Soonhung Han, Soonjo Kwon , p.108-123 , CAD Journal 2020, Volume 17 Number 1](http://www.cad-journal.net/files/vol_17/CAD_17(1)_2020_108-123.pdf)

### Summary of Work To-Date 

As of June 13th, 2016, here is a summary of the work that has been done for this project:

-   jrheinlaender produced a lot of code in 2012 that relies heavily on the Sketch workbench for resolving \"Robust References\"
-   ickby had taken a stab at incorporating some or jrheinlaender\'s code into modern freecad. [This post](http://forum.freecadweb.org/viewtopic.php?f=10&t=2656&start=60#p124844) has a link to his github repo.
-   In 2016, ezzieyguywuf revived jrheinlaender\'s thread and subsequently started his own. You can see it [here](http://forum.freecadweb.org/viewtopic.php?f=10&t=15847)
-   ezzieyguywuf developed a \"light weight\" opencascade program for duplicating the Topological Naming issue and for testing potential solutions. See his github repo [freecadTopoTesting](https://github.com/ezzieyguywuf/freecadTopoTesting) here
-   ezzieyguywuf incorporated the opencascade TNaming toolkit into his test code, and showed how this could help resolve some of the Topological Naming issues. See the github repo
-   [Topological Naming](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming) github repo by realthunder
-   [Topological Naming Algorithm](https://github.com/realthunder/FreeCAD_assembly3/wiki/Topological-Naming-Algorithm) github repo by realthunder

## Organizing

### Information about TNaming 

See [here](https://github.com/ezzieyguywuf/freecadTopoTesting/blob/master/TNaming_Writeup.md) for a decent write-up on the github repo [freecadTopoTesting](https://github.com/ezzieyguywuf/freecadTopoTesting) by ezzieyguywuf. Here are some highlights:

-   opencascade\'s TNaming relies upon the [TDF\_Data data framework](https://dev.opencascade.org/doc/occt-7.5.0/refman/html/class_t_d_f___reference.html#details).
-   TDF\_Data is a key component of the opencascade OCAF thing, but can be used independent of it
-   TDF\_Data is essentially a tree in which data is added and then read at a later date
-   Whenever a TNaming\_NamedShape attribute is added to a node on the TDF\_Data tree, a TNaming\_UsedShapes attribute is added to the root of the tree
    -   **NOTE:** this TNaming\_UsedShapes attribute is critical to the utility of the TNaming toolkit. It contains a history of all the TopoDS\_Shape used during the \'history\' of the part
-   TNaming\_Builder is used to add information to the TDF\_Data tree. It adds a TNaming\_NamedShape to a given node on the tree, as well as updating the TNaming\_UsedShapes database as necessary.
-   Any time the TopoDS\_Shape is changed, it must be logged in the TDF\_Data structure
    -   Again, TNaming\_Builder is used for this
    -   See [here](http://www.opencascade.com/doc/occt-7.0.0/overview/html/occt_user_guides__ocaf.html#occt_ocaf_5_6_1) in the opencascade documentation for a table listing what must be stored in the database. **NOTE:** this table appears to be incomplete. Some additional testing may need to be done
    -   In short, any time the TopoDS\_Shape is modified, any modified/generated/deleted features must be logged. For the most part, since we\'re dealing with solids, this means we must log the modified/generated/deleted Faces on the solid
-   The TNaming\_Selector class is used to \"select\" a feature that is being tracked on the TDF\_Data tree
    -   a \"selected\" feature is one that opencascade\'s TNaming algorithm will maintain a constant reference to, regardless of topological changes

## Next actions 

-   Defining the scope
-   Python test cases
-   Interface in Part::TopoShape (+ python binding)

### Next Steps (as of June 13th, 2016) 

1.  Determine if opencascade TNaming toolkit fully resolves Topological Naming issue in FreeCAD
    -   What are all instances where Topological Naming is a problem?
    -   What are complex scenarios where this approach will need to work?
2.  Incorporate TNaming code into FreeCAD
    1.  Start with a bare-bones approach, i.e. Make a Cube and a Cylinder, Fuse, Fillet, and then re-size the Cylinder. Fillet should not move
    2.  Gradually add more functionality
3.  Determine if TNaming will be the solution long-term
4.  Whether or not TNaming is the long-term solution, figure out a way to \'serialize/deserialize\' the data that TNaming uses for persistence across sessions




[Category:Roadmap](Category:Roadmap.md)
