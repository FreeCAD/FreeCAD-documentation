---
 TutorialInfo:t
   Topic: Aggiungere equazioni FEM 
   Level:  
   Time:  
   Author: User:M42kus
   FCVersion: 
   Files: 
---

# Add FEM Equation Tutorial/it







## Introduzione

In questo tutorial aggiungeremo a FreeCAD l\'equazione di flusso e implementeremo il supporto per il risolutore elmer. Prima di leggere questo tutorial è necessario aver letto e compreso il tutorial [ Estendere il modulo FEM](Extend_FEM_Module/it.md).

L\'operazione può essere suddivisa in cinque parti:

-   **Nuovo tipo di equazione**. Questo passaggio deve essere eseguito solo se l\'equazione non esiste ancora in FreeCAD (al contrario di un\'equazione già presente in FreeCAD ma non supportata dal risolutore di destinazione).
-   **Nuovo oggetto equazione**. Aggiunta di un oggetto documento concreto che rappresenta l\'equazione specifica di Elmer.
-   **Estendere l\'oggetto risolutore**. Aggiungere il supporto per la nuova equazione all\'oggetto risolutore di Elmer.
-   **Estendere l\'oggetto scrittore**. Estensione dell\'esportazione dell\'analisi di Elmer per supportare il nuovo tipo di equazione.
-   **Strumento GUI per creare un\'equazione**. Accedere alla nuova funzione dell\'equazione tramite la GUI dell\'ambiente.



## Nuovo tipo di equazione 

In questo passaggio modificheremo il seguente file:

-    **src/Mod/Fem/femsolver/equationbase.py**
    

Il tipo di equazione è condiviso tra tutti gli oggetti dell\'equazione dei diversi solutori. Ogni tipo ha uno specificatore di stringa (ad esempio \"Heat\") e un comando dedicato che aggiunge l\'equazione al risolutore selezionato. Ciò consente una GUI più semplice in cui si ha un solo pulsante per l\'equazione del calore che viene utilizzata per tutti i solutori supportati.

Innanzitutto, aggiungere la nuova equazione al modulo {{Incode|equationbase.py}}. Ogni equazione richiede due classi. Un proxy di documento e un proxy di visualizzazione. Queste due classi verranno successivamente utilizzate come classi base per le classi di equazioni specifiche di Elmer. Basta copiarle ed incollarle da un tipo di equazione esistente e regolare il percorso dell\'icona all\'interno di {{Incode|getIcon(self)}} del proxy di visualizzazione.


```python
class FlowProxy(BaseProxy):
    pass

class FlowViewProxy(BaseViewProxy):
    def getIcon(self):
        return ":/icons/FEM_EquationFlow.svg"
```



## Nuovo oggetto equazione di Elmer 

In questo passaggio implementeremo l\'oggetto documento. Dobbiamo aggiungere un nuovo file {{Incode|flow.py}} in:

-    **src/Mod/Fem/femsolver/elmer/equations/flow.py**
    

e modificare i seguenti file:

-    **src/Mod/Fem/ObjectsFem.py**
    

-    **src/Mod/Fem/CMakeLists.txt**
    

Si inizi aggiungendo il nuovo file {{Incode|flow.py}}. Questo file può essere copiato da un\'equazione esistente.

### Keywords

-   Se la nuova equazione supporta solo parole chiave per sistemi **lineari** copiare il modulo {{Incode|femsolver/elmer/equations/elasticity.py}}.
-   Se la nuova equazione supporta parole chiave sia per i sistemi **lineari** che **non lineari**, copiare {{Incode|femsolver/elmer/equations/heat.py}}.

L\'equazione del flusso in Elmer è un\'equazione potenzialmente non lineare. Ciò significa che si baserà il lavoro su {{Incode|heat.py}}.



### Modifica dei file 

Dopo aver copiato {{Incode|heat.py}} in {{Incode|flow.py}}, modificare {{Incode|flow.py}} in queste posizioni:

-   l\'argomento del nome della funzione del modulo {{Incode|create}},
-   le classi base della classe {{Incode|Proxy}},
-   l\'attributo {{Incode|Type}} della classe {{Incode|Proxy}},
-   le classi {{Incode|ViewProxy}}.


