---
- GuiCommand:/fr
   Name:PartDesign_Pocket
   Name/fr:PartDesign Cavité
   MenuLocation:Conception de pièces → Créer une fonction soustractive → Cavité
   Workbenches:[PartDesign](PartDesign_Workbench/fr.md)
   SeeAlso:[PartDesign Protrusion](PartDesign_Pad/fr.md)
---

## Description

L\'outil **Cavité** découpe un solide en extrudant une esquisse (ou une face du solide) selon un tracé rectiligne et en le soustrayant du solide.

![](images/PartDesign_Pocket_example.svg ) *Le profil d\'esquisse (A) a été appliqué sur la face de dessus du solide (B) ; le résultat après l\'opération de cavité est montré à droite.*

## Utilisation

1.  Sélectionner une esquisse.

    :   Celle-ci doit être appliquée sur la face planaire d\'un solide ou d\'une fonction PartDesign existant, sinon un message d\'erreur apparaîtra. {{VersionMinus/fr|0.16}}
2.  Cliquer sur le bouton **<img src="images/PartDesign_Pocket.svg" width=16px> '''Créer une cavité...'''**.
3.  Définir les paramètres de cavité (voir section suivante).
4.  Cliquer sur OK.

## Options

![](images/Pocket_options_fr.png )

À la création d\'une cavité, le dialogue **Paramètres de cavité** offre cinq façons différentes de définir la longueur (profondeur) à laquelle la cavité sera extrudée :

### Dimension

Permet de saisir une valeur numérique pour la profondeur de la cavité. La direction par défaut de la cavité est vers le haut du plan d\'esquisse. L\'extrusion s\'effectue [normale](http://fr.wikipedia.org/wiki/Normale_%C3%A0_une_surface) au plan de l\'esquisse. Les valeurs numériques négatives ne sont pas allouées.

### Au premier {#au_premier}

La cavité sera prolongée jusqu\'à la première face rencontrée dans la direction d\'extrusion. Autrement dit, elle coupera à travers le solide jusqu\'à ce qu\'elle atteigne un espace vide.

### À travers tout {#à_travers_tout}

La cavité coupera à travers tout le solide dans la direction d\'extrusion. Avec l\'option **Symétrique au plan**, la cavité coupera à travers tout dans les deux directions.**Remarque :** Pour des raisons techniques, *À travers tout* est en fait une cavité de 10 mètres de profondeur. Si vous avez besoin de cavités plus profondes, utilisez *Dimension*.

### Jusqu\'à la face {#jusquà_la_face}

La cavité sera extrudée jusqu\'à une face dans le support qui peut être choisie en cliquant dessus.

### Deux dimensions {#deux_dimensions}

Permet de saisir une seconde valeur de longueur pour prolonger la poche dans la direction opposée (dans le support). La direction peut également être changée avec l\'option **Inversé**. {{VersionPlus/fr|0.17}}

## Limitations

-   Utilisez le type **Dimension** ou **À travers tout** dans la mesure du possible, car les autres types peuvent parfois causer problème quand la cavité est utilisée pour une répétition linéaire ou circulaire.
-   Autrement, la fonction cavité partage les mêmes [limitations](PartDesign_Pad/fr#Limitations.md) que la fonction protrusion.

## Liens utiles {#liens_utiles}

Un [exemple pratique](http://forum.freecadweb.org/viewtopic.php?f=3&t=3733&start=10) sur le forum (en anglais).





{{PartDesign Tools navi

}} 
