# Debian Unstable/it
[Debian Unstable](https://wiki.debian.org/DebianUnstable) è una distribuzione \"rolling\" usata per lo [sviluppo di Debian](Debian_development/it.md) e raccomandata per utenti avanzati nello sviluppo e nella creazione di pacchetti di FreeCAD. I nuovi pacchetti sono pronti non appena vengono caricati e compilati, a meno che l\'autore del caricamento non li abbia contrassegnati per [Debian Experimental](https://wiki.debian.org/DebianExperimental) che richiede l\'installazione esplicita (dopo alcune impostazioni per abilitare la distribuzione extra) tramite .

Spesso, le persone che usano Debian Testing dovrebbero effettivamente usare Debian Unstable; Debian Testing dovrebbe essere considerato solo una \"QA release pocket\", poiché, sebbene possa sembrare più stabile di Unstable, in realtà c\'è uno svantaggio. I nuovi pacchetti vengono caricati su Debian Unstable e migrano su Testing dopo un po\' di tempo, quindi correzioni di sicurezza e importanti modifiche al pacchetto possono essere ritardate in modo inappropriato.

Ci sono due cose fondamentali per una buona esperienza utente in Unstable. La prima è non eseguire mai alla cieca sudo apt full-upgrade o i suoi equivalenti senza prima controllare i risultati dell\'operazione. Se sta dicendo che libererai centinaia di MB di spazio, è in corso una transizione del pacchetto che rimuoverà una buona parte del tuo sistema. Invece, si può tranquillamente eseguire sudo apt upgrade e ottenere nuovi pacchetti. A volte, ciò comporterà il blocco dei pacchetti, il che significa che potrebbe essere appropriato eseguire full-upgrade poiché la disinstallazione dei pacchetti potrebbe essere effettivamente necessaria.

La seconda è accettare che si sta prendendo parte allo sviluppo di Debian e utilizzare gli strumenti e i metodi appropriati. Ad esempio, ciò potrebbe significare installare pacchetti come apt-listbugs o apt-listchanges o iscriversi a mailing list Debian come [1](https://lists.debian.org/debian-devel-announce/debian-devel-announce@lists.debian.org).

Sebbene Debian Unstable sia perfettamente adatta per l\'uso quotidiano a lungo termine, è anche molto facile da eseguire in una macchina virtuale, dove le rotture non saranno un grosso problema. Basta scaricare una ISO di Debian Testing, installarla in una VM e aggiornarla, quindi modificare /etc/apt/sources.list in modo che contenga qualcosa come:

deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) testing main contrib non-free
deb [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
# deb-src [http://security.debian.org/debian-security](http://security.debian.org/debian-security) testing/updates main contrib non-free
deb [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free
# deb-src [http://ftp.us.debian.org/debian/](http://ftp.us.debian.org/debian/) unstable main contrib non-free

Se si vuole abilitare i pacchetti da Experimental, inserire questo in /etc/apt/sources.list.d/experimental.list:

deb [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free
# deb-src [http://deb.debian.org/debian](http://deb.debian.org/debian) experimental main contrib non-free



---
![](images/Right_arrow.png) [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer Documentation.md) > Debian Unstable/it
