---
- GuiCommand:
   Name: Part JoinEmbed
   Name/fr: Part Intégrer
   MenuLocation: Part - Joindre - Intégrer un objet
   Workbenches: [Part](Part_Workbench/fr.md)
   Version: 0.16
   SeeAlso: [Part Connecter](Part_JoinConnect/fr.md), [Part Découper](Part_JoinCutout/fr.md), [Part Opération booléenne](Part_Boolean/fr.md), [Part Évidement](Part_Thickness/fr.md)
---

# Part JoinEmbed/fr

## Description

L\'outil Intégrer un objet incorpore un objet à paroi (un tuyau, par exemple) dans un autre objet à paroi.

![600px](images/JoinFeatures_Embed.png)

## Utilisation

1.  Sélectionnez d\'abord l\'objet de base, puis l\'objet à intégrer. L\'ordre de sélection est important. Il suffit de sélectionner une sous-forme de chaque objet (par exemple, des faces).
2.  Lancez la commande Intégrer un objet.

Un objet Part Intégrer est créé, avec le mode défini sur \'Embed\' (Intégré). Les objets originaux sont masqués et le résultat de l\'intégration est affiché dand la vue 3D.

## Propriétés


{{TitleProperty|Base}}

-    **Base**: Référence à l\'objet de base (celui dans lequel l\'autre objet doit être incorporé). L\'objet doit être un seul solide.

-    **Tool**: Référence à l\'objet Insert (l\'objet à incorporer). L\'objet peut être un solide unique ou un [composé valide](Part_Compound/fr.md) de solides.

-    **Mode**: Le mode opératoire est égal à \'Intégrer\' (Changer ce qui transformera l\'Insert en une autre Part_JoinXXX). La valeur \'bypass\' peut être utilisée pour désactiver temporairement les calculs longs (un composé de Base et Insert sera créé, ce qui est une opération rapide).

-    **Refine**: Définit si l\'opération [Affiner](Part_RefineShape/fr.md) doit être appliquée ou non à la forme finale. La valeur par défaut est déterminée par une case à cocher \"Affiner automatiquement la forme après l\'opération booléenne\" dans les préférences de PartDesign. Lorsque la propriété Mode est réglée sur \"bypass\", Affiner est ignoré (jamais appliqué).

## Exemple

1.  Créez un tuyau en appliquant [évidement (ou coque)](Part_Thickness/fr.md) à un [cylindre](Part_Cylinder/fr.md) :
    <img alt="" src=images/JoinFeatures_Example_step1.png  style="width:320px;">
2.  Créez un autre tuyau de plus petit diamètre et placez-le de manière à ce qu\'il perce la paroi du premier tuyau :
    ![320px](images/JoinFeatures_Example_step2.png)
3.  Sélectionnez le premier tuyau, puis le second (l\'ordre de sélection est important), puis cliquez sur l\'option \"Intégrer l\'objet\" dans le bouton de la barre d\'outils déroulante Outils de jointure.
    ![320px](images/JoinFeatures_Example_step3_Embed.png)
4.  Utilisez un outil de section ([Std Créer une section \...](Std_ToggleClipPlane/fr.md), [Arch Plan de coupe](Arch_SectionPlane/fr.md), [Arch Couper selon un plan](Arch_CutPlane/fr.md)) pour afficher les éléments internes. Sur la photo ci-dessous, le plan de coupe Arch est utilisé.
    ![320px](images/JoinFeatures_Example_step4_Embed.png)

## Algorithme

Les algorithmes derrière les outils Joindre sont assez simples et leur compréhension est importante pour utiliser les outils correctement.

1\. L\'objet de base est [soustraction booléenne](Part_Cut/fr.md) avec l\'objet Insert. La forme résultante est un ensemble ([composé](Part_Compound/fr.md)) de solides non sécants (généralement deux).

2\. Le composé résultant est filtré : seul le plus grand solide est conservé.

3\. Le plus grand solide est une [Union](Part_Fuse/fr.md) avec l\'objet Tool.

4\. Si la propriété Affiner est vraie, la forme résultante est [affinée](Part_RefineShape/fr.md).
![800px](images/_JoinFeatures-Algo-Embed.png)

### Remarques

-   Si après l'étape 1, l'objet reste en un seul morceau, le résultat de l'intégration sera équivalent à une [Part union](Part_Fuse/fr.md) de Base et de Tool, mais dont le calcul prendra plus de temps.
-   Actuellement, l\'outil produira un résultat inattendu si un composé est fourni comme Base. Cela pourra être changé dans le futur.
-   Étant donné que la plus grande pièce est déterminée en comparant les volumes des pièces, l\'outil ne peut fonctionner qu\'avec des solides. Cela pourra être changé dans le futur.

## Script

L\'outil Joindre peut être utilisé dans des [macros](macros/fr.md) à partir de la console Python en utilisant la fonction suivante :


```pythonJoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed')```

-   Crée une fonction Intégration vide (ou une autre fonction de jointure, selon le mode transmis). Les propriétés Base et Insert doivent être affectées explicitement, après.
-   Renvoie l\'objet nouvellement créé.

Exemple :


{{code|code=
import JoinFeatures
j = JoinFeatures.makePartJoinFeature(name = 'Embed', mode = 'Embed' )
j.Base = FreeCADGui.Selection.getSelection()[0]
j.Tool = FreeCADGui.Selection.getSelection()[1]
}}

L\'outil lui-même est implémenté en Python, voir **/Mod/Part/JoinFeatures.py** ([Github link](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Part/JoinFeatures.py)) là où FreeCAD est installé.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part JoinEmbed/fr
