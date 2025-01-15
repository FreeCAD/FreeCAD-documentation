---
 GuiCommand:
   Name: Sketcher Trimming
   Name/fr: Sketcher Ajuster
   MenuLocation: Esquisse , Outils d'esquisse , Ajuster une arête
   Workbenches: Sketcher_Workbench/fr
   Shortcut: **G** **T**
   Version: 0.12
   SeeAlso: Sketcher_Split/fr, Sketcher_Extend/fr
---

# Sketcher Trimming/fr

## Description

L\'outil <img alt="" src=images/Sketcher_Trimming.svg  style="width:24px;"> [Sketcher Ajuster](Sketcher_Trimming/fr.md) ajuste une arête aux intersections les plus proches avec d\'autres arêtes. Si l\'arête sélectionnée ne croise pas d\'autres arêtes, elle sera supprimée.



## Utilisation

Voir aussi : [Aides au dessin](Sketcher_Workbench/fr#Aides_au_dessin.md).

1.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/Sketcher_Trimming.svg" width=16px> [Ajuster une arête](Sketcher_Trimming/fr.md)**.
    -   Sélectionnez l\'option **Esquisse → Outils d'esquisse → <img src="images/Sketcher_Trimming.svg" width=16px> Ajuster une arête** du menu.
    -   Cliquez avec le bouton droit de la souris dans la [vue 3D](3D_view/fr.md) et sélectionnez l\'option **<img src="images/Sketcher_Trimming.svg" width=16px> Ajuster une arête** du menu contextuel.
    -   Utilisez le raccourci clavier : **G** puis **T**.
2.  S\'il y a une précédente sélection, elle est effacée. L\'outil n\'accepte pas de présélection.
3.  Le curseur se transforme en croix avec l\'icône de l\'outil.
4.  Il existe deux modes :
    -   Ajustage par simple clic :
        1.  Déplacez le curseur sur une partie de l\'arête à ajuster.
        2.  L\'arête est mis en évidence et les points d\'ajustage sont marqués par des cercles temporaires.
        3.  Cliquez pour confirmer.
        4.  L\'arête est ajusté aux points marqués.
    -   Maintenir et faire glisser l\'ajustage : {{Version/fr|1.0}}
        1.  Maintenir le bouton gauche de la souris enfoncé.
        2.  Déplacez le curseur sur les parties des arêtes à ajuster.
        3.  L\'ajustage s\'effectue immédiatement.
        4.  Relâchez le bouton gauche de la souris.
5.  Si une partie est ajustée, les contraintes existantes applicables sont transférées à la nouvelle arête résultante. Des [contraintes Point sur objet](Sketcher_ConstrainPointOnObject/fr.md) sont ajoutées entre le(s) point(s) d\'extrémité de l\'arête ajustée et le(s) arête(s) découpé(s).
6.  Cet outil fonctionne toujours en mode continu : il est possible de continuer à ajuster des arêtes.
7.  Pour terminer, cliquez dans une zone vide de la [vue 3D](3D_view/fr.md), cliquez avec le bouton droit de la souris, ou appuyez sur **Échap** ou démarrez un autre outil de création de géométrie ou de contrainte.



---
⏵ [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher Trimming/fr
