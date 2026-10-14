# 05 — Recommandations et roadmap de monétisation

*14 octobre 2026. Skills appliqués : `product-marketing` (positionnement), `marketing-council`
(arbitrage), `pricing` et `offers` (packaging, offre), `marketing-plan` (AARRR, phasage,
critères d'arrêt), `aso` (si passage aux stores).*

## 0. Cadre fixé par le porteur

| Paramètre | Réponse (14/10/2026) | Conséquence de conception |
|---|---|---|
| Ambition à 2–3 ans | Revenu d'appoint (quelques centaines à quelques milliers d'€/an), sans levée de fonds ni recrutement | Viser **100 à 300 passes par an**, pas la France entière |
| Temps | **Développement intensif jusqu'à la saison des morilles (printemps 2027)**, puis **moins de 15 h/semaine** | Phase 1 (6 à 9 semaines de travail) logée de novembre 2026 à mars 2027 ; tout ce qui tourne en saison doit être **automatique** |
| Périmètre | **Prospection seule** : connaître les coins à champignons ; **aucune identification**, même pédagogique | Carte + calendrier de pousse + bonnes pratiques de cueillette ; avertissement « pas d'avis sur la comestibilité » (doc 04 §5.1) |
| Cible | B2C, zones riches en champignons, **accessible aux novices** | Simplicité de la carte et bonnes pratiques ; précision de montagne pour les confirmés |
| Modèle | **Payant d'abord**, gratuit très restreint ; **produit fini uniquement, pas de prévente** | Démo minimale ; lancement commercial quand le produit est complet (§5) |
| Open source | **Non** : code, modèles et données préparées propriétaires | Dépôt à passer en privé ; **option A** retenue pour l'ODbL (doc 04 §9) |
| Coûts | **Scénario minimal** au départ, montée ligne par ligne si besoin ; relecture juridique **non chiffrée** | §4 |
| Statut | **Micro-entreprise en création** (régime classique) | Franchise de TVA, cotisations sur le chiffre d'affaires, médiateur obligatoire (doc 04 §5.8) |
| Nom | **« Le Bon Versant »** retenu (« Myco Map » écarté) | Suites pratiques au §9 : domaines, marque, renommage du dépôt plus tard |
| Appli mobile | Le porteur la juge « un vrai plus, voire indispensable » (hors-ligne, habitudes des stores) ; **arbitrage du calendrier en attente** | Analyse et options au §10 ; question au §8 |

---

## 1. Positionnement (chaîne de Dunford, via `product-marketing`)

| Maillon | Contenu pour Le Bon Versant |
|---|---|
| **Alternatives réelles** | (1) Expérience et bouche-à-oreille ; (2) Géoportail (BD Forêt) + carte IGN, gratuits ; (3) indices gratuits (Champiscope, les-champignons.fr) ; (4) cartes payantes France entière (Mycora, Champi, Chasseurs de champignons) |
| **Attributs uniques** | Relief 5 m et canopée LIDAR HD à 50 m en montagne ; « pourquoi ici » par maille ; fenêtre de pousse à 14 jours par espèce ; itinéraire parking → zone avec temps de marche ; **validation publiée** (résultats chiffrés, pas le code, à produire) |
| **Valeur** | Moins de soirées de prospection, des secteurs nouveaux qu'on comprend, le bon jour pour y aller, un retour à la voiture sans se perdre, et ne pas cueillir là où c'est interdit |
| **Clients qui y tiennent le plus** | Cueilleurs des **massifs alpins** (S1), randonneurs-montagnards équipés (S3), et novices (S2) qui veulent une carte simple et les règles du jeu |
| **Catégorie** | **Côté recherche** : les mots des clients, « coins à champignons », « carte champignons » (SEO, stores). **Côté positionnement** : dans cette catégorie, *la carte de prospection des massifs de montagne*, et pas une promesse de « kilos » |
| **Style** | **Gros poisson dans une petite mare** : dominer quelques massifs, pas concurrencer Mycora sur la France |

**Promesse de travail** (à tester, pas un slogan définitif) :
*« Où et quand chercher dans votre massif cette semaine, expliqué maille par maille, avec le
chemin depuis la voiture. »*

