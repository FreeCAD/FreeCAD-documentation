---
- GuiCommand:
   Name:Part Sweep
   Name/fr:Part Balayage
   MenuLocation:Part - Balayage...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Lissage](Part_Loft/fr.md)
---

# Part Sweep/fr

## Description

L\'outil <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Part Balayage](Part_Sweep/fr.md) est utilisé pour créer une face, une coque ou une forme solide à partir d\'un ou plusieurs profils (coupes) projetés le long d\'une trajectoire.

L\'outil Balayage est similaire à l\'outil <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Lissage](Part_Loft/fr.md) avec l\'ajout d\'une trajectoire pour définir la projection entre les profils.

![](images/Part_Sweep_simple.png ) *Un balayage solide généré depuis un profil (A) projeté le long d\'un chemin (B).*



## Utilisation

1.  Appuyer sur le bouton **<img src="images/Part_Sweep.svg" width=16px> '''Balayage...'''**. Les paramètres de balayage s\'affichent dans le [Panneau des tâches](Task_Panel/fr.md).
2.  Dans la colonne de gauche *Profils disponibles* (précédemment *Sommet/Arête/Ligne/Face* sous la v0.16), cliquer sur l\'élément à utiliser comme profil de balayage, puis cliquer sur la flèche droite pour le placer dans la colonne de droite *Profils sélectionnés* (précédemment *Balayage* sous la v0.16). Répéter si plus d\'un profil est désiré. Utiliser les flèches haut et bas pour réorganiser les profils sélectionnés.
3.  Cliquer sur le bouton **Chemin de balayage** puis choisir l\'un des modes de sélection suivants :
    -   *Sélection de segments* : sélectionner une à une les arêtes dans la [vue 3D](3D_view/fr.md) (en maintenant la touche **Ctrl** enfoncée pour sélection multiple) puis cliquer sur le bouton **Fait**. Le balayage sera généré seulement le long des arêtes sélectionnées.
    -   *Sélection du chemin entier* : basculer vers l\'onglet Modèle, sélectionner l\'objet 2D à utiliser comme chemin dans l\'arborescence, basculer à nouveau vers le [Panneau des tâches](Task_Panel/fr.md) puis cliquer sur le bouton **Fait**. Le balayage sera généré le long de tous les arêtes contigües trouvées dans l\'objet 2D.
