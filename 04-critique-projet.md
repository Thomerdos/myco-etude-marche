# 04 — Critique du projet face au marché

*14 octobre 2026. Critique franche, calibrée sur l'objectif du porteur : **revenu d'appoint**,
**payant d'abord** (produit fini uniquement, sans prévente), **B2C accessible aux novices**,
périmètre **prospection seule** (aucune identification), développement intensif jusqu'au
printemps 2027 puis **moins de 15 h/semaine**, coûts en scénario minimal, micro-entreprise en
création, nom commercial retenu **« Le Bon Versant »** (« Myco Map » écarté) (décisions du
14/10/2026).*

Chaque point est classé :

- 🔴 **Bloquant** : interdit de faire payer tant que ce n'est pas réglé.
- 🟠 **Important** : freine fortement la conversion ou la rétention.
- 🟡 **Amélioration**.

Chaque point se termine par une **action** concrète.

---

## 1. Verdict en une phrase

Le Bon Versant (prototype `myco-map`) a **le meilleur moteur d'habitat de montagne observé sur
le marché français**, mais
c'est **un moteur sans voiture** : pas de produit déployable, pas de preuve que le score
prédit quoi que ce soit, des licences d'exploitation non commerciales, et une interface pensée
pour son auteur plutôt que pour un novice qui sort en forêt avec son téléphone.

## 2. Différenciateurs : réels, mais encore invisibles pour l'acheteur

| Atout | Réel ? | Perçu par l'acheteur ? |
|---|---|---|
| Relief 5 m (RGE ALTI) + canopée LIDAR HD (hauteur, trouées) à 50 m | **Oui** : aucun concurrent observé ne le revendique (doc 02 §7) | **Non, en l'état.** Les clients parlent de « nouveaux coins » et de « temps gagné » (doc 03 §4.1), pas de MNH. Mapignon affiche déjà « âges, densité de canopée » |
| Score explicable par critère | Oui (`InspectLocation`, `AGENTS.md`) | Potentiellement, si c'est formulé en clair (« versant nord frais, hêtraie dense, sol neutre ») |
| Projection à 14 jours par espèce, avec phénologie | Oui. Les concurrents annoncent J+5 à J+10 | Oui (fenêtre de tir), à condition d'être simple |
| Itinéraire parking → sentier → approche, GPX, KMZ | Oui. Un seul concurrent propose un itinéraire | Oui, surtout pour S3 (montagnards) |
| Méthode documentée et sourcée (en interne, puisque le code reste fermé, §9) | Oui | **Non directement.** Ce qui se montre, c'est l'explication par maille et une validation chiffrée (Boletik publie ×2,8) |

**Critique.** La différence technique est réelle mais **non traduite en bénéfice** et **non
prouvée**. Le contradicteur du conseil (Sharp, doc 05) le résumerait ainsi : l'acheteur ne
perçoit pas la différenciation, il perçoit ce qu'il retrouve facilement.
**Action** : formuler chaque atout comme un résultat (« le versant qui garde l'humidité 10 jours
après l'orage ») et publier une validation (§4).

## 3. Produit et déploiement

### 🔴 3.1 Rien n'est déployable

Le backend tourne avec `php -S` (serveur intégré, mono-processus), en `APP_ENV=dev` et
`APP_DEBUG=1`, avec un CORS limité à localhost. Il n'y a ni HTTPS, ni reverse proxy, ni
supervision, ni sauvegarde (doc 01 §3.4).
**Action** : une image de production (PHP-FPM ou FrankenPHP, Caddy pour TLS), `APP_ENV=prod`,
un seul petit serveur. Les données d'habitat sont précalculées et peuvent être servies comme
**fichiers statiques** (§3.3).

### 🔴 3.2 Ni comptes, ni paiement, ni contrôle d'accès

Un modèle « payant d'abord » suppose au minimum : identification, paiement, droits par zone,
résiliation.
**Action** : le plus simple à maintenir en solo, c'est **Stripe Checkout + Customer Portal**
(résiliation en un clic par le client) et une **clé d'accès par pass**, sans gestion de mot de
passe (lien magique par e-mail). C'est précisément ce qui manque à Chasseurs de champignons
d'après les avis Trustpilot.

### 🟠 3.3 Architecture de calcul inadaptée à un service public

- `GET /api/layer` renvoie jusqu'à **70 000 valeurs JSON** par requête (`DEFAULT_MAX_CELLS`) et
  recalcule le score pour chaque vue. C'est lourd en 4G en forêt et lourd pour un serveur
  mono-processus.
- **Cache météo indexé sur l'emprise exacte de la vue** (`OpenMeteoWeather::fieldFor`,
  `md5(serialize($bounds))` + heure) : chaque déplacement ou zoom distinct déclenche un nouveau
  téléchargement d'une grille 13×13 (169 points). Le nombre d'appels **croît avec les
  utilisateurs**, ce qui coûte cher dès qu'on paie au volume (§5.2).
