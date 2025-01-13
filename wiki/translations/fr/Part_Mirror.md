---
 GuiCommand:
   Name: Part_Mirror
   Name/fr: Part Objet en miroir
   MenuLocation: Part , Créer un objet en miroir...
   Workbenches: Part_Workbench/fr
---

# Part Mirror/fr

## Description

**Part Objet en miroir** crée un nouvel objet (image) qui est la réflexion de l\'objet source sélectionné par rapport à un plan miroir. Le plan miroir peut être un plan standard (**XY**, **YZ**, ou **XZ**) ou n\'importe quel plan parallèle à un plan standard ou ({{Version/fr|1.0}}) tout plan arbitraire en utilisant un objet de référence.

Un exemple :

![](images/PARTMirrorBeforev11.png )



*Avant*

![](images/PARTMirrorAfterv11.png )



*Après avoir été reflété par le plan YZ*



## Utilisation

![](images/PartMirroring_Scr1.png )

1.  Vous pouvez sélectionner un ou plusieurs objets sources.
2.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Part_Mirror.svg" width=16px> [Créer un objet en miroir...](Part_Mirror/fr.md)**.
    -   Sélectionnez l\'option **Part → <img src="images/Part_Mirror.svg" width=16px> Créer un objet en miroir...** du menu.
3.  Si vous n\'avez pas encore sélectionné d\'objets ou si vous souhaitez modifier la sélection : choisissez un ou plusieurs objets dans la liste **Formes**.
4.  Faites l\'une des choses suivantes :
    -   Sélectionnez un **Plan miroir** standard dans la liste déroulante.

    -   
        {{Version/fr|1.0}}
        
        : sélectionnez un objet de référence dans la [vue en arborescence](Tree_view/fr.md) ou la [vue 3D](3D_view/fr.md). L\'objet de référence peut être n\'importe quelle face plane ou arête circulaire.
5.  Appuyez sur le bouton **OK**.
6.  Pour chaque objet source, un objet Part Mirror séparé est créé.

Lorsque le bouton de sélection indique **Sélectionner**, vous êtes en mode de sélection de référence et une sélection est activée, qui interdit la sélection d\'objets de référence non pris en charge. Cliquez sur le bouton pour désactiver la sélection. Le bouton devient alors **Sélectionner la référence**.

Le plan du miroir est défini par une **Normal** (normale, direction) et une **Base** (position). Lorsque la propriété **Mirror Plane** (plan miroir) contient un objet de référence, ces propriétés sont en lecture seule car elles sont alors calculées sur la base de cet objet. Le plan est infini même si l\'objet de référence ne l\'est pas.

Un objet de référence peut être une face plane, telle que la face d\'une [Part Cube](Part_Box/fr.md), une arête circulaire, un [PartDesign Plan de référence](PartDesign_Plane/fr.md), un [plan d\'origine](App_OriginGroupExtension/fr.md) d\'un conteneur [Std Part](Std_Part/fr.md) ou tout objet ayant une seule face plane ou une seule arête circulaire. Les [liens](App_Link/fr.md) sont également pris en charge. Notez cependant que les surfaces des B-splines, telles que les [Part surfaces réglées](Part_RuledSurface/fr.md) ou les [Part Faces issues d\'un lissage](Part_Loft/fr.md) ne sont pas prises en charge.

## Options

Si un plan standard est sélectionné au lieu d\'un objet de référence, les cases **Point de base** peuvent être utilisées pour le déplacer. Seule une des cases **X**, **Y** ou **Z** est effective pour un plan standard donné.

  Plan miroir   Point de base   Résultat
    
  **XY**        **Z**           Déplace le plan du miroir le long de l\'axe **Z**.
  **XY**        **X**, **Y**    Pas d\'effet.
  **XZ**        **Y**           Déplace le plan du miroir le long de l\'axe **Y**.
  **XZ**        **X**, **Z**    Pas d\'effet.
  **YZ**        **X**           Déplace le plan du miroir le long de l\'axe **X**.
  **YZ**        **Y**, **Z**    Pas d\'effet.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme objets sources. {{Version/fr|0.20}}
-   Après avoir sélectionné un plan miroir standard, **Normal** et **Base** de l\'objet Part Mirror peuvent être remplacées par n\'importe quelle valeur. Ainsi, même sans objet de référence, vous n\'êtes pas limité aux plans standard.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/fr
