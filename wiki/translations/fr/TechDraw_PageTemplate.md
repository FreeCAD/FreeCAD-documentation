---
- GuiCommand:/fr
   Name:TechDraw PageTemplate
   Name/fr:TechDraw Page à partir d'un modèle
   MenuLocation:TechDraw → Insérer une nouvelle page à partir d'un modèle
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Page par défaut](TechDraw_PageDefault/fr.md), [TechDraw Modèles](TechDraw_Templates/fr.md)
---

# TechDraw PageTemplate/fr

## Description

L\'outil Page à partir d\'un modèle crée un nouvel objet Page à l\'aide du fichier de modèle sélectionné dans une boîte de dialogue.

Le répertoire de départ de la boîte de dialogue peut être spécifié dans les [TechDraw Préférences](TechDraw_Preferences/fr.md).

<img alt="" src=images/A4_Landscape_ISO7200_Pep.svg  style="width:400px;">



*L'un des modèles fournis avec TechDraw : A4 ISO 7200_Pep, page orientée paysage, avec des champs de texte modifiables*

## Utilisation

-   Appuyez sur le bouton **<img src="images/TechDraw_PageTemplate.svg" width=16px> [Insérer une nouvelle page à partir d'un modèle](TechDraw_PageTemplate/fr.md)**.

## Propriétés

-    {{PropertyData/fr|Projection Type}}: Type de projection par défaut (premier ou troisième angle) pour cette Page.

-    {{PropertyData/fr|Scale}}: Échelle par défaut pour les vues dans cette page.

## Script


**Voir aussi :**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Page à partir d\'un modèle peut être utilisé dans des [macros](Macros/fr.md) et depuis la console [Python](Python/fr.md) en utilisant les fonctions suivantes : 
```python
templateFileSpec = QtGui.QFileDialog.getOpenFileName(self.baseWidget,
                                                     dialogCaption, 
                                                     dialogDir,
                                                     dialogFilter)
page = FreeCAD.ActiveDocument.addObject('TechDraw::DrawPage','Page')
template = FreeCAD.ActiveDocument.addObject('TechDraw::DrawSVGTemplate','Template')
template.Template = templateFileSpec
page.Template = FreeCAD.ActiveDocument.Template
```

-   Crée une nouvelle page dans le document courant.

### Champs de texte éditables 


**Voir aussi :**

[TechDraw Modèles](TechDraw_Templates/fr.md) pour plus d\'informations sur la création de modèles.

Voir les informations dans [TechDraw Nouvelle page par défaut](TechDraw_New_Default/fr.md) pour modifier manuellement les champs de texte modifiables dans le code de la feuille.





{{TechDraw Tools navi

}}

---
[documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw PageTemplate/fr
