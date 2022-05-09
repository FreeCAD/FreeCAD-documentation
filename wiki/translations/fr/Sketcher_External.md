---
- GuiCommand   */fr
   Name   *Sketcher External
   Name/fr   *Sketcher Géométrie externe
   MenuLocation   *Esquisse → Géométries d'esquisse → Géométrie externe
   Workbenches   *[Sketcher](Sketcher_Workbench/fr.md)
   Shortcut   ***G** **X**
   SeeAlso   *[Sketcher Basculer en géométrie de construction](Sketcher_ToggleConstruction/fr.md)
---

# Sketcher External/fr

## Description

L\'outil **<img src="images/Sketcher_External.svg" width=16px> [Géométrie externe](Sketcher_External/fr.md)** est utile lorsque vous avez besoin de créer une contrainte entre un élément de l\'esquisse et un élément hors de l\'esquisse. Il fonctionne en insérant une géométrie de construction liée dans l\'esquisse. La couleur par défaut des arêtes externes liés est magenta. Comme pour les géométries de construction non liée (bleu), la géométrie externe liée est visible uniquement lorsque l\'esquisse est en mode d\'édition, et n\'est pas utilisée directement dans le résultat subséquent. Les deux types de géométrie de construction sont utilisés en tant que référence pour les contraintes dans l\'esquisse.

Attention, l\'utilisation de cet outil pour créer un lien vers une géométrie (solide) créée peut conduire à des résultats inattendus en raison du [Problème de dénomination topologique](Topological_naming_problem/fr.md). Voir également [Conseils pour des modèles stables](Feature_editing/fr#Conseils_pour_la_cr.C3.A9ation_de_mod.C3.A8les_robustes.md).

<FILE   *Sketcher_ExternalEsempio1.png>

## Utilisation

-   Créer une nouvelle esquisse, ou ouvrir une esquisse existante.
-   Cliquer sur le bouton **[<img src=images/Sketcher_External.svg style="width   *16px"> [Géométrie externe](Sketcher_External/fr.md)**.
-   Sélectionner une arête ou un sommet que vous voulez lier dans l\'esquisse.
-   Appuyer sur **Echap** ou sélectionner un autre outil pour quitter l\'outil.

### Règles de sélection 

-   Seuls les arêtes et les sommets des objets du même système de coordonnées sont autorisés.

Autrement dit, l\'esquisse et l\'objet doivent être dans le même Corps (lorsqu\'ils se trouvent dans l\'atelier Part Design), ou dans la même Part (lorsqu\'ils sont dans l\'atelier Part), ou les deux en dehors des Parts et Corps.

Par exemple, si l\'esquisse ouverte est dans Body, vous pouvez utiliser une autre esquisse de Body comme géométrie externe, mais vous ne pouvez pas utiliser une esquisse de Body001 ou une arête d\'un cube Part dans la racine du projet. Utilisez la fonction forme liée (Shapebinder) pour importer une copie de l\'objet dans le système de coordonnées de l\'esquisse ouverte. Ensuite, vous pourrez utiliser les arêtes / sommets de l\'objet Shapebinder.

-   Aucune dépendance circulaire n\'est autorisée.

Cela signifie que vous ne pouvez pas créer de lien vers Pocket avec cette esquisse. Vous ne pouvez pas créer de lien vers un objet qui dépend de l\'esquisse.

CIl n\'est pas nécessaire que l\'esquisse soit sur une face pour utiliser cet outil. Les liens directs entre les esquisses sont possibles et encouragés car ils sont plus fiables.

### Comment savoir si tout a fonctionné 

Une ligne de couleur (magenta par défaut) sera surimposée sur une arête si celle-ci est liée avec succès (les sommets seront rouges), et sera visible dans l\'esquisse seulement dans le mode d\'édition d\'esquisse.

### Similarité des lignes de construction 

Les lignes de géométrie externe magenta sont semblables aux [lignes de construction](Sketcher_ToggleConstruction/fr.md) bleues sauf que les premières sont liées de façon paramétrique à un élément solide à laquelle l\'esquisse est attachée. Les lignes de construction sont des lignes de travail internes à l\'esquisse et seront uniquement utilisées pour la construction de la géométrie, et non pour les opérations sur le solide, comme les protrusions et les cavités.

### Utilisation de géométrie externe dans l\'atelier PartDesign 

Pendant le travail dans PartDesign, l\'outil de géométrie externe est utilisé pour faciliter la mise en place d\'un élément solide de votre construction, par rapport à la construction de l\'étape précédente. L\'atelier PartDesign est destiné à la production d\'un seul solide, par conséquent, les esquisses créées avec la géométrie externe sont utilisés pour créer une nouvelle entité pour ce solide.

L\'outil de géométrie externe peut, par exemple, être utilisé comme référence pour une contrainte utilisée pour positionner un trou dans un objet, à un emplacement spécifique relatif à une arête ou un sommet.

### Utilisation de géométrie externe dans l\'atelier Part 

Vous pouvez utiliser n\'importe quelle géométrie Part située dans le système de coordonnées de l\'esquisse. Il est conseillé de lier à la première fonction possible, car cela forme un lien plus stable.

## Exemple

Ci-dessous, une esquisse appliquée sur la face supérieure d\'un solide créé à partir d\'une protrusion d\'une esquisse précédemment construite. Les lignes magenta sont des lignes de géométrie externe liées aux deux arêtes de cette protrusion pré-existante.

Dans ce cas, elles sont utilisées comme référence pour les contraintes de tangence avec la circonférence d\'un cercle. Elles sont également utilisés comme référence pour des contraintes horizontale et verticale pour localiser le centre du deuxième cercle par rapport au bout et le haut de l\'objet.

<FILE   *Sketcher_ExternalEsempio2.png>

Voici la même esquisse en mode d\'édition, avec la protrusion sur laquelle elle est appliquée masquée.

<FILE   *Sketcher_ExternalEsempio4.png>

Lorsque l\'esquisse est fermée, les lignes de géométrie externe ne sont pas visibles.

<FILE   *Sketcher_ExternalEsempio3.png>





{{Sketcher_Tools_navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Sketcher](Sketcher_Workbench.md) > Sketcher External/fr
