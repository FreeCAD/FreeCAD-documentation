---
- GuiCommand:
   Name:Arch Profile
   Name/it:Profilo
   Workbenches:[Arch](Arch_Workbench/it.md)
   MenuLocation:Arch - Profilo
   Version:0.19
---

# Arch Profile/it


</div>

## Descrizione

Lo strumento **Profilo** crea un oggetto profilo 2D parametrico. Questo oggetto può quindi essere utilizzato come base in diversi altri strumenti che eseguono estrusioni, come [Carpenteria](Arch_Frame/it.md), [Facciata continua](Arch_CurtainWall/it.md) o [Estrusione di Part](Part_Extrude/it.md).

Vedere [l\'elenco dei preset disponibili](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/profiles.csv).

Lo strumento profilo è anche integrato nello strumento [Struttura](Arch_Structure/it.md), tutti i profili preimpostati sono disponibili anche lì.

## Utilizzo

1.  Premere il pulsante **<img src="images/Arch_Profile.svg" width=16px> [Profilo](Arch_Profile/it.md)**.
2.  Selezionare un profilo preimpostato nel pannello delle azioni dello strumento.
3.  Fare clic su un punto nella vista 3D per posizionare il profilo.

## Proprietà

### Dati

-    **Height**: L\'altezza complessiva del profilo

-    **Width**: La larghezza complessiva del profilo

-    **Diameter**: Il diametro del profilo (solo per i profili circolari)

-    **Thickness**: Lo spessore della parete del tubo (solo per i profili cavi circolari e rettangolari)

-    **Web Thickness**: Lo spessore dell\'anima del profilo (solo per i profili H e I)

-    **Flange Thickness**: Lo spessore della flangia o ala del profilo (solo per i profili H e I)

## Aggiungere dei profili personalizzati 

L\'utente può creare un file CSV aggiuntivo, contenente le definizioni del profilo personalizzato. Deve essere denominato `profiles.csv` e inserito in {{Code|lang=bash|code=
$FREECAD_USER_DIR/Arch/
}}

Il percorso `$FREECAD_USER_DIR` può essere ottenuto dalla [console Python](Python_console/it.md): {{Code|lang=bash|code=
FreeCAD.getUserAppDataDir()
}}

Il contenuto del file `profiles.csv` personalizzato deve essere modellato con le stesse regole del [profiles.csv](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/Presets/profiles.csv) nel codice sorgente.

Il file CSV deve contenere una riga per ogni profilo disponibile, formattata come segue:


<div class="mw-translate-fuzzy">

-   Per profili a C: Category, Name, Class, Diameter, Thickness
-   Per i profili H e U: Category, Name, Class, Width, Height, Web thickness, Flange thickness
-   Per profili R: Category, Name, Class, Width, Height
-   Per profili RH: Category, Name, Class, Width, Height, Thickness


</div>

Tutte le misure devono essere in millimetri. Le possibili classi di profilo sono:


<div class="mw-translate-fuzzy">

-   C: Tubo circolare
-   H: Profilo H o I
-   R: Rettangolare
-   RH: Rettangolare pieno
-   U: Profilo a U


</div>

È possibile creare tipi di profilo aggiuntivi, ma è necessario prima definire una classe corrispondente in [ArchProfile.py](https://github.com/FreeCAD/FreeCAD/blob/master/src/Mod/Arch/ArchProfile.py).

## Script

Lo strumento Profilo può essere utilizzato nelle [macro](macros/it.md) e dalla console [Python](Python/it.md) tramite la seguente funzione:


```python
profile = makeProfile(profile_list)
```

Dove profile_list contiene i diversi elementi di un elenco nel file CSV.

Esempio:


```python
import Arch
Arch.makeProfile([0, 'REC', 'REC100x100', 'R', 100, 100])
```

Dove il primo elemento della lista è un numero d\'ordine non ancora utilizzato.



---
![](images/Button_right.svg) [documentation index](../README.md) > [Arch](Arch_Workbench.md) > Arch Profile/it
