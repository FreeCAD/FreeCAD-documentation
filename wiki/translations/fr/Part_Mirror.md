---
- GuiCommand:
   Name: Part_Mirror
   Name/fr: Part Miroir
   MenuLocation: Part - Mise en miroir...
   Workbenches: [Part](Part_Workbench/fr.md)
---

# Part Mirror/fr

## Description

**Part Miroir** crée un nouvel objet (image) qui est la réflexion de l\'objet source sélectionné par rapport à un plan miroir. Le plan miroir peut être un plan standard (**XY**, **YZ**, ou **XZ**) ou n\'importe quel plan parallèle à un plan standard.

Un exemple :

![Avant](images/PARTMirrorBeforev11.png )

![Après (symétrisé par rapport au plan **YZ**)](images/PARTMirrorAfterv11.png ) 



## Utilisation

![](images/PARTMirrorDialogv11.png )

1.  Sélectionnez l\'objet source dans la liste du panneau de mise en miroir.
2.  Sélectionnez un **Plan miroir** standard dans le menu déroulant.
3.  Appuyez sur **OK** pour créer l\'objet image.




## Options

Les cases **Point de base** peuvent être utilisées pour déplacer le miroir plan parallèle au plan de standard sélectionné. Seul l\'une des cases **X**, **Y** ou **Z** est active pour un plan standard donné.

  Plan miroir   Point de base   Résultat
    
  **XY**        **Z**           Déplace le plan de symmétrie le long de l\'axe **Z**.
  **XY**        **X**, **Y**    Pas d\'effet.
  **XZ**        **Y**           Déplace le plan de symmétrie le long de l\'axe **Y**.
  **XZ**        **X**, **Z**    Pas d\'effet.
  **YZ**        **X**           Déplace le plan de symmétrie le long de l\'axe **X**.
  **YZ**        **Y**, **Z**    Pas d\'effet.



## Remarques

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme objets sources. {{Version/fr|0.20}}
-   Les plans de miroir arbitraires (c\'est-à-dire non parallèles à un plan standard) ne sont pas pris en charge.



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Mirror/fr
