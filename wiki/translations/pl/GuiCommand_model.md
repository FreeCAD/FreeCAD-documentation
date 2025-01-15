---
 GuiCommand:
   Name: Base ExampleCommandModel
   Name/pl: Szablon polecenia GUI
   Icon:  
   MenuLocation: Menu , menu podrzędne , Tekst menu dla polecenia
   Workbenches: Workbench_Name
   Shortcut: **F** **C**
   Version: 0.19
   SeeAlso:  
---

# GuiCommand model/pl



## Opis

Gdy strona jest w budowie, dodaj szablon [Template:UnfinishedDocu](Template_UnfinishedDocu.md) na górze strony, wpisując po prostu: ****.

W pierwszym akapicie należy podać krótki opis działania polecenia. Opis może odnosić się do innych stołów roboczych, takich jak <img alt="" src=images/Workbench_Sketcher.svg  style="width:24px;">. [Szkicownik](Sketcher_Workbench/pl.md). 
*(*Uwaga edytora:*Obraz ma 24px, a nie 16px)*

Pamiętaj, aby używać [Template:Version](Template_Version.md), [Template:VersionMinus](Template_VersionMinus.md), [Template:VersionPlus](Template_VersionPlus.md) i [Template:Obsolete](Template_Obsolete.md) w stosownych przypadkach.

Na przykład: Funkcja `App::Link` (<small>(v0.19)</small> ) umożliwia łączenie między złożeniami podrzędnymi itp\...

