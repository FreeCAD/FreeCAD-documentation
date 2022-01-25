---
- GuiCommand:/fr
   Name:Part Sweep
   Name/fr:Part Balayage
   MenuLocation:Pièce → Balayage...
   Workbenches:[Part](Part_Workbench/fr.md)
   SeeAlso:[Part Lissage](Part_Loft/fr.md)
---

# Part Sweep/fr

## Description

L\'outil <img alt="" src=images/Part_Sweep.svg  style="width:24px;"> [Part Balayage](Part_Sweep/fr.md) est utilisé pour créer une face, une enveloppe ou une forme solide à partir d\'un ou plusieurs profils (coupes) projetés le long d\'un chemin.

L\'outil de balayage est similaire à l\'outil <img alt="" src=images/Part_Loft.svg  style="width:24px;"> [Part Lissage](Part_Loft/fr.md) avec l\'ajout d\'un chemin pour définir la projection entre les profils.

![](images/Part_Sweep_simple.png ) *Un balayage solide généré depuis un profil (A) projeté le long d\'un chemin (B).*

## Utilisation

1.  Appuyer sur le bouton **<img src="images/Part_Sweep.svg" width=16px> '''Balayage'''**. Les paramètres de balayage s\'affichent dans le [Panneau des tâches](Task_Panel/fr.md).
2.  Dans la colonne de gauche *Profils disponibles* (précédemment *Sommet/Arête/Ligne/Face* sous la v0.16), cliquer sur l\'élément à utiliser comme profil de balayage, puis cliquer sur la flèche droite pour le placer dans la colonne de droite *Profils sélectionnés* (précédemment *Balayage* sous la v0.16). Répéter si plus d\'un profil est désiré. Utiliser les flèches haut et bas pour réorganiser les profils sélectionnés.
3.  Cliquer sur le bouton **Chemin de balayage** puis choisir l\'un des modes de sélection suivants :
    -   *Sélection de segments* : sélectionner une à une les arêtes dans la [vue 3D](3D_view/fr.md) (en maintenant la touche **CTRL** enfoncée pour sélection multiple) puis cliquer sur le bouton **Fait**. Le balayage sera généré seulement le long des arêtes sélectionnées.
    -   *Sélection du chemin entier* : basculer vers l\'onglet Modèle, sélectionner l\'objet 2D à utiliser comme chemin dans l\'arborescence, basculer à nouveau vers le [Panneau des tâches](Task_Panel/fr.md) puis cliquer sur le bouton **Fait**. Le balayage sera généré le long de tous les arêtes contigües trouvées dans l\'objet 2D.
