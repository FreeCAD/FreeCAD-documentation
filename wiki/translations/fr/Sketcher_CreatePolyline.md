---
 GuiCommand:
   Name: Sketcher CreatePolyline
   Name/fr: Sketcher Polyligne
   MenuLocation: Esquisse , Géométries d'esquisse , Créer une polyligne
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **M**
   SeeAlso: Sketcher_CreateLine/fr
---

# Sketcher CreatePolyline/fr

## Description

L\'outil <img alt="" src=images/Sketcher_CreatePolyline.svg  style="width:24px;"> [Sketcher Polyligne](Sketcher_CreatePolyline/fr.md) crée une série de segments de lignes et d\'arcs reliés par leurs extrémités. L\'outil dispose de plusieurs modes.

![](images/Sketcher_PolylineExample1.png )



*Polyligne commençant par une ligne, un arc tangent, un arc perpendiculaire puis une ligne tangente.*



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_CreatePolyline.svg" width=16px> [Créer une polyligne](Sketcher_CreatePolyline/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Géométries d'esquisse → <img src="images/Sketcher_CreatePolyline.svg" width=16px> Créer une polyligne** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_CreatePolyline.svg" width=16px> Créer une polyligne** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **M**.
2.  Le curseur se transforme en croix avec l\'icône de l\'outil.
3.  Les modes de l\'outil nécessitent un segment précédent. Effectuez l\'une des opérations suivantes :
    -   Choisissez deux points pour définir un segment de ligne.
    -   Choisissez l\'extrémité d\'un segment de ligne ou d\'arc existant (Les [contraintes automatiques](Sketcher_Workbench/fr#Contraintes_automatiques.md) doivent être activées).
4.  Vous pourvez appuyer sur la touche **M** une ou plusieurs fois pour passer d\'un mode à l\'autre pour le segment suivant. Les modes disponibles sont les suivants :
    -   Ligne perpendiculaire au segment précédent.
    -   Ligne tangentielle au segment précédent (c\'est le mode initial si le segment précédent est un arc).
    -   Arc tangentiel au segment précédent.
    -   Arc perpendiculaire (gauche) au segment précédent.
    -   Arc perpendiculaire (droite) au segment précédent.
    -   Ligne uniquement connectée au segment précédent.
5.  Lorsque vous êtes dans l\'un des modes d\'arc, vous pouvez maintenir la touche **Ctrl** enfoncée pour aimanter l\'arc par incrémentation de 45° par rapport au segment précédent.
6.  Choisissez le dernier point du segment.
7.  Vous pouvez répéter cette opération pour créer d\'autres segments.
8.  Pour terminer la saisie, effectuez l\'une des opérations suivantes :
    -   Accrochez au point de départ pour créer une polyligne fermée.
    -   Cliquez avec le bouton droit de la souris ou appuyez sur **Échap** pour créer une polyligne ouverte.
9.  Les segments de la polyligne ont été créés et les contraintes applicables ont été ajoutées.
10. Si l\'outil fonctionne en [mode continu](Sketcher_Workbench/fr#Modes_continus.md) :
    1.  Il est possible de continuer à créer des polylignes.
    2.  Pour terminer, cliquez avec le bouton droit de la souris ou appuyez sur **Échap**, ou démarrez un autre outil de création de géométrie ou de contrainte.





{{Sketcher_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher CreatePolyline/fr
