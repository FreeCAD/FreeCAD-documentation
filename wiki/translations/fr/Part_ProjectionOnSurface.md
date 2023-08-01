---
- GuiCommand:
   Name:Part ProjectionOnSurface
   Name/fr:Part Projection sur surface
   MenuLocation:Part - Créer une projection sur une surface...
   Workbenches:[Part](Part_Workbench/fr.md)
   Version:0.19
---

# Part ProjectionOnSurface/fr



## Description


**[<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Projection sur surface](Part_ProjectionOnSurface/fr.md)**

est utilisé pour projeter une [forme](Shape/fr.md) au-dessus d\'une surface depuis une autre [forme](Shape/fr.md). Cela peut être utilisé pour projeter un logo ou un objet texte (voir **[<img src=images/_Draft_ShapeString.svg style="width:16px"> [Draft Formes à partir texte](Draft_ShapeString/fr.md)**) sur des surfaces courbes pour créer des effets intéressants.

À partir d\'une [forme](Shape/fr.md), cet outil peut projeter des arêtes, des polylignes (arêtes fermées) ou des faces entières à partir de celle-ci. Le résultat peut être de nouvelles arêtes, de nouvelles polylignes, de nouvelles faces ou même de nouveaux solides extrudés qui peuvent être utilisés dans des <img alt="" src=images/Part_Boolean.svg  style="width:24px;"> [opérations booléennes](Part_Boolean/fr.md) pour des effets tels que la gravure ou l\'estampage.

<img alt="" src=images/Part_ProjectionOnSurface1.png  style="width:300px;"> <img alt="" src=images/Part_ProjectionOnSurface2.png  style="width:300px;">



*Projection d'un logo sur une surface courbe*



## Utilisation

