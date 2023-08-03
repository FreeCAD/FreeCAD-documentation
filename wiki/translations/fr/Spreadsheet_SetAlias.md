---
 GuiCommand:
   Name: Spreadsheet SetAlias
   Name/fr: Spreadsheet Alias
   MenuLocation: 
   Workbenches: Spreadsheet_Workbench/fr
   Version: 0.17
---

# Spreadsheet SetAlias/fr

## Description

L\'outil **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Spreadsheet Alias](Spreadsheet_SetAlias/fr.md)** ouvre une boîte de dialogue pour configurer un alias pour une cellule. Au lieu d\'utiliser le nom de cellule exact comme A2, B3 ou C4, un nom personnalisé peut être utilisé.



## Utilisation

1.  Assurez-vous qu\'il y a une **[<img src=images/Spreadsheet_CreateSheet.svg style="width:16px"> [feuille de calcul](Spreadsheet_CreateSheet/fr.md)** ouverte pour que le bouton soit activé.
2.  Sélectionnez une cellule.
3.  Appuyez sur le bouton **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Alias](Spreadsheet_SetAlias/fr.md)**.
4.  Saisissez un alias :
    -   Seuls les caractères alphanumériques et les traits de soulignement (`A` à `Z`, `a` à `z`, `0` à `9` et `_`) sont autorisés.
    -   Le premier caractère doit être une lettre.
    -   L\'utilisation de 1 ou 2 lettres majuscules suivies de 1 à 5 chiffres, par exemple `AB123`, n\'est pas autorisée car elle est considérée comme une adresse de cellule.
    -   Les séquences de caractères qui sont des unités ne sont pas autorisées. Par exemple, `W` est un alias invalide car il s\'agit de l\'unité de [Watt](https://fr.wikipedia.org/wiki/Watt). Comme FreeCAD supporte de nombreuses unités, il est préférable d\'éviter les alias courts. Voir [Expressions](Expressions/fr#Unit.C3.A9s.md).
    -   L\'utilisation des constantes mathématiques `pi` et `e` comme alias conduira à des erreurs et doit être évitée.
    -   N\'utilisez pas d\'espaces dans les alias, car cela créerait également des erreurs.





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet SetAlias/fr
