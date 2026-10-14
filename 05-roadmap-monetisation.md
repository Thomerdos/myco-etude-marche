# 05 — Recommandations et roadmap de monétisation

*14 octobre 2026. Skills appliqués : `product-marketing` (positionnement), `marketing-council`
(arbitrage), `pricing` et `offers` (packaging, offre), `marketing-plan` (AARRR, phasage,
critères d'arrêt), `aso` (si passage aux stores).*

## 0. Cadre fixé par le porteur

| Paramètre | Réponse (14/10/2026) | Conséquence de conception |
|---|---|---|
| Ambition à 2–3 ans | Revenu d'appoint (quelques centaines à quelques milliers d'€/an), sans levée de fonds ni recrutement | Viser **100 à 300 passes par an**, pas la France entière |
| Temps | Phase initiale de développement maintenant, puis **moins de 15 h/semaine** | Tout ce qui tourne en saison doit être **automatique** |
| Budget | **Non précisé** | Coût quasi nul hors hébergement ; chaque coût récurrent est signalé comme décision ouverte |
| Cible | B2C, zones riches en champignons, **accessible aux novices** | Précision de montagne + couche sécurité et pédagogie incluse |
| Modèle | **Payant d'abord**, gratuit très restreint | Démo minimale, pas de freemium |
| Open source | **Non : code, modèles et données préparées propriétaires** (précision du 14/10/2026) | Dépôt à passer en privé ; conformité ODbL des couches OSM à gérer (doc 04 §9) |
| Coûts | Budget de développement non chiffré ; **estimations de coûts récurrents demandées** | Scénarios « minimal » et « confort » chiffrés au §4 |

---

## 1. Positionnement (chaîne de Dunford, via `product-marketing`)

| Maillon | Contenu pour myco-map |
|---|---|
| **Alternatives réelles** | (1) Expérience et bouche-à-oreille ; (2) Géoportail (BD Forêt) + carte IGN, gratuits ; (3) indices gratuits (Champiscope, les-champignons.fr) ; (4) cartes payantes France entière (Mycora, Champi, Chasseurs de champignons) |
| **Attributs uniques** | Relief 5 m et canopée LIDAR HD à 50 m en montagne ; « pourquoi ici » par maille ; fenêtre de pousse à 14 jours par espèce ; itinéraire parking → zone avec temps de marche ; **validation publiée** (résultats chiffrés, pas le code, à produire) |
| **Valeur** | Moins de soirées de prospection, des secteurs nouveaux qu'on comprend, le bon jour pour y aller, un retour à la voiture sans se perdre, et ne pas cueillir là où c'est interdit |
| **Clients qui y tiennent le plus** | Cueilleurs des **massifs alpins** (S1), randonneurs-montagnards équipés (S3), et novices accompagnés par la couche sécurité (S2) |
| **Catégorie** | Pas « carte des coins à champignons » (catégorie encombrée et soupçonnée de promettre des « kilos »), mais **« carte de prospection des massifs de montagne »** |
| **Style** | **Gros poisson dans une petite mare** : dominer quelques massifs, pas concurrencer Mycora sur la France |

**Promesse de travail** (à tester, pas un slogan définitif) :
*« Où et quand chercher dans votre massif cette semaine, expliqué maille par maille, avec le
chemin depuis la voiture. »*

