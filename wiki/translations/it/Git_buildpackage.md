# Git buildpackage/it
I moderni flussi di lavoro di sviluppo Debian coinvolgono [creare pacchetti con Git](https://wiki.debian.org/PackagingWithGit) e lo strumento principale per farlo è [gbp.html git-buildpackage](http://honk.sigxcpu.org/projects/git-buildpackage/manual-html/). git-buildpackage fornisce un comando gbp con diverse opzioni simili al comando git stesso. Molti di questi comandi sono essi stessi solo un wrapper di strumenti Debian di livello inferiore, quindi la complessità nell\'apprendimento della pacchettizzazione può essere piuttosto elevata.

Per aggirare questo problema, ecco i passaggi brevi e semplici per iniziare con git-buildpackage. Dovrebbe funzionare su quasi tutte le distribuzioni basate su Debian, ma consiglio di lavorarci in un ambiente pulito e separato, una macchina virtuale [Debian Unstable](Debian_Unstable/it.md).

1.  Installarlo con sudo apt install git-buildpackage
2.  Prendere i dotfile alla fine di questa pagina. Ci sarà bisogno di: ~/.gbp.conf, ~/.pbuilderrc, and ~/.quiltrc
3.  La compilazione del pacchetto avverrà in un ambiente pulito. Crearlo con sudo git-pbuilder create
4.  Trovare l\'URL di un pacchetto che vuoi creare su <https://salsa.debian.org>, l\'istanza GitLab self-hosted del progetto Debian
5.  Crearne un clone con 
6.  Accedere alla cartella del repository clonato con cd
7.  Eseguire la build con gbp buildpackage -us -uc
8.  Al termine, i pacchetti saranno disponibili in ../build-area/.

##### gbp.conf

Location: ~/.gbp.conf

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.gbp.conf>

##### pbuilderrc

Location: ~/.pbuilderrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.pbuilderrc>

##### quiltrc

Location: ~/.quiltrc

<https://gitlab.com/kkremitzki/dotfiles/blob/master/.quiltrc>



---
⏵ [documentation index](../README.md) > [Packaging](Category_Packaging.md) > [Developer Documentation](Category_Developer%20Documentation.md) > Git buildpackage/it
