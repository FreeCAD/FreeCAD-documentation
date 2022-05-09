---
- GuiCommand   */fr
   Name   *FEM ConstraintContact
   Name/fr   *FEM Contrainte de contact
   MenuLocation   *Modèle → Contraintes mécaniques → Contrainte de contact
   Workbenches   *[Atelier FEM](FEM_Workbench/fr.md)
   SeeAlso   *[FEM Contrainte fixe](FEM_ConstraintFixed/fr.md)
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
-   Développement pour un contact multiple en même temps    * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=130#p303275>
-   Parce que les maillages multiples ne sont actuellement pas supportés, le contact doit être appliqué à des faces séparées par (au moins) une petite distance. Si les faces se touchaient (sans espace entre elles), le résultat d\'une opération d\'union booléenne ou de fragmentation booléenne (nécessaire pour éviter d\'avoir des maillages multiples, ce qui n\'est pas autorisé pour le moment) serait un maillage continu et donc plus besoin d\'utiliser le contact. Voir [Discussion sur le forum](https   *//forum.freecadweb.org/viewtopic.php?f=18&t=62307).

## Remarques

### Astuces pour modéliser 

-   à partir de <https   *//forum.freecadweb.org/viewtopic.php?f=18&p=340874#p340494>
-   mieux utiliser les éléments linéaires, sinon les calculs prennent beaucoup de temps
-   attribution maître/esclave    *
    -   la plus grande des deux surfaces doit servir de surface maître.
    -   si les surfaces sont de taille comparable, la surface du corps le plus rigide devrait faire office de surface principale.
    -   si les surfaces sont de taille et de rigidité comparables, la surface avec le maillage plus grossier devrait servir de surface maîtresse.

### CalculiX

1.  La rigidité du contact doit être 10 fois plus tendre (young\'s modulus) que le modulus pour avoir un contact dur. Plus la valeur de la rigidité du contact est élevée, plus le contact entre les surfaces est difficile.
2.  La face esclave est la face qui pénètre dans la face maître, et présente donc plus de déformation.
3.  La carte \*CONTACT PAIR est utilisée pour modéliser le contact dans CalculiX. La contrainte utilise le contact de pénalité face à face et la formule du contact est expliquée en détail ici <http   *//web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>

-   Vue d\'ensemble pour différents types de contact   * <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>
-   Autres informations intéressantes   *
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> et messages suivants!!!
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=20276>
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=21331>
    -   <https   *//forum.freecadweb.org/viewtopic.php?f=18&t=15699> (sujet de contact initial)

-   Un exemple de contact très détaillé avec CalculiX. ([lien](http   *//dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   Un exemple très cool aussi dans le sous forum allemand. ([Lien](https   *//forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintContact/fr
