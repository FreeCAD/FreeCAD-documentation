# Release notes 1.0/fr
**FreeCAD 1.0 est en cours de développement, il n'y a pas encore de date de sortie prévue.**


{{Message|
Des fonctionnalités sont-elles manquantes? Mentionnez-les dans les [https   *//forum.freecadweb.org/viewtopic.php?f&#61;10&t&#61;69438 Notes de publication pour v1.0] du fil du forum.

Voir [Contribuer à FreeCAD](Help_FreeCAD/fr.md) pour savoir comment contribuer à FreeCAD.
}}


{{Message|Toutes les images de cette page doivent utiliser le suffixe **_relnotes_1.0**}}


{{TOCright}}

**FreeCAD 1.0** a été publié le **JJ MM 2023**, téléchargez la depuis la page [Téléchargement](Download/fr.md). Cette page liste toutes les nouvelles fonctionnalités et les changements.

Les notes de versions plus anciennes de FreeCAD sont disponibles dans la [liste des notes de versions](Feature_list/fr#Notes_de_versions.md).

L\'endroit pour une image accrocheuse sélectionnée par les administrateurs sur le [forum des modèles des utilisateurs](https   *//forum.freecadweb.org/viewforum.php?f=24).

## Général

## Interface utilisateur 

### Autres améliorations de l\'interface utilisateur 

## Noyau et API 

### Noyau

### API


<div class="mw-collapsible mw-collapsed toccolours">

#### Nouvelles API en Python 


<div class="mw-collapsible-content">

-   *ShapeFix\_EdgeConnectPy*    * Classe racine pour les opérations de fixation. [commit 4d4adb93](https   *//github.com/FreeCAD/FreeCAD/commit/4d4adb93)
-   *ShapeFix\_EdgePy*    * Correction d\'un bord invalide. [commit 4089cbfb](https   *//github.com/FreeCAD/FreeCAD/commit/4089cbfb)
-   *ShapeFix\_FaceConnectPy*    * Reconstruit la connectivité entre les faces dans le shell. [commit a0eb2e9d](https   *//github.com/FreeCAD/FreeCAD/commit/a0eb2e9d)
-   *ShapeFix\_FacePy*    * Classe pour les opérations de fixation sur les faces. [commit b6cd635c](https   *//github.com/FreeCAD/FreeCAD/commit/b6cd635c)
-   *ShapeFix\_FixSmallFacePy*    * Classe pour fixer les opérations sur les faces. [commit 4c2946c8](https   *//github.com/FreeCAD/FreeCAD/commit/4c2946c8)
-   *ShapeFix\_FixSmallSolidPy*    * Correction des solides de petite taille. [commit b70d8d37](https   *//github.com/FreeCAD/FreeCAD/commit/b70d8d37)
-   *ShapeFix\_FreeBoundsPy*    * Destinée à fournir les limites libres de la forme. [commit 1ee1aee1](https   *//github.com/FreeCAD/FreeCAD/commit/1ee1aee1)
-   *ShapeFix\_RootPy*    * Classe racine pour les opérations de fixation. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_ShapePy*    * Classe pour fixer les opérations sur les formes. [commit 87db9dcc](https   *//github.com/FreeCAD/FreeCAD/commit/87db9dcc)
-   *ShapeFix\_ShapeTolerancePy*    * Modifie les tolérances des sous formes (sommets, arêtes, faces). [commit 125d5b63](https   *//github.com/FreeCAD/FreeCAD/commit/125d5b63)
-   *ShapeFix\_ShellPy*    * Classe racine pour les opérations de fixation. [commit f3e941a3](https   *//github.com/FreeCAD/FreeCAD/commit/f3e941a3)
-   *ShapeFix\_SolidPy*    * Classe racine pour les opérations de fixation. [commit 8d568793](https   *//github.com/FreeCAD/FreeCAD/commit/8d568793)
-   *ShapeFix\_SplitCommonVertexPy*    * Classe pour les opérations de fixation sur les formes. [commit 4b44c54c](https   *//github.com/FreeCAD/FreeCAD/commit/4b44c54c)
-   *ShapeFix\_SplitToolPy*    * Outil pour diviser et couper les bords. [commit bbecc3f2](https   *//github.com/FreeCAD/FreeCAD/commit/bbecc3f2)
-   *ShapeFix\_WireframePy*    * Fournit des méthodes pour fixer le fil de fer d\'une forme. [commit 6843a461](https   *//github.com/FreeCAD/FreeCAD/commit/6843a461)
-   *ShapeFix\_WirePy*    * Classe pour fixer les opérations sur les fils. [commit 94f6279a](https   *//github.com/FreeCAD/FreeCAD/commit/94f6279a)
-   *ShapeFix\_WireVertexPy*    * Fixation des arêtes déconnectées dans le fil. [commit 8c6ffc99](https   *//github.com/FreeCAD/FreeCAD/commit/8c6ffc99)


</div>

#### API en Python modifiées 


</div>

## Gestionnaire d\'Addon 

## Atelier Arch 

## Atelier Draft 

### Autres améliorations de Draft 

## Atelier FEM 

### Autres améliorations de FEM 

## Exportation

## Mesh

### Autres améliorations de Mesh 

## Atelier OpenSCAD 

## Atelier Part 

### Autres améliorations de Part 

## Atelier PartDesign 

### Autres améliorations de PartDesign 

## Atelier Path 

-   Intégration de Camotics. Si Camotics (version 1.2.2 ou ultérieure) est installé, une nouvelle icône sera ajoutée à la barre d\'outils Path. Sélectionnez une Path Tâche et appuyez sur le bouton pour ouvrir la boîte de dialogue Camotics. Faites ensuite glisser le curseur pour générer un solide simulé en tout point du travail. Vous pouvez également lancer l\'application Camotics complète pour exécuter la simulation animée. Cela entraîne un post-traitement silencieux de la tâche et la création d\'un fichier de projet camotics. [Pull request \#6637](https   *//github.com/FreeCAD/FreeCAD/pull/6637)

-   Des chaînes de substitution supplémentaires pour le nommage automatique des sorties. Si la sortie est divisée en plusieurs fichiers, les noms de fichiers peuvent automatiquement substituer le label du contrôleur d\'outil, WCS, ou le label de l\'opération. Ceci s\'ajoute aux autres chaînes de substitution existantes comme la date, le nom du travail, etc.

## Module Plot 

## Atelier Sketcher 

### Autres améliorations de Sketcher 

## Atelier Spreadsheet 

### Autres améliorations de Spreadsheet 

## Atelier TechDraw 

### Autres améliorations de TechDraw 

## Web

## Ateliers externes 

### A2plus

### Assembly3

### Assembly4

### FCGear

### Ship

## Compilation

Depuis cette version, FreeCAD ne peut être compilé qu\'avec Qt 5.x et Python 3.x. La version la plus basse de Python supportée est la 3.8 selon le [Cycle de développement de FreeCAD 1.0](FreeCAD_1.0_Development_Cycle/fr.md).

Pour compiler FreeCAD voir les instructions pour [Windows](Compile_on_Windows/fr.md), [Linux](Compile_on_Linux/fr.md) et [MacOS](Compile_on_MacOS/fr.md).

Les systèmes d\'exploitation pris en charge sont    *

-   Windows 7, 8, 10 et 11
-   Linux Ubuntu Focal Fossa (20.04) et plus récent
-   MacOS    * 10.12 Sierra ou plus récent

## Limitations connues 

### Windows 32 bits 

Depuis FreeCAD 0.19, nous ne supportons plus officiellement Windows 32 bits. FreeCAD pourrait fonctionner sur ces systèmes, mais aucun support n\'est donné.

### Bureau distant sous Windows 

Selon les capacités graphiques OpenGL d\'un ordinateur, il se peut que l\'on rencontre un plantage lors de l\'exécution de FreeCAD via le bureau à distance. Pour résoudre ce problème, mettez à jour votre pilote OpenGL. Si cela ne vous aide pas    *

-   Téléchargez [cette bibliothèque OpenGL](https   *//downloads.fdossena.com/geth.php?r=mesa64-latest) pour Windows 64 bits et extrayez-la.
-   Renommez le fichier DLL en *opengl32sw.dll* et copiez-le dans le sous-dossier *bin* du dossier d\'installation de FreeCAD (écrasez la DLL existante).

[Category   *News](Category_News.md) [Category   *Documentation](Category_Documentation.md) [Category   *Releases](Category_Releases.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [News](Category_News.md) > [Documentation](Category_Documentation.md) > [Releases](Category_Releases.md) > Release notes 1.0/fr
