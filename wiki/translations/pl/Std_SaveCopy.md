---
 GuiCommand:
   Name: Std SaveCopy
   Name/pl: Std: Zapisz jako kopię
   MenuLocation: Plik , Zapisz jako kopię ...
   Workbenches: wszystkie
   SeeAlso: Std_SaveAs/pl, Std_Save/pl
---

# Std SaveCopy/pl



## Opis

Polecenie **Zapisz jako kopię** zapisuje kopię aktywnego dokument w pliku pod nową nazwą.



## Użycie

1.  Wybierz z menu opcję **Plik → <img src="images/Std_SaveCopy.svg" width=16px> Zapisz jako kopię ...**.
2.  Wprowadź nazwę pliku w oknie dialogowym.
3.  Naciśnij przycisk **Zapisz**.



## Opcje

-   Naciśnij przycisk **Esc** lub przycisk **Anuluj** aby przerwać wykonywanie polecenia.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Aby zapisać kopię dokumentu, należy użyć metody `saveCopy` obiektu *document*.


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



---
⏵ [documentation index](../README.md) > Std SaveCopy/pl
