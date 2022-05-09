---
- GuiCommand   */fr
   Name   *Std DependencyGraph
   Name/fr   *Std Graphique de dépendances
   MenuLocation   *Outils → Graphique de dépendance...
   Workbenches   *Tous
---

# Std DependencyGraph/fr

## Description

La commande **Std Graphique de dépendances** affiche les dépendances entre les objets du document actif dans un\' graphique de dépendance \'. Contrairement à la [Vue en arborescence](Tree_view/fr.md), les objets sont répertoriés dans l\'ordre chronologique inverse, avec le premier objet créé en bas.

Il peut être utile pour analyser un document FreeCAD et localiser des fourches dans l\'arborescence. La forme du graphe dépendra de l\'atelier utilisé pour créer les objets du document. Par exemple, un modèle créé exclusivement dans l\'[atelier PartDesign](PartDesign_Workbench/fr.md) peut afficher un graphique de dépendances linéaire avec une seule branche verticale. Un modèle fait sous l\'[atelier Part](Part_Workbench/fr.md) sera formé de plusieurs branches, mais pour une pièce unique, celles-ci se joindront au sommet après des opérations [Part Booléennes](Part_Boolean/fr.md). Si ce n\'est pas le cas alors il s\'agit d\'objets distincts.

Le graphique de dépendance est un outil purementde visualisation. Il ne peut donc pas être édité. Il se met automatiquement à jour si des changements sont apportés au modèle.

<img alt="" src=images/Std_DependencyGraph_example.svg  style="width   *400px;"> 
*Exemple de graphe de dépendances avec un corps PartDesign à gauche et un objet créé avec des opérations Part à droite*

## Installation

