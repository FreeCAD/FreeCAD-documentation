---
- GuiCommand:
   Name: Arch Schedule
   Name/fr: Arch Nomenclature
   MenuLocation: Arch - Nomenclature
   Workbenches: [Arch](Arch_Workbench/fr.md)
   SeeAlso: [Arch Équipement](Arch_Equipment/fr.md)
---

# Arch Schedule/fr

## Description

L\'outil Nomenclature vous permet de créer et d\'alimenter automatiquement une [feuille de calculs](Spreadsheet_Workbench/fr.md) avec les contenus recueillis dans le modèle.


**Remarque**

: cet outil a été complètement réécrit dans la version 0.17 de FreeCAD et est différent des versions précédentes.

Pour une solution plus générale, consultez l\'[atelier Reporting](https://github.com/furti/FreeCAD-Reporting/tree/master) dans la liste des [ateliers externes](External_workbenches/fr.md). Cet atelier utilise la syntaxe SQL pour extraire des informations du document.



## Utilisation

1.  Ouvrer ou créer un document FreeCAD qui contient plusieurs objets.
2.  Cliquer sur le bouton **<img src="images/Arch_Schedule.svg" width=16px> [Nomenclature](Arch_Schedule/fr.md)**.
3.  Ajuster les options désirées.
4.  Cliquer **OK**.



## Déroulement des tâches 

Tout d\'abord, vous devez disposer d\'un modèle. Par exemple, voici un document avec quelques objets. Ici ce sont des objets Arch, mais d\'autres objets sont également pris en charge.

![](images/Arch_schedule_example01.jpg )

Vous appuyez sur le bouton **<img src="images/Arch_Schedule.svg" width=16px> [Nomenclature](Arch_Schedule/fr.md)**. Vous obtenez un panneau de tâches comme celui-ci. Il est assez large, vous devrez donc élargir le panneau des tâches pour travailler confortablement.

![](images/Arch_schedule_example02.jpg )

Ensuite, vous pouvez remplir le classeur ligne par ligne. Chaque ligne est une \"requête\" et affichera une ligne dans la feuille de calcul. Appuyez sur le bouton **Ajouter** pour ajouter une nouvelle ligne et double-cliquez sur chaque cellule de cette ligne pour remplir les valeurs. Le bouton **Supprimer** supprimera la ligne qui contient une cellule sélectionnée, et **Effacer** supprimera toutes les lignes. Les valeurs possibles à mettre dans les colonnes sont :

-   **Description** : description pour cette requête. La colonne Description sera la première colonne de la feuille de calcul résultante. Une description est obligatoire pour qu\'une requête soit effectuée. Si vous laissez la cellule de description vide, toute la ligne sera ignorée et laissée vide dans la feuille de calcul. Cela vous permet d\'ajouter des lignes \"séparateur\".
-   **Value** : il s\'agit de la requête réelle que vous souhaitez effectuer sur tous les objets sélectionnés par la requête. Il peut s\'agir de deux choses: soit le mot `count`, soit une propriété d\'objet:
    -   Si vous entrez `count` (ou `Count` ou `COUNT`, insensible à la casse), les objets sélectionnés seront simplement comptés.
    -   Si vous entrez une propriété d\'objet, la valeur de cette propriété pour chacun des objets sélectionnés sera extraite et résumée. Les objets qui ne possèdent pas la propriété seront ignorés. Utilisez la notation par points pour récupérer les propriétés des propriétés: `PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. Si la propriété avant le premier point commence par une lettre minuscule, elle sera considérée comme une référence à l\'objet lui-même et sera ignorée. Saisir par exemple `object.Shape.Volume` équivaut à saisir `Shape.Volume`.
-   **Unité** : unité optionnelle pour exprimer les résultats. C\'est à vous de donner une unité qui correspond à la requête que vous faites, par exemple, si vous récupérez des volumes, vous devez utiliser une unité de volume, telle que `m^3`. Si vous utilisez une mauvaise unité, par ex.cm, vous obtiendrez de mauvais résultats.
-   **Objets** : vous pouvez laisser ce champs vide, alors tous les objets du document seront considérés par cette requête, ou donner une liste séparée par des points-virgules (;) des noms d\'objets (pas d\'étiquettes). Si l\'un des objets de cette liste est un groupe, ses enfants seront également sélectionnés. La manière la plus simple d\'utiliser cette fonctionnalité est donc de regrouper vos objets de manière significative dans le document, et de donner ici simplement un nom de groupe. Vous pouvez également utiliser le bouton **Selection** pour ajouter des objets actuellement sélectionnés dans le document.
-   **Filtre** : ici vous pouvez ajouter un point-virgule `;` - liste de filtres séparés. Chaque filtre est écrit sous la forme: `property:value`. Vous ne pouvez utiliser que des propriétés contenant une valeur de chaîne. La propriété et la valeur ne sont pas sensibles à la casse. `value` peut être omis mais pas `:`. Pour gérer correctement les nomenclatures créées avec les versions précédentes d\'Arch Nomenclature, la propriété `type` sera traduite en propriété `ifctype`. Il est conseillé de ne pas utiliser `type` dans les nouveaux horaires.

:   Par exemple :

    :   
        `label:floor1;ifctype:window`
        
        ne conservera que les objets qui ont \"floor1\" dans leur **Label** et \"window\" dans leur **IFC Type**. Une fenêtre avec **Label** \"Floor1-AA\" et **IFC Type** \"Window Standard Case\" sera inclus.

    :   
        `label:door`
        
        ne conservera que les objets qui ont \"door\" dans leur **Label**.

    :   
        `!label:door`
        
        ne conservera que les objets qui n\'ont pas de \"door\" dans leur **Label**.

    :   
        `ifctype:structural`
        
        ne conservera que les objets qui ont \"structural\" dans leur **IFC Type**.

    :   
        `!ifctype:something`
        
        ne conservera que les objets qui n\'ont pas de \"structural\" dans leur **IFC Type** ou qui n\'ont pas la propriété **IFC Type**.

    :   
        `!ifctype:`
        
        ne conservera que les objets qui n\'ont pas la propriété **IFC Type**.

Le bouton **Import** vous permet de construire cette liste dans une autre application avec tableur, et de l\'importer ici en tant que fichier CSV.

Nous pouvons donc construire une liste de requêtes comme celle-ci :

![](images/Arch_schedule_example03.jpg )

Après cela, appuyez sur le bouton **OK** et un nouvel objet Nomenclature est ajouté au document, qui contient une feuille de calcul de résultats :

![](images/Arch_schedule_example04.jpg )

En double-cliquant sur l\'objet Nomenclature, vous revenez au panneau des tâches et modifiez les valeurs. En double-cliquant sur la feuille de calcul elle-même, vous obtenez les résultats dans 3 colonnes: description, valeur, unité (le cas échéant) :

![](images/Arch_schedule_example05.jpg )

La feuille de calcul peut ensuite être exportée au format CSV normalement, à partir de l\'atelier Spreadsheet.



## Propriétés dynamiques 

Il est possible d\'ajouter vos propres propriétés aux objets. Celles-ci sont appelées [propriétés dynamiques](Property_editor/fr#Actions.md). Si elles ont été ajoutées avec l\'option **Prefix group name** sélectionnée, leurs noms commenceront effectivement par le nom du groupe, mais ce préfixe ne sera pas affiché dans l\'[Éditeur de propriétés](Property_editor/fr.md). Leurs noms ont la forme suivante : `NameOfGroup_NameOfProperty`. Pour les référencer dans une nomenclature, ce nom complet doit être utilisé.



---
⏵ [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Schedule/fr