**Messages de preuve** (ne les utiliser que lorsqu'ils sont vrais) : « X % des observations
GBIF de cèpes en Isère tombent dans les 10 % de mailles les mieux notées » ; « résiliation en
un clic, pas de renouvellement surprise ».

**Mots à éviter** (`offers`, vocabulaire banni) : « coins secrets », « kilos garantis »,
« révolutionnaire », « IA qui trouve les champignons », toute probabilité de trouver.

## 2. Conseil marketing (simulation)

> *Conseil simulé : chaque avis est construit à partir des cadres publiés de chaque conseiller,
> pas d'un avis réel de ces personnes sur ce projet.*

**Question posée** : comment faire payer quelques centaines de cueilleurs par an, en solo, sur
un marché encombré, avec une promesse « novice-friendly » ?
**Siègent** : April Dunford (positionnement), Seth Godin (plus petite audience viable),
Alex Hormozi (offre), et Byron Sharp, **contradicteur désigné**, qui se méfie de la
différenciation et de la niche.

**Dunford — positionnement contre les vraies alternatives.** Sa première question : que ferait
le client si myco-map n'existait pas ? Réponse : Géoportail le soir, ou Champi. Les attributs
qu'aucune alternative n'a sont la précision de montagne, l'explication et l'itinéraire. Ils ne
valent quelque chose que pour ceux qui cherchent dans des **terrains raides et variés**. Elle
choisirait le style « gros poisson, petite mare » et refuserait de créer une catégorie.
*En résumé : vendre la meilleure carte de prospection des Alpes du Nord, pas une carte de
France de plus.*

**Godin — plus petite audience viable.** À qui est-ce destiné, et à quoi ça sert ? Quelques
centaines de cueilleurs alpins qui se reconnaissent dans « les gens comme nous préparent leur
sortie sérieusement et respectent la forêt ». Il demanderait la permission avant de vendre : un
**bulletin de pousse par massif**, attendu après chaque orage. Il mettrait en garde contre la
course vers le bas de Mapignon et Boletik.
*En résumé : servir une petite tribu de façon remarquable, et la laisser en parler.*

**Hormozi — équation de valeur.** Il noterait les quatre leviers :
résultat rêvé 6/10 (nouveaux secteurs, panier) ; **probabilité perçue 3/10** (aucune preuve) ;
délai 7/10 (fenêtre J+14, alertes) ; effort 4/10 (interface experte). Le levier le plus faible
est la probabilité perçue. Il faut donc une validation publiée et une garantie, pas une baisse
de prix. Il refuserait de concurrencer à 6,99 € et vendrait **plus cher avec plus de valeur
empilée** : hors-ligne, itinéraire, alertes, fiches de sécurité, carte imprimée.
*En résumé : ne pas baisser le prix ; augmenter la certitude et réduire l'effort.*

**Sharp — contradicteur.** Les acheteurs perçoivent rarement la différenciation. Ils achètent
ce dont ils se souviennent et ce qu'ils trouvent facilement. Une niche de quelques centaines
d'acheteurs aura aussi moins de fidélité (« double peine »). Il demanderait d'être présent à
**tous** les moments d'entrée dans la catégorie (« ça pousse ? » après la pluie, « champignons
+ nom du massif ») avec des signes distinctifs constants (nom, couleur, carte reconnaissable),
plutôt que de compter sur la loyauté.
*En résumé : une niche, d'accord, mais être partout où l'on cherche dans cette niche, avec une
identité constante.*

**Où le conseil diverge**

1. **Différenciation contre disponibilité** (Dunford et Hormozi face à Sharp). Le vrai arbitrage
   est le suivant : investir dans la preuve de précision, ou dans la présence SEO et
   communautaire ? *Ce qui trancherait* : la validation GBIF. Si l'écart avec le hasard est net,
   la différenciation est démontrable et vaut d'être mise en avant. S'il est faible, Sharp a
   raison et il faut miser sur la présence.
2. **Prix plus élevé et plus de valeur, ou prix d'appel** (Hormozi face à la tentation Boletik).
   Ce qui trancherait : un sondage Van Westendorp et une pré-vente à deux niveaux de prix.
3. **Permission ou vente directe** (Godin face au « payant d'abord »). Compromis : le bulletin
   gratuit est **éditorial** (au niveau du massif, sans carte détaillée). Il construit la
   permission sans transformer le produit en freemium.

**Synthèse du président**

- **À faire** : (1) publier la validation avant de vendre ; (2) un bulletin de pousse par
  massif comme seul gratuit récurrent ; (3) un pass saison à valeur empilée, sans prix
  plancher ; (4) une présence constante sur les recherches « champignons + massif ».
- **Signal d'alerte** (Sharp) : si moins de 2 % des abonnés au bulletin achètent un pass en
  saison, la niche est trop petite ou mal servie ; il faut élargir à d'autres massifs avant
  d'ajouter des fonctions.
- **Exécution** : `pricing`, `offers`, `copywriting`, `content-strategy`, `emails`.

## 3. Offre et packaging (`pricing` + `offers`)

### 3.1 Gamme proposée (deux paliers, une seule métrique : la zone)

| Produit | Contenu | Prix de test | Logique |
|---|---|---|---|
| **Découverte** (gratuit, très restreint) | 1 **secteur vitrine fixe** (environ 10 × 10 km), semaine en cours, mode simple, sans export, sans hors-ligne, sans compte ; plus le **bulletin de pousse par massif** par e-mail | 0 € | Démonstration et permission, conforme au « gratuit très restreint ». Ce n'est pas un freemium : aucune zone personnelle |
| **Pass Saison — 1 massif** | 12 mois, toutes espèces, carte complète du massif, J+14, « pourquoi ici », itinéraires GPX/KMZ, **hors-ligne**, alertes après orage, fiches sécurité et confusions, couche forêts publiques | **19 €** (fourchette à tester : 15–25 €) | Métrique zone × saison (doc 03 §6.2) ; au-dessus de l'ancre Boletik, sous Champi et Chasseurs |
| **Pass Saison — Tous massifs** | Idem, sur tous les massifs couverts (Alpes du Nord, puis Jura…) | **29 €** (à tester) | Répond à la plainte « je suis à la frontière de deux zones » (10 % chez Chasseurs) ; permet de monter en gamme à mesure que la couverture s'étend |
| **Carte imprimée du massif** (achat unique, hors saison) | Carte A1 du potentiel d'habitat du massif, légende pédagogique, mentions de sécurité et de légalité | À fixer entre 39 et 59 € (coût d'impression à la demande **non vérifié**) | Revenu de novembre à mars, cadeau de fin d'année ; Les Cartes Terroirs valide le format à 69,99 € |

