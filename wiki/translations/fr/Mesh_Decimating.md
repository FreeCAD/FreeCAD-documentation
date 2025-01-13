---
 GuiCommand:
   Name: Mesh Decimating
   Name/fr: Mesh Décimation
   MenuLocation: Maillages , Décimation...
   Workbenches: Mesh_Workbench/fr
---

# Mesh Decimating/fr

## Description

La commande **Décimation** réduit le nombre de faces des objets maillés.



## Utilisation

1.  Sélectionnez un ou plusieurs objets maillés.
2.  Il existe plusieurs façons de lancer la commande :
    -   Appuyez sur le bouton **<img src="images/Mesh_Decimating.svg" width=16px> [Décimation...](Mesh_Decimating/fr.md)
**
    -   Sélectionnez l\'option **Maillages → <img src="images/Mesh_Decimating.svg" width=16px> Décimation...** du menu.
3.  Le panneau des tâches **Décimation** s\'ouvre.
4.  Spécifiez la **Réduction** :
    -   Si un seul objet maillé a été sélectionné et que vous choisissez l\'option **Nombre absolu** :
        -   Déplacez le curseur ou entrez un nombre pour spécifier un nombre absolu de faces.
    -   Dans d\'autres cas :
        -   Déplacez le curseur ou entrez un nombre pour spécifier un pourcentage de faces.
        -   Spécifiez la **Tolérance**. Le paramètre de tolérance dans le processus de simplification du maillage agit comme un paramètre de contrôle de la qualité. Imaginez que vous essayez de simplifier une sculpture détaillée en une forme plus grossière sans perdre trop de ses caractéristiques importantes. En définissant une tolérance plus élevée, vous autorisez des changements plus importants et une simplification plus poussée, ce qui se traduit par une forme plus grossière. Une tolérance plus faible signifie que le processus de simplification sera plus prudent et ne procédera qu\'à de petits ajustements, ce qui permettra de conserver une forme plus proche de l\'original. Si la tolérance est fixée à zéro, le processus simplifiera la forme autant que possible dans le cadre de ses règles, en recherchant un équilibre entre la réduction de la complexité et le maintien de la forme originale reconnaissable.
5.  Appuyez sur le bouton **OK** pour terminer la commande.





{{Mesh Tools navi

}}



---
⏵ [documentation index](../README.md) > [Mesh](Mesh_Workbench.md) > Mesh Decimating/fr
