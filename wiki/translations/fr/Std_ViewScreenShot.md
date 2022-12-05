---
- GuiCommand:/fr
   Name:Std_ViewScreenShot
   Name/fr:Std Capture d'écran
   MenuLocation:Outils → Enregistrer l'image...
   Workbenches:Tous
   SeeAlso:[Std Imprimer](Std_Print/fr.md), [Std Exporter au format PDF](Std_PrintPdf/fr.md), [Macro Snip](Macro_Snip/fr.md)
---

# Std ViewScreenShot/fr

## Description

La commande **Std Capture d\'écran** ouvre une boîte de dialogue pour créer un fichier image, une capture d\'écran, à partir de la [vue 3D](3D_view/fr.md) active.

<img alt="" src=images/Save_picture.png  style="width:800px;"> 
*La boîte de dialogue Enregistrer l'image après avoir appuyé sur le bouton avancé*

## Utilisation

1.  Sélectionnez l\'option **Outils → <img src="images/Std_ViewScreenShot.svg" width=16px> Enregistrer l'image...** dans le menu.
2.  La boîte de dialogue Enregistrer l\'image s\'ouvre.
3.  Appuyez sur le bouton **Etendu** pour afficher un panneau supplémentaire dans la boîte de dialogue. Pour plus d\'informations, voir [Options](#Options.md).
4.  Naviguez éventuellement vers le bon dossier.
5.  Saisissez un nom de fichier et sélectionnez le type de fichier.
6.  Appuyez sur le bouton **Enregistrer** pour créer le fichier image et fermer la boîte de dialogue.

## Options

### Tailles de l\'image 

1.  Sélectionnez une taille standard dans la liste déroulante **Tailles standards** ou spécifiez la **Largeur** et la **Hauteur** pour une taille personnalisée.
2.  En option, appuyez sur un bouton **Rapport d\'aspect** pour définir le rapport largeur/hauteur de l\'image. Si la zone de saisie **Largeur** est choisie, la hauteur de l\'image changera et vice versa.

### Propriétés de l\'image 

1.  Sélectionnez une option dans la liste déroulante **Arrière-plan** :
    -   
        {{Value|Current}}
        
        Cette option utilise l\'arrière-plan de la vue 3D.

    -   
        {{Value|White}}
        

    -   
        {{Value|Black}}
        

    -   
        {{Value|Transparent}}
        
        Tous les formats d\'image ne prennent pas en charge la transparence.
2.  Sélectionnez une option dans la liste déroulante **Méthode de création** :
    -   
        {{Value|Offscreen (New)}}
        
        Il s\'agit de la méthode par défaut. Cette méthode prend en charge [anti-aliasing](https://en.wikipedia.org/wiki/Multisample_anti-aliasing). *Informations techniques: les classes les plus importantes pour cette méthode sont QOffscreenSurface et QOpenGLFramebufferObject de Qt.*

    -   
        {{Value|Offscreen (Vieille)}}
        
        Cette méthode ne fonctionne pas sur de nombreux systèmes Linux récents car elle repose sur le pilote graphique. Cette méthode ne prend pas en charge l\'anticrénelage. *Informations techniques: il s\'agit d\'une véritable méthode de rendu hors écran qui utilise uniquement les fonctions de la bibliothèque Coin3d.*

    -   
        {{Value|Framebuffer (personnalisé)}}
        
        Cette méthode prend en charge l\'anticrénelage. *Informations techniques: si l\'anti-aliasing est désactivé, cette méthode lit l\'image directement à partir du rendu graphique, sinon elle se transforme en un framebuffer et obtient l\'image à partir de là. L\'élément clé de cette méthode est la classe QOpenGLFramebufferObject de Qt.*

    -   
        {{Value|Framebuffer (tel quel)}}
        
        Cette méthode utilise les mêmes techniques que **Framebuffer (personnalisé)**. Il prend également en charge l\'anticrénelage, mais présente certaines limitations liées aux tailles personnalisées et utilise toujours l\'arrière-plan actuel de la vue 3D.

### Commentaire de l\'image 

1.  Sélectionnez l\'option {{RadioButton|TRUE|Insérer MIBA}} pour ajouter des informations [MIBA](MIBA.md) au fichier. Tous les formats d\'image ne le prennent pas en charge.
2.  Ou sélectionnez l\'option {{RadioButton|TRUE|Insérer un commentaire}} et tapez un commentaire dans le champ de texte pour incorporer un commentaire dans le fichier. Tous les formats d\'image ne le prennent pas en charge.
3.  Cochez la case {{CheckBox|TRUE|Ajouter un filigrane}} pour ajouter un filigrane. Le filigrane est placé dans le coin inférieur gauche de l\'image et se compose du logo et du nom FreeCAD au-dessus de l\'URL principale de FreeCAD : [www.freecadweb.org](http://www.freecadweb.org).

## Remarques

-   Le nombre de formats de fichier image disponibles peut varier selon votre système d\'exploitation.
-   Certains pilotes OpenGL n\'autorisent pas les rendus au-dessus d\'une certaine taille maximale.

## Préférences

-   L\'arrière-plan de la vue 3D peut être modifié dans les préférences : **Édition → Préférences → Affichage → Couleurs → Couleur d'arrière plan**. Voir [Réglage des préférences](Preferences_Editor/fr#Couleurs.md).
-   Pour modifier l\'anticrénelage de la vue 3D : **Édition → Préférences → Affichage → Vue 3D → Rendering → Anticrénelage**. Voir [Réglage des préférences](Preferences_Editor/fr#Vue_3D.md).

## Script

Il est possible de créer des captures d\'écran avec du code Python.


```python
Gui.ActiveDocument.ActiveView.saveImage('C:/temp/test.png',1656,783,'Current')
```

Ce script enregistre une série de captures d\'écran de différentes tailles et de différentes directions. Le type de caméra, orthographique ou en perspective, est également modifié.


```python
import Part, PartGui
# Loading test part
Part.open('C:/Documents and Settings/jriegel/My Documents/Projects/FreeCAD/data/Blade.stp')
OutDir = 'C:/temp/'
 
# Creating images with different Views, Cameras and sizes
for p in ['PerspectiveCamera','OrthographicCamera']:
    Gui.SendMsgToActiveView(p)
    for f in ['ViewAxo','ViewFront','ViewTop']:
        Gui.SendMsgToActiveView(f)
        for x,y in [[500,500],[1000,3000],[3000,1000],[3000,3000],[8000,8000]]:
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.jpg',x,y,'White')
            Gui.ActiveDocument.ActiveView.saveImage(OutDir + 'Blade_' + p +'_' + f + '_' + x + '_' + y + '.png',x,y,'Transparent')

# Close active document
App.closeDocument(App.ActiveDocument.Name)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std ViewScreenShot/fr
