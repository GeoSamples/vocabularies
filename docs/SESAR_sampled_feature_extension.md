---
comment: | 
  WARNING: This file is generated. Any edits will be lost!
format:
  html:
    ascii: true
    toc: true
    toc-depth: 4
    number-sections: true
    anchor-sections: false
    number-depth: 8
execute:
  echo: false
---

[]{#SESARsampledfeatureextension}

# **Concept scheme:** SESAR sampled feature extension

Vocabulary last modified:  2024-08-26

subtitle: 
  Terms to categorize sampled features in more detail. This vocabualary extends the iSamples Sampled FEature Type vocabulary with concepts from the GeoSciML envent environment vocabulary, and adds several additional concepts.

Namespace: 
[`https://w3id.org/isample/earthenv/essampledfeature/0.1/essfvocabulary`](https://w3id.org/isample/earthenv/essampledfeature/0.1/essfvocabulary)

**History**

* 2024-08-26 SMR generate to account for sampled features in SESAR

- [Any sampled feature](#anysampledfeature)
    - [Anthropogenic environment](#anthropogenicenvironment)
        - [Active human occupation site](#activehumanoccupationsite)
            - [Experiment setting](#experimentsetting)
            - [Laboratory or curatorial environment](#laboratorycuratorialenvironment)
        - [Site of past human activities](#pasthumanoccupationsite)
    - [Biological entity](#biologicalentity)
    - [Earth environment](#earthenvironment)
        - [tectonically defined setting](#tectonic_setting)
            - [back arc setting](#back_arc_setting)
            - [collisional setting](#collisional_setting)
            - [crustal setting](#crust)
                - [continental crustal setting](#continental_crust)
                    - [collisional setting](#collisional_setting)
                    - [foreland setting](#foreland_setting)
                    - [hinterland tectonic setting](#hinterland_setting)
                    - [lower continental crustal setting](#lower_continental_crust)
                    - [middle continental crust setting](#middle_continental_crust_setting)
                    - [upper continental crustal setting](#upper_continental_crustal_setting)
                - [oceanic crustal setting](#oceanic_crust)
                    - [lower oceanic crustal setting](#lower_oceanic_crustal_setting)
                    - [upper oceanic crustal setting](#upper_oceanic_crustal_setting)
                - [transitional crustal setting](#transitional_crust)
            - [extended terrane setting](#extended_terrane)
                - [continental rift setting](#continental_rift_setting)
            - [foreland setting](#foreland_setting)
            - [hinterland tectonic setting](#hinterland_setting)
            - [hot spot setting](#hot_spot_setting)
            - [intraplate tectonic setting](#intraplate_tectonic_setting)
                - [inactive spreading center setting](#inactive_spreading_center)
                - [seamount setting](#seamount_setting)
            - [mantle setting](#mantle)
                - [lower mantle setting](#lower_mantle)
                - [upper mantle setting](#upper_mantle)
            - [passive continental margin setting](#passive_continental_margin_setting)
            - [plate margin setting](#plate_margin_setting)
                - [active continental margin setting](#active_continental_margin_setting)
                - [active spreading center setting](#active_spreading_center)
                    - [fast spreading center setting](#fast_spreading_center_setting)
                    - [medium rate spreading center setting](#medium_spreading_center_setting)
                    - [slow spreading center setting](#slow_spreading_center_setting)
                - [forearc setting](#forearc_setting)
                - [subduction zone setting](#subduction_zone_setting)
                - [transform plate boundary setting](#transform_plate_boundary_setting)
                - [volcanic arc setting](#volcanic_arc_setting)
            - [plate spreading center setting](#plate_spreading_center)
                - [active spreading center setting](#active_spreading_center)
                    - [fast spreading center setting](#fast_spreading_center_setting)
                    - [medium rate spreading center setting](#medium_spreading_center_setting)
                    - [slow spreading center setting](#slow_spreading_center_setting)
                - [inactive spreading center setting](#inactive_spreading_center)
        - [Volcanic Setting ](#volcanicsetting)
        - [Atmosphere](#atmosphere)
        - [Earth interior](#earthinterior)
            - [contact metamorphic setting](#contact_metamorphic_origin)
            - [crustal setting](#crust)
                - [continental crustal setting](#continental_crust)
                    - [collisional setting](#collisional_setting)
                    - [foreland setting](#foreland_setting)
                    - [hinterland tectonic setting](#hinterland_setting)
                    - [lower continental crustal setting](#lower_continental_crust)
                    - [middle continental crust setting](#middle_continental_crust_setting)
                    - [upper continental crustal setting](#upper_continental_crustal_setting)
                - [oceanic crustal setting](#oceanic_crust)
                    - [lower oceanic crustal setting](#lower_oceanic_crustal_setting)
                    - [upper oceanic crustal setting](#upper_oceanic_crustal_setting)
                - [transitional crustal setting](#transitional_crust)
            - [high pressure low temperature earth interior setting](#high_pressure_low_temperature_earth_interior_setting)
            - [hypabyssal setting](#hypabyssal_setting)
            - [low pressure high temperature setting](#low_pressure_high_temperature_setting)
            - [mantle setting](#mantle)
                - [lower mantle setting](#lower_mantle)
                - [upper mantle setting](#upper_mantle)
            - [regional metamorphic setting](#regional_metamorphic_origin)
            - [ultra high pressure crustal setting](#ultra_high_pressure_crustal_setting)
            - [mineralized system setting](#mineralizedbody)
            - [plutonic setting](#plutoniccomplex)
            - [stratigraphic section setting](#stratigraphicsection)
        - [Earth surface](#earthsurface)
            - [anoxic setting](#anoxic_setting)
            - [arid or semi arid environment setting](#arid_or_semi_arid_environment_setting)
                - [gibber plain setting](#gibber_plain)
                - [marginal marine sabkha setting](#marginal_marine_sabkha_setting)
                - [playa setting](#playa_setting)
                - [sand plain setting](#sand_plain)
            - [cave setting](#cave)
            - [hillslope setting](#hillslope_setting)
            - [humid temperate climatic setting](#humid_temperate_climatic_setting)
            - [humid tropical climatic setting](#humid_tropical_climatic_setting)
            - [polar climatic setting](#polar_climatic_setting)
                - [Glacier environment](#glacierenvironment)
                    - [englacial setting](#englacial_setting)
                    - [glacial outwash plain setting](#glacial_outwash_plain_setting)
                    - [glacier lateral setting](#glacier_lateral_setting)
                    - [proglacial setting](#proglacial_setting)
                        - [glacier terminus setting](#glacier_terminus_setting)
                    - [subglacial setting](#subglacial_setting)
                    - [supraglacial setting](#supraglacial_setting)
            - [shoreline settings](#shoreline_settings)
                - [barrier island coastline setting](#barrier_island_coastline_setting)
                    - [barrier beach setting](#barrier_beach)
                    - [barrier lagoon setting](#barrier_lagoon)
                - [beach setting](#beach)
                    - [barrier beach setting](#barrier_beach)
                - [carbonate dominated shoreline setting](#carbonate_dominated_shoreline_setting)
                - [coastal plain setting](#coastal_plain_setting)
                - [deltaic system setting](#deltaic_system_setting)
                    - [delta front setting](#delta_front)
                    - [delta plain setting](#delta_plain)
                        - [lower delta plain setting](#lower_delta_plain)
                        - [upper delta plain setting](#upper_delta_plain)
                    - [delta distributary channel setting](#distributary_channel)
                    - [delta distributary mouth setting](#distributary_mouth)
                    - [estuarine delta setting](#estuarine_delta)
                    - [interdistributary bay setting](#interdistributary_bay)
                    - [lacustrine delta setting](#lacustrine_delta)
                    - [prodelta setting](#prodelta)
                - [estuary setting](#estuary_setting)
                    - [estuarine delta setting](#estuarine_delta)
                    - [estuarine lagoon setting](#estuarine_lagoon)
                - [lagoonal setting](#lagoonal_setting)
                    - [barrier lagoon setting](#barrier_lagoon)
                    - [estuarine lagoon setting](#estuarine_lagoon)
                - [low energy shoreline setting](#low_energy_shoreline_setting)
                    - [algal flat setting](#algal_flat_setting)
                    - [marginal marine sabkha setting](#marginal_marine_sabkha_setting)
                    - [mud flat setting](#mud_flat_setting)
                - [rocky coast setting](#rocky_coast_setting)
                - [strandplain setting](#strandplain_setting)
                - [supratidal setting](#supratidal)
                - [tidal setting](#tidal_setting)
                    - [intertidal setting](#intertidal)
                    - [lower delta plain setting](#lower_delta_plain)
                    - [tidal channel setting](#tidal_channel)
                    - [tidal flat setting](#tidal_flat_setting)
                        - [tidal marsh setting](#tidal_marsh)
            - [subaqueous setting](#subaqueous_setting)
                - [interdistributary bay setting](#interdistributary_bay)
                - [intertidal setting](#intertidal)
                - [marine setting](#marine_setting)
                    - [above carbonate compensation depth setting](#above_carbonate_compensation_depth_setting)
                    - [abyssal setting](#abyssal)
                    - [basin plain setting](#basin_plain_setting)
                    - [bathyal setting](#bathyal)
                        - [lower bathyal setting](#lower_bathyal)
                        - [middle bathyal setting](#middle_bathyal)
                        - [upper bathyal setting](#upper_bathyal)
                    - [below carbonate compensation depth setting](#below_carbonate_compensation_depth_setting)
                    - [biological reef setting](#biological_reef_setting)
                        - [backreef setting](#backreef)
                        - [forereef setting](#forereef)
                        - [reef flat setting](#reef_flat)
                    - [continental borderland setting](#continental_borderland_setting)
                    - [continental shelf setting](#continental_shelf_setting)
                    - [deep sea trench setting](#deep_sea_trench)
                    - [epicontinental marine setting](#epicontinental_marine_setting)
                    - [hadal setting](#hadal)
                    - [marine carbonate platform setting](#marine_carbonate_platform_setting)
                    - [neritic setting](#neritic)
                        - [inner neritic setting](#inner_neritic)
                        - [middle neritic setting](#middle_neritic)
                        - [outer neritic setting](#outer_neritic)
                    - [ocean highland setting](#ocean_highland_setting)
                        - [mid ocean ridge setting](#mid_ocean_ridge_setting)
                        - [oceanic plateau setting](#oceanic_plateau_setting)
                        - [seamount setting](#seamount_setting)
                    - [slope rise setting](#slope_rise_setting)
                    - [submarine fan setting](#submarine_fan_setting)
                - [prodelta setting](#prodelta)
                - [tidal channel setting](#tidal_channel)
            - [terrestrial setting](#terrestrial_setting)
                - [aeolian process setting](#aeolian_process_setting)
                    - [dunefield setting](#dunefield)
                        - [coastal dune field setting](#coastal_dune_field)
                    - [sand plain setting](#sand_plain)
                - [bog setting](#bog)
                    - [basin bog setting](#basin_bog)
                    - [blanket bog](#blanket_bog)
                - [gibber plain setting](#gibber_plain)
                - [glacial outwash plain setting](#glacial_outwash_plain_setting)
                - [lacustrine setting](#lacustrine_setting)
                    - [lacustrine delta setting](#lacustrine_delta)
                - [piedmont slope system setting](#piedmont_slope_system_setting)
                    - [alluvial fan setting](#alluvial_fan)
                    - [alluvial plain setting](#alluvial_plain)
                    - [pediment setting](#pediment_setting)
                - [playa setting](#playa_setting)
                - [river plain system setting](#river_plain_system_setting)
                    - [abandoned river channel setting](#abandoned_channel)
                    - [cutoff meander setting](#cutoff_meander)
                    - [floodplain setting](#floodplain)
                    - [river channel setting](#river_channel)
                        - [braided river channel setting](#braided_channel)
                        - [meandering river channel setting](#meandering_channel)
                - [sand plain setting](#sand_plain)
                - [upper delta plain setting](#upper_delta_plain)
            - [wetland setting](#wetland_setting)
                - [bog setting](#bog)
                    - [basin bog setting](#basin_bog)
                    - [blanket bog](#blanket_bog)
                - [swamp or marsh setting](#swamp_or_marsh_setting)
                    - [tidal marsh setting](#tidal_marsh)
            - [Lake river or stream bottom](#lakeriverstreambottom)
            - [Marine water body bottom](#marinewaterbodybottom)
            - [Subaerial surface environment](#subaerialsurfaceenvironment)
                - [aeolian process setting](#aeolian_process_setting)
                    - [dunefield setting](#dunefield)
                        - [coastal dune field setting](#coastal_dune_field)
                    - [sand plain setting](#sand_plain)
                - [coastal plain setting](#coastal_plain_setting)
                - [gibber plain setting](#gibber_plain)
                - [piedmont slope system setting](#piedmont_slope_system_setting)
                    - [alluvial fan setting](#alluvial_fan)
                    - [alluvial plain setting](#alluvial_plain)
                    - [pediment setting](#pediment_setting)
                - [playa setting](#playa_setting)
                - [river plain system setting](#river_plain_system_setting)
                    - [abandoned river channel setting](#abandoned_channel)
                    - [cutoff meander setting](#cutoff_meander)
                    - [floodplain setting](#floodplain)
                    - [river channel setting](#river_channel)
                        - [braided river channel setting](#braided_channel)
                        - [meandering river channel setting](#meandering_channel)
                - [strandplain setting](#strandplain_setting)
                - [supratidal setting](#supratidal)
                - [soil profile setting](#soilprofile)
        - [Glacier environment](#glacierenvironment)
            - [englacial setting](#englacial_setting)
            - [glacial outwash plain setting](#glacial_outwash_plain_setting)
            - [glacier lateral setting](#glacier_lateral_setting)
            - [proglacial setting](#proglacial_setting)
                - [glacier terminus setting](#glacier_terminus_setting)
            - [subglacial setting](#subglacial_setting)
            - [supraglacial setting](#supraglacial_setting)
        - [Subsurface fluid reservoir](#subsurfacefluidreservoir)
        - [Water body](#waterbody)
            - [Marine environment](#marinewaterbody)
            - [Terrestrial water body](#terrestrialwaterbody)
    - [Extraterrestrial environment](#extraterrestrialenvironment)

**Concepts**

[]{#anysampledfeature}

##  Any sampled feature
- Any thing that can be sampled. Top concept in sampled feature type
vocabulary.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/anysampledfeature
- **Other Properties:**

[]{#anthropogenicenvironment}

###  Anthropogenic environment
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is produced by or related to human activity past or
present.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/anthropogenicenvironment
- **Other Properties:**

[]{#activehumanoccupationsite}

####  Active human occupation site
- **Child of**:
 [`Anthropogenic environment`](#anthropogenicenvironment)
- sampled feature is a site at which there are ongoing human
activities
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/activehumanoccupationsite
- **Other Properties:**

[]{#experimentsetting}

#####  Experiment setting
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
- Sampled feature is an experimental set up that produced the sample;
the sample is the product of the experiment.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/experimentsetting
- **Other Properties:**

[]{#laboratorycuratorialenvironment}

#####  Laboratory or curatorial environment
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
- Sampled feature is a laboratory or other research site, collected
with intention of characterizing the environment in which data are
collected or other research conducted, that might affect results or
safety; e.g. lab blank measurements.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/laboratorycuratorialenvironment
- **Other Properties:**

[]{#pasthumanoccupationsite}

####  Site of past human activities
- **Child of**:
 [`Anthropogenic environment`](#anthropogenicenvironment)
- sampled feature is a place where humans have been and left evidence
of their activity. Includes prehistoric and paleo hominid sites
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/pasthumanoccupationsite
- **Other Properties:**

[]{#biologicalentity}

###  Biological entity
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is an organism. Use for samples that represent some
species of organism as the proximate sampled feature, not the
environment that the organism inhabits.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/biologicalentity
- **Other Properties:**

[]{#earthenvironment}

###  Earth environment
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is the natural Earth environment
- **See Also**:
* [<http://purl.bioontology.org/ontology/MESH/D004777>](http://purl.bioontology.org/ontology/MESH/D004777)
* [<http://semanticscience.org/resource/SIO_000955>](http://semanticscience.org/resource/SIO_000955)
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/earthenvironment
- **Other Properties:**

[]{#tectonic_setting}

####  tectonically defined setting
- **Child of**:
 [`Earth environment`](#earthenvironment)
-
- Setting defined by relationships to tectonic plates on or in the
Earth.
- **Source:**

- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tectonic_setting
- **Other Properties:**

[]{#back_arc_setting}

#####  back arc setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting adjacent to a volcanic arc formed above a
subduction zone. The back arc setting is on the opposite side of the
volcanic arc from the trench at which oceanic crust is consumed in a
subduction zone. Back arc setting includes terrane that is affected by
plate margin and arc-related processes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/back_arc_setting
- **Other Properties:**

[]{#collisional_setting}

#####  collisional setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting in which two continental crustal plates impact and
are sutured together after intervening oceanic crust is entirely
consumed at a subduction zone separating the plates. Such collision
typically involves major mountain forming events, exemplified by the
modern Alpine and Himalayan mountain chains.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/collisional_setting
- **Other Properties:**

[]{#crust}

#####  crustal setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
 [`Earth interior`](#earthinterior)
- The outermost layer or shell of the Earth, defined according to
various criteria, including seismic velocity, density and composition,
that part of the Earth above the Mohorovicic discontinuity, made up of
the sial and the sima.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/crust
- **Other Properties:**

[]{#continental_crust}

######  continental crustal setting
- **Child of**:
 [`crustal setting`](#crust)
- That type of the Earth's crust which underlies the continents and
the continental shelves, it is equivalent to the sial and continental
sima and ranges in thickness from about 25 km to more than 70 km under
mountain ranges, averaging ~40 km. The density of the continental
crust averages ~2.8 g/cm3 and is ~2.7 g.cm3 in the upper layer. The
velocities of compressional seismic waves through it average ~6.5 km/s
and are less than ~7.0 km/sec.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/continental_crust
- **Other Properties:**

[]{#collisional_setting}

#######  collisional setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting in which two continental crustal plates impact and
are sutured together after intervening oceanic crust is entirely
consumed at a subduction zone separating the plates. Such collision
typically involves major mountain forming events, exemplified by the
modern Alpine and Himalayan mountain chains.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/collisional_setting
- **Other Properties:**

[]{#foreland_setting}

#######  foreland setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- The exterior area of an orogenic belt where deformation occurs
without significant metamorphism. Generally the foreland is closer to
the continental interior than other portions of the orogenic belt are.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/foreland_setting
- **Other Properties:**

[]{#hinterland_setting}

#######  hinterland tectonic setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting in the internal part of an orogenic belt,
characterized by plastic deformation of rocks accompanied by
significant metamorphism, typically involving crystalline basement
rocks. Typically denotes the most structurally thickened part of an
orogenic belt, between a magmatic arc or collision zone and a more
'external' foreland setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hinterland_setting
- **Other Properties:**

[]{#lower_continental_crust}

#######  lower continental crustal setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
- Continental crustal setting characterized by upper amphibolite to
granulite facies metamorphism, insitu melting, residual anhydrous
metamorphic rocks, and ductile flow of rock bodies.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_continental_crust
- **Other Properties:**

[]{#middle_continental_crust_setting}

#######  middle continental crust setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
- Continental crustal setting characterized by greenschist to upper
amphibolite facies metamorphism, plutonic igneous rocks, and ductile
deformation.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/middle_continental_crust_setting
- **Other Properties:**

[]{#upper_continental_crustal_setting}

#######  upper continental crustal setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
- Continental crustal setting dominated by non metamorphosed to low
greenschist facies metamorphic rocks, and brittle deformation.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_continental_crustal_setting
- **Other Properties:**

[]{#oceanic_crust}

######  oceanic crustal setting
- **Child of**:
 [`crustal setting`](#crust)
- That type of the Earth's crust which underlies the ocean basins. The
oceanic crust is 5-10 km thick, it has a density of 2.9 g/cm3, and
compressional seismic-wave velocities travelling through it at 4-7.2
km/sec. Setting in crust produced by submarine volcanism at a mid
ocean ridge.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/oceanic_crust
- **Other Properties:**

[]{#lower_oceanic_crustal_setting}

#######  lower oceanic crustal setting
- **Child of**:
 [`oceanic crustal setting`](#oceanic_crust)
- Setting characterized by dominantly intrusive mafic rocks, with
sheeted dike complexes in upper part and gabbroic to ultramafic
intrusive or metamorphic rocks in lower part.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_oceanic_crustal_setting
- **Other Properties:**

[]{#upper_oceanic_crustal_setting}

#######  upper oceanic crustal setting
- **Child of**:
 [`oceanic crustal setting`](#oceanic_crust)
- Oceanic crustal setting dominated by extrusive rocks, abyssal
oceanic sediment, with increasing mafic intrusive rock in lower part.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_oceanic_crustal_setting
- **Other Properties:**

[]{#transitional_crust}

######  transitional crustal setting
- **Child of**:
 [`crustal setting`](#crust)
- Crust formed in the transition zone between continental and oceanic
crust, during the history of continental rifting that culminates in
the formation of a new ocean.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/transitional_crust
- **Other Properties:**

[]{#extended_terrane}

#####  extended terrane setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting characterized by extension of the upper crust
manifested by formation of rift valleys or basin and range
physiography, with arrays of low to high angle normal faults. Modern
examples include the North Sea, East Africa, and the Basin and Range
of the North American Cordillera. Typically applied in continental
crustal settings.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/extended_terrane
- **Other Properties:**

[]{#continental_rift_setting}

######  continental rift setting
- **Child of**:
 [`extended terrane setting`](#extended_terrane)
- Extended terrane in a zone of continental breakup, may include
incipient oceanic crust. Examples include Red Sea, East Africa Rift,
Salton Trough
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/continental_rift_setting
- **Other Properties:**

[]{#foreland_setting}

#####  foreland setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- The exterior area of an orogenic belt where deformation occurs
without significant metamorphism. Generally the foreland is closer to
the continental interior than other portions of the orogenic belt are.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/foreland_setting
- **Other Properties:**

[]{#hinterland_setting}

#####  hinterland tectonic setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting in the internal part of an orogenic belt,
characterized by plastic deformation of rocks accompanied by
significant metamorphism, typically involving crystalline basement
rocks. Typically denotes the most structurally thickened part of an
orogenic belt, between a magmatic arc or collision zone and a more
'external' foreland setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hinterland_setting
- **Other Properties:**

[]{#hot_spot_setting}

#####  hot spot setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Setting in a zone of high heat flow from the mantle. Typically
identified in intraplate settings, but hot spot may also interact with
active plate margins (Iceland...). Includes surface manifestations
like volcanic center, but also includes crust and mantle
manifestations as well.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hot_spot_setting
- **Other Properties:**

[]{#intraplate_tectonic_setting}

#####  intraplate tectonic setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Tectonically stable setting far from any active plate margins.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/intraplate_tectonic_setting
- **Other Properties:**

[]{#inactive_spreading_center}

######  inactive spreading center setting
- **Child of**:
 [`intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`plate spreading center setting`](#plate_spreading_center)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/inactive_spreading_center
- **Other Properties:**

[]{#seamount_setting}

######  seamount setting
- **Child of**:
 [`intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`ocean highland setting`](#ocean_highland_setting)
- Setting that consists of a conical mountain on the ocean floor
(guyot). Typically characterized by active volcanism, pelagic
sedimentation. If the mountain is high enough to reach the photic
zone, carbonate production may result in reef building to produce a
carbonate platform or atoll setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/seamount_setting
- **Other Properties:**

[]{#mantle}

#####  mantle setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
 [`Earth interior`](#earthinterior)
- The zone of the Earth below the crust and above the core, which is
divided into the upper mantle and the lower mantle, with a transition
zone separating them.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/mantle
- **Other Properties:**

[]{#lower_mantle}

######  lower mantle setting
- **Child of**:
 [`mantle setting`](#mantle)
- That part of the mantle that lies below a depth of about 660 km.
With increasing depth, density increases from ~4.4 g/cm3-to ~5.6
g/cm3, and velocity of compressional seismic waves increases from
~10.7 km/s to ~13.7 km/s (Dziewonski and Anderson, 1981).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_mantle
- **Other Properties:**

[]{#upper_mantle}

######  upper mantle setting
- **Child of**:
 [`mantle setting`](#mantle)
- That part of the mantle which lies above a depth of about 660 km and
has a density of 3.4 g/cm3 to 4.0 g/cm3 with increasing depth.
Similarly, P-wave velocity increases from about 8 to 11 km/sec with
depth and S wave velocity increases from about 4.5 to 6 km/sec with
depth. It is presumed to be peridotitic in composition. It includes
the subcrustal lithosphere the asthenosphere and the transition zone,
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_mantle
- **Other Properties:**

[]{#passive_continental_margin_setting}

#####  passive continental margin setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Boundary of continental crust into oceanic crust of an oceanic basin
that is not a subduction zone or transform fault system. Generally is
rifted margin formed when ocean basin was initially formed.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/passive_continental_margin_setting
- **Other Properties:**

[]{#plate_margin_setting}

#####  plate margin setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting at the boundary between two tectonic plates.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/plate_margin_setting
- **Other Properties:**

[]{#active_continental_margin_setting}

######  active continental margin setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
- Plate margin setting on continental crust.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/active_continental_margin_setting
- **Other Properties:**

[]{#active_spreading_center}

######  active spreading center setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
 [`plate spreading center setting`](#plate_spreading_center)
- Divergent plate margin at which new oceanic crust is being formed
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/active_spreading_center
- **Other Properties:**

[]{#fast_spreading_center_setting}

#######  fast spreading center setting
- **Child of**:
 [`active spreading center setting`](#active_spreading_center)
- Spreading center at which the opening rate is greater than 100 mm
per year.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/fast_spreading_center_setting
- **Other Properties:**

[]{#medium_spreading_center_setting}

#######  medium rate spreading center setting
- **Child of**:
 [`active spreading center setting`](#active_spreading_center)
- Spreading center at which the opening rate is between 50 and 100 mm
per year.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/medium_spreading_center_setting
- **Other Properties:**

[]{#slow_spreading_center_setting}

#######  slow spreading center setting
- **Child of**:
 [`active spreading center setting`](#active_spreading_center)
- Spreading center at which the opening rate is less than 50 mm per
year.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/slow_spreading_center_setting
- **Other Properties:**

[]{#forearc_setting}

######  forearc setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
- Tectonic setting between a subduction-related trench and a volcanic
arc
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/forearc_setting
- **Other Properties:**

[]{#subduction_zone_setting}

######  subduction zone setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
- Tectonic setting at which a tectonic plate, usually oceanic, is
moving down into the mantle beneath another overriding plate.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/subduction_zone_setting
- **Other Properties:**

[]{#transform_plate_boundary_setting}

######  transform plate boundary setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
- Plate boundary at which the adjacent plates are moving laterally
relative to each other.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/transform_plate_boundary_setting
- **Other Properties:**

[]{#volcanic_arc_setting}

######  volcanic arc setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
- A generally curvillinear belt of volcanoes above a subduction zone.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/volcanic_arc_setting
- **Other Properties:**

[]{#plate_spreading_center}

#####  plate spreading center setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting where new oceanic crust is being or has been formed
at a divergent plate boundary. Includes active and inactive spreading
centers.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/plate_spreading_center
- **Other Properties:**

[]{#active_spreading_center}

######  active spreading center setting
- **Child of**:
 [`plate margin setting`](#plate_margin_setting)
 [`plate spreading center setting`](#plate_spreading_center)
- Divergent plate margin at which new oceanic crust is being formed
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/active_spreading_center
- **Other Properties:**

[]{#fast_spreading_center_setting}

#######  fast spreading center setting
- **Child of**:
 [`active spreading center setting`](#active_spreading_center)
- Spreading center at which the opening rate is greater than 100 mm
per year.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/fast_spreading_center_setting
- **Other Properties:**

[]{#medium_spreading_center_setting}

#######  medium rate spreading center setting
- **Child of**:
 [`active spreading center setting`](#active_spreading_center)
- Spreading center at which the opening rate is between 50 and 100 mm
per year.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/medium_spreading_center_setting
- **Other Properties:**

[]{#slow_spreading_center_setting}

#######  slow spreading center setting
- **Child of**:
 [`active spreading center setting`](#active_spreading_center)
- Spreading center at which the opening rate is less than 50 mm per
year.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/slow_spreading_center_setting
- **Other Properties:**

[]{#inactive_spreading_center}

######  inactive spreading center setting
- **Child of**:
 [`intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`plate spreading center setting`](#plate_spreading_center)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/inactive_spreading_center
- **Other Properties:**

[]{#volcanicsetting}

####  Volcanic Setting
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Settings related to the eruption of lava near, at, or above the
earth surface. Might include atmospheric products of volcanic
eruption, in terrestrial, lacustrine, or marine environments, related
hypabyssal intrusions or hydrothermal systems.
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/essampledfeature/0.1/volcanicsetting
- **Other Properties:**

[]{#atmosphere}

####  Atmosphere
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is the Earth's atmosphere
- **See Also**:
* [<http://purl.obolibrary.org/obo/ENVO_01000267>](http://purl.obolibrary.org/obo/ENVO_01000267)
* [<http://purl.obolibrary.org/obo/RBO_00000018>](http://purl.obolibrary.org/obo/RBO_00000018)
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/atmosphere
- **Other Properties:**

[]{#earthinterior}

####  Earth interior
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Geologic environments within the solid Earth.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/earthinterior
- **Other Properties:**

[]{#contact_metamorphic_origin}

#####  contact metamorphic setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Metamorphism of country rock at the contact of an igneous body.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/contact_metamorphic_origin
- **Other Properties:**

[]{#crust}

#####  crustal setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
 [`Earth interior`](#earthinterior)
- The outermost layer or shell of the Earth, defined according to
various criteria, including seismic velocity, density and composition,
that part of the Earth above the Mohorovicic discontinuity, made up of
the sial and the sima.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/crust
- **Other Properties:**

[]{#continental_crust}

######  continental crustal setting
- **Child of**:
 [`crustal setting`](#crust)
- That type of the Earth's crust which underlies the continents and
the continental shelves, it is equivalent to the sial and continental
sima and ranges in thickness from about 25 km to more than 70 km under
mountain ranges, averaging ~40 km. The density of the continental
crust averages ~2.8 g/cm3 and is ~2.7 g.cm3 in the upper layer. The
velocities of compressional seismic waves through it average ~6.5 km/s
and are less than ~7.0 km/sec.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/continental_crust
- **Other Properties:**

[]{#collisional_setting}

#######  collisional setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting in which two continental crustal plates impact and
are sutured together after intervening oceanic crust is entirely
consumed at a subduction zone separating the plates. Such collision
typically involves major mountain forming events, exemplified by the
modern Alpine and Himalayan mountain chains.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/collisional_setting
- **Other Properties:**

[]{#foreland_setting}

#######  foreland setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- The exterior area of an orogenic belt where deformation occurs
without significant metamorphism. Generally the foreland is closer to
the continental interior than other portions of the orogenic belt are.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/foreland_setting
- **Other Properties:**

[]{#hinterland_setting}

#######  hinterland tectonic setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
 [`tectonically defined setting`](#tectonic_setting)
- Tectonic setting in the internal part of an orogenic belt,
characterized by plastic deformation of rocks accompanied by
significant metamorphism, typically involving crystalline basement
rocks. Typically denotes the most structurally thickened part of an
orogenic belt, between a magmatic arc or collision zone and a more
'external' foreland setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hinterland_setting
- **Other Properties:**

[]{#lower_continental_crust}

#######  lower continental crustal setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
- Continental crustal setting characterized by upper amphibolite to
granulite facies metamorphism, insitu melting, residual anhydrous
metamorphic rocks, and ductile flow of rock bodies.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_continental_crust
- **Other Properties:**

[]{#middle_continental_crust_setting}

#######  middle continental crust setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
- Continental crustal setting characterized by greenschist to upper
amphibolite facies metamorphism, plutonic igneous rocks, and ductile
deformation.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/middle_continental_crust_setting
- **Other Properties:**

[]{#upper_continental_crustal_setting}

#######  upper continental crustal setting
- **Child of**:
 [`continental crustal setting`](#continental_crust)
- Continental crustal setting dominated by non metamorphosed to low
greenschist facies metamorphic rocks, and brittle deformation.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_continental_crustal_setting
- **Other Properties:**

[]{#oceanic_crust}

######  oceanic crustal setting
- **Child of**:
 [`crustal setting`](#crust)
- That type of the Earth's crust which underlies the ocean basins. The
oceanic crust is 5-10 km thick, it has a density of 2.9 g/cm3, and
compressional seismic-wave velocities travelling through it at 4-7.2
km/sec. Setting in crust produced by submarine volcanism at a mid
ocean ridge.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/oceanic_crust
- **Other Properties:**

[]{#lower_oceanic_crustal_setting}

#######  lower oceanic crustal setting
- **Child of**:
 [`oceanic crustal setting`](#oceanic_crust)
- Setting characterized by dominantly intrusive mafic rocks, with
sheeted dike complexes in upper part and gabbroic to ultramafic
intrusive or metamorphic rocks in lower part.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_oceanic_crustal_setting
- **Other Properties:**

[]{#upper_oceanic_crustal_setting}

#######  upper oceanic crustal setting
- **Child of**:
 [`oceanic crustal setting`](#oceanic_crust)
- Oceanic crustal setting dominated by extrusive rocks, abyssal
oceanic sediment, with increasing mafic intrusive rock in lower part.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_oceanic_crustal_setting
- **Other Properties:**

[]{#transitional_crust}

######  transitional crustal setting
- **Child of**:
 [`crustal setting`](#crust)
- Crust formed in the transition zone between continental and oceanic
crust, during the history of continental rifting that culminates in
the formation of a new ocean.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/transitional_crust
- **Other Properties:**

[]{#high_pressure_low_temperature_earth_interior_setting}

#####  high pressure low temperature earth interior setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- High pressure environment characterized by geothermal gradient
significantly lower than standard continental geotherm, enviornment in
which blueschist facies metamorphic rocks form. Typically associated
with subduction zones.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/high_pressure_low_temperature_earth_interior_setting
- **Other Properties:**

[]{#hypabyssal_setting}

#####  hypabyssal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Igneous environment close to the Earth's surface, characterized by
more rapid cooling than plutonic setting to produce generally fine-
grained intrusive igneous rock that is commonly associated with co-
magmatic volcanic rocks.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hypabyssal_setting
- **Other Properties:**

[]{#low_pressure_high_temperature_setting}

#####  low pressure high temperature setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Setting characterized by temperatures significantly higher that
those associated with normal continental geothermal gradient.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/low_pressure_high_temperature_setting
- **Other Properties:**

[]{#mantle}

#####  mantle setting
- **Child of**:
 [`tectonically defined setting`](#tectonic_setting)
 [`Earth interior`](#earthinterior)
- The zone of the Earth below the crust and above the core, which is
divided into the upper mantle and the lower mantle, with a transition
zone separating them.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/mantle
- **Other Properties:**

[]{#lower_mantle}

######  lower mantle setting
- **Child of**:
 [`mantle setting`](#mantle)
- That part of the mantle that lies below a depth of about 660 km.
With increasing depth, density increases from ~4.4 g/cm3-to ~5.6
g/cm3, and velocity of compressional seismic waves increases from
~10.7 km/s to ~13.7 km/s (Dziewonski and Anderson, 1981).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_mantle
- **Other Properties:**

[]{#upper_mantle}

######  upper mantle setting
- **Child of**:
 [`mantle setting`](#mantle)
- That part of the mantle which lies above a depth of about 660 km and
has a density of 3.4 g/cm3 to 4.0 g/cm3 with increasing depth.
Similarly, P-wave velocity increases from about 8 to 11 km/sec with
depth and S wave velocity increases from about 4.5 to 6 km/sec with
depth. It is presumed to be peridotitic in composition. It includes
the subcrustal lithosphere the asthenosphere and the transition zone,
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_mantle
- **Other Properties:**

[]{#regional_metamorphic_origin}

#####  regional metamorphic setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Metamorphism not obviously localized along contacts of igneous
bodies, includes burial metamorphism and ocean ridge metamorphism
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/regional_metamorphic_origin
- **Other Properties:**

[]{#ultra_high_pressure_crustal_setting}

#####  ultra high pressure crustal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Setting characterized by pressures characteristic of upper mantle,
but indicated by mineral assemblage in crustal composition rocks.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/ultra_high_pressure_crustal_setting
- **Other Properties:**

[]{#mineralizedbody}

#####  mineralized system setting
- **Child of**:
 [`Earth interior`](#earthinterior)
-
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/essampledfeature/0.1/mineralizedbody
- **Other Properties:**

[]{#plutoniccomplex}

#####  plutonic setting
- **Child of**:
 [`Earth interior`](#earthinterior)
-
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/essampledfeature/0.1/plutoniccomplex
- **Other Properties:**

[]{#stratigraphicsection}

#####  stratigraphic section setting
- **Child of**:
 [`Earth interior`](#earthinterior)
-
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/essampledfeature/0.1/stratigraphicsection
- **Other Properties:**

[]{#earthsurface}

####  Earth surface
* `earth surface setting`
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Geologic environments on the surface of the solid Earth. Hierarchy
presented here is based on assumption that a particular setting may be
specified by a combination of a climatic setting with one or more
process or geomorphically defined settings..
- Sampled feature is the interface between solid earth and hydrosphere
or atmosphere. Includes samples representing things collected on the
surface, in the uppermost part of the material below the surface, or
air or water directly at the contact with the Earth surface.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/earthsurface
- **Other Properties:**

[]{#anoxic_setting}

#####  anoxic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting depleted in oxygen, typically subaqueous.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/anoxic_setting
- **Other Properties:**

[]{#arid_or_semi_arid_environment_setting}

#####  arid or semi arid environment setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting characterized by mean annual precipitation of 10 inches (25
cm) or less. (Jackson, 1997, p. 172). Equivalent to SLTT 'Desert
setting', but use 'Arid' to emphasize climatic nature of setting
definition.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/arid_or_semi_arid_environment_setting
- **Other Properties:**

[]{#gibber_plain}

######  gibber plain setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/gibber_plain
- **Other Properties:**

[]{#marginal_marine_sabkha_setting}

######  marginal marine sabkha setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`low energy shoreline setting`](#low_energy_shoreline_setting)
- Setting characterized by arid to semi-arid conditions on restricted
coastal plains mostly above normal high tide level, with evaporite-
saline mineral, tidal-flood, and eolian deposits. Boundaries with
intertidal setting and non-tidal terrestrial setting are gradational.
(Jackson, 1997, p. 561).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/marginal_marine_sabkha_setting
- **Other Properties:**

[]{#playa_setting}

######  playa setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/playa_setting
- **Other Properties:**

[]{#sand_plain}

######  sand plain setting
- **Child of**:
 [`aeolian process setting`](#aeolian_process_setting)
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
- A sand-covered plain dominated by aeolian processes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/sand_plain
- **Other Properties:**

[]{#cave}

#####  cave setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- A natural underground open space, it generally has a connection to
the surface, is large enough for a person to enter, and extends into
darkness. The most common type of cave is formed in limestone by
dissolution.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/cave
- **Other Properties:**

[]{#hillslope_setting}

#####  hillslope setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Earth surface setting characterized by surface slope angles high
enough that gravity alone becomes a significant factor in geomorphic
development, as well as base-of-slope areas influenced by hillslope
processes. Hillslope activities include creep, sliding, slumping,
falling, and other downslope movements caused by slope collapse
induced by gravitational influence on earth materials. May be
subaerial or subaqueous.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hillslope_setting
- **Other Properties:**

[]{#humid_temperate_climatic_setting}

#####  humid temperate climatic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting with seasonal climate having hot to cold or humid to arid
seasons.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/humid_temperate_climatic_setting
- **Other Properties:**

[]{#humid_tropical_climatic_setting}

#####  humid tropical climatic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting with hot humid climate influenced by equatorial air masses,
no winter season.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/humid_tropical_climatic_setting
- **Other Properties:**

[]{#polar_climatic_setting}

#####  polar climatic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting with climate dominated by temperatures below the freezing
temperature of water. Includes polar deserts because precipitation is
generally scant at high latitude. Climate controlled by arctic air
masses, cold dry environment with short summer.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/polar_climatic_setting
- **Other Properties:**

[]{#glacierenvironment}

######  Glacier environment
* `glacier related setting`
- **Child of**:
 [`polar climatic setting`](#polar_climatic_setting)
 [`Earth environment`](#earthenvironment)
- Earth surface setting with geography defined by spatial relationship
to glaciers (e.g. on top of a glacier, next to a glacier, in front of
a glacier...). Processes related to moving ice dominate sediment
transport and deposition and landform development. Includes
subaqueous, shoreline, and terrestrial settings that are impacted by
the presence of glaciers. Considered a geographically defined setting
in that a glacier is a geographic feature.
- Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock
or water directly under or on top of such ice.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/glacierenvironment
- **Other Properties:**

[]{#englacial_setting}

#######  englacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Contained, embedded, or carried within the body of a glacier or ice
sheet, said of meltwater streams, till, drift, moraine
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/englacial_setting
- **Other Properties:**

[]{#glacial_outwash_plain_setting}

#######  glacial outwash plain setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Glacier environment`](#glacierenvironment)
- Areas adjacent to glacial front dominated by sediment and water
supplied by glacial melting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacial_outwash_plain_setting
- **Other Properties:**

[]{#glacier_lateral_setting}

#######  glacier lateral setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Settings adjacent to edges of confined glacier.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacier_lateral_setting
- **Other Properties:**

[]{#proglacial_setting}

#######  proglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Immediately in front of or just beyond the outer limits of a glacier
or ice sheet, generally at or near its lower end, said of lakes,
streams, deposits, and other features produced by or derived from the
glacier ice
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/proglacial_setting
- **Other Properties:**

[]{#glacier_terminus_setting}

########  glacier terminus setting
- **Child of**:
 [`proglacial setting`](#proglacial_setting)
- Region of sediment deposition due to melting of glacier ice.
ablation and flow till setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacier_terminus_setting
- **Other Properties:**

[]{#subglacial_setting}

#######  subglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Formed or accumulated in or by the bottom parts of a glacier or ice
sheet, said of meltwater streams, till, moraine, etc.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/subglacial_setting
- **Other Properties:**

[]{#supraglacial_setting}

#######  supraglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Carried upon, deposited from, or pertaining to the top surface of a
glacier or ice sheet, said of meltwater streams, till, drift, etc.
(Jackson, 1997, p. 639). Dreimanis (1988, p. 39) recommendation that
\supraglacial\ supersede \superglacial\ is followed.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/supraglacial_setting
- **Other Properties:**

[]{#shoreline_settings}

#####  shoreline settings
- **Child of**:
 [`Earth surface`](#earthsurface)
- Geologic settings characterized by location adjacent to the ocean or
a lake. A zone of indefinite width (may be many kilometers), bordering
a body of water that extends from the water line inland to the first
major change in landform features. Includes settings that may be
subaerial, intermittently subaqueous, or shallow subaqueous, but are
intrinsically associated with the interface between land areas and
water bodies.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/shoreline_settings
- **Other Properties:**

[]{#barrier_island_coastline_setting}

######  barrier island coastline setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- setting meant to include all the various geographic elements
typically associated with a barrier island coastline, including the
barrier islands, and geomorphic/geographic elements that are linked by
processes associated with the presence of the island (e.g. wash over
fans, inlet channel, back barrier lagoon).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/barrier_island_coastline_setting
- **Other Properties:**

[]{#barrier_beach}

#######  barrier beach setting
- **Child of**:
 [`barrier island coastline setting`](#barrier_island_coastline_setting)
 [`beach setting`](#beach)
- A narrow, elongate sand or gravel ridge rising slightly above the
high-tide level and extending generally parallel with the shore, but
separated from it by a lagoon (Shepard, 1954, p.1904), estuary, or
marsh, it is extended by longshore transport and is rarely more than
several kilometers long.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/barrier_beach
- **Other Properties:**

[]{#barrier_lagoon}

#######  barrier lagoon setting
- **Child of**:
 [`barrier island coastline setting`](#barrier_island_coastline_setting)
 [`lagoonal setting`](#lagoonal_setting)
- A lagoon that is roughly parallel to the coast and is separated from
the open ocean by a strip of land or by a barrier reef. Tidal
influence is typically restricted and the lagoon is commonly
hypersaline.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/barrier_lagoon
- **Other Properties:**

[]{#beach}

######  beach setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- The unconsolidated material at the shoreline that covers a gently
sloping zone, typically with a concave profile, extending landward
from the low-water line to the place where there is a definite change
in material or physiographic form (such as a cliff), or to the line of
permanent vegetation (usually the effective limit of the highest storm
waves), at the shore of a body of water, formed and washed by waves or
tides, usually covered by sand or gravel, and lacking a bare rocky
surface.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/beach
- **Other Properties:**

[]{#barrier_beach}

#######  barrier beach setting
- **Child of**:
 [`barrier island coastline setting`](#barrier_island_coastline_setting)
 [`beach setting`](#beach)
- A narrow, elongate sand or gravel ridge rising slightly above the
high-tide level and extending generally parallel with the shore, but
separated from it by a lagoon (Shepard, 1954, p.1904), estuary, or
marsh, it is extended by longshore transport and is rarely more than
several kilometers long.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/barrier_beach
- **Other Properties:**

[]{#carbonate_dominated_shoreline_setting}

######  carbonate dominated shoreline setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- A shoreline setting in which terrigenous input is minor compared to
local carbonate sediment production. Constructional biogenic activity
is an important element in geomorphic development.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/carbonate_dominated_shoreline_setting
- **Other Properties:**

[]{#coastal_plain_setting}

######  coastal plain setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A low relief plain bordering a water body extending inland to the
nearest elevated land, sloping very gently towards the water body.
Distinguished from alluvial plain by presence of relict shoreline-
related deposits or morphology.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/coastal_plain_setting
- **Other Properties:**

[]{#deltaic_system_setting}

######  deltaic system setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- Environments at the mouth of a river or stream that enters a
standing body of water (ocean or lake). The delta forms a triangular
or fan-shaped plain of considerable area. Subaerial parts of the delta
are crossed by many distributaries of the main river, and commonly
extend beyond the general trend of the coast. Subaqueous parts of the
delta merge with the adjacent basin floor, and are progressively
influenced by non-fluvial processes. Deltas result from the
accumulation of sediment supplied by the river in such quantities that
it is not removed by tides, waves, and currents. Adapted from the
Glossary of Geology definition for delta (Jackson, 1997, p. 167).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/deltaic_system_setting
- **Other Properties:**

[]{#delta_front}

#######  delta front setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
- A narrow zone where deposition in deltas is most active, consisting
of a continuous sheet of sand, and occurring within the effective
depth of wave erosion (10 m or less). It is the zone separating the
prodelta from the delta plain, and it may or may not be steep\
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/delta_front
- **Other Properties:**

[]{#delta_plain}

#######  delta plain setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
- The level or nearly level surface composing the landward part of a
large or compound delta, strictly, an alluvial plain characterized by
repeated channel bifurcation and divergence, multiple distributary
channels, and interdistributary flood basins
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/delta_plain
- **Other Properties:**

[]{#lower_delta_plain}

########  lower delta plain setting
- **Child of**:
 [`delta plain setting`](#delta_plain)
 [`tidal setting`](#tidal_setting)
- The part of a delta plain which is penetrated by saline water and is
subject to tidal processes
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_delta_plain
- **Other Properties:**

[]{#upper_delta_plain}

########  upper delta plain setting
- **Child of**:
 [`delta plain setting`](#delta_plain)
 [`terrestrial setting`](#terrestrial_setting)
- The part of a delta plain essentially unaffected by basinal
processes. They do not differ substantially from alluvial environments
except that areas of swamp, marsh and lakes are usually more
widespread and channels may bifurcate downstream
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_delta_plain
- **Other Properties:**

[]{#distributary_channel}

#######  delta distributary channel setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
- A divergent stream flowing away from the main stream and not
returning to it, as in a delta or on an alluvial plain
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/distributary_channel
- **Other Properties:**

[]{#distributary_mouth}

#######  delta distributary mouth setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
- The mouth of a delta distributary channel where fluvial discharge
moves from confined to unconfined flow conditions
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/distributary_mouth
- **Other Properties:**

[]{#estuarine_delta}

#######  estuarine delta setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`estuary setting`](#estuary_setting)
- A delta that has filled, or is in the process of filling, an estuary
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/estuarine_delta
- **Other Properties:**

[]{#interdistributary_bay}

#######  interdistributary bay setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`subaqueous setting`](#subaqueous_setting)
- A pronounced indentation of the delta front between advancing stream
distributaries, occupied by shallow water, and either open to the sea
or partly enclosed by minor distributaries
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/interdistributary_bay
- **Other Properties:**

[]{#lacustrine_delta}

#######  lacustrine delta setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`lacustrine setting`](#lacustrine_setting)
- The low, nearly flat, alluvial tract of land at or near the mouth of
a river, commonly forming a triangular or fan-shaped plain of
considerable area, crossed by many distributaries of the main river,
perhaps extending beyond the general trend of the lake shore,
resulting from the accumulation of sediment supplied by the river in
such quantities that it is not removed by waves or currents. Most
deltas are partly subaerial and partly below water.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine_delta
- **Other Properties:**

[]{#prodelta}

#######  prodelta setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`subaqueous setting`](#subaqueous_setting)
- The part of a delta that is below the effective depth of wave
erosion, lying beyond the delta front, and sloping gently down to the
floor of the basin into which the delta is advancing and where clastic
river sediment ceases to be a significant part of the basin-floor
deposits, it is entirely below the water level
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/prodelta
- **Other Properties:**

[]{#estuary_setting}

######  estuary setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- Environments at the seaward end or the widened funnel-shaped tidal
mouth of a river valley where fresh water comes into contact with
seawater and where tidal effects are evident (adapted from Glossary of
Geology, Jackson, 1997, p. 217).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/estuary_setting
- **Other Properties:**

[]{#estuarine_delta}

#######  estuarine delta setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`estuary setting`](#estuary_setting)
- A delta that has filled, or is in the process of filling, an estuary
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/estuarine_delta
- **Other Properties:**

[]{#estuarine_lagoon}

#######  estuarine lagoon setting
- **Child of**:
 [`estuary setting`](#estuary_setting)
 [`lagoonal setting`](#lagoonal_setting)
- A lagoon produced by the temporary sealing of a river estuary by a
storm barrier. Such lagoons are usually seasonal and exist until the
river breaches the barrier, they occur in regions of low or spasmodic
rainfall
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/estuarine_lagoon
- **Other Properties:**

[]{#lagoonal_setting}

######  lagoonal setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- A shallow stretch of salt or brackish water, partly or completely
separated from a sea or lake by an offshore reef, barrier island, sand
or spit (Jackson, 1997). Water is shallow, tidal and wave-produced
effects on sediments, strong light reaches sediment..
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lagoonal_setting
- **Other Properties:**

[]{#barrier_lagoon}

#######  barrier lagoon setting
- **Child of**:
 [`barrier island coastline setting`](#barrier_island_coastline_setting)
 [`lagoonal setting`](#lagoonal_setting)
- A lagoon that is roughly parallel to the coast and is separated from
the open ocean by a strip of land or by a barrier reef. Tidal
influence is typically restricted and the lagoon is commonly
hypersaline.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/barrier_lagoon
- **Other Properties:**

[]{#estuarine_lagoon}

#######  estuarine lagoon setting
- **Child of**:
 [`estuary setting`](#estuary_setting)
 [`lagoonal setting`](#lagoonal_setting)
- A lagoon produced by the temporary sealing of a river estuary by a
storm barrier. Such lagoons are usually seasonal and exist until the
river breaches the barrier, they occur in regions of low or spasmodic
rainfall
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/estuarine_lagoon
- **Other Properties:**

[]{#low_energy_shoreline_setting}

######  low energy shoreline setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- Settings characterized by very low surface slope and proximity to
shoreline. Generally within peritidal setting, but characterized by
low surface gradients and generally low-energy sedimentary processes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/low_energy_shoreline_setting
- **Other Properties:**

[]{#algal_flat_setting}

#######  algal flat setting
- **Child of**:
 [`low energy shoreline setting`](#low_energy_shoreline_setting)
- Modern algal flats are found on rock or mud in areas flooded only by
the highest tides and are often subject to high evaporation rates.
Algal flats survive only when an area is salty enough to eliminate
snails and other herbivorous animals that eat algae, yet is not so
salty that the algae cannot survive. The most common species of algae
found on algal flats are blue-green algae of the genera Scytonema and
Schizothrix. These algae can tolerate the daily extremes in
temperature and oxygen that typify conditions on the flats. Other
plants sometimes found on algal flats include one-celled green algae,
flagellates, diatoms, bacteria, and isolated scrubby red and black
mangroves, as well as patches of saltwort. Animals include false
cerith, cerion snails, fiddler crabs, and great land crabs. Flats with
well developed algal mats are restricted for the most part to the
Keys, with Sugarloaf and Crane Keys offering prime examples of algal
flat habitat. (Audubon, 1991)
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/algal_flat_setting
- **Other Properties:**

[]{#marginal_marine_sabkha_setting}

#######  marginal marine sabkha setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`low energy shoreline setting`](#low_energy_shoreline_setting)
- Setting characterized by arid to semi-arid conditions on restricted
coastal plains mostly above normal high tide level, with evaporite-
saline mineral, tidal-flood, and eolian deposits. Boundaries with
intertidal setting and non-tidal terrestrial setting are gradational.
(Jackson, 1997, p. 561).
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/marginal_marine_sabkha_setting
- **Other Properties:**

[]{#mud_flat_setting}

#######  mud flat setting
- **Child of**:
 [`low energy shoreline setting`](#low_energy_shoreline_setting)
- A relatively level area of fine grained material (e.g. silt) along a
shore (as in a sheltered estuary or chenier-plain) or around an
island, alternately covered and uncovered by the tide or covered by
shallow water, and barren of vegetation. Includes most tidal flats,
but lacks denotation of tidal influence.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/mud_flat_setting
- **Other Properties:**

[]{#rocky_coast_setting}

######  rocky coast setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- Shoreline with significant relief and abundant rock outcrop.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/rocky_coast_setting
- **Other Properties:**

[]{#strandplain_setting}

######  strandplain setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A prograded shore built seaward by waves and currents, and
continuous for some distance along the coast. It is characterized by
subparallel beach ridges and swales, in places with associated dunes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/strandplain_setting
- **Other Properties:**

[]{#supratidal}

######  supratidal setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Pertaining to the shore area marginal to the littoral zone, just
above high-tide level
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/supratidal
- **Other Properties:**

[]{#tidal_setting}

######  tidal setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
- Setting subject to tidal processes
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tidal_setting
- **Other Properties:**

[]{#intertidal}

#######  intertidal setting
- **Child of**:
 [`subaqueous setting`](#subaqueous_setting)
 [`tidal setting`](#tidal_setting)
- Pertaining to the benthic ocean environment or depth zone between
high water and low water, also, pertaining to the organisms of that
environment
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/intertidal
- **Other Properties:**

[]{#lower_delta_plain}

#######  lower delta plain setting
- **Child of**:
 [`delta plain setting`](#delta_plain)
 [`tidal setting`](#tidal_setting)
- The part of a delta plain which is penetrated by saline water and is
subject to tidal processes
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_delta_plain
- **Other Properties:**

[]{#tidal_channel}

#######  tidal channel setting
- **Child of**:
 [`subaqueous setting`](#subaqueous_setting)
 [`tidal setting`](#tidal_setting)
- A major channel followed by the tidal currents, extending from
offshore into a tidal marsh or a tidal flat.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tidal_channel
- **Other Properties:**

[]{#tidal_flat_setting}

#######  tidal flat setting
- **Child of**:
 [`tidal setting`](#tidal_setting)
- An extensive, nearly horizontal, barren tract of land that is
alternately covered and uncovered by the tide, and consisting of
unconsolidated sediment (mostly mud and sand). It may form the top
surface of a deltaic deposit.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tidal_flat_setting
- **Other Properties:**

[]{#tidal_marsh}

########  tidal marsh setting
- **Child of**:
 [`swamp or marsh setting`](#swamp_or_marsh_setting)
 [`tidal flat setting`](#tidal_flat_setting)
- A marsh bordering a coast (as in a shallow lagoon or sheltered bay),
formed of mud and of the resistant mat of roots of salt-tolerant
plants, and regularly inundated during high tides, a marshy tidal
flat.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tidal_marsh
- **Other Properties:**

[]{#subaqueous_setting}

#####  subaqueous setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting situated in or under permanent, standing water. Used for
marine and lacustrine settings, but not for fluvial settings.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/subaqueous_setting
- **Other Properties:**

[]{#interdistributary_bay}

######  interdistributary bay setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`subaqueous setting`](#subaqueous_setting)
- A pronounced indentation of the delta front between advancing stream
distributaries, occupied by shallow water, and either open to the sea
or partly enclosed by minor distributaries
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/interdistributary_bay
- **Other Properties:**

[]{#intertidal}

######  intertidal setting
- **Child of**:
 [`subaqueous setting`](#subaqueous_setting)
 [`tidal setting`](#tidal_setting)
- Pertaining to the benthic ocean environment or depth zone between
high water and low water, also, pertaining to the organisms of that
environment
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/intertidal
- **Other Properties:**

[]{#marine_setting}

######  marine setting
- **Child of**:
 [`subaqueous setting`](#subaqueous_setting)
- Setting characterized by location under the surface of the sea.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/marine_setting
- **Other Properties:**

[]{#above_carbonate_compensation_depth_setting}

#######  above carbonate compensation depth setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Marine environment in which carbonate sediment does not dissolve
before reaching the sea floor and can accumulate.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/above_carbonate_compensation_depth_setting
- **Other Properties:**

[]{#abyssal}

#######  abyssal setting
- **Child of**:
 [`marine setting`](#marine_setting)
- The ocean environment at water depths between 3500 and 6000 metres
- **Alternate labels:**
laut dalam, 
tubir, 
深成的, 
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/abyssal
- **Other Properties:**

[]{#basin_plain_setting}

#######  basin plain setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Near flat areas of ocean floor, slope less than 1:1000, generally
receive only distal turbidite and pelagic sediments.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/basin_plain_setting
- **Other Properties:**

[]{#bathyal}

#######  bathyal setting
- **Child of**:
 [`marine setting`](#marine_setting)
- The ocean environment at water depths between 200 and 3500 metres
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/bathyal
- **Other Properties:**

[]{#lower_bathyal}

########  lower bathyal setting
- **Child of**:
 [`bathyal setting`](#bathyal)
- The ocean environment at depths between 1000 and 3500 metres
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lower_bathyal
- **Other Properties:**

[]{#middle_bathyal}

########  middle bathyal setting
- **Child of**:
 [`bathyal setting`](#bathyal)
- The ocean environment at water depths between 600 and 1000 metres
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/middle_bathyal
- **Other Properties:**

[]{#upper_bathyal}

########  upper bathyal setting
- **Child of**:
 [`bathyal setting`](#bathyal)
- The ocean environment at water depths between 200 and 600 metres
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_bathyal
- **Other Properties:**

[]{#below_carbonate_compensation_depth_setting}

#######  below carbonate compensation depth setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Marine environment in which water is deep enough that carbonate
sediment goes into solution before it can accumulate on the sea floor.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/below_carbonate_compensation_depth_setting
- **Other Properties:**

[]{#biological_reef_setting}

#######  biological reef setting
- **Child of**:
 [`marine setting`](#marine_setting)
- A ridgelike or moundlike structure, layered or massive, built by
sedentary calcareous organisms, esp. corals, and consisting mostly of
their remains, it is wave-resistant and stands topographically above
the surrounding contemporaneously deposited sediment.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/biological_reef_setting
- **Other Properties:**

[]{#backreef}

########  backreef setting
- **Child of**:
 [`biological reef setting`](#biological_reef_setting)
- The landward side of a reef. The term is often used adjectivally to
refer to deposits within the restricted lagoon behind a barrier reef,
such as the back-reef facies of lagoonal deposits. In some places, as
on a platform-edge reef tract, back reef refers to the side of the
reef away from the open sea, even though no land may be nearby
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/backreef
- **Other Properties:**

[]{#forereef}

########  forereef setting
- **Child of**:
 [`biological reef setting`](#biological_reef_setting)
- The seaward side of a reef, the slope covered with deposits of
coarse reef talus
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/forereef
- **Other Properties:**

[]{#reef_flat}

########  reef flat setting
- **Child of**:
 [`biological reef setting`](#biological_reef_setting)
- A stony platform of reef rock, landward of the reef crest at or
above the low tide level, occasionally with patches of living coral
and associated organisms, and commonly strewn with coral fragments and
coral sand. It may include shallow pools, irregular gullies, low
islands of sand or rubble (often vegetated, esp. by palms), and
scattered colonies of the more hardy species of coral
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/reef_flat
- **Other Properties:**

[]{#continental_borderland_setting}

#######  continental borderland setting
- **Child of**:
 [`marine setting`](#marine_setting)
- An area of the continental margin between the shoreline and the
continental slope that is topographically more complex than the
continental shelf. It is characterized by ridges and basins, some of
which are below the depth of the continental shelf. An example is the
southern California continental borderland,.... (Jackson, 1997, p.
138)..
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/continental_borderland_setting
- **Other Properties:**

[]{#continental_shelf_setting}

#######  continental shelf setting
- **Child of**:
 [`marine setting`](#marine_setting)
- That part of the ocean floor that is between the shoreline and the
continental slope (or, when there is no noticeable continental slope,
a depth of 200 m). It is characterized by its gentle slope of 0.1
degree (Jackson, 1997, p. 138). Continental shelves have a classic
shoreline-shelf-slope profile termed 'clinoform'.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/continental_shelf_setting
- **Other Properties:**

[]{#deep_sea_trench}

#######  deep sea trench setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Deep ocean basin with steep (average 10 degrees) slope toward land,
more gentle slope (average 5 degrees) towards the sea, and abundant
seismic activity on landward side of trench. Does not denote water
depth, but may be very deep.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/deep_sea_trench
- **Other Properties:**

[]{#epicontinental_marine_setting}

#######  epicontinental marine setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Marine setting situated within the interior of the continent, rather
than at the edge of a continent.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/epicontinental_marine_setting
- **Other Properties:**

[]{#hadal}

#######  hadal setting
- **Child of**:
 [`marine setting`](#marine_setting)
- The deepest oceanic environment, i.e., over 6000 m in depth. Always
in deep sea trench.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/hadal
- **Other Properties:**

[]{#marine_carbonate_platform_setting}

#######  marine carbonate platform setting
- **Child of**:
 [`marine setting`](#marine_setting)
- A shallow submerged plateau separated from continental landmasses,
on which high biological carbonate production rates produce enough
sediment to maintain the platform surface near sea level. Grades into
atoll as area becomes smaller and ringing coral reefs become more
prominent part of the setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/marine_carbonate_platform_setting
- **Other Properties:**

[]{#neritic}

#######  neritic setting
- **Child of**:
 [`marine setting`](#marine_setting)
- The ocean environment at depths between low-tide level and 200
metres, or between low-tide level and approximately the edge of the
continental shelf
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/neritic
- **Other Properties:**

[]{#inner_neritic}

########  inner neritic setting
- **Child of**:
 [`neritic setting`](#neritic)
- The ocean environment at depths between low tide level and 30 metres
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/inner_neritic
- **Other Properties:**

[]{#middle_neritic}

########  middle neritic setting
- **Child of**:
 [`neritic setting`](#neritic)
- The ocean environment at depths between 30 and 100 metres
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/middle_neritic
- **Other Properties:**

[]{#outer_neritic}

########  outer neritic setting
- **Child of**:
 [`neritic setting`](#neritic)
- The ocean environment at depths between 100 and 200 metres or
between low-tide level and approximately the edge of the continental
shelf
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/outer_neritic
- **Other Properties:**

[]{#ocean_highland_setting}

#######  ocean highland setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Broad category for subaqueous marine settings characterized by
significant relief above adjacent sea floor.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/ocean_highland_setting
- **Other Properties:**

[]{#mid_ocean_ridge_setting}

########  mid ocean ridge setting
- **Child of**:
 [`ocean highland setting`](#ocean_highland_setting)
- Ocean highland associated with a divergent continental margin
(spreading center). Setting is characterized by active volcanism,
locally steep reliefhydrothermal activity, and pelagic sedimentation.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/mid_ocean_ridge_setting
- **Other Properties:**

[]{#oceanic_plateau_setting}

########  oceanic plateau setting
- **Child of**:
 [`ocean highland setting`](#ocean_highland_setting)
- Region of elevated ocean crust that commonly rises to within 2-3 km
of the surface above an abyssal sea floor that lies several km deeper.
Climate and water depths are such that a marine carbonate platform
does not develop.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/oceanic_plateau_setting
- **Other Properties:**

[]{#seamount_setting}

########  seamount setting
- **Child of**:
 [`intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`ocean highland setting`](#ocean_highland_setting)
- Setting that consists of a conical mountain on the ocean floor
(guyot). Typically characterized by active volcanism, pelagic
sedimentation. If the mountain is high enough to reach the photic
zone, carbonate production may result in reef building to produce a
carbonate platform or atoll setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/seamount_setting
- **Other Properties:**

[]{#slope_rise_setting}

#######  slope rise setting
- **Child of**:
 [`marine setting`](#marine_setting)
- The part of a subaqueous basin that is between a bordering shelf
setting, which separate the basin from an adjacent landmass, and a
very low-relief basin plain setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/slope_rise_setting
- **Other Properties:**

[]{#submarine_fan_setting}

#######  submarine fan setting
- **Child of**:
 [`marine setting`](#marine_setting)
- Large fan-shaped cones of sediment on the ocean floor, generally
associated with submarine canyons that provide sediment supply to
build the fan..
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/submarine_fan_setting
- **Other Properties:**

[]{#prodelta}

######  prodelta setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`subaqueous setting`](#subaqueous_setting)
- The part of a delta that is below the effective depth of wave
erosion, lying beyond the delta front, and sloping gently down to the
floor of the basin into which the delta is advancing and where clastic
river sediment ceases to be a significant part of the basin-floor
deposits, it is entirely below the water level
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/prodelta
- **Other Properties:**

[]{#tidal_channel}

######  tidal channel setting
- **Child of**:
 [`subaqueous setting`](#subaqueous_setting)
 [`tidal setting`](#tidal_setting)
- A major channel followed by the tidal currents, extending from
offshore into a tidal marsh or a tidal flat.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tidal_channel
- **Other Properties:**

[]{#terrestrial_setting}

#####  terrestrial setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting characterized by absence of direct marine influence. Most of
the subaerial settings are also terrestrial, but lacustrine settings,
while terrestrial, are not subaerial, so the subaerial settings are
not included as subcategories.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/terrestrial_setting
- **Other Properties:**

[]{#aeolian_process_setting}

######  aeolian process setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Sedimentary setting in which wind is the dominant process producing,
transporting, and depositing sediment. Typically has low-relief plain
or piedmont slope physiography.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/aeolian_process_setting
- **Other Properties:**

[]{#dunefield}

#######  dunefield setting
- **Child of**:
 [`aeolian process setting`](#aeolian_process_setting)
- Extensive deposits on sand in an area where the supply is abundant.
As a characteristic, individual dunes somewhat resemble barchans but
are highly irregular in shape and crowded, erg areas of the Sahara are
an example.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/dunefield
- **Other Properties:**

[]{#coastal_dune_field}

########  coastal dune field setting
- **Child of**:
 [`dunefield setting`](#dunefield)
- A dune field on low-lying land recently abandoned or built up by the
sea, the dunes may ascend a cliff and travel inland.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/coastal_dune_field
- **Other Properties:**

[]{#sand_plain}

#######  sand plain setting
- **Child of**:
 [`aeolian process setting`](#aeolian_process_setting)
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
- A sand-covered plain dominated by aeolian processes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/sand_plain
- **Other Properties:**

[]{#bog}

######  bog setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`wetland setting`](#wetland_setting)
- Waterlogged, spongy ground, consisting primarily of mosses,
containing acidic, decaying vegetation that may develop into peat.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/bog
- **Other Properties:**

[]{#basin_bog}

#######  basin bog setting
- **Child of**:
 [`bog setting`](#bog)
- An ombrotrophic or ombrogene peat/bog whose nutrient supply is
exclusively from rain water (including snow and atmospheric fallout)
therefore making nutrients extremely oligotrophic
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/basin_bog
- **Other Properties:**

[]{#blanket_bog}

#######  blanket bog
- **Child of**:
 [`bog setting`](#bog)
- Topogeneous bog/peat whose moisture content is largely dependent on
surface water. It is relatively rich in plant nutrients, nitrogen, and
mineral matter, is mildly acidic to nearly neutral, and contains
little or no cellulose, forms in topographic depressions with
essential stagnat or non-moving minerotrophic water supply
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/blanket_bog
- **Other Properties:**

[]{#gibber_plain}

######  gibber plain setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/gibber_plain
- **Other Properties:**

[]{#glacial_outwash_plain_setting}

######  glacial outwash plain setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Glacier environment`](#glacierenvironment)
- Areas adjacent to glacial front dominated by sediment and water
supplied by glacial melting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacial_outwash_plain_setting
- **Other Properties:**

[]{#lacustrine_setting}

######  lacustrine setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
- Setting associated with a lake. Always overlaps with terrestrial,
may overlap with subaerial, subaqueous, or shoreline.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine_setting
- **Other Properties:**

[]{#lacustrine_delta}

#######  lacustrine delta setting
- **Child of**:
 [`deltaic system setting`](#deltaic_system_setting)
 [`lacustrine setting`](#lacustrine_setting)
- The low, nearly flat, alluvial tract of land at or near the mouth of
a river, commonly forming a triangular or fan-shaped plain of
considerable area, crossed by many distributaries of the main river,
perhaps extending beyond the general trend of the lake shore,
resulting from the accumulation of sediment supplied by the river in
such quantities that it is not removed by waves or currents. Most
deltas are partly subaerial and partly below water.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/lacustrine_delta
- **Other Properties:**

[]{#piedmont_slope_system_setting}

######  piedmont slope system setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Location on gentle slope at the foot of a mountain, generally used
in terms of intermontane-basin terrain. Main components include: (a)
An erosional surface on bedrock adjacent to the receding mountain
front (pediment, rock pediment), (b) A constructional surface
comprising individual alluvial fans and interfan valleys, also near
the mountain front, and (c) A distal complex of coalescent fans
(bajada), and alluvial slopes without fan form. Piedmont slopes grade
to basin-floor depressions with alluvial and temporary lake plains or
to surfaces associated with through drainage.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/piedmont_slope_system_setting
- **Other Properties:**

[]{#alluvial_fan}

#######  alluvial fan setting
- **Child of**:
 [`piedmont slope system setting`](#piedmont_slope_system_setting)
- A low, outspread, relatively flat to gently sloping mass of loose
rock material, shaped like an open fan or a segment of a cone,
deposited by a stream (esp. in a semiarid region) at the place where
it issues from a narrow mountain valley upon a plain or broad valley,
or where a tributary stream is near or at its junction with the main
stream, or wherever a constriction in a valley abruptly ceases or the
gradient of the stream suddenly decreases, it is steepest near the
mouth of the valley where its apex points upstream, and it slopes
gently and convexly outward with gradually decreasing gradient
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/alluvial_fan
- **Other Properties:**

[]{#alluvial_plain}

#######  alluvial plain setting
- **Child of**:
 [`piedmont slope system setting`](#piedmont_slope_system_setting)
- An assemblage landforms produced by alluvial and fluvial processes
(braided streams, terraces, etc.) that form low gradient, regional
ramps along the flanks of mountains and extend great distances from
their sources (e.g.high Plains of North America). (NRCS GLOSSARY OF
LANDFORM AND GEOLOGIC TERMS). A level or gently sloping tract or a
slightly undulating land surface produced by extensive deposition of
alluvium... Synonym-- wash plain,...river plain, aggraded valley
plain,... (Jackson, 1997, p. 17). May include one or more River plain
systems.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/alluvial_plain
- **Other Properties:**

[]{#pediment_setting}

#######  pediment setting
- **Child of**:
 [`piedmont slope system setting`](#piedmont_slope_system_setting)
- A gently sloping erosional surface developed at the foot of a
receding hill or mountain slope. The surface may be essentially bare,
exposing earth material that extends beneath adjacent uplands, or it
may be thinly mantled with alluvium and colluvium, ultimately in
transit from upland front to basin or valley lowland. In hill-foot
slope terrain the mantle is designated \pedisediment.\ The term has
been used in several geomorphic contexts: Pediments may be classed
with respect to (a) landscape positions, for example, intermontane-
basin piedmont or valley-border footslope surfaces (respectively,
apron and terrace pediments (Cooke and Warren, 1973)), (b) type of
material eroded, bedrock or regolith, or (c) combinations of the
above. Compare - Piedmont slope..
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/pediment_setting
- **Other Properties:**

[]{#playa_setting}

######  playa setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/playa_setting
- **Other Properties:**

[]{#river_plain_system_setting}

######  river plain system setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Geologic setting dominated by a river system, river plains may occur
in any climatic setting. Includes active channels, abandoned channels,
levees, oxbow lakes, flood plain. May be part of an alluvial plain
that includes terraces composed of abandoned river plain deposits.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/river_plain_system_setting
- **Other Properties:**

[]{#abandoned_channel}

#######  abandoned river channel setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- A drainage channel along which runoff no longer occurs, as on an
alluvial fan
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/abandoned_channel
- **Other Properties:**

[]{#cutoff_meander}

#######  cutoff meander setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- The abandoned, bow- or horseshoe-shaped channel of a former meander,
left when the stream formed a cutoff across a narrow meander neck.
Note that these are typically lakes, thus also lacustrine.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/cutoff_meander
- **Other Properties:**

[]{#floodplain}

#######  floodplain setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- The surface or strip of relatively smooth land adjacent to a river
channel, constructed by the present river in its existing regimen and
covered with water when the river overflows its banks. It is built of
alluvium carried by the river during floods and deposited in the
sluggish water beyond the influence of the swiftest current. A river
has one floodplain and may have one or more terraces representing
abandoned floodplains
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/floodplain
- **Other Properties:**

[]{#river_channel}

#######  river channel setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- The bed where a natural body of surface water flows or may flow, a
natural passageway or depression of perceptible extent containing
continuously or periodically flowing water, or forming a connecting
link between two bodies of water, a watercourse
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/river_channel
- **Other Properties:**

[]{#braided_channel}

########  braided river channel setting
- **Child of**:
 [`river channel setting`](#river_channel)
- A stream that divides into or follows an interlacing or tangled
network of several small branching and reuniting shallow channels
separated from each other by ephemeral branch islands or channel bars,
resembling in plan the strands of a complex braid. Such a stream is
generally believed to indicate an inability to carry all of its load,
such as an overloaded and aggrading stream flowing in a wide channel
on a floodplain
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/braided_channel
- **Other Properties:**

[]{#meandering_channel}

########  meandering river channel setting
- **Child of**:
 [`river channel setting`](#river_channel)
- Produced by a mature stream swinging from side to side as it flows
across its floodplain or shifts its course laterally toward the convex
side of an original curve
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/meandering_channel
- **Other Properties:**

[]{#sand_plain}

######  sand plain setting
- **Child of**:
 [`aeolian process setting`](#aeolian_process_setting)
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
- A sand-covered plain dominated by aeolian processes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/sand_plain
- **Other Properties:**

[]{#upper_delta_plain}

######  upper delta plain setting
- **Child of**:
 [`delta plain setting`](#delta_plain)
 [`terrestrial setting`](#terrestrial_setting)
- The part of a delta plain essentially unaffected by basinal
processes. They do not differ substantially from alluvial environments
except that areas of swamp, marsh and lakes are usually more
widespread and channels may bifurcate downstream
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/upper_delta_plain
- **Other Properties:**

[]{#wetland_setting}

#####  wetland setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting characterized by gentle surface slope, and at least
intermittent presence of standing water, which may be fresh, brackish,
or saline. Wetland may be terrestrial setting or shoreline setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/wetland_setting
- **Other Properties:**

[]{#bog}

######  bog setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`wetland setting`](#wetland_setting)
- Waterlogged, spongy ground, consisting primarily of mosses,
containing acidic, decaying vegetation that may develop into peat.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/bog
- **Other Properties:**

[]{#basin_bog}

#######  basin bog setting
- **Child of**:
 [`bog setting`](#bog)
- An ombrotrophic or ombrogene peat/bog whose nutrient supply is
exclusively from rain water (including snow and atmospheric fallout)
therefore making nutrients extremely oligotrophic
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/basin_bog
- **Other Properties:**

[]{#blanket_bog}

#######  blanket bog
- **Child of**:
 [`bog setting`](#bog)
- Topogeneous bog/peat whose moisture content is largely dependent on
surface water. It is relatively rich in plant nutrients, nitrogen, and
mineral matter, is mildly acidic to nearly neutral, and contains
little or no cellulose, forms in topographic depressions with
essential stagnat or non-moving minerotrophic water supply
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/blanket_bog
- **Other Properties:**

[]{#swamp_or_marsh_setting}

######  swamp or marsh setting
- **Child of**:
 [`wetland setting`](#wetland_setting)
- A water-saturated, periodically wet or continually flooded area with
the surface not deeply submerged, essentially without the formation of
peat. Marshes are characterized by sedges, cattails, rushes, or other
aquatic and grasslike vegetation. Swamps are characterized by tree and
brush vegetation.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/swamp_or_marsh_setting
- **Other Properties:**

[]{#tidal_marsh}

#######  tidal marsh setting
- **Child of**:
 [`swamp or marsh setting`](#swamp_or_marsh_setting)
 [`tidal flat setting`](#tidal_flat_setting)
- A marsh bordering a coast (as in a shallow lagoon or sheltered bay),
formed of mud and of the resistant mat of roots of salt-tolerant
plants, and regularly inundated during high tides, a marshy tidal
flat.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/tidal_marsh
- **Other Properties:**

[]{#lakeriverstreambottom}

#####  Lake river or stream bottom
- **Child of**:
 [`Earth surface`](#earthsurface)
- Sampled feature is the interface between the solid Earth interface
and a lake or flowing water body.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/lakeriverstreambottom
- **Other Properties:**

[]{#marinewaterbodybottom}

#####  Marine water body bottom
- **Child of**:
 [`Earth surface`](#earthsurface)
- Sampled feature is the interface between the solid Earth and a
marine or brackish water body. Includes benthic boundary layer:  the
bottom layer of water and the uppermost layer of sediment directly
influenced by the overlying water.
- **Alternate labels:**
Sea floor
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/marinewaterbodybottom
- **Other Properties:**

[]{#subaerialsurfaceenvironment}

#####  Subaerial surface environment
* `subaerial setting`
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting at the interface between the solid earth and the atmosphere,
includes some shallow subaqueous settings in river channels and
playas. Characterized by conditions and processes, such as erosion,
that exist or operate in the open air on or immediately adjacent to
the land surface
- sampled feature is the interface between solid Earth and atmosphere.
Sample is collected on the surface, or immediately below surface (zone
of bioturbation). Include soil and recently deposited subaerial
sediment at the surface.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/subaerialsurfaceenvironment
- **Other Properties:**

[]{#aeolian_process_setting}

######  aeolian process setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Sedimentary setting in which wind is the dominant process producing,
transporting, and depositing sediment. Typically has low-relief plain
or piedmont slope physiography.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/aeolian_process_setting
- **Other Properties:**

[]{#dunefield}

#######  dunefield setting
- **Child of**:
 [`aeolian process setting`](#aeolian_process_setting)
- Extensive deposits on sand in an area where the supply is abundant.
As a characteristic, individual dunes somewhat resemble barchans but
are highly irregular in shape and crowded, erg areas of the Sahara are
an example.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/dunefield
- **Other Properties:**

[]{#coastal_dune_field}

########  coastal dune field setting
- **Child of**:
 [`dunefield setting`](#dunefield)
- A dune field on low-lying land recently abandoned or built up by the
sea, the dunes may ascend a cliff and travel inland.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/coastal_dune_field
- **Other Properties:**

[]{#sand_plain}

#######  sand plain setting
- **Child of**:
 [`aeolian process setting`](#aeolian_process_setting)
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
- A sand-covered plain dominated by aeolian processes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/sand_plain
- **Other Properties:**

[]{#coastal_plain_setting}

######  coastal plain setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A low relief plain bordering a water body extending inland to the
nearest elevated land, sloping very gently towards the water body.
Distinguished from alluvial plain by presence of relict shoreline-
related deposits or morphology.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/coastal_plain_setting
- **Other Properties:**

[]{#gibber_plain}

######  gibber plain setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/gibber_plain
- **Other Properties:**

[]{#piedmont_slope_system_setting}

######  piedmont slope system setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Location on gentle slope at the foot of a mountain, generally used
in terms of intermontane-basin terrain. Main components include: (a)
An erosional surface on bedrock adjacent to the receding mountain
front (pediment, rock pediment), (b) A constructional surface
comprising individual alluvial fans and interfan valleys, also near
the mountain front, and (c) A distal complex of coalescent fans
(bajada), and alluvial slopes without fan form. Piedmont slopes grade
to basin-floor depressions with alluvial and temporary lake plains or
to surfaces associated with through drainage.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/piedmont_slope_system_setting
- **Other Properties:**

[]{#alluvial_fan}

#######  alluvial fan setting
- **Child of**:
 [`piedmont slope system setting`](#piedmont_slope_system_setting)
- A low, outspread, relatively flat to gently sloping mass of loose
rock material, shaped like an open fan or a segment of a cone,
deposited by a stream (esp. in a semiarid region) at the place where
it issues from a narrow mountain valley upon a plain or broad valley,
or where a tributary stream is near or at its junction with the main
stream, or wherever a constriction in a valley abruptly ceases or the
gradient of the stream suddenly decreases, it is steepest near the
mouth of the valley where its apex points upstream, and it slopes
gently and convexly outward with gradually decreasing gradient
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/alluvial_fan
- **Other Properties:**

[]{#alluvial_plain}

#######  alluvial plain setting
- **Child of**:
 [`piedmont slope system setting`](#piedmont_slope_system_setting)
- An assemblage landforms produced by alluvial and fluvial processes
(braided streams, terraces, etc.) that form low gradient, regional
ramps along the flanks of mountains and extend great distances from
their sources (e.g.high Plains of North America). (NRCS GLOSSARY OF
LANDFORM AND GEOLOGIC TERMS). A level or gently sloping tract or a
slightly undulating land surface produced by extensive deposition of
alluvium... Synonym-- wash plain,...river plain, aggraded valley
plain,... (Jackson, 1997, p. 17). May include one or more River plain
systems.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/alluvial_plain
- **Other Properties:**

[]{#pediment_setting}

#######  pediment setting
- **Child of**:
 [`piedmont slope system setting`](#piedmont_slope_system_setting)
- A gently sloping erosional surface developed at the foot of a
receding hill or mountain slope. The surface may be essentially bare,
exposing earth material that extends beneath adjacent uplands, or it
may be thinly mantled with alluvium and colluvium, ultimately in
transit from upland front to basin or valley lowland. In hill-foot
slope terrain the mantle is designated \pedisediment.\ The term has
been used in several geomorphic contexts: Pediments may be classed
with respect to (a) landscape positions, for example, intermontane-
basin piedmont or valley-border footslope surfaces (respectively,
apron and terrace pediments (Cooke and Warren, 1973)), (b) type of
material eroded, bedrock or regolith, or (c) combinations of the
above. Compare - Piedmont slope..
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/pediment_setting
- **Other Properties:**

[]{#playa_setting}

######  playa setting
- **Child of**:
 [`arid or semi arid environment setting`](#arid_or_semi_arid_environment_setting)
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/playa_setting
- **Other Properties:**

[]{#river_plain_system_setting}

######  river plain system setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Geologic setting dominated by a river system, river plains may occur
in any climatic setting. Includes active channels, abandoned channels,
levees, oxbow lakes, flood plain. May be part of an alluvial plain
that includes terraces composed of abandoned river plain deposits.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/river_plain_system_setting
- **Other Properties:**

[]{#abandoned_channel}

#######  abandoned river channel setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- A drainage channel along which runoff no longer occurs, as on an
alluvial fan
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/abandoned_channel
- **Other Properties:**

[]{#cutoff_meander}

#######  cutoff meander setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- The abandoned, bow- or horseshoe-shaped channel of a former meander,
left when the stream formed a cutoff across a narrow meander neck.
Note that these are typically lakes, thus also lacustrine.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/cutoff_meander
- **Other Properties:**

[]{#floodplain}

#######  floodplain setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- The surface or strip of relatively smooth land adjacent to a river
channel, constructed by the present river in its existing regimen and
covered with water when the river overflows its banks. It is built of
alluvium carried by the river during floods and deposited in the
sluggish water beyond the influence of the swiftest current. A river
has one floodplain and may have one or more terraces representing
abandoned floodplains
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/floodplain
- **Other Properties:**

[]{#river_channel}

#######  river channel setting
- **Child of**:
 [`river plain system setting`](#river_plain_system_setting)
- The bed where a natural body of surface water flows or may flow, a
natural passageway or depression of perceptible extent containing
continuously or periodically flowing water, or forming a connecting
link between two bodies of water, a watercourse
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/river_channel
- **Other Properties:**

[]{#braided_channel}

########  braided river channel setting
- **Child of**:
 [`river channel setting`](#river_channel)
- A stream that divides into or follows an interlacing or tangled
network of several small branching and reuniting shallow channels
separated from each other by ephemeral branch islands or channel bars,
resembling in plan the strands of a complex braid. Such a stream is
generally believed to indicate an inability to carry all of its load,
such as an overloaded and aggrading stream flowing in a wide channel
on a floodplain
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/braided_channel
- **Other Properties:**

[]{#meandering_channel}

########  meandering river channel setting
- **Child of**:
 [`river channel setting`](#river_channel)
- Produced by a mature stream swinging from side to side as it flows
across its floodplain or shifts its course laterally toward the convex
side of an original curve
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/meandering_channel
- **Other Properties:**

[]{#strandplain_setting}

######  strandplain setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A prograded shore built seaward by waves and currents, and
continuous for some distance along the coast. It is characterized by
subparallel beach ridges and swales, in places with associated dunes.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/strandplain_setting
- **Other Properties:**

[]{#supratidal}

######  supratidal setting
- **Child of**:
 [`shoreline settings`](#shoreline_settings)
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Pertaining to the shore area marginal to the littoral zone, just
above high-tide level
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/supratidal
- **Other Properties:**

[]{#soilprofile}

######  soil profile setting
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
-
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/essampledfeature/0.1/soilprofile
- **Other Properties:**

[]{#glacierenvironment}

####  Glacier environment
* `glacier related setting`
- **Child of**:
 [`polar climatic setting`](#polar_climatic_setting)
 [`Earth environment`](#earthenvironment)
- Earth surface setting with geography defined by spatial relationship
to glaciers (e.g. on top of a glacier, next to a glacier, in front of
a glacier...). Processes related to moving ice dominate sediment
transport and deposition and landform development. Includes
subaqueous, shoreline, and terrestrial settings that are impacted by
the presence of glaciers. Considered a geographically defined setting
in that a glacier is a geographic feature.
- Sampled feature is a glacier, ice sheet, ice shelf, iceberg, or rock
or water directly under or on top of such ice.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/glacierenvironment
- **Other Properties:**

[]{#englacial_setting}

#####  englacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Contained, embedded, or carried within the body of a glacier or ice
sheet, said of meltwater streams, till, drift, moraine
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/englacial_setting
- **Other Properties:**

[]{#glacial_outwash_plain_setting}

#####  glacial outwash plain setting
- **Child of**:
 [`terrestrial setting`](#terrestrial_setting)
 [`Glacier environment`](#glacierenvironment)
- Areas adjacent to glacial front dominated by sediment and water
supplied by glacial melting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacial_outwash_plain_setting
- **Other Properties:**

[]{#glacier_lateral_setting}

#####  glacier lateral setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Settings adjacent to edges of confined glacier.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacier_lateral_setting
- **Other Properties:**

[]{#proglacial_setting}

#####  proglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Immediately in front of or just beyond the outer limits of a glacier
or ice sheet, generally at or near its lower end, said of lakes,
streams, deposits, and other features produced by or derived from the
glacier ice
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/proglacial_setting
- **Other Properties:**

[]{#glacier_terminus_setting}

######  glacier terminus setting
- **Child of**:
 [`proglacial setting`](#proglacial_setting)
- Region of sediment deposition due to melting of glacier ice.
ablation and flow till setting.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/glacier_terminus_setting
- **Other Properties:**

[]{#subglacial_setting}

#####  subglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Formed or accumulated in or by the bottom parts of a glacier or ice
sheet, said of meltwater streams, till, moraine, etc.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/subglacial_setting
- **Other Properties:**

[]{#supraglacial_setting}

#####  supraglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Carried upon, deposited from, or pertaining to the top surface of a
glacier or ice sheet, said of meltwater streams, till, drift, etc.
(Jackson, 1997, p. 639). Dreimanis (1988, p. 39) recommendation that
\supraglacial\ supersede \superglacial\ is followed.
- **Concept URI:** http://resource.geosciml.org/classifier/cgi/eventenvironment/supraglacial_setting
- **Other Properties:**

[]{#subsurfacefluidreservoir}

####  Subsurface fluid reservoir
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is fluid that resides in fractures, intergranular
porosity or other open space in the solid earth.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/subsurfacefluidreservoir
- **Other Properties:**

[]{#waterbody}

####  Water body
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is the Earth's hydrosphere.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/waterbody
- **Other Properties:**

[]{#marinewaterbody}

#####  Marine environment
- **Child of**:
 [`Water body`](#waterbody)
- Sampled feature is the marine hydrosphere.
- **See Also**:
* [<http://purl.obolibrary.org/obo/ENVO_01000686>](http://purl.obolibrary.org/obo/ENVO_01000686)
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/marinewaterbody
- **Other Properties:**

[]{#terrestrialwaterbody}

#####  Terrestrial water body
- **Child of**:
 [`Water body`](#waterbody)
- Sampled feature is terrestrial hydrosphere-- lake, other standing
water, or a flowing water body (river, stream..). Include saline water
in terrestrial evaporite environments.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/terrestrialwaterbody
- **Other Properties:**

[]{#extraterrestrialenvironment}

###  Extraterrestrial environment
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is the environment outside of solid earth,
hydrosphere, or atmosphere.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/1.0/extraterrestrialenvironment
- **Other Properties:**


