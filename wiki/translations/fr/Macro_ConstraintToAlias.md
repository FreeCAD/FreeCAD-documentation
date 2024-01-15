# Macro ConstraintToAlias/fr
{{Macro/fr
|Name=Macro ConstraintToAlias
|Name/fr=Macro ConstraintToAlias
|Icon=ConstraintToAlias.svg
|Description=Créer un alias depuis l'éditeur de Sketcher à partir d'une contrainte nommée sélectionnée.
|Author=TheMarkster
|Version=0.2023.12.10
|Date=2023-12.10
|FCVersion=0.21
|Download=[https://wiki.freecad.org/images/3/31/ConstraintToAlias.svg Icône de la barre d'outils]
}}

## Description

Souvent, lors de l\'édition d\'une esquisse, nous avons besoin d\'un alias de feuille de calcul et d\'une valeur pour lier une contrainte, mais nous n\'avons pas encore créé cet alias. Dans ce cas, nous devons fermer l\'esquisse, passer à la vue du tableur, créer l\'alias, revenir à l\'éditeur d\'esquisse et lier la contrainte à l\'alias.

Avec cette macro, il suffit de créer la contrainte, de lui donner un nom et une valeur, puis d\'exécuter la macro. Elle affiche une boîte de dialogue dans laquelle vous pouvez modifier l\'étiquette de la colonne A, la valeur et l\'alias de la colonne B, et cliquer sur OK pour que l\'alias soit créé pour vous et que la contrainte y soit liée par des expressions.

<img alt="" src=images/ConstraintToAlias_scr1.png  style="width:400px;">



## Utilisation

Créez une contrainte en lui donnant un nom, puis sélectionnez cette contrainte et exécutez la macro. Le nom de la contrainte sera le nom par défaut de l\'alias à créer dans la feuille de calcul et de l\'étiquette de la colonne A. La boîte de dialogue donne un aperçu de ce à quoi ressemblera la feuille de calcul une fois l\'alias créé.

La macro n\'utilise que les colonnes A et B pour les alias qu\'elle génère, en commençant par la ligne 2 et en cherchant jusqu\'à ce qu\'elle trouve deux cellules vides dans ces colonnes. Il n\'est pas possible de sélectionner une autre ligne de feuille de calcul à utiliser dans la boîte de dialogue, mais vous pouvez modifier les champs étiquette, alias et valeur avant de cliquer sur OK pour créer l\'alias. Si aucune contrainte n\'est sélectionnée, la boîte de dialogue présente des valeurs par défaut pour l\'étiquette, l\'alias et la valeur. Cette fonctionnalité a été ajoutée dans la version 0.2023.11.07 pour les cas où, en dehors de l\'esquisse, il peut être utile d\'utiliser la macro pour ajouter un nouvel alias à la feuille de calcul, par exemple lors de la saisie de la longueur d\'une protrusion.

S\'il n\'y a pas encore de feuille de calcul dans le document actif, la macro en créera une nommée \"ss\". S\'il n\'y a qu\'une seule feuille de calcul, c\'est elle qui sera utilisée. S\'il y a plusieurs feuilles de calcul, elles seront ajoutées à la liste déroulante des feuilles de calcul en haut de la boîte de dialogue. Sélectionnez dans cette liste déroulante la feuille de calcul à laquelle vous souhaitez ajouter l\'alias.

Dans la boîte de dialogue, les alias de la cellule de la colonne B sont indiqués entre accolades, par exemple {{Value|{alias_for_this_cell} 32}}. Lorsque l\'alias est créé, vous ne verrez pas ce texte dans la feuille de calcul, mais seulement {{Value|32}}, tandis que l\'alias pour cette cellule sera {{Value|alias_for_this_cell}}.

Dans la capture d\'écran ci-dessus, vous remarquerez que le champ Alias est en rouge. Cela indique que cet alias existe déjà dans la feuille de calcul et que vous devez donc lui donner un autre nom ou l\'annuler si vous n\'avez pas réalisé qu\'il existait déjà. Notez également que certains caractères, comme les espaces, ne sont pas autorisés pour les noms d\'alias. Les espaces sont automatiquement convertis en caractères de soulignement. Les autres caractères spéciaux sont également traités de cette manière. Vous verrez le nom de l\'alias dans sa forme finale dans l\'aperçu de la feuille de calcul.

App::Links est pris en charge, y compris les liens vers des feuilles de calcul dans d\'autres documents.

Si la contrainte d\'esquisse sélectionnée est déjà liée à une expression, cette expression est effacée et réinitialisée pour pointer vers l\'alias de feuille de calcul nouvellement créé. La valeur de l\'alias est créée par la valeur, vous devrez donc modifier la cellule Value dans la boîte de dialogue pour recréer l\'expression, par exemple {{Value|<nowiki>=</nowiki>width * height}} où largeur et hauteur sont des alias dans la feuille de calcul. Vous ne pouvez pas renvoyer à des contraintes dans l\'esquisse, car cela créerait une redondance cyclique.

## Limitations

-   Seules les colonnes A et B sont prises en charge.
-   La recherche d\'une nouvelle ligne vide commence à la ligne 2, en ignorant tout contenu existant dans la ligne 1.
-   Les cellules de prévisualisation dans la boîte de dialogue sont en lecture seule et ne peuvent pas être modifiées dans la boîte de dialogue, à l\'exception de la ligne d\'alias à créer, qui est modifiée via les champs Étiquette, Alias et Valeur.



## Code du gestionnaire d\'extensions 


{{Codeextralink|https://gist.github.com/mwganson/005765b49123d80cbb54569e081779a1/raw/556bf483802da8d756f869a4f894ba150d322305/ConstraintToAlias.FCMacro|ConstraintToAlias.FCMacro}}



## Icône

Icône de la barre d\'outils ![](images/ConstraintToAlias.svg )

## Script

**Macro ConstraintToAlias.FCMacro**


{{CodeDownload|https://gist.github.com/mwganson/005765b49123d80cbb54569e081779a1|ConstraintToAlias.FCMacro}}



---
⏵ [documentation index](../README.md) > Macro ConstraintToAlias/fr
