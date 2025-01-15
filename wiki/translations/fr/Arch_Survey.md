---
 GuiCommand:
   Name: Arch Survey
   Name/fr: Arch Prendre des cotes
   MenuLocation: Utilitaires , Prendre des cotes
   Workbenches: BIM_Workbench/fr
   SeeAlso: Macro_FCInfo/fr, Macro_SimpleProperties/fr
---

# Arch Survey/fr

## Description

L\'outil **Arch Prendre des cotes** permet d\'accéder à un mode spécial de mesure. Il permet de prendre rapidement des mesures et des informations sur un modèle et de transférer ces renseignements à d\'autres applications. Une fois que vous êtes en mode Prendre des cotes, et que vous cliquez sur différents sous-éléments de l\'objet 3D, vous récupérez les informations suivantes (en fonction de ce sur quoi vous cliquez) :

-   Si vous cliquez sur un bord, vous obtenez sa longueur
-   Si vous cliquez sur un sommet, vous obtenez sa hauteur (coordonnée sur l\'axe Z)
-   Si vous cliquez sur une face, vous obtenez sa surface
-   Si vous double-cliquez sur n\'importe quoi, donc sélectionner la totalité de l\'objet, vous obtenez son volume

Lorsque les informations sont recueillies, trois choses se produisent :

-   Une étiquette est placée au dessus de l\'élément sélectionné, qui affiche la valeur (par \"a\" pour la région, \"l\" pour la longueur, \"z\" à la hauteur, ou \"v\" pour le volume)
-   la valeur numérique est copiée dans le presse-papiers, vous pouvez ainsi la coller dans une autre application
-   Une ligne est affichée dans la fenêtre de FreeCAD. Lorsque vous quittez le mode survey, ces lignes peuvent être copiées et collées dans une autre application (les valeurs sont séparées par des virgules, rendant facile la conversion des données pour l\'utilisation dans une feuille de calcul)
-   La longueur totale ou la zone des éléments sur lesquels vous avez cliqué jusqu\'à présent est également imprimée dans la fenêtre de sortie
-   Chaque longueur ou zone est également enregistrée dans la fenêtre de dialogue des tâches

<img alt="" src=images/Arch_Survey_example.jpg  style="width:640px;">

*L\'image ci-dessus montre ce qui arrive lorsque vous exécutez le mode survey.*



## Utilisation

1.  Sélectionnez l\'option **Utilitaires → <img src="images/Arch_Survey.svg" width=16px> Prendre des cotes** du menu.
2.  Cliquez sur un sommet, arête, face ou double-cliquez sur l\'élément pour sélectionner l\'objet entier.
3.  Cliquez hors de toute géométrie (arrière-plan de la vue 3D) pour supprimer les étiquettes existantes, imprimer une ligne totale dans la fenêtre de dialogue Tâche et relancer le comptage des longueurs et des surfaces à partir de zéro.
4.  Cliquez sur la touche **Échap** ou sur le bouton **Fermer** pour quitter le mode Prendre des cotes et retirer toutes les étiquettes.

## Options

-   Vous pouvez ajouter une étiquette personnalisée à n\'importe quelle ligne dans la fenêtre de dialogue Tâche en cliquant sur cette ligne, puis en ajoutant un texte dans le champ de description, puis appuyez sur le bouton **set description**.
-   Une fois que vous avez terminé, avant de fermer, vous pouvez exporter le contenu de la fenêtre de dialogue Tâche en appuyant sur le bouton \"exporter CSV\". Le fichier CSV résultant peut ensuite être ouvert dans n\'importe quelle application de tableur telle qu\'Excel ou LibreOffice Calc. Les valeurs et les unités seront séparées dans le fichier CSV résultant, et les totaux sont écrits en tant que fonctions SUM().

<img alt="" src=images/Arch_Survey_spreadsheet.jpg  style="width:640px;">



## Script


**Voir aussi :**

[Arch API](Arch_API/fr.md) et [Débuter avec les scripts FreeCAD](FreeCAD_Scripting_Basics/fr.md).

L\'outil Prendre des cotes n\'a pas d\'interface de programmation, mais collecte les mêmes informations à partir de n\'importe quel objet sélectionné basé sur [Part](Part_Workbench/fr.md) et est facilement reproductible avec le script suivant :


```python
import FreeCADGui

selection = FreeCADGui.Selection.getSelectionEx()

for obj in selection:
    for element in obj.SubObjects:
        print("Area: %f", element.Area)
        print("Length: %f", element.Length)
        print("Volume: %f", element.Volume)
        print("Center of Mass: %f", element.CenterOfMass)
```



---
⏵ [documentation index](../README.md) > Arch Survey/fr
