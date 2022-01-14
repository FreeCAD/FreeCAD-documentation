# Object API/pl
**''(Październik 2019)'' Nie edytuj tych stron. Informacje są niekompletne i nieaktualne. Najnowsze API można znaleźć w [https://www.freecadweb.org/api automatycznie generowana dokumentacja API], lub wygenerować dokumentację samodzielnie, śledząc dokument [Dokumentacja źródłowa](Source_documentation/pl.md).**

Jako parametryczne, obiekty dokumentów FreeCAD mogą mieć wiele dodatkowych właściwości, ale te są podstawowe, obecne w każdym obiekcie dokumentu FreeCAD. Obiekty mogą być wyszukiwane po prostu przez ich nazwę. Przykład: 
```python
myObj = FreeCAD.ActiveDocument.myObjectName
print myObj.PropertiesList
```


{{APIProperty|Content|Reprezentacja XML właściwości obiektu.}}


{{APIProperty|Label|Pobiera/ustawia etykietę obiektu. Łańcuch może być typu unicode.}}


{{APIProperty|Name|Niepowtarzalna nazwa obiektu.}}


{{APIProperty|Placement|Pobiera/ustawia umiejscowienie obiektu. Umiejscowienie określa orientację (obrót) i pozycję ( położenie) w przestrzeni 3D. Funkcja ta jest używana, gdy nie jest wymagane skalowanie lub inne zniekształcenie.}}


{{APIProperty|PropertiesList|Lista właściwości obiektu}}


{{APIProperty|State|Status obiektu w programie FreeCAD ''(np. czy musi być ponownie obliczony)''}}


{{APIProperty|Type|Ciąg znaków opisujący typ obiektu}}


{{APIProperty|ViewObject|Powiązany dostawca widoku obiektu ''(obiekt FreeCADGUI)''}}


{{APIFunction|getAllDerivedFrom| | |Wszyscy potomkowie tego obiektu}}


{{APIFunction|getDocumentationOfProperty| | |Ciąg dokumentacji właściwości tej klasy.}}


{{APIFunction|getGroupOfProperty| | |Nazwa grupy, do której należy właściwość w tej klasie. Właściwości są posortowane w różnych grupach dla wygody.}}


{{APIFunction|getPropertyByName| | |Wartość nazwanej właściwości.}}


{{APIFunction|getTypeOfProperty| | |Typ nazwanej właściwości. Może to być ''(Hidden, ReadOnly, Output)'' lub dowolna kombinacja.}}


{{APIFunction|isDerivedFrom| | |Prawda jeśli podany typ jest ojcem}}


{{APIFunction|purgeTouched| |Zaznacza obiekt jako niezmieniony| }}


{{APIFunction|touch| |Zaznacza obiekt jako zmieniony ''(dotknięty)''| }}


 

[<img src="images/Property.png" style="width:16px"> API](Category_API.md) [<img src="images/Property.png" style="width:16px"> Poweruser Documentation](Category_Poweruser_Documentation.md)

---
[documentation index](../README.md) > [API](Category_API.md) > Object API/pl
