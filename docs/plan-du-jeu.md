# Plan du jeu et logique de progression

## Vue d'ensemble

Le monde de Terminus est un faux systeme de fichiers. Chaque salle correspond a un dossier, chaque personnage ou objet a un element sur lequel on peut lancer une commande.

La progression suit trois grands blocs :

1. apprentissage de base et sortie du debut de jeu
2. grand hub `PlaceDuVillage` avec plusieurs quetes paralleles
3. zone finale des trolls puis des fichiers noyau

## Ordre conseille

L'ordre le plus propre, confirme par les PDF d'aide et le code source, est le suivant :

1. `BoisDesLutins`
2. `AcadémieDesBots`
3. `Prairie`
4. `Montagnes`
5. `Cave -> Tunnel -> Portail`
6. `PlaceDuVillage`
7. `PlaceDuMarché`
8. `BoutiqueArtisanale`
9. `Bibliothèque`
10. `CheminEnPierres`
11. `PontCassé`
12. `CheminInquiétant`
13. `CaveDesTrolls`
14. `Toboggan`
15. `FichiersNoyau`
16. `PlusDeFichiersNoyau`
17. `Paradis`

## Commandes apprises et source de l'apprentissage

| Commande | Comment on l'obtient | Role dans la suite |
|---|---|---|
| `cd` | disponible des le debut, expliquee par `Palourde` | se deplacer |
| `ls` | disponible des le debut, expliquee par `Palourde` | voir les chemins et objets |
| `cat` | disponible des le debut | lire les objets et parler aux personnages |
| `pwd` | lire `RentreChezToi` dans `BoisDesLutins` | savoir ou on se trouve |
| `mv` | lire `Professeur` dans `Cours` | deplacer objets et debloquer plusieurs passages |
| `exit` | lire `VieilHomme` dans `Montagnes` | commande secondaire, peu utile pour finir |
| `help` et `man` | lire `Manuscrit` | aide et rappel de syntaxe |
| `unzip` | lire `SacÀDos` dans `PlaceDuMarché` | sortir les "couts" du sac |
| `mkdir` | acheter au `Vendeur` | creer `Maison` |
| `rm` | acheter au `Vendeur` | enlever rocher, ronces, troll |
| `touch` | lire `Artisane` | creer `Planche` et `rouage` |
| `cp` | cree en faisant `touch rouage` | dupliquer `rouage` et `EpisDeMais` |
| `grep` | lire `Grep` dans `PièceSecrète` | trouver le mot de passe |
| `sudo` | lire `Prospectus` dans `FichiersNoyau` | lire `Certificat` |

## Enigmes principales

### 1. Academie

But : apprendre `mv` et vider la salle d'entrainement.

Commande efficace :

```bash
mv Pilier* ~/
```

Effet : les trois piliers quittent la salle, ce qui clot la zone academie.

### 2. Debloquer la montagne

But : ouvrir l'acces aux `Montagnes`.

Commande :

```bash
cat Poney
```

Effet : `Montagnes` apparait depuis `Prairie`.

### 3. Ouvrir le tunnel

But : enlever le gros rocher du `Cellier`.

Commande :

```bash
mv Rocher PetitRenfoncement
```

Effet : le `Tunnel` devient accessible.

### 4. Marche

But : obtenir `unzip`, `mkdir` et `rm`.

Commandes :

```bash
cat SacÀDos
unzip SacÀDos.zip
cat Vendeur
cat Vendeur
```

Remarque : il faut bien acheter les deux sorts, sinon on se bloque plus tard.

### 5. Boutique artisanale

But : apprendre `touch` puis `cp`.

Commandes :

```bash
cat Artisane
touch rouage
cp rouage rouage1
cp rouage rouage2
cp rouage rouage3
cp rouage rouage4
cp rouage rouage5
```

### 6. Bibliotheque

But : trouver `grep`.

Commandes :

```bash
./IntrigantLevier
cd PièceSecrète
cat Grep
```

### 7. Pont casse

But : reconstruire le pont puis construire une maison.

Commandes :

```bash
touch Planche
cd Clairière
mkdir Maison
```

### 8. Cave des trolls

But : ouvrir le toboggan et liberer l'enfant.

Commandes qui marchent :

```bash
rm TrollMoche
mv Cage/EnfantKidnapé .
```

### 9. Fichiers noyau

But : obtenir `sudo`, trouver le mot de passe et lire `Certificat`.

Commandes :

```bash
cat Prospectus
cat Instructions
cd PlusDeFichiersNoyau
grep pass *.txt
sudo cat Certificat
```

Mot de passe :

```text
IHTFP
```

### 10. Fin du jeu

Commandes finales :

```bash
cd Paradis
ls
```
