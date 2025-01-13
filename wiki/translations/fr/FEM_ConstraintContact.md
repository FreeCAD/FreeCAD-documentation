---
 GuiCommand:Container
|
{{GuiCommand/fr
   Name: FEM ConstraintContact
   Name/fr: FEM Contrainte de contact
   MenuLocation: Modèle , Conditions limites et charges mécaniques , Contrainte de contact
   Workbenches: FEM_Workbench/fr
   SeeAlso: FEM_ConstraintFixed/fr
}}
{{GuiCommandFemInfo/fr
   Solvers: CalculiX
}}
---

# FEM ConstraintContact/fr

## Description

Crée une contrainte de contact entre deux surfaces. Contrairement au cas de la [contrainte de liaison](FEM_ConstraintTie/fr.md), les surfaces peuvent se séparer et glisser l\'une sur l\'autre (avec ou sans frottement) au cours de l\'analyse.



## Utilisation

1.  Il y a plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/FEM_ConstraintContact.svg" width=16px> [Contrainte de contact](FEM_ConstraintContact/fr.md)**.
    -   Sélectionnez l\'option **Modèle → Conditions limites et charges mécaniques → <img src="images/FEM_ConstraintContact.svg" width=16px> Contrainte de contact** du menu.

2.  Sélectionnez la face principale. Cliquez sur le premier bouton **Ajouter**. Pour supprimer une face de la sélection, cliquez dessus et appuyez sur le premier bouton **Supprimer**.

3.  Sélectionnez le face esclave. Appuyez sur le deuxième bouton **Ajouter**. Pour supprimer une face de la sélection, cliquez dessus et appuyez sur le deuxième bouton **Supprimer**.

4.  Vous pouvez saisir une rigidité de contact.

5.  
    {{Version/fr|1.0}}: vous pouvez saisir un ajustement du jeu. Tous les nœuds de la face esclave dont la distance par rapport à la face maître est inférieure ou égale à ce nombre seront déplacés pour se trouver sur la face maître au début de l\'analyse. Cet ajustement ne provoque aucune contrainte.

6.  
    {{Version/fr|1.0}}: vous pouvez cocher la case *Activer la friction* pour spécifier le coefficient de friction et la valeur de la pente de contact.

7.  Entrer optionnellement un coefficient de friction. La valeur par défaut de 0 signifie un contact sans frottement.

8.  
    {{Version/fr|1.0}}: vous pouvez saisir une valeur de la *pente de la courbe de collage*. Il s\'agit d\'un équivalent de la rigidité de contact pour le comportement de frottements. Elle définit la pente de la relation linéaire entre la contrainte de cisaillement et le déplacement tangentiel relatif dans la plage de contact (avant que le glissement ne se produise).

## Limitations

-   La contrainte de contact ne peut être appliquée qu\'à deux faces.
-   Développement pour un contact multiple à la fois : <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=130#p303275>
-   Parce que les maillages multiples ne sont actuellement pas pris en charge, le contact doit être appliqué à des faces qui sont séparées par (au moins) une petite distance. Si les faces se touchaient (sans espace entre elles), le résultat d\'une opération d\'union booléenne ou de fragmentation booléenne (nécessaire pour éviter d\'avoir des maillages multiples, ce qui n\'est pas autorisé pour le moment) serait un maillage continu et donc plus besoin d\'utiliser le contact. Voir [Discussion sur le forum](https://forum.freecadweb.org/viewtopic.php?f=18&t=62307).



## Remarques



### Astuces pour modéliser 

-   À partir de <https://forum.freecadweb.org/viewtopic.php?f=18&p=340874#p340494>
-   L\'utilisation d\'éléments linéaires est recommandée. Dans le cas contraire, les calculs peuvent prendre beaucoup de temps.
-   Affectation maître/esclave :
    -   La plus grande des deux surfaces doit être la surface maîtresse.
    -   Si les surfaces sont de taille comparable, la surface du corps le plus rigide doit être la surface maîtresse.
    -   Si les surfaces sont de taille et de rigidité comparables, la surface dont le maillage est le plus grossier doit être considérée comme la surface maîtresse.

### CalculiX

-   La rigidité de contact peut être estimée de 5 à 50 fois le module de Young du matériau. Plus la valeur de la rigidité de contact est élevée, plus le contact entre les surfaces est dur.
-   La face esclave est la face qui pénètre dans la face maîtresse et subit donc une plus grande déformation.
-   Le jeu de paramètres \*CONTACT PAIR est utilisée pour modéliser le contact dans CalculiX. La contrainte utilise le contact de pénalité Face-à-Face et la formulation du contact est expliquée en détail sur <http://web.mit.edu/calculix_v2.7/CalculiX/ccx_2.7/doc/ccx/node112.html>.
-   Vue d\'ensemble des différents types de contact : <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699&start=90#p188736>
-   Autres informations intéressantes :
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=23102#p180709> et les posts suivants !!!
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=20276>
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=21331>
    -   <https://forum.freecadweb.org/viewtopic.php?f=18&t=15699> (sujet du contact initial)

-   Un exemple de contact très détaillé avec CalculiX. ([lien](http://dip28p.web.fc2.com/calculix/netgen2calculix/index.html))

-   Un exemple intéressant dans le sous forum allemand. ([Lien](https://forum.freecadweb.org/viewtopic.php?f=13&t=39663&start=10#p337254))





{{FEM Tools navi

}}



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM ConstraintContact/fr