```python
def create(doc, name="'''Flow'''"):
    return femutils.createObject(
        doc, name, Proxy, ViewProxy)

class Proxy(nonlinear.Proxy, equationbase.'''Flow'''Proxy):

    Type = "Fem::EquationElmer'''Flow'''"

    def __init__(self, obj):
        super(Proxy, self).__init__(obj)
        obj.Priority = 10

class ViewProxy(nonlinear.ViewProxy, equationbase.'''Flow'''ViewProxy):
    pass
```

Quindi è necessario modificare le proprietà aggiunte tramite la funzione {{Incode|obj.addProperty(..)}} con quelle richieste dall\'equazione.

Al momento della stesura di questo tutorial l\'equazione del flusso di Elmer non ha proprietà speciali. Vedere l\'equazione dell\'elasticità di Elmer per un esempio con le proprietà.

Infine bisogna registrare una definizione **makeEquationFlow** in {{Incode|src/Mod/Fem/ObjectsFem.py}} duplicando una voce disponibile.

FreeCAD utilizza **make** per costruire il programma. Quindi si deve registrare il nuovo file del modulo ({{Incode|flow.py}}) in {{Incode|src/Mod/Fem/CMakeLists.txt}} nel modo descritto in [Extend FEM Module](https://www.freecadweb.org/wiki/Extend_FEM_Module). Gli elenchi adatti possono essere facilmente trovati cercando i file dei moduli di equazioni esistenti di Elmer.



## Estendere l\'oggetto risolutore 

In questo passaggio modificheremo il seguente file:

-    **src/Mod/Fem/femsolver/elmer/solver.py**
    

In questo momento è stato informato FreeCAD dell\'esistenza di un nuovo tipo di equazione e si è anche aggiunto un comando che aggiunge questa equazione all\'oggetto del risolutore selezionato. Si è anche implementato un oggetto equazione concreta per Elmer. Ciò che resta da fare ora è stabilire la connessione tra Elmer e l\'equazione del flusso. Questo deve essere fatto direttamente nell\'oggetto risolutore Elmer.

Registrare il modulo in cui abbiamo appena implementato il nostro nuovo oggetto equazione ({{Incode|flow.py}}) con l\'identificatore dell\'equazione del passaggio 1 (\"Flow\") nell\'elenco {{Incode|_EQUATIONS}} in {{Incode| elmer/solver.py}}.


```python
from .equations import electrostatic
+from .equations import flow

...

_EQUATIONS = {
    "Heat": heat,
    "Elasticity": elasticity,
+    "Flow": flow,
}
```



## Estendere l\'oggetto writer 

In questo passaggio modificheremo il seguente file:

-    **src/Mod/Fem/femsolver/elmer/writer.py**
    

Questo file contiene la classe {{Incode|Writer}} che esporta l\'analisi nel formato Elmer SIF.

Per ogni equazione supportata, esistono due metodi principali che gestiscono l\'esportazione della rispettiva equazione. Basta copiarli tutti da un\'equazione esistente e adattarli alle tue esigenze.

-    {{Incode|_getFlowSolver}}
    

-    {{Incode|_handleFlow}}
    

Si deve registrare il metodo {{Incode|_handleFlow}} all\'interno della classe {{Incode|Writer}}:


```python
class Writer(object):
...
    def write(self):
...
        self._handleFlow()

...

```


{{Incode|_handleFlow}}

può controllare una serie di altri metodi dettagliati. L\'equazione di flusso utilizza i seguenti metodi dettagliati:

-    {{Incode|_handleFlowConstants}}
    

-    {{Incode|_handleFlowMaterial}}
    

-    {{Incode|_handleFlowInitialVelocity}}
    

-    {{Incode|_handleFlowBndConditions}}
    

-    {{Incode|_handleFlowEquation}}
    

Ora è terminata la parte funzione della nuova equazione. Successivamente, si collegherà la nuova equazione tramite la GUI.



## Strumento Gui per creare un\'equazione 

É appena stata creata una nuova classe di equazioni. Per accedervi dalla GUI FEM, si deve creare un pulsante e collegarlo alla nuova classe di equazioni. Si veda questo tutorial: [Aggiungere un pulsante alla barra strumenti di FEM](Add_Button_to_FEM_Toolbar_Tutorial/it.md).



---
⏵ [documentation index](../README.md) > [FEM](Category_FEM.md) > [Developer Documentation](Category_Developer Documentation.md) > Add FEM Equation Tutorial/it
