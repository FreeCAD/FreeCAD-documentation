# Path ToolShape/fr
{{TOCright}}

## Description

Les Formes d\'outils sont un élément essentiel du système [Path Outils](Path_Tools/fr.md). Les Formes d\'outils sont les modèles à partir desquels les Outils coupants sont créés. Elles représentent la forme physique spécifique d\'un outil. Une forme d\'outil ne décrit pas complètement l\'outil - pour cela, des paramètres supplémentaires sont nécessaires, qui seront ajoutés lorsqu\'un outil réel sera paramétré à partir du modèle.

Initialement, les Formes d\'outil sont juste des documents FreeCAD avec un seul corps créé à partir de l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier Part Design](PartDesign_Workbench/fr.md).

La création de nouvelles Formes d\'outil est un sujet avancé. Les Formes d\'outil les plus couramment utilisés existent déjà et sont fournis avec l\'installation de FreeCAD à l\'adresse suivante:

-   Sous Linux, il s\'agit généralement de `/usr/lib64/FreeCAD/Mod/Path/Tools/Shape`.
-   Sous Windows, il s\'agit généralement de `C:\Program Files\FreeCAD\Mod\Path\Tools\Shape`.
-   Sous macOS, il s\'agit généralement de `/Applications/FreeCAD/Mod/Path/Tools/Shape` {{ColoredText||Red|--> doit être révisé}}.

Ce sont :

:   
    {{FileName|ballend.fcstd}}
    

:   
    {{FileName|bullnose.fcstd}}
    

:   
    {{FileName|chamfer.fcstd}}
    

:   
    {{FileName|drill.fcstd}}
    

:   
    {{FileName|endmill.fcstd}}
    

:   
    {{FileName|probe.fcstd}}
    

:   
    {{FileName|slittingsaw.fcstd}}
    

:   
    {{FileName|thread-mill.fcstd}}
    

:   
    {{FileName|v-bit.fcstd}}
    

Elles se trouvent dans le sous-répertoire {{FileName|/Mod/Path/Tools/Shape/}} où FreeCAD a été installé.

## Utilisation

1.  Créez un nouveau document FreeCAD.
2.  Ouvrez l\'<img alt="" src=images/Workbench_PartDesign.svg  style="width:24px;"> [atelier Part Design](PartDesign_Workbench/fr.md).
3.  Créez un corps et donnez-lui une étiquette que vous voulez voir apparaître dans la sélection des outils.
4.  Créez une esquisse dans le plan XZ et dessinez la moitié du profil de l\'embout.
    -   Placez le centre supérieur de l\'embout sur l\'origine `(0,0)`.
5.  Pour toute contrainte servant de paramètre à l\'outil (comme la longueur totale), créez une contrainte nommée.
    -   Le nom est l\'étiquette du champ de saisie.
    -   Les noms sont divisés en mots aux frontières CamelCase dans la boîte de dialogue d\'édition.
    -   Utilisez un `;` dans le nom pour ajouter un texte d\'aide qui s\'affichera dans l\'info-bulle des champs de saisie.
    -   Si l\'outil est utilisé par des opérations anciennes, il devrait au moins avoir une contrainte appelée diamètre.
    -   Utilisez des lignes de construction pour les contraintes qui ne sont pas directement accessibles, comme le diamètre et l\'angle.
    -   Toute contrainte sans nom ne sera pas modifiable pour un outil spécifique.
6.  Une fois l\'esquisse entièrement contrainte, fermez l\'esquisse.
7.  Faites tourner l\'esquisse autour de l\'axe z.
8.  Enregistrez le document en tant que nouveau fichier dans le répertoire Shape.

## Images miniatures des outils 

Les outils coupants auront une petite image de l\'outil dans l\'arbre si l\'image est enregistrée avec les vignettes actives.

Remarques importantes :

-   Avant d\'enregistrer le document, assurez-vous que vous avez sélectionné Save Thumbnail et désélectionné Add program logo dans les préférences de FreeCAD.
-   Assurez-vous également de passer en vue de face et d\'adapter le contenu à l\'écran.
-   Ce que vous voyez lorsque vous enregistrez le document sera la représentation visuelle du modèle.

## Options





{{Path_Tools_navi

}}

---
[documentation index](../README.md) > [Path](Path_Workbench.md) > Path ToolShape/fr
