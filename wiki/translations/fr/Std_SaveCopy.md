---
- GuiCommand:/fr
   Name:Std SaveCopy
   Name/fr:Std Enregistrer une copie
   MenuLocation:Fichier → Enregistrer une copie...
   Workbenches:Tous
   SeeAlso:[Std Enregistrer sous](Std_SaveAs/fr.md), [Std Enregistrer](Std_Save/fr.md)
---

# Std SaveCopy/fr

## Description

La commande **Std Enregistrer une copie** enregistre une copie du document actif sous un nouveau nom de fichier.

## Utilisation

1.  Sélectionnez l\'option **Fichier → <img src="images/Std_SaveCopy.svg" width=16px> Enregistrer une copie...** dans le menu.
2.  Entrez un nom de fichier dans la boîte de dialogue.
3.  Appuyez sur le bouton **Enregistrer**.

## Options

-   Appuyez sur **Echap** ou sur le bouton **Annuler** pour annuler la commande.

## Préférences

-   Le dernier emplacement de fichier utilisé est stocké: **Outils → Editer les paramètres... → BaseApp → Preferences → General → FileOpenSavePath**.

## Script


**Voir aussi:**

[FreeCAD Script de base](FreeCAD_Scripting_Basics/fr.md).

Pour Enregistrer une copie du document, utilisez la méthode `saveCopy` de l\'objet document.


```python
import FreeCAD
from pathlib import Path

# The folder and filename we will use:
fld = 'D:/testfiles/'
fnm = fld + 'testCopy.FCStd'

# Make sure fld exists:
Path(fld).mkdir(parents=True, exist_ok=True)

doc = FreeCAD.newDocument()
doc.saveCopy(fnm)
```





{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std SaveCopy/fr
