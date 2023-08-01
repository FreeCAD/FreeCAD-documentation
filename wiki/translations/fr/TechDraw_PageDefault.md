---
- GuiCommand:/fr
   Name:TechDraw PageDefault
   Name/fr:TechDraw Page par défaut
   MenuLocation:TechDraw → Page → Insérer une page par défaut
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Page à partir d'un modèle](TechDraw_PageTemplate/fr.md), [TechDraw Modèles](TechDraw_Templates/fr.md)
---

# TechDraw PageDefault/fr

## Description

L\'outil **TechDraw Page par défaut** crée un nouvel objet Page à l\'aide du fichier de modèle spécifié dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Modèle par défaut fourni avec TechDraw : A4_LandscapeTD.svg*



## Utilisation

1.  Un document actif doit exister.
2.  Il y a plusieurs façons de lancer l\'outil :
    -   Appuyez sur le bouton **<img src="images/TechDraw_PageDefault.svg" width=16px> [Insérer une page par défaut](TechDraw_PageDefault/fr.md)**.
    -   Sélectionnez l\'option **TechDraw → Page → <img src="images/TechDraw_PageDefault.svg" width=16px> Insérer une page par défaut** du menu.



## Remarques

-   Si une page est marquée comme \"Ne pas garder à jour\" soit par sa propriété **Keep Updated**, soit par l\'option **Activer/désactiver la mise à jour** du menu contextuel, soit par le réglage dans les Préférences, elle ignorera les changements dans le modèle 3D. Il se peut que vous remarquiez des anomalies (géométrie manquante, valeurs de dimension manquantes, etc.) dans l\'apparence de la page. Ces anomalies se corrigeront d\'elles-mêmes lorsque la page sera mise à jour à l\'aide de l\'outil [Redessiner une page](TechDraw_RedrawPage/fr.md). La page aura cette icône <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:24px;"> dans la [vue en arborescence](Tree_view/fr.md) pendant que la mise à jour est suspendue. Ce paramètre affecte également le processus de démarrage. Si une page est marquée comme \"Ne pas garder à jour\", elle ne sera pas dessinée au démarrage du programme.

-   Si le modèle par défaut n\'est pas spécifié dans votre fichier de configuration utilisateur `user.cfg`, l\'outil va essayer :

:   
    
```python
    $INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    





:   Où `$INSTALL_DIR` est le répertoire d\'installation de FreeCAD, par exemple :





:   
    
```python
    /usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
    
```
    



## Propriétés



### Données


{{TitleProperty|Base}}

-    **Projection Type**: type de projection par défaut (premier ou troisième angle) pour cette page.


{{TitleProperty|Page}}

-    **KeepUpdated**: si la valeur est false, la page n\'est pas mise à jour avec les modifications apportées au modèle 3D. Utile pour les dessins compliqués/lents. Voir les Remarques.

-    **Template**: lien vers l\'objet [Modèle](TechDraw_Templates/fr.md) de cette page.

-    **Views**: liste de liens vers les vues sur cette page.

-    **Scale**: échelle par défaut pour les Vues dans cette page.

-    **Next Balloon Index**: numérotation automatique des infobulles.



### Vue


{{TitleProperty|Grid}}

-    **Show Grid**: affiche une grille sur cette page. {{Version/fr|0.20}}

-    **Grid Spacing**: distance entre les lignes de la grille en mm. {{Version/fr|0.20}}



## Script

Voir [TechDraw Page à partir d\'un modèle](TechDraw_PageTemplate/fr#Script.md).





{{TechDraw Tools navi

}}



---
![](images/Button_right.svg) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/fr
