---
- GuiCommand   */fr
   Name   *FEM ConstraintContact
   Name/fr   *FEM Contrainte de contact
   MenuLocation   *Modèle → Contraintes mécaniques → Contrainte de contact
   Workbenches   *[Atelier FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Contrainte d'immobilisation](FEM_ConstraintFixed/fr.md)
---

# FEM ConstraintContact/fr

## Description

Crée une contrainte FEM de contact entre deux surfaces.

## Utilisation

1.  Il existe plusieurs façons d\'appeler la commande   *
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintContact.svg" width=16px> [Contrainte de contact](FEM_ConstraintContact/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Contraintes mécaniques → <img src="images/FEM_ConstraintContact.svg" width=16px> Contrainte de contact** dans le menu.
2.  Sélectionnez la face principale.
3.  Sélectionnez la face esclave.
4.  Entrez une raideur de contact.
5.  Entrez un coefficient de frottement.

## Limitations

-   La contrainte de contact ne peut être appliquée qu\'à deux faces.
-   Développement pour un contact multiple à la fois    * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=130#p303275>
-   Parce que les maillages multiples ne sont actuellement pas pris en charge, le contact doit être appliqué à des faces qui sont séparées par (au moins) une petite distance. Si les faces se touchaient (sans espace entre elles), le résultat d\'une opération d\'union booléenne ou de fragmentation booléenne (nécessaire pour éviter d\'avoir des maillages multiples, ce qui n\'est pas autorisé pour le moment) serait un maillage continu et donc plus besoin d\'utiliser le contact. Voir [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=62307).

## Remarques

### Astuces pour modéliser 

-   A partir de <https   *//forum.freecadweb.org/viewtopic.php?f=18&p=340874#p340494>
-   Il vaut mieux utiliser des éléments linéaires, sinon les calculs prennent beaucoup de temps.
-   Affectation maître/esclave    *
    -   La plus grande des deux surfaces doit être la surface maîtresse.
    -   Si les surfaces sont de taille comparable, la surface du corps le plus rigide doit être la surface maîtresse.
    -   Si les surfaces sont de taille et de rigidité comparables, la surface dont le maillage est le plus grossier doit être considérée comme la surface maîtresse.

### CalculiX

-   La rigidité de contact doit être 10 fois supérieure au module de Young du matériau pour un contact dur. Plus la valeur de la rigidité de contact est élevée, plus le contact entre les surfaces est dur.
-   La face esclave est la face qui pénètre dans la face maître, et subit donc plus de déformation.
-   La carte \*CONTACT PAIR est utilisée pour modéliser le contact dans CalculiX. La contrainte utilise le contact de pénalité Face-à-Face et la formulation du contact est expliquée en détail sur <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>.
-   Vue d\'ensemble des différents types de contact    * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>
-   Autres informations intéressantes    *
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> et les posts suivants !!!
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=20276>
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=21331>
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=15699> (sujet du contact initial)

-   Un exemple de contact très détaillé avec CalculiX. ([lien](http   *//dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   Un très bon exemple aussi dans le sous forum allemand. ([Lien](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintContact/fr
