---
- GuiCommand:/fr
   Name:Std UnitsCalculator
   Name/fr:Std Convertisseur d'unités
   MenuLocation:Outils → Calculateurs d'unités
   Workbenches:Tous
---

# Std UnitsCalculator/fr

## Description

La commande **Std Convertisseur d\'unités** ouvre la boîte de dialogue calculatrice d\'unités. Le calculateur d\'unités peut être utilisé pour convertir des valeurs d\'un système d\'unités à un autre.

![](images/Units_Calculator_it.png ) *Boîte de dialogue du calculateur d'unités*

## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_UnitsCalculator.svg" width=16px> Calculateur d'unités ...** dans le menu.
2.  La boîte de dialogue Calculatrice d\'unités s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
3.  La boîte de dialogue est non modale, ce qui signifie qu\'elle peut rester ouverte pendant que vous continuez à travailler dans FreeCAD.
4.  Appuyez sur le bouton **Fermer** pour fermer la boîte de dialogue.

## Options

### Première ligne 

1.  Entrez une valeur avec des unités dans la première zone de saisie. Par exemple {{Value|10 mm}}.
    -   Les unités avec exposants doivent être saisies en utilisant la notation {{Value|^}}. Par exemple {{Value|1 m^2}}.
    -   Si la valeur d\'entrée ne peut pas être reconnue ou si les unités sont inconnues, la boîte **=\>** affichera le message \'syntax error\' .
2.  Entrez les unités cibles dans la zone de saisie **comme**. Par exemple {{Value|in}}.
    -   Si les unités sont inconnues, la case **=\>** affichera le message \'unité inconnue\'.
    -   Si les unités des première et deuxième zones de saisie ne correspondent pas, la zone **=\>** affichera le message \'unit mismatch\'. Dans l\'exemple, les unités correspondent comme \'mm\' et \'in\' sont les deux unités de longueur.
3.  S\'il n\'y a pas d\'erreur de saisie, la case **=\>** affichera immédiatement le résultat. Pour les valeurs d\'exemple, le résultat est {{Value|0,394 in}}.
4.  Appuyez sur le bouton **Copie** pour copier le contenu de la boîte **=\>** dans le presse-papiers. La valeur peut ensuite par exemple être collée dans un panneau de tâches ou une boîte de dialogue FreeCAD.

### Zone de texte 

1.  La conversion effectuée dans la ligne supérieure peut être copiée dans la zone de texte en appuyant sur **Entrée** dans la première ou la deuxième zone de saisie.
2.  La zone de texte peut contenir plusieurs conversions et son contenu peut être sélectionné et copié dans le presse-papiers avec **Ctrl+C** et utilisé dans d\'autres programmes.

### Quantité


**Cette nouvelle partie ({{Version/fr|0.19**) du calculateur d'unités souffre encore de quelques bugs.}}

1.  Sélectionnez une option dans la liste déroulante **Système d\'unités**. Ce sera le système d\'unités cible. Sélectionnez **Preference system** pour utiliser le système d\'unités défini dans [Préférences](Preferences_Editor/fr#Unit.C3.A9s.md).
2.  Sélectionnez une option dans la liste déroulante **Catégorie d\'unité**.
3.  Entrez une valeur avec des unités dans la zone de saisie **Quantity**. Les unités doivent correspondre à la catégorie d\'unité.
    -   Si la catégorie d\'unité \'\' \'Zone\' \'\' a été sélectionnée, la saisie de certaines unités est problématique. Par exemple, pour saisir {{Value|m^2}}, vous devez d\'abord saisir {{Value|m^2}}, placez le curseur avant le caractère {{Value|^}}, puis entrez {{Value|m}}.
4.  Cliquez dans la zone de saisie **Décimales** et appuyez sur **Entrée** pour convertir la valeur dans la zone de saisie **Quantity**.

## Remarques

-   Voir la page [Expressions](Expressions/fr#Unit.C3.A9s.md) pour une liste de toutes les unités connues.





{{Std Base navi

}}

---
[documentation index](../README.md) > Std UnitsCalculator/fr
