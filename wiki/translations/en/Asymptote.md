# Asymptote/en
{{TOCright}}

## Description

[Asymptote](https   *//asymptote.sourceforge.io/) is a vector language for 2D and 3D computer graphics. Asymptote code can be included in [LaTeX](https   *//www.latex-project.org/) documents or used to generate [PostScript](https   *//en.wikipedia.org/wiki/PostScript), [PDF](PDF.md), [SVG](SVG.md), [WebGL](https   *//www.khronos.org/webgl/), and [PRC](https   *//en.wikipedia.org/wiki/PRC_(file_format)) files. Interactive 3D PDF files created from Asymptote code require Acrobat Reader version 9 or higher.

Asymptote support was added in FreeCAD version 0.19.

## Exporting

1.  Optionally assign colors to the faces of the object you want to export with the <img alt="" src=images/Part_FaceColors.svg  style="width   *24px;"> [Part FaceColors](Part_FaceColors.md) command.
2.  Change to the <img alt="" src=images/Workbench_Mesh.svg  style="width   *24px;"> [Mesh Workbench](Mesh_Workbench.md).
3.  Create a mesh from the object with the <img alt="" src=images/Mesh_FromPartShape.svg  style="width   *24px;"> [Mesh FromPartShape](Mesh_FromPartShape.md) command.
4.  Select the new mesh object.
5.  Invoke the <img alt="" src=images/Mesh_Export.svg  style="width   *24px;"> [Mesh Export](Mesh_Export.md) command.
6.  Select the ***.asy** file format in the dialog box.
7.  Enter a filename.
8.  Press the **Save** button.

## Converting

You need the [Asymptote compiler](https   *//sourceforge.net/projects/asymptote/) to convert ***.asy** files. To convert to PDF a [LaTeX](https   *//www.latex-project.org/get/) system is also required.

The compiler is a command line tool. To covert to PDF you can use this syntax   * 
```pythonPathToAsyExecutable/asy -f pdf AsymptoteFileName.asy```

## Related

-   [Import Export](Import_Export.md)

## Video tutorials 

The following videos are in Spanish   *

-   [A way of generating interactive pdf-3D files. (1/3) (From FreeCAD, MeshLab and LaTeX)](https   *//www.youtube.com/watch?v=U0m3643Vb1Q)
-   [A way of generating interactive pdf-3D files. (2/3) (From Asymptote and LaTex)](https   *//www.youtube.com/watch?v=PhVNvDZIerM)
-   [A way of generating interactive pdf-3D files. (3/3) (From FreeCAD, Asymptote and LaTeX)](https   *//www.youtube.com/watch?v=Q_ufaCN2hb4)


{{Mesh Tools navi

}} 

[Category   *File\_Formats](Category_File_Formats.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Mesh](Category_Mesh.md) > Asymptote/en
