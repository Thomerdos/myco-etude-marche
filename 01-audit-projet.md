# 01 — Audit du projet myco-map

*État au 14 octobre 2026, commit `44fd865`. **myco-map** est le nom de code du dépôt ; le nom
commercial retenu pour le produit est **Le Bon Versant** (décision du 14/10/2026, doc 05 §9). Audit factuel : ce qui marche, ce qui est esquissé,
ce qui manque. Les jugements de valeur sont réservés au document 04.*

## 1. Fiche d'identité

| Élément | Constat |
|---|---|
| Nature | Application web de **cartographie du potentiel mycologique** (habitat + météo), pas d'identification de champignons |
| Emprise | **Une seule zone** : Grenoble — Chartreuse, Belledonne, Vercors (44,72–45,45 N / 5,38–6,30 E ≈ 5 800 km²) |
| Grille | 50 m, **2 349 750 mailles** (1 446 × 1 625) précalculées en SQLite (~150 Mo, 205 Mo pour la base locale enrichie) |
| Espèces | 6 : cèpe, trompette de la mort, chanterelles, girolle, pied de mouton, morille |
| Historique | 54 commits, du 23 au 27 août 2026 (+ base locale du 28 août) ; aucun commit depuis 7 semaines |
| Taille du code | Backend PHP : 84 fichiers / ~9 500 lignes ; frontend Vue/TS : ~3 200 lignes ; 13 scripts Python/shell : ~2 400 lignes |
| Dépôt | GitHub public `Thomerdos/myco-map`, 0 étoile, 0 fork, code **MIT**, base précalculée **ODbL** |
| Utilisateurs | Aucun (pas de déploiement public, pas d'analytics) |
| Revenus | Aucun |

## 2. Architecture

- **Backend** Symfony 7.4 / PHP 8.4, découpage DDD strict (`Domain` sans dépendance framework,
  `Application` = cas d'usage, `Infrastructure` = adaptateurs). Ports du domaine câblés dans
  `backend/config/services.yaml` (`ElevationSampler`, `LandCoverSource`, `GeologySource`,
  `CanopyCoverSource`, `CanopyHeightSource`, `CanopyGapSource`, `SoilPhSource`, `WeatherSource`,
  `TerrainCellStore`, `SpeciesCatalog`).
- **Frontend** Vue 3 + Vite + Leaflet, TypeScript strict, UnoCSS, `@vuetify/v0`, police Inter
  (chargée depuis Google Fonts), CSS Leaflet chargé depuis unpkg.
- **Données** : précalcul lourd et manuel (`./dev.sh precompute`) vers SQLite ; météo à la volée
  (Open-Meteo, cache 2 h).
- **Exécution** : Docker Compose uniquement ; le backend tourne avec le **serveur PHP intégré**
  (`php -S 0.0.0.0:8765`), `APP_ENV=dev`, `APP_DEBUG=1` dans `docker-compose.yml`.
- **CI** GitHub Actions : lint du conteneur Symfony + YAML, restauration de la base (≥ 500 000
  mailles), `vue-tsc` + build frontend. **Aucun test unitaire ou fonctionnel** (`backend/tests`
  n'existe pas).

## 3. Inventaire fonctionnel

### 3.1 Ce qui marche (implémenté et branché)

| Fonction | Détail | Où |
|---|---|---|
| Score de potentiel par maille | Somme pondérée de 9 critères + plafonds (hors forêt 18, hors saison 38, incubation 48/62) | `SuitabilityCalculator`, `Criterion` |
| Deux modes | « Chance de trouver » (météo + habitat) et « Potentiel d'habitat » (terrain seul, poids renormalisés) | `ScoringMode` |
| Projection 14 jours | Barre J+0…J+14 avec score par jour sur la vue | `ProjectScoreHorizon` (`HORIZON_DAYS = 14`) |
| Phénologie de pousse | Épisode déclenchant ≥ 15 mm, délais par espèce, assèchement post-orage, amorçage par sécheresse | `FlushClock`, `WeatherConditions` |
| Météo | Grille 13×13 Open-Meteo `meteofrance_seamless` (AROME/ARPEGE), 31 j d'historique | `OpenMeteoWeather` |
| 11 masques | potentiel, altitude, exposition, pente, couvert, densité, pH/substrat, humidité topo, lisière, apport en eau, accès | `MapLayer` |
| Détail au clic | Décomposition du score par critère, terrain, explication en français, calendrier de pousse | `InspectLocation`, `DetailPanel.vue` |
| Accès | Dijkstra le long du réseau OSM depuis route carrossable / parking (2 km) + 500 m d'approche, pente > 40° bloquée ; temps à 4 km/h ; GPX d'itinéraire | `PathNetworkAccess`, `TraceAccessWalk` |
| Secteurs ≥ 90 | Repères des meilleurs secteurs, espacés | `RenderLayerGrid` |
| Export GPS | KMZ (masque PNG + points) et GPX générés **dans le navigateur** | `gpsExport.ts`, `zipStore.ts` |
| Filtre accessibilité | Masquer les mailles hors budget de marche | `accessible=` |
| Fonds de carte | Plan OSM, OpenTopoMap, satellite Esri | `MycoMap.vue` |
| Responsive minimal | Point de rupture 720 px : panneaux repliables, barre de jours défilante | `App.vue`, `TopBar.vue` |

### 3.2 Pipelines de données (scripts Docker)

| Source | Commande | Statut |
|---|---|---|
| Relief AWS Terrarium (~13 m/px) | précalcul | Défaut |
| IGN RGE ALTI 5 m | `./dev.sh rgealti` | Branché (optionnel) |
| IGN LIDAR HD (MNH : hauteur + trouées) | scripts `fetch_lidar_mnh_links.py` → `download_lidar_links.py` → `convert_lidar_chm.py` | Branché (optionnel, enchaînement manuel en 3 étapes) |
| IGN BD Forêt V2 | `./dev.sh bdforet` | Branché (optionnel) |
| BRGM Charm-50 | `./dev.sh geologie` | Branché (repli pH) |
| EcoDataCube pH 0–20 cm | `./dev.sh soilph` | Branché (optionnel) |
| Copernicus TCD 10 m | `./dev.sh tcd` (compte CDSE requis) | Branché (optionnel) |
| OSM / Overpass | précalcul | Couvert (repli), hydrographie, réseau d'accès |

Sur la machine de développement, ~13 Go de données locales (`backend/var/`, dont 8,8 Go
d'altimétrie).

### 3.3 Ce qui est esquissé

- **Calibrage** : la procédure « Calibrage avec vos spots » existe dans le README, mais aucun jeu
  d'observations n'alimente le dépôt ; les poids sont des **priors d'expert** explicitement non
  validés (`AGENTS.md`, « Statut honnête des poids »). Seul un re-challenge qualitatif sur une
  emprise Chartreuse est documenté (`best=96,3`, 193 mailles ≥ 90).
- **Adaptation à une autre région** : documentée, mais demande d'éditer les bornes dans
  `services.yaml` **et** dans plusieurs scripts Python, puis de tout retélécharger et précalculer.
- **Responsive** : un seul point de rupture ; pas de parcours pensé pour le téléphone en forêt.
- **Branding** : le `<title>` HTML dit « Forage Mapper — Grenoble & massifs », l'interface dit
  « Myco Map ».

### 3.4 Ce qui manque (pour un produit public)

| Domaine | Manque |
|---|---|
| Déploiement | Aucune configuration de production (serveur PHP intégré, mode debug, CORS limité à localhost, pas de reverse proxy, pas de HTTPS) |
| Comptes / paiement | Ni authentification, ni abonnement, ni paiement |
| Hors-ligne | Ni PWA, ni service worker, ni paquets de zones téléchargeables |
| Multi-régions | Une emprise codée en dur ; la France entière demanderait ~95 fois la zone actuelle (≈ 220 M mailles, ~14 Go de SQLite, estimation linéaire) |
| Mise à jour des données | Aucune tâche planifiée (OSM, BD Forêt, TCD ne se rafraîchissent jamais seuls) |
| Validation | Aucune mesure de performance prédictive (pas de comparaison avec GBIF/INPN ou des récoltes) |
| Tests | Aucun test backend |
| Observabilité | Ni analytics, ni suivi d'erreurs, ni métriques |
| Juridique | Ni CGU, ni mentions légales, ni politique de confidentialité ; avertissement présent seulement dans le README / `ATTRIBUTION.md` |
| Contenu | Pas de fiches espèces, ni de pages de sécurité (confusions toxiques), ni d'onboarding |
| Licences d'exploitation | Météo et fonds de carte utilisés dans leurs offres gratuites / « usage raisonnable » (voir 04) |

## 4. Points forts techniques (factuels)

1. **Profondeur des données** : LIDAR HD (hauteur de canopée + trouées), RGE ALTI 5 m, TCD 10 m,
   pH EcoDataCube, BD Forêt, Charm-50, météo AROME. Aucun concurrent observé ne déclare publiquement
   utiliser LIDAR HD (voir 02).
2. **Explicabilité** : chaque score se décompose par critère, avec un libellé métier ; le modèle,
   ses poids et ses divergences avec la littérature sont documentés et sourcés (`AGENTS.md`).
3. **Temporalité** : projection à 14 jours avec horloge de pousse par espèce (délais, assèchement).
4. **Actionnable sur le terrain** : itinéraire parking → sentier → approche, GPX, KMZ pour les
   applis GPS (Locus, OsmAnd, Iphigénie…).
5. **Architecture propre** : DDD, ports/adaptateurs, sources interchangeables à l'exécution.

## 5. Synthèse de l'audit

myco-map est un **prototype technique avancé et honnête** (modèle documenté, limites écrites),
construit en une semaine sur une seule région. Il n'a ni déploiement, ni utilisateurs, ni
validation empirique, ni couche produit (comptes, paiement, hors-ligne, onboarding, juridique).
La valeur accumulée tient au **pipeline de données de montagne** et au **moteur de score
explicable**, pas à un produit commercialisable.

Sources internes : `README.md`, `AGENTS.md`, `ATTRIBUTION.md`, `data/README.md`,
`backend/config/services.yaml`, `docker-compose.yml`, `backend/Dockerfile`,
`.github/workflows/ci.yml`, `git log`.
