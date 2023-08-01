# Asymptote/fr
{{TOCright}}

## Description

[Asymptote](https://asymptote.sourceforge.io/) est un langage vectoriel pour l\'infographie 2D et 3D. Le code Asymptote peut être inclus dans des documents [LaTeX](https://www.latex-project.org/) ou utilisé pour générer [PostScript](https://fr.wikipedia.org/wiki/PostScript), [PDF](PDF/fr.md), [SVG](SVG/fr.md), [WebGL](https://www.khronos.org/webgl/) et [PRC](https://fr.wikipedia.org/wiki/PRC_(fichier)). Les fichiers PDF 3D interactifs créés à partir du code Asymptote nécessitent Acrobat Reader version 9 ou supérieure.

Le support d\'Asymptote a été ajouté dans la version 0.19 de FreeCAD.

## Exporter

1.  Attribuez éventuellement des couleurs aux faces de l\'objet que vous souhaitez exporter avec la commande <img alt="" src=images/Part_FaceColors.svg  style="width:24px;"> [Part Définir les couleurs](Part_FaceColors/fr.md).
2.  Passez à l\'<img alt="" src=images/Workbench_Mesh.svg  style="width:24px;"> [atelier Mesh](Mesh_Workbench/fr.md).
3.  Créez un maillage à partir de l\'objet avec la commande <img alt="" src=images/Mesh_FromPartShape.svg  style="width:24px;"> [Mesh Tesselation](Mesh_FromPartShape/fr.md).
4.  Sélectionnez le nouvel objet maillage.
5.  Appelez la commande <img alt="" src=images/Mesh_Export.svg  style="width:24px;"> [Mesh Exporter un maillage](Mesh_Export/fr.md).
6.  Sélectionnez le format de fichier ***.asy** dans la boîte de dialogue.
7.  Entrez un nom de fichier.
8.  Appuyez sur le bouton **Save**.

## Convertir

Vous avez besoin du [compilateur Asymptote](https://sourceforge.net/projects/asymptote/) pour convertir les fichiers ***.asy**. Pour convertir en PDF, [LaTeX](https://www.latex-project.org/get/) est également requis.

Le compilateur est un outil de ligne de commande. Pour convertir en PDF, vous pouvez utiliser cette syntaxe: 
```pythonPathToAsyExecutable/asy -f pdf AsymptoteFileName.asy```

## En relation 

-   [Import Export](Import_Export/fr.md)

## Tutoriels vidéo 

Les vidéos suivantes sont en espagnol :

-   [Une manière de générer des fichiers PDF-3D interactifs. (1/3) (à partir de FreeCAD, MeshLab et LaTeX)](https://www.youtube.com/watch?v=U0m3643Vb1Q)
-   [Une manière de générer des fichiers PDF-3D interactifs. (2/3) (De Asymptote et LaTex)](https://www.youtube.com/watch?v=PhVNvDZIerM)
-   [Une manière de générer des fichiers PDF-3D interactifs. (3/3) (à partir de FreeCAD, Asymptote et LaTeX)](https://www.youtube.com/watch?v=Q_ufaCN2hb4)


{{Mesh Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [File_Formats](Category_File_Formats.md) > [Mesh](Category_Mesh.md) > Asymptote/fr