1.  Assurez-vous d\'avoir au moins deux objets dans votre document; l\'objet \"source\" que vous souhaitez projeter et l\'objet \"cible\" où la projection sera faite.
2.  Cliquez sur **[<img src=images/Part_ProjectionOnSurface.svg style="width:16px"> [Créer une projection sur une surface](Part_ProjectionOnSurface/fr.md)** pour lancer un [Panneau des tâches](Task_Panel/fr.md) avec différentes options.
3.  Cliquez sur **Sélectionner la surface de projection**, puis cliquez sur la surface \"cible\" où la projection sera créée.
4.  Cliquez ensuite sur le bouton spécifique pour choisir le type de sous-élément que vous souhaitez ajouter à votre objet de projection.
    -   
        **Ajouter une face**
        
        : sélectionnez une face source.

    -   
        **Ajouter une polyligne**
        
        : sélectionnez une arête source. L\'outil extraira la polyligne entière auquel appartient l\'arête. Par exemple, en choisissant une seule arête d\'un polygone, il projettera le polygone entier.

    -   
        **Ajouter une arête**
        
        : sélectionnez un bord source. L\'outil projettera uniquement l\'arête sélectionnée.

    -   Une fois qu\'un bouton est enfoncé, choisissez un sous-élément dans la [Vue 3D](3D_view/fr.md). Si vous souhaitez le désélectionner, choisissez à nouveau le même élément.

    -   Lorsque vous êtes satisfait de votre sélection, appuyez sur le même bouton **Ajouter...** pour quitter le mode de sélection.
5.  Cliquez ensuite sur le bouton radio spécifique pour choisir le type de forme de projection à créer.
    -   
        {{RadioButton|TRUE|Tout afficher}}
        
        : cela affichera tous les types de polylignes fermées et d\'arêtes sur la surface cible. Si un sous-élément \"face\" a été sélectionné à l\'étape précédente, un aperçu d\'un objet solide extrudé à partir de la projection sera affiché, en fonction de la valeur de **Hauteur de l'extrusion**.

    -   
        {{RadioButton|TRUE|Afficher les faces}}
        
        : cela affichera un aperçu d\'une face remplie sur la surface cible. Cela ne fonctionnera que si vous avez sélectionné un sous-élément \"face\" à l\'étape précédente; si vous avez sélectionné une \"polyligne\" fermée, seules les arêtes (pas de face) seront créées comme projection. Si vous avez sélectionné \"arêtes\", seules ces arêtes seront créées comme projection.

    -   
        {{RadioButton|TRUE|Afficher les arêtes}}
        
        : cela affichera un aperçu des arêtes sur la surface cible. Cela fonctionnera si vous avez ajouté un sous-élément \"face\", \"polyligne\" ou \"arête\" à l\'étape précédente. Même si vous avez ajouté une \"face\" remplie, seules les arêtes seront créées en tant que projection.
6.  Appuyez sur le **OK** pour terminer l\'opération et produire le nouvel objet de projection.

Remarques :

-   La direction de projection est automatiquement prise à partir de la direction de la caméra dans la [Vue 3D](3D_view/fr.md) au moment où l\'outil est lancé.
-   Pour changer la direction, déplacez la caméra et appuyez sur **Obtenir la direction actuelle de la caméra**.
-   Vous pouvez également appuyer sur les boutons **X :**, **Y :** ou **Z :** pour définir la direction de projection vers les principaux axes globaux, +X, -X, +Y, -Y, +Z, ou -Z.
-   Cependant, notez que changer la direction de projection ne mettra pas automatiquement à jour l\'aperçu de projection. Pour ce faire, vous devez re-sélectionner la géométrie en appuyant sur les boutons **Ajouter...** et en sélectionnant à nouveau les sous-éléments.



## Options

-    **Hauteur de l'extrusion**: hauteur de la forme solide qui est créée en extrudant la face projetée à partir de la surface cible et le long du négatif de la direction de projection. Par exemple, si la direction de projection est le long de +Y {{Value|(0, 1, 0)}}, l\'extrusion sera créée dans la direction -Y {{Value|(0, -1, 0)}}. Cette extrusion solide ne sera créée que si le sous-élément sélectionné était une face fermée, en appuyant sur le bouton **Ajouter une face** et en choisissant l\'option {{RadioButton|TRUE|Tout afficher}}.

-    **Profondeur du solide**: distance à laquelle l\'objet de projection est déplacé le long de la direction de projection. Les valeurs négatives déplaceront l\'objet dans la direction opposée. Cela permet de créer une projection décalée de la surface cible.



## Limitations

L\'algorithme de projection n\'est parfois pas en mesure de créer une face de projection valide. Si cela se produit, une extrusion solide ne pourra pas non plus être créée.

Si ça arrive :

-   Vérifiez si votre face source est valide. Lancer l\'outil **[<img src=images/Part_CheckGeometry.svg style="width:16px"> [Part Vérifier la géométrie](Part_CheckGeometry/fr.md)** pour obtenir des indices.
-   Vérifiez si la direction de projection est valide. La face source peut-elle être projetée de manière réaliste sur la surface cible? Une projection droite toucherait-elle la surface? Ajustez la caméra de sorte que la face source soit devant la surface cible et réessayez.
-   Essayez d\'utiliser l\'option {{RadioButton|TRUE|Afficher les bords}}. Les bords sont-ils correctement projetés? Essayez de créer à la main une face avec les bords.

La projection effectuée dans l\'atelier Part n\'est pas paramétrique. Si vous avez besoin d\'un flux de travail paramétrique, veuillez consulter la [classe Projection](https://gist.github.com/CsatiZoltan/f4fd10bf20923143ba0e0678ea1d3d61), qui est un objet scripté en Python, destiné à une utilisation programmatique.



## Liens

-   Fil de discussion du forum : [Project faces onto bent surface](https://forum.freecadweb.org/viewtopic.php?f=9&t=33700)



## Exemples



---
![](images/Button_right.svg) [documentation index](../README.md) > [Part](Part_Workbench.md) > Part ProjectionOnSurface/fr