Dodaj obrazek, jeśli to możliwe, i postępuj zgodnie z wytycznymi w [WikiPages](WikiPages#Grafika.md). Przykład zaczerpnięty z [Wyciągnięcia po ścieżce](Part_Sweep/pl.md): ![](images/Part_Sweep_simple.png ) 
*Opcjonalnie: dodaj podpis pod obrazem, aby wyjaśnić działanie narzędzia.*

Zamykające i otwierające znaczniki tłumaczenia powinny otaczać obrazy i inne stałe elementy, jeśli nie muszą być tłumaczone. Podpis powinien być zawsze przetłumaczony.



## Użycie

1.  Istnieje kilka sposobów wywołania polecenia:
    -   Naciśnij przycisk **<img src="images/Std_Open.svg" width=16px> [Base ExampleCommandModel](GuiCommand_model/pl.md)
**. *(*Uwaga edytora:*Wykorzystuje to szablon [Template:Button](Template_Button.md), konieczne jest powiązanie z poleceniem, jak pokazano w tym przykładzie)*
    -   Wybierz opcję z menu **Menu → menu podrzędne → <img src="images/Std_Open.svg" width=16px> Tekst menu dla opcji polecenia
**. *(*Uwaga edytora:*To używa szablonu [Template:MenuCommand](Template_MenuCommand.md))*
    -   Wybierz opcję **Submenu → <img src="images/Std_Open.svg" width=16px> Tekst menu dla polecenia
** z menu kontekstowego [Widoku drzewa](Tree_view/pl.md) lub [Widoku 3D](3D_view/pl.md). *(*Uwaga edytora:*Używa to również szablonu [Template:MenuCommand](Template_MenuCommand.md), nie wszystkie polecenia mogą być dostępne z menu kontekstowego)*
    -   Użyj skrótu klawiaturowego **F**, a następnie **C** lub **Ctrl** + **Z**. *(*Uwaga edytora:*Wykorzystuje to szablon [Template:KEY](Template_KEY.md), nie wszystkie polecenia mają skrót klawiaturowy)*
2.  Szczegółowe kroki według potrzeb. Niektóre kroki mogą wymagać naciśnięcia **Keyboard**, podczas gdy inne mogą wymagać kliknięcia myszą na **Przycisk**.
3.  Ustaw opcje i naciśnij **OK**.



## Opcje

-   Opcjonalnie. Wymień tutaj opcje polecenia. Zobacz na przykład [Polilinia](Draft_Wire/pl.md).



## Przykład

Opcjonalnie.



## Uwagi

-   Opcjonalnie. Użyj listy punktów, jeśli jest wiele elementów. Można tu również wspomnieć o ograniczeniach.



## Właściwości

Zapoznaj się również z informacjami na stronie: [Edytor właściwości](Property_editor/pl.md).

Obiekt jest zwykle pochodną obiektu bazowego. Nie należy wymieniać właściwości, które są dziedziczone z tego obiektu bazowego. Zobacz na przykład [Polilinia](Draft_Wire/pl#Właściwości.md).



### Dane


{{TitleProperty|Grupa właściwości}}

-    **Property Name 1|PropertyType**: Opis właściwości. *(*Uwaga edytora:*aby znaleźć {{Value|PropertyType}} wybierz **Wyświetl wszystko** w menu kontekstowym [Edytora własciwości](Property_editor/pl.md). Podpowiedź każdej właściwości będzie zawierać te informacje. Ale {{Value|PropertyType}} można również znaleźć w kodzie źródłowym)*.



### Widok


{{TitleProperty|Grupa właściwości}}

-    **Property Name 2|PropertyType**: Opis właściwości.



## Tworzenie skryptów 

Zobacz również stronę: [Dokumentacja API generowana automatycznie](https://freecad.github.io/SourceDoc/) oraz [Podstawy pisania skryptów dla FreeCAD](FreeCAD_Scripting_Basics/pl.md).

Narzędzie **Przykład polecenia GUI** może być używane w [makrodefinicjach](Macros/pl.md) i z konsoli [Python](Python/pl.md) za pomocą następujących funkcji:


```python
Object = makeExampleCommandModel(Data1, Data2)
```

-   Tworzy `Object` używając `Data1` i `Data2`.

Przykład:


```python
import FreeCAD, Base

Model = Base.makeExampleCommandModel(FreeCAD.Data1, FreeCAD.Data2)
```



## Pozostałe

Opcjonalnie.



## Blok do zaznaczenia 


<languages/>

<translate>



{{GuiCommand
|Name=Base ExampleCommandModel
|Icon= 
|MenuLocation=Menu → Submenu → Menu text for the command
|Workbenches=[Workbench](Workbench_Name.md)
|Shortcut=**F** **C**
|Version=0.19
|SeeAlso= 
}}

== Description ==

While the page is under construction, add the [[Template:UnfinishedDocu]] template at the top of the page by simply typing: ''''''

In this first paragraph give a short description of what the command does. The description can refer to other workbenches such as the <img src="images/Workbench_Sketcher.svg" width=24px> [Sketcher Workbench](Sketcher_Workbench.md). (''Editor note:'' The image is 24px, not 16px)

Remember to use [[Template:Version]], [[Template:VersionMinus]], [[Template:VersionPlus]] and [[Template:Obsolete]] when applicable.

For example: The `App::Link` feature (<small>(v0.19)</small> ) allows linking between sub-assemblies etc...

Add an image if possible, and please follow the guidelines in [WikiPages](WikiPages#Graphics.md). Example taken from [Part Sweep](Part_Sweep.md):
</translate>
![](images/)
<translate>

*Optional: add a caption below the image to explain what the tool does*

Closing and opening translate tags should surround images, and other fixed elements, if they don't need to be translated. The caption should always be translated.

== Usage ==

# There are several ways to invoke the command:
#* Press the **<img src="images/Std_Open.svg" width=16px> [Base ExampleCommandModel](GuiCommand_model.md)** button. (''Editor note:'' This uses the [[Template:Button]] template, it is necessary to link to the command as shown in this example)
#* Select the **Menu → Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the menu. (''Editor note:'' This uses the [[Template:MenuCommand]] template)
#* Select the **Submenu → <img src="images/Std_Open.svg" width=16px> Menu text for the command** option from the [Tree view](Tree_view.md) context menu or [3D view](3D_view.md) context menu. (''Editor note:'' This also uses the [[Template:MenuCommand]] template, not all commands can be accessed from a context menu)
#* Use the keyboard shortcut **F** then **C** or **Ctrl**+**Z**. (''Editor note:'' This uses the [[Template:KEY]] template, not all commands have a keyboard shortcut)
# Detailed steps as needed. Some steps may need **Keyboard** presses while others may require using the mouse to click on a **Button**.
# Set options and press **OK**.

== Options ==

* Optional. List the command options here. See for example [Draft Wire](Draft_Wire.md).

== Example ==

Optional.

== Notes ==

* Optional. Use a bullet list if there are multiple items. You can also mention limitations here.

== Properties ==

See also: [Property editor](Property_editor.md).

An object is usually derived from a base object. You should not list the properties that are inherited from that base object. See for example [Draft Wire](Draft_Wire#Properties.md).

=== Data ===

{{TitleProperty|Property Group}}

* **Property Name 1|PropertyType**: Description of the property. (''Editor note:'' to find the {{Value|PropertyType}} select **Show all** in the context menu of the [Property editor](Property_editor.md). The tooltip of each property will then include this information. But the {{Value|PropertyType}} can also be found in the source code.)

=== View ===

{{TitleProperty|Property Group}}

* **Property Name 2|PropertyType**: Description of the property.

== Scripting ==

See also: [https://freecad.github.io/SourceDoc/ Autogenerated API documentation] and [FreeCAD Scripting Basics](FreeCAD_Scripting_Basics.md).

The ExampleCommandModel tool can be used in [macros](Macros.md) and from the [Python](Python.md) console by using the following function:

</translate>
```python
Object = makeExampleCommandModel(Data1, Data2)
```
<translate>

* Creates an `Object` using `Data1` and `Data2`.

Example:

</translate>
```python
import FreeCAD, Base

Model = Base.makeExampleCommandModel(FreeCAD.Data1, FreeCAD.Data2)
```
<translate>

== Other ==

Optional.




</translate>
{{Workbench_Tools_navi}} 






{{Workbench_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Workbench_Tools_navi{{#translation:}}}} <!--use the](Category_Workbench_Tools_navi{{#translation:}}}}%20<!--use%20the.md) > GuiCommand model/pl
