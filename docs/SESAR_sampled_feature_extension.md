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

Vocabulary last modified:  2024-10-03

subtitle: 
  Terms to categorize sampled features in more detail. This vocabualary extends the iSamples Sampled FEature Type vocabulary with concepts from the GeoSciML envent environment vocabulary, and adds several additional concepts.

Namespace: 
[`https://w3id.org/sesar/sampledfeature/sfvocabulary`](https://w3id.org/sesar/sampledfeature/sfvocabulary)

**History**

* 2024-08-26 SMR generate to account for sampled features in SESAR
* 2024-10-03 SMR add terms to cover data in SESAR legacy data, map to IMLGS sampled feature, and SESAR physiographic features vocabulary (https://www.geosamples.org/vocabularies/physiographic-feature).  Continue to refine structure of vocabulary, add and update definitions, mapping to ENVO terms.

- [Any sampled feature](#anysampledfeature)
    - [Anthropogenic environment](#anthropogenicenvironment)
        - [Active human occupation site](#activehumanoccupationsite)
            - [Experiment setting](#experimentsetting)
            - [Laboratory or curatorial environment](#laboratorycuratorialenvironment)
            - [Agricultural site](#agricultural_site)
            - [Canal](#canal)
            - [Mining site](#mining_site)
            - [Urban setting](#urban_setting)
        - [Site of past human activities](#pasthumanoccupationsite)
        - [Harbor](#harbor)
        - [Quarry](#quarry)
    - [Biological entity](#biologicalentity)
    - [Earth environment](#earthenvironment)
        - [Atmosphere](#atmosphere)
        - [Earth interior](#earthinterior)
            - [Contact metamorphic zone](#contact_metamorphic_zone)
            - [Crustal setting](#crust)
                - [Continental crust](#continental_crust)
                    - [Collisional setting](#collisional_setting)
                    - [Foreland setting](#foreland_setting)
                        - [Foreland basin](#foreland_basin)
                        - [Foreland fold and thrust belt](#foreland_fold_thrust_belt)
                    - [Hinterland tectonic setting](#hinterland_setting)
                    - [Lower continental crust](#lower_continental_crust)
                    - [Middle continental crust](#middle_continental_crust)
                    - [Upper continental crust](#upper_continental_crust)
                - [Ocean crust](#ocean_crust)
                    - [Lower oceanic crust](#lower_oceanic_crust)
                    - [Upper ocean crust](#upper_ocean_crust)
                - [Transitional crust](#transitional_crust)
            - [Geologic unit](#geologic_unit)
                - [Melange](#melange)
                - [Ophiolite](#ophiolite)
                - [Soil profile](#soil_profile)
                - [Stratigraphic section](#stratigraphic_section)
                - [Thrust sheet](#thrust_sheet)
                - [Xenolith](#xenolith)
            - [High pressure low temperature earth interior setting](#high_pressure_low_temperature_earth_interior_setting)
            - [Hypabyssal setting](#hypabyssal_setting)
            - [Intrusive igneous complex](#intrusive_igneous_complex)
            - [Low pressure high temperature setting](#low_pressure_high_temperature_setting)
            - [Mantle](#mantle)
                - [Lower mantle](#lower_mantle)
                - [Upper mantle](#upper_mantle)
            - [Mineralized system](#mineralized_body)
            - [Regional metamorphic setting](#regional_metamorphic_setting)
            - [Ultra high pressure crustal setting](#ultra_high_pressure_crustal_setting)
        - [Earth surface](#earthsurface)
            - [Subaerial surface environment](#subaerialsurfaceenvironment)
                - [Coastal plain](#coastal_plain)
                - [Continental divide](#continental_divide)
                - [Eolian process setting](#eolian_process_setting)
                    - [Dune](#dune)
                    - [Dunefield](#dunefield)
                        - [Coastal dune field](#coastal_dune_field)
                    - [Sand plain](#sand_plain)
                - [Forest](#forest)
                - [Gibber plain](#gibber_plain)
                - [Intermittent stream channel](#intermittent_stream_channel)
                - [Karst](#karst)
                - [Piedmont slope](#piedmont_slope)
                    - [Alluvial fan](#alluvial_fan)
                    - [Alluvial plain](#alluvial_plain)
                    - [Pediment](#pediment)
                - [Playa](#playa)
                - [Prairie](#prairie)
                - [River system](#river_system)
                    - [Abandoned river channel](#abandoned_channel)
                    - [Cutoff meander](#cutoff_meander)
                    - [Floodplain](#floodplain)
                    - [River channel](#river_channel)
                        - [Braided river channel](#braided_channel)
                        - [Meandering river channel](#meandering_channel)
                - [Soil profile](#soil_profile)
                - [Strandplain](#strandplain)
                - [Subaerial canyon](#subaerial_canyon)
                - [Subaerial escarpment](#subaerial_escarpment)
                - [Supratidal setting](#supratidal_setting)
                - [Terrace](#terrace)
                - [Tidal flat](#tidal_flat)
                    - [Tidal marsh](#tidal_marsh)
            - [Anoxic environment](#anoxic_environment)
            - [Arid or semi arid environment](#arid_or_semi_arid_environment)
                - [Gibber plain](#gibber_plain)
                - [Marginal marine sabkha](#marginal_marine_sabkha)
                - [Playa](#playa)
                - [Sand plain](#sand_plain)
            - [Cave](#cave)
            - [Hillslope](#hillslope_setting)
                - [Landslide](#landslide)
            - [Humid temperate climatic setting](#humid_temperate_climatic_setting)
            - [Humid tropical climatic setting](#humid_tropical_climatic_setting)
            - [Island](#island)
            - [Outcrop](#outcrop)
            - [Physiographic feature](#physiographic_feature)
                - [Arch-natural formation ](#arch_natural_formation)
                - [Badlands](#badlands)
                - [Basin-physiography](#basin)
                - [Canyon](#canyon)
                    - [Subaerial canyon](#subaerial_canyon)
                    - [Submarine canyon](#submarine_canyon)
                - [Cape](#cape)
                - [Channel](#channel)
                    - [Delta distributary channel](#distributary_channel)
                    - [Intermittent stream channel](#intermittent_stream_channel)
                    - [River channel](#river_channel)
                        - [Braided river channel](#braided_channel)
                        - [Meandering river channel](#meandering_channel)
                    - [Submarine channel](#submarine_channel)
                    - [Tidal channel](#tidal_channel)
                - [Cirque](#cirque)
                - [Cliff](#cliff)
                - [Crater](#crater)
                - [Dune](#dune)
                - [Escarpment](#escarpment)
                    - [Subaerial escarpment](#subaerial_escarpment)
                    - [Submarine escarpment](#submarine_escarpment)
                - [Hill](#hill)
                    - [Butte](#butte)
                    - [Drumlin](#drumlin)
                - [Hummock](#hummock)
                - [Isthmus](#isthmus)
                - [Mesa](#mesa)
                - [Moraine](#moraine)
                - [Mountain](#mountain)
                - [Mountain range](#mountain_range)
                - [Plain](#plain)
                    - [Basin plain](#abyssal_plain)
                    - [Alluvial plain](#alluvial_plain)
                    - [Coastal plain](#coastal_plain)
                    - [Delta plain](#delta_plain)
                        - [Lower delta plain](#lower_delta_plain)
                        - [Upper delta plain](#upper_delta_plain)
                    - [Gibber plain](#gibber_plain)
                    - [Playa](#playa)
                    - [Sand plain](#sand_plain)
                - [Plateau](#plateau)
                    - [Ocean plateau](#ocean_plateau)
                - [Ridge](#ridge)
                    - [Submarine ridge](#submarine_ridge)
                        - [Active ocean ridge](#active_ocean_ridge)
                            - [Ocean ridge axial valley](#axial_valley)
                            - [Submarine vent](#submarine_vent)
                        - [Inactive spreading center](#inactive_spreading_center)
                        - [Ocean ridge crest](#ocean_ridge_crest)
                        - [Ocean ridge flank](#ocean_ridge_flank)
                - [Valley](#valley)
            - [Polar climatic setting](#polar_climatic_setting)
                - [Glacier environment](#glacierenvironment)
                    - [Cirque](#cirque)
                    - [Englacial setting](#englacial_setting)
                    - [Glacial outwash plain](#glacial_outwash_plain)
                    - [Glacier lateral setting](#glacier_lateral_setting)
                    - [Proglacial setting](#proglacial_setting)
                        - [Glacier terminus](#glacier_terminus)
                    - [Subglacial setting](#subglacial_setting)
                    - [Supraglacial setting](#supraglacial_setting)
            - [Shoreline](#shoreline)
                - [Barrier island coastline](#barrier_island_coastline)
                    - [Barrier beach](#barrier_beach)
                    - [Barrier lagoon](#barrier_lagoon)
                - [Beach](#beach)
                    - [Barrier beach](#barrier_beach)
                - [Cape](#cape)
                - [Carbonate dominated shoreline](#carbonate_dominated_shoreline)
                - [Coastal plain](#coastal_plain)
                - [Deltaic system](#deltaic_system)
                    - [Delta front](#delta_front)
                    - [Delta plain](#delta_plain)
                        - [Lower delta plain](#lower_delta_plain)
                        - [Upper delta plain](#upper_delta_plain)
                    - [Delta distributary channel](#distributary_channel)
                    - [Delta distributary mouth](#distributary_mouth)
                    - [Estuarine delta](#estuarine_delta)
                    - [Interdistributary bay](#interdistributary_bay)
                    - [Lacustrine delta](#lacustrine_delta)
                    - [Prodelta setting](#prodelta)
                - [Estuary](#estuary)
                    - [Estuarine delta](#estuarine_delta)
                    - [Estuarine lagoon](#estuarine_lagoon)
                - [Lagoonal setting](#lagoonal_setting)
                    - [Barrier lagoon](#barrier_lagoon)
                    - [Estuarine lagoon](#estuarine_lagoon)
                - [Low energy shoreline setting](#low_energy_shoreline_setting)
                    - [Algal flat](#algal_flat)
                    - [Marginal marine sabkha](#marginal_marine_sabkha)
                    - [Mud flat](#mud_flat)
                - [Rocky coast](#rocky_coast)
                - [Strandplain](#strandplain)
                - [Supratidal setting](#supratidal_setting)
                - [Tidal setting](#tidal_setting)
                    - [Intertidal setting](#intertidal)
                    - [Lower delta plain](#lower_delta_plain)
                    - [Tidal channel](#tidal_channel)
                    - [Tidal flat](#tidal_flat)
                        - [Tidal marsh](#tidal_marsh)
            - [Subaqueous setting](#subaqueous_setting)
                - [Lake river or stream bottom](#lakeriverstreambottom)
                - [Interdistributary bay](#interdistributary_bay)
                - [Intertidal setting](#intertidal)
                - [Lacustrine setting](#lacustrine_setting)
                    - [Lacustrine delta](#lacustrine_delta)
                    - [Lake](#lake)
                        - [Fresh water lake](#lake_fresh_water)
                        - [Saline lake](#lake_saline)
                - [Marine setting](#marine_setting)
                    - [Marine water body bottom](#marinewaterbodybottom)
                        - [Basin plain](#abyssal_plain)
                        - [Biological reef](#biological_reef)
                            - [Backreef setting](#backreef)
                            - [Forereef setting](#forereef_setting)
                            - [Reef flat](#reef_flat)
                        - [Carbonate mound](#carbonate_mound)
                        - [Marine carbonate platform](#marine_carbonate_platform)
                        - [Ocean highland](#ocean_highland)
                            - [Ocean plateau](#ocean_plateau)
                            - [Seamount](#seamount)
                            - [Submarine ridge](#submarine_ridge)
                                - [Active ocean ridge](#active_ocean_ridge)
                                    - [Ocean ridge axial valley](#axial_valley)
                                    - [Submarine vent](#submarine_vent)
                                - [Inactive spreading center](#inactive_spreading_center)
                                - [Ocean ridge crest](#ocean_ridge_crest)
                                - [Ocean ridge flank](#ocean_ridge_flank)
                        - [Slope rise setting](#slope_rise_setting)
                            - [Seafloor rise, continental](#rise_continental)
                            - [Seafloor rise, insular](#rise_insular)
                            - [Seafloor slope, continental](#slope_continental)
                            - [Seafloor slope, insular](#slope_insular)
                        - [Submarine canyon](#submarine_canyon)
                        - [Submarine channel](#submarine_channel)
                        - [Submarine escarpment](#submarine_escarpment)
                        - [Submarine fan](#submarine_fan)
                    - [Above carbonate compensation depth](#above_carbonate_compensation_depth)
                    - [Abyssal setting](#abyssal_setting)
                    - [Bathyal setting](#bathyal_setting)
                        - [Lower bathyal setting](#lower_bathyal_setting)
                        - [Middle bathyal setting](#middle_bathyal_setting)
                        - [upper bathyal setting](#upper_bathyal_setting)
                    - [Below carbonate compensation depth setting](#below_carbonate_compensation_depth_setting)
                    - [Continental borderland](#continental_borderland)
                    - [Deep sea trench](#deep_sea_trench)
                        - [Continental margin trench](#continental_margin_trench)
                        - [Hadal setting](#hadal_setting)
                        - [Intraoceanic trench](#intraoceanic_trench)
                    - [Epicontinental marine setting](#epicontinental_marine_setting)
                    - [Marginal shelf](#marginal_shelf)
                        - [Continental shelf](#continental_shelf)
                        - [Insular shelf](#insular_shelf)
                    - [Marine carbonate platform](#marine_carbonate_platform)
                    - [Neritic setting](#neritic_setting)
                    - [Ocean highland](#ocean_highland)
                        - [Ocean plateau](#ocean_plateau)
                        - [Seamount](#seamount)
                        - [Submarine ridge](#submarine_ridge)
                            - [Active ocean ridge](#active_ocean_ridge)
                                - [Ocean ridge axial valley](#axial_valley)
                                - [Submarine vent](#submarine_vent)
                            - [Inactive spreading center](#inactive_spreading_center)
                            - [Ocean ridge crest](#ocean_ridge_crest)
                            - [Ocean ridge flank](#ocean_ridge_flank)
                    - [Slope rise setting](#slope_rise_setting)
                        - [Seafloor rise, continental](#rise_continental)
                        - [Seafloor rise, insular](#rise_insular)
                        - [Seafloor slope, continental](#slope_continental)
                        - [Seafloor slope, insular](#slope_insular)
                    - [Submarine bank](#submarine_bank)
                    - [Submarine fan](#submarine_fan)
                - [Prodelta setting](#prodelta)
                - [Subaqueous bar](#subaqueous_bar)
                - [Tidal channel](#tidal_channel)
            - [Terrestrial setting](#terrestrial_setting)
                - [Bog](#bog)
                - [Drainage basin](#drainage_basin)
                - [Gibber plain](#gibber_plain)
                - [Glacial outwash plain](#glacial_outwash_plain)
                - [Lacustrine setting](#lacustrine_setting)
                    - [Lacustrine delta](#lacustrine_delta)
                    - [Lake](#lake)
                        - [Fresh water lake](#lake_fresh_water)
                        - [Saline lake](#lake_saline)
                - [Piedmont slope](#piedmont_slope)
                    - [Alluvial fan](#alluvial_fan)
                    - [Alluvial plain](#alluvial_plain)
                    - [Pediment](#pediment)
                - [Playa](#playa)
                - [River system](#river_system)
                    - [Abandoned river channel](#abandoned_channel)
                    - [Cutoff meander](#cutoff_meander)
                    - [Floodplain](#floodplain)
                    - [River channel](#river_channel)
                        - [Braided river channel](#braided_channel)
                        - [Meandering river channel](#meandering_channel)
            - [Volcano](#volcano)
            - [Wetland](#wetland)
                - [Bog](#bog)
                - [Swamp or marsh](#swamp_or_marsh)
                    - [Tidal marsh](#tidal_marsh)
        - [Glacier environment](#glacierenvironment)
            - [Cirque](#cirque)
            - [Englacial setting](#englacial_setting)
            - [Glacial outwash plain](#glacial_outwash_plain)
            - [Glacier lateral setting](#glacier_lateral_setting)
            - [Proglacial setting](#proglacial_setting)
                - [Glacier terminus](#glacier_terminus)
            - [Subglacial setting](#subglacial_setting)
            - [Supraglacial setting](#supraglacial_setting)
        - [Subsurface fluid reservoir](#subsurfacefluidreservoir)
            - [Aquifer ](#aquifer)
        - [Water body](#waterbody)
            - [Marine water body](#marinewaterbody)
                - [Fjord](#fiord)
            - [Terrestrial water body](#terrestrialwaterbody)
                - [Lake](#lake)
                    - [Fresh water lake](#lake_fresh_water)
                    - [Saline lake](#lake_saline)
                - [River or stream](#river_stream)
            - [Bay](#bay)
            - [Bight](#bight)
            - [Canal](#canal)
        - [Continent](#continent)
        - [Continental Margin](#continental_margin)
            - [Active continental margin](#active_continental_margin)
            - [Passive continental margin](#passive_continental_margin)
        - [Geologic structure](#geologic_structure)
            - [Ductile shear zone ](#ductile_shear_zone)
            - [Geologic fault](#fault)
            - [Fault scarp](#fault_scarp)
            - [Geologic fold](#fold)
            - [Impact structure](#impact_structure)
        - [Igneous system](#igneous_system)
            - [Hypabyssal setting](#hypabyssal_setting)
            - [Intrusive igneous complex](#intrusive_igneous_complex)
            - [Volcanic Setting](#volcanic_setting)
                - [Inactive spreading center](#inactive_spreading_center)
                - [Plate spreading center](#plate_spreading_center)
                - [Seamount](#seamount)
                - [Volcanic arc](#volcanic_arc)
                    - [Continental volcanic arc](#continental_volcanic_arc)
                    - [Island arc](#island_arc)
                - [Volcano](#volcano)
        - [Sedimentary basin](#sedimentary_basin)
            - [Foreland basin](#foreland_basin)
        - [Tectonically defined setting](#tectonic_setting)
            - [Back arc setting](#back_arc_setting)
            - [Collisional setting](#collisional_setting)
            - [Crustal setting](#crust)
                - [Continental crust](#continental_crust)
                    - [Collisional setting](#collisional_setting)
                    - [Foreland setting](#foreland_setting)
                        - [Foreland basin](#foreland_basin)
                        - [Foreland fold and thrust belt](#foreland_fold_thrust_belt)
                    - [Hinterland tectonic setting](#hinterland_setting)
                    - [Lower continental crust](#lower_continental_crust)
                    - [Middle continental crust](#middle_continental_crust)
                    - [Upper continental crust](#upper_continental_crust)
                - [Ocean crust](#ocean_crust)
                    - [Lower oceanic crust](#lower_oceanic_crust)
                    - [Upper ocean crust](#upper_ocean_crust)
                - [Transitional crust](#transitional_crust)
            - [Extended terrane](#extended_terrane)
                - [Continental rift](#continental_rift_setting)
                - [Plate spreading center](#plate_spreading_center)
                - [Rift zone](#rift_zone)
            - [Foreland setting](#foreland_setting)
                - [Foreland basin](#foreland_basin)
                - [Foreland fold and thrust belt](#foreland_fold_thrust_belt)
            - [Hinterland tectonic setting](#hinterland_setting)
            - [Hot spot](#hot_spot)
            - [Intraplate tectonic setting](#intraplate_tectonic_setting)
                - [Inactive spreading center](#inactive_spreading_center)
                - [Seamount](#seamount)
            - [Mantle](#mantle)
                - [Lower mantle](#lower_mantle)
                - [Upper mantle](#upper_mantle)
            - [Plate margin](#plate_margin)
                - [Active continental margin](#active_continental_margin)
                - [Forearc setting](#forearc_setting)
                - [Fracture zone](#fracture_zone)
                - [Subduction zone](#subduction_zone)
                - [Transform plate boundary](#transform_plate_boundary)
                - [Volcanic arc](#volcanic_arc)
                    - [Continental volcanic arc](#continental_volcanic_arc)
                    - [Island arc](#island_arc)
            - [Plate triple junction](#triple_junction)
    - [Extraterrestrial environment](#extraterrestrialenvironment)

**Concepts**

[]{#anysampledfeature}

##  Any sampled feature
- Any thing that can be sampled. Top concept in sampled feature type
vocabulary.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/anysampledfeature
- **Other Properties:**

[]{#anthropogenicenvironment}

###  Anthropogenic environment
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is produced by or related to human activity past or
present.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/anthropogenicenvironment
- **Other Properties:**

[]{#activehumanoccupationsite}

####  Active human occupation site
- **Child of**:
 [`Anthropogenic environment`](#anthropogenicenvironment)
- sampled feature is a site at which there are ongoing human
activities
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/activehumanoccupationsite
- **Other Properties:**

[]{#experimentsetting}

#####  Experiment setting
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
- Sampled feature is an experimental set up that produced the sample;
the sample is the product of the experiment.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/experimentsetting
- **Other Properties:**

[]{#laboratorycuratorialenvironment}

#####  Laboratory or curatorial environment
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
- Sampled feature is a laboratory or other research site, collected
with intention of characterizing the environment in which data are
collected or other research conducted, that might affect results or
safety; e.g. lab blank measurements.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/laboratorycuratorialenvironment
- **Other Properties:**

[]{#agricultural_site}

#####  Agricultural site
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
- Site involved in crop cultivation, livestock production,
aquaculture, or forestry to produce food or non-food products.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Agriculture, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/agricultural_site
- **Other Properties:**

[]{#canal}

#####  Canal
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
 [`Water body`](#waterbody)
- A human manufactured water channel to manage surface water resources
for irrigation, transportation, or human consumption.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/canal
- **Other Properties:**

[]{#mining_site}

#####  Mining site
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mining_site
- **Other Properties:**

[]{#urban_setting}

#####  Urban setting
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
- a densely populated area with many human-made structures; a human
settlement with a high population density and an infrastructure of
built environment
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Urban_area, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/urban_setting
- **Other Properties:**

[]{#pasthumanoccupationsite}

####  Site of past human activities
- **Child of**:
 [`Anthropogenic environment`](#anthropogenicenvironment)
- sampled feature is a place where humans have been and left evidence
of their activity. Includes prehistoric and paleo hominid sites
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/pasthumanoccupationsite
- **Other Properties:**

[]{#harbor}

####  Harbor
- **Child of**:
 [`Anthropogenic environment`](#anthropogenicenvironment)
- A coastal feature useful to humans to bring water craft to shore,
onload and offload cargo, and provide protection from storms.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/harbor
- **Other Properties:**

[]{#quarry}

####  Quarry
- **Child of**:
 [`Anthropogenic environment`](#anthropogenicenvironment)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/quarry
- **Other Properties:**

[]{#biologicalentity}

###  Biological entity
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is an organism. Use for samples that represent some
species of organism as the proximate sampled feature, not the
environment that the organism inhabits.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/biologicalentity
- **Other Properties:**

[]{#earthenvironment}

###  Earth environment
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is the natural Earth environment
- **See Also**:
* [<http://purl.bioontology.org/ontology/MESH/D004777>](http://purl.bioontology.org/ontology/MESH/D004777)
* [<http://semanticscience.org/resource/SIO_000955>](http://semanticscience.org/resource/SIO_000955)
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/earthenvironment
- **Other Properties:**

[]{#atmosphere}

####  Atmosphere
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is the Earth's atmosphere
- **See Also**:
* [<http://purl.obolibrary.org/obo/ENVO_01000267>](http://purl.obolibrary.org/obo/ENVO_01000267)
* [<http://purl.obolibrary.org/obo/RBO_00000018>](http://purl.obolibrary.org/obo/RBO_00000018)
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/atmosphere
- **Other Properties:**

[]{#earthinterior}

####  Earth interior
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Geologic environments within the solid Earth.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/earthinterior
- **Other Properties:**

[]{#contact_metamorphic_zone}

#####  Contact metamorphic zone
- **Child of**:
 [`Earth interior`](#earthinterior)
- Zone of metamorphism associated with the contact of an igneous body.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0, 2004, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/contact_metamorphic_zone
- **Other Properties:**

[]{#crust}

#####  Crustal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Tectonically defined setting`](#tectonic_setting)
- The outermost layer or shell of the Earth, defined according to
various criteria, including seismic velocity, density and composition,
that part of the Earth above the Mohorovicic discontinuity, made up of
the sial and the sima.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/crust
- **Other Properties:**

[]{#continental_crust}

######  Continental crust
- **Child of**:
 [`Crustal setting`](#crust)
- That type of the Earth's crust which underlies the continents and
the continental shelves, it is equivalent to the sial and continental
sima and ranges in thickness from about 25 km to more than 70 km under
mountain ranges, averaging ~40 km. The density of the continental
crust averages ~2.8 g/cm3 and is ~2.7 g.cm3 in the upper layer. The
velocities of compressional seismic waves through it average ~6.5 km/s
and are less than ~7.0 km/sec.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_crust
- **Other Properties:**

[]{#collisional_setting}

#######  Collisional setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting in which two continental crustal plates impact and
are sutured together after intervening oceanic crust is entirely
consumed at a subduction zone separating the plates. Such collision
typically involves major mountain forming events, exemplified by the
modern Alpine and Himalayan mountain chains.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/collisional_setting
- **Other Properties:**

[]{#foreland_setting}

#######  Foreland setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- The exterior area of an orogenic belt where deformation occurs
without significant metamorphism. Generally the foreland is closer to
the continental interior than other portions of the orogenic belt are.
- **Source:**
1-GE WP3, Neuendorf et al.(2005), p. 250, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_setting
- **Other Properties:**

[]{#foreland_basin}

########  Foreland basin
- **Child of**:
 [`Foreland setting`](#foreland_setting)
 [`Sedimentary basin`](#sedimentary_basin)
- an elongate region of potential sediment accommodation that forms on
continental crust between a contractional orogenic belt and the
adjacent craton, mainly in response to geodynamic processes related to
subduction and the resulting peripheral or retroarc fold-thrust belt.
- **Source:**
SESAR legacy localities, 
https://doi.org/10.1046/j.1365-2117.1996.01491.x, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_basin
- **Other Properties:**

[]{#foreland_fold_thrust_belt}

########  Foreland fold and thrust belt
- **Child of**:
 [`Foreland setting`](#foreland_setting)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_fold_thrust_belt
- **Other Properties:**

[]{#hinterland_setting}

#######  Hinterland tectonic setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting in the internal part of an orogenic belt,
characterized by plastic deformation of rocks accompanied by
significant metamorphism, typically involving crystalline basement
rocks. Typically denotes the most structurally thickened part of an
orogenic belt, between a magmatic arc or collision zone and a more
'external' foreland setting.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hinterland_setting
- **Other Properties:**

[]{#lower_continental_crust}

#######  Lower continental crust
- **Child of**:
 [`Continental crust`](#continental_crust)
- Continental crustal setting characterized by upper amphibolite to
granulite facies metamorphism, insitu melting, residual anhydrous
metamorphic rocks, and ductile flow of rock bodies.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_continental_crust
- **Other Properties:**

[]{#middle_continental_crust}

#######  Middle continental crust
- **Child of**:
 [`Continental crust`](#continental_crust)
- Continental crustal setting characterized by greenschist to upper
amphibolite facies metamorphism, plutonic igneous rocks, and ductile
deformation.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/middle_continental_crust
- **Other Properties:**

[]{#upper_continental_crust}

#######  Upper continental crust
- **Child of**:
 [`Continental crust`](#continental_crust)
- Continental crustal setting dominated by non metamorphosed to low
greenschist facies metamorphic rocks, and brittle deformation.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_continental_crust
- **Other Properties:**

[]{#ocean_crust}

######  Ocean crust
- **Child of**:
 [`Crustal setting`](#crust)
- That type of the Earth's crust which underlies the ocean basins. The
oceanic crust is 5-10 km thick, it has a density of 2.9 g/cm3, and
compressional seismic-wave velocities travelling through it at 4-7.2
km/sec. Setting in crust produced by submarine volcanism at a mid
ocean ridge.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_crust
- **Other Properties:**

[]{#lower_oceanic_crust}

#######  Lower oceanic crust
- **Child of**:
 [`Ocean crust`](#ocean_crust)
- Setting characterized by dominantly intrusive mafic rocks, with
sheeted dike complexes in upper part and gabbroic to ultramafic
intrusive or metamorphic rocks in lower part.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_oceanic_crust
- **Other Properties:**

[]{#upper_ocean_crust}

#######  Upper ocean crust
- **Child of**:
 [`Ocean crust`](#ocean_crust)
- Oceanic crustal setting dominated by extrusive rocks, abyssal
oceanic sediment, with increasing mafic intrusive rock in lower part.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_ocean_crust
- **Other Properties:**

[]{#transitional_crust}

######  Transitional crust
- **Child of**:
 [`Crustal setting`](#crust)
- Crust formed in the transition zone between continental and oceanic
crust, during the history of continental rifting that culminates in
the formation of a new ocean.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/transitional_crust
- **Other Properties:**

[]{#geologic_unit}

#####  Geologic unit
- **Child of**:
 [`Earth interior`](#earthinterior)
- Sampled feature is a rock body that has some identifying and unity
criteria that constitutes a part of the Earth's crust or mantle.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/geologic_unit
- **Other Properties:**

[]{#melange}

######  Melange
- **Child of**:
 [`Geologic unit`](#geologic_unit)
- A body of rock characterized by a lack of continuous bedding and the
inclusion of fragments of rock of all sizes, contained in a fine-
grained deformed matrix. The melange typically consists of a jumble of
large blocks of varied lithology.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/M%C3%A9lange, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/melange
- **Other Properties:**

[]{#ophiolite}

######  Ophiolite
- **Child of**:
 [`Geologic unit`](#geologic_unit)
- A rock body interpreted to represent exhumed ocean crust.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ophiolite
- **Other Properties:**

[]{#soil_profile}

######  Soil profile
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Geologic unit`](#geologic_unit)
- Sampled feature is a section through the soil accumulation at the
Earth's surface.
- **Source:**
sessf:sfvocabulary
- **Concept URI:** https://w3id.org/sesar/sampledfeature/soil_profile
- **Other Properties:**

[]{#stratigraphic_section}

######  Stratigraphic section
- **Child of**:
 [`Geologic unit`](#geologic_unit)
- Sampled feature is a sequence of sedimentary (and possibly volcanic)
layers deposited in a sequence in a particular region.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/sampledfeature/stratigraphic_section
- **Other Properties:**

[]{#thrust_sheet}

######  Thrust sheet
- **Child of**:
 [`Geologic unit`](#geologic_unit)
- A body of rock bounded at its base by a thrust fault, and bounded
above by the Earth surface or a different thrust fault.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/thrust_sheet
- **Other Properties:**

[]{#xenolith}

######  Xenolith
- **Child of**:
 [`Geologic unit`](#geologic_unit)
- small rock body contained within an igneous host rock body.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/xenolith
- **Other Properties:**

[]{#high_pressure_low_temperature_earth_interior_setting}

#####  High pressure low temperature earth interior setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- High pressure environment characterized by geothermal gradient
significantly lower than standard continental geotherm, enviornment in
which blueschist facies metamorphic rocks form. Typically associated
with subduction zones.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/high_pressure_low_temperature_earth_interior_setting
- **Other Properties:**

[]{#hypabyssal_setting}

#####  Hypabyssal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Igneous system`](#igneous_system)
- Igneous environment close to the Earth's surface, characterized by
more rapid cooling than plutonic setting to produce generally fine-
grained intrusive igneous rock that is commonly associated with co-
magmatic volcanic rocks.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hypabyssal_setting
- **Other Properties:**

[]{#intrusive_igneous_complex}

#####  Intrusive igneous complex
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Igneous system`](#igneous_system)
- Features related to igneous activity wholly within the Earth,
characterized by slow cooling to produce generally medium to coarse-
grained intrusive igneous rocks.
- **Source:**
SESAR legacy data
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intrusive_igneous_complex
- **Other Properties:**

[]{#low_pressure_high_temperature_setting}

#####  Low pressure high temperature setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Setting characterized by temperatures significantly higher that
those associated with normal continental geothermal gradient.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/low_pressure_high_temperature_setting
- **Other Properties:**

[]{#mantle}

#####  Mantle
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Tectonically defined setting`](#tectonic_setting)
- The zone of the Earth below the crust and above the core, which is
divided into the upper mantle and the lower mantle, with a transition
zone separating them.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mantle
- **Other Properties:**

[]{#lower_mantle}

######  Lower mantle
- **Child of**:
 [`Mantle`](#mantle)
- That part of the mantle that lies below a depth of about 660 km.
With increasing depth, density increases from ~4.4 g/cm3-to ~5.6
g/cm3, and velocity of compressional seismic waves increases from
~10.7 km/s to ~13.7 km/s (Dziewonski and Anderson, 1981).
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_mantle
- **Other Properties:**

[]{#upper_mantle}

######  Upper mantle
- **Child of**:
 [`Mantle`](#mantle)
- That part of the mantle which lies above a depth of about 660 km and
has a density of 3.4 g/cm3 to 4.0 g/cm3 with increasing depth.
Similarly, P-wave velocity increases from about 8 to 11 km/sec with
depth and S wave velocity increases from about 4.5 to 6 km/sec with
depth. It is presumed to be peridotitic in composition. It includes
the subcrustal lithosphere the asthenosphere and the transition zone,
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_mantle
- **Other Properties:**

[]{#mineralized_body}

#####  Mineralized system
- **Child of**:
 [`Earth interior`](#earthinterior)
- Sampled feature is a part of the Earth that has been enriched in
elements of economic interest
- **Source:**
sessf:sfvocabulary
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mineralized_body
- **Other Properties:**

[]{#regional_metamorphic_setting}

#####  Regional metamorphic setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Metamorphism not obviously localized along contacts of igneous
bodies, includes burial metamorphism and ocean ridge metamorphism
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0, 2004, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/regional_metamorphic_setting
- **Other Properties:**

[]{#ultra_high_pressure_crustal_setting}

#####  Ultra high pressure crustal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
- Setting characterized by pressures characteristic of upper mantle,
but indicated by mineral assemblage in crustal composition rocks.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ultra_high_pressure_crustal_setting
- **Other Properties:**

[]{#earthsurface}

####  Earth surface
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is the interface between solid earth and hydrosphere
or atmosphere. Includes samples representing things collected on the
surface, in the uppermost part of the material below the surface, or
air or water directly at the contact with the Earth surface.
Hierarchy presented here is based on assumption that a particular
setting may be specified by a combination of a climatic setting with
one or more process or geomorphic- or physiographic- defined settings.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/earthsurface
- **Other Properties:**

[]{#subaerialsurfaceenvironment}

#####  Subaerial surface environment
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting at the interface between the solid earth and the atmosphere,
includes some shallow subaqueous settings in river channels and
playas. Characterized by conditions and processes, such as erosion,
that exist or operate in the open air on or immediately adjacent to
the land surface
- **Alternate labels:**
subaerial setting
- **Source:**
Neuendorf et al., 2005
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/subaerialsurfaceenvironment
- **Other Properties:**

[]{#coastal_plain}

######  Coastal plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Plain`](#plain)
 [`Shoreline`](#shoreline)
- A low relief plain bordering a water body extending inland to the
nearest elevated land, sloping very gently towards the water body.
Distinguished from alluvial plain by presence of relict shoreline-
related deposits or morphology.
- **Source:**
based on Neuendorf et al, 2005, p. 125, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/coastal_plain
- **Other Properties:**

[]{#continental_divide}

######  Continental divide
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- a topographic boundary that separates areas on a continent such that
the drainage basin on one side of the boundary feeds into one ocean or
sea, and the basin on the other side either feeds into a different
ocean or sea, or else is not connected to the open sea.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Continental_divide, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_divide
- **Other Properties:**

[]{#eolian_process_setting}

######  Eolian process setting
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- Sedimentary setting in which wind is the dominant process producing,
transporting, and depositing sediment. Typically has low-relief plain
or piedmont slope physiography.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/eolian_process_setting
- **Other Properties:**

[]{#dune}

#######  Dune
- **Child of**:
 [`Eolian process setting`](#eolian_process_setting)
 [`Physiographic feature`](#physiographic_feature)
- a mound or hill of loose, windblown granular material (typically
sand), capable of wind-driven movement, while  retaining its
characteristic shape
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/dune
- **Other Properties:**

[]{#dunefield}

#######  Dunefield
- **Child of**:
 [`Eolian process setting`](#eolian_process_setting)
- Extensive deposits on sand in an area where the supply is abundant.
As a characteristic, individual dunes somewhat resemble barchans but
are highly irregular in shape and crowded, erg areas of the Sahara are
an example.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/dunefield
- **Other Properties:**

[]{#coastal_dune_field}

########  Coastal dune field
- **Child of**:
 [`Dunefield`](#dunefield)
- A dune field on low-lying land recently abandoned or built up by the
sea, the dunes may ascend a cliff and travel inland.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/coastal_dune_field
- **Other Properties:**

[]{#sand_plain}

#######  Sand plain
- **Child of**:
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Eolian process setting`](#eolian_process_setting)
 [`Plain`](#plain)
- A sand-covered plain dominated by aeolian processes.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/sand_plain
- **Other Properties:**

[]{#forest}

######  Forest
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- An area with a high density of trees.
- **Source:**
<http://purl.obolibrary.org/obo/ENVO_00000111>, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/forest
- **Other Properties:**

[]{#gibber_plain}

######  Gibber plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/gibber_plain
- **Other Properties:**

[]{#intermittent_stream_channel}

######  Intermittent stream channel
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Channel`](#channel)
- a watercourse that temporarily or seasonally fills and flows after
sufficient rain.
- **Alternate labels:**
Arroyo, 
Dry gulch, 
Dry valley, 
Wadi, 
Wash, 
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Arroyo_(watercourse), 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intermittent_stream_channel
- **Other Properties:**

[]{#karst}

######  Karst
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- A landform that formed by dissolution of soluble rock like limestone
or gypsum, characterized by sinkholes, caves, and underground drainage
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/karst
- **Other Properties:**

[]{#piedmont_slope}

######  Piedmont slope
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Location on gentle slope at the foot of a mountain, generally used
in terms of intermontane-basin terrain. Main components include: (a)
An erosional surface on bedrock adjacent to the receding mountain
front (pediment, rock pediment), (b) A constructional surface
comprising individual alluvial fans and interfan valleys, also near
the mountain front, and (c) A distal complex of coalescent fans
(bajada), and alluvial slopes without fan form. Piedmont slopes grade
to basin-floor depressions with alluvial and temporary lake plains or
to surfaces associated with through drainage.
- **Source:**
Hawley and Parsons, 1980+F98, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/piedmont_slope
- **Other Properties:**

[]{#alluvial_fan}

#######  Alluvial fan
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
- A low, outspread, relatively flat to gently sloping mass of loose
rock material, shaped like an open fan or a segment of a cone,
deposited by a stream (esp. in a semiarid region) at the place where
it issues from a narrow mountain valley upon a plain or broad valley,
or where a tributary stream is near or at its junction with the main
stream, or wherever a constriction in a valley abruptly ceases or the
gradient of the stream suddenly decreases, it is steepest near the
mouth of the valley where its apex points upstream, and it slopes
gently and convexly outward with gradually decreasing gradient
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/alluvial_fan
- **Other Properties:**

[]{#alluvial_plain}

#######  Alluvial plain
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
 [`Plain`](#plain)
- An assemblage landforms produced by alluvial and fluvial processes
(braided streams, terraces, etc.) that form low gradient, regional
ramps along the flanks of mountains and extend great distances from
their sources (e.g.high Plains of North America). (NRCS GLOSSARY OF
LANDFORM AND GEOLOGIC TERMS). A level or gently sloping tract or a
slightly undulating land surface produced by extensive deposition of
alluvium... Synonym-- wash plain,...river plain, aggraded valley
plain,... (Jackson, 1997, p. 17). May include one or more River plain
systems.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/alluvial_plain
- **Other Properties:**

[]{#pediment}

#######  Pediment
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
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
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, NRCS, 2001, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/pediment
- **Other Properties:**

[]{#playa}

######  Playa
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Source:**
Based on Hawley and Parsons, 1980, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/playa
- **Other Properties:**

[]{#prairie}

######  Prairie
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- a region of relatively level to rolling grassland, generally
treeless
- **Alternate labels:**
pampas, 
savanna, 
steppe, 
temperate grassland, 
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/prairie
- **Other Properties:**

[]{#river_system}

######  River system
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Geologic setting dominated by a river system in any climatic
setting. Includes active channels, abandoned channels, levees, oxbow
lakes, flood plain. May be part of an alluvial plain that includes
terraces composed of abandoned river plain deposits.
- **Alternate labels:**
Fluvial setting
- **Source:**
<http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment>
- **Concept URI:** https://w3id.org/sesar/sampledfeature/river_system
- **Other Properties:**

[]{#abandoned_channel}

#######  Abandoned river channel
- **Child of**:
 [`River system`](#river_system)
- A drainage channel along which runoff no longer occurs, as on an
alluvial fan
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/abandoned_channel
- **Other Properties:**

[]{#cutoff_meander}

#######  Cutoff meander
- **Child of**:
 [`River system`](#river_system)
- The abandoned, bow- or horseshoe-shaped channel of a former meander,
left when the stream formed a cutoff across a narrow meander neck.
Note that these are typically lakes, thus also lacustrine.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cutoff_meander
- **Other Properties:**

[]{#floodplain}

#######  Floodplain
- **Child of**:
 [`River system`](#river_system)
- The surface or strip of relatively smooth land adjacent to a river
channel, constructed by the present river in its existing regimen and
covered with water when the river overflows its banks. It is built of
alluvium carried by the river during floods and deposited in the
sluggish water beyond the influence of the swiftest current. A river
has one floodplain and may have one or more terraces representing
abandoned floodplains
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/floodplain
- **Other Properties:**

[]{#river_channel}

#######  River channel
- **Child of**:
 [`Channel`](#channel)
 [`River system`](#river_system)
- The bed where a natural body of surface water flows or may flow, a
natural passageway or depression of perceptible extent containing
continuously or periodically flowing water, or forming a connecting
link between two bodies of water, a watercourse
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/river_channel
- **Other Properties:**

[]{#braided_channel}

########  Braided river channel
- **Child of**:
 [`River channel`](#river_channel)
- A stream that divides into or follows an interlacing or tangled
network of several small branching and reuniting shallow channels
separated from each other by ephemeral branch islands or channel bars,
resembling in plan the strands of a complex braid. Such a stream is
generally believed to indicate an inability to carry all of its load,
such as an overloaded and aggrading stream flowing in a wide channel
on a floodplain
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/braided_channel
- **Other Properties:**

[]{#meandering_channel}

########  Meandering river channel
- **Child of**:
 [`River channel`](#river_channel)
- Produced by a mature stream swinging from side to side as it flows
across its floodplain or shifts its course laterally toward the convex
side of an original curve
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/meandering_channel
- **Other Properties:**

[]{#soil_profile}

######  Soil profile
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Geologic unit`](#geologic_unit)
- Sampled feature is a section through the soil accumulation at the
Earth's surface.
- **Source:**
sessf:sfvocabulary
- **Concept URI:** https://w3id.org/sesar/sampledfeature/soil_profile
- **Other Properties:**

[]{#strandplain}

######  Strandplain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Shoreline`](#shoreline)
- A prograded shore built seaward by waves and currents, and
continuous for some distance along the coast. It is characterized by
subparallel beach ridges and swales, in places with associated dunes.
- **Source:**
based on Jackson 1997, p. 626, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/strandplain
- **Other Properties:**

[]{#subaerial_canyon}

######  Subaerial canyon
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Canyon`](#canyon)
- A canyon that is open to the Earth's atmosphere
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subaerial_canyon
- **Other Properties:**

[]{#subaerial_escarpment}

######  Subaerial escarpment
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Escarpment`](#escarpment)
- An escarpment that is on the land surface, open to the atmosphere.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subaerial_escarpment
- **Other Properties:**

[]{#supratidal_setting}

######  Supratidal setting
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Shoreline`](#shoreline)
- Pertaining to the shore area marginal to the littoral zone, just
above high-tide level
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/supratidal_setting
- **Other Properties:**

[]{#terrace}

######  Terrace
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
- a long, narrow, relatively flat surface, bounded on one side by a
descending slope and on the other by an ascending slope, defining a
bench like feature in the Earth surface.
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/terrace
- **Other Properties:**

[]{#tidal_flat}

######  Tidal flat
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Tidal setting`](#tidal_setting)
- An extensive, nearly horizontal, barren tract of land that is
alternately covered and uncovered by the tide, and consisting of
unconsolidated sediment (mostly mud and sand). It may form the top
surface of a deltaic deposit.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_flat
- **Other Properties:**

[]{#tidal_marsh}

#######  Tidal marsh
- **Child of**:
 [`Swamp or marsh`](#swamp_or_marsh)
 [`Tidal flat`](#tidal_flat)
- A marsh bordering a coast (as in a shallow lagoon or sheltered bay),
formed of mud and of the resistant mat of roots of salt-tolerant
plants, and regularly inundated during high tides, a marshy tidal
flat.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_marsh
- **Other Properties:**

[]{#anoxic_environment}

#####  Anoxic environment
- **Child of**:
 [`Earth surface`](#earthsurface)
- Environment depleted in oxygen, typically subaqueous.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/anoxic_environment
- **Other Properties:**

[]{#arid_or_semi_arid_environment}

#####  Arid or semi arid environment
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting characterized by mean annual precipitation of 10 inches (25
cm) or less. (Jackson, 1997, p. 172). Equivalent to SLTT 'Desert
setting', but use 'Arid' to emphasize climatic nature of setting
definition.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/arid_or_semi_arid_environment
- **Other Properties:**

[]{#gibber_plain}

######  Gibber plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/gibber_plain
- **Other Properties:**

[]{#marginal_marine_sabkha}

######  Marginal marine sabkha
- **Child of**:
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Low energy shoreline setting`](#low_energy_shoreline_setting)
- Setting characterized by arid to semi-arid conditions on restricted
coastal plains mostly above normal high tide level, with evaporite-
saline mineral, tidal-flood, and eolian deposits. Boundaries with
intertidal setting and non-tidal terrestrial setting are gradational.
(Jackson, 1997, p. 561).
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, based on Jackson 1997, Neuendorf et al. 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/marginal_marine_sabkha
- **Other Properties:**

[]{#playa}

######  Playa
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Source:**
Based on Hawley and Parsons, 1980, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/playa
- **Other Properties:**

[]{#sand_plain}

######  Sand plain
- **Child of**:
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Eolian process setting`](#eolian_process_setting)
 [`Plain`](#plain)
- A sand-covered plain dominated by aeolian processes.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/sand_plain
- **Other Properties:**

[]{#cave}

#####  Cave
- **Child of**:
 [`Earth surface`](#earthsurface)
- A natural underground open space, it generally has a connection to
the surface, is large enough for a person to enter, and extends into
darkness. The most common type of cave is formed in limestone by
dissolution.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cave
- **Other Properties:**

[]{#hillslope_setting}

#####  Hillslope
- **Child of**:
 [`Earth surface`](#earthsurface)
- Earth surface setting characterized by surface slope angles high
enough that gravity alone becomes a significant factor in geomorphic
development, as well as base-of-slope areas influenced by hillslope
processes. Hillslope activities include creep, sliding, slumping,
falling, and other downslope movements caused by slope collapse
induced by gravitational influence on earth materials. May be
subaerial or subaqueous.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, Hawley, J.W., and Parsons, R.B. 1980. Glossary of selected geomorphic and geologic terms. Mimeo. USDA Soil Conservation Service, West National Technical Center, Portland, OR. 30 p., 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hillslope_setting
- **Other Properties:**

[]{#landslide}

######  Landslide
- **Child of**:
 [`Hillslope`](#hillslope_setting)
- a mass of rock, debris, or earth that has moved down a slope under
the influence of gravity
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/landslide
- **Other Properties:**

[]{#humid_temperate_climatic_setting}

#####  Humid temperate climatic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting with seasonal climate having hot to cold or humid to arid
seasons.
- **Source:**
Cleland, D.T., Avers, P.E., McNab, W.H., Jensen, M.E., Bailey, R.G., King, T., Russell, W.E. 1997. National Hierarchical Framework of Ecological Units, in Boyce, M. S., Haney, A., ed., Ecosystem Management Applications for Sustainable Forest and WildlifeResources: Yale University Press, New Haven, CT. pp. 181-200., 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/humid_temperate_climatic_setting
- **Other Properties:**

[]{#humid_tropical_climatic_setting}

#####  Humid tropical climatic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting with hot humid climate influenced by equatorial air masses,
no winter season.
- **Source:**
Cleland, D.T., Avers, P.E., McNab, W.H., Jensen, M.E., Bailey, R.G., King, T., Russell, W.E. 1997. National Hierarchical Framework of Ecological Units, in Boyce, M. S., Haney, A., ed., Ecosystem Management Applications for Sustainable Forest and WildlifeResources: Yale University Press, New Haven, CT. pp. 181-200., 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/humid_tropical_climatic_setting
- **Other Properties:**

[]{#island}

#####  Island
- **Child of**:
 [`Earth surface`](#earthsurface)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/island
- **Other Properties:**

[]{#outcrop}

#####  Outcrop
- **Child of**:
 [`Earth surface`](#earthsurface)
- Sampled feature is an exposure of rock or sediment at the Earth's
surface
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/outcrop
- **Other Properties:**

[]{#physiographic_feature}

#####  Physiographic feature
- **Child of**:
 [`Earth surface`](#earthsurface)
- A feature that is defined by the morphology of the Earth surface
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/physiographic_feature
- **Other Properties:**

[]{#arch_natural_formation}

######  Arch-natural formation
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A landform consting of rock in a curved symmetrical structure that
spans an opening and support the weight of the rock above the opening.
- **Source:**
Oxford English Dictionary, 
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Natural_arch, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/arch_natural_formation
- **Other Properties:**

[]{#badlands}

######  Badlands
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A dry terrain where soft sedimentary rock and clay-rich soils have
been extensively eroded, characterized by steep slopes, minimal
vegetation, lack of a substantial regolith, and high drainage density.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Badlands, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/badlands
- **Other Properties:**

[]{#basin}

######  Basin-physiography
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- landform sunken or depressed below the surrounding area
- **Alternate labels:**
Depression-physiography
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Depression_(geology), 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/basin
- **Other Properties:**

[]{#canyon}

######  Canyon
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- a deep, relatively narrow, steep-sided valley confined between walls
cutting through a plateau or mountainous area
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/canyon
- **Other Properties:**

[]{#subaerial_canyon}

#######  Subaerial canyon
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Canyon`](#canyon)
- A canyon that is open to the Earth's atmosphere
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subaerial_canyon
- **Other Properties:**

[]{#submarine_canyon}

#######  Submarine canyon
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Canyon`](#canyon)
- A canyon that is cut in the ocean floor.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_canyon
- **Other Properties:**

[]{#cape}

######  Cape
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
 [`Shoreline`](#shoreline)
- A mass of land that extends from a coastline into an adjacent body
of water
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cape
- **Other Properties:**

[]{#channel}

######  Channel
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A natural passageway or depression of perceptible extent that
contains a continuously or periodically flowing fluid
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/channel
- **Other Properties:**

[]{#distributary_channel}

#######  Delta distributary channel
- **Child of**:
 [`Channel`](#channel)
 [`Deltaic system`](#deltaic_system)
- A divergent stream flowing away from the main stream and not
returning to it, as in a delta or on an alluvial plain
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/distributary_channel
- **Other Properties:**

[]{#intermittent_stream_channel}

#######  Intermittent stream channel
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Channel`](#channel)
- a watercourse that temporarily or seasonally fills and flows after
sufficient rain.
- **Alternate labels:**
Arroyo, 
Dry gulch, 
Dry valley, 
Wadi, 
Wash, 
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Arroyo_(watercourse), 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intermittent_stream_channel
- **Other Properties:**

[]{#river_channel}

#######  River channel
- **Child of**:
 [`Channel`](#channel)
 [`River system`](#river_system)
- The bed where a natural body of surface water flows or may flow, a
natural passageway or depression of perceptible extent containing
continuously or periodically flowing water, or forming a connecting
link between two bodies of water, a watercourse
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/river_channel
- **Other Properties:**

[]{#braided_channel}

########  Braided river channel
- **Child of**:
 [`River channel`](#river_channel)
- A stream that divides into or follows an interlacing or tangled
network of several small branching and reuniting shallow channels
separated from each other by ephemeral branch islands or channel bars,
resembling in plan the strands of a complex braid. Such a stream is
generally believed to indicate an inability to carry all of its load,
such as an overloaded and aggrading stream flowing in a wide channel
on a floodplain
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/braided_channel
- **Other Properties:**

[]{#meandering_channel}

########  Meandering river channel
- **Child of**:
 [`River channel`](#river_channel)
- Produced by a mature stream swinging from side to side as it flows
across its floodplain or shifts its course laterally toward the convex
side of an original curve
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/meandering_channel
- **Other Properties:**

[]{#submarine_channel}

#######  Submarine channel
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Channel`](#channel)
-
- **Source:**
SESAR legacy localities, 
split IMLGS submarine canyon or channel into separate concepts, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_channel
- **Other Properties:**

[]{#tidal_channel}

#######  Tidal channel
- **Child of**:
 [`Channel`](#channel)
 [`Subaqueous setting`](#subaqueous_setting)
 [`Tidal setting`](#tidal_setting)
- A major channel followed by the tidal currents, extending from
offshore into a tidal marsh or a tidal flat.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_channel
- **Other Properties:**

[]{#cirque}

######  Cirque
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
 [`Physiographic feature`](#physiographic_feature)
- a steep-walled, half-bowl-like recess in a mountain, formed by the
erosive activty of a mountain glacier
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cirque
- **Other Properties:**

[]{#cliff}

######  Cliff
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A high, very steep to vertical rock face.
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cliff
- **Other Properties:**

[]{#crater}

######  Crater
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A broadly circular depression in the Earth surface, commonly with a
raised rim
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/crater
- **Other Properties:**

[]{#dune}

######  Dune
- **Child of**:
 [`Eolian process setting`](#eolian_process_setting)
 [`Physiographic feature`](#physiographic_feature)
- a mound or hill of loose, windblown granular material (typically
sand), capable of wind-driven movement, while  retaining its
characteristic shape
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/dune
- **Other Properties:**

[]{#escarpment}

######  Escarpment
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- a steep slope or long cliff that separates two relatively level
areas having different elevations.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Escarpment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/escarpment
- **Other Properties:**

[]{#subaerial_escarpment}

#######  Subaerial escarpment
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Escarpment`](#escarpment)
- An escarpment that is on the land surface, open to the atmosphere.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subaerial_escarpment
- **Other Properties:**

[]{#submarine_escarpment}

#######  Submarine escarpment
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Escarpment`](#escarpment)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_escarpment
- **Other Properties:**

[]{#hill}

######  Hill
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- an elevation of the Earth surface, of limited extent, having a well
defined outline, rounded morphology, and generally considered to be
less that 300 m (1000 ft) from base to summit
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hill
- **Other Properties:**

[]{#butte}

#######  Butte
- **Child of**:
 [`Hill`](#hill)
- an isolated hill with steep, often vertical sides and relatively
flat top; buttes are smaller landforms than mesas, plateaus or
tablelands
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Butte, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/butte
- **Other Properties:**

[]{#drumlin}

#######  Drumlin
- **Child of**:
 [`Hill`](#hill)
- a low, smoothly rounded, strongly elongated oval hill formed by the
flow of a glacier over non-consolidated sediment, typically older
glacial deposits
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/drumlin
- **Other Properties:**

[]{#hummock}

######  Hummock
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- a rounded or conical very low hill rising slightly from the adjacent
surface
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hummock
- **Other Properties:**

[]{#isthmus}

######  Isthmus
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- narrow strip of land connecting two large land areas otherwise
separated by bodies of water.
- **Source:**
SESAR legacy localities, 
https://www.britannica.com/science/isthmus, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/isthmus
- **Other Properties:**

[]{#mesa}

######  Mesa
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- an isolated, flat-topped elevation,  bounded on all sides by steep
escarpments,  standing distinctly above a surrounding plain.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Mesa, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mesa
- **Other Properties:**

[]{#moraine}

######  Moraine
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A mound, hill, ridge or other elevated feature that is an
accumulation of debris transported by a glacier
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/moraine
- **Other Properties:**

[]{#mountain}

######  Mountain
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- a portion of the Earth's surface that is sufficiently elevated above
the surrounding  surface to be a distinct feature. Generally has steep
sides. Differentiate from a plateau in having a limited summit area;
higher than a hill, typically rising at least 300 metres (980 ft)
above the surrounding surface.
- **Source:**
SESAR legacy localities, 
based on Neuendorf et al., 2005, and https://en.wikipedia.org/wiki/Mountain, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mountain
- **Other Properties:**

[]{#mountain_range}

######  Mountain range
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A region characterized by a succession of mountains or narrowly
spaced mountain ridges, closely related in position, formation, and
age
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mountain_range
- **Other Properties:**

[]{#plain}

######  Plain
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- a relatively flat area of the Earth surface characterized by very
low relief  with no prominent irregularities.
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/plain
- **Other Properties:**

[]{#abyssal_plain}

#######  Basin plain
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Plain`](#plain)
- Near flat areas of ocean floor, slope less than 1:1000, generally
receive only distal turbidite and pelagic sediments.
- **Alternate labels:**
Abyssal plain
- **Source:**
Bates & Jackson, 1987, Heezen & Laughton, 1963, Reading, 1978, p. 390, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/abyssal_plain
- **Other Properties:**

[]{#alluvial_plain}

#######  Alluvial plain
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
 [`Plain`](#plain)
- An assemblage landforms produced by alluvial and fluvial processes
(braided streams, terraces, etc.) that form low gradient, regional
ramps along the flanks of mountains and extend great distances from
their sources (e.g.high Plains of North America). (NRCS GLOSSARY OF
LANDFORM AND GEOLOGIC TERMS). A level or gently sloping tract or a
slightly undulating land surface produced by extensive deposition of
alluvium... Synonym-- wash plain,...river plain, aggraded valley
plain,... (Jackson, 1997, p. 17). May include one or more River plain
systems.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/alluvial_plain
- **Other Properties:**

[]{#coastal_plain}

#######  Coastal plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Plain`](#plain)
 [`Shoreline`](#shoreline)
- A low relief plain bordering a water body extending inland to the
nearest elevated land, sloping very gently towards the water body.
Distinguished from alluvial plain by presence of relict shoreline-
related deposits or morphology.
- **Source:**
based on Neuendorf et al, 2005, p. 125, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/coastal_plain
- **Other Properties:**

[]{#delta_plain}

#######  Delta plain
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Plain`](#plain)
- The level or nearly level surface composing the landward part of a
large or compound delta, strictly, an alluvial plain characterized by
repeated channel bifurcation and divergence, multiple distributary
channels, and interdistributary flood basins
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/delta_plain
- **Other Properties:**

[]{#lower_delta_plain}

########  Lower delta plain
- **Child of**:
 [`Delta plain`](#delta_plain)
 [`Tidal setting`](#tidal_setting)
- The part of a delta plain which is penetrated by saline water and is
subject to tidal processes
- **Source:**
Readingh.G. & Collinson, J.D., 1996. Clastic coasts. 154-231 in Readingh.G. (ed.), Sedimentary Environments: Processses, Facies and Stratigraphy, third edition. Blackwell Science, Oxford, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_delta_plain
- **Other Properties:**

[]{#upper_delta_plain}

########  Upper delta plain
- **Child of**:
 [`Delta plain`](#delta_plain)
- The part of a delta plain essentially unaffected by basinal
processes. They do not differ substantially from alluvial environments
except that areas of swamp, marsh and lakes are usually more
widespread and channels may bifurcate downstream
- **Source:**
Readingh.G. & Collinson, J.D., 1996. Clastic coasts. 154-231 in Readingh.G. (ed.), Sedimentary Environments: Processses, Facies and Stratigraphy, third edition. Blackwell Science, Oxford, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_delta_plain
- **Other Properties:**

[]{#gibber_plain}

#######  Gibber plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/gibber_plain
- **Other Properties:**

[]{#playa}

#######  Playa
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Source:**
Based on Hawley and Parsons, 1980, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/playa
- **Other Properties:**

[]{#sand_plain}

#######  Sand plain
- **Child of**:
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Eolian process setting`](#eolian_process_setting)
 [`Plain`](#plain)
- A sand-covered plain dominated by aeolian processes.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/sand_plain
- **Other Properties:**

[]{#plateau}

######  Plateau
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- An extensive, relatively flat area of the Earth's surface that is
significantly elevated above the adjacent region.
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/plateau
- **Other Properties:**

[]{#ocean_plateau}

#######  Ocean plateau
- **Child of**:
 [`Ocean highland`](#ocean_highland)
 [`Plateau`](#plateau)
- Region of elevated ocean crust that commonly rises to within 2-3 km
of the surface above an abyssal sea floor that lies several km deeper.
Climate and water depths are such that a marine carbonate platform
does not develop.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_plateau
- **Other Properties:**

[]{#ridge}

######  Ridge
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- A long, narrow, elevated landform separated from the surrounding
terrain by slopes.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Ridge, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ridge
- **Other Properties:**

[]{#submarine_ridge}

#######  Submarine ridge
- **Child of**:
 [`Ocean highland`](#ocean_highland)
 [`Ridge`](#ridge)
- A ridge on the ocean floor
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_ridge
- **Other Properties:**

[]{#active_ocean_ridge}

########  Active ocean ridge
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
- Ocean highland associated with a divergent continental margin
(spreading center). Setting is characterized by active volcanism,
locally steep relief, hydrothermal activity, and pelagic
sedimentation.
- **Concept URI:** https://w3id.org/sesar/sampledfeature/active_ocean_ridge
- **Other Properties:**

[]{#axial_valley}

#########  Ocean ridge axial valley
- **Child of**:
 [`Active ocean ridge`](#active_ocean_ridge)
- A linear depression along the crest of an active ocean ridge
spreading center.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/axial_valley
- **Other Properties:**

[]{#submarine_vent}

#########  Submarine vent
- **Child of**:
 [`Active ocean ridge`](#active_ocean_ridge)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_vent
- **Other Properties:**

[]{#inactive_spreading_center}

########  Inactive spreading center
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Submarine ridge`](#submarine_ridge)
 [`Volcanic Setting`](#volcanic_setting)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Alternate labels:**
Aseismic ocean ridge
- **Source:**
IMLGS sampled feature, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/inactive_spreading_center
- **Other Properties:**

[]{#ocean_ridge_crest}

########  Ocean ridge crest
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_ridge_crest
- **Other Properties:**

[]{#ocean_ridge_flank}

########  Ocean ridge flank
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_ridge_flank
- **Other Properties:**

[]{#valley}

######  Valley
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
- a relatively flat area bounded by hills or mountains
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/valley
- **Other Properties:**

[]{#polar_climatic_setting}

#####  Polar climatic setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting with climate dominated by temperatures below the freezing
temperature of water. Includes polar deserts because precipitation is
generally scant at high latitude. Climate controlled by arctic air
masses, cold dry environment with short summer.
- **Source:**
Cleland, D.T., Avers, P.E., McNab, W.H., Jensen, M.E., Bailey, R.G., King, T., Russell, W.E. 1997. National Hierarchical Framework of Ecological Units, in Boyce, M. S., Haney, A., ed., Ecosystem Management Applications for Sustainable Forest and WildlifeResources: Yale University Press, New Haven, CT. pp. 181-200., 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/polar_climatic_setting
- **Other Properties:**

[]{#glacierenvironment}

######  Glacier environment
- **Child of**:
 [`Earth environment`](#earthenvironment)
 [`Polar climatic setting`](#polar_climatic_setting)
- Earth surface setting with geography defined by spatial relationship
to glaciers (e.g. on top of a glacier, next to a glacier, in front of
a glacier...). Processes related to moving ice dominate sediment
transport and deposition and landform development. Includes
subaqueous, shoreline, and terrestrial settings that are impacted by
the presence of glaciers. Considered a geographically defined setting
in that a glacier is a geographic feature.  Includes glacier, ice
sheet, ice shelf, iceberg, or rock or water directly under or on top
of such ice.
- **Alternate labels:**
glacier related setting
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/glacierenvironment
- **Other Properties:**

[]{#cirque}

#######  Cirque
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
 [`Physiographic feature`](#physiographic_feature)
- a steep-walled, half-bowl-like recess in a mountain, formed by the
erosive activty of a mountain glacier
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cirque
- **Other Properties:**

[]{#englacial_setting}

#######  Englacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Contained, embedded, or carried within the body of a glacier or ice
sheet, said of meltwater streams, till, drift, moraine
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/englacial_setting
- **Other Properties:**

[]{#glacial_outwash_plain}

#######  Glacial outwash plain
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Areas adjacent to glacial front dominated by sediment and water
supplied by glacial melting.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacial_outwash_plain
- **Other Properties:**

[]{#glacier_lateral_setting}

#######  Glacier lateral setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Settings adjacent to edges of confined glacier.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacier_lateral_setting
- **Other Properties:**

[]{#proglacial_setting}

#######  Proglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Immediately in front of or just beyond the outer limits of a glacier
or ice sheet, generally at or near its lower end, said of lakes,
streams, deposits, and other features produced by or derived from the
glacier ice
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/proglacial_setting
- **Other Properties:**

[]{#glacier_terminus}

########  Glacier terminus
- **Child of**:
 [`Proglacial setting`](#proglacial_setting)
- Region of sediment deposition due to melting of glacier ice.
ablation and flow till setting.
- **Source:**
NADM SLTTs, 2004, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacier_terminus
- **Other Properties:**

[]{#subglacial_setting}

#######  Subglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Formed or accumulated in or by the bottom parts of a glacier or ice
sheet, said of meltwater streams, till, moraine, etc.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subglacial_setting
- **Other Properties:**

[]{#supraglacial_setting}

#######  Supraglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Carried upon, deposited from, or pertaining to the top surface of a
glacier or ice sheet, said of meltwater streams, till, drift, etc.
(Jackson, 1997, p. 639). Dreimanis (1988, p. 39) recommendation that
\supraglacial\ supersede \superglacial\ is followed.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/supraglacial_setting
- **Other Properties:**

[]{#shoreline}

#####  Shoreline
- **Child of**:
 [`Earth surface`](#earthsurface)
- Geologic settings characterized by location adjacent to the ocean or
a lake. A zone of indefinite width (may be many kilometers), bordering
a body of water that extends from the water line inland to the first
major change in landform features. Includes settings that may be
subaerial, intermittently subaqueous, or shallow subaqueous, but are
intrinsically associated with the interface between land areas and
water bodies.
- **Alternate labels:**
Coast
- **Source:**
based on Neuendorf et al, 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/shoreline
- **Other Properties:**

[]{#barrier_island_coastline}

######  Barrier island coastline
- **Child of**:
 [`Shoreline`](#shoreline)
- setting meant to include all the various geographic elements
typically associated with a barrier island coastline, including the
barrier islands, and geomorphic/geographic elements that are linked by
processes associated with the presence of the island (e.g. wash over
fans, inlet channel, back barrier lagoon).
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/barrier_island_coastline
- **Other Properties:**

[]{#barrier_beach}

#######  Barrier beach
- **Child of**:
 [`Barrier island coastline`](#barrier_island_coastline)
 [`Beach`](#beach)
- A narrow, elongate sand or gravel ridge rising slightly above the
high-tide level and extending generally parallel with the shore, but
separated from it by a lagoon (Shepard, 1954, p.1904), estuary, or
marsh, it is extended by longshore transport and is rarely more than
several kilometers long.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/barrier_beach
- **Other Properties:**

[]{#barrier_lagoon}

#######  Barrier lagoon
- **Child of**:
 [`Barrier island coastline`](#barrier_island_coastline)
 [`Lagoonal setting`](#lagoonal_setting)
- A lagoon that is roughly parallel to the coast and is separated from
the open ocean by a strip of land or by a barrier reef. Tidal
influence is typically restricted and the lagoon is commonly
hypersaline.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/barrier_lagoon
- **Other Properties:**

[]{#beach}

######  Beach
- **Child of**:
 [`Shoreline`](#shoreline)
- The unconsolidated material at the shoreline that covers a gently
sloping zone, typically with a concave profile, extending landward
from the low-water line to the place where there is a definite change
in material or physiographic form (such as a cliff), or to the line of
permanent vegetation (usually the effective limit of the highest storm
waves), at the shore of a body of water, formed and washed by waves or
tides, usually covered by sand or gravel, and lacking a bare rocky
surface.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/beach
- **Other Properties:**

[]{#barrier_beach}

#######  Barrier beach
- **Child of**:
 [`Barrier island coastline`](#barrier_island_coastline)
 [`Beach`](#beach)
- A narrow, elongate sand or gravel ridge rising slightly above the
high-tide level and extending generally parallel with the shore, but
separated from it by a lagoon (Shepard, 1954, p.1904), estuary, or
marsh, it is extended by longshore transport and is rarely more than
several kilometers long.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/barrier_beach
- **Other Properties:**

[]{#cape}

######  Cape
- **Child of**:
 [`Physiographic feature`](#physiographic_feature)
 [`Shoreline`](#shoreline)
- A mass of land that extends from a coastline into an adjacent body
of water
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cape
- **Other Properties:**

[]{#carbonate_dominated_shoreline}

######  Carbonate dominated shoreline
- **Child of**:
 [`Shoreline`](#shoreline)
- A shoreline setting in which terrigenous input is minor compared to
local carbonate sediment production. Constructional biogenic activity
is an important element in geomorphic development.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/carbonate_dominated_shoreline
- **Other Properties:**

[]{#coastal_plain}

######  Coastal plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Plain`](#plain)
 [`Shoreline`](#shoreline)
- A low relief plain bordering a water body extending inland to the
nearest elevated land, sloping very gently towards the water body.
Distinguished from alluvial plain by presence of relict shoreline-
related deposits or morphology.
- **Source:**
based on Neuendorf et al, 2005, p. 125, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/coastal_plain
- **Other Properties:**

[]{#deltaic_system}

######  Deltaic system
- **Child of**:
 [`Shoreline`](#shoreline)
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
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/deltaic_system
- **Other Properties:**

[]{#delta_front}

#######  Delta front
- **Child of**:
 [`Deltaic system`](#deltaic_system)
- A narrow zone where deposition in deltas is most active, consisting
of a continuous sheet of sand, and occurring within the effective
depth of wave erosion (10 m or less). It is the zone separating the
prodelta from the delta plain, and it may or may not be steep\
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/delta_front
- **Other Properties:**

[]{#delta_plain}

#######  Delta plain
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Plain`](#plain)
- The level or nearly level surface composing the landward part of a
large or compound delta, strictly, an alluvial plain characterized by
repeated channel bifurcation and divergence, multiple distributary
channels, and interdistributary flood basins
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/delta_plain
- **Other Properties:**

[]{#lower_delta_plain}

########  Lower delta plain
- **Child of**:
 [`Delta plain`](#delta_plain)
 [`Tidal setting`](#tidal_setting)
- The part of a delta plain which is penetrated by saline water and is
subject to tidal processes
- **Source:**
Readingh.G. & Collinson, J.D., 1996. Clastic coasts. 154-231 in Readingh.G. (ed.), Sedimentary Environments: Processses, Facies and Stratigraphy, third edition. Blackwell Science, Oxford, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_delta_plain
- **Other Properties:**

[]{#upper_delta_plain}

########  Upper delta plain
- **Child of**:
 [`Delta plain`](#delta_plain)
- The part of a delta plain essentially unaffected by basinal
processes. They do not differ substantially from alluvial environments
except that areas of swamp, marsh and lakes are usually more
widespread and channels may bifurcate downstream
- **Source:**
Readingh.G. & Collinson, J.D., 1996. Clastic coasts. 154-231 in Readingh.G. (ed.), Sedimentary Environments: Processses, Facies and Stratigraphy, third edition. Blackwell Science, Oxford, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_delta_plain
- **Other Properties:**

[]{#distributary_channel}

#######  Delta distributary channel
- **Child of**:
 [`Channel`](#channel)
 [`Deltaic system`](#deltaic_system)
- A divergent stream flowing away from the main stream and not
returning to it, as in a delta or on an alluvial plain
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/distributary_channel
- **Other Properties:**

[]{#distributary_mouth}

#######  Delta distributary mouth
- **Child of**:
 [`Deltaic system`](#deltaic_system)
- The mouth of a delta distributary channel where fluvial discharge
moves from confined to unconfined flow conditions
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/distributary_mouth
- **Other Properties:**

[]{#estuarine_delta}

#######  Estuarine delta
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Estuary`](#estuary)
- A delta that has filled, or is in the process of filling, an estuary
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/estuarine_delta
- **Other Properties:**

[]{#interdistributary_bay}

#######  Interdistributary bay
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Subaqueous setting`](#subaqueous_setting)
- A pronounced indentation of the delta front between advancing stream
distributaries, occupied by shallow water, and either open to the sea
or partly enclosed by minor distributaries
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/interdistributary_bay
- **Other Properties:**

[]{#lacustrine_delta}

#######  Lacustrine delta
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Lacustrine setting`](#lacustrine_setting)
- The low, nearly flat, alluvial tract of land at or near the mouth of
a river, commonly forming a triangular or fan-shaped plain of
considerable area, crossed by many distributaries of the main river,
perhaps extending beyond the general trend of the lake shore,
resulting from the accumulation of sediment supplied by the river in
such quantities that it is not removed by waves or currents. Most
deltas are partly subaerial and partly below water.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lacustrine_delta
- **Other Properties:**

[]{#prodelta}

#######  Prodelta setting
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Subaqueous setting`](#subaqueous_setting)
- The part of a delta that is below the effective depth of wave
erosion, lying beyond the delta front, and sloping gently down to the
floor of the basin into which the delta is advancing and where clastic
river sediment ceases to be a significant part of the basin-floor
deposits, it is entirely below the water level
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/prodelta
- **Other Properties:**

[]{#estuary}

######  Estuary
- **Child of**:
 [`Shoreline`](#shoreline)
- Environments at the seaward end or the widened funnel-shaped tidal
mouth of a river valley where fresh water comes into contact with
seawater and where tidal effects are evident (adapted from Glossary of
Geology, Jackson, 1997, p. 217).
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/estuary
- **Other Properties:**

[]{#estuarine_delta}

#######  Estuarine delta
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Estuary`](#estuary)
- A delta that has filled, or is in the process of filling, an estuary
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/estuarine_delta
- **Other Properties:**

[]{#estuarine_lagoon}

#######  Estuarine lagoon
- **Child of**:
 [`Estuary`](#estuary)
 [`Lagoonal setting`](#lagoonal_setting)
- A lagoon produced by the temporary sealing of a river estuary by a
storm barrier. Such lagoons are usually seasonal and exist until the
river breaches the barrier, they occur in regions of low or spasmodic
rainfall
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/estuarine_lagoon
- **Other Properties:**

[]{#lagoonal_setting}

######  Lagoonal setting
- **Child of**:
 [`Shoreline`](#shoreline)
- A shallow stretch of salt or brackish water, partly or completely
separated from a sea or lake by an offshore reef, barrier island, sand
or spit (Jackson, 1997). Water is shallow, tidal and wave-produced
effects on sediments, strong light reaches sediment..
- **Source:**
generalize from Jackson 1997 and North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lagoonal_setting
- **Other Properties:**

[]{#barrier_lagoon}

#######  Barrier lagoon
- **Child of**:
 [`Barrier island coastline`](#barrier_island_coastline)
 [`Lagoonal setting`](#lagoonal_setting)
- A lagoon that is roughly parallel to the coast and is separated from
the open ocean by a strip of land or by a barrier reef. Tidal
influence is typically restricted and the lagoon is commonly
hypersaline.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/barrier_lagoon
- **Other Properties:**

[]{#estuarine_lagoon}

#######  Estuarine lagoon
- **Child of**:
 [`Estuary`](#estuary)
 [`Lagoonal setting`](#lagoonal_setting)
- A lagoon produced by the temporary sealing of a river estuary by a
storm barrier. Such lagoons are usually seasonal and exist until the
river breaches the barrier, they occur in regions of low or spasmodic
rainfall
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/estuarine_lagoon
- **Other Properties:**

[]{#low_energy_shoreline_setting}

######  Low energy shoreline setting
- **Child of**:
 [`Shoreline`](#shoreline)
- Settings characterized by very low surface slope and proximity to
shoreline. Generally within peritidal setting, but characterized by
low surface gradients and generally low-energy sedimentary processes.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/low_energy_shoreline_setting
- **Other Properties:**

[]{#algal_flat}

#######  Algal flat
- **Child of**:
 [`Low energy shoreline setting`](#low_energy_shoreline_setting)
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
- **Source:**
http://www.audubonofflorida.org/main/wetlands/chp3.htm, Reading, 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/algal_flat
- **Other Properties:**

[]{#marginal_marine_sabkha}

#######  Marginal marine sabkha
- **Child of**:
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Low energy shoreline setting`](#low_energy_shoreline_setting)
- Setting characterized by arid to semi-arid conditions on restricted
coastal plains mostly above normal high tide level, with evaporite-
saline mineral, tidal-flood, and eolian deposits. Boundaries with
intertidal setting and non-tidal terrestrial setting are gradational.
(Jackson, 1997, p. 561).
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, based on Jackson 1997, Neuendorf et al. 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/marginal_marine_sabkha
- **Other Properties:**

[]{#mud_flat}

#######  Mud flat
- **Child of**:
 [`Low energy shoreline setting`](#low_energy_shoreline_setting)
- A relatively level area of fine grained material (e.g. silt) along a
shore (as in a sheltered estuary or chenier-plain) or around an
island, alternately covered and uncovered by the tide or covered by
shallow water, and barren of vegetation. Includes most tidal flats,
but lacks denotation of tidal influence.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, Jackson, 1997, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mud_flat
- **Other Properties:**

[]{#rocky_coast}

######  Rocky coast
- **Child of**:
 [`Shoreline`](#shoreline)
- Shoreline with significant relief and abundant rock outcrop.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/rocky_coast
- **Other Properties:**

[]{#strandplain}

######  Strandplain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Shoreline`](#shoreline)
- A prograded shore built seaward by waves and currents, and
continuous for some distance along the coast. It is characterized by
subparallel beach ridges and swales, in places with associated dunes.
- **Source:**
based on Jackson 1997, p. 626, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/strandplain
- **Other Properties:**

[]{#supratidal_setting}

######  Supratidal setting
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Shoreline`](#shoreline)
- Pertaining to the shore area marginal to the littoral zone, just
above high-tide level
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/supratidal_setting
- **Other Properties:**

[]{#tidal_setting}

######  Tidal setting
- **Child of**:
 [`Shoreline`](#shoreline)
- Setting subject to tidal processes
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_setting
- **Other Properties:**

[]{#intertidal}

#######  Intertidal setting
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
 [`Tidal setting`](#tidal_setting)
- Pertaining to the benthic ocean environment or depth zone between
high water and low water, also, pertaining to the organisms of that
environment
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intertidal
- **Other Properties:**

[]{#lower_delta_plain}

#######  Lower delta plain
- **Child of**:
 [`Delta plain`](#delta_plain)
 [`Tidal setting`](#tidal_setting)
- The part of a delta plain which is penetrated by saline water and is
subject to tidal processes
- **Source:**
Readingh.G. & Collinson, J.D., 1996. Clastic coasts. 154-231 in Readingh.G. (ed.), Sedimentary Environments: Processses, Facies and Stratigraphy, third edition. Blackwell Science, Oxford, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_delta_plain
- **Other Properties:**

[]{#tidal_channel}

#######  Tidal channel
- **Child of**:
 [`Channel`](#channel)
 [`Subaqueous setting`](#subaqueous_setting)
 [`Tidal setting`](#tidal_setting)
- A major channel followed by the tidal currents, extending from
offshore into a tidal marsh or a tidal flat.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_channel
- **Other Properties:**

[]{#tidal_flat}

#######  Tidal flat
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Tidal setting`](#tidal_setting)
- An extensive, nearly horizontal, barren tract of land that is
alternately covered and uncovered by the tide, and consisting of
unconsolidated sediment (mostly mud and sand). It may form the top
surface of a deltaic deposit.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_flat
- **Other Properties:**

[]{#tidal_marsh}

########  Tidal marsh
- **Child of**:
 [`Swamp or marsh`](#swamp_or_marsh)
 [`Tidal flat`](#tidal_flat)
- A marsh bordering a coast (as in a shallow lagoon or sheltered bay),
formed of mud and of the resistant mat of roots of salt-tolerant
plants, and regularly inundated during high tides, a marshy tidal
flat.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_marsh
- **Other Properties:**

[]{#subaqueous_setting}

#####  Subaqueous setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting situated in or under permanent, standing water. Used for
marine and lacustrine settings, but not for fluvial settings.
- **Source:**
based on North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subaqueous_setting
- **Other Properties:**

[]{#lakeriverstreambottom}

######  Lake river or stream bottom
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
- Sampled feature is the interface between the solid Earth interface
and a lake or flowing water body.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/lakeriverstreambottom
- **Other Properties:**

[]{#interdistributary_bay}

######  Interdistributary bay
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Subaqueous setting`](#subaqueous_setting)
- A pronounced indentation of the delta front between advancing stream
distributaries, occupied by shallow water, and either open to the sea
or partly enclosed by minor distributaries
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/interdistributary_bay
- **Other Properties:**

[]{#intertidal}

######  Intertidal setting
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
 [`Tidal setting`](#tidal_setting)
- Pertaining to the benthic ocean environment or depth zone between
high water and low water, also, pertaining to the organisms of that
environment
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intertidal
- **Other Properties:**

[]{#lacustrine_setting}

######  Lacustrine setting
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
 [`Terrestrial setting`](#terrestrial_setting)
- Setting associated with a lake. Always overlaps with terrestrial,
may overlap with subaerial, subaqueous, or shoreline.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lacustrine_setting
- **Other Properties:**

[]{#lacustrine_delta}

#######  Lacustrine delta
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Lacustrine setting`](#lacustrine_setting)
- The low, nearly flat, alluvial tract of land at or near the mouth of
a river, commonly forming a triangular or fan-shaped plain of
considerable area, crossed by many distributaries of the main river,
perhaps extending beyond the general trend of the lake shore,
resulting from the accumulation of sediment supplied by the river in
such quantities that it is not removed by waves or currents. Most
deltas are partly subaerial and partly below water.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lacustrine_delta
- **Other Properties:**

[]{#lake}

#######  Lake
- **Child of**:
 [`Terrestrial water body`](#terrestrialwaterbody)
 [`Lacustrine setting`](#lacustrine_setting)
- A body of water on the Earth's surface, localized in a basin or
interconnected basins surrounded by dry land.
- **Alternate labels:**
Pond
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake
- **Other Properties:**

[]{#lake_fresh_water}

########  Fresh water lake
- **Child of**:
 [`Lake`](#lake)
- Natural lakes or human impounded fresh water resevoirs.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake_fresh_water
- **Other Properties:**

[]{#lake_saline}

########  Saline lake
- **Child of**:
 [`Lake`](#lake)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake_saline
- **Other Properties:**

[]{#marine_setting}

######  Marine setting
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
- Setting characterized by location under the surface of the sea.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, Webster's Encyclopedic Unabridged Dictionary of the English Language, 2001, p. 1894., 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/marine_setting
- **Other Properties:**

[]{#marinewaterbodybottom}

#######  Marine water body bottom
- **Child of**:
 [`Marine setting`](#marine_setting)
- Sampled feature is the interface between the solid Earth and a
marine or brackish water body.  Includes benthic boundary layer: the
bottom layer of water and the uppermost layer of sediment directly
influenced by the overlying water.
- **Alternate labels:**
Sea floor
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/marinewaterbodybottom
- **Other Properties:**

[]{#abyssal_plain}

########  Basin plain
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Plain`](#plain)
- Near flat areas of ocean floor, slope less than 1:1000, generally
receive only distal turbidite and pelagic sediments.
- **Alternate labels:**
Abyssal plain
- **Source:**
Bates & Jackson, 1987, Heezen & Laughton, 1963, Reading, 1978, p. 390, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/abyssal_plain
- **Other Properties:**

[]{#biological_reef}

########  Biological reef
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
- A ridgelike or moundlike structure, layered or massive, built by
sedentary calcareous organisms, esp. corals, and consisting mostly of
their remains, it is wave-resistant and stands topographically above
the surrounding contemporaneously deposited sediment.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/biological_reef
- **Other Properties:**

[]{#backreef}

#########  Backreef setting
- **Child of**:
 [`Biological reef`](#biological_reef)
- The landward side of a reef. The term is often used adjectivally to
refer to deposits within the restricted lagoon behind a barrier reef,
such as the back-reef facies of lagoonal deposits. In some places, as
on a platform-edge reef tract, back reef refers to the side of the
reef away from the open sea, even though no land may be nearby
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/backreef
- **Other Properties:**

[]{#forereef_setting}

#########  Forereef setting
- **Child of**:
 [`Biological reef`](#biological_reef)
- The seaward side of a reef, the slope covered with deposits of
coarse reef talus
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/forereef_setting
- **Other Properties:**

[]{#reef_flat}

#########  Reef flat
- **Child of**:
 [`Biological reef`](#biological_reef)
- A stony platform of reef rock, landward of the reef crest at or
above the low tide level, occasionally with patches of living coral
and associated organisms, and commonly strewn with coral fragments and
coral sand. It may include shallow pools, irregular gullies, low
islands of sand or rubble (often vegetated, esp. by palms), and
scattered colonies of the more hardy species of coral
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/reef_flat
- **Other Properties:**

[]{#carbonate_mound}

########  Carbonate mound
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
- a seafloor elevation formed by calcareous framework-building
organisms, varying in shapes, sizes, and heights, generally less than
500 meters. These mounds can be circular, arcuate, elongated, or
irregular, with heights ranging from a few meters to over 300 meters,
and are commonly found in temperate to high latitudes on the
continental slope.
- **Source:**
SESAR legacy localities, 
https://www.sciencedirect.com/topics/earth-and-planetary-sciences/carbonate-mound: AI generated definition based on: 
Treatise on Geomorphology (Second Edition), 2022 (https://www.sciencedirect.com/science/article/pii/B9780128182345001292), 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/carbonate_mound
- **Other Properties:**

[]{#marine_carbonate_platform}

########  Marine carbonate platform
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- A shallow submerged plateau separated from continental landmasses,
on which high biological carbonate production rates produce enough
sediment to maintain the platform surface near sea level. Grades into
atoll as area becomes smaller and ringing coral reefs become more
prominent part of the setting.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/marine_carbonate_platform
- **Other Properties:**

[]{#ocean_highland}

########  Ocean highland
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- Broad category for subaqueous marine settings characterized by
significant relief above adjacent sea floor.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_highland
- **Other Properties:**

[]{#ocean_plateau}

#########  Ocean plateau
- **Child of**:
 [`Ocean highland`](#ocean_highland)
 [`Plateau`](#plateau)
- Region of elevated ocean crust that commonly rises to within 2-3 km
of the surface above an abyssal sea floor that lies several km deeper.
Climate and water depths are such that a marine carbonate platform
does not develop.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_plateau
- **Other Properties:**

[]{#seamount}

#########  Seamount
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Ocean highland`](#ocean_highland)
 [`Volcanic Setting`](#volcanic_setting)
- Setting that consists of a conical mountain on the ocean floor
(guyot). Typically characterized by active volcanism, pelagic
sedimentation. If the mountain is high enough to reach the photic
zone, carbonate production may result in reef building to produce a
carbonate platform or atoll setting.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/seamount
- **Other Properties:**

[]{#submarine_ridge}

#########  Submarine ridge
- **Child of**:
 [`Ocean highland`](#ocean_highland)
 [`Ridge`](#ridge)
- A ridge on the ocean floor
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_ridge
- **Other Properties:**

[]{#active_ocean_ridge}

##########  Active ocean ridge
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
- Ocean highland associated with a divergent continental margin
(spreading center). Setting is characterized by active volcanism,
locally steep relief, hydrothermal activity, and pelagic
sedimentation.
- **Concept URI:** https://w3id.org/sesar/sampledfeature/active_ocean_ridge
- **Other Properties:**

[]{#axial_valley}

###########  Ocean ridge axial valley
- **Child of**:
 [`Active ocean ridge`](#active_ocean_ridge)
- A linear depression along the crest of an active ocean ridge
spreading center.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/axial_valley
- **Other Properties:**

[]{#submarine_vent}

###########  Submarine vent
- **Child of**:
 [`Active ocean ridge`](#active_ocean_ridge)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_vent
- **Other Properties:**

[]{#inactive_spreading_center}

##########  Inactive spreading center
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Submarine ridge`](#submarine_ridge)
 [`Volcanic Setting`](#volcanic_setting)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Alternate labels:**
Aseismic ocean ridge
- **Source:**
IMLGS sampled feature, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/inactive_spreading_center
- **Other Properties:**

[]{#ocean_ridge_crest}

##########  Ocean ridge crest
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_ridge_crest
- **Other Properties:**

[]{#ocean_ridge_flank}

##########  Ocean ridge flank
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_ridge_flank
- **Other Properties:**

[]{#slope_rise_setting}

########  Slope rise setting
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- The part of a subaqueous basin that is between a bordering shelf
setting, which separate the basin from an adjacent landmass, and a
very low-relief basin plain setting.
- **Source:**
based on NADM SLTTs, 2004, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/slope_rise_setting
- **Other Properties:**

[]{#rise_continental}

#########  Seafloor rise, continental
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/rise_continental
- **Other Properties:**

[]{#rise_insular}

#########  Seafloor rise, insular
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/rise_insular
- **Other Properties:**

[]{#slope_continental}

#########  Seafloor slope, continental
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/slope_continental
- **Other Properties:**

[]{#slope_insular}

#########  Seafloor slope, insular
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/slope_insular
- **Other Properties:**

[]{#submarine_canyon}

########  Submarine canyon
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Canyon`](#canyon)
- A canyon that is cut in the ocean floor.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_canyon
- **Other Properties:**

[]{#submarine_channel}

########  Submarine channel
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Channel`](#channel)
-
- **Source:**
SESAR legacy localities, 
split IMLGS submarine canyon or channel into separate concepts, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_channel
- **Other Properties:**

[]{#submarine_escarpment}

########  Submarine escarpment
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Escarpment`](#escarpment)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_escarpment
- **Other Properties:**

[]{#submarine_fan}

########  Submarine fan
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- Large fan-shaped cones of sediment on the ocean floor, generally
associated with submarine canyons that provide sediment supply to
build the fan..
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_fan
- **Other Properties:**

[]{#above_carbonate_compensation_depth}

#######  Above carbonate compensation depth
- **Child of**:
 [`Marine setting`](#marine_setting)
- Marine environment in which carbonate sediment does not dissolve
before reaching the sea floor and can accumulate.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/above_carbonate_compensation_depth
- **Other Properties:**

[]{#abyssal_setting}

#######  Abyssal setting
- **Child of**:
 [`Marine setting`](#marine_setting)
- The ocean environment at water depths between 3500 and 6000 metres
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/abyssal_setting
- **Other Properties:**

[]{#bathyal_setting}

#######  Bathyal setting
- **Child of**:
 [`Marine setting`](#marine_setting)
- The ocean environment at water depths between 200 and 3500 metres
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/bathyal_setting
- **Other Properties:**

[]{#lower_bathyal_setting}

########  Lower bathyal setting
- **Child of**:
 [`Bathyal setting`](#bathyal_setting)
- The ocean environment at depths between 1000 and 3500 metres
- **Source:**
Neuendorf, K.K.E., Mehl, J.P. & Jackson, J.A. (eds), 2005. Glossary of geology, 5th Edition. American Geological Institute, Alexandria, 779 p., Berggren, W.A. & Miller, K.G., 1989. Cenozoic bathyal and abyssal calcareous benthic foraminiferal zonation. Micropalaeontology 35, 308-320, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_bathyal_setting
- **Other Properties:**

[]{#middle_bathyal_setting}

########  Middle bathyal setting
- **Child of**:
 [`Bathyal setting`](#bathyal_setting)
- The ocean environment at water depths between 600 and 1000 metres
- **Source:**
Berggren, W.A. & Miller, K.G., 1989. Cenozoic bathyal and abyssal calcareous benthic foraminiferal zonation. Micropalaeontology 35, 308-320, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/middle_bathyal_setting
- **Other Properties:**

[]{#upper_bathyal_setting}

########  upper bathyal setting
- **Child of**:
 [`Bathyal setting`](#bathyal_setting)
- The ocean environment at water depths between 200 and 600 metres
- **Source:**
Berggren, W.A. & Miller, K.G., 1989. Cenozoic bathyal and abyssal calcareous benthic foraminiferal zonation. Micropalaeontology 35, 308-320, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_bathyal_setting
- **Other Properties:**

[]{#below_carbonate_compensation_depth_setting}

#######  Below carbonate compensation depth setting
- **Child of**:
 [`Marine setting`](#marine_setting)
- Marine environment in which water is deep enough that carbonate
sediment goes into solution before it can accumulate on the sea floor.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/below_carbonate_compensation_depth_setting
- **Other Properties:**

[]{#continental_borderland}

#######  Continental borderland
- **Child of**:
 [`Marine setting`](#marine_setting)
- An area of the continental margin between the shoreline and the
continental slope that is topographically more complex than the
continental shelf. It is characterized by ridges and basins, some of
which are below the depth of the continental shelf. An example is the
southern California continental borderland,.... (Jackson, 1997, p.
138)..
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_borderland
- **Other Properties:**

[]{#deep_sea_trench}

#######  Deep sea trench
- **Child of**:
 [`Marine setting`](#marine_setting)
- Deep ocean basin with steep (average 10 degrees) slope toward land,
more gentle slope (average 5 degrees) towards the sea, and abundant
seismic activity on landward side of trench. Does not denote water
depth, but may be very deep.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/deep_sea_trench
- **Other Properties:**

[]{#continental_margin_trench}

########  Continental margin trench
- **Child of**:
 [`Deep sea trench`](#deep_sea_trench)
- A deep submarine valley associated with subduction of an oceanic
plate underneath a continent.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_margin_trench
- **Other Properties:**

[]{#hadal_setting}

########  Hadal setting
- **Child of**:
 [`Deep sea trench`](#deep_sea_trench)
- The deepest oceanic environment, i.e., over 6000 m in depth. Always
in deep sea trench.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hadal_setting
- **Other Properties:**

[]{#intraoceanic_trench}

########  Intraoceanic trench
- **Child of**:
 [`Deep sea trench`](#deep_sea_trench)
- A deep submarine valley associated with a subduction zone between
oceanic tectonic plates
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intraoceanic_trench
- **Other Properties:**

[]{#epicontinental_marine_setting}

#######  Epicontinental marine setting
- **Child of**:
 [`Marine setting`](#marine_setting)
- Marine setting situated within the interior of the continent, rather
than at the edge of a continent.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/epicontinental_marine_setting
- **Other Properties:**

[]{#marginal_shelf}

#######  Marginal shelf
- **Child of**:
 [`Marine setting`](#marine_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/marginal_shelf
- **Other Properties:**

[]{#continental_shelf}

########  Continental shelf
- **Child of**:
 [`Marginal shelf`](#marginal_shelf)
- That part of the ocean floor that is between the shoreline and the
continental slope (or, when there is no noticeable continental slope,
a depth of 200 m). It is characterized by its gentle slope of 0.1
degree (Jackson, 1997, p. 138). Continental shelves have a classic
shoreline-shelf-slope profile termed 'clinoform'.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_shelf
- **Other Properties:**

[]{#insular_shelf}

########  Insular shelf
- **Child of**:
 [`Marginal shelf`](#marginal_shelf)
- That part of the ocean floor that is between the shoreline of an
island and the shelf-slope boundary (or, when there is no noticeable
shelf-slope boundary, a depth of 200 m). It is characterized by its
gentle slope of 0.1 degree (Jackson, 1997, p. 138).
- **Source:**
IMLGS sampled feature, 
definition based on gsmlee:continental_shelf_setting definition, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/insular_shelf
- **Other Properties:**

[]{#marine_carbonate_platform}

#######  Marine carbonate platform
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- A shallow submerged plateau separated from continental landmasses,
on which high biological carbonate production rates produce enough
sediment to maintain the platform surface near sea level. Grades into
atoll as area becomes smaller and ringing coral reefs become more
prominent part of the setting.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/marine_carbonate_platform
- **Other Properties:**

[]{#neritic_setting}

#######  Neritic setting
- **Child of**:
 [`Marine setting`](#marine_setting)
- The ocean environment at depths between low-tide level and 200
metres, or between low-tide level and approximately the edge of the
continental shelf
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/neritic_setting
- **Other Properties:**

[]{#ocean_highland}

#######  Ocean highland
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- Broad category for subaqueous marine settings characterized by
significant relief above adjacent sea floor.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_highland
- **Other Properties:**

[]{#ocean_plateau}

########  Ocean plateau
- **Child of**:
 [`Ocean highland`](#ocean_highland)
 [`Plateau`](#plateau)
- Region of elevated ocean crust that commonly rises to within 2-3 km
of the surface above an abyssal sea floor that lies several km deeper.
Climate and water depths are such that a marine carbonate platform
does not develop.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_plateau
- **Other Properties:**

[]{#seamount}

########  Seamount
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Ocean highland`](#ocean_highland)
 [`Volcanic Setting`](#volcanic_setting)
- Setting that consists of a conical mountain on the ocean floor
(guyot). Typically characterized by active volcanism, pelagic
sedimentation. If the mountain is high enough to reach the photic
zone, carbonate production may result in reef building to produce a
carbonate platform or atoll setting.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/seamount
- **Other Properties:**

[]{#submarine_ridge}

########  Submarine ridge
- **Child of**:
 [`Ocean highland`](#ocean_highland)
 [`Ridge`](#ridge)
- A ridge on the ocean floor
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_ridge
- **Other Properties:**

[]{#active_ocean_ridge}

#########  Active ocean ridge
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
- Ocean highland associated with a divergent continental margin
(spreading center). Setting is characterized by active volcanism,
locally steep relief, hydrothermal activity, and pelagic
sedimentation.
- **Concept URI:** https://w3id.org/sesar/sampledfeature/active_ocean_ridge
- **Other Properties:**

[]{#axial_valley}

##########  Ocean ridge axial valley
- **Child of**:
 [`Active ocean ridge`](#active_ocean_ridge)
- A linear depression along the crest of an active ocean ridge
spreading center.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/axial_valley
- **Other Properties:**

[]{#submarine_vent}

##########  Submarine vent
- **Child of**:
 [`Active ocean ridge`](#active_ocean_ridge)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_vent
- **Other Properties:**

[]{#inactive_spreading_center}

#########  Inactive spreading center
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Submarine ridge`](#submarine_ridge)
 [`Volcanic Setting`](#volcanic_setting)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Alternate labels:**
Aseismic ocean ridge
- **Source:**
IMLGS sampled feature, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/inactive_spreading_center
- **Other Properties:**

[]{#ocean_ridge_crest}

#########  Ocean ridge crest
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_ridge_crest
- **Other Properties:**

[]{#ocean_ridge_flank}

#########  Ocean ridge flank
- **Child of**:
 [`Submarine ridge`](#submarine_ridge)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_ridge_flank
- **Other Properties:**

[]{#slope_rise_setting}

#######  Slope rise setting
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- The part of a subaqueous basin that is between a bordering shelf
setting, which separate the basin from an adjacent landmass, and a
very low-relief basin plain setting.
- **Source:**
based on NADM SLTTs, 2004, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/slope_rise_setting
- **Other Properties:**

[]{#rise_continental}

########  Seafloor rise, continental
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/rise_continental
- **Other Properties:**

[]{#rise_insular}

########  Seafloor rise, insular
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/rise_insular
- **Other Properties:**

[]{#slope_continental}

########  Seafloor slope, continental
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/slope_continental
- **Other Properties:**

[]{#slope_insular}

########  Seafloor slope, insular
- **Child of**:
 [`Slope rise setting`](#slope_rise_setting)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/slope_insular
- **Other Properties:**

[]{#submarine_bank}

#######  Submarine bank
- **Child of**:
 [`Marine setting`](#marine_setting)
- a part of the seabed that is shallow compared to its surrounding
area.
- **Source:**
SESAR legacy localities, 
https://en.wikipedia.org/wiki/Ocean_bank, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_bank
- **Other Properties:**

[]{#submarine_fan}

#######  Submarine fan
- **Child of**:
 [`Marine water body bottom`](#marinewaterbodybottom)
 [`Marine setting`](#marine_setting)
- Large fan-shaped cones of sediment on the ocean floor, generally
associated with submarine canyons that provide sediment supply to
build the fan..
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/submarine_fan
- **Other Properties:**

[]{#prodelta}

######  Prodelta setting
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Subaqueous setting`](#subaqueous_setting)
- The part of a delta that is below the effective depth of wave
erosion, lying beyond the delta front, and sloping gently down to the
floor of the basin into which the delta is advancing and where clastic
river sediment ceases to be a significant part of the basin-floor
deposits, it is entirely below the water level
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/prodelta
- **Other Properties:**

[]{#subaqueous_bar}

######  Subaqueous bar
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subaqueous_bar
- **Other Properties:**

[]{#tidal_channel}

######  Tidal channel
- **Child of**:
 [`Channel`](#channel)
 [`Subaqueous setting`](#subaqueous_setting)
 [`Tidal setting`](#tidal_setting)
- A major channel followed by the tidal currents, extending from
offshore into a tidal marsh or a tidal flat.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_channel
- **Other Properties:**

[]{#terrestrial_setting}

#####  Terrestrial setting
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting characterized by absence of direct marine influence. Most of
the subaerial settings are also terrestrial, but e.g. lacustrine
settings, while terrestrial, are not subaerial.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/terrestrial_setting
- **Other Properties:**

[]{#bog}

######  Bog
- **Child of**:
 [`Terrestrial setting`](#terrestrial_setting)
 [`Wetland`](#wetland)
- Waterlogged, spongy ground, consisting primarily of mosses,
containing acidic, decaying vegetation that may develop into peat.
- **Source:**
Jackson, 1997, North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/bog
- **Other Properties:**

[]{#drainage_basin}

######  Drainage basin
- **Child of**:
 [`Terrestrial setting`](#terrestrial_setting)
- an area of land where all flowing surface water converges to a
single point, such as a river mouth, or flows into another body of
water, such as a lake or ocean
- **Alternate labels:**
Watershed
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/drainage_basin
- **Other Properties:**

[]{#gibber_plain}

######  Gibber plain
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- A desert plain strewn with wind-abraded pebbles, or gibbers, a
gravelly desert.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/gibber_plain
- **Other Properties:**

[]{#glacial_outwash_plain}

######  Glacial outwash plain
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Areas adjacent to glacial front dominated by sediment and water
supplied by glacial melting.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacial_outwash_plain
- **Other Properties:**

[]{#lacustrine_setting}

######  Lacustrine setting
- **Child of**:
 [`Subaqueous setting`](#subaqueous_setting)
 [`Terrestrial setting`](#terrestrial_setting)
- Setting associated with a lake. Always overlaps with terrestrial,
may overlap with subaerial, subaqueous, or shoreline.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lacustrine_setting
- **Other Properties:**

[]{#lacustrine_delta}

#######  Lacustrine delta
- **Child of**:
 [`Deltaic system`](#deltaic_system)
 [`Lacustrine setting`](#lacustrine_setting)
- The low, nearly flat, alluvial tract of land at or near the mouth of
a river, commonly forming a triangular or fan-shaped plain of
considerable area, crossed by many distributaries of the main river,
perhaps extending beyond the general trend of the lake shore,
resulting from the accumulation of sediment supplied by the river in
such quantities that it is not removed by waves or currents. Most
deltas are partly subaerial and partly below water.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lacustrine_delta
- **Other Properties:**

[]{#lake}

#######  Lake
- **Child of**:
 [`Terrestrial water body`](#terrestrialwaterbody)
 [`Lacustrine setting`](#lacustrine_setting)
- A body of water on the Earth's surface, localized in a basin or
interconnected basins surrounded by dry land.
- **Alternate labels:**
Pond
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake
- **Other Properties:**

[]{#lake_fresh_water}

########  Fresh water lake
- **Child of**:
 [`Lake`](#lake)
- Natural lakes or human impounded fresh water resevoirs.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake_fresh_water
- **Other Properties:**

[]{#lake_saline}

########  Saline lake
- **Child of**:
 [`Lake`](#lake)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake_saline
- **Other Properties:**

[]{#piedmont_slope}

######  Piedmont slope
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Location on gentle slope at the foot of a mountain, generally used
in terms of intermontane-basin terrain. Main components include: (a)
An erosional surface on bedrock adjacent to the receding mountain
front (pediment, rock pediment), (b) A constructional surface
comprising individual alluvial fans and interfan valleys, also near
the mountain front, and (c) A distal complex of coalescent fans
(bajada), and alluvial slopes without fan form. Piedmont slopes grade
to basin-floor depressions with alluvial and temporary lake plains or
to surfaces associated with through drainage.
- **Source:**
Hawley and Parsons, 1980+F98, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/piedmont_slope
- **Other Properties:**

[]{#alluvial_fan}

#######  Alluvial fan
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
- A low, outspread, relatively flat to gently sloping mass of loose
rock material, shaped like an open fan or a segment of a cone,
deposited by a stream (esp. in a semiarid region) at the place where
it issues from a narrow mountain valley upon a plain or broad valley,
or where a tributary stream is near or at its junction with the main
stream, or wherever a constriction in a valley abruptly ceases or the
gradient of the stream suddenly decreases, it is steepest near the
mouth of the valley where its apex points upstream, and it slopes
gently and convexly outward with gradually decreasing gradient
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/alluvial_fan
- **Other Properties:**

[]{#alluvial_plain}

#######  Alluvial plain
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
 [`Plain`](#plain)
- An assemblage landforms produced by alluvial and fluvial processes
(braided streams, terraces, etc.) that form low gradient, regional
ramps along the flanks of mountains and extend great distances from
their sources (e.g.high Plains of North America). (NRCS GLOSSARY OF
LANDFORM AND GEOLOGIC TERMS). A level or gently sloping tract or a
slightly undulating land surface produced by extensive deposition of
alluvium... Synonym-- wash plain,...river plain, aggraded valley
plain,... (Jackson, 1997, p. 17). May include one or more River plain
systems.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/alluvial_plain
- **Other Properties:**

[]{#pediment}

#######  Pediment
- **Child of**:
 [`Piedmont slope`](#piedmont_slope)
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
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, NRCS, 2001, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/pediment
- **Other Properties:**

[]{#playa}

######  Playa
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Arid or semi arid environment`](#arid_or_semi_arid_environment)
 [`Plain`](#plain)
 [`Terrestrial setting`](#terrestrial_setting)
- The usually dry and nearly level plain that occupies the lowest
parts of closed depressions, such as those occurring on intermontane
basin floors. Temporary flooding occurs primarily in response to
precipitation-runoff events.
- **Source:**
Based on Hawley and Parsons, 1980, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/playa
- **Other Properties:**

[]{#river_system}

######  River system
- **Child of**:
 [`Subaerial surface environment`](#subaerialsurfaceenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Geologic setting dominated by a river system in any climatic
setting. Includes active channels, abandoned channels, levees, oxbow
lakes, flood plain. May be part of an alluvial plain that includes
terraces composed of abandoned river plain deposits.
- **Alternate labels:**
Fluvial setting
- **Source:**
<http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment>
- **Concept URI:** https://w3id.org/sesar/sampledfeature/river_system
- **Other Properties:**

[]{#abandoned_channel}

#######  Abandoned river channel
- **Child of**:
 [`River system`](#river_system)
- A drainage channel along which runoff no longer occurs, as on an
alluvial fan
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/abandoned_channel
- **Other Properties:**

[]{#cutoff_meander}

#######  Cutoff meander
- **Child of**:
 [`River system`](#river_system)
- The abandoned, bow- or horseshoe-shaped channel of a former meander,
left when the stream formed a cutoff across a narrow meander neck.
Note that these are typically lakes, thus also lacustrine.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cutoff_meander
- **Other Properties:**

[]{#floodplain}

#######  Floodplain
- **Child of**:
 [`River system`](#river_system)
- The surface or strip of relatively smooth land adjacent to a river
channel, constructed by the present river in its existing regimen and
covered with water when the river overflows its banks. It is built of
alluvium carried by the river during floods and deposited in the
sluggish water beyond the influence of the swiftest current. A river
has one floodplain and may have one or more terraces representing
abandoned floodplains
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/floodplain
- **Other Properties:**

[]{#river_channel}

#######  River channel
- **Child of**:
 [`Channel`](#channel)
 [`River system`](#river_system)
- The bed where a natural body of surface water flows or may flow, a
natural passageway or depression of perceptible extent containing
continuously or periodically flowing water, or forming a connecting
link between two bodies of water, a watercourse
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/river_channel
- **Other Properties:**

[]{#braided_channel}

########  Braided river channel
- **Child of**:
 [`River channel`](#river_channel)
- A stream that divides into or follows an interlacing or tangled
network of several small branching and reuniting shallow channels
separated from each other by ephemeral branch islands or channel bars,
resembling in plan the strands of a complex braid. Such a stream is
generally believed to indicate an inability to carry all of its load,
such as an overloaded and aggrading stream flowing in a wide channel
on a floodplain
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/braided_channel
- **Other Properties:**

[]{#meandering_channel}

########  Meandering river channel
- **Child of**:
 [`River channel`](#river_channel)
- Produced by a mature stream swinging from side to side as it flows
across its floodplain or shifts its course laterally toward the convex
side of an original curve
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/meandering_channel
- **Other Properties:**

[]{#volcano}

#####  Volcano
- **Child of**:
 [`Earth surface`](#earthsurface)
 [`Volcanic Setting`](#volcanic_setting)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/volcano
- **Other Properties:**

[]{#wetland}

#####  Wetland
- **Child of**:
 [`Earth surface`](#earthsurface)
- Setting characterized by gentle surface slope, and at least
intermittent presence of standing water, which may be fresh, brackish,
or saline. Wetland may be terrestrial setting or shoreline setting.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/wetland
- **Other Properties:**

[]{#bog}

######  Bog
- **Child of**:
 [`Terrestrial setting`](#terrestrial_setting)
 [`Wetland`](#wetland)
- Waterlogged, spongy ground, consisting primarily of mosses,
containing acidic, decaying vegetation that may develop into peat.
- **Source:**
Jackson, 1997, North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/,, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/bog
- **Other Properties:**

[]{#swamp_or_marsh}

######  Swamp or marsh
- **Child of**:
 [`Wetland`](#wetland)
- A water-saturated, periodically wet or continually flooded area with
the surface not deeply submerged, essentially without the formation of
peat. Marshes are characterized by sedges, cattails, rushes, or other
aquatic and grasslike vegetation. Swamps are characterized by tree and
brush vegetation.
- **Source:**
Neuendorf et al 2005, Soil Science Society of America, 1997., 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/swamp_or_marsh
- **Other Properties:**

[]{#tidal_marsh}

#######  Tidal marsh
- **Child of**:
 [`Swamp or marsh`](#swamp_or_marsh)
 [`Tidal flat`](#tidal_flat)
- A marsh bordering a coast (as in a shallow lagoon or sheltered bay),
formed of mud and of the resistant mat of roots of salt-tolerant
plants, and regularly inundated during high tides, a marshy tidal
flat.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tidal_marsh
- **Other Properties:**

[]{#glacierenvironment}

####  Glacier environment
- **Child of**:
 [`Earth environment`](#earthenvironment)
 [`Polar climatic setting`](#polar_climatic_setting)
- Earth surface setting with geography defined by spatial relationship
to glaciers (e.g. on top of a glacier, next to a glacier, in front of
a glacier...). Processes related to moving ice dominate sediment
transport and deposition and landform development. Includes
subaqueous, shoreline, and terrestrial settings that are impacted by
the presence of glaciers. Considered a geographically defined setting
in that a glacier is a geographic feature.  Includes glacier, ice
sheet, ice shelf, iceberg, or rock or water directly under or on top
of such ice.
- **Alternate labels:**
glacier related setting
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/glacierenvironment
- **Other Properties:**

[]{#cirque}

#####  Cirque
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
 [`Physiographic feature`](#physiographic_feature)
- a steep-walled, half-bowl-like recess in a mountain, formed by the
erosive activty of a mountain glacier
- **Source:**
Neuendorf et al., 2005, Glossary of Geology, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/cirque
- **Other Properties:**

[]{#englacial_setting}

#####  Englacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Contained, embedded, or carried within the body of a glacier or ice
sheet, said of meltwater streams, till, drift, moraine
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/englacial_setting
- **Other Properties:**

[]{#glacial_outwash_plain}

#####  Glacial outwash plain
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
 [`Terrestrial setting`](#terrestrial_setting)
- Areas adjacent to glacial front dominated by sediment and water
supplied by glacial melting.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacial_outwash_plain
- **Other Properties:**

[]{#glacier_lateral_setting}

#####  Glacier lateral setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Settings adjacent to edges of confined glacier.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacier_lateral_setting
- **Other Properties:**

[]{#proglacial_setting}

#####  Proglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Immediately in front of or just beyond the outer limits of a glacier
or ice sheet, generally at or near its lower end, said of lakes,
streams, deposits, and other features produced by or derived from the
glacier ice
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/proglacial_setting
- **Other Properties:**

[]{#glacier_terminus}

######  Glacier terminus
- **Child of**:
 [`Proglacial setting`](#proglacial_setting)
- Region of sediment deposition due to melting of glacier ice.
ablation and flow till setting.
- **Source:**
NADM SLTTs, 2004, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/glacier_terminus
- **Other Properties:**

[]{#subglacial_setting}

#####  Subglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Formed or accumulated in or by the bottom parts of a glacier or ice
sheet, said of meltwater streams, till, moraine, etc.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subglacial_setting
- **Other Properties:**

[]{#supraglacial_setting}

#####  Supraglacial setting
- **Child of**:
 [`Glacier environment`](#glacierenvironment)
- Carried upon, deposited from, or pertaining to the top surface of a
glacier or ice sheet, said of meltwater streams, till, drift, etc.
(Jackson, 1997, p. 639). Dreimanis (1988, p. 39) recommendation that
\supraglacial\ supersede \superglacial\ is followed.
- **Source:**
North American Geologic-map Data Model Science Language Technical Team, 2004, Sedimentary materials:science language for their classification, description, and interpretation in digital geologic-map databases, Version 1.0 (12/18/2004): U.S. Geological Survey Open-File Report 2004-1451 appendix C, 595 p., accessed at http://pubs.usgs.gov/of/2004/1451/sltt/appendixC/, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/supraglacial_setting
- **Other Properties:**

[]{#subsurfacefluidreservoir}

####  Subsurface fluid reservoir
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is fluid that resides in fractures, intergranular
porosity or other open space in the solid earth.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/subsurfacefluidreservoir
- **Other Properties:**

[]{#aquifer}

#####  Aquifer
- **Child of**:
 [`Subsurface fluid reservoir`](#subsurfacefluidreservoir)
- A body of porous and permeable Earth Material containing
interstitial water that can move through the material.
- **Source:**
SESAR legacy localities, 
based on Neuendorf et al., 2005, Glossary of Geology, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/aquifer
- **Other Properties:**

[]{#waterbody}

####  Water body
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is the Earth's hydrosphere.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/waterbody
- **Other Properties:**

[]{#marinewaterbody}

#####  Marine water body
- **Child of**:
 [`Water body`](#waterbody)
- Sampled feature is the marine hydrosphere.
- **See Also**:
* [<http://purl.obolibrary.org/obo/ENVO_01000686>](http://purl.obolibrary.org/obo/ENVO_01000686)
- **Alternate labels:**
Marine environment
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/marinewaterbody
- **Other Properties:**

[]{#fiord}

######  Fjord
- **Child of**:
 [`Marine water body`](#marinewaterbody)
- A long and narrow sea inlet with high steeply sloped walled sides. A
fjord is a landform created during a period of glaciation.
- **Source:**
<http://purl.obolibrary.org/obo/ENVO_00000039>, 
IMLGS sampled feature, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/fiord
- **Other Properties:**

[]{#terrestrialwaterbody}

#####  Terrestrial water body
- **Child of**:
 [`Water body`](#waterbody)
- Sampled feature is terrestrial hydrosphere-- lake, other standing
water, or a flowing water body (river, stream..). Include saline water
in terrestrial evaporite environments.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/terrestrialwaterbody
- **Other Properties:**

[]{#lake}

######  Lake
- **Child of**:
 [`Terrestrial water body`](#terrestrialwaterbody)
 [`Lacustrine setting`](#lacustrine_setting)
- A body of water on the Earth's surface, localized in a basin or
interconnected basins surrounded by dry land.
- **Alternate labels:**
Pond
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake
- **Other Properties:**

[]{#lake_fresh_water}

#######  Fresh water lake
- **Child of**:
 [`Lake`](#lake)
- Natural lakes or human impounded fresh water resevoirs.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake_fresh_water
- **Other Properties:**

[]{#lake_saline}

#######  Saline lake
- **Child of**:
 [`Lake`](#lake)
-
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lake_saline
- **Other Properties:**

[]{#river_stream}

######  River or stream
- **Child of**:
 [`Terrestrial water body`](#terrestrialwaterbody)
- A body of fresh water flowing in a channel to the sea, a lake, or
another such flowing body of water.
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/river_stream
- **Other Properties:**

[]{#bay}

#####  Bay
- **Child of**:
 [`Water body`](#waterbody)
- An area of water bordered by land on three sides.
- **Source:**
Based on IMLGS sampled feature harbor or small bay
- **Concept URI:** https://w3id.org/sesar/sampledfeature/bay
- **Other Properties:**

[]{#bight}

#####  Bight
- **Child of**:
 [`Water body`](#waterbody)
- a concave bend or curvature in a coastline forming a very open bay
- **Source:**
Neuendorf et al., Glossary of Geology, 2005, 
SESAR legacy localities, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/bight
- **Other Properties:**

[]{#canal}

#####  Canal
- **Child of**:
 [`Active human occupation site`](#activehumanoccupationsite)
 [`Water body`](#waterbody)
- A human manufactured water channel to manage surface water resources
for irrigation, transportation, or human consumption.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/canal
- **Other Properties:**

[]{#continent}

####  Continent
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Sampled feature is on or within continental crust.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continent
- **Other Properties:**

[]{#continental_margin}

####  Continental Margin
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Boundary zone between continental crust and oceanic crust.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_margin
- **Other Properties:**

[]{#active_continental_margin}

#####  Active continental margin
- **Child of**:
 [`Continental Margin`](#continental_margin)
 [`Plate margin`](#plate_margin)
- A plate boundary between continental and oceanic crust that is a
zone of active faulting, i.e. a transform fault or subduction zone.
- **Concept URI:** https://w3id.org/sesar/sampledfeature/active_continental_margin
- **Other Properties:**

[]{#passive_continental_margin}

#####  Passive continental margin
- **Child of**:
 [`Continental Margin`](#continental_margin)
- Boundary of continental crust into oceanic crust of an oceanic basin
that is not a subduction zone or transform fault system. Generally is
rifted margin formed when ocean basin was initially formed.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/passive_continental_margin
- **Other Properties:**

[]{#geologic_structure}

####  Geologic structure
- **Child of**:
 [`Earth environment`](#earthenvironment)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/geologic_structure
- **Other Properties:**

[]{#ductile_shear_zone}

#####  Ductile shear zone
- **Child of**:
 [`Geologic structure`](#geologic_structure)
- Tabular or sheetlike and planar or curviplanar zones in which rocks
are more highly strained through crystal plastic processes than rocks
adjacent to the zone
- **Source:**
SESAR legacy localities, 
https://doi.org/10.1016/B978-0-12-816802-8.00002-0, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ductile_shear_zone
- **Other Properties:**

[]{#fault}

#####  Geologic fault
- **Child of**:
 [`Geologic structure`](#geologic_structure)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/fault
- **Other Properties:**

[]{#fault_scarp}

#####  Fault scarp
- **Child of**:
 [`Geologic structure`](#geologic_structure)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/fault_scarp
- **Other Properties:**

[]{#fold}

#####  Geologic fold
- **Child of**:
 [`Geologic structure`](#geologic_structure)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/fold
- **Other Properties:**

[]{#impact_structure}

#####  Impact structure
- **Child of**:
 [`Geologic structure`](#geologic_structure)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/impact_structure
- **Other Properties:**

[]{#igneous_system}

####  Igneous system
- **Child of**:
 [`Earth environment`](#earthenvironment)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/igneous_system
- **Other Properties:**

[]{#hypabyssal_setting}

#####  Hypabyssal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Igneous system`](#igneous_system)
- Igneous environment close to the Earth's surface, characterized by
more rapid cooling than plutonic setting to produce generally fine-
grained intrusive igneous rock that is commonly associated with co-
magmatic volcanic rocks.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hypabyssal_setting
- **Other Properties:**

[]{#intrusive_igneous_complex}

#####  Intrusive igneous complex
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Igneous system`](#igneous_system)
- Features related to igneous activity wholly within the Earth,
characterized by slow cooling to produce generally medium to coarse-
grained intrusive igneous rocks.
- **Source:**
SESAR legacy data
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intrusive_igneous_complex
- **Other Properties:**

[]{#volcanic_setting}

#####  Volcanic Setting
- **Child of**:
 [`Igneous system`](#igneous_system)
- Features related to the eruption of lava near, at, or above the
earth surface. Might include atmospheric products of volcanic
eruption, in terrestrial, lacustrine, or marine environments, related
hypabyssal intrusions or hydrothermal systems.
- **Source:**
sessf:sfvocabulary
- **Concept URI:** https://w3id.org/sesar/sampledfeature/volcanic_setting
- **Other Properties:**

[]{#inactive_spreading_center}

######  Inactive spreading center
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Submarine ridge`](#submarine_ridge)
 [`Volcanic Setting`](#volcanic_setting)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Alternate labels:**
Aseismic ocean ridge
- **Source:**
IMLGS sampled feature, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/inactive_spreading_center
- **Other Properties:**

[]{#plate_spreading_center}

######  Plate spreading center
- **Child of**:
 [`Extended terrane`](#extended_terrane)
 [`Volcanic Setting`](#volcanic_setting)
- Tectonic setting where new oceanic crust is being or has been formed
at a divergent plate boundary.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/plate_spreading_center
- **Other Properties:**

[]{#seamount}

######  Seamount
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Ocean highland`](#ocean_highland)
 [`Volcanic Setting`](#volcanic_setting)
- Setting that consists of a conical mountain on the ocean floor
(guyot). Typically characterized by active volcanism, pelagic
sedimentation. If the mountain is high enough to reach the photic
zone, carbonate production may result in reef building to produce a
carbonate platform or atoll setting.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/seamount
- **Other Properties:**

[]{#volcanic_arc}

######  Volcanic arc
- **Child of**:
 [`Plate margin`](#plate_margin)
 [`Volcanic Setting`](#volcanic_setting)
- A generally curvillinear belt of volcanoes above a subduction zone.
- **Source:**
1-GE WP3, Neuendorf et al.(2005), p. 710, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/volcanic_arc
- **Other Properties:**

[]{#continental_volcanic_arc}

#######  Continental volcanic arc
- **Child of**:
 [`Volcanic arc`](#volcanic_arc)
- a linear chain of volcanos formed above a subduction zone with ocean
crust subducting beneath a continent
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_volcanic_arc
- **Other Properties:**

[]{#island_arc}

#######  Island arc
- **Child of**:
 [`Volcanic arc`](#volcanic_arc)
- A volcanic arc related to an intraoceanic subduction zone,
consisting of a chain of islands formed by volcanos above a subduction
zone.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/island_arc
- **Other Properties:**

[]{#volcano}

######  Volcano
- **Child of**:
 [`Earth surface`](#earthsurface)
 [`Volcanic Setting`](#volcanic_setting)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/volcano
- **Other Properties:**

[]{#sedimentary_basin}

####  Sedimentary basin
- **Child of**:
 [`Earth environment`](#earthenvironment)
- A region that accumulates sedimentary (and possibly subordinate
interbedded volcanic) rocks, typically bounded by geologic structures.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/sedimentary_basin
- **Other Properties:**

[]{#foreland_basin}

#####  Foreland basin
- **Child of**:
 [`Foreland setting`](#foreland_setting)
 [`Sedimentary basin`](#sedimentary_basin)
- an elongate region of potential sediment accommodation that forms on
continental crust between a contractional orogenic belt and the
adjacent craton, mainly in response to geodynamic processes related to
subduction and the resulting peripheral or retroarc fold-thrust belt.
- **Source:**
SESAR legacy localities, 
https://doi.org/10.1046/j.1365-2117.1996.01491.x, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_basin
- **Other Properties:**

[]{#tectonic_setting}

####  Tectonically defined setting
- **Child of**:
 [`Earth environment`](#earthenvironment)
- Setting defined by relationships to tectonic plates on or in the
Earth.
- **Source:**
<http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment>
- **Concept URI:** https://w3id.org/sesar/sampledfeature/tectonic_setting
- **Other Properties:**

[]{#back_arc_setting}

#####  Back arc setting
- **Child of**:
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting adjacent to a volcanic arc formed above a
subduction zone. The back arc setting is on the opposite side of the
volcanic arc from the trench at which oceanic crust is consumed in a
subduction zone. Back arc setting includes terrane that is affected by
plate margin and arc-related processes.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/back_arc_setting
- **Other Properties:**

[]{#collisional_setting}

#####  Collisional setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting in which two continental crustal plates impact and
are sutured together after intervening oceanic crust is entirely
consumed at a subduction zone separating the plates. Such collision
typically involves major mountain forming events, exemplified by the
modern Alpine and Himalayan mountain chains.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/collisional_setting
- **Other Properties:**

[]{#crust}

#####  Crustal setting
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Tectonically defined setting`](#tectonic_setting)
- The outermost layer or shell of the Earth, defined according to
various criteria, including seismic velocity, density and composition,
that part of the Earth above the Mohorovicic discontinuity, made up of
the sial and the sima.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/crust
- **Other Properties:**

[]{#continental_crust}

######  Continental crust
- **Child of**:
 [`Crustal setting`](#crust)
- That type of the Earth's crust which underlies the continents and
the continental shelves, it is equivalent to the sial and continental
sima and ranges in thickness from about 25 km to more than 70 km under
mountain ranges, averaging ~40 km. The density of the continental
crust averages ~2.8 g/cm3 and is ~2.7 g.cm3 in the upper layer. The
velocities of compressional seismic waves through it average ~6.5 km/s
and are less than ~7.0 km/sec.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_crust
- **Other Properties:**

[]{#collisional_setting}

#######  Collisional setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting in which two continental crustal plates impact and
are sutured together after intervening oceanic crust is entirely
consumed at a subduction zone separating the plates. Such collision
typically involves major mountain forming events, exemplified by the
modern Alpine and Himalayan mountain chains.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/collisional_setting
- **Other Properties:**

[]{#foreland_setting}

#######  Foreland setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- The exterior area of an orogenic belt where deformation occurs
without significant metamorphism. Generally the foreland is closer to
the continental interior than other portions of the orogenic belt are.
- **Source:**
1-GE WP3, Neuendorf et al.(2005), p. 250, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_setting
- **Other Properties:**

[]{#foreland_basin}

########  Foreland basin
- **Child of**:
 [`Foreland setting`](#foreland_setting)
 [`Sedimentary basin`](#sedimentary_basin)
- an elongate region of potential sediment accommodation that forms on
continental crust between a contractional orogenic belt and the
adjacent craton, mainly in response to geodynamic processes related to
subduction and the resulting peripheral or retroarc fold-thrust belt.
- **Source:**
SESAR legacy localities, 
https://doi.org/10.1046/j.1365-2117.1996.01491.x, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_basin
- **Other Properties:**

[]{#foreland_fold_thrust_belt}

########  Foreland fold and thrust belt
- **Child of**:
 [`Foreland setting`](#foreland_setting)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_fold_thrust_belt
- **Other Properties:**

[]{#hinterland_setting}

#######  Hinterland tectonic setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting in the internal part of an orogenic belt,
characterized by plastic deformation of rocks accompanied by
significant metamorphism, typically involving crystalline basement
rocks. Typically denotes the most structurally thickened part of an
orogenic belt, between a magmatic arc or collision zone and a more
'external' foreland setting.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hinterland_setting
- **Other Properties:**

[]{#lower_continental_crust}

#######  Lower continental crust
- **Child of**:
 [`Continental crust`](#continental_crust)
- Continental crustal setting characterized by upper amphibolite to
granulite facies metamorphism, insitu melting, residual anhydrous
metamorphic rocks, and ductile flow of rock bodies.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_continental_crust
- **Other Properties:**

[]{#middle_continental_crust}

#######  Middle continental crust
- **Child of**:
 [`Continental crust`](#continental_crust)
- Continental crustal setting characterized by greenschist to upper
amphibolite facies metamorphism, plutonic igneous rocks, and ductile
deformation.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/middle_continental_crust
- **Other Properties:**

[]{#upper_continental_crust}

#######  Upper continental crust
- **Child of**:
 [`Continental crust`](#continental_crust)
- Continental crustal setting dominated by non metamorphosed to low
greenschist facies metamorphic rocks, and brittle deformation.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_continental_crust
- **Other Properties:**

[]{#ocean_crust}

######  Ocean crust
- **Child of**:
 [`Crustal setting`](#crust)
- That type of the Earth's crust which underlies the ocean basins. The
oceanic crust is 5-10 km thick, it has a density of 2.9 g/cm3, and
compressional seismic-wave velocities travelling through it at 4-7.2
km/sec. Setting in crust produced by submarine volcanism at a mid
ocean ridge.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/ocean_crust
- **Other Properties:**

[]{#lower_oceanic_crust}

#######  Lower oceanic crust
- **Child of**:
 [`Ocean crust`](#ocean_crust)
- Setting characterized by dominantly intrusive mafic rocks, with
sheeted dike complexes in upper part and gabbroic to ultramafic
intrusive or metamorphic rocks in lower part.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_oceanic_crust
- **Other Properties:**

[]{#upper_ocean_crust}

#######  Upper ocean crust
- **Child of**:
 [`Ocean crust`](#ocean_crust)
- Oceanic crustal setting dominated by extrusive rocks, abyssal
oceanic sediment, with increasing mafic intrusive rock in lower part.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_ocean_crust
- **Other Properties:**

[]{#transitional_crust}

######  Transitional crust
- **Child of**:
 [`Crustal setting`](#crust)
- Crust formed in the transition zone between continental and oceanic
crust, during the history of continental rifting that culminates in
the formation of a new ocean.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/transitional_crust
- **Other Properties:**

[]{#extended_terrane}

#####  Extended terrane
- **Child of**:
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting characterized by extension of the upper crust
manifested by formation of rift valleys or basin and range
physiography, with arrays of low to high angle normal faults. Modern
examples include the North Sea, East Africa, and the Basin and Range
of the North American Cordillera. Typically applied in continental
crustal settings.
- **Source:**
This vocabulary, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/extended_terrane
- **Other Properties:**

[]{#continental_rift_setting}

######  Continental rift
- **Child of**:
 [`Extended terrane`](#extended_terrane)
- Extended terrane in a zone of continental breakup, may include
incipient oceanic crust. Examples include Red Sea, East Africa Rift,
Salton Trough
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_rift_setting
- **Other Properties:**

[]{#plate_spreading_center}

######  Plate spreading center
- **Child of**:
 [`Extended terrane`](#extended_terrane)
 [`Volcanic Setting`](#volcanic_setting)
- Tectonic setting where new oceanic crust is being or has been formed
at a divergent plate boundary.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/plate_spreading_center
- **Other Properties:**

[]{#rift_zone}

######  Rift zone
- **Child of**:
 [`Extended terrane`](#extended_terrane)
- A regional extended terrane in a zone of plate or plate-fragment
divergence
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/rift_zone
- **Other Properties:**

[]{#foreland_setting}

#####  Foreland setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- The exterior area of an orogenic belt where deformation occurs
without significant metamorphism. Generally the foreland is closer to
the continental interior than other portions of the orogenic belt are.
- **Source:**
1-GE WP3, Neuendorf et al.(2005), p. 250, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_setting
- **Other Properties:**

[]{#foreland_basin}

######  Foreland basin
- **Child of**:
 [`Foreland setting`](#foreland_setting)
 [`Sedimentary basin`](#sedimentary_basin)
- an elongate region of potential sediment accommodation that forms on
continental crust between a contractional orogenic belt and the
adjacent craton, mainly in response to geodynamic processes related to
subduction and the resulting peripheral or retroarc fold-thrust belt.
- **Source:**
SESAR legacy localities, 
https://doi.org/10.1046/j.1365-2117.1996.01491.x, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_basin
- **Other Properties:**

[]{#foreland_fold_thrust_belt}

######  Foreland fold and thrust belt
- **Child of**:
 [`Foreland setting`](#foreland_setting)
-
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/foreland_fold_thrust_belt
- **Other Properties:**

[]{#hinterland_setting}

#####  Hinterland tectonic setting
- **Child of**:
 [`Continental crust`](#continental_crust)
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting in the internal part of an orogenic belt,
characterized by plastic deformation of rocks accompanied by
significant metamorphism, typically involving crystalline basement
rocks. Typically denotes the most structurally thickened part of an
orogenic belt, between a magmatic arc or collision zone and a more
'external' foreland setting.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hinterland_setting
- **Other Properties:**

[]{#hot_spot}

#####  Hot spot
- **Child of**:
 [`Tectonically defined setting`](#tectonic_setting)
- Setting in a zone of high heat flow from the mantle. Typically
identified in intraplate settings, but hot spot may also interact with
active plate margins (Iceland...). Includes surface manifestations
like volcanic center, but also includes crust and mantle
manifestations as well.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/hot_spot
- **Other Properties:**

[]{#intraplate_tectonic_setting}

#####  Intraplate tectonic setting
- **Child of**:
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonically stable setting far from any active plate margins.
- **Source:**
This vocabulary, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/intraplate_tectonic_setting
- **Other Properties:**

[]{#inactive_spreading_center}

######  Inactive spreading center
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Submarine ridge`](#submarine_ridge)
 [`Volcanic Setting`](#volcanic_setting)
- Setting on oceanic crust formed at a spreading center that has been
abandoned.
- **Alternate labels:**
Aseismic ocean ridge
- **Source:**
IMLGS sampled feature, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/inactive_spreading_center
- **Other Properties:**

[]{#seamount}

######  Seamount
- **Child of**:
 [`Intraplate tectonic setting`](#intraplate_tectonic_setting)
 [`Ocean highland`](#ocean_highland)
 [`Volcanic Setting`](#volcanic_setting)
- Setting that consists of a conical mountain on the ocean floor
(guyot). Typically characterized by active volcanism, pelagic
sedimentation. If the mountain is high enough to reach the photic
zone, carbonate production may result in reef building to produce a
carbonate platform or atoll setting.
- **Source:**
Reading 1978, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/seamount
- **Other Properties:**

[]{#mantle}

#####  Mantle
- **Child of**:
 [`Earth interior`](#earthinterior)
 [`Tectonically defined setting`](#tectonic_setting)
- The zone of the Earth below the crust and above the core, which is
divided into the upper mantle and the lower mantle, with a transition
zone separating them.
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/mantle
- **Other Properties:**

[]{#lower_mantle}

######  Lower mantle
- **Child of**:
 [`Mantle`](#mantle)
- That part of the mantle that lies below a depth of about 660 km.
With increasing depth, density increases from ~4.4 g/cm3-to ~5.6
g/cm3, and velocity of compressional seismic waves increases from
~10.7 km/s to ~13.7 km/s (Dziewonski and Anderson, 1981).
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/lower_mantle
- **Other Properties:**

[]{#upper_mantle}

######  Upper mantle
- **Child of**:
 [`Mantle`](#mantle)
- That part of the mantle which lies above a depth of about 660 km and
has a density of 3.4 g/cm3 to 4.0 g/cm3 with increasing depth.
Similarly, P-wave velocity increases from about 8 to 11 km/sec with
depth and S wave velocity increases from about 4.5 to 6 km/sec with
depth. It is presumed to be peridotitic in composition. It includes
the subcrustal lithosphere the asthenosphere and the transition zone,
- **Source:**
Neuendorf et al., 2005, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/upper_mantle
- **Other Properties:**

[]{#plate_margin}

#####  Plate margin
- **Child of**:
 [`Tectonically defined setting`](#tectonic_setting)
- Tectonic setting at the boundary between two tectonic plates.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/plate_margin
- **Other Properties:**

[]{#active_continental_margin}

######  Active continental margin
- **Child of**:
 [`Continental Margin`](#continental_margin)
 [`Plate margin`](#plate_margin)
- A plate boundary between continental and oceanic crust that is a
zone of active faulting, i.e. a transform fault or subduction zone.
- **Concept URI:** https://w3id.org/sesar/sampledfeature/active_continental_margin
- **Other Properties:**

[]{#forearc_setting}

######  Forearc setting
- **Child of**:
 [`Plate margin`](#plate_margin)
- Tectonic setting between a subduction-related trench and a volcanic
arc
- **Source:**
1-GE WP3, Neuendorf et al.(2005), p. 249, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/forearc_setting
- **Other Properties:**

[]{#fracture_zone}

######  Fracture zone
- **Child of**:
 [`Plate margin`](#plate_margin)
- a tranform fault offsetting an oceanic spreading center
- **Source:**
IMLGS sampled feature
- **Concept URI:** https://w3id.org/sesar/sampledfeature/fracture_zone
- **Other Properties:**

[]{#subduction_zone}

######  Subduction zone
- **Child of**:
 [`Plate margin`](#plate_margin)
- Tectonic setting at which a tectonic plate, usually oceanic, is
moving down into the mantle beneath another overriding plate.
- **Source:**
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment
- **Concept URI:** https://w3id.org/sesar/sampledfeature/subduction_zone
- **Other Properties:**

[]{#transform_plate_boundary}

######  Transform plate boundary
- **Child of**:
 [`Plate margin`](#plate_margin)
- Plate boundary at which the adjacent plates are moving laterally
relative to each other.
- **Source:**
This vocabulary, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/transform_plate_boundary
- **Other Properties:**

[]{#volcanic_arc}

######  Volcanic arc
- **Child of**:
 [`Plate margin`](#plate_margin)
 [`Volcanic Setting`](#volcanic_setting)
- A generally curvillinear belt of volcanoes above a subduction zone.
- **Source:**
1-GE WP3, Neuendorf et al.(2005), p. 710, 
http://resource.geosciml.org/classifierscheme/cgi/2016.01/eventenvironment, 
- **Concept URI:** https://w3id.org/sesar/sampledfeature/volcanic_arc
- **Other Properties:**

[]{#continental_volcanic_arc}

#######  Continental volcanic arc
- **Child of**:
 [`Volcanic arc`](#volcanic_arc)
- a linear chain of volcanos formed above a subduction zone with ocean
crust subducting beneath a continent
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/continental_volcanic_arc
- **Other Properties:**

[]{#island_arc}

#######  Island arc
- **Child of**:
 [`Volcanic arc`](#volcanic_arc)
- A volcanic arc related to an intraoceanic subduction zone,
consisting of a chain of islands formed by volcanos above a subduction
zone.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/island_arc
- **Other Properties:**

[]{#triple_junction}

#####  Plate triple junction
- **Child of**:
 [`Tectonically defined setting`](#tectonic_setting)
- a setting characterized by interaction of three tectonic plates.
- **Source:**
SESAR legacy localities
- **Concept URI:** https://w3id.org/sesar/sampledfeature/triple_junction
- **Other Properties:**

[]{#extraterrestrialenvironment}

###  Extraterrestrial environment
- **Child of**:
 [`Any sampled feature`](#anysampledfeature)
- Sampled feature is the environment outside of solid earth,
hydrosphere, or atmosphere.
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/extraterrestrialenvironment
- **Other Properties:**


