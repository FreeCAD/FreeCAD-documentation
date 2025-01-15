# BCF support
**This project was realized during [GSOC 2019](#GSOC_2019.md)**

This page is dedicated to the description of the [Google Summer of Code 2019](Google_Summer_of_Code.md) project idea of adding BCF support to FreeCAD.

## Outline

[BIM Collaboration Format](https://www.buildingsmart.org/bim-collaboration-format-explained/) (or BCF) is a file format aimed at coordinating the work of several participants in a [Building Information Modeling (BIM)](https://en.wikipedia.org/wiki/Building_information_modeling) project. The format specifications are [maintained by BuildingSMART](http://www.buildingsmart-tech.org/specifications/bcf-releases), the same consortium behind the [IFC](https://en.wikipedia.org/wiki/Industry_Foundation_Classes) file format.

The BCF format implements a series of tools to allow users to create, annotate, classify, comment, discuss and solve issues on a BIM model. It works as a thin layer containing issues related to a BIM model. The BCF file itself doesn\'t contain or relate explicitly to the model, which allow different people who work on a same project but with different applications to still be able to discuss and process the same issues.

This project idea proposes to implement a BCF viewer for FreeCAD. The viewer would allow to:

-   Open BCF files
-   View the different issues with their comments and images (screenshots)
-   Navigate in a FreeCAD model to a camera position stored in the BCF file
-   Comment, annotate, classify and tag issues
-   Create new issues, save screenshots and camera position
-   Save BCF files
-   If time permits, explore the possibilities of server-based BCF serving (API)

## Details

-   Get familiar with FreeCAD and the current state of BIM tools
-   Get familiar with [PySide](https://en.wikipedia.org/wiki/PySide) and Qt
-   Get familiar with the BCF format, gather a series of test files
-   Implement the different functions needed to interact with BCF files and data
-   Implement a Graphical User Interface to these functions

## Expected Outcome 

-   Documentation. Like all open-source projects, it is of uttermost importance to document a lot everything you do. This allows for other people to take on and extend your work more easily.
-   A complete, working GUI application, that works as a plugin/addon inside FreeCAD.

## Future Possibilities 

BCF use in the BIM industry is still at its infancy. One can think of many possible extensions, such as:

-   Connecting with other (open-source) communication structures: forums, chat/messaging systems, etc\...
-   Connecting with other issues tracking systems

## Project Properties 

### Skills

-   Programming language: Python + PySide
-   Knowledge of BIM modeling and workflows is a plus, or be ready to practice!

### Difficulty

Medium

### Additional Information 

-   Potential mentors: [Yorik](http://forum.freecadweb.org/memberlist.php?mode=viewprofile&u=68)

## GSOC 2019 

This workbench was created during a GSOC 2019 by user \'podestplatz\'. Relevant links:

-   [Dev logs](https://podestplatz.github.io/FreeCAD-blog/posts/dev-logs/)
-   FreeCAD blog - BCF integration ([link](https://podestplatz.github.io/FreeCAD-blog/))
-   [BCF git repo](https://github.com/podestplatz/BCF-Plugin-FreeCAD/)



---
⏵ [documentation index](../README.md) > [Google Summer of Code](Category_Google%20Summer%20of%20Code.md) > BCF support
