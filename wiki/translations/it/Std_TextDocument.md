---
- GuiCommand:/it
   Name:Std_TextDocument
   Name/it:Aggiungi un documento di testo
   MenuLocation:Strumenti → Aggiungi un documento di testo
   Workbenches:Tutti
   Version:0.19
   SeeAlso:[Forma da testo di Draft](Draft_ShapeString/it.md), [Testo di Draft](Draft_Text/it.md)
---

# Std TextDocument/it

## Descrizione

Il comando **Aggiungi un documento di testo** crea un oggetto in grado di contenere un testo arbitrario. Questo elemento può essere utilizzato per scrivere delle informazioni generali o della documentazione sul modello.

## Utilizzo

1.  Andare nel menu **Strumenti → Aggiungi un documento di testo**.
2.  Fare doppio clic sul nuovo oggetto creato nella [vista ad albero](tree_view/it.md) per aprire una scheda in cui scrivere il testo.
3.  Aggiungere il testo.
4.  Chiudere la scheda e salvare il file quando viene richiesto.

## Proprietà

### Vista


{{TitleProperty|Editor}}

-    **Font Name|Font**: un nome di carattere, ad esempio, {{Value|Ubuntu Mono}}.

-    **Font Size|Float**: una dimensione del carattere in punti, ad esempio, {{Value|11}}.

-    **Read Only|Bool**: il valore predefinito è `False`. Se impostato su `True` il testo non può essere modificato.

-    **Syntax Highlighter|Enumeration**: il valore predefinito è {{Value|None}}. Se impostato su {{Value|Python}}, il testo verrà evidenziato come nella [console Python](Python_console/it.md).

## Script


**Vedere anche:**

[Script di base per FreeCAD](FreeCAD_Scripting_Basics/it.md), e [script di oggetti](scripted_objects/it.md).

Vedere [Part Feature](Part_Feature/it.md) per le informazioni generali sull\'aggiunta di oggetti a un documento.

Un oggetto `App::TextDocument` viene creato con il metodo `addObject()` del documento. Una volta che esiste un TextDocument, le sue informazioni testuali vengono archiviate nel suo attributo `Text`. Questo attributo può essere utilizzato in altri oggetti, ad esempio, come stringa in una **<img src="images/Draft_ShapeString.svg" width=16px> [Forma da testo](Draft_ShapeString/it.md) di Draft** .


```python
import FreeCAD as App
import Draft

doc = App.newDocument()
obj = App.ActiveDocument.addObject("App::TextDocument", "Text_document")
obj.Text = "textual information"
App.ActiveDocument.recompute()

obj2 = Draft.makeShapeString(obj.Text, "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
App.ActiveDocument.recompute()
```


<div class="mw-translate-fuzzy">





</div>


{{Std Base navi

}}



---
![](images/Right_arrow.png) [documentation index](../README.md) > Std TextDocument/it
