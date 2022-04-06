---
- GuiCommand:/fr
   Name:Part JoinCutout
   Name/fr:Part Découpe
   |MenuLocation:Part → Joindre → Découpe pour objet
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.16
   SeeAlso:[Part Connecter](Part_JoinConnect/fr.md), [Part Intégrer](Part_JoinEmbed/fr.md), [Part Opération booléenne](Part_Boolean/fr.md), [Part Évidement](Part_Thickness/fr.md)
---

# Part JoinCutout/fr

## Description

L\'outil <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> [Part Découpe](Part_JoinCutout/fr.md) crée une découpe dans un objet muré (par exemple, un tuyau) pour s\'adapter à un autre objet à paroi.

![600px](images/JoinFeatures_Cutout.png)

## Utilisation

1.  Sélectionnez d\'abord l\'objet de base, puis l\'objet pour définir la découpe.
    L\'ordre de sélection est important. Il suffit de sélectionner une sous-forme de chaque objet (par ex. des faces).
2.  Appelez la commande Part Découpe de plusieurs manières :
    -   En appuyant sur le bouton <img alt="" src=images/Part_JoinCutout.svg  style="width:24px;"> [Part Découpe](Part_JoinCutout/fr.md) dans la barre d\'outils Part
    -   Utilisation de l\'entrée **Part → Joindre → Découpe de l'objet** dans le menu Part

Un objet Part JoinFeature est créé avec le mode défini sur \'Cutout\' (Découpe). Les objets originaux sont masqués et le résultat de la découpe est affiché dans la [vue 3D](3D_view/fr.md).

## Propriétés


{{TitleProperty|Base}}

-    **Base**: Référence à l\'objet de base (celui dans lequel on veut faire la découpe). L\'objet doit être un solide unique.

-    **Tool**: Référence à l\'objet Empreinte (l\'objet à utiliser pour la découpe). L\'objet peut être un solide unique ou un [composé valide](Part_Compound/fr.md) de solides.

-    **Mode**: Le mode de fonctionnement est égal à \'Cutout\' (Découpe) (Changement qui transformera l\'Empreinte en une autre Part\_JoinXXX). La valeur \'bypass\' peut être utilisée pour désactiver temporairement les calculs longs (un composé composé de Base et d\'Empreinte sera créé, ce qui est une opération rapide).

-    **Refine**: définit s\'il faut appliquer l\'opération [Part Affiner](Part_RefineShape/fr.md) ou non, à la forme finale. La valeur par défaut est déterminée par la case à cocher \"Affiner automatiquement la forme après l\'opération booléenne\" dans les préférences de PartDesign. Lorsque la propriété Mode est \'bypass\', affiner est ignoré (jamais appliqué).

## Exemple

1.  Créez un tuyau en appliquant [Part évidement](Part_Thickness/fr.md) à un [cylindre](Part_Cylinder/fr.md) :
    ![320px](images/JoinFeatures_Example_step1.png)
2.  Créez un autre tuyau de plus petit diamètre et placez-le de manière à ce qu\'il perce la paroi du premier tuyau :
    ![320px](images/_JoinFeatures_Example_step2.png)
3.  Sélectionnez le premier tuyau, puis le second (l\'ordre de sélection est important), puis cliquez sur l\'option \'Découpe pour l\'objet\' dans le bouton de la barre d\'outils déroulante Outils de jointure.
    ![320px](images/JoinFeatures_Example_step3_Cutout.png)

## Algorithme

Les algorithmes derrière les outils Joindre sont assez simples et leur compréhension est importante pour utiliser les outils correctement.

1\. L\'objet de base subit une [soustraction booléenne](Part_Cut/fr.md) de l\'objet Empreinte. La forme résultante est un ensemble ([composé](Part_Compound/fr.md)) de solides non sécants (généralement deux).

2\. Le composé résultant est filtré : seul le plus grand solide est conservé.

3\. Si la propriété Refine (Affiner) est vraie, la forme résultante est [affinée](Part_RefineShape/fr.md).
![800px](images/JoinFeatures-Algo-Cutout.png)

### Remarques

-   Si après l'étape 1, l'objet reste en un seul morceau, le résultat de la découpe sera équivalent à une [Part Soustraction booléenne](Part_Cut/fr.md) de la base et de l'empreinte.
-   Actuellement, l\'outil produira un résultat inattendu, si un composé est fourni comme base. Cela pourra être changé dans le futur.
-   Étant donné que la plus grande pièce est déterminée en comparant les volumes des pièces, l\'outil ne peut fonctionner qu\'avec des solides. Cela pourra être changé dans le futur.

## Script

L\'outil Joindre peut être utilisé dans des [macros](macros/fr.md) à partir de la console Python en utilisant la fonction suivante :


```pythonJoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout')```

-   Crée une fonction Cutout (découpe) vide (ou une autre fonction Joindre, selon le mode sélectionné). Les propriétés Base et Tool (empreinte) doivent ensuite être attribuées explicitement.
-   Retourne le nouvel objet créé.

Exemple : {{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Cutout', mode = 'Cutout' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

L\'outil lui-même est implémenté en Python, voir {{FileName|/Mod/Part/JoinFeatures.py}} ([Github link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) là où FreeCAD est installé.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinCutout/fr
