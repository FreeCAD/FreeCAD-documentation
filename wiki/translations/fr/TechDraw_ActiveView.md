---
- GuiCommand:/fr
   Name:TechDraw ActiveView
   Name/fr:TechDraw Vue active
   MenuLocation:TechDraw →  Vues des autres ateliers → Insérer la vue active (dans la vue 3D)
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   Version:0.19
   SeeAlso:[TechDraw Image](TechDraw_Image/fr.md)
---

# TechDraw ActiveView/fr

## Description

L\'outil **TechDraw Vue active** insère une image bitmap de la fenêtre 3D active dans une page de dessin.

![](images/TechDraw_ActiveView_example.png ) 
*Une vue simple du modèle 3D.*



## utilisation

1.  Aller à la bonne [Vue 3D](3D_view/fr.md).
2.  S\'il y a plusieurs pages de dessin dans le document : sélectionnez éventuellement la page souhaitée dans la [Vue en arborescence](Tree_view/fr.md). Ceci n\'est pas optionnel pour {{VersionMinus/fr|0.19}}.
3.  Il existe plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_ActiveView.svg" width=16px> [Insérer la vue active (dans la vue 3D)](TechDraw_ActiveView/fr.md)**.
    -   Sélectionnez le bouton **TechDraw → Vues des autres ateliers → <img src="images/TechDraw_ActiveView.svg" width=16px> Insérer la vue active (dans la vue 3D)** dans le menu.
4.  S\'il y a plusieurs pages de dessin dans le document et que vous n\'avez pas encore sélectionné de page, la boîte de dialogue **Sélecteur de page** s\'ouvre : {{Version/fr|0.20}}
    1.  Sélectionnez la page souhaitée.
    2.  Appuyez sur le bouton **OK**.
5.  Le panneau de tâches **De la vue active à la vue TechDraw** s\'ouvre. Voir [Options](#Options.md) pour plus d\'informations.
6.  Appuyez sur le bouton **OK**.

## Options

Les éléments suivants peuvent être spécifiés :

-    **Recadrer**: recadrer le bitmap généré.

-    **Largeur**: largeur (en mm) pour recadrer la vue générée.

-    **Hauteur**: hauteur (en mm) à recadrer la vue générée.

-    **Pas d'arrière-plan**: si cette case est cochée, le bitmap généré aura un fond transparent.

-    **Arrière-plan opaque**: si cette case est cochée, le bitmap généré aura un arrière-plan de la couleur sélectionnée.

-    **Utiliser un arrière-plan 3D**: si cette case est cochée, le bitmap généré utilisera l\'arrière-plan de la fenêtre 3D.



## Remarques

-   Les Vues actives sont statiques une fois générées, elles ne sont jamais mises à jour avec les modifications apportées au modèle 3D.
-   Une Vue active est en réalité une [Image](TechDraw_Image/fr.md). Sa **Scale Type** est donc toujours initialisée comme {{Value|Custom}}.
-   Dans {{VersionMinus/fr|0.20}}, une Vue active était un [Symbole](TechDraw_Symbol/fr.md).



## Propriétés

Voir [TechDraw Image](TechDraw_Image/fr#Propri.C3.A9t.C3.A9s.md).





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw ActiveView/fr