4.  Définir les options [Solide](#Solide.md) et [Frenet](#Frenet.md).
5.  Cliquer sur **OK**.

### Géométrie acceptée 

-   **Profils** : peuvent être un point (sommet), ligne (Arête), filaire ou une face. Arêtes et filaires peuvent être soit ouverts ou fermés. Il existe différentes [Limitations et complications du profil](Part_Sweep/fr#Profil__Limitations_et_complications.md), voir ci-dessous. Cependant, les profils peuvent provenir des primitives de l\'atelier Part, de fonctions de l\'atelier Draft et d\'esquisses.

-   **Chemin** : peut être une ligne (Arête) ou une série de lignes de connexion, filaire ou différentes primitives de l\'atelier Part, une fonction de l\'atelier Draft ou un esquisse. Le chemin est souvent sélectionné directement depuis la fenêtre du modèle principal, mais il peut aussi être choisi parmi la [vue en arborescence](Tree_view/fr.md) (onglet Modèle de la [Vue Combinée](Combo_view/fr.md)). Le chemin peut être soit une forme entière appropriée ou une sous-composante appropriée d\'une forme plus avancée (par exemple, une arête d\'un <img alt="" src=images/Part_Box.svg  style="width:24px;"> [Part Cube](Part_Box/fr.md) pourrait être choisi comme chemin). Le chemin peut être ouvert ou fermé et créer ainsi un balayage soit ouvert ou fermée. Un chemin fermé tel que la partie d\'un cercle se traduira par un balayage fermé. Par exemple, un balayage d\'un petit cercle autour d\'un chemin d\'un cercle plus large va créer un tore.

## Propriétés

### Solide

Si \"Solide\" est défini à \"true\" (vrai), FreeCAD crée un solide, pourvu que les profils forment une géométrie fermée; si défini à \"false\" (faux), FreeCAD crée une face ou (si plus d\'une face) crée une coque pour les profils ouverts ou fermés.

### Frenet

<img alt="" src=images/Sweep-frenet-comp.png  style="width:500px;">

Les propriétés \"Frenet\" contrôlent la façon dont l\'orientation du profil change quand il suit la trajectoire de balayage. Si \"Frenet\" est \"false\" (faux), l\'orientation du profil est maintenu cohérent point à point. La déformation minimum a la torsion. Non intuitivement, lorsqu\'un profil est balayé le long d\'une hélice, il en résulte une orientation du profil glissant lentement (en rotation), quand il suit l\'hélice. Régler \"Frenet\" a \"true\", on évite ce genre de dérive.

Si \"Frenet\" est à \"true\", l\'orientation du profil est calculée à partir de la courbure et des vecteurs tangents du chemin. Cela permet de maintenir l\'orientation du profil uniforme lors du balayage le long d\'une hélice (parce que vecteur de courbure d\'une hélice droite pointe toujours vers son axe). Toutefois, lorsque le chemin n\'est pas une hélice, la forme obtenue peut parfois avoir d\'étranges torsions. Pour plus d\'informations, voir [Repère de Frenet](https://fr.wikipedia.org/wiki/Rep%C3%A8re_de_Frenet).

### Transition

\"Transition\" définit le style de transition du Balayage joint dans le chemin, si le chemin ne définit pas la transition d\'angle (par exemple, lorsque le chemin est un fil). La propriété n\'est pas indiquée dans le [Panneau des tâches](Task_panel/fr.md) et peut être trouvée dans les propriétés après que le Balayage a été créé.

## Profil: Limitations et complications 

-   Un sommet ou un point
    -   Un sommet ou un point ne peuvent être utilisés comme le premier et / ou le dernier profil dans la liste des profils.
        -   Par exemple
            -   vous ne pouvez pas balayer d\'un cercle à un point, à une ellipse.
            -   Cependant vous pourriez Balayer d\'un point à un cercle à une ellipse à un autre point.
-   Les Profils géométrique ouvert ou fermé ne peuvent pas être mélangés dans un seul balayage
    -   Dans un balayage, tous les profils (lignes, fils etc.) doivent être soit ouvert ou fermé.
        -   Par exemple
            -   FreeCAD ne peut pas balayer entre un Cercle et une Ligne par défaut.
-   Atelier Draft (planche à dessin) projets
    -   Les projets de l\'Atelier Draft peuvent être directement utilisés comme un profil dans FreeCAD 0,14 ou versions plus élevées.
        -   Par exemple, les projets suivants de Draft peuvent être utilisés comme profils dans un Balayage
            -   Polygone.
            -   Point, ligne, fil,
            -   B-spline, Courbe de Bézier
            -   Cercle, Ellipse, Rectangle
-   PartDesign Sketches (Conception de Pièces Esquisse)
    -   Le profil peut être créé avec un croquis. Toutefois, seule une esquisse valide sera affichée dans la liste pour être disponible pour la sélection.
    -   Le croquis doit contenir un seul fil ou ligne ouverte ou fermée (peut être plusieurs lignes, si ces lignes sont toutes connectées car elles représentent alors un seul fil)
-   Part Workbench (Atelier Pièce)
    -   Le profil peut être une primitive géométrique valide qui peut être créé avec l\'outil [Primitives](Part_Primitives/fr.md)
        -   par exemple les primitives géométriques suivantes peuvent être un profil valide
            -   Point (Sommet), ligne (Arête)
            -   Hélice, Spirale
            -   Cercle, Ellipse
            -   Polygone régulier
            -   Plan (Face)

## Liens

-   Puisque la fonction Balayage est souvent utilisée pour créer des filets de vis, nous vous suggérons la lecture du [Tutoriel création de vis](Thread_for_Screw_Tutorial/fr.md).



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part Sweep/fr