4.  Définir les options [Solide](#Solide.md) et [Frenet](#Frenet.md).
5.  Cliquer sur **OK**.



### Géométrie acceptée 

-   **Profils** : peuvent être un point (sommet), ligne (arête), polyligne ou une face. Arêtes et polylignes peuvent être soit ouvertes ou fermées. Il existe différentes [Limitations et complications du profil](#Limitations_et_complications_du_profil.md), voir ci-dessous. Cependant, les profils peuvent provenir des primitives de l\'atelier Part, de fonctions de l\'atelier Draft et d\'esquisses.

-   **Chemin** : peut être une ligne (arête) ou une série de lignes de connexion, polyligne ou différentes primitives de l\'atelier Part, une fonction de l\'atelier Draft ou un esquisse. Le chemin est souvent sélectionné directement depuis la fenêtre du modèle principal, mais il peut aussi être choisi parmi la [vue en arborescence](Tree_view/fr.md) (onglet Modèle de la [Vue Combinée](Combo_view/fr.md)). Le chemin peut être soit une forme entière appropriée ou une sous-composante appropriée d\'une forme plus avancée (par exemple, une arête d\'un <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md) pourrait être choisi comme chemin). Le chemin peut être ouvert ou fermé et créer ainsi un balayage soit ouvert ou fermée. Un chemin fermé tel que la partie d\'un cercle se traduira par un balayage fermé. Par exemple, un balayage d\'un petit cercle autour d\'un chemin d\'un cercle plus large va créer un tore.

-   Les objets [App Link](App_Link/fr.md) liés aux types d\'objets appropriés et les conteneurs [App Part](App_Part/fr.md) contenant les objets visibles appropriés peuvent également être utilisés comme profils et trajectoires. {{Version/fr|0.20}}



## Propriétés



### Solide

Si \"Créer le solide\" est défini à \"vrai\", FreeCAD crée un solide, pourvu que les profils forment une géométrie fermée; si défini à \"faux\", FreeCAD crée une face ou (si plus d\'une face) crée une coque pour les profils ouverts ou fermés.

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

La propriété \"Frenet\" contrôle la façon dont l\'orientation du profil change quand il suit la trajectoire de balayage. Si \"Frenet\" est \"faux\", l\'orientation du profil est maintenu cohérent point à point. La forme qui en résulte présente le moins de torsion possible. De manière peu intuitive, lorsqu\'un profil est balayé le long d\'une hélice, il en résulte que l\'orientation du profil glisse (tourne) lentement en suivant l\'hélice. Le réglage de \"Frenet\" à vrai empêche une telle dérive.

Si \"Frenet\" est à \"vrai\", l\'orientation du profil est calculée à partir de la courbure et des vecteurs tangents du chemin. Cela permet de maintenir l\'orientation du profil uniforme lors du balayage le long d\'une hélice (parce que vecteur de courbure d\'une hélice droite pointe toujours vers son axe). Toutefois, lorsque le chemin n\'est pas une hélice, la forme obtenue peut parfois avoir d\'étranges torsions. Pour plus d\'informations, voir [Repère de Frenet](https://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet).

### Transition

\"Transition\" définit le style de transition du Balayage à un joint de la trajectoire, si la trajectoire ne définit pas la transition d\'angle (par exemple lorsque la trajectoire est une polyligne). La propriété n\'est pas indiquée dans le [Panneau des tâches](Task_panel/fr.md) et peut être trouvée dans les propriétés après que le balayage ait été créé.



## Limitations et complications du profil 

-   Un sommet ou un point
    -   Un sommet ou un point ne peut être utilisé que comme premier et/ou dernier profil dans la liste des profils.
        -   Par exemple
            -   vous ne pouvez pas effectuer un balayage d\'un cercle à un point, puis à une ellipse.
            -   par contre, vous pouvez effectuer un balayage à partir d\'un point, d\'un cercle, d\'une ellipse et d\'un autre point.
-   Les profils de géométrie ouverte ou fermée ne peuvent pas être mélangés dans un seul sweep.
    -   Dans un même balayage, tous les profils (lignes, polylignes, etc.) doivent être ouverts ou fermés.
        -   Par exemple
            -   FreeCAD ne peut pas effectuer un balayage entre un Part cercle et une Part ligne par défaut.
-   Fonctions de l\'atelier Draft
    -   Les fonctions de l\'atelier Draft peuvent être utilisées directement comme profil dans FreeCAD 0.14 ou plus.
        -   Par exemple, les fonctions suivantes peuvent être utilisées comme profils dans un Part Balayage
            -   polygone.
            -   point, ligne, polyligne
            -   B-spline, courbe de Bézier
            -   cercle, ellipse, rectangle
-   PartDesign Esquisses
    -   Le profil peut être créé avec une esquisse. Toutefois, seule une esquisse valide sera affichée dans la liste et pourra être sélectionnée.
    -   L\'esquisse ne doit contenir qu\'une seule polyligne ou ligne ouverte ou fermée (il peut s\'agir de plusieurs lignes, si ces lignes sont toutes connectées telles quelles, elles constituent alors une seule polyligne).
-   Atelier Part
    -   Le profil peut être une Part primitive géométrique valide, qui peut être créée à l\'aide des [Part Outils primitives](Part_Primitives/fr.md).
        -   Par exemple, les Part primitives géométriques suivantes peuvent constituer un profil valide
            -   point (sommet), ligne (arête)
            -   hélice, spirale
            -   cercle, ellipse
            -   polygone régulier
            -   plan (face)



## Liens

-   La fonction Balayage est souvent utilisée pour créer des filets de vis, nous vous suggérons la lecture du [Tutoriel création de vis](Thread_for_Screw_Tutorial/fr.md).



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/fr