- Ajouter une région, c'est éditer les bornes dans `services.yaml` **et** dans plusieurs
  scripts, puis lancer environ 13 Go de téléchargements et une chaîne LIDAR en 3 étapes
  manuelles. Avec moins de 15 h/semaine, cela limite à 1 ou 2 régions.

**Action** : séparer **habitat statique** (tuiles raster précalculées par espèce, servies par
CDN ou fichiers, cacheables à l'infini) et **facteur météo** (grille fixe par région,
recalculée **une fois par heure ou par jour** par une tâche planifiée, indépendante des
utilisateurs). Le navigateur compose les deux. Le coût serveur devient presque constant, quel
que soit le trafic.

### 🔴 3.4 Pas de mode hors-ligne

En montagne, le réseau est souvent absent. Champi et Expert de Cueillette vendent le
hors-ligne ; Komoot, Visorando, Cartes IGN et OsmAnd le proposent par région (doc 05 §10.3). Le
prototype n'a ni PWA ni paquets de zones. Le GPX et le KMZ ne compensent qu'en partie, via une
appli tierce.
**Action** : télécharger le **massif acheté** (tuiles d'habitat, dernière projection météo, fond
Protomaps auto-hébergé, §5.3). C'est la fonction qui justifie le pass (S1/S3). Le **support**
(PWA ou appli hybride) est discuté au §3.6.

### 🟠 3.5 Une seule région, figée

Le plus gros défaut commercial est une emprise unique sans mise à jour automatique. C'est
pourtant un bon choix de départ : l'Isère est 3ᵉ de France en observations des 5 espèces
(doc 03 §3).
**Action** : rester sur les **Alpes du Nord** (ajouter Savoie et Haute-Savoie) pour la première
saison payante. Industrialiser l'ajout de zone (un fichier de configuration par massif) avant
d'aller vers le Jura.

### 🟠 3.6 Application mobile : l'intuition du porteur est juste pour iOS, pas encore prouvée pour le lancement

Le porteur juge une vraie appli mobile « un vrai plus, voire indispensable », pour le hors-ligne
et parce que le public installe des applis depuis les stores, pas des PWA. Vérification
(détail et sources en doc 05 §10) :

- **Hors-ligne : fondé sur iOS.** Une PWA peut perdre ses données. Safari efface les données
  écrites par script après 7 jours d'usage sans interaction, et aucune exemption n'est
  documentée pour les applis de l'écran d'accueil. Le stockage persistant y est accordé « selon
  des heuristiques ». Une appli native range ses paquets dans un dossier que le système ne purge
  pas. Sur Android (~64 % du trafic mobile en France), Chrome donne jusqu'à 60 % du disque et le
  stockage persistant suffit.
- **Usages : plausible, non mesuré.** Aucun taux d'installation indépendant des PWA n'existe.
  Les applis de terrain sont natives, mais dans cette niche les acteurs web seulement
  (Chasseurs de champignons, Mycora, The Mycologist) ont l'audience la plus visible.
- **Hybride : Capacitor seulement.** C'est le seul des trois cadres cités qui reprend
  l'interface Vue telle quelle ; React Native et Flutter imposent de la réécrire.