**Pourquoi pas de paliers par fonctionnalité** : chaque palier supplémentaire, c'est du
support et des cas limites. À moins de 15 h/semaine, **une seule métrique (la zone)** est plus
simple à maintenir et à expliquer.

**Pourquoi pas de mensuel** : l'usage tient à quelques semaines par an (doc 03 §5). Un mensuel
pousse à résilier après la poussée ; c'est le problème vécu chez Chasseurs de champignons.

### 3.2 Les six composantes de l'offre (`offers`)

| Composante | Proposition |
|---|---|
| **Cœur** | Le Pass Saison du massif |
| **Bonus** (réels, pas gonflés) | Fiches « ne pas confondre » pour les 6 espèces ; export GPX vers l'appli de randonnée de l'utilisateur ; carte des sociétés mycologiques et des centres antipoison ; rappel des règles de cueillette du département |
| **Garantie** | **Remboursement intégral sous 14 jours, sans justification** ; **pas de renouvellement automatique par défaut** (rappel par e-mail, renouvellement en un clic). C'est le contre-pied direct des avis négatifs sur Chasseurs de champignons. *Conditions à relire juridiquement (droit de rétractation sur contenu numérique).* |
| **Rareté réelle** | **100 passes « fondateurs »** à prix réduit (par exemple 12 €), **tarif garanti tant que le pass est renouvelé sans interruption**, ouverts jusqu'à la veille de la saison des morilles 2027. Pas de faux compte à rebours |
| **Nom** | « Pass Saison [nom du massif] ». Le nom de marque reste à choisir (doc 04 §6) |
| **Prix et paiement** | Paiement unique annuel via Stripe Checkout ; Customer Portal pour factures et remboursements |

### 3.3 Arbitrages assumés

| Option | Gain | Coût | Choix |
|---|---|---|---|
| Prix bas (≤ 10 €), comme Boletik | Conversion facile | Piège du 9 € ; course vers le bas ; ~200 passes pour 2 k€ | ❌ |
| Prix moyen (19–29 €) | Couvre les coûts avec peu d'acheteurs ; cohérent avec la valeur empilée | Exige une preuve (validation) | ✅ à tester |
| Abonnement mensuel | Revenu récurrent apparent | Inadapté à la saisonnalité ; résiliations ; support | ❌ |
| Freemium généreux | Audience | Contraire au choix du porteur ; coûts serveur et météo | ❌ |
| Appli native sur les stores | Visibilité ASO | Commission, revue, double maintenance | ⏸ plus tard (§7) |
| B2B (offices de tourisme, accompagnateurs) | Revenus plus gros par client | Vente active, hors cible B2C | ⏸ option 2028+ |
| Identification photo | Attente des novices | Responsabilité, 35–49 % de fiabilité, marché saturé | ❌ définitif |

### 3.4 Économie unitaire

