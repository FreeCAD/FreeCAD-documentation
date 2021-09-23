---
- GuiCommand:/fr
   Name:Std New
   Name/fr:Std Nouveau
   MenuLocation:Fichier → Nouveau
   Workbenches:Tous
   Shortcut:**Ctrl**+**N**
   SeeAlso:[Std Ouvrir](Std_Open/fr.md), [Std Importer](Std_Import/fr.md)
---

# Std New/fr

## Description

La commande **Std Nouveau** crée un nouveau document vide et en fait le document actif.

## Utilisation

1.  Lancez la commande de plusieurs manières:
    -   En appuyant sur le bouton **<img src="images/Std_New.svg" width=16px> [Std Nouveau](Std_New/fr.md)
**
2.  \* Sélectionnez l\'option **File → <img src="images/Std_New.svg" width=16px> Nouveau** dans le menu.
3.  \* Utilisez le raccourci clavier: **Ctrl**+**N**.

## Préférences

-   FreeCAD créera un nouveau document au démarrage si **Outils → Editer paramètres ... → BaseApp → Preferences → Document → CreateNewDoc** est réglé sur `True`. Ce paramètre peut également être modifié dans les [Réglage des préférences](Preferences_Editor/fr#Document.md).
-   Certaines propriétés du document: noms d\'auteur, nom de l\'entreprise et informations de licence, peuvent être prédéfinies dans [Réglage des préférences](Preferences_Editor/fr#Document.md).

## Propriétés

La plupart des propriétés peuvent également être modifiées dans la boîte de dialogue de la commande [Std Information sur le projet](Std_ProjectInfo/fr.md).

-    **Comment**: n\'importe quel commentaire.

-    **Company**: nom de l\'entreprise. **Peut être prédéfini**.

-    **Created By**: nom de l\'auteur. **Peut être prédéfini**.

-    **Creation Date**: horodatage automatique. **Non modifiable**.

-    **File Name**: le chemin complet du fichier. Vide si le document n\'a pas été enregistré. **Non modifiable**.

-    **Id**: Pas encore implémenté.

-    **Label**: nom qui apparaîtra dans la [vue en arborescence](tree_view/fr.md). Par défaut, le nom du document.

-    **Last Modified By**: nom de l\'auteur. **Peut être prédéfini**.

-    **Last Modified Date**: horodatage automatique. **Non modifiable**.

-    **License**: type de licence. **Peut être prédéfini**.

-    **License URL**: URL de licence. **Peut être prédéfini**.

-    **Show Hidden**: Si la valeur est true, les éléments qui ont été masqués dans la [vue en arborescence](tree_view/fr.md) seront quand même affichés. Masquer des éléments dans l\'arborescence peut être utile lorsque vous travaillez sur des modèles plus grands.

-    **Tip**: Pas encore implémenté.

-    **Tip Name**: Pas encore implémenté.

-    **Transient Dir**: répertoire transitoire utilisé pour les données de récupération. **Non modifiable**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour créer un nouveau document, utilisez la méthode `newDocument([name], [hidden<nowiki>=</nowiki>False])` de l\'application FreeCAD. Le nom du document doit être unique, ce qui est vérifié automatiquement. Si aucun nom n\'est fourni, le document sera nommé \"Sans titre\". Si `hidden<nowiki>=</nowiki>True` est utilisé, le nouveau document ne sera pas affiché dans l\'interface graphique et aucun onglet n\'apparaîtra pour ce document.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'test.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveAs(fnm)

FreeCAD.closeDocument(doc.Name)

doc = FreeCAD.open(fnm)
doc.save()

FreeCAD.closeDocument(doc.Name)
```





{{Std Base navi

}}

---
[documentation index](../README.md) > Std New/fr
