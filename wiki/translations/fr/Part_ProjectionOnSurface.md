---
- GuiCommand:/fr
   Name:Part ProjectionOnSurface
   Name/fr:Part Projection sur surface
   MenuLocation:Pièce → Créer une projection sur une surface...
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
---

# Part ProjectionOnSurface/fr

## Description


**<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Projection sur surface](Part_ProjectionOnSurface/fr.md)**

est utilisé pour projeter une <img src=images/_Draft_ShapeString.svg style="width:forme](Shape/fr.md) au-dessus d\'une surface depuis une autre [forme](Shape/fr.md). Cela peut être utilisé pour projeter un logo ou un objet texte (voir **[16px"> [Draft Formes à partir texte](Draft_ShapeString/fr.md)**) sur des surfaces courbes pour créer des effets intéressants.

À partir d\'une _ pour des effets tels que la gravure ou l\'estampage.

<img alt="" src=images/Part_ProjectionOnSurface1.png  style="width:300px;"> <img alt="" src=images/Part_ProjectionOnSurface2.png  style="width:300px;">


*Projection d'un logo sur une surface courbe*

## Utilisation

1.  Assurez-vous d\'avoir au moins deux objets dans votre document; l\'objet \"source\" que vous souhaitez projeter et l\'objet \"cible\" où la projection sera faite.
2.  Cliquez sur **<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Créer une projection sur une surface](Part_ProjectionOnSurface/fr.md)** pour lancer un [Panneau des tâches](Task_Panel/fr.md) avec différentes options.
3.  Cliquez sur **Select projection surface**, puis cliquez sur la surface \"cible\" où la projection sera créée.
4.  Cliquez ensuite sur le bouton spécifique pour choisir le type de sous-élément que vous souhaitez ajouter à votre objet de projection.
    -   
        **Add face**
        
        : sélectionnez une face source.

    -   
        **Add wire**
        
        : sélectionnez une arête source. L\'outil extraira tout le fil auquel appartient l\'arête. Par exemple, en choisissant une seule arête d\'un polygone, il projettera le polygone entier.

    -   
        **Add edge**
        
        : sélectionnez un bord source. L\'outil projettera uniquement l\'arête sélectionnée.

    -   Une fois qu\'un bouton est enfoncé, choisissez un sous-élément dans la [Vue 3D](3D_view/fr.md). Si vous souhaitez le désélectionner, choisissez à nouveau le même élément.

    -   Lorsque vous êtes satisfait de votre sélection, appuyez sur le même bouton **Add...** pour quitter le mode de sélection.
5.  Cliquez ensuite sur le bouton radio spécifique pour choisir le type de forme de projection à créer.
    -   
        {{RadioButton|TRUE|Show all}}
        
        : il affichera tous les types de fils fermés et d\'arêtes sur la surface cible. Si un sous-élément \"face\" a été sélectionné à l\'étape précédente, un aperçu d\'un objet solide extrudé à partir de la projection sera affiché, en fonction de la valeur de **Extrude height**.

    -   
        {{RadioButton|TRUE|Show faces}}
        
        : il affichera un aperçu d\'une face remplie sur la surface cible. Cela ne fonctionnera que si vous avez sélectionné un sous-élément \"face\" à l\'étape précédente; si vous avez sélectionné un \"fil\" fermé, seules les arêtes (pas de face) seront créées comme projection; si vous avez sélectionné «arêtes», seules ces arêtes seront créées comme projection.

    -   
        {{RadioButton|TRUE|Show bords}}
        
        : il affichera un aperçu des arêtes sur la surface cible. Cela fonctionnera si vous avez ajouté un sous-élément «face», «fil» ou «bord» à l\'étape précédente; même si vous avez ajouté une \"face\" remplie, seules les arêtes seront créées en tant que projection.
6.  Appuyez sur le **OK** pour terminer l\'opération et produire le nouvel objet de projection.

Remarques:

-   La direction de projection est automatiquement prise à partir de la direction de la caméra dans la [Vue 3D](3D_view/fr.md) au moment où l\'outil est lancé.
-   Pour changer la direction, déplacez la caméra et appuyez sur **Obtenir la direction actuelle de la caméra**.
-   Vous pouvez également appuyer sur les boutons **X:**, **Y:** ou **Z:** pour définir la direction de projection vers les principaux axes globaux, +X, -X, +Y, -Y, +Z, ou -Z.
-   Cependant, notez que changer la direction de projection ne mettra pas automatiquement à jour l\'aperçu de projection; pour ce faire, vous devez re-sélectionner la géométrie en appuyant sur les boutons **Ajouter...** et en sélectionnant à nouveau les sous-éléments.

## Options

-    **Extrude height**: c\'est la hauteur de la forme solide qui est créée en extrudant la face projetée à partir de la surface cible et le long du négatif de la direction de projection. Par exemple, si la direction de projection est le long de +Y {{Value|(0, 1, 0)}}, l\'extrusion sera créée dans la direction -Y {{Value|(0, -1, 0)}}. Cette extrusion solide ne sera créée que si le sous-élément sélectionné était une face fermée, en appuyant sur le bouton **Add face** et en choisissant l\'option {{RadioButton|TRUE|Show all}}.

-    **Solid depth**: c\'est la distance à laquelle l\'objet de projection est déplacé le long de la direction de projection. Les valeurs négatives déplaceront l\'objet dans la direction opposée; cela permet de créer une projection décalée de la surface cible.

## Limitations

L\'algorithme de projection n\'est parfois pas en mesure de créer une face de projection valide. Si cela se produit, une extrusion solide ne pourra pas non plus être créée.

Si ça arrive:

-   Vérifiez si votre face source est valide, essayez d\'exécuter l\'outil **<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)** pour obtenir des indices.
-   Vérifiez si la direction de projection est valide. La face source peut-elle être projetée de manière réaliste sur la surface cible? Une projection droite toucherait-elle la surface? Ajustez la caméra de sorte que la face source soit devant la surface cible et réessayez.
-   Essayez d\'utiliser l\'option {{RadioButton|TRUE|Afficher les bords}}. Les bords sont-ils correctement projetés? Essayez de créer à la main une face avec les bords.

## Liens

-   Fil de discussion du forum: [Project faces onto bent surface](https://forum.freecadweb.org/viewtopic.php?f=9&t=33700)

## Exemples

---
[documentation index](../README.md) > [Part](Part_Workbench.md) > Part ProjectionOnSurface/fr
