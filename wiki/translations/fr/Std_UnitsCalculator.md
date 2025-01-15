---
 GuiCommand:
   Name: Std UnitsCalculator
   Name/fr: Std Convertisseur d'unités
   MenuLocation: Outils , Convertisseur d'unités...
   Workbenches: Tous
---

# Std UnitsCalculator/fr

## Description

La commande **Std Convertisseur d\'unités** ouvre le convertisseur d\'unités. Le convertisseur d\'unités peut être utilisé pour convertir des valeurs d\'un système d\'unités à un autre.

![](images/Std_UnitsCalculator_Dialog.png ) 
*Fenêtre de dialogue du convertisseur d'unités*



## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_UnitsCalculator.svg" width=16px> Convertisseur d'unités...** du menu.
2.  La fenêtre de dialogue **Convertisseur d\'unités** s\'ouvre. Pour plus d\'informations, voir [Options](#Options.md).
3.  La fenêtre de dialogue est non modale, ce qui signifie qu\'elle peut rester ouverte pendant que vous travaillez dans FreeCAD.
4.  Appuyez sur le bouton **Fermer** pour fermer la fenêtre de dialogue.

## Options



### Première ligne 

1.  Entrez une valeur avec des unités dans la première zone de saisie. Par exemple {{Value|10 mm}}.
    -   Les unités avec exposants doivent être saisies en utilisant la notation {{Value|^}}. Par exemple {{Value|1 m^2}}.
    -   Si la valeur d\'entrée ne peut pas être reconnue ou si les unités sont inconnues, la case **=\>** affichera le message \"erreur de syntaxe\".
2.  Entrez l\'unité cible dans la zone de saisie **en**. Par exemple {{Value|in}}.
    -   Si les unités sont inconnues, la case **=\>** affichera le message \"unité inconnue\".
    -   Si les unités de la première et deuxième zone de saisie ne correspondent pas, la case **=\>** affichera le message \"unité incompatible\". Dans l\'exemple, les unités à convertir \"mm\" et \"in\" sont deux unités de longueur.
3.  S\'il n\'y a pas d\'erreur de saisie, la case **=\>** affichera immédiatement le résultat. Pour les valeurs de l\'exemple, le résultat est {{Value|0,394 in}}.
4.  Appuyez sur le bouton **Copier** pour copier le contenu de la case **=\>** dans le presse-papiers. La valeur peut ensuite par exemple être collée dans un panneau de tâches ou une fenêtre de dialogue FreeCAD.



### Zone de texte 

1.  La conversion effectuée dans la ligne supérieure peut être copiée dans la zone de texte en appuyant sur **Entrée** dans la première ou la deuxième zone de saisie.
2.  La zone de texte peut contenir plusieurs conversions et son contenu peut être sélectionné et copié dans le presse-papiers avec **Ctrl+C** et utilisé dans d\'autres programmes.



### Quantité

1.  Sélectionnez une option dans la liste déroulante **Système d\'unités**. Ce sera le système d\'unités cible. Sélectionnez **Preference system** pour utiliser le système d\'unités défini dans les [préférences](Preferences_Editor/fr#Unit.C3.A9s.md).
2.  Sélectionnez une option dans la liste déroulante **Catégorie d\'unités**.
3.  Entrez une valeur avec des unités dans la zone de saisie **Quantité**. Les unités doivent correspondre à la catégorie d\'unités.
4.  Cliquez dans la zone de saisie **Décimales** et appuyez sur **Entrée** pour convertir la valeur dans la zone de saisie **Quantité**.



## Remarques

-   Voir la page [Expressions](Expressions/fr#Unit.C3.A9s.md) pour une liste de toutes les unités connues.



---
⏵ [documentation index](../README.md) > Std UnitsCalculator/fr
