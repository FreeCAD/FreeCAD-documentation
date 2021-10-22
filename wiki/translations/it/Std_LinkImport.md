---
- GuiCommand:/it
   Name:Std_LinkImport
   Name/it:Importa un link
   MenuLocation:Nessuna
   Workbenches:Tutti
   Version:0.19
   SeeAlso:[Crea un link](Std_LinkMake/it.md), [Crea un link relativo](Std_LinkMakeRelative/it.md), [Importa tutti i link](Std_LinkImportAll/it.md)
---

# Std LinkImport/it

## Descrizione

Lo strumento <img alt="" src=images/Std_LinkImport.svg  style="width:16px;"> [Importa link](Std_LinkImport/it.md) importa un **Linked Object** da un collegamento nel documento corrente, quindi modifica l\'associazione in questo oggetto.

Questa operazione è utile quando si lavora con gli [assemblaggi](assembly/it.md) al fine di organizzare i modelli riutilizzabili che possono trovarsi in altri documenti.

Usare **<img src=images/Std_LinkImportAll.svg style="width:16px"> Importa tutti i link** per importare tutti gli oggetti collegati.

## Utilizzo

1.  Assicurarsi di avere un documento \"sorgente\" con un oggetto originale, ad esempio, una <img alt="" src=images/Std_Part.svg  style="width:16px;"> [Parte](Std_Part/it.md) e un secondo documento \"destinazione\" con un collegamento a quell\'oggetto.
2.  Aprire il documento di destinazione e selezionare il collegamento all\'oggetto; la sua **Linked Object** dovrebbe mostrare qualcosa di simile a {{Value|source#Part}}.
3.  Premere **<img src=images/Std_LinkImport.svg style="width:16px"> [Importa link](Std_LinkImport/it.md)**.

Una copia della <img alt="" src=images/Std_Part.svg  style="width:16px;"> Parte originale deve ora essere all\'interno del documento \"destinazione\" corrente. La proprietà **Linked Object** del collegamento deve ora mostrare {{Value|Part}}, indicando che il collegamento non punta più a {{Value|Part}} nel \"sorgente\", ma a {{Value|Part}} nel documento corrente (\"destinazione\").

![](images/Std_Link_tree_import_1_example.png ) ![](images/Std_Link_tree_import_2_example.png )



*A sinistra: un collegamento punta all'oggetto nel documento "sorgente". A destra: l'oggetto originale è stato importato (copiato) nel documento "destinazione" e il collegamento esistente è stato modificato per puntare a questa copia, quindi non punta più all'oggetto del  "sorgente".*





{{Std Base navi

}}

---
[documentation index](../README.md) > Std LinkImport/it
