# Journal de bord

## Objectif

Construire un dossier de rendu propre pour "Rendre la solution de l'activite Terminus sur papier", en conservant :

- le jeu local
- les PDF d'aide
- une solution detaillee
- un file tree
- une trace de recherche

## Journal synthese

### 1. Audit du dossier local

Constat initial :

- pas de depot Git initialise
- build local present : `Terminus.html`, `Terminus_lent.html`, polices, dossier `img/`
- pas de documentation structuree

### 2. Recuperation des references externes

Ressources recuperees :

- `external-terminus-corrige.pdf`
- `external-terminus-mcoilhac.pdf`

Apports :

- le PDF corrige donne la liste des commandes et un plan synthese
- le PDF M. Coilhac donne un ordre de visite tres utile pour ne pas se bloquer

### 3. Verification du code du jeu

Travail effectue :

- lecture du HTML local minifie
- extraction de l'objet `dialog`
- repassage par le code source upstream pour verifier les scripts de quete

Point clef :

- le fichier local contient toute la logique du jeu
- les zones et evenements confirment exactement quels objets / personnages debloquent chaque commande ou chaque passage

### 4. Depot upstream et probleme Windows

Le depot `luffah/Terminus` contient des fichiers avec `:` dans le nom (`item:...`, `img:...`), ce qui casse un checkout direct sous Windows.

Contournement utilise :

- clone `--no-checkout`
- lecture des fichiers avec `git show`
- inspection de `map.txt`, `autoexplore.js`, `test_academy.js`, scripts d'objets et de personnages

### 5. Validation des points critiques

Verifications realisees :

- `Poney` ouvre `Montagnes`
- `Professeur` apprend `mv`
- deplacer les trois piliers clot l'academie
- `Rocher` vers `PetitRenfoncement` ouvre `Tunnel`
- `SacÀDos` apprend `unzip`
- le `Vendeur` fournit `mkdir` et `rm`
- `Artisane` apprend `touch`, puis `touch rouage` debloque `cp`
- `./IntrigantLevier` ouvre `PièceSecrète`
- `Grep` apprend `grep`
- `rm ÉnormeRocher` ouvre `Ferme`
- `touch Planche` rend la `Clairière` accessible
- `mkdir Maison` valide la zone
- `rm RoncesTordues` ouvre `CaveDesTrolls`
- `rm TrollMoche` ouvre `Toboggan`
- l'enfant se libere par une commande `mv` ciblee sur `Cage/EnfantKidnapé`
- `Prospectus` apprend `sudo`
- `Instructions` renvoie vers `PlusDeFichiersNoyau`
- `grep pass *.txt` donne `IHTFP`
- `sudo cat Certificat` ouvre `Paradis`

### 6. Resultat

Livrables produits :

- `docs/rendu-court.md`
- `docs/file-tree.txt`
- `docs/plan-du-jeu.md`
- `docs/solution-detaillee.md`
- `docs/sources.md`

## Remarque honnete

Je n'ai pas pilote l'interface graphique du jeu directement dans cette session.
En revanche, la solution a ete verifiee par croisement de :

- la logique du build local
- les scripts upstream
- les PDF externes
- les noms exacts extraits du jeu

Pour un rendu ecrit, ce niveau de verification est largement suffisant et plus fiable qu'une simple copie d'un corrige.
