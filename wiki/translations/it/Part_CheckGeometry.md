---
 GuiCommand:
   Name: Part CheckGeometry
   Name/it: Part Controlla geometria‏‎
   MenuLocation: Parte , Controlla la geometria
   Workbenches: Part Workbench/it
---

# Part CheckGeometry/it



## Descrizione

Lo strumento **<img src="images/Part_CheckGeometry.svg" width=16px> [Controlla la geometria](Part_CheckGeometry/it.md)** esegue una verifica e segnala se la geometria è un solido valido. Lo strumento controlla se la [Rappresentazione della delimitazione](https://en.wikipedia.org/wiki/Boundary_representation) (BRep o [B-rep](Glossary/it#B.md)) del modello è valida.



## Utilizzo

1.  Selezionare una parte (attenzione a selezionare l\'intera parte e non solo una faccia per verificare la validità del solido)
2.  Richiamare lo strumento in uno dei seguenti modi:
    -   Facendo clic sul pulsante **<img src="images/Part_CheckGeometry.svg" width=16px> [Controlla la geometria](Part_CheckGeometry/it.md)** disponibile nella barra degli strumenti dell\'ambiente Part.
    -   Utilizzando la voce **Parte → <img src="images/Part_CheckGeometry.svg" width=16px> Controlla la geometria** dal menu in alto.
3.  Si apre il pannello delle attività **Impostazioni**, a meno che non sia abilitato **Salta pagina impostazioni**. Vedi [Opzioni](#Opzioni.md) per ulteriori informazioni. Fai clic su **Esegui controllo**.

I risultati verranno riportati nel [Pannello delle azioni](Task_panel/it.md). Se il controllo ha prodotto errori: fare clic nel report su uno specifico messaggio di errore e l\'oggetto geometrico corrispondente (bordo, faccia, ecc.) verrà evidenziato nella [Vista 3D](3D_view/it.md).



## Opzioni



### Salta la pagina delle impostazioni 

Se selezionato, le successive invocazioni dello strumento salteranno la visualizzazione del pannello delle attività **Impostazioni**.



### Esegui controllo BOP 

Se selezionato, viene eseguito inoltre un controllo delle operazioni booleane (BOP).



### Registro degli errori 

Se selezionato, eventuali errori rilevati verranno registrati anche nella [finestra dei report](Report_view/it.md)



## Contenuto della forma 

Oltre a rilevare potenziali errori geometrici, questo strumento mostra una serie di proprietà relative all\'oggetto selezionato:

-   Oggetto controllato
-   Tipo di forma
-   Numero di entità geometriche: vertici, bordi, fili, facce, gusci, solidi, compsolidi, composti, forme totali
-   Proprietà geometriche e di massa:
    -   Area
    -   Volume
    -   Massa
    -   Lunghezza
    -   Centro di Massa
    -   Orientamento
    -   Asse di simmetria
    -   Punto di simmetria
    -   Momenti
    -   Primo asse d\'inerzia
    -   Secondo asse d\'inerzia
    -   Terzo asse d\'inerzia
    -   Raggio d\'inerzia
    -   Posizionamento globale



## Note

-   Utilizzando questo strumento è possibile controllare anche gli oggetti [App Link](App_Link/it.md) collegati ai tipi di oggetto appropriati e i contenitori [App Part](App_Part/it.md) con gli oggetti visibili appropriati all\'interno. Per [Link app](App_Link/it.md) viene controllata la forma dell\'oggetto collegato. Per i contenitori [App Part](App_Part/it.md) gli oggetti visibili all\'interno vengono controllati come composti. {{Version/it|0.20}}
-   FreeCAD non dispone di metodi per riparare automaticamente la geometria. Se vengono rilevati errori, i passaggi necessari per creare il modello devono essere esaminati e corretti manualmente.





{{Part_Tools_navi

}}



---
⏵ [documentation index](../README.md) > [Part](Part_Workbench.md) > Part CheckGeometry/it