- **Coût réel.** Sur iOS, un pass vendu dans l'appli passe par l'achat intégré (règle 3.1.1 ;
  la règle 3.1.3(b) exige de le proposer aussi en achat intégré). Avec la TVA collectée par le
  store et 15 % de commission, le net d'un pass à 19 € tombe de ≈ 14,40 € à ≈ 9,40–10,60 €. Il
  faut ajouter ~120 € de frais la première année, la publication de l'adresse du vendeur (DSA),
  la revue Apple et 3 à 5 semaines de travail.

**Action** : rendre le code hors-ligne **portable** dès la phase 1 (~1 jour), lancer en PWA avec
des atténuations iOS, mesurer pendant la saison des morilles, puis décider au 15/06/2027
(option A, doc 05 §10.7). **Le choix du calendrier revient au porteur** (doc 05 §8, point 4).

## 4. 🔴 Preuve : un score non validé ne se vend pas honnêtement

Les poids sont des « priors d'expert » (`AGENTS.md`). Le seul contrôle documenté est
qualitatif (distribution des scores en Chartreuse). Aucune mesure ne dit si les mailles à 90
concentrent plus de champignons que les autres. Boletik publie déjà une concentration ×2,8 sur
des observations GBIF.
**Action** (environ 2 jours de travail) : récupérer les occurrences GBIF et OpenObs de l'emprise
(environ 660 en Isère sur 5 taxons, doc 03 §3), calculer la **part des observations capturée
par le décile supérieur des mailles** en mode habitat, par espèce, et la comparer au hasard.
Publier le résultat **quel qu'il soit**, avec ses biais : effort d'observation près des
sentiers, et accès qui corrèle avec la présence. Si le lift est faible, c'est un signal de
**re-calibrage avant toute vente**. C'est aussi la règle de re-challenge d'`AGENTS.md`.

## 5. Juridique et licences

### 🔴 5.1 Responsabilité : le périmètre « prospection seule » protège, à condition de le tenir

**Décision du porteur (14/10/2026)** : **aucune partie identification**, même pédagogique. Le
produit dit **où et quand chercher**, et les **bonnes pratiques de cueillette**. C'est la bonne
décision face au risque :

- La confusion la plus fréquente en 2024 est le **clitocybe de l'olivier pris pour une girolle
  ou une chanterelle** (Anses). Or le produit oriente vers girolles, chanterelles et morilles,
  cette dernière pouvant être confondue avec la gyromitre, toxique.
- L'identification par photo plafonne à 35–49 % de réussite, et l'Anses comme UFC-Que Choisir
  s'en méfient (doc 03 §2). En ne donnant **aucun avis sur un champignon cueilli**, Le Bon Versant
  sort du terrain où se jouent les intoxications.

