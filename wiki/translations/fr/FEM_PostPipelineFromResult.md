---
- GuiCommand:/fr
   Name:FEM PostPipelineFromResult
   Name/fr:FEM Post pipeline des résultats
   MenuLocation:Results → post pipeline from result
   Workbenches:[FEM](FEM_Workbench/fr.md)
   Version:0.17
   SeeAlso:[FEM Tutoriel](FEM_tutorial/fr.md)
---

# FEM PostPipelineFromResult/fr

**\* Vous avez besoin d\'un objet résultat valide dans le **<img src="images/FEM_Analysis.svg" width=24px> [FEM Conteneur d'analyse](FEM_Analysis/fr.md)
**, tel que **CalculiX static results**.**

## Description

Pipeline est un objet de résultat qui crée une nouvelle représentation graphique des résultats d\'analyse FEM sur la pièce analysée. Il ajoute une gamme de couleurs et d'autres options d'affichage.

## Utilisation

-   Sélectionnez l\'objet de résultat
-   Cliquez sur le bouton <img alt="" src=images/FEM_PostPipelineFromResult.svg  style="width:24px;"> ou cliquez sur le menu **Résultats** et sur l\'élément **Post Pipeline from results**. Un nouvel objet appelé \"Pipeline\" sera ajouté à votre document. notez si apparaît en dehors du conteneur d\'analyse.
-   Double-cliquez sur le nouvel objet Pipeline dans l'arborescence du modèle et sélectionnez le type de propriétés à afficher. Les paramètres typiques sont: Mode: **Surface**, Field: **Stress Von Mises**

![](images/Pipeline.PNG )

:\* Mode: comment dessiner les résultats

:\* Field: Propriété de résultat à dessiner

:\* Vector: Si une propriété est un vecteur, vous pouvez limiter les données à un axe (X, Y, Z) ou sélectionner Magnitude pour utiliser la valeur du vecteur.

-   Si vous ne voyez aucun modèle dans la zone graphique, allez dans et activez **Edition → Préférences → Affichage → Rendu → Couleur du rétroéclairage**.
-   Si vous double-cliquez sur l\'échelle, vous pouvez modifier les propriétés d\'affichage.

![](images/SIMTUT_05.PNG )

:\* Gradient: vous pouvez sélectionner l'ordre inversé du dégradé de couleur par défaut ou noir-blanc ou blanc-noir.

:\* Parameter range: les valeurs minimales et maximales sont automatiquement renseignées lorsque vous sélectionnez une propriété à évaluer sur l\'objet **Pipeline**. vous pouvez les modifier, mais assurez-vous de savoir ce que vous faites. Vous pouvez également modifier le nombre d\'étiquettes affichées et le nombre de décimales à afficher.

## Limitations

A nouveau, notez que la représentation des résultats (appelée VTK) par le pipeline sur la pièce affichée diffère des résultats du dégradé de couleur visibles lorsque vous terminez la solution. Les valeurs de l\'échelle de dégradé ne peuvent pas être appliquées à l\'objet résultat de la solution.





{{FEM Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [FEM](Category_FEM.md) > FEM PostPipelineFromResult/fr
