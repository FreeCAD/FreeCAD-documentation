---
- GuiCommand:/fr
   Name:Arch Schedule
   Name/fr:Arch Planificateur
   MenuLocation:Arch → Planification
   Workbenches:[Arch](Arch_Workbench/fr.md)
   SeeAlso:[Arch Équipement](Arch_Equipment/fr.md)
---

# Arch Schedule/fr

## Description

L\'outil Planificateur vous permet de créer et de remplir automatiquement une [feuille de calculs](Spreadsheet_Workbench/fr.md) avec les données du modèle.


**Remarque**

: Cet outil a été complètement réécrit dans la version 0.17 de FreeCAD et est différent des versions précédentes.

Pour une solution plus générale, consultez le [Reporting Workbench](https://github.com/furti/FreeCAD-Reporting/tree/master) dans la liste des [ateliers externes](External_workbenches/fr.md). Cet atelier utilise la syntaxe SQL pour extraire des informations du document.

## Utilisation

1.  Ouvrir ou créer un document FreeCAD qui contient plusieurs objets.
2.  Cliquer sur le bouton **<img src="images/Arch_Schedule.svg" width=16px> [Crée une planification](Arch_Schedule/fr.md)**.
3.  Ajuster les options désirées.
4.  Cliquer **OK**.

## Déroulement des tâches 

D\'abord, vous devez avoir un modèle. Par exemple, voici un document avec plusieurs objets. Ici ce sont des objets Arch, mais ça n\'est pas obligatoire, ça peut être n\'importe quel objet.

![](images/Arch_schedule_example01.jpg )

Vous appuyez sur le bouton **<img src="images/Arch_Schedule.svg" width=16px> [Arch Crée une planification](Arch_Schedule/fr.md)**. Vous obtenez un panneau de tâches comme celui-ci. Il est assez large, vous devrez donc élargir le panneau des tâches pour travailler confortablement.

![](images/Arch_schedule_example02.jpg )

Ensuite, vous pouvez remplir le classeur ligne par ligne. Chaque ligne est une \"requête\" et affichera une ligne dans la feuille de calcul. Appuyez sur le bouton **Ajouter** pour ajouter une nouvelle ligne et double-cliquez sur chaque cellule de cette ligne pour remplir les valeurs. Le bouton **Suppr** supprimera la ligne qui contient une cellule sélectionnée, et **Effacer** supprimera toutes les lignes. Les valeurs possibles à mettre dans les colonnes sont:

-   **Description**: Une description pour la requête. La colonne Description sera la première colonne de la feuille de calcul résultante. Une description est obligatoire pour qu\'une requête soit effectuée. Si vous laissez la cellule de description vide, toute la ligne sera ignorée et laissée vide dans la feuille de calcul. Cela vous permet d\'ajouter des lignes \"séparateur\".
-   **Value**: Il s\'agit de la requête réelle que vous souhaitez effectuer sur tous les objets sélectionnés par la requête. Il peut s\'agir de deux choses: soit le mot `count`, soit une propriété d\'objet:
    -   Si vous entrez `count` (ou `Count` ou `COUNT`, il est insensible à la casse), les objets sélectionnés seront simplement comptés.
    -   Si vous entrez une propriété d\'objet, la valeur de cette propriété pour chacun des objets sélectionnés sera extraite et résumée. Les objets qui ne possèdent pas la propriété seront ignorés. Utilisez la notation par points pour récupérer les propriétés des propriétés: `PropertyOfObject.PropertyOfProperty1.PropertyOfProperty2`. Si la propriété avant le premier point commence par une lettre minuscule, elle sera considérée comme une référence à l\'objet lui-même et sera ignorée. Saisir par exemple `object.Shape.Volume` équivaut à saisir `Shape.Volume`.
-   **Unit**: Une unité optionnelle pour exprimer les résultats. C\'est à vous de donner une unité qui correspond à la requête que vous faites, par exemple, si vous récupérez des volumes, vous devez utiliser une unité de volume, telle que `m^3`. Si vous utilisez une mauvaise unité, par ex.cm, vous obtiendrez de mauvais résultats.
-   **Objects**: Vous pouvez laisser ce champs vide, alors tous les objets du document seront considérés par cette requête, ou donner une liste séparée par des points-virgules (;) des noms d\'objets (pas d\'étiquettes). Si l\'un des objets de cette liste est un groupe, ses enfants seront également sélectionnés. La manière la plus simple d\'utiliser cette fonctionnalité est donc de regrouper vos objets de manière significative dans le document, et de donner ici simplement un nom de groupe. Vous pouvez également utiliser le bouton **Selection** pour ajouter des objets actuellement sélectionnés dans le document.
-   **Filter**: Ici vous pouvez ajouter un point-virgule `;` - liste de filtres séparés. Chaque filtre est écrit sous la forme: `property:value`. Vous ne pouvez utiliser que des propriétés contenant une valeur de chaîne. La propriété et la valeur ne sont pas sensibles à la casse. `value` peut être omis mais pas `:`. Pour gérer correctement les planifications créées avec les versions précédentes d\'Arch Schedule, la propriété `type` sera traduite en propriété `ifctype`. Il est conseillé de ne pas utiliser `type` dans les nouveaux horaires.

:   Par exemple:

    :   
        `label:floor1;ifctype:window`
        
        ne conservera que les objets qui ont \"floor1\" dans leur {{PropertyData/fr|Label}} et \"window\" dans leur {{PropertyData/fr|IFC Type}}. Une fenêtre avec {{PropertyData/fr|Label}} \"Floor1-AA\" et **IFC Type** \"Window Standard Case\" sera inclus.

    :   
        `label:door`
        
        Ne conservera que les objets qui ont \"door\" dans leur {{PropertyData/fr|Label}}.

    :   
        `!label:door`
        
        Ne conservera que les objets qui n\'ont pas de \"door\" dans leur {{PropertyData/fr|Label}}.

    :   
        `ifctype:structural`
        
        Ne conservera que les objets qui ont \"structural\" dans leur {{PropertyData/fr|IFC Type}}.

    :   
        `!ifctype:something`
        
        Ne conservera que les objets qui n\'ont pas de \"structural\" dans leur {{PropertyData/fr|IFC Type}} ou qui n\'ont pas la propriété {{PropertyData/fr|IFC Type}}.

    :   
        `!ifctype:`
        
        Ne conservera que les objets qui n\'ont pas la propriété {{PropertyData/fr|IFC Type}}.

Le bouton **Import** vous permet de construire cette liste dans une autre application avec tableur, et de l\'importer ici en tant que fichier csv.

Nous pouvons donc construire une liste de requêtes comme celle-ci:

![](images/Arch_schedule_example03.jpg )

Après cela, appuyez sur le bouton **OK** et un nouvel objet Classeur est ajouté au document, qui contient une feuille de calcul de résultats:

![](images/Arch_schedule_example04.jpg )

En double-cliquant sur l\'objet Classeur, vous revenez au panneau des tâches et modifiez les valeurs. En double-cliquant sur la feuille de calcul elle-même, vous obtenez les résultats dans 3 colonnes: description, valeur, unité (le cas échéant):

![](images/Arch_schedule_example05.jpg )

A partir du plan de travail Spreadsheet, la feuille de calcul peut ensuite être exportée normalement vers un fichier csv.

## Propriétés dynamiques 

Il est possible d\'ajouter vos propres propriétés aux objets. Celles-ci sont appelées [propriétés dynamiques](Property_editor/fr#Actions.md). Si elles ont été ajoutées avec l\'option **Prefix group name** sélectionnée, leurs noms commenceront effectivement par le nom du groupe, mais ce préfixe ne sera pas affiché dans l\'[Éditeur de propriétés](Property_editor/fr.md). Leurs noms ont la forme suivante: `NameOfGroup_NameOfProperty`. Pour les référencer dans un calendrier, ce nom complet doit être utilisé.



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Schedule/fr
