# ViewObject API/pl
 **''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

Kiedy GUI jest uruchomione, każdy obiekt w dokumencie FreeCAD ma powiązany obiekt widoku, który rezyduje w odpowiedniku dokumentu FreeCADGui. Obiekt widoku może zostać pobrany na dwa sposoby. Przykład: 
```python
myViewObj = FreeCAD.ActiveDocument.myObjectName.ViewObject
myViewObj = FreeCADGui.ActiveDocument.myObjectName
print myViewObj.IV
```


{{APIProperty|Annotation|węzeł anotacji obiektu ViewObject.}}


{{APIProperty|BoundingBox|ramka otaczająca.}}


{{APIProperty|Content|reprezentacja XML właściwości obiektu ViewObject.}}


{{APIProperty|DisplayMode|aktualny tryb wyświetlania.}}


{{APIProperty|IV|reprezentacja obiektu ViewObject w programie Inventor.}}


{{APIProperty|Object|powiązany obiekt dokumentu FreeCAD obiektu ViewObject.}}


{{APIProperty|PropertiesList|lista własciwości obiektu ViewObject.}}


{{APIProperty|RootNode|węzeł Inventor obiektu ViewObject ''(obiekt pivy.coin)''.}}


{{APIProperty|Selectable|zwraca wartość {{True}} jeśli obiekt jest dostępny do wyboru.}}


{{APIProperty|Type|typ obiektu ViewObject.}}


{{APIProperty|Visibility|wraca wartość {{True}} jesli obiekt viewObject jest widzialny.}}


{{APIFunction|getAllDerivedFrom| | |wszystkie wystąpienia tego obiektu.}}


{{APIFunction|getDocumentationOfProperty| | |łańcuch dokumentacji właściwości tej klasy.}}


{{APIFunction|getGroupOfProperty| | |nazwa grupy, do której należy dana właściwość w tej klasie. Właściwości posortowane w różnie nazwanych grupach dla wygody.}}


{{APIFunction|getPropertyByName| | |wartość określonej właściwości.}}


{{APIFunction|getTypeOfProperty| | |typ określonej właściwości. Może to być ''(Hidden, ReadOnly, Output)'' lub dowolna kombinacja.}}


{{APIFunction|hide| |Ukrywa obiekt.| }}


{{APIFunction|isDerivedFrom|string|Sprawdza czy ten obiekt jest pochodną podanego typu obiektu|Zwraca wartość {{True}} jeśli podany typ jest ojcem}}


{{APIFunction|isVisible| |Sprawdza, czy obiekt jest widzialny| boolean}}


{{APIFunction|listDisplayModes| |Wyświetla listę wszystkich trybów wyświetlania|lista}}


{{APIFunction|setTransformation|coin.SoTransform|Ustawia transformację na węźle Inventor.|}}


{{APIFunction|show| |Pokazuje obiekt, jeśli jest ukryty.|}}


{{APIFunction|toString| | |ciąg znaków reprezentujący węzeł Inventor.}}


{{APIFunction|update| |Aktualizuje reprezentację obiektu w widoku.| }}


 

[Category:API](Category:API.md) [Category:Poweruser Documentation](Category:Poweruser_Documentation.md)
