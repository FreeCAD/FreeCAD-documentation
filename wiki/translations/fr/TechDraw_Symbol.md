---
- GuiCommand:/fr
   Name:TechDraw Symbol
   Name/fr:TechDraw Symbole SVG
   MenuLocation:TechDraw → Insérer un symbole SVG
   Workbenches:[TechDraw](TechDraw_Workbench/fr.md)
   SeeAlso:[TechDraw Modèles](TechDraw_Templates/fr.md), [Draft SVG](Draft_SVG/fr.md)
---

# TechDraw Symbol/fr

## Description

L\'outil Symbole insère un fichier [SVG](SVG/fr.md) dans la page. Ce symbole peut être tout ce qui peut aider à annoter votre dessin et ne nécessite aucune modification supplémentaire.

<img alt="" src=images/TechDraw_SymbolSVG_sample.png  style="width:250px;"> 
*Rose des vents ajoutée à la page de dessin. Ce symbole est disponible en installant le module complémentaire "symbols_library" avec le [Gestionnaire d'Addon](Std_AddonMgr/fr.md)*

## Utilisation

1.  Appuyez sur le bouton **<img src="images/TechDraw_Symbol.svg" width=16px> [Insérer un symbole SVG](TechDraw_Symbol/fr.md)
**
2.  Une boîte de dialogue s\'ouvre.
3.  Sélectionnez un emplacement et un nom de fichier.
4.  Appuyez sur **OK**

Si le symbole semble plus grand que prévu, utilisez la propriété scale (échelle) pour ajuster sa taille.

## Remarques

-    **Scale Type**pour les symboles est toujours défini sur *Personnalisé* lors de la création. C\'est pour plus de commodité, car les symboles sont presque toujours mis à l\'échelle différemment du reste des objets de la page.

## Propriétés


{{TitleProperty|Base}}

Voir [TechDraw Vue](TechDraw_View/fr#Propri.C3.A9t.C3.A9s.md)

-    **X**
    

-    **Y**
    

-    **Lock Position**
    

-    **Rotation**
    

-    **Scale Type**
    

-    **Scale**
    

-    **Caption**
    


{{TitleProperty|Drawing view}}

-    **Editable Texts**: Liste des textes modifiables, le cas échéant.

## Script


**Voir aussi:**

[TechDraw API](TechDraw_API/fr.md) et [Débuter avec les scripts](FreeCAD_Scripting_Basics/fr.md).

L\'outil Symbole peut être utilisé dans des [macro](Macros/fr.md) et à partir de la console [Python](Python/fr.md) à l\'aide des fonctions suivantes:


```python
sym = FreeCAD.ActiveDocument.addObject('TechDraw::DrawViewSymbol','TestSymbol')
rc = page.addView(anno)
f = open(unicode(symbolFileSpec,'utf-8'),'r')
svg = f.read()
f.close()
sym.Symbol = svg
rc = page.addView(sym)
```





{{TechDraw Tools navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > [TechDraw](TechDraw_Workbench.md) > TechDraw Symbol/fr
