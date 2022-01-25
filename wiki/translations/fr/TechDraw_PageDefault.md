---
- GuiCommand:/fr
   Name:TechDraw PageDefault
   Name/fr:TechDraw Page par défaut
   MenuLocation:TechDraw → Insérer une nouvelle page par défaut
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Page à partir d'un modèle](TechDraw_PageTemplate/fr.md), [TechDraw Modèles](TechDraw_Templates/fr.md)
---

# TechDraw PageDefault/fr

## Description

L\'outil Nouvelle Page par défaut crée un nouvel objet Page à l\'aide du fichier de modèle spécifié dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

<img alt="" src=images/A4_LandscapeTD.svg  style="width:400px;"> 
*Modèle par défaut fourni avec TechDraw : page A4 paysage avec champs de texte modifiables*

## Utilisation

-   Appuyez sur le bouton **<img src="images/TechDraw_PageDefault.svg" width=16px> [Insérer une nouvelle page par défaut](TechDraw_PageDefault/fr.md)**. (Un document actif doit exister.)

## Remarques

-   Si une page est marquée comme \"Ne pas garder à jour\" soit par le biais de la propriété KeepUpdated ou par le paramètre dans les Préférences, les changements dans le modèle 3D seront ignorés. Vous pouvez remarquer des anomalies (géométrie manquante, valeurs de dimension manquantes, etc.) dans l\'apparence de la page. Ceux-ci se corrigent une fois la Page mise à jour. L\'icône <img alt="" src=images/TechDraw_Tree_Page_Unsync.svg  style="width:32px;"> de la page s\'affiche dans l\'arborescence lorsque la mise à jour est suspendue. Ce paramètre affecte également le processus de démarrage. Si la page est marquée \"ne pas garder à jour\", elle ne sera pas dessinée au début du programme.

Si le modèle par défaut n\'est pas spécifié dans votre fichier de configuration utilisateur `user.cfg`, l\'outil va essayer 
```python
$INSTALL_DIR/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

Où `$INSTALL_DIR` est le répertoire d\'installation de FreeCAD, par exemple 
```python
/usr/share/freecad/Mod/TechDraw/Templates/A4_LandscapeTD.svg
```

## Propriétés

-    {{PropertyData/fr|Projection Type}}: Type de projection par défaut (premier ou troisième angle) pour cette page.

-    {{PropertyData/fr|KeepUpdated}}: Si la valeur est false, la Page n\'est pas mise à jour avec les modifications apportées au modèle 3D. Utile pour les dessins compliqués/lents. Voir les Remarques.

-    {{PropertyData/fr|Template}}: Un lien vers cette Page [Modèle](TechDraw_Templates/fr.md) .

-    {{PropertyData/fr|Views}}: Une liste de liens vers les vues sur cette page.

-    {{PropertyData/fr|Scale}}: Échelle par défaut pour les Vues dans cette Page.

## Script


**See also :**

[TechDraw API](TechDraw_API/fr.md) et [FreeCAD Script de Base](FreeCAD_Scripting_Basics/fr.md).

L\'outil Nouvelle page par défaut peut être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant les fonctions suivantes: 
```python
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Crée une nouvelle page dans le document courant.

### Champs de texte éditables 


**Voir aussi :**

[TechDraw Modèles](TechDraw_Templates/fr.md) pour plus d\'informations sur la création de modèles.

Une fois qu\'une nouvelle page a été créée, son attribut `Template` contient un dictionnaire `EditableTexts` avec le nom des champs modifiables (keys) et leurs valeurs textuelles. Copiez ce dictionnaire dans une variable, apportez des modifications, puis réaffectez le dictionnaire à l\'attribut `EditableTexts` pour afficher les modifications.


```python
page = FreeCAD.ActiveDocument.Page
texts = page.Template.EditableTexts

for key, value in texts.items():
    print("{0} = {1}".format(key, value))

texts["FC-Title"] = "The title of my page"
page.Template.EditableTexts = texts
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageDefault/fr
