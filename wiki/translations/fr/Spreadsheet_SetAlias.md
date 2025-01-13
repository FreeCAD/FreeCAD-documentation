---
 GuiCommand:
   Name: Spreadsheet SetAlias
   Name/fr: Spreadsheet Alias
   MenuLocation: 
   Workbenches: Spreadsheet_Workbench/fr
   Shortcut: **Ctrl**+**Maj**+**A**
   Version: 0.17
---

# Spreadsheet SetAlias/fr

## Description

L\'outil <img alt="" src=images/Spreadsheet_SetAlias.svg  style="width:24px;"> **Spreadsheet Alias** ouvre une boîte de dialogue pour configurer un alias pour une cellule. Au lieu d\'utiliser l\'exact nom de la cellule tel que A2, B3 ou C4, un nom personnalisé peut être utilisé.



## Utilisation

1.  Assurez-vous qu\'il existe une [feuille de calcul](Spreadsheet_CreateSheet/fr.md) active.
2.  Sélectionnez une cellule.
3.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **[<img src=images/Spreadsheet_SetAlias.svg style="width:16px"> [Alias](Spreadsheet_SetAlias/fr.md)**.
    -   Utilisez le raccourci clavier : **Ctrl**+**Maj**+**A**.
4.  Saisissez un alias :
    -   Seuls les caractères alphanumériques et les traits de soulignement (`A` à `Z`, `a` à `z`, `0` à `9` et `_`) sont autorisés.
    -   Le premier caractère doit être une lettre.
    -   L\'utilisation de 1 ou 2 lettres majuscules suivies de 1 à 5 chiffres, par exemple `AB123`, n\'est pas autorisée car elle est considérée comme une adresse de cellule.
    -   Les séquences de caractères qui sont des unités ne sont pas autorisées. Par exemple, `W` est un alias invalide car il s\'agit de l\'unité de [Watt](https://fr.wikipedia.org/wiki/Watt). Comme FreeCAD supporte de nombreuses unités, il est préférable d\'éviter les alias courts. Voir [Expressions](Expressions/fr#Unit.C3.A9s.md).
    -   L\'utilisation des constantes mathématiques `pi` et `e` comme alias conduira à des erreurs et doit être évitée.
    -   N\'utilisez pas d\'espaces dans les alias, cela créerait également des erreurs.





{{Spreadsheet_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Spreadsheet](Spreadsheet_Workbench.md) > Spreadsheet SetAlias/fr