**Messages de preuve** (ne les utiliser que lorsqu'ils sont vrais) : « X % des observations
GBIF de cèpes en Isère tombent dans les 10 % de mailles les mieux notées » ; « résiliation en
un clic, pas de renouvellement surprise ».

**Mots à éviter** (`offers`, vocabulaire banni) : « coins secrets », « kilos garantis »,
« révolutionnaire », « IA qui trouve les champignons », toute probabilité de trouver, et **tout
vocabulaire d'identification** (« reconnaître », « comestible », « sans risque »).

## 2. Conseil marketing (simulation)

> *Conseil simulé : chaque avis est construit à partir des cadres publiés de chaque conseiller,
> pas d'un avis réel de ces personnes sur ce projet.*

**Question posée** : comment faire payer quelques centaines de cueilleurs par an, en solo, sur
un marché encombré, avec une carte de prospection accessible aux novices et sans
identification ?
**Siègent** : April Dunford (positionnement), Seth Godin (plus petite audience viable),
Alex Hormozi (offre), et Byron Sharp, **contradicteur désigné**, qui se méfie de la
différenciation et de la niche.

**Dunford — positionnement contre les vraies alternatives.** Sa première question : que ferait
le client si Le Bon Versant n'existait pas ? Réponse : Géoportail le soir, ou Champi. Les attributs
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
empilée** : hors-ligne, itinéraire, alertes, calendrier de pousse, règles de cueillette.
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
   Ce qui trancherait : un sondage Van Westendorp auprès des inscrits au bulletin, puis la
   conversion réelle des premières semaines de vente (pas de prévente, choix du porteur).
3. **Permission ou vente directe** (Godin face au « payant d'abord »). Compromis : le bulletin
   gratuit est **éditorial** (au niveau du massif, sans carte détaillée). Il construit la
   permission sans transformer le produit en freemium.

**Synthèse du président**

- **À faire** : (1) publier la validation avant d'ouvrir les ventes ; (2) un bulletin de pousse par
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
| **Pass Saison — 1 massif** | 12 mois, toutes espèces, carte complète du massif, J+14, « pourquoi ici », itinéraires GPX/KMZ, **hors-ligne**, alertes après orage, calendrier de pousse par espèce, **bonnes pratiques et règles de cueillette**, couche forêts publiques | **19 €** (fourchette à tester : 15–25 €) | Métrique zone × saison (doc 03 §6.2) ; au-dessus de l'ancre Boletik, sous Champi et Chasseurs |
| **Pass Saison — Tous massifs** | Idem, sur tous les massifs couverts (Alpes du Nord, puis Jura…) | **29 €** (à tester) | Répond à la plainte « je suis à la frontière de deux zones » (10 % chez Chasseurs) ; permet de monter en gamme à mesure que la couverture s'étend |
| **Carte imprimée du massif** (achat unique, hors saison, **à partir de 2028**) | Carte A1 du potentiel d'habitat du massif, légende de prospection, règles de cueillette | À fixer entre 39 et 59 € (coût d'impression à la demande **non vérifié** ; vente de biens à un autre taux de cotisations, doc 04 §5.8) | Revenu de novembre à mars, cadeau de fin d'année ; Les Cartes Terroirs valide le format à 69,99 € |

**Pourquoi pas de paliers par fonctionnalité** : chaque palier supplémentaire, c'est du
support et des cas limites. À moins de 15 h/semaine, **une seule métrique (la zone)** est plus
simple à maintenir et à expliquer.

**Pourquoi pas de mensuel** : l'usage tient à quelques semaines par an (doc 03 §5). Un mensuel
pousse à résilier après la poussée ; c'est le problème vécu chez Chasseurs de champignons.

### 3.2 Les six composantes de l'offre (`offers`)

| Composante | Proposition |
|---|---|
| **Cœur** | Le Pass Saison du massif |
| **Bonus** (réels, pas gonflés) | Calendrier de pousse par espèce et par massif ; export GPX vers l'appli de randonnée de l'utilisateur ; règles de cueillette du département (quotas, propriété, arrêtés) ; guide des bonnes pratiques (prélèvement, respect du milieu, sécurité en montagne) |
| **Garantie** | **Remboursement intégral sous 14 jours, sans justification** ; **pas de renouvellement automatique par défaut** (rappel par e-mail, renouvellement en un clic). C'est le contre-pied direct des avis négatifs sur Chasseurs de champignons. *Conditions à relire juridiquement (droit de rétractation sur contenu numérique).* |
| **Urgence réelle** | **Pas de prévente ni de passes fondateurs** (choix du porteur). La seule urgence est **la saison elle-même** : le pass s'achète quand la pluie annonce une poussée, et le bulletin le rappelle. Pas de faux compte à rebours, pas de rareté inventée |
| **Nom** | **Le Bon Versant** — « Pass Saison Chartreuse », « Pass Saison Vercors »… (un pass par massif) ; « Pass Montagne » pour tous les massifs |
| **Prix et paiement** | Paiement unique annuel via Stripe Checkout ; Customer Portal pour factures et remboursements ; mention « TVA non applicable » tant que la franchise s'applique (micro-entreprise, doc 04 §5.8) |

### 3.3 Arbitrages assumés

| Option | Gain | Coût | Choix |
|---|---|---|---|
| Prix bas (≤ 10 €), comme Boletik | Conversion facile | Piège du 9 € ; course vers le bas ; ~200 passes pour 2 k€ | ❌ |
| Prix moyen (19–29 €) | Couvre les coûts avec peu d'acheteurs ; cohérent avec la valeur empilée | Exige une preuve (validation) | ✅ à tester |
| Abonnement mensuel | Revenu récurrent apparent | Inadapté à la saisonnalité ; résiliations ; support | ❌ |
| Freemium généreux | Audience | Contraire au choix du porteur ; coûts serveur et météo | ❌ |
| Appli hybride sur les stores (Capacitor) | Hors-ligne fiable sur iOS ; visibilité dans les stores ; habitude d'installation | −26 à −35 % de net par pass vendu dans l'appli, ~120 € de frais la 1ʳᵉ année, +3 à 5 semaines de travail, revue Apple | ⏸ à arbitrer (§10) : recommandé après une saison de mesure |
| B2B (offices de tourisme, accompagnateurs) | Revenus plus gros par client | Vente active, hors cible B2C | ⏸ option 2028+ |
| Identification (photo **ou pédagogique**) | Attente des novices | Responsabilité, 35–49 % de fiabilité en photo, marché saturé ; **hors périmètre par décision du porteur** | ❌ définitif |
| Prévente / passes fondateurs | Trésorerie et preuve d'achat avant la fin du développement | Engagement de livraison ; refusé par le porteur | ❌ |

### 3.4 Économie unitaire (micro-entreprise en franchise de TVA)

- **Stripe** : **1,5 % + 0,25 €** par carte de l'EEE, sans abonnement ; les frais ne sont pas
  rendus en cas de remboursement ([stripe.com/fr/pricing](https://stripe.com/fr/pricing),
  relevé du 14/10/2026).
- **Cotisations sociales** : **21,2 %** du prix encaissé (prestations de services BIC), plus
  ~0,2 % de formation professionnelle. Sources secondaires, **à confirmer sur urssaf.fr**. ACRE
  ignorée ici, par prudence.
- **TVA** : non facturée (franchise jusqu'à 37 500 €) ; le prix affiché est le prix encaissé.

| Produit | Prix | Stripe | Cotisations (~21,4 %) | **Net avant impôt** |
|---|---|---|---|---|
| Pass Saison — 1 massif | 19 € | 0,54 € | 4,07 € | **≈ 14,40 €** |
| Pass Saison — tous massifs | 29 € | 0,69 € | 6,21 € | **≈ 22,11 €** |
| Moyenne (mix) | 22 € | 0,58 € | 4,71 € | **≈ 16,71 €** |

L'impôt sur le revenu (barème, ou versement libératoire optionnel de 1,7 %) n'est pas déduit.
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
| **Stores** (si applis, §10) | — | Apple : **99 $/an** (99 € selon des sources françaises, non vérifié chez Apple) ; Google Play : **25 $ une fois** ; commissions de 10 à 15 % **sur le prix hors TVA**, la TVA étant collectée par le store | [aide Google Play](https://support.google.com/googleplay/android-developer/answer/113468), [Apple Newsroom](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/) ; détail au §10.4 |
| **Relecture juridique** (CGU/CGV, lecture de l'ODbL) | **Non chiffré** | **Non chiffré** | Pas de budget fixé par le porteur |
| **Médiateur de la consommation** (obligatoire en B2C) | **30 à 80 €/an** | Idem | Source commerciale, **non vérifié** ([portail-autoentrepreneur.fr](https://www.portail-autoentrepreneur.fr/academie/creation-auto-entreprise/mediation-consommation)) |
| **Cotisations sociales** (micro-entreprise) | ~21,4 % du chiffre d'affaires (déjà déduit dans le net par pass, §3.4) | Idem | Sources secondaires, à confirmer sur urssaf.fr |
| **TVA** | Franchise : rien à reverser, mais la TVA payée sur les dépenses n'est **pas récupérable** → coûts comptés TTC ci-dessous | Idem | Doc 04 §5.8 |
| **Dépôt de marque INPI** (ponctuel, pas récurrent) | ~190 € pour une classe, valable 10 ans | Idem (+40 € par classe) | Sources secondaires, à confirmer sur inpi.fr |
| **CFE, comptabilité, banque** | **Non instruit** | **Non instruit** | À vérifier à la création |

### 4.4 Deux scénarios annuels — **minimal retenu** au départ

| Ligne | **Coût minimal (retenu)** | **Confort** |
|---|---|---|
| Serveur | Hetzner CX23 + IPv4 : 71,88 € HT | Hetzner CX33 + IPv4 : 107,88 € HT |
| Sauvegardes | 20 % : 13,18 € HT | 20 % : 20,38 € HT |
| Base de données | SQLite : 0 € | SQLite : 0 € |
| Stockage et sortie | R2 gratuit (≤ 10 Go) : 0 € | R2 ~30 Go : ~3,60 $ |
| CDN | — | Bunny : ~12 à 15 $ |
| Fond de carte | Protomaps auto-hébergé : 0 € | Idem : 0 € |
| Météo | Météo-France ouvert : 0 € | Open-Meteo Standard : 348 $ |
| E-mails | Resend gratuit : 0 € | Resend Pro : 240 $ |
| Supervision | Gratuit : 0 € | UptimeRobot Solo : 108 € HT |
| Domaine | ~7,79 € HT (non vérifié) | ~7,79 € HT (non vérifié) |
| Médiateur de la consommation | 30 à 80 € (non vérifié) | 30 à 80 € (non vérifié) |
| Relecture juridique | Non chiffré | Non chiffré |
| **Total HT (hors médiateur)** | **≈ 93 €** | **≈ 244 € + ~606 $ ≈ 760 à 820 €** |
| **Total payé (TVA non récupérable + médiateur)** | **≈ 140 à 190 €/an** | **≈ 840 à 1 065 €/an** (selon la TVA appliquée par les fournisseurs hors UE) |
| **Passes à 19 € pour couvrir** (net ≈ 14,40 € après Stripe et cotisations) | **≈ 10 à 14 passes** | **≈ 58 à 74 passes** |

**Montée ligne par ligne** (décision du porteur) : la première ligne à ajouter, si l'ingestion
Météo-France s'avère trop coûteuse en temps, est **Open-Meteo Standard**. Le total passe alors
à **≈ 440 à 590 €/an**, soit **≈ 31 à 41 passes**. Ensuite viennent Resend Pro, si le bulletin
dépasse 100 envois par jour, puis la supervision payante.

**Ponctuel** : dépôt de marque INPI ~190 € (≈ 13 passes, une fois pour 10 ans).
**Non compris** : relecture juridique, impôt sur le revenu, CFE, temps passé, matériel, stores
(avec les deux stores : ≈ 260 à 315 € la première année, et 18 à 34 passes pour couvrir, §10.5).

### 4.5 Résultat selon les ventes (après Stripe et cotisations, avant impôt sur le revenu)

| Passes vendus par an | Net (Stripe + cotisations déduits) | − coût minimal (140–190 €) | − confort (840–1 065 €) |
|---|---|---|---|
| 50 (19 €) | ≈ 720 € | **≈ 530 à 580 €** | **≈ −120 à −345 €** (perte) |
| 150 (22 € en moyenne) | ≈ 2 507 € | **≈ 2 317 à 2 367 €** | **≈ 1 442 à 1 667 €** |
| 300 (22 € en moyenne) | ≈ 5 013 € | **≈ 4 823 à 4 873 €** | **≈ 3 948 à 4 173 €** |

**Lecture** : en scénario minimal, l'activité couvre ses coûts dès **une quinzaine de passes**.
Le confort fait perdre de l'argent sous ~60 passes et ne se justifie qu'au-delà d'une centaine
de passes par an, ou si le temps gagné vaut plus que ~700 €/an. Le revenu net reste dans la
fourchette « revenu d'appoint » visée (quelques centaines à quelques milliers d'euros).

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

### Calendrier d'ensemble

```
oct.–mi-nov. 2026   Phase 0  validation, entretiens, décisions (fin de saison d'automne)
mi-nov. 2026–fév. 2027  Phase 1  construction du produit fini (dev intensif, 6 à 9 semaines de travail)
mars 2027           Phase 1b bêta fermée gratuite du produit fini + mise en place légale et paiement
début avril 2027    LANCEMENT du produit fini (ouverture des ventes, saison des morilles)
avril–mai 2027      Phase 2  première saison payante, puis passage sous 15 h/semaine
juin–nov. 2027      Phase 3  saison principale
15 juin 2027        décision sur les applis hybrides (§10.7, option A)
2028+               Phase 4  un massif de plus par an
```

### Phase 0 — Validation et décisions (maintenant → mi-novembre 2026, fin de la saison d'automne)

| Action | AARRR | Effort | Impact | Critère de succès / d'arrêt |
|---|---|---|---|---|
| **Passer le dépôt de code en privé**, remplacer la licence MIT par « tous droits réservés », mettre à jour README / `ATTRIBUTION.md` / `AGENTS.md` (doc 04 §9.1). L'étude reste publiée volontairement sur GitHub Pages | — | < 1 h | 🔥 Protège le code futur | Dépôt de code privé |
| **Validation GBIF / OpenObs** du score sur l'Isère (doc 04 §4) | Revenu (preuve) | ~2 j | 🔥 Élevé | Écart avec le hasard ≥ ~1,5 pour au moins le cèpe ou la girolle, sinon **re-calibrage avant de construire la suite** |
| **10 entretiens** de cueilleurs (expositions mycologiques d'octobre, sociétés de la FMBDS, groupes locaux) | Toutes étapes | ~10 h | 🔥 Élevé | Phrases exactes sur les douleurs, prix évoqués, et les 3 fonctions jugées indispensables |
| **Le Bon Versant** : réserver **tout de suite** `lebonversant.fr` et `lebonversant.com` (+ variantes à tirets), puis recherche d'antériorité INPI (§9) | Acquisition | ~½ j | 🔥 Élevé (le nom est public via l'étude) | Domaines réservés ; aucune antériorité bloquante |
| Volumes de recherche (Keyword Planner) : « coins à champignons + massif » | Acquisition | ~2 h | Moyen | Volume par massif connu |
| Héberger localement Inter et Leaflet (RGPD) | — | < 1 h | Faible, mais sans regret | — |
| Page d'attente : promesse, **inscription au bulletin et à la liste de lancement, sans paiement** | Acquisition | ~1 j | Élevé | ≥ 100 inscrits avant le lancement d'avril 2027 |

### Phase 1 — Construction du produit fini (mi-novembre 2026 → fin février 2027, développement intensif)

Environ **15 semaines calendaires** pour **6 à 9 semaines de travail** estimées : la marge
absorbe les fêtes de fin d'année et les imprévus.

| Ordre | Action | Effort | Raison |
|---|---|---|---|
| 1 | Déploiement de production minimal (PHP-FPM ou FrankenPHP, TLS, `prod`) sur un VPS **scénario minimal** (Hetzner CX23 ou OVH VPS-1, SQLite, R2) | 2–3 j | Doc 04 §3.1, §4.4 |
| 2 | **Habitat statique en tuiles + météo planifiée** par grille fixe | ~1 sem | Coût et charge ≈ constants ; condition des moins de 15 h/semaine |
| 3 | Météo : **ingestion Météo-France** (0 €, 3–5 j). Repli : Open-Meteo Standard (29 $/mois, ~½ j) si l'ingestion déborde | ½–5 j | Doc 04 §5.2 |
| 4 | Fonds de carte : **extrait Protomaps auto-hébergé** (hors-ligne autorisé, attribution OSM) | 1–2 j | Doc 04 §5.3 |
| 5 | **PWA hors-ligne** par massif acheté ; stockage des paquets derrière une interface, pour réutiliser le code dans une coque Capacitor (§10.7) ; atténuations iOS (stockage persistant, état du paquet, repli GPX/KMZ) | 1–2 sem (+~1 j) | 🔥 Justifie le pass |
| 6 | **Mode simple + onboarding mobile d'abord** (« où chercher cette semaine ») ; nom **Le Bon Versant** dans l'interface, à la place de « Forage Mapper » et « Myco Map » | 1–2 sem | 🔥 Conversion des novices |
| 7 | Forêts publiques ONF + « marche estimée » + plafond de pente en mode novice ; **bonnes pratiques et règles de cueillette** ; avertissement « pas d'avis sur la comestibilité » | 3–4 j | Doc 04 §5.1, §5.5–5.6 |
| 8 | Calendrier de pousse par espèce et pages de prospection par massif (sans identification) | 2–3 j | Contenu du pass et SEO |
| 9 | Extension aux **Alpes du Nord** complètes (Savoie, Haute-Savoie), calcul en tâche de fond | 3–5 j | Doc 03 §3 |
| 10 | **Conformité ODbL, option A** : page de téléchargement des couches dérivées d'OSM, ou de leur algorithme | ~½ j | Doc 04 §9.2 |
| 11 | Stripe Checkout + Portal, passes par zone, lien magique | 3–5 j | Doc 04 §3.2 |
| 12 | Tests de non-régression du score | 1–2 j | Doc 04 §7 |

### Phase 1b — Bêta du produit fini et mise en route légale (mars 2027)

- **Bêta fermée gratuite** de 15 à 30 testeurs (recrutés en phase 0) sur le produit **complet**.
  C'est un test qualité, **pas une prévente** : aucun paiement.
- **Création de la micro-entreprise**, adhésion à un **médiateur de la consommation**, mentions
  légales, CGU/CGV (relecture juridique si un budget est dégagé), Stripe en mode réel.
- Dépôt de la marque **« Le Bon Versant »** à l'INPI (~190 € pour une classe, ~230 € pour deux, à confirmer), si la recherche d'antériorité est propre (§9).
- **Critère de passage au lancement** : aucun bug bloquant, et au moins la moitié des testeurs
  disent qu'ils paieraient le pass au prix annoncé.

### Lancement et Phase 2 — Première saison payante (avril–mai 2027 : morilles)

- **Ouverture des ventes du produit fini** début avril, annoncée au bulletin et à la liste de
  lancement. Aucune remise « fondateur ». Le prix affiché est le prix de la saison.
- Petite saison (morilles : 78 observations GBIF en Isère, 52 en Haute-Savoie). C'est un **test
  grandeur nature** à faible enjeu.
- Mesurer, pour la décision sur les applis au 15/06/2027 (§10.7) : part d'iOS parmi les
  acheteurs ; paquets hors-ligne disparus ; question « auriez-vous préféré une appli sur un
  store ? ».
- Mesurer : visites → secteur vitrine → pass ; remboursements ; usage hors-ligne ; ouverture des
  alertes.
- **Sondage Van Westendorp** auprès des inscrits pour confirmer le prix d'automne.
- **Fin du développement intensif** : passage au régime de **moins de 15 h/semaine**.
- **Critère d'arrêt** : **moins de 15 passes vendus au 31 mai 2027** (seuil de couverture du
  scénario minimal) **ou** conversion des inscrits inférieure à 2 % → revoir prix, offre ou
  positionnement avant l'automne.

### Phase 3 — Saison principale (juin–novembre 2027)

- Bulletin de pousse **automatique** après chaque épisode déclenchant (le moteur `FlushClock`
  le détecte déjà) : rétention et permission sans travail manuel.
- Contenu saisonnier par massif (« Champignons en Chartreuse : où et quand ») : une page par
  massif et par espèce, rédigée une fois et mise à jour par les données.
- Présence aux expositions mycologiques d'automne et dans la presse locale (angle : « une carte
  qui publie sa précision »).
- Régime de croisière : **moins de 15 h/semaine**, surtout support et contenu.
- **Critère de réussite** : **≥ 50 passes vendus au 30 novembre 2027**, soit environ 530 à 580 €
  net après coûts en scénario minimal : l'objectif « revenu d'appoint » est atteint. **Moins de
  20** → arrêter ou repositionner.

### Phase 4 — Consolidation (2028 et après)

- **Un massif de plus par an**, choisi sur la densité d'observations : Jura et Doubs, puis
  Hautes-Pyrénées (doc 03 §3).
- Précalcul annuel scripté (janvier–février).
- Carte imprimée en vente pour la fin d'année.
- **Applis hybrides Capacitor** (option A du §10.7) : si la décision du 15/06/2027 est
  positive, elles sont construites pendant l'hiver 2027–2028 et sortent pour les morilles de
  2028.
- Options à réévaluer **uniquement si les chiffres le justifient** : offre pour accompagnateurs en montagne ou offices de tourisme, Suisse et Italie
  alpines.

### Ce que l'on ne fait pas, et pourquoi

| Idée | Raison |
|---|---|
| France entière | Incompatible avec moins de 15 h/semaine ; dilue l'avantage montagne ; marché encombré |
| Identification (photo ou pédagogique) | Hors périmètre par décision du porteur ; responsabilité ; fiabilité de 35 à 49 % en photo |
| Prévente, passes fondateurs | Refusé par le porteur : on vend le produit fini |
| Migration OSM → BD TOPO | Option B écartée (option A retenue) ; à reconsidérer seulement si l'ODbL devient une gêne |
| Publicité payante | Budget non précisé ; saisonnalité ; coût d'acquisition inconnu |
| Communauté de partage de coins | Culture du secret (vandalisme en 2016) ; modération chronophage |
| Applis natives (Swift, Kotlin), React Native ou Flutter | Réécriture de l'interface Vue ; seul Capacitor garde une base web unique (§10.1) |
| Applis hybrides dès avril 2027 (option B) | Recommandation de l'étude, **sous réserve de l'arbitrage du porteur** (§8, point 4) : marge, calendrier, aucune preuve de marché encore (§10.7) |

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

*Calendrier : voir §10.7 (décision au 15/06/2027 dans l'option recommandée). Grille ASO
appliquée en prévision ; aucune fiche n'existe encore.*

- **Emballage** : une **coque Capacitor commune** à iOS et Android (§10.1). Une *Trusted Web
  Activity* suffirait pour Google Play, mais pas pour iOS, et le hors-ligne natif est justement
  l'argument sur iOS. **Apple** : un simple emballage web risque un refus au titre de la règle
  4.2 (« fonctionnalité minimale ») ; le hors-ligne par massif et la géolocalisation sont les
  fonctions natives à mettre en avant.
- **Achats** : dans l'appli, le pass passe par l'achat intégré du store, avec commission et
  TVA prélevées à la source (§10.4–10.5).
- **Titre (≤ 30 car.)** : marque + mot-clé, « Le Bon Versant : champignons » (28 car.).
  Sous-titre Apple (≤ 30) : « Prévision cèpes et girolles » (27 car.). Champ de mots-clés Apple
  (100 octets, sans répéter le titre) : `alpes,chartreuse,vercors,belledonne,savoie,morilles,cueillette,coins,pousse,randonnee`.
- **Captures** : les 3 premières disent tout. (1) « Où chercher cette semaine dans votre
  massif » ; (2) « Pourquoi ici : versant frais, hêtraie, sol neutre » ; (3) « Le chemin depuis
  la voiture, même hors réseau ».
- **Notes** : solliciter un avis après une sortie réussie (3 demandes par an maximum sur iOS) ;
  répondre à tous les avis négatifs, ce que Champignouf n'a pas fait en 2020.

## 8. Décisions prises et questions restantes

**Décidé le 14/10/2026** :

| Sujet | Décision |
|---|---|
| Open source | Non : tout reste propriétaire |
| Scénario de coûts | Minimal, montée ligne par ligne |
| Temps | Développement intensif jusqu'au printemps 2027, puis moins de 15 h/semaine |
| Identification | Supprimée du périmètre : prospection et bonnes pratiques uniquement |
| Statut | Micro-entreprise à créer (régime classique) |
| Nom | **Le Bon Versant** (« Myco Map » écarté) |
| Prévente | Non : lancement du produit fini |
| ODbL | Option A : publier les couches dérivées d'OSM |

**Restant ouvert** :

1. **Budget de relecture juridique** (CGU/CGV, lecture de l'ODbL) : non chiffré à ce jour.
2. **Classes de dépôt INPI** pour « Le Bon Versant » (§9) : à confirmer lors de la recherche
   d'antériorité.
3. **Moment du renommage du dépôt** `myco-map` (§9).
4. **Appli mobile : quel calendrier ?** (§10.7). L'intuition du porteur est fondée pour iOS
   (hors-ligne plus sûr en natif, usage normal des applis de terrain), mais une appli hybride
   coûte un quart à un tiers de la marge par pass vendu dans l'appli, ~120 € de frais la
   première année et 3 à 5 semaines de travail. **A** (recommandé) : PWA au lancement, code
   hors-ligne portable, décision au 15/06/2027 sur les mesures, applis pour 2028. **B** : applis
   dès avril 2027, en réduisant le périmètre de lancement ou en le décalant. **C** : applis
   construites pendant la saison 2027, pour l'automne.

## 9. Nom de marque : « Le Bon Versant » (retenu)

**Décision du porteur (14/10/2026)** : le produit s'appellera **Le Bon Versant**. `myco-map`
reste le nom de code du dépôt tant qu'il n'est pas renommé. **Aucun fichier ni dépôt n'a été
renommé.**

**Pourquoi ce nom tient** : il dit « montagne » et « le bon côté où chercher », ce qui
correspond au positionnement (§1). Il n'emprunte rien au vocabulaire des concurrents (Myco-,
Champi-, Cèpe-…). Il laisse la place aux mots-clés dans les titres : « Le Bon Versant :
champignons » fait 28 caractères (§7). Il nomme aussi naturellement les produits :
« Pass Saison Chartreuse », « Pass Montagne ».

### Suites pratiques

| # | Action | Quand | Coût | Statut au 14/10/2026 |
|---|---|---|---|---|
| 1 | **Réserver `lebonversant.fr` et `lebonversant.com`**, et idéalement `le-bon-versant.fr` et `le-bon-versant.com` (redirections). Urgent : l'étude publique révèle le nom | Immédiatement | ~quelques €/an par domaine (.fr ~7,79 € HT selon une source non officielle ; .com **non vérifié**) | **Non enregistrés** selon les registres (RDAP AFNIC et Verisign), revérifiés le 14/10/2026 pour les quatre variantes. Rien ne garantit qu'ils le restent |
| 2 | **Recherche d'antériorité** sur [data.inpi.fr](https://data.inpi.fr/) (et EUIPO pour information) : marques identiques ou proches dans les classes visées. Le rapprochement avec **« leboncoin »**, marque notoire, mérite un regard particulier ; aucune analyse juridique n'a été faite ici | Phase 0 | 0 € si on la fait soi-même | **Non faite** : base INPI non interrogeable depuis cette étude |
| 3 | **Dépôt de marque INPI** si la recherche est propre. Classes de Nice *envisageables* : **9** (application et logiciel téléchargeables) et **42** (logiciel en ligne, SaaS) ; d'autres selon la recherche. **À valider**, idéalement avec un conseil | Phase 1b (mars 2027), avant le lancement | ~190 € pour une classe, +40 € par classe supplémentaire, valable 10 ans (sources secondaires, à confirmer sur inpi.fr) | À faire |
| 4 | Nom dans le produit : `<title>`, en-tête, e-mails, mentions légales, CGV ; abandon de « Forage Mapper » et « Myco Map » | Phase 1 (ordre 6) | 0 € | À faire |
| 5 | Identités secondaires (adresse e-mail, comptes sur les réseaux utilisés) | Avec le domaine | 0 € | Non vérifié |
| 6 | **Renommer le dépôt git** (par exemple `le-bon-versant`) en même temps que son passage en privé ou plus tard, puis mettre à jour le remote local et les mentions dans README / `AGENTS.md`. Le site d'étude `myco-etude-marche` est un dépôt distinct, non concerné | Au choix du porteur | 0 € | **Non fait** (consigne : ne rien renommer) |

### Shortlist étudiée (pour mémoire)

**Méthode** : des noms français, distincts du paysage concurrentiel (Mycora, Champi,
Champiscope, Chasseurs de champignons, The Mycologist, Mapignon, Boletik, MycoDB, Sporecast,
Mushroom Map, Coins à champignons, Expert de Cueillette) et cohérents avec le positionnement
« prospection en montagne ».

- **Domaines** : statut d'enregistrement interrogé le 14/10/2026 sur les registres officiels,
  en RDAP (`rdap.nic.fr` pour .fr, `rdap.verisign.com` pour .com). « Non enregistré » signifie
  que le registre ne connaît pas le domaine ; cela ne garantit ni le prix ni l'absence de
  réservation entre-temps. Contrôle : `google.fr` répond « enregistré », un nom aléatoire
  répond « non enregistré ».
- **Usage existant** : recherche web sur le nom exact ; aucun usage commercial n'a été trouvé
  pour les candidats retenus.
- **Marque** : la base INPI et EUIPO n'a **pas** pu être interrogée → **« non vérifié »**
  partout. Une recherche d'antériorité sur data.inpi.fr est nécessaire avant tout dépôt.

| # | Nom | Connotation | Risque de confusion | .fr | .com | Marque INPI |
|---|---|---|---|---|---|---|
| 1 | **Le Bon Versant** | Montagne, « le bon côté » où chercher ; écho familier et positif | Faible avec les concurrents ; **clin d'œil à « leboncoin »** : légitime, mais à faire valider (marque notoire) | `lebonversant.fr` non enregistré | `lebonversant.com` non enregistré | Non vérifié |
| 2 | **La Bonne Pousse** | Timing de la poussée, vocabulaire de cueilleur | Faible ; « pousse » est aussi très utilisé en jardinage et alimentation (Pousse Pousse, Les Petites Pousses) | `labonnepousse.fr` non enregistré | `labonnepousse.com` non enregistré | Non vérifié |
| 3 | **Boletopo** | Bolet + topo : terrain, carte de relief | Faible ; centré sur les bolets alors que le produit couvre aussi trompettes, girolles et morilles | `boletopo.fr` non enregistré | `boletopo.com` non enregistré | Non vérifié |
| 4 | **Combe à Cèpes** | Terroir, combes humides des massifs ; poétique | Faible ; restreint au cèpe | `combeacepes.fr` non enregistré | `combeacepes.com` non enregistré | Non vérifié |
| 5 | **Cueilloir** | Mot français existant (outil pour cueillir) : simple, mémorisable | Faible avec les concurrents ; **nom commun**, donc marque potentiellement peu distinctive | `cueilloir.fr` non enregistré | `cueilloir.com` non enregistré | Non vérifié |
| 6 | **Fongitop** | « Fongi » (fonge) + « top » (topographie, ou « le top ») | Faible ; sonorité moins française | `fongitop.fr` non enregistré | `fongitop.com` non enregistré | Non vérifié |
| 7 | **Trouvecèpes** | Direct, très SEO (« cèpes ») | Faible ; mais **promesse de résultat** contraire au vocabulaire honnête retenu (§1), et restreint au cèpe | `trouvecepes.fr` non enregistré | `trouvecepes.com` non enregistré | Non vérifié |
| 8 | **Sylvacoin** | Sylve (forêt) + coin | Faible avec les concurrents ; **« coin » se lit « crypto-monnaie » en anglais** | `sylvacoin.fr` non enregistré | `sylvacoin.com` non enregistré | Non vérifié |

**Écartés au filtre des domaines** (les deux extensions déjà enregistrées) : *Versant*,
*Versant Nord*, *Poussée*, *Sporée*, *Combe*, *Humus*, *Litière*, *Mousseron*, *Fongeo*,
*Cépéo*, *Prospecteur*. *Sous-Bois* a son .fr libre mais son .com pris.
**Écarté au filtre de la confusion** : *MycoTopo* (domaines libres, mais le préfixe « Myco »
rapproche de Mycora et MycoDB, et du nom déjà écarté).

**Recommandation qui avait été faite** (suivie par le porteur) : **Le Bon Versant** en premier choix. Il incarne le
positionnement montagne, se retient, n'emprunte rien aux concurrents, et laisse la place aux
mots-clés dans les titres (titre de store en 28 caractères : « Le Bon Versant : champignons »). Second choix : **La
Bonne Pousse**, qui parle du timing, l'autre moitié de la promesse. **Le choix final revient au
porteur** ; il a choisi **Le Bon Versant** le 14/10/2026.

## 10. Application mobile : PWA d'abord, ou application hybride ?

*Analyse demandée par le porteur le 14/10/2026. Son intuition : une vraie application mobile est
un vrai plus, voire indispensable, pour deux raisons : (1) le **hors-ligne natif**, parce que
le réseau manque souvent en montagne ; (2) les **usages**, parce que le public a l'habitude
d'installer une appli depuis l'App Store ou le Play Store, pas une PWA. Il envisage une appli
**hybride** pour garder une base web unique. Sources consultées le 14/10/2026 ; « non vérifié »
quand aucune source fiable n'a été trouvée. Les efforts sont des **estimations de l'étude**,
pas des chiffres sourcés.*

### 10.1 Verdict sur l'intuition

| Argument | Verdict | Pourquoi |
|---|---|---|
| **Hors-ligne fiable** | ✅ **Fondé sur iOS** ; ⚠️ **peu fondé sur Android** | Sur iOS, rien ne garantit qu'une PWA garde ses données : WebKit accorde le stockage persistant « selon des heuristiques » et ne dit nulle part que les applis web de l'écran d'accueil échappent à l'éviction. Une appli native range ses fichiers dans un dossier que le système ne purge pas (détail au §10.2). Sur Android, Chrome donne jusqu'à 60 % du disque par origine, et les données persistantes ne sont effacées que par l'utilisateur |
| **Habitude des stores** | ⚠️ **Plausible, non mesurée** | Aucune étude indépendante ne donne de taux d'installation des PWA (seulement des chiffres de vendeurs). Les applis de terrain de référence sont natives : Komoot, Visorando, Cartes IGN, OsmAnd, Champi. Mais dans cette niche, l'acteur à la plus grosse audience, Chasseurs de champignons, est **web seulement**, comme Mycora et The Mycologist. Champi, natif et hors-ligne, n'affiche que « 500+ » installations Android (non vérifié) |
| **Hybride = base web unique** | ✅ **Seulement avec Capacitor** | Le frontend est en Vue 3. Capacitor embarque l'appli web telle quelle (« peut être ajouté à tout projet JavaScript moderne », [capacitorjs.com](https://capacitorjs.com/docs), v8). React Native et Flutter imposent de **réécrire l'interface** (~3 200 lignes, doc 01) : ce n'est plus une base web unique |
| **« Indispensable dès le lancement »** | ❌ **Non démontré**, et coûteux | Commissions et TVA prélevées par les stores (−26 à −35 % de net par pass vendu dans l'appli), ~120 € de frais la première année, 3 à 5 semaines de travail en plus dans une phase 1 sans marge (§10.5–10.6) |

**En résumé** : l'intuition est juste sur le fond pour iOS. Le hors-ligne natif y est plus sûr,
et c'est l'usage normal des applis de terrain. Elle n'est pas démontrée pour le lancement : la
moitié Android (environ 64 % du trafic mobile en France) est bien servie par une PWA. Le
prototype exporte déjà le GPX et le KMZ vers des applis natives (Iphigénie, OsmAnd, Locus),
ce qui offre un repli hors-ligne. Surtout, un achat dans une appli iOS ou Android passe par les
stores, ce qui coûte de la marge.

### 10.2 PWA ou appli native : faits vérifiés

| Critère | PWA (web installé) | Appli hybride Capacitor (stores) | Sources |
|---|---|---|---|
| **Installation** | Android : Chrome propose l'installation. iOS : **pas d'invite** ; il faut passer par Partager puis « Sur l'écran d'accueil ». Depuis iOS 26, tout site ajouté à l'écran d'accueil s'ouvre en mode appli par défaut | Recherche et installation dans le store, geste familier | [Chrome Developers](https://developer.chrome.google.cn/blog/pwa-install-features), [heise (iOS 26)](https://heise.de/-10749652) |
| **Taux d'installation réel** | **Non disponible** : seuls des chiffres de vendeurs circulent (par exemple « ~85 % », auto-déclaré). Google rapporte des hausses relatives, pas de taux absolu | Taux de conversion des fiches store dans cette niche : **non disponible** (aucun outil ASO connecté) | [PWA Stats](https://www.pwastats.com/tags/home-screen), [add-to-homescreen](https://github.com/philfung/add-to-homescreen) |
| **Quota de stockage** | Chrome : jusqu'à 60 % du disque par origine. Safari 17+ : jusqu'à ~60 % par origine dans le navigateur ; une appli de l'écran d'accueil a le même quota | Pas de quota web : fichiers de l'appli | [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria), [WebKit, 2023](https://webkit.org/blog/14403/updates-to-storage-policy/) |
| **Éviction (le vrai risque)** | Stockage « au mieux » : effacé en bloc sous pression de stockage. Safari efface aussi les données écrites par script après **7 jours d'usage du navigateur sans interaction** avec le site. Pour les applis de l'écran d'accueil, Apple a seulement dit en 2020 qu'elles ont leur propre compteur ; aucune exemption n'est documentée. Le stockage persistant (`navigator.storage.persist()`) est accordé sur iOS selon des heuristiques, dont le fait d'être installé | Dossier *Application Support* : sauvegardé et **non purgé** par le système (seul *Caches* l'est) | [MDN](https://developer.mozilla.org/en-US/docs/Web/API/Storage_API/Storage_quotas_and_eviction_criteria), [WebKit](https://webkit.org/blog/14403/updates-to-storage-policy/), [Apple WWDC 2017](https://developer.apple.com/videos/play/fall2017/204), [WebKit bug 237350](https://bugs.webkit.org/show_bug.cgi?id=237350) |
| **Stabilité de la plateforme** | En 2024, Apple a retiré les applis web de l'écran d'accueil dans l'UE (bêta d'iOS 17.4), puis a fait marche arrière | Dépend des règles des stores (revue, commissions) | [Engadget](https://www.engadget.com/apple-backtracks-on-plans-to-get-rid-of-web-apps-on-iphones-in-the-eu-195232177.html) |
| **Notifications** | Web Push sur iOS 16.4 et plus, **seulement pour les applis de l'écran d'accueil**, avec une permission demandée après un geste de l'utilisateur | Notifications natives | [WebKit](https://webkit.org/blog/13878/web-push-for-web-apps-on-ios-and-ipados/) |
| **Performance** | Leaflet dans le navigateur | Même moteur web, dans une WebView | **Non mesuré** ; pas d'écart déterminant attendu pour une carte Leaflet |
| **Paiement** | **Stripe**, aucune commission de plateforme, franchise de TVA | **Achat intégré obligatoire** pour débloquer du contenu (Apple 3.1.1). Une appli qui donne accès à des achats faits sur le web doit **aussi** les proposer en achat intégré (3.1.3(b)). L'exception « compagnon gratuit » (3.1.3(f)) vise des exemples comme la VoIP ou le stockage en ligne, et des développeurs SaaS rapportent des refus | [App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/), [forum Apple 811018](https://developer.apple.com/forums/thread/811018) |
| **Mises à jour** | Immédiates, sans revue | Revue Apple à chaque version ; cible Android à relever chaque année (API 36 exigée au 31/08/2026 pour les nouvelles applis et mises à jour) | [Google Play, cible d'API](https://developer.android.com/google/play/requirements/target-sdk) |
| **Visibilité** | SEO : le canal déjà prévu (§6) | ASO : volumes de recherche **non disponibles** | — |

**Parts de marché** : en France, Android pèse **~64 %** du trafic web mobile et iOS **~36 %**
(StatCounter, août 2026 ; c'est une mesure de trafic, pas de parc,
[gs.statcounter.com](https://gs.statcounter.com/os-market-share/mobile/france/)). Le point
faible de la PWA concerne donc environ un tiers des utilisateurs.

### 10.3 Le hors-ligne chez les applis de terrain

| Appli | Plateforme | Hors-ligne | Prix | Source |
|---|---|---|---|---|
| **Komoot** | iOS, Android | Cartes **par région**, téléchargées dans l'appli seulement, en Wi-Fi conseillé ; itinéraires téléchargeables un par un | Régions à l'unité, ou monde entier avec Premium (prix non relevés) | [aide Komoot](https://support.komoot.com/hc/articles/10356476920986) |
| **Visorando** | iOS, Android, web | Cartes topographiques IGN 1:25 000 et satellite **accessibles hors ligne sur mobile**, avec Premium ; itinéraire téléchargé avant de partir | **6 €/mois ou 25 €/an** ; essai de 3 jours | [visorando.com/premium](https://visorando.com/premium.html) |
| **Cartes IGN** (appli officielle de l'IGN, lancée en mai 2024) | iOS, Android, **pas de version ordinateur** | Téléchargement de cartes pour un usage hors connexion, **sauf certains fonds soumis à des droits** | Gratuit | [dossier de presse IGN](https://www.ign.fr/files/default/2024-05/DP-APPLI-CARTES-IGN-MAI-2024.pdf), [Presse-citron](https://www.presse-citron.net/telecharger/geographie-et-voyage/cartographie-geolocalisation/cartes-ign.html) |
| **OsmAnd** | iOS, Android | **Cartes vectorielles par pays ou région**. Version gratuite : 7 téléchargements sur Android (5 sur iOS), mises à jour comprises. Rhône-Alpes : ~860 Mo (forum non daté, **non vérifié**) | Payant pour l'illimité | [docs OsmAnd](https://docs.osmand.net/docs/user/purchases/android), [forum Suunto](https://forum.suunto.com/topic/11208/size-of-maps) |
| **Champi** | iOS, Android | **Zones téléchargées** | 9,99 €/mois ; 149,99 € pour 5 ans par région (doc 02 §2.2) | Doc 02 |
| **Iphigénie** | iOS | Fonds IGN hors-ligne | 24,99 €/an | Doc 02 |
| Mycora, The Mycologist, Chasseurs de champignons | **Web seulement** | Non observé | Doc 02 | Doc 02 ; [chasseursdechampignons.com](https://www.chasseursdechampignons.com/) |

« **Champignons Net** » et « **IGN La Clé des champs** » : **aucune appli trouvée sous ces
noms**. L'appli officielle de l'IGN s'appelle **Cartes IGN** ; l'ONF publie **Clés de forêt**,
une appli naturaliste. Si le porteur pensait à une autre appli, il faut son nom exact sur le
store.

**Ce qu'il faut en retenir** :

1. Le modèle du secteur, ce sont des **paquets par région ou par massif**, téléchargés
   volontairement avant la sortie. C'est exactement le « massif acheté » prévu (doc 04 §3.4).
2. Les fonds de carte publics **ne se pré-téléchargent pas librement** : la politique des tuiles
   OSM interdit le téléchargement en masse et renvoie vers l'auto-hébergement
   ([OSMF](https://operations.osmfoundation.org/policies/tiles/),
   [tuiles vectorielles](https://operations.osmfoundation.org/policies/vector/)). Pour la
   Géoplateforme IGN, les conditions du hors-ligne restent **non vérifiées** : la page d'aide ne
   donne que la licence Etalab du site
   ([cartes.gouv.fr](https://cartes.gouv.fr/aide/fr/guides-utilisateur/utiliser-les-services-de-la-geoplateforme/diffusion/)).
   L'**extrait Protomaps auto-hébergé** (PMTiles), déjà retenu (§4.2), vaut donc **pour la
   PWA comme pour l'appli**. Ce travail est commun aux deux voies.
3. **Taille du paquet** : à mesurer. L'hypothèse du §4.1 (100 à 200 Mo par massif) reste dans
   l'ordre de grandeur des cartes régionales d'OsmAnd. Aucune des deux voies n'est bloquée par
   la taille.

### 10.4 Coûts fixes et contraintes de publication

| Poste | Montant ou règle | Source |
|---|---|---|
| Apple Developer Program | **99 $/an** ; **99 €** selon des sources françaises (prix 2026 en euros **non vérifié** sur la page d'Apple). Pas d'exonération pour un particulier ou une entreprise individuelle | [iPhonesoft](https://iphonesoft.fr/2021/04/09/app-apple-developer-payer-compte-developpeur-france), [AppleInsider](https://appleinsider.com/articles/20/02/03/apple-extends-developer-program-fee-waivers-to-8-countries) |
| Google Play Console | **25 $ une fois** | [aide Google Play](https://support.google.com/googleplay/android-developer/answer/113468) |
| Commission Apple (UE, depuis le 01/10/2026) | Achat intégré : **15 %** pour le Small Business Program, 26 % sinon. Paiement alternatif ou lien vers le site : **10 %** pour le Small Business Program (20 % ou 15 % sinon) | [Apple Newsroom, 08/2026](https://www.apple.com/newsroom/2026/08/apple-announces-changes-for-apps-in-the-european-union/) |
| Commission Google (EEE, depuis le 30/06/2026) | **10 %** sur le premier million de dollars, **+ 5 % de frais de facturation** avec Google Play Billing ; pas de frais de facturation pour les liens web externes. La grille officielle est mal lisible : **à confirmer dans la console** | [aide Google Play](https://support.google.com/googleplay/android-developer/answer/112622?hl=en), [PocketGamer.biz](https://www.pocketgamer.biz/google-play-expands-billing-options-and-lowers-fees-for-developers/) |
| TVA | Apple et Google sont **vendeurs réputés** : ils collectent la TVA (20 % en France) et calculent la commission **sur le prix hors TVA**. La franchise de TVA de la micro-entreprise **ne protège plus** le prix public | [RevenueCat](https://www.revenuecat.com/docs/taxes-and-commissions), [Appfigures](https://appfigures.com/support/kb/616/how-vat-is-handled-by-apple-and-google-play) |
| Compte Google personnel | Créé après le 13/11/2023 : **test fermé avec 12 testeurs pendant 14 jours** avant toute mise en production | [aide Google Play](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en-GB) |
| Statut de commerçant (DSA) | Toute appli payante dans l'UE affiche les coordonnées du vendeur. Pour un particulier : **adresse (ou boîte postale)**, téléphone et e-mail, **publics** sur la fiche. Une domiciliation est à prévoir | [9to5Mac](https://9to5mac.com/2024/10/17/developers-address-phone-number-eu-app-store) |
| Remboursements | Sur iOS, le remboursement d'un achat intégré se demande **à Apple**. La garantie « remboursé sous 14 jours » (§3.2) ne dépend alors plus du porteur | Règles Apple ; **détail à vérifier** |
| Revue Apple | Une interface qui ne fait qu'emballer un site risque un refus (règle 4.2). Le hors-ligne par massif et la géolocalisation sont des arguments | [App Review Guidelines 4.2](https://developer.apple.com/app-store/review/guidelines/) |

### 10.5 Économie unitaire : un pass à 19 € selon le canal

*Hypothèses : prix public de 19 € TTC partout ; cotisations ~21,4 % (§3.4) ; commissions
Small Business Program. L'**assiette des cotisations** pour une vente via un store
(reversement net ou prix public) est **à valider** avec l'URSSAF ou un comptable, d'où une
fourchette.*

| Canal | Calcul | **Net avant impôt** | Écart avec le web |
|---|---|---|---|
| **Web (Stripe)**, franchise de TVA | 19 − 0,54 (Stripe) − 4,07 (cotisations) | **≈ 14,40 €** | — |
| **Achat intégré Apple** (UE, 15 %) | 19 ÷ 1,20 = 15,83 HT ; −15 % → 13,46 € reversés ; − cotisations (2,88 à 4,07) | **≈ 9,40 à 10,60 €** | **−26 à −35 %** |
| **Google Play Billing** (10 % + 5 %) | Même calcul | **≈ 9,40 à 10,60 €** | **−26 à −35 %** |
| Lien depuis l'appli iOS vers le site (UE, 10 %) | 19 − 0,54 − 1,90 (base de la commission **non vérifiée**) − 4,07 | **≈ 12,50 €** | −13 % ; demande une autorisation d'Apple et des déclarations |

**Coûts fixes avec les deux stores** : scénario minimal (140 à 190 €) + Apple (99 €) + Google
(25 $, environ 21 à 24 €) ≈ **260 à 315 € la première année**, puis ≈ 240 à 290 €/an.
**Seuil de couverture** : **18 à 22 passes** si tout est vendu sur le web ; **25 à 34 passes**
si tout est vendu dans les applis. C'est **environ le double** du seuil actuel (10 à 14
passes, §4.4), et plus que le critère d'arrêt de la phase 2 (15 passes au 31/05/2027).

### 10.6 Charge de travail pour un développeur seul

| Lot | PWA seule | En plus pour Capacitor (iOS + Android) |
|---|---|---|
| Paquet hors-ligne par massif (fond Protomaps + tuiles d'habitat + projection J+14 figée) | 1–2 sem (déjà dans la phase 1, ordre 5) | Réutilisé |
| Coque Capacitor, stockage natif des paquets, permissions de géolocalisation | — | 3–5 j |
| Achats intégrés Apple et Google, validation côté serveur, restauration, lien entre le compte web et le compte appli | — | 1–2 sem |
| Fiches des stores, captures, déclarations de confidentialité, statut de commerçant | — | 2–3 j |
| Test fermé Google (12 testeurs × 14 jours) | — | Calendaire ; peut se caler sur la bêta de mars (phase 1b) |
| **Total au lancement** | Prévu | **+3 à 5 semaines de travail** |
| **Entretien annuel** | Mises à jour web | +2 à 5 j/an (cible Android, SDK iOS, versions majeures de Capacitor) + revue Apple à chaque version + support des achats dans les stores |

**Le point de calendrier** : la phase 1 compte déjà 6 à 9 semaines de travail sur ~15 semaines
calendaires. Avec 3 à 5 semaines de plus, on arrive à 9 à 14 semaines : **la marge disparaît**
et le lancement d'avril est menacé. Après le lancement, le porteur passe sous 15 h/semaine, dont
5 à 10 h de fonctionnement en saison (§4.6). Les mêmes 3 à 5 semaines prendraient alors **2 à
4 mois de calendrier**. Reporter l'appli n'est donc pas gratuit. La période creuse de l'hiver
2027–2028 est le meilleur créneau pour la construire, avec une sortie pour les morilles de 2028.

### 10.7 Trois options

| | **A. PWA au lancement, décision sur données (recommandé)** | **B. Applis hybrides dès avril 2027** | **C. Applis hybrides pour l'automne 2027** |
|---|---|---|---|
| Lancement d'avril 2027 | Web + PWA, Stripe | Web + PWA + iOS + Android | Web + PWA |
| Applis | Décision au **15/06/2027** ; construites pendant l'hiver 2027–2028 ; sorties pour les morilles de 2028 | Dès le lancement | Construites de mai à août 2027, pendant la saison |
| Phase 1 | Inchangée, plus ~1 j pour rendre le hors-ligne **portable** (stockage derrière une interface, pour réutiliser le code dans Capacitor) | +3 à 5 sem : il faut **réduire le périmètre** (garder l'emprise actuelle au lieu des Alpes du Nord, ordre 9 ; reporter les pages calendrier, ordre 8) **ou décaler** le lancement | Inchangée |
| Hors-ligne iOS au lancement | Au mieux (stockage persistant demandé, état du paquet affiché, repli GPX/KMZ) | Fiable | Au mieux, puis fiable à l'automne |
| Marge par pass | 14,40 € | 9,40 à 14,40 € selon le canal | Idem que B à partir de l'automne |
| Seuil de couverture | 10 à 14 passes | 18 à 34 passes | 18 à 34 passes à partir de l'automne |
| Risque principal | Perdre des acheteurs iOS qui exigent une appli | Lancement retardé ou amputé ; double maintenance avant toute preuve de marché | Charge de travail en pleine saison, au-delà de 15 h/semaine |

**Recommandation : option A.**

1. La PWA couvre bien Android (~64 % du trafic).
2. Le repli GPX/KMZ vers des applis natives existe déjà.
3. Les stores coûtent un quart à un tiers de la marge, et doublent le seuil de couverture.
4. La phase 1 n'a pas de marge.
5. L'argument des « usages » n'est pas mesuré ; la saison des morilles 2027 le mesurera.

On accepte de prendre l'intuition du porteur au sérieux. Le code hors-ligne est donc rendu
portable dès la phase 1, et les applis ne sont qu'une coque à ajouter.

**Atténuations iOS au lancement (option A)** :

- appeler `navigator.storage.persist()` après l'installation ;
- afficher l'état du paquet à chaque ouverture (« Chartreuse disponible hors réseau, mis à jour
  le … ») et prévenir quand un paquet attendu a disparu ;
- rappel « vérifiez votre massif avant de partir » dans le bulletin ;
- export GPX/KMZ mis en avant comme filet de sécurité ;
- guide d'installation iOS en deux écrans.

**Mesures en phase 2, pour décider au 15/06/2027** :

- part d'iOS parmi les acheteurs ;
- paquets disparus (éviction détectée au lancement de la PWA, signal anonyme) ;
- demandes au support liées au hors-ligne ;
- question à l'achat et dans le sondage Van Westendorp : « auriez-vous préféré une appli sur
  l'App Store ou le Play Store ? ».

**Règle de décision proposée** : construire les applis si le critère de la phase 2 est atteint
(au moins 15 passes) **et** si au moins un des signaux suivants apparaît :

- des paquets disparus chez au moins 5 % des utilisateurs iOS actifs ;
- au moins 20 % des répondants qui demandent une appli ;
- des plaintes récurrentes sur le hors-ligne.

Ces seuils sont des propositions, à ajuster par le porteur.

**Arbitrage à faire par le porteur** : c'est un vrai choix stratégique. Il oppose la fiabilité
du hors-ligne sur iOS et la présence dans les stores, d'un côté, à la marge, au calendrier de
lancement et à la charge de maintenance, de l'autre. La question est posée au §8 (point 4).
