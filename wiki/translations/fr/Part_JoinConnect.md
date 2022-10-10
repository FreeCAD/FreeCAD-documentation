---
- GuiCommand   */fr
   Name   *Part JoinConnect
   Name/fr   *Part Connecter des objets
   MenuLocation   *Part → Joindre → Connecter des objets
   Workbenches   *[Part](Part_Workbench/fr.md)
   Version   *0.16
   SeeAlso   *[Part Intégrer](Part_JoinEmbed/fr.md), [Part Découper](Part_JoinCutout/fr.md), [Part Opération booléenne](Part_Boolean/fr.md), [Part Évidement](Part_Thickness/fr.md)
---

# Part JoinConnect/fr

## Description

Outil de connexion pour joindre deux objets creux (par exemple deux tuyaux). Peut aussi joindre des coques et des fils.

![600px](images/JoinFeatures_Connect.png)

## Utilisation

1.  Sélectionnez les objets à connecter.
    L\'ordre de sélection n\'est pas important car l\'action de l\'outil est symétrique. Il suffit de sélectionner un élément de chaque objet (par ex. leurs faces). Vous pouvez également sélectionner un composé contenant toutes les formes à connecter, par ex. [Draft Réseau orthogonal](Draft_OrthoArray/fr.md).
2.  Lancez la commande Part Connecter des objets de plusieurs manières   *
    -   Appuyez sur le bouton <img alt="" src=images/Part_JoinConnect.svg  style="width   *24px;"> [Connecter des objets](Part_JoinConnect/fr.md) dans la barre d\'outils Part
    -   Utilisez l\'entrée **Part → Joindre → Connecter des objets** dans le menu Part

Un objet paramétrique Connect est créé. Les objets d\'origine sont cachés et le résultat de l\'intersection est affiché dans la [vue 3D](3D_view/fr.md).

## Propriétés


{{TitleProperty|Connect}}

-    **Objects**   * Liste les objets a connecter. En général deux objets suffisent, un compound d\'objets fonctionne (Depuis V0.17, cette propriété n\'est pas affichée dans l\'[éditeur de propriétés](Property_editor/fr.md) mais seulement disponible via [Python](#Script.md)).

-    **Refine**   * choisir d\'appliquer ou non un [Affinage de forme](Part_RefineShape/fr.md) sur la forme finale. Par défaut cette valeur est déterminée par la case *Affiner les modèles automatiquement après une opération booléenne* dans les [PartDesign Préférences](PartDesign_Preferences/fr.md).

-    **Tolerance**   * Valeur de \"flou\". Il s\'agit d\'une tolérance supplémentaire à appliquer lors de la recherche d\'intersections, en plus des tolérances stockées dans les formes d\'entrée.

## Exemple

1.  Créer un tuyau en appliquant un [Part évidement](Part_Thickness/fr.md) sur un [Part cylindre](Part_Cylinder/fr.md)    *
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Créer un autre tuyau plus petit, et le [Part placer](Placement/fr.md) pour qu\'il perce le premier tuyau    *
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Sélectionner le premier tuyau puis le second, et cliquer sur l\'option \'Connecter des objets\' du menu déroulant Joindre des objets à paroi.
    ![320px](images/JoinFeatures_Example_step3_Connect.png)
4.  Utiliser divers outils de plan de coupe ([Std Créer une section \...](Std_ToggleClipPlane/fr.md), [Arch Plan de section](Arch_SectionPlane/fr.md), [Arch Couper selon un plan](Arch_CutPlane/fr.md)) pour voir l\'intérieur. Dans l\'image ci-dessous, Arch Section Plane est utilisé.
    ![320px](images/JoinFeatures_Example_step4_Connect.png)

## Algorithme

Les algorithmes derrière les outils Joindre sont très simples, et les comprendre est important pour utiliser les outils correctement. L\'algorithme de Connecter, en particulier, est plus complexe que les autres, mais il suffit généralement d\'y penser comme d\'une variante symétrique de l\'[algorithme intégré](Part_JoinEmbed/fr#Algorithme.md).

1\. Chaque objet est coupé à l\'intersection avec l\'autre (voir [Part Fragments booléens](Part_BooleanFragments/fr.md))

2\. Parmi les morceaux d\'un objet, seul le plus grand est conservé ; tout le reste est jeté.

3\. Les pièces d\'intersection qui touchent au moins deux objets sont ajoutées au résultat. Ensuite, les pièces sont jointes pour former le résultat de Connecter.

### Remarques

-   Si, à l\'étape 1, chaque objet reste en un seul morceau, le résultat de Connecter sera équivalent à la [Part Union](Part_Fuse/fr.md) des objets.
-   Actuellement, tous les composés fournis sont explosés avant la connexion. Cela signifie que les composés à intersection automatique, qui ne sont pas valides pour toutes les autres opérations booléennes, sont valables pour Connecter. (Cela pourra être changé à l\'avenir.)
-   La \"plus grande\" pièce est celle qui a la plus grande masse. C\'est-à-dire que pour les solides, les volumes sont comparés; pour les coques et les faces, les zones sont comparées, etc.
-   Depuis FreeCAD v0.17.8053, et si la version OCC est la version 6.9.0 et ultérieure, Connecter est presque aussi rapide que toutes les autres opérations booléennes. Pour les versions plus anciennes, Connecter est environ 5 fois plus lent qu\'une opération booléenne normale et ne fonctionne que sur les solides.

## Script

L\'outil Joindre peut être utilisé dans des [macros](Macros/fr.md) à partir de la [console Python](Python_console/fr.md) en utilisant la fonction suivante    *

**BOPTools.JoinFeatures.makeConnect(name)**

-   Crée une fonction Connect vide. La propriété \'Objets\' doit être attribuée explicitement par la suite.
-   Renvoie l\'objet nouvellement créé.

Connecter peut également être appliqué à des formes simples, sans avoir besoin d\'un objet document, via    *

**Part.BOPTools.JoinAPI.connect(list_of_shapes, tolerance = 0.0)**

Cela peut être utile pour créer des fonctionnalités de script personnalisées Python.

Exemple    *


{{code|code=
import Part
j = Part.BOPTools.JoinFeatures.makeConnect(name= 'Connect')
j.Objects = FreeCADGui.Selection.getSelection()
}}

L\'outil lui-même est implémenté en Python, voir **/Mod/Part/BOPTools/JoinFeatures.py** ([Github lien](https   *//github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/BOPTools/JoinFeatures.py)) là où FreeCAD est installé.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinConnect/fr