Frais Stripe pour une carte de l'Espace économique européen : **1,5 % + 0,25 €** par paiement,
sans abonnement ; un remboursement ne rend pas ces frais ([stripe.com/fr/pricing](https://stripe.com/fr/pricing),
relevé du 14/10/2026). Net par vente :

| Produit | Prix | Frais Stripe | **Net** |
|---|---|---|---|
| Pass fondateur | 12 € | 0,43 € | **11,57 €** |
| Pass Saison — 1 massif | 19 € | 0,535 € | **18,47 €** |
| Pass Saison — tous massifs | 29 € | 0,685 € | **28,32 €** |

Les coûts récurrents et le nombre de passes nécessaires sont au §4.

## 4. Coûts récurrents : estimations chiffrées

*Prix relevés les 13 et 14/10/2026 sur les sources citées, **hors TVA** sauf mention. « Tiers »
= relevé sur un site comparateur et non sur la page du fournisseur : à confirmer dans la console
avant de s'engager. « Non vérifié » = aucune source fiable trouvée. Les montants en dollars ne
sont pas convertis à un taux précis : on prend 0,85 à 0,95 € par dollar, taux **non vérifié**.*

### 4.1 Hypothèses de dimensionnement

| Hypothèse | Valeur retenue | Base |
|---|---|---|
| Zone servie | Alpes du Nord (Isère, Savoie, Haute-Savoie, Drôme) ≈ 24 000 km² | Surfaces départementales en ordre de grandeur, non revérifiées |
| Mailles de 50 m | ≈ 9,7 M (environ 4 fois l'emprise actuelle) | Calcul |
| Base SQLite | ≈ 0,6 à 0,8 Go | Extrapolation linéaire de 150–205 Mo pour 2,35 M mailles (doc 01) |
| Tuiles d'habitat (6 espèces, zooms 10 à 15) | ≈ 2 à 4 Go | Hypothèse : ~32 000 tuiles par espèce × 10–20 Ko |
| Fond de carte hors-ligne (extrait Protomaps de la zone) | 0,5 à 2 Go | **Non mesuré** ; la taille double à chaque niveau de zoom ([docs Protomaps](https://docs.protomaps.com/basemaps/downloads)) |
| Données brutes de travail (LIDAR, MNT…) | ~13 Go, **restent sur la machine de développement** | Doc 01 ; inutiles en production |
| Payants en saison | Jusqu'à 300 | Haut de l'objectif (§3.4) |
| Trafic sortant | 300 × 2 à 4 téléchargements hors-ligne de 100–200 Mo ≈ **60 à 240 Go par saison**, plus la navigation | Hypothèse |
| Météo | Grille fixe de 169 points par région, rafraîchie toutes les 1 à 3 h, **indépendante du trafic** (doc 04 §3.3) → ~42 000 à 126 000 requêtes par mois et par région, multipliées par ~2 à 3 selon les règles de pondération d'Open-Meteo (plus de 2 semaines d'historique ou plus de 10 variables comptent plusieurs appels, [open-meteo.com/en/pricing](https://open-meteo.com/en/pricing)) → **~80 000 à 380 000 appels/mois** | Calcul ; le décompte des requêtes multi-points n'est pas précisé par Open-Meteo |

### 4.2 Hébergement : options chiffrées

| Brique | Option | Prix relevé | Source | Remarque |
|---|---|---|---|---|
| **Serveur** | Hetzner Cloud **CX23** (2 vCPU, 4 Go, 40 Go, 20 To de trafic) | **5,49 €/mois + 0,50 € d'IPv4** = 5,99 €/mois | Tiers : [costgoat.com](https://costgoat.com/pricing/hetzner) (MAJ du 05/09/2026) | Allemagne / Finlande seulement ; hausse de prix le 15/06/2026 ; un relevé de septembre signale une indisponibilité ponctuelle |
| | Hetzner **CX33** (4 vCPU, 8 Go, 80 Go) | **8,49 € + 0,50 €** = 8,99 €/mois | Tiers, idem | Confort |
| | OVHcloud **VPS-1** | **6,49 €/mois** (66,19 €/an en prépaiement, tiers) | [Blog OVHcloud](https://blog.ovhcloud.com/en/posts/pricing-evolution-of-public-cloud-bare-metal-and-vps-at-ovhcloud/) | Hébergeur français ; spécifications non listées sur le blog (4 vCPU, 8 Go, 75 Go selon un tiers) |
| | OVHcloud **VPS-2** | **9,99 €/mois** | Idem | Confort |
| **Sauvegardes** | Sauvegardes Hetzner | **20 % du prix du serveur** (7 conservées) | Tiers, idem | Soit ~1,10 € à 1,70 €/mois |
| **Base de données** | **SQLite sur le serveur** (en lecture seule pour l'habitat) | 0 € | — | **Recommandé** : la donnée est précalculée, pas besoin d'un SGBD managé |
| | PostgreSQL managé Scaleway DB-DEV-S | ~0,0156 €/h, soit **~11,40 €/mois** (calcul à partir du tarif horaire, non publié comme tel) + stockage | [Scaleway](https://www.scaleway.com/fr/tarifs/managed-databases) via résultat de recherche | **Non recommandé** : coût sans bénéfice pour ce produit |
| **Stockage des tuiles et paquets hors-ligne** | Cloudflare **R2** | **10 Go/mois gratuits**, puis **0,015 $/Go-mois** ; **sortie gratuite** | [developers.cloudflare.com/r2/pricing](https://developers.cloudflare.com/r2/pricing/) | La sortie gratuite neutralise le coût des téléchargements hors-ligne |
| | Disque du serveur (40 à 80 Go) | Inclus | — | Suffisant au départ ; 20 To de trafic inclus chez Hetzner |
| **CDN** (optionnel) | Bunny CDN | **0,01 $/Go** en Europe, **minimum 1 $/mois** | [bunny.net/pricing/cdn](https://bunny.net/pricing/cdn/) | Utile seulement si la latence pose problème |
| **Fond de carte** | Extrait **Protomaps** auto-hébergé (PMTiles) | 0 € hors stockage | [docs Protomaps](https://docs.protomaps.com/basemaps/downloads) | « Œuvre produite » ODbL : attribution OSM obligatoire ; autorise le hors-ligne puisqu'on l'héberge soi-même |
| | MapTiler Cloud **Flex** | **30 $/mois** ; l'offre gratuite vise le « non-commercial » | [maptiler.com/cloud/pricing](https://www.maptiler.com/cloud/pricing/) | Droits hors-ligne **non précisés** sur la page |
| | Géoplateforme IGN (Plan IGN, orthophotos) en ligne | Gratuit selon des retours d'usagers | Conditions commerciales et hors-ligne **non vérifiées** | À confirmer avant usage |

### 4.3 Maintenance et services : coûts récurrents

| Poste | Option « coût minimal » | Option « confort » | Sources |
|---|---|---|---|
| **Météo** | **Données ouvertes Météo-France** (AROME, Licence Ouverte) : 0 € ; ingestion GRIB à développer (3 à 5 jours estimés) ; conditions de l'API du portail Météo-France non vérifiées | **Open-Meteo API Standard : 29 $/mois** (1 M d'appels, licence commerciale incluse) ; Professional 99 $/mois | [data.gouv AROME](https://data.gouv.fr/en/datasets/donnees-du-modele-atmospherique-arome-a-aire-limitee-a-haute-resolution) ; [blog Open-Meteo](https://openmeteo.substack.com/p/api-subscriptions-for-commercial) (la page de prix en ligne n'affiche pas les montants) |
| **Domaine** | .fr : **~7,79 € HT/an** | Idem (+ .com, non vérifié) | Source non officielle, **non vérifié** sur la boutique OVHcloud France |
| **E-mails** (liens magiques, reçus, alertes, bulletin) | **Resend gratuit** : 3 000/mois, **100/jour** au plus | **Resend Pro : 20 $/mois** (50 000/mois, sans plafond journalier) | [resend.com/pricing](https://resend.com/pricing) |
| **Paiement** | Stripe : **1,5 % + 0,25 €** par carte de l'EEE, sans abonnement ; Checkout inclus | Idem ; Stripe Tax en option : 0,5 % par transaction (no-code) | [stripe.com/fr/pricing](https://stripe.com/fr/pricing) |
| **Sauvegardes** | Sauvegardes Hetzner (20 %) ou copie vers R2 (gratuit sous 10 Go) | Les deux | Voir §4.2 |
| **Supervision** | UptimeRobot **gratuit** (50 sondes, 5 min ; décrit comme « pour projets hobby et non-profit », usage commercial **non confirmé**) + Sentry **Developer gratuit** (1 utilisateur, 5 000 erreurs/mois) | UptimeRobot **Solo : 9 €/mois** en annuel (108 €/an) ; Sentry Team (26 $/mois) jugé superflu | [uptimerobot.com/pricing](https://uptimerobot.com/pricing/), [sentry.io/pricing](https://sentry.io/pricing/) |
| **Stores** (plus tard, §7) | — | Apple : ~99 $/an ; Google Play : ~25 $ une fois | Sources secondaires ([splitmetrics](https://splitmetrics.com/blog/google-play-apple-app-store-fees/)), **à confirmer** |
| **Relecture juridique** (CGU/CGV) | **Non chiffré** | **Non chiffré** | — |
| **Statut, cotisations, comptabilité** | **Non instruit** | **Non instruit** | — |

### 4.4 Deux scénarios annuels

| Ligne | **Coût minimal** | **Confort** |
|---|---|---|
| Serveur | Hetzner CX23 + IPv4 : 71,88 € | Hetzner CX33 + IPv4 : 107,88 € |
| Sauvegardes | 20 % : 13,18 € | 20 % : 20,38 € |
| Base de données | SQLite : 0 € | SQLite : 0 € |
| Stockage et sortie | R2 gratuit (≤ 10 Go) : 0 € | R2 ~30 Go : ~3,60 $ |
| CDN | — | Bunny : ~12 à 15 $ |
| Fond de carte | Protomaps auto-hébergé : 0 € | Idem : 0 € |
| Météo | Météo-France ouvert : 0 € | Open-Meteo Standard : 348 $ |
| E-mails | Resend gratuit : 0 € | Resend Pro : 240 $ |
| Supervision | Gratuit : 0 € | UptimeRobot Solo : 108 € |
| Domaine | ~7,79 € (non vérifié) | ~7,79 € (non vérifié) |
| **Total HT** | **≈ 93 €/an** | **≈ 244 € + ~606 $ ≈ 760 à 820 €/an** |
| **Passes à 19 € pour couvrir** (net 18,47 €) | **≈ 6 passes** (≈ 7 si la TVA de 20 % n'est pas récupérable) | **≈ 42 à 45 passes** (davantage TTC) |

**Scénario intermédiaire recommandé si l'ingestion Météo-France prend trop de temps** :
minimal + Open-Meteo Standard ≈ 93 € + 348 $ ≈ **390 à 425 €/an**, soit **≈ 21 à 23 passes**.

**Non compris** : relecture juridique, cotisations sociales et impôts, temps passé, matériel,
stores. Le passage d'un scénario à l'autre se fait **ligne par ligne**, au fil des besoins.

### 4.5 Résultat selon les ventes (avant impôts et cotisations, non instruits)

| Passes vendus par an | Net Stripe (prix moyen) | − coût minimal (93 €) | − confort (~800 €) |
|---|---|---|---|
| 50 (19 €) | 923 € | **≈ 830 €** | **≈ 120 €** |
| 150 (22 € en moyenne, net 21,42 €) | 3 213 € | **≈ 3 120 €** | **≈ 2 410 €** |
| 300 (22 € en moyenne) | 6 426 € | **≈ 6 330 €** | **≈ 5 630 €** |

**Lecture** : le scénario minimal est rentable dès la première dizaine de passes. Le confort ne
se justifie qu'au-delà d'environ 100 passes par an, ou si le temps gagné (pas d'ingestion
Météo-France, e-mails sans plafond) vaut plus que ~700 €/an.

### 4.6 Charge de travail récurrente (objectif : moins de 15 h/semaine)

| Tâche | Fréquence | Charge estimée |
|---|---|---|
| Support (questions, remboursements) | En saison | 1 à 3 h/semaine |
| Supervision et incidents | Alertes automatiques | ~1 h/semaine en saison |
| Mises à jour de sécurité (système, PHP, dépendances) | Mensuelle | 1 à 2 h/mois |
| Bulletin de pousse | Généré automatiquement après un épisode pluvieux, puis relu | ~30 min par envoi, 1 à 2 par semaine en saison |
| Contenu, SEO, présence communautaire | En saison | 2 à 4 h/semaine |
| Comptabilité, rapprochement Stripe | Mensuelle | ~1 h/mois |
| Précalcul annuel des données | Janvier–février | 2 à 3 jours/an |
| Nouveau massif | Une fois par an, hors saison | 1 à 2 semaines/an |
| Revue des prix et licences des fournisseurs | Annuelle | ~½ journée/an |
| **Total** | | **≈ 5 à 10 h/semaine en saison ; 1 à 3 h/semaine en moyenne hors saison**, plus les blocs annuels |

**Condition** : cela suppose la refonte « habitat statique + météo planifiée » (doc 04 §3.3).
Sans elle, la charge et les coûts croissent avec le trafic.

## 5. Roadmap par phases

*Les efforts sont des ordres de grandeur pour un développeur seul qui connaît le code. L'impact
est noté sur l'objectif « revenu d'appoint ». Le calendrier suit les deux fenêtres de saison.*

### Phase 0 — Gains rapides et validation (maintenant → mi-novembre 2026, fin de la saison d'automne)

| Action | AARRR | Effort | Impact | Critère de succès / d'arrêt |
|---|---|---|---|---|
| **Passer le dépôt GitHub en privé avant tout push**, remplacer la licence MIT par « tous droits réservés », mettre à jour README / `ATTRIBUTION.md` / `AGENTS.md` (doc 04 §9.1) | — | < 1 h | 🔥 Protège la stratégie et le code futur | Fait **avant** de pousser cette étude |
| **Conformité ODbL** : publier les couches dérivées d'OSM (lisière, eau, réseau d'accès) ou leur algorithme de dérivation, séparément du reste (doc 04 §9.2, option A) | — | ~½ j | Obligatoire dès qu'un produit est public | Page « Données OpenStreetMap » en ligne |
| **Validation GBIF / OpenObs** du score sur l'Isère (doc 04 §4) | Revenu (preuve) | ~2 j | 🔥 Élevé | Écart avec le hasard ≥ ~1,5 pour au moins le cèpe ou la girolle, sinon **re-calibrage avant toute vente** |
| **10 entretiens** de cueilleurs (expositions mycologiques d'octobre, sociétés de la FMBDS, groupes locaux) | Toutes étapes | ~10 h | 🔥 Élevé | Phrases exactes sur les douleurs, prix évoqués, et les 3 fonctions jugées indispensables |
| **Bêta fermée** de 15 à 30 testeurs recrutés pendant les entretiens (outil de recherche, pas un freemium) | Activation | ~1 j | Moyen | Un testeur sur deux revient après la pluie suivante |
| Volumes de recherche (Keyword Planner) : « champignons + massif » | Acquisition | ~2 h | Moyen | Volume par massif connu |
| Héberger localement Inter et Leaflet (RGPD) | — | < 1 h | Faible, mais sans regret | — |
| Page d'attente : promesse, inscription au bulletin, **pré-réservation fondateurs** | Acquisition | ~1–2 j | Élevé | ≥ 100 inscrits au bulletin avant février 2027 |

### Phase 1 — Construction du produit vendable (novembre 2026 → mars 2027, phase de développement intensif)

| Action | Effort | Impact | Raison |
|---|---|---|---|
| Déploiement de production minimal (PHP-FPM ou FrankenPHP, TLS, `prod`) | 2–3 j | Bloquant levé | Doc 04 §3.1 |
| Hébergement **scénario minimal** (§4.4) : un VPS (Hetzner CX23 ou OVH VPS-1), SQLite, tuiles et paquets hors-ligne sur R2 | inclus | ≈ 93 €/an | §4 |
| Météo : **ingestion Météo-France** (0 €, 3–5 j) **ou** Open-Meteo Standard (29 $/mois, ~½ j) — choisir selon le temps disponible | ½–5 j | Bloquant levé | Doc 04 §5.2, §4.3 |
| Fonds de carte : **extrait Protomaps auto-hébergé** (hors-ligne autorisé, attribution OSM) ; IGN en ligne si les conditions le permettent | 1–2 j | Bloquant levé | Doc 04 §5.3, §4.2 |
| **Habitat statique en tuiles + météo planifiée** par grille fixe | ~1 sem | Coût et charge ≈ constants | Indispensable pour tenir à moins de 15 h/sem |
| **PWA hors-ligne** par massif acheté | 1–2 sem | 🔥 Justifie le pass | Doc 04 §3.4 |
| **Mode simple + onboarding mobile d'abord** | 1–2 sem | 🔥 Conversion des novices | Doc 04 §6 |
| Couche sécurité (fiches confusions, règles, antipoison, sociétés) + CGU/CGV | 3–5 j (+ relecture) | Bloquant levé | Doc 04 §5.1 |
| Forêts publiques ONF + « marche estimée » + plafond de pente en mode novice | 2–3 j | Différenciant et sécurisant | Doc 04 §5.5–5.6 |
| Stripe Checkout + Portal, passes par zone, lien magique | 3–5 j | Bloquant levé | Doc 04 §3.2 |
| Extension aux **Alpes du Nord** complètes (Savoie, Haute-Savoie) | 3–5 j de calcul + vérifications | Multiplie le marché adressable | Doc 03 §3 |
| *Option* : remplacer OSM par la **BD TOPO** (routes, sentiers, eau) pour supprimer le partage à l'identique ODbL ; tester d'abord la complétude des sentiers | 1–2 sem | Données 100 % propriétaires | Doc 04 §9.2, option B |
| Tests de non-régression du score | 1–2 j | Sécurise les recalibrages | Doc 04 §7 |
| Ouverture des **100 passes fondateurs** (février–mars) | — | Premier revenu et vraie preuve d'achat | Critère d'arrêt ci-dessous |

**Critère d'arrêt de la phase 1** : **moins de 30 passes fondateurs vendus au 31 mars 2027**
(avec plus de 100 inscrits au bulletin) indique que la proposition ne prend pas. Revoir le prix,
l'offre ou le positionnement avant d'investir davantage.

### Phase 2 — Première saison payante (avril–mai 2027 : morilles)

- Petite saison (morilles : 78 observations GBIF en Isère, 52 en Haute-Savoie). C'est un **test
  grandeur nature** à faible enjeu.
- Mesurer : visites de la page → démo → pass ; remboursements ; usage hors-ligne ; ouverture des
  alertes.
- **Sondage Van Westendorp** auprès des inscrits au bulletin pour fixer le prix d'automne.

### Phase 3 — Saison principale (juin–novembre 2027)

- Bulletin de pousse **automatique** après chaque épisode déclenchant (le moteur `FlushClock`
  le détecte déjà) : rétention et permission sans travail manuel.
- Contenu saisonnier par massif (« Champignons en Chartreuse : où et quand ») : une page par
  massif et par espèce, rédigée une fois et mise à jour par les données.
- Présence aux expositions mycologiques d'automne et dans la presse locale (angle : « une carte
  qui publie sa précision »).
- Régime de croisière : **moins de 15 h/semaine**, surtout support et contenu.

### Phase 4 — Consolidation (2028 et après)

- **Un massif de plus par an**, choisi sur la densité d'observations : Jura et Doubs, puis
  Hautes-Pyrénées (doc 03 §3).
- Précalcul annuel scripté (janvier–février).
- Carte imprimée en vente pour la fin d'année.
- Options à réévaluer **uniquement si les chiffres le justifient** : application sur les
  stores (§7), offre pour accompagnateurs en montagne ou offices de tourisme, Suisse et Italie
  alpines.

### Ce que l'on ne fait pas, et pourquoi

| Idée | Raison |
|---|---|
| France entière | Incompatible avec moins de 15 h/semaine ; dilue l'avantage montagne ; marché encombré |
| Identification photo | Responsabilité ; fiabilité de 35 à 49 % ; défiance de l'Anses |
| Publicité payante | Budget non précisé ; saisonnalité ; coût d'acquisition inconnu |
| Communauté de partage de coins | Culture du secret (vandalisme en 2016) ; modération chronophage |
| Applis natives dès le départ | Double maintenance ; la PWA suffit pour valider |

## 6. Plan marketing allégé (`marketing-plan`, adapté à un solo sans budget)

| Étape AARRR | Actions | Indicateur avancé |
|---|---|---|
| **Acquisition** | Pages SEO par massif et espèce ; bulletin de pousse ; sociétés mycologiques (FMBDS) ; presse locale après un orage ; publication de la validation ; présence ponctuelle dans les groupes Facebook (selon leurs règles) | Inscrits au bulletin par semaine en saison |
| **Activation** | Secteur vitrine en mode simple ; premier bénéfice en moins de 60 s ; démo « pourquoi ici » | % de visiteurs qui ouvrent le détail d'une maille |
| **Rétention** | Alertes automatiques après orage ; rappel de renouvellement ; fiches saisonnières | Taux d'ouverture des alertes ; renouvellement d'une année sur l'autre |
| **Recommandation** | Pass cadeau ; carte imprimée offerte ; « partagez un secteur vitrine » | Part des achats issus d'un cadeau ou d'un lien |
| **Revenu** | Pass massif, Pass tous massifs, carte imprimée | Passes vendus par saison ; prix moyen ; taux de remboursement |

**Indicateur principal** : **nombre de passes actifs pendant la saison d'automne**.
**Décisions ouvertes liées au plan** : coût d'acquisition inconnu (pas de données) ; budget
non précisé.

## 7. Si l'on passe aux stores un jour (`aso`)

*À ne considérer qu'après une saison réussie en PWA. Grille ASO appliquée en prévision ;
aucune fiche n'existe encore.*

- **Google Play** : publier la PWA via une *Trusted Web Activity*, à moindre coût.
  **Apple** : un simple emballage web risque un refus au titre de la règle 4.2 (« fonctionnalité
  minimale ») ; prévoir des fonctions natives (hors-ligne, géolocalisation).
- **Titre (≤ 30 car.)** : marque + mot-clé, par exemple « [Nom] : carte champignons ».
  Sous-titre Apple (≤ 30) : « Prévision cèpes et girolles » (27 car.). Champ de mots-clés Apple
  (100 octets, sans répéter le titre) : `alpes,chartreuse,vercors,belledonne,savoie,morilles,cueillette,coins,pousse,randonnee`.
- **Captures** : les 3 premières disent tout. (1) « Où chercher cette semaine dans votre
  massif » ; (2) « Pourquoi ici : versant frais, hêtraie, sol neutre » ; (3) « Le chemin depuis
  la voiture, même hors réseau ».
- **Notes** : solliciter un avis après une sortie réussie (3 demandes par an maximum sur iOS) ;
  répondre à tous les avis négatifs, ce que Champignouf n'a pas fait en 2020.

## 8. Questions stratégiques encore ouvertes

*Réglées le 14/10/2026 : open source (**non**, tout reste propriétaire) ; estimations de coûts
récurrents (§4).*

1. **Scénario de coûts** : partir sur le **minimal (~93 €/an)**, l'**intermédiaire** (~390 à
   425 €/an avec Open-Meteo, moins de développement) ou le **confort** (~760 à 820 €/an) ?
   Recommandation : minimal, puis montée ligne par ligne.
2. **Relecture juridique** des CGU/CGV et de la lecture de l'ODbL : quel budget, ou une
   rédaction autonome à partir de modèles ?
3. **Durée de la phase initiale** : combien de semaines de développement intensif avant de
   passer sous 15 h/semaine ? La phase 1 représente environ 6 à 9 semaines.
4. **Promesse « identification »** : la limiter à de la **pédagogie et de la prévention**, **sans
   identification par photo** ?
5. **Statut juridique de vendeur** (micro-entreprise ou autre) : existe-t-il déjà ?
6. **Nom et marque** : garder « Myco Map » (générique, proche de Mycora et MycoDB) ou en chercher
   un distinctif ?
7. **Pré-vente** : d'accord pour encaisser des passes fondateurs avant la livraison complète
   (date de livraison annoncée, remboursement garanti) ?
8. **Données OSM** : se contenter de l'option A (publier les couches OSM dérivées) ou investir
   dans l'option B (BD TOPO, données entièrement propriétaires) ?