**Ce qui reste nécessaire** (cela relève des bonnes pratiques et du cadre légal, pas de
l'identification) :

1. un **avertissement permanent et visible** : « Cette carte indique des zones à prospecter.
   Elle ne dit rien de la comestibilité d'un champignon ; faites toujours contrôler votre
   cueillette (pharmacien, société mycologique) » ;
2. les **bonnes pratiques de cueillette** : quotas, propriété, respect du milieu (couper ou
   tourner sans arracher, ne pas ratisser), saisons de chasse, sécurité en montagne ;
3. des **CGU et CGV** qui décrivent le service comme une aide à la prospection, sans garantie
   de récolte. Relecture juridique conseillée (coût **non chiffré**).

**Conséquence produit** : retirer de la feuille de route toute « fiche confusion » ou tout
« guide d'identification ». La promesse « accessible aux novices » repose sur la **simplicité
de la carte** et sur les **bonnes pratiques**, pas sur la reconnaissance des espèces.

### 🔴 5.2 Météo : l'offre gratuite d'Open-Meteo interdit l'usage commercial

« Free … for non-commercial use » ; un abonnement est requis pour un service payant, et donne
une clé API ([open-meteo.com/en/pricing](https://open-meteo.com/en/pricing)). Prix actuel non
affiché lors du relevé (une ancienne annonce parlait de 29 $/mois).
**Action** : soit souscrire (coût récurrent à couvrir par les premiers passes), soit basculer
sur les **données ouvertes Météo-France** (AROME et observations, publiées sous Licence
Ouverte selon nos informations, **à vérifier** sur meteo.data.gouv.fr), avec plus de travail
d'ingestion. À arbitrer selon le budget, qui n'est pas précisé.

### 🔴 5.3 Fonds de carte non exploitables commercialement en l'état

- `tile.openstreetmap.org` : accès retirable « à tout moment » pour un service commercial,
  **hors-ligne interdit** ([politique OSMF](https://operations.osmfoundation.org/policies/tiles/)).
  Le code utilise encore les sous-domaines `{s}.tile.openstreetmap.org`.
- Imagerie **Esri** : conditions commerciales non établies (doc 03 §6.4).
- OpenTopoMap : CC BY-SA, « usage raisonnable ».

**Action** : passer aux **fonds IGN de la Géoplateforme** (Plan IGN, orthophotos, sous Licence
Ouverte ; le SCAN 25 reste sous licence et est exclu), ou à un fournisseur de tuiles sous
contrat. **Conditions de service et hors-ligne à vérifier** avant de construire la PWA.
Pour les **paquets hors-ligne**, l'extrait **Protomaps auto-hébergé** (PMTiles, attribution
OSM) est la voie retenue (doc 05 §4.2) : la politique des tuiles OSM interdit le
pré-téléchargement, et les conditions du hors-ligne de la Géoplateforme IGN ne sont pas
vérifiées (doc 05 §10.3). Cela vaut pour une PWA comme pour une appli.

### 🟠 5.4 Licences des données : globalement favorables, avec deux vigilances

| Source | Licence | Usage commercial | Vigilance |
|---|---|---|---|
| IGN (BD Forêt, RGE ALTI) | Licence Ouverte 2.0 | Oui, avec attribution | — |
| IGN LIDAR HD | Présumée Licence Ouverte | **Non vérifié sur la fiche produit** | Vérifier avant de communiquer dessus |
| BRGM Charm-50 | Licence Ouverte 2.0 (selon [data.gouv](https://data.gouv.fr/en/datasets/cartes-geologiques-departementales-a-1-50-000-bd-charm-50)) | Oui | Fiche communautaire, à confirmer sur Infoterre |
| Copernicus TCD | Accès libre, attribution, mention « modifié » | Oui | Ne pas suggérer un soutien de l'UE |
| EcoDataCube pH | CC-BY (d'après `AGENTS.md`) | Oui | **Non vérifié sur le web** |
| OSM (couvert, eau, réseau d'accès) | **ODbL** | Oui | **Partage à l'identique** : une base dérivée distribuée (paquet hors-ligne contenant les données) doit être offerte sous ODbL. Des tuiles image rendues sont un « produit dérivé » (attribution seule). Concevoir les paquets hors-ligne en conséquence |
| Overpass public | Politique d'usage | Précalcul ponctuel acceptable ; pas en ligne pour des utilisateurs | Le code l'utilise seulement au précalcul : OK |

### 🟠 5.5 Droit de cueillir : la carte peut induire en infraction

Le masque « accès » mesure une **marche possible**, pas un **droit d'entrer**. En forêt privée,
cueillir sans autorisation est une contravention de 4ᵉ classe, et au-delà de 10 L un délit de
vol (Code forestier R163-5 et L163-11, [réponse ministérielle](https://questions.assemblee-nationale.fr/dyn/14/questions/QANR5L14QE9341.pdf)).
En forêt publique soumise au régime forestier, une autorisation est présumée jusqu'à 5 L, sauf
arrêté contraire. Un novice lira « accessible » comme « autorisé ».
**Action** : ajouter la couche **forêts publiques ONF** (open data, [data.gouv](https://www.data.gouv.fr/datasets/forets-publiques-diffusion-publique/informations),
documentation lacunaire), renommer « accès » en « marche estimée », afficher les arrêtés
préfectoraux connus du massif. Ce trou de marché devient un argument de vente, au cœur des
« bonnes pratiques ».

### 🟠 5.6 Sécurité en montagne

L'itinéraire autorise **500 m d'approche hors sentier jusqu'à 40° de pente**
(`AccessThreshold`). Pour un novice, une pente de 40° est un terrain dangereux.
**Action** : mode novice qui plafonne l'approche (par exemple 25°, valeur à valider), étiquette
« hors sentier » visible sur le tracé et le GPX, et un avertissement.

### 🟠 5.7 RGPD

- Aujourd'hui, aucune donnée personnelle n'est stockée. C'est un atout à préserver.
- **Google Fonts chargé depuis le CDN** (`index.html`) : transfert d'IP vers Google. Un tribunal
  allemand l'a jugé illicite sans consentement (LG München I, 20/01/2022). Le CSS Leaflet vient
  aussi d'unpkg.
  **Action** : héberger Inter et Leaflet localement (une heure de travail).
- Futurs comptes, spots personnels et géolocalisation : suivre les recommandations de la CNIL
  (minimisation, localisation ponctuelle plutôt que continue, information claire —
  [CNIL](https://cnil.fr/fr/geolocalisation-applications-mobiles-quelles-regles)). Faire de la
  vie privée un argument, comme Boletik avec ses spots chiffrés en local.

### 🟠 5.8 Micro-entreprise en création : obligations et coûts

Le porteur créera une **micro-entreprise** (régime classique). Points à intégrer, **à confirmer
sur urssaf.fr, impots.gouv.fr et service-public.fr** (seules des sources secondaires ont été
consultées) :

| Sujet | Ce que disent les sources | Effet sur le projet |
|---|---|---|
| Nature de l'activité | Vente d'accès numériques à des particuliers : *prestation de services* (classement BIC ou BNC à confirmer au moment de la déclaration) | Détermine le taux de cotisations |
| **Cotisations sociales** | **21,2 %** du chiffre d'affaires pour les prestations de services BIC, 25,6 % pour les BNC du régime général ; plus 0,1 à 0,3 % de formation professionnelle (sources secondaires concordantes, par exemple [portail-autoentrepreneur.fr](https://www.portail-autoentrepreneur.fr/academie/statut-auto-entrepreneur/cotisations)) ; réduction **ACRE** possible au démarrage (modalités divergentes selon les sources) | Sur un pass à 19 €, ~4 € de cotisations (§3.4 du doc 05) |
| **TVA** | Franchise en base jusqu'à **37 500 €** de prestations de services (seuil majoré 41 250 €) ; le seuil unique à 25 000 € a été abandonné en novembre 2025 ([comptabook.fr](https://comptabook.fr/tva/seuil-franchise-tva-2026/), à confirmer sur service-public.fr) | Pas de TVA facturée : le prix affiché est le prix encaissé ; en contrepartie, **la TVA payée sur les dépenses n'est pas récupérable** (coûts à compter TTC) |
| **Médiateur de la consommation** | **Obligatoire** pour vendre à des particuliers, en ligne ou non ; mention dans les CGV ; amende administrative possible en cas d'oubli ; coût d'adhésion **30 à 80 €/an** selon une source commerciale (**non vérifié**) ([portail-autoentrepreneur.fr](https://www.portail-autoentrepreneur.fr/academie/creation-auto-entreprise/mediation-consommation)) | Ligne de coût récurrente ajoutée au doc 05 §4 |
| Mentions légales, CGV, droit de rétractation sur contenu numérique | Obligatoires ; conditions de renonciation au droit de rétractation à rédiger avec soin | Inclus dans la relecture juridique (**non chiffré**) |
| CFE, compte bancaire dédié, impôt sur le revenu (barème ou versement libératoire de 1,7 % en BIC services, option) | **Non instruits** en détail | À vérifier à la création |
| Dépôt de marque INPI | ~**190 €** pour une classe, +40 € par classe ; renouvellement à 10 ans (sources secondaires, par exemple [captaincontrat.com](https://www.captaincontrat.com/articles-creation-entreprise/cout-depot-marque-inpi)) | Coût ponctuel, conseillé une fois le nom choisi (doc 05 §9) |

## 6. UX et onboarding (cible novice)

| Constat | Gravité | Action |
|---|---|---|
| Jargon dans l'interface et les explications : « TCD », « pH / substrat », « phénologie », « apport en eau », 11 masques | 🟠 | Mode « simple » par défaut : 1 carte (« où chercher cette semaine »), 3 niveaux en mots, et le détail technique derrière un dépliant « pourquoi ? » |
| Aucun onboarding ; ouverture sur une carte de 5 800 km² | 🟠 | Parcours en 3 étapes : espèce → « près de moi » ou « mon massif » → « quand y aller ». Premier bénéfice en moins de 60 s |
| Pensé ordinateur ; un seul point de rupture à 720 px | 🔴 pour un usage terrain | Conception mobile d'abord (la carte se consulte sur le terrain) |
| Le score affiché est un indice, pas une probabilité (mention présente) | 🟡 bon point | Garder ; c'est exactement l'incompréhension relevée chez les concurrents (« 80 % ≠ 80 % de chances ») |
| Branding incohérent (« Forage Mapper » dans le `<title>`, « Myco Map » ailleurs) ; nom retenu : **Le Bon Versant** | 🟡 | Remplacer les deux noms dans l'interface pendant la phase 1 ; réserver les domaines et déposer la marque (doc 05 §9) |
| Pas de calendrier lisible par espèce | 🟠 | Fiches courtes **de prospection** par espèce : habitat, altitude, saison, délai après la pluie ; **aucun contenu d'identification** |

## 7. Qualité et maintenabilité, à moins de 15 h/semaine

- 🟠 **Aucun test backend** : chaque recalibrage risque une régression silencieuse du score.
  **Action** : des tests de non-régression sur une poignée de mailles de référence (score
  attendu ± tolérance) et le contrôle « somme des poids = 1 ».
- 🟠 **Données qui vieillissent** : rien ne rafraîchit OSM, BD Forêt ou TCD. **Action** : un
  précalcul annuel scripté de bout en bout, hors saison (janvier–février).
- 🟡 **Développement en rafale** (54 commits en 5 jours, rien depuis 7 semaines) : le code est
  propre mais le rythme n'a pas été testé. Le régime de croisière doit être conçu pour **ne
  rien exiger en saison** à part la météo automatique.

## 8. Positionnement : le piège du « France entière »

Le marché est encombré au centre (doc 02 §6). Le reflexe « couvrir toute la France pour faire
comme Mycora » est incompatible avec moins de 15 h/semaine **et** dilue le seul avantage
(précision montagne). À l'inverse, un massif unique limite le revenu à quelques centaines
d'euros par an (doc 03 §7.3). **Le bon compromis est un chapelet de massifs à forte densité
d'observations, ajoutés un par saison.**

## 9. Code fermé : décision prise, conséquences à gérer

**Décision du porteur (14/10/2026)** : **pas d'open source**. Le code, les modèles (profils
d'espèces, poids) et les données préparées restent **propriétaires**.

### 🔴 9.1 Le dépôt est encore public sous MIT

Au 14/10/2026, `Thomerdos/myco-map` est **public** sur GitHub sous licence MIT (0 étoile,
0 fork). **L'étude de marché, elle, est publiée volontairement** sur GitHub Pages
(<https://thomerdos.github.io/myco-etude-marche/>), avec l'accord du porteur : stratégie, prix
et nom retenu sont donc publics. C'est le **code** qu'il faut fermer.

- Le code **déjà publié** reste utilisable sous MIT par quiconque en a obtenu une copie : une
  licence accordée ne se retire pas. La fermeture vaut **pour la suite**.
- **Action** (par le porteur, car c'est irréversible côté visibilité) :
  1. passer le **dépôt de code** en **privé** ;
  2. remplacer `LICENSE` (MIT) par une mention « tous droits réservés » pour les versions
     futures ;
  3. mettre à jour README, `ATTRIBUTION.md` et `AGENTS.md`, qui mentionnent la licence MIT ;
  4. retirer du dépôt l'archive `data/*.sqlite.gz`, ou au moins cesser de la mettre à jour ;
  5. **plus tard**, renommer le dépôt (par exemple `le-bon-versant`) et mettre à jour le remote
     local. **Non fait** : le choix du moment revient au porteur (doc 05 §9).
- **Conséquence marketing** : l'argument « méthode publiée » disparaît. Il reste l'**explication
  par maille** (dans le produit) et la **validation publiée** (résultats, pas le code). C'est ce
  que fait Boletik.

### 🔴 9.2 Code fermé ≠ données fermées : l'ODbL s'applique toujours aux couches OSM

Les couches **couvert de repli, lisière, cours d'eau et réseau d'accès** viennent
d'OpenStreetMap. Elles forment une *base dérivée*. L'ODbL prévoit que si l'on rend public
« une base dérivée **ou une œuvre produite à partir d'une base dérivée** », il faut offrir
gratuitement, en ligne, **soit la base dérivée entière, soit un fichier décrivant les
modifications ou la méthode pour les faire (par exemple un algorithme)**
([ODbL 1.0, §4.4 et §4.6](https://opendatacommons.org/licenses/odbl/1-0/)). Les tuiles de
score vendues sont des œuvres produites à partir de ces couches.

| Option | Effet | Coût |
|---|---|---|
| **A. Publier les seules couches OSM dérivées** (distances à la lisière et à l'eau, réseau d'accès) sous ODbL, ou la description de leur algorithme de dérivation, en gardant le reste séparé (base « collective », §4.5) | Conforme ; le score, la calibration et les données IGN restent propriétaires | Faible : une page de téléchargement ou de documentation |
| **B. Remplacer OSM par la BD TOPO de l'IGN** (routes, chemins, hydrographie ; Licence Ouverte, attribution seule) et BD Forêt pour le couvert | Plus aucune obligation de partage à l'identique | 1–2 semaines ; **complétude des sentiers BD TOPO face à OSM à tester** sur le massif |

**Décision du porteur (14/10/2026) : option A.** On publie les seules couches dérivées d'OSM
(ou leur algorithme de dérivation), séparées du reste. Le score, la calibration et les données
IGN restent propriétaires. *Lecture de la licence par un non-juriste : à faire confirmer.*

Les **fonds de carte** issus d'OSM tels quels (par exemple un extrait Protomaps auto-hébergé,
diffusé comme « œuvre produite », [docs Protomaps](https://docs.protomaps.com/basemaps/downloads))
ne demandent que l'attribution, puisqu'on ne modifie pas la base.

## 10. Récapitulatif priorisé

| # | Point | Gravité | Effort estimé |
|---|---|---|---|
| 1 | Validation GBIF / OpenObs du score (§4) | 🔴 | ~2 jours |
| 2 | Licences commerciales météo et fonds de carte (§5.2, §5.3) | 🔴 | 1–3 jours + coût récurrent |
| 3 | Avertissement « pas d'avis sur la comestibilité », bonnes pratiques de cueillette, CGU/CGV (§5.1) | 🔴 | 2–3 jours (+ relecture juridique) |
| 4 | Déploiement de production minimal (§3.1) | 🔴 | 2–3 jours |
| 5 | Paiement, pass, résiliation simple (§3.2) | 🔴 | 3–5 jours |
| 6 | Hors-ligne par massif (§3.4), code portable vers Capacitor (§3.6) | 🔴 terrain | 1–2 semaines (+~1 jour) |
| 7 | Habitat statique + météo planifiée (§3.3) | 🟠 | 1 semaine |
| 8 | Mode simple, onboarding, mobile d'abord (§6) | 🟠 | 1–2 semaines |
| 9 | Forêts publiques et « marche estimée » (§5.5) | 🟠 | 2–3 jours |
| 10 | Polices et CSS hébergés localement (§5.7) | 🟠 | < 1 h |
| 11 | Tests de non-régression (§7) | 🟠 | 1–2 jours |
| 12 | « Le Bon Versant » : domaines, recherche d'antériorité, dépôt INPI, nom dans l'interface (§6, doc 05 §9) | 🟠 | ½ jour + ~190–230 € INPI |
| 13 | Dépôt privé + licence propriétaire + conformité ODbL, option A retenue (§9) | 🔴 | < 1 jour |
| 14 | Création de la micro-entreprise, médiateur, mentions légales (§5.8) | 🟠 | ½–1 jour + 30–80 €/an (non vérifié) |
| 15 | Applis hybrides iOS et Android (§3.6) : calendrier à arbitrer par le porteur | 🟠 | +3 à 5 semaines + ~120 € la 1ʳᵉ année ; −26 à −35 % de net par pass vendu dans l'appli |

*Les efforts sont des ordres de grandeur pour un développeur seul qui connaît le code ; ce ne
sont pas des engagements.*
