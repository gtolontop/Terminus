# Rendu court - solution de l'activite Terminus

## 1. But du jeu

Le jeu Terminus sert a apprendre des commandes de terminal UNIX en resolvant des enigmes dans un monde represente comme un systeme de fichiers.

Les commandes importantes apprises au fil du jeu sont :

- depart : `cd`, `ls`, `cat`
- BoisDesLutins : `pwd`
- Cours : `mv`
- Montagnes : `exit`
- Manuscrit : `help`, `man`
- PlaceDuMarche : `unzip`, puis achat de `mkdir` et `rm`
- BoutiqueArtisanale : `touch`, puis `cp`
- PieceSecrete : `grep`
- FichiersNoyau : `sudo`

## 2. Solution resumee

1. Depuis `Départ`, aller dans `BoisDesLutins`, lire `RentreChezToi` pour apprendre `pwd`, puis aller a `AcadémieDesBots/Cours` et lire `Professeur` pour apprendre `mv`.
2. Aller a `SalleDEntrainement` et deplacer les trois piliers hors de la salle, par exemple avec `mv Pilier* ~/`.
3. Revenir a `Prairie`, lire `Poney` pour debloquer `Montagnes`.
4. Aller a `Montagnes`, lire `VieilHomme`, puis lire `Manuscrit`.
5. Aller a `Cave/SombreCorridor/Cellier`, faire `mv Rocher PetitRenfoncement`, puis entrer dans `Tunnel`, `ChambreDePierre`, `Portail`, puis `PlaceDuVillage`.
6. A `PlaceDuMarché` :
   - `cat SacÀDos`
   - `unzip SacÀDos.zip`
   - parler deux fois au `Vendeur` pour acheter `mkdir` et `rm`
7. A `BoutiqueArtisanale` :
   - `cat Artisane`
   - `touch rouage`
   - `cp rouage rouage1`
   - `cp rouage rouage2`
   - `cp rouage rouage3`
   - `cp rouage rouage4`
   - `cp rouage rouage5`
8. A `Bibliothèque` :
   - `./IntrigantLevier`
   - `cd PièceSecrète`
   - `cat Grep`
9. A `CheminEnPierres` : `rm ÉnormeRocher`
10. A `PontCassé` :
   - `touch Planche`
   - `cd Clairière`
   - `mkdir Maison`
11. A `CheminInquiétant` : `rm RoncesTordues`
12. A `CaveDesTrolls` :
   - `rm TrollMoche`
   - depuis la salle, liberer l'enfant avec un deplacement du type `mv Cage/EnfantKidnapé .`
13. Aller a `Toboggan`, puis `FichiersNoyau` :
   - `cat Prospectus`
   - `cat Instructions`
   - `cd PlusDeFichiersNoyau`
   - `grep pass *.txt`
   - on obtient le mot de passe `IHTFP`
   - revenir et faire `sudo cat Certificat`
14. Entrer le mot de passe `IHTFP`, puis aller a `Paradis` et faire `ls`.

## 3. File tree simplifie

Voir le fichier [docs/file-tree.txt](/Users/teamr/Desktop/terminus/docs/file-tree.txt).

## 4. Conclusion

La solution complete consiste donc a apprendre les commandes dans l'ordre, a ouvrir les passages caches, puis a utiliser `grep` et `sudo` pour atteindre `Paradis` et terminer le jeu.