Pour utiliser la commande, un logiciel tiers nommé [Graphviz](http   *//graphviz.org/) doit être installé. Si vous ne l\'avez pas préinstallé ou s\'il est installé dans un emplacement non conventionnel, FreeCAD affichera la boîte de dialogue suivante   *

![](images/FreeCAD-0.17-missing-Graphviz-error-dialogue.png )

### Windows

Téléchargez le programme d\'installation **graphviz-2.xx** depuis la page [page de téléchargement Graphviz](https   *//graphviz.org/download/#windows) puis lancez l\'installation. Certaines versions plus anciennes semblent avoir des problèmes pour afficher le graphique. Les versions 2.38 et plus récentes sont connues pour être fiables. Vous pouvez trouver toutes les versions de Graphviz sur [Gitlab](https   *//gitlab.com/graphviz/graphviz/-/releases).

### MacOSX

Vous pouvez installer graphviz à l\'aide du gestionnaire de paquets [Homebrew](https   *//brew.sh/index_fr.html). (Lors de l\'installation de Homebrew, ne soyez pas nerveux, si MacOS vous demande d\'installer des mises à jour, par exemple pour les outils de ligne de commande Xcode. Ces mises à jour sont effectuées plus tard par le processus d\'installation.)


{{Code|lang=text|code=
brew install graphviz
}}

Ceci installe les binaires de graphviz sous /usr/local/bin pour macOS sur Intel, et /opt/homebrew pour macOS sur Apple Silicon/ARM. FreeCAD va chercher là tout seul. Si le programme n\'y est pas trouvé, il vous est demandé d\'entrer le chemin. Malheureusement, nous ne pouvons pas y naviguer directement à partir de la boîte de dialogue de sélection de fichier qui s\'affiche à partir de **Outils → Graphique de dépendance...**. Lorsque vous avez la boîte de dialogue de sélection de fichier, vous avez deux possibilités    * Vous pouvez utiliser la combinaison de touches Cmd+Shift+. qui vous montrera tous les éléments cachés, ou vous utilisez les touches Cmd+Shift+G pour obtenir un champ de saisie pour le chemin. Validez


{{Code|lang=text|code=
/usr/local/bin
}}

ou


{{Code|lang=text|code=
/opt/homebrew/bin
}}

puis confirmez le champ de saisie et l\'invite de dialogue.

Au cas où les fichiers Graphviz seraient installés à un autre emplacement, tentez de trouver le programme avec la commande


{{Code|lang=text|code=
type dot
}}

Le résultat ressemblera à


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Et vous pouvez ensuite diriger FreeCAD vers ce répertoire.

### Linux

Dans la plupart des distributions Linux (Debian/Ubuntu, Fedora, OpenSUSE), il suffit d\'installer le paquet graphviz depuis les dépôts. Toutefois, similaire à Mac/OSX, dans certains cas les fichiers binaires de Graphviz sont installés dans un emplacement non-standard. Essayez de trouver le programme avec la commande   *


{{Code|lang=text|code=
type dot
}}

Le résultat pourrait être


{{Code|lang=text|code=
dot is /usr/local/bin/dot
}}

Et vous pouvez ensuite pointer FreeCAD vers ce répertoire.

## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_DependencyGraph.svg" width=16px> Graphique de dépendance...** dans le menu.
2.  Un nouvel onglet intitulé **Graphique de dépendance** s\'ouvre dans [Zone de vue principale](Main_view_area/fr.md).
3.  Utilisez la molette de défilement de la souris pour effectuer un zoom avant ou arrière.
4.  Utilisez les curseurs en bas et à droite de l\'écran pour effectuer un panoramique de la vue. Vous pouvez aussi ({{Version/fr|0.19}}) maintenir le bouton gauche de la souris enfoncé et déplacer la souris.

## Enregistrer

Vous pouvez enregistrer un graphique de dépendance    *

1.  Assurez-vous que l\'onglet Graphique des dépendances est au premier plan.
2.  Sélectionnez l\'option **Fichier → [Enregistrer](Std_Save/fr.md)** ou **Fichier → [Enregistrer sous](Std_SaveAs/fr.md)** dans le menu.
3.  Saisissez un nom de fichier et sélectionnez le type de fichier (\*.png, \*.bmp, \*.gif, \*.jpg, \*.svg ou \*.pdf).
4.  Appuyez sur le bouton **Enregistrer**.

## Principes généraux 

-   Le graphe affiche les objets en ordre chronologique inversé, de bas en haut.
-   La direction des flèches indiquant les dépendances doit toujours pointer vers le bas, de l\'objet enfant à l\'objet parent. Une flèche pointant vers le haut indique une dépendance cyclique, un problème qui doit être résolu.
-   Une esquisse contenant des liens vers des [géométries externes](Sketcher_External/fr.md) aura un numéro avec un suffixe \"x\" à côté de la flèche la reliant à son parent, indiquant le nombre de géométries externes liées dans l\'esquisse.
-   Les objets peuvent avoir des dépendances à plusieurs parents. Par exemple, pour un modèle construit dans [Atelier PartDesign](PartDesign_Workbench/fr.md), une cavité (Pocket) sera liée à son esquisse (Sketch) et à la fonctionnalité Protrusion (Pad) qui l'a précédée.
-   Les dépendances non autorisées (par exemple, entre une opération [Atelier Draft](Draft_Workbench/fr.md)/[Atelier Part](Part_Workbench/fr.md) et un élément à l\'intérieur d\'un [PartDesign Corps](PartDesign_Body/fr.md)) seront affichées avec une flèche rouge. Ce type de lien affiche généralement une erreur \'Links go out of allowed scope\' (Liens hors de portée autorisée) dans la [Vue rapport](Report_view/fr.md).
-   Le [Part conteneur ](Std_Part/fr.md) et le [PartDesign Corps](PartDesign_Body/fr.md) englobent leur contenu dans un encadré avec un arrière-plan de couleur aléatoire. Leur origine englobe également leur contenu (plans et axes standard) dans un encadré.
-   Le [Groupe](Std_Group/fr.md) est affiché comme un élément unique lié à son contenu.

## Limitations

-   Le graphique de dépendance ne peut pas détecter les problèmes causés par le [Problème de dénomination topologique](Topological_naming_problem/fr.md). Si une esquisse change de face après une modification, elle est toujours liée à la fonction. Même si certaines fonctions sont rompues, le graphique de dépendance restera inchangé.





{{Std Base navi

}} 

[Category   *3rd Party](Category_3rd_Party.md)



---
![](images/Right_arrow.png) [documentation index](../README.md) > [3rd Party](Category_3rd Party.md) > Std DependencyGraph/fr
