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

[]{#MaterialSamplecollectionmethods}

# **Concept scheme:** Material Sample collection methods

Vocabulary last modified:  2024-09-12

subtitle: 
  Material sample collection methods focused on methods found in SESAR data (2024-08-31 dump), harmonized with CGI GTWG sampling methods draft, Geoscience Australia sampling methods, and SeaDataNet Sample Collection vocabulary.  The SeaDataNet  vocabulary is nominally about instruments, but many of the concepts implicitly denote methods.

Namespace: 
[`https://w3id.org/sesar/samplingmethods/0.1/samplingmethods`](https://w3id.org/sesar/samplingmethods/0.1/samplingmethods)

**History**


- [Sampling method](#sm100)
    - [Airfall dust collection](#airfall_dust_collector)
    - [Drilling](#drilling)
        - [Auger](#auger)
            - [Hand auger](#ses217)
        - [Core drilling](#core_drilling_unspecified)
            - [Air cooled core drilling](#core_air)
            - [Core catcher](#core_catcher)
            - [Core cutter](#core_cutter)
            - [Diamond bit drill coring](#core_diamond)
                - [core conventional](#core_conventional)
            - [Coring from submersible](#core_rov)
            - [Rotary sidewall coring](#sidewall_core_mechanical)
            - [Hand auger coring](#sm007)
        - [Percussion drilling](#percussion_drilling)
            - [cable tool drilling](#cable_tool_drilling)
            - [RAB drilling](#rab_drilling)
            - [Rotary hammer drilling](#rotary_hammer_drilling)
        - [Rotary drilling](#rotary_drilling)
            - [reverse circulation drilling](#reverse_circulation_drilling)
        - [Sidewall coring](#sidewall_core)
            - [Percussion sidewall coring](#sidewall_core_bullet)
            - [Rotary sidewall coring](#sidewall_core_mechanical)
    - [Field mapping survey](#field_mapping_observation)
    - [Filtration residue sampling](#filtration)
        - [Filtered dust collector](#filtered_dust_collector)
        - [Cartridge filter residue](#ses207)
        - [Suspended sediment separate](#sm021)
    - [Chain saw](#ses208)
    - [Subaqueous organism trap](#ses213)
    - [Micropillar Sampling](#ses224)
    - [Pulverize](#ses226)
    - [Scoop](#ses227)
    - [Settlement Plate](#ses228)
    - [Shaker table](#ses229)
    - [Suction Sampling](#ses233)
        - [Syringe sampling](#ses212)
        - [Slurp sampling](#slurpsampling)
    - [Core preserved with wax](#ses234)
    - [Sediment trap](#sm018)
    - [Coring](#sm041)
        - [Core drilling](#core_drilling_unspecified)
            - [Air cooled core drilling](#core_air)
            - [Core catcher](#core_catcher)
            - [Core cutter](#core_cutter)
            - [Diamond bit drill coring](#core_diamond)
                - [core conventional](#core_conventional)
            - [Coring from submersible](#core_rov)
            - [Rotary sidewall coring](#sidewall_core_mechanical)
            - [Hand auger coring](#sm007)
        - [Sidewall coring](#sidewall_core)
            - [Percussion sidewall coring](#sidewall_core_bullet)
            - [Rotary sidewall coring](#sidewall_core_mechanical)
        - [Soft material coring](#sm005)
            - [Geoprobe coring](#core_geoprobe)
            - [core Mackereth](#core_mackereth)
            - [Push coring](#core_push)
                - [Hand held coring](#sm027)
            - [core spike](#core_spike)
            - [Free fall coring](#freefallcoring)
            - [Phleger coring](#phlegercoring)
            - [Trigger coring](#ses220)
            - [Kasten coring](#ses221)
            - [Slide hammer coring](#ses232)
            - [Box coring](#sm025)
            - [Gravity coring](#sm026)
            - [Multi coring](#sm028)
            - [Piston coring](#sm029)
            - [Probe core](#sm030)
            - [Vibrator coring](#sm031)
                - [Sonic coring](#core_sonic)
            - [Wax coring](#waxcoring)
    - [Fluid sampling](#sm043)
        - [Borehole fluid sampling](#borehole_fluid_sampling)
            - [Airlift water sampling](#airlift)
            - [Artesian flow sampling](#artesian_flow)
            - [Borehole bailer sampling](#bailer)
                - [Point souce bailer sampling](#in_situ_grab_sampler)
            - [Borehole drill stem test](#borehole_dst_test)
            - [Borehole production test](#borehole_prod_test)
            - [Borehole wireline formation test](#borehole_wft_test)
            - [Borehole water pumping](#boreholewaterpump)
            - [Liquid-gas separation](#liquid-gas_separation)
        - [Pump sampling](#pumpsampling)
        - [Ghostbuster fluid sampler](#ses215)
        - [Gas sampling](#sm013)
            - [Gas tight bottle sampling](#ses214)
            - [Evacuated bottle gas sampling](#sm011)
                - [Inverted funnel to evacuated bottle gas collection](#sm008)
            - [Flow through bottle gas sampling](#sm012)
                - [Inverted funnel to flow through bottle gas collection](#sm009)
        - [Water sampling](#sm014)
            - [Airlift water sampling](#airlift)
            - [Artesian flow sampling](#artesian_flow)
            - [Borehole bailer sampling](#bailer)
                - [Point souce bailer sampling](#in_situ_grab_sampler)
            - [Borehole water pumping](#boreholewaterpump)
            - [Container sampling](#bottlesampling)
                - [Niskin bottle](#ses225)
            - [core press](#core_press)
            - [Lysimeter water collection](#lysimeter)
            - [Rain gauge](#rain_gauge)
            - [Niskin bottle](#ses225)
            - [Composite water sampling](#sm010)
                - [Composite water sampling- preserve with reagent](#sm001)
                    - [Composite water sampling- filter and preserve with reagent](#sm003)
                - [Composite water sampling-filter](#sm002)
                    - [Composite water sampling- filter and preserve with reagent](#sm003)
            - [Water sampling- preserve with reagent](#sm022)
                - [Water sampling-filter and preserve with reagent](#sm024)
            - [Water sampling-filter](#sm023)
                - [Cartridge filter filtrate](#ses206)
                - [Water sampling-filter and preserve with reagent](#sm024)
            - [Vacuum pore water sampling](#vacuumporewatersampling)
    - [Other sampling procedure](#sm044)
    - [Processed separation](#sm045)
        - [Chemical separation](#chemicalseparation)
        - [Density separation](#densityseparation)
            - [Panned concentrate sampling](#sm019)
        - [Grain size separation](#grainsize_separation)
            - [Sieved aggregate](#ses231)
        - [Microanalytic sampling](#microanalyticsampling)
        - [Split processed sample](#sm020)
        - [Suspended sediment separate](#sm021)
        - [Splitting from bulk sample](#sm046)
    - [Surface grab](#sm047)
        - [Backhoe](#ses202)
        - [Mechanical grab from surface](#ses222)
        - [Blasting](#sm032)
        - [Manual grab](#sm035)
            - [Human grab from surface](#ses218)
                - [Manual surface grab](#sm017)
                - [Lag sample](#sm040)
            - [Collected from outcrop](#sm016)
                - [Chip sampling](#ses210)
                - [Hammer from outcrop](#ses216)
                - [Channel sampling](#sm015)
            - [Grab from trench or pit](#sm034)
        - [Stream sediment composite](#sm037)
        - [Stream sediment single grab](#sm038)
        - [Water body bottom grab](#sm039)
            - [Smith Mcintyre grab sampling](#grab_smith_mcintyre)
            - [Submersible grab](#ses201)
            - [Campbell grab sampling](#ses205)
            - [Sediment grab](#sm036)
                - [grab Eckman](#grab_eckman)
                - [grab Shipek](#grab_shipek)
                - [Van Veen grab sampling](#grab_van_veen)
        - [Subaerial surface sampling](#surface_material_sampling)
            - [Outcrop sampling](#outcrop_sampling)
            - [Pit or trench sampling](#pit_or_trench_sampling)
            - [Shovel](#ses230)
            - [Undergound mine sampling](#undergound_mine_sampling)
    - [Sediment water incubation sampling](#sm200)
        - [bottle incubation](#bottle_incubation)
            - [bottle incubation dark](#bottle_incubation_dark)
            - [bottle incubation light](#bottle_incubation_light)
        - [Chamber incubation](#chamber_incubation)
            - [chamber incubation dark](#chamber_incubation_dark)
            - [chamber incubation light](#chamber_incubation_light)
        - [core incubation dark](#core_incubation_dark)
        - [core incubation light](#core_incubation_light)
    - [unknown](#unknown)
    - [Water body survey sampling](#waterbodysampling)
        - [Benthic sled sampling](#epibenthic_sled)
        - [Dredge sampling](#sm033)
            - [dredge diamantina](#diamantina_dredge)
            - [dredge pipe](#pipe_dredge)
            - [Chain bag dredge](#sm006)
        - [Water body bottom grab](#sm039)
            - [Smith Mcintyre grab sampling](#grab_smith_mcintyre)
            - [Submersible grab](#ses201)
            - [Campbell grab sampling](#ses205)
            - [Sediment grab](#sm036)
                - [grab Eckman](#grab_eckman)
                - [grab Shipek](#grab_shipek)
                - [Van Veen grab sampling](#grab_van_veen)
        - [Trawl sampling](#trawlsampling)
            - [Benthic trawl](#benthic_trawl)
            - [Agassiz trawl](#ses200)
            - [Beam trawl](#ses203)
            - [Blake trawl](#ses204)
            - [Menzie trawl](#ses223)
        - [Water body water sampling](#waterbodywatersampling)
            - [Borehole water pumping](#boreholewaterpump)
            - [Container sampling](#bottlesampling)
                - [Niskin bottle](#ses225)
            - [Composite water sampling](#sm010)
                - [Composite water sampling- preserve with reagent](#sm001)
                    - [Composite water sampling- filter and preserve with reagent](#sm003)
                - [Composite water sampling-filter](#sm002)
                    - [Composite water sampling- filter and preserve with reagent](#sm003)
            - [Water sampling- preserve with reagent](#sm022)
                - [Water sampling-filter and preserve with reagent](#sm024)
            - [Water sampling-filter](#sm023)
                - [Cartridge filter filtrate](#ses206)
                - [Water sampling-filter and preserve with reagent](#sm024)

**Concepts**

[]{#sm100}

##  Sampling method
- Top concept, for all methods used to collect material samples
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm100
- **Other Properties:**

[]{#airfall_dust_collector}

###  Airfall dust collection
- **Child of**:
 [`Sampling method`](#sm100)
- Sample of fine-grained solid material that is passively collected by
airfall from the atmosphere.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/airfall_dust_collector
- **Other Properties:**

[]{#drilling}

###  Drilling
- **Child of**:
 [`Sampling method`](#sm100)
- Sampling by a hole drilled into the Earth by any method
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/drilling
- **Other Properties:**

[]{#auger}

####  Auger
- **Child of**:
 [`Drilling`](#drilling)
- Specimens collected by hand or mechanical auger which enable samples
to be taken at intervals down profile. For example regolith, soil or
sediment.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/auger
- **Other Properties:**

[]{#ses217}

#####  Hand auger
- **Child of**:
 [`Auger`](#auger)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses217
- **Other Properties:**

[]{#core_drilling_unspecified}

####  Core drilling
- **Child of**:
 [`Drilling`](#drilling)
 [`Coring`](#sm041)
- Sampling of a core of earth material by an unspecified drilling
method
- **Source:**
Geoscience Australia, 
SESAR collection method, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_drilling_unspecified
- **Other Properties:**

[]{#core_air}

#####  Air cooled core drilling
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- Rock or sediment core derived from a dry, air-cooled diamond
drilling method.
- **Alternate labels:**
core air
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_air
- **Other Properties:**

[]{#core_catcher}

#####  Core catcher
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- A method by which a specimen of sediment is collected from the end
of the core in the core catcher. The core catcher has curved finger-
like projections that extend down to the lowest part of the core
liner. The core catcher helps keep the sediment in the core liner when
the core is being removed from the surface.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_catcher
- **Other Properties:**

[]{#core_cutter}

#####  Core cutter
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- A method by which a specimen of sediment is collected from the
lowest part of a coring assembly at the core cutter. The core cutter
has sharp edges which cut and shape the sediment entering the core
liner as the corer goes into the sediment.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_cutter
- **Other Properties:**

[]{#core_diamond}

#####  Diamond bit drill coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- Rock or sediment core drilling using a liquid-cooled, diamond or
tungsten carbide bit.
- **Alternate labels:**
core diamond
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_diamond
- **Other Properties:**

[]{#core_conventional}

######  core conventional
- **Child of**:
 [`Diamond bit drill coring`](#core_diamond)
- Core drilling using diamond or tungsten carbide bit using a core
barrel with fibreglass inner sleeves. Used in the oil industry.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_conventional
- **Other Properties:**

[]{#core_rov}

#####  Coring from submersible
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- A core produced by a drill mounted on a submersible vehicle, ROV,
HOV.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_rov
- **Other Properties:**

[]{#sidewall_core_mechanical}

#####  Rotary sidewall coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
 [`Sidewall coring`](#sidewall_core)
- Mechanical tools use hollow rotary drills to cut and then pull out
core plugs. Up to 75 plugs can be recovered on one run. With full
recovery, cores from typical percussion tools are 1 in. [2.5 cm] in
diameter by 1 3/4 in. [4.4 cm] long, while those from mechanical tools
are 0.91 in. [2.3 cm] in diameter by 2 in. [5 cm] long. The latter are
also known as rotary sidewall cores.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core_mechanical
- **Other Properties:**

[]{#sm007}

#####  Hand auger coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- core extracted from sediment or soil by a hand rotated tool with a
special bit that extracts short segments of cored sediment; many
variations in design.
- **Source:**
this vocabulary; http://www.oakenviro.com/pdfs/Dutch%20Auger%20equipment%20options%20-%20Eijkelkamp.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm007
- **Other Properties:**

[]{#percussion_drilling}

####  Percussion drilling
- **Child of**:
 [`Drilling`](#drilling)
- Rock or sediment chips or fragments derived from a percussion
(hammer) method. Include pneumatic drilling
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/percussion_drilling
- **Other Properties:**

[]{#cable_tool_drilling}

#####  cable tool drilling
- **Child of**:
 [`Percussion drilling`](#percussion_drilling)
- A percussion drilling method that uses a heavy drilling tool that is
raised and lowered with enough force to pulverise the rock, with the
debris removed by a bailer.
- **Source:**
National Groundwater Information System (NGIS)
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/cable_tool_drilling
- **Other Properties:**

[]{#rab_drilling}

#####  RAB drilling
- **Child of**:
 [`Percussion drilling`](#percussion_drilling)
- RAB, rotary air blast, or Down-the-hole drilling. Rock or sediment
chips or fragments are derived from a percussion drilling method where
the cuttings are blown up the outside of the rods and collected at
surface, using air or a combination of air and foam lift the cuttings.
- **Alternate labels:**
rotary air blast drilling
- **Source:**
http://www.foragefte.com; http://www.masterdrilling.com
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/rab_drilling
- **Other Properties:**

[]{#rotary_hammer_drilling}

#####  Rotary hammer drilling
- **Child of**:
 [`Percussion drilling`](#percussion_drilling)
- A percussion drilling method using a cutting tool powered by
compressed air that creates a rapid percussion effect coupled with
rotary action to drill hard rocks.
- **Alternate labels:**
hammer drilling, 
jack hammer drilling, 
pneumatic drilling, 
- **Source:**
National Groundwater Information System (NGIS)
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/rotary_hammer_drilling
- **Other Properties:**

[]{#rotary_drilling}

####  Rotary drilling
- **Child of**:
 [`Drilling`](#drilling)
- A drilling method using a drill stem equipped with a bit that is
rotated to cut and grind the rock with a fluid pumped down the stem to
force cuttings up through the annular space between the stem and the
wall of the hole
- **Source:**
National Groundwater Information System (NGIS)
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/rotary_drilling
- **Other Properties:**

[]{#reverse_circulation_drilling}

#####  reverse circulation drilling
- **Child of**:
 [`Rotary drilling`](#rotary_drilling)
- A drilling technique similar to rotary drilling except that drilling
fluid flow down the annular space between the drilling stem and the
wall of the hole forcing cuttings up through the inside of the drill
stem .
- **Alternate labels:**
RC
- **Source:**
National Groundwater Information System (NGIS)
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/reverse_circulation_drilling
- **Other Properties:**

[]{#sidewall_core}

####  Sidewall coring
- **Child of**:
 [`Drilling`](#drilling)
 [`Coring`](#sm041)
- A method to extract core or plug from the sidewall of a borehole.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core
- **Other Properties:**

[]{#sidewall_core_bullet}

#####  Percussion sidewall coring
- **Child of**:
 [`Sidewall coring`](#sidewall_core)
- Percussion cores are taken by firing hollow bullets into the
formation. The bullets are attached to the tool by fasteners, and are
retrieved, along with the core inside, by pulling up the tool and the
fasteners. Percussion coring tools typically hold 20 to 30 bullets,
but two or three tools can be combined on one run in the hole.
- **Alternate labels:**
sidewall core, bullet
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core_bullet
- **Other Properties:**

[]{#sidewall_core_mechanical}

#####  Rotary sidewall coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
 [`Sidewall coring`](#sidewall_core)
- Mechanical tools use hollow rotary drills to cut and then pull out
core plugs. Up to 75 plugs can be recovered on one run. With full
recovery, cores from typical percussion tools are 1 in. [2.5 cm] in
diameter by 1 3/4 in. [4.4 cm] long, while those from mechanical tools
are 0.91 in. [2.3 cm] in diameter by 2 in. [5 cm] long. The latter are
also known as rotary sidewall cores.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core_mechanical
- **Other Properties:**

[]{#field_mapping_observation}

###  Field mapping survey
- **Child of**:
 [`Sampling method`](#sm100)
- A mapping survey undertaken in a land environment. May include
observations and/or sampling.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/field_mapping_observation
- **Other Properties:**

[]{#filtration}

###  Filtration residue sampling
- **Child of**:
 [`Sampling method`](#sm100)
- Separation of undissolved sediment and biological particles
collected from a water column by filtration. For total dissolved
solids measurements the sample is filtered through a glass fibre
filter under controlled conditions.  The type of filter is dependent
on the method used and the purpose of the determination.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/filtration
- **Other Properties:**

[]{#filtered_dust_collector}

####  Filtered dust collector
- **Child of**:
 [`Filtration residue sampling`](#filtration)
- Sample of fine-grained solid material that is actively collected
from the atmosphere by pumping and filtration.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/filtered_dust_collector
- **Other Properties:**

[]{#ses207}

####  Cartridge filter residue
- **Child of**:
 [`Filtration residue sampling`](#filtration)
- material left behind when liquid passed throught cartridge filter
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses207
- **Other Properties:**

[]{#sm021}

####  Suspended sediment separate
- **Child of**:
 [`Filtration residue sampling`](#filtration)
 [`Processed separation`](#sm045)
- Suspended sediment separated from containing water by filtration or
centrifuge.
- **Source:**
SESAR collection method; this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm021
- **Other Properties:**

[]{#ses208}

###  Chain saw
- **Child of**:
 [`Sampling method`](#sm100)
- Sample extracted from feature of interest by cutting with a chain
saw.
- **Source:**
SESAR data
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses208
- **Other Properties:**

[]{#ses213}

###  Subaqueous organism trap
- **Child of**:
 [`Sampling method`](#sm100)
- Collection of sample using trap to collect organisms in water, e.g.
crabs, bacteria.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses213
- **Other Properties:**

[]{#ses224}

###  Micropillar Sampling
- **Child of**:
 [`Sampling method`](#sm100)
- focused ion beam (FIB) machining is used to fabricate nano to micron
sized pillars of material for testing of mechanical properties
- **Source:**
https://www.sciencedirect.com/topics/engineering/micropillar-compression
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses224
- **Other Properties:**

[]{#ses226}

###  Pulverize
- **Child of**:
 [`Sampling method`](#sm100)
- reduce to powder
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses226
- **Other Properties:**

[]{#ses227}

###  Scoop
- **Child of**:
 [`Sampling method`](#sm100)
- Interpret to mean collecting some amount of a liquid or fine-grained
aggregate using a spoon-like instrument (scoop); size can range from
milligram to kilogram mass.  Metallurgy: _A shallow, spherical
1.25-inch diameter disc is sawed out of the feature of interest._
https://www.stress.com/services/materials-engineering/field-
inspection-and-testing/non-destructive-scoop-sampling/.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses227
- **Other Properties:**

[]{#ses228}

###  Settlement Plate
- **Child of**:
 [`Sampling method`](#sm100)
- Plates designed to remain in an environment (typically subaqueous)
to monitor biome development. DOI: 10.13140/RG.2.2.33138.71361.  Also
colonization substrate sampler collected in submarine exploration.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses228
- **Other Properties:**

[]{#ses229}

###  Shaker table
- **Child of**:
 [`Sampling method`](#sm100)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses229
- **Other Properties:**

[]{#ses233}

###  Suction Sampling
- **Child of**:
 [`Sampling method`](#sm100)
- Sampling a fluid (liquid, gas, colloid, suspension...) by drawing it
into a sample collection container using a pressure gradient.
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses233
- **Other Properties:**

[]{#ses212}

####  Syringe sampling
- **Child of**:
 [`Suction Sampling`](#ses233)
- Sampling by using a tube with a plunger to pull material into a
cylinder; used in soils, soft sediment, and fluids, commonly for
analysis of volatiles.
- **Source:**
Based on web search for syringe sampling and inspection of SESAR records reporting methods with 'syringe' in the text.  Examples from soil environmental sampling, sediment sampling, water sampling
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses212
- **Other Properties:**

[]{#slurpsampling}

####  Slurp sampling
- **Child of**:
 [`Suction Sampling`](#ses233)
- For some small, delicate, or flexible specimens, the “slurp” hose is
used to ensure that the sample is collected and handled with the
proper care. ROV pilots use the manipulator arm to pick up the handle
of this vacuum-like hose, which then sucks up water, sediment, and
small or delicate fauna into one of the slurp containers.
- **Source:**
https://nautiluslive.org/science/sampling-procedures
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/slurpsampling
- **Other Properties:**

[]{#ses234}

###  Core preserved with wax
- **Child of**:
 [`Sampling method`](#sm100)
- Core coated with wax or other sealant to preserve volatile content
- **Source:**
https://jgmaas.com/SCA/2014/SCA2014-097.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses234
- **Other Properties:**

[]{#sm018}

###  Sediment trap
- **Child of**:
 [`Sampling method`](#sm100)
- Sediment traps are containers placed in the water column to collect
particles falling toward the sea floor. The traps collect tiny
sediment or larger accumulations called marine snow - made up of
organic matter, dead sea creatures, tiny shells, dust and minerals.
- **Source:**
Geoscience Australia, 
SESAR collection method; , 
http://www.whoi.edu/instruments/viewInstrument.do?id=10286, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm018
- **Other Properties:**

[]{#sm041}

###  Coring
- **Child of**:
 [`Sampling method`](#sm100)
- Sample is removed from sampling feature by extracting an undisturbed
provile  typically as a long cylinder  meant to preserve the internal
structure of the sampled sediment or rock.  sample extracted as a
cylinder of material drilled out of the feature of interest; diameter
can range from mm to m, lengths mm to 100_s of m.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm041
- **Other Properties:**

[]{#core_drilling_unspecified}

####  Core drilling
- **Child of**:
 [`Drilling`](#drilling)
 [`Coring`](#sm041)
- Sampling of a core of earth material by an unspecified drilling
method
- **Source:**
Geoscience Australia, 
SESAR collection method, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_drilling_unspecified
- **Other Properties:**

[]{#core_air}

#####  Air cooled core drilling
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- Rock or sediment core derived from a dry, air-cooled diamond
drilling method.
- **Alternate labels:**
core air
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_air
- **Other Properties:**

[]{#core_catcher}

#####  Core catcher
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- A method by which a specimen of sediment is collected from the end
of the core in the core catcher. The core catcher has curved finger-
like projections that extend down to the lowest part of the core
liner. The core catcher helps keep the sediment in the core liner when
the core is being removed from the surface.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_catcher
- **Other Properties:**

[]{#core_cutter}

#####  Core cutter
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- A method by which a specimen of sediment is collected from the
lowest part of a coring assembly at the core cutter. The core cutter
has sharp edges which cut and shape the sediment entering the core
liner as the corer goes into the sediment.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_cutter
- **Other Properties:**

[]{#core_diamond}

#####  Diamond bit drill coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- Rock or sediment core drilling using a liquid-cooled, diamond or
tungsten carbide bit.
- **Alternate labels:**
core diamond
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_diamond
- **Other Properties:**

[]{#core_conventional}

######  core conventional
- **Child of**:
 [`Diamond bit drill coring`](#core_diamond)
- Core drilling using diamond or tungsten carbide bit using a core
barrel with fibreglass inner sleeves. Used in the oil industry.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_conventional
- **Other Properties:**

[]{#core_rov}

#####  Coring from submersible
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- A core produced by a drill mounted on a submersible vehicle, ROV,
HOV.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_rov
- **Other Properties:**

[]{#sidewall_core_mechanical}

#####  Rotary sidewall coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
 [`Sidewall coring`](#sidewall_core)
- Mechanical tools use hollow rotary drills to cut and then pull out
core plugs. Up to 75 plugs can be recovered on one run. With full
recovery, cores from typical percussion tools are 1 in. [2.5 cm] in
diameter by 1 3/4 in. [4.4 cm] long, while those from mechanical tools
are 0.91 in. [2.3 cm] in diameter by 2 in. [5 cm] long. The latter are
also known as rotary sidewall cores.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core_mechanical
- **Other Properties:**

[]{#sm007}

#####  Hand auger coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
- core extracted from sediment or soil by a hand rotated tool with a
special bit that extracts short segments of cored sediment; many
variations in design.
- **Source:**
this vocabulary; http://www.oakenviro.com/pdfs/Dutch%20Auger%20equipment%20options%20-%20Eijkelkamp.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm007
- **Other Properties:**

[]{#sidewall_core}

####  Sidewall coring
- **Child of**:
 [`Drilling`](#drilling)
 [`Coring`](#sm041)
- A method to extract core or plug from the sidewall of a borehole.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core
- **Other Properties:**

[]{#sidewall_core_bullet}

#####  Percussion sidewall coring
- **Child of**:
 [`Sidewall coring`](#sidewall_core)
- Percussion cores are taken by firing hollow bullets into the
formation. The bullets are attached to the tool by fasteners, and are
retrieved, along with the core inside, by pulling up the tool and the
fasteners. Percussion coring tools typically hold 20 to 30 bullets,
but two or three tools can be combined on one run in the hole.
- **Alternate labels:**
sidewall core, bullet
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core_bullet
- **Other Properties:**

[]{#sidewall_core_mechanical}

#####  Rotary sidewall coring
- **Child of**:
 [`Core drilling`](#core_drilling_unspecified)
 [`Sidewall coring`](#sidewall_core)
- Mechanical tools use hollow rotary drills to cut and then pull out
core plugs. Up to 75 plugs can be recovered on one run. With full
recovery, cores from typical percussion tools are 1 in. [2.5 cm] in
diameter by 1 3/4 in. [4.4 cm] long, while those from mechanical tools
are 0.91 in. [2.3 cm] in diameter by 2 in. [5 cm] long. The latter are
also known as rotary sidewall cores.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sidewall_core_mechanical
- **Other Properties:**

[]{#sm005}

####  Soft material coring
- **Child of**:
 [`Coring`](#sm041)
- General category for methods to extract columnar samples
perpendicular to the depositional surface from soil or sediment that
is poorly enough consolidated that it can be sampled without rotary
drilling.
- **Source:**
SESAR collection method
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm005
- **Other Properties:**

[]{#core_geoprobe}

#####  Geoprobe coring
- **Child of**:
 [`Soft material coring`](#sm005)
- High quality core extracted by hydraulic power. Used in rough
terrain, soft sand, mud, shallow water, or tight, congested areas.
Long high quality cores.
- **Alternate labels:**
core geoprobe
- **Source:**
Geoscience Australia, 
https://geoprobe.com/tooling/rock-coring-wet-rotary-systems, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_geoprobe
- **Other Properties:**

[]{#core_mackereth}

#####  core Mackereth
- **Child of**:
 [`Soft material coring`](#sm005)
- The Mackereth is a complex coring system utilizing compressed gas to
penetrate and recover single-drive moderate (up to 12 m) cores from
lakes of diverse depths.  Mackereth cores can be deployed on virutally
any small craft and and can be used in water depths up to 80 m.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_mackereth
- **Other Properties:**

[]{#core_push}

#####  Push coring
- **Child of**:
 [`Soft material coring`](#sm005)
- A pipe that is pushed into the sediment to gain a core that is no
longer than 2m long. Core pipe has a valve on top that is used to
create a vacuum at the top of the core when pulling the core out of
the sediment. Can be operated by a human working on land, shallow
water, or from a boat in shallow water with a pipe extension to reach
the bottom. Can be operated mechanically from a submersible (HOV or
ROV).
- **Alternate labels:**
core push
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_push
- **Other Properties:**

[]{#sm027}

######  Hand held coring
- **Child of**:
 [`Push coring`](#core_push)
- Collects core by operator pushing the core tube into the sediment to
be sampled; may be assisted by vibration induced in the core tube.
Like push core, but manually operated.
- **Source:**
SESAR collection method
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm027
- **Other Properties:**

[]{#core_spike}

#####  core spike
- **Child of**:
 [`Soft material coring`](#sm005)
- A core of surficial material taken by driving a spike into the
ground.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_spike
- **Other Properties:**

[]{#freefallcoring}

#####  Free fall coring
- **Child of**:
 [`Soft material coring`](#sm005)
- collection of core with a tube that has an assembly with weights and
fins, allowed to drop through the water column and penetrate water
bottom sediment.
- **Source:**
reported in SESAR data.
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/freefallcoring
- **Other Properties:**

[]{#phlegercoring}

#####  Phleger coring
- **Child of**:
 [`Soft material coring`](#sm005)
- Small coring device for use in shallow water, for cores <1 m in
length, in  sediment types ranging from soft to sandy, semi-compacted
material, as well as peat and plant roots in shallow lakes or marshes
- **Source:**
https://archive.epa.gov/water/archive/polwaste/web/pdf/ch3.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/phlegercoring
- **Other Properties:**

[]{#ses220}

#####  Trigger coring
- **Child of**:
 [`Soft material coring`](#sm005)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses220
- **Other Properties:**

[]{#ses221}

#####  Kasten coring
- **Child of**:
 [`Soft material coring`](#sm005)
- Large volume, reletatively undisturbed sediment core (~3m long) from
a Kasten Corer. The corer is constructed of stainless steel and is
square in cross-section. A weight of several hundred kilograms on top
of the corer pushes it 2-3 metres into the seabed. It is designed for
sedimentological and geochemical sampling of fine-grained sediments.
This type of corer obtains relatively undisturbed cores and can
preserve the sediment/water interface. This type of core is useful for
determining sediment accumulation rates.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses221
- **Other Properties:**

[]{#ses232}

#####  Slide hammer coring
- **Child of**:
 [`Soft material coring`](#sm005)
-
- **Source:**
SESAR collection methods
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses232
- **Other Properties:**

[]{#sm025}

#####  Box coring
- **Child of**:
 [`Soft material coring`](#sm005)
- A method that obtains a large volume or large surface area core with
shallow penetration and minimum disturbance. Commonly uses a double
spade system.  A box core uses trigger plates that contact the
seafloor to close the top and bottom of a metal box plunged into the
seabed. This device neatly extracts a plug of sediment that is mostly
undisturbed and allows scientists to examine the layers of sediment
carefully and any marine life found within.  Use this category for
Eckman Dredge samples as well
- **Alternate labels:**
core box
- **Source:**
Geoscience Australia, 
SESAR collection method; http://www.deepreef.org/technology/9-grab.html; http://www.eu-hermione.net/box-core; http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf (Eckman dredge), 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm025
- **Other Properties:**

[]{#sm026}

#####  Gravity coring
- **Child of**:
 [`Soft material coring`](#sm005)
- Coring that relies on the weight of the device for penetration into
the seafloor. Geoscience Australia's gravity corer consists of a one
tonne weight atop a steel core barrel which houses an internal PVC
core sleeve. The unit is lowered to a predetermined height above the
seafloor using a wire rope before being allowed to freefall. The
resulting core enters the internal sleeve and is held in place by a
core catcher. The wire rope is then reeled in and the inner sleeve is
removed from the core barrel and the core is processed. Gravity cores
up to 12 metres in length can be collected with some systems but in
practice recoveries are typically less than six metres. The gravity
corer is designed for use in areas of soft, unconsolidated sediment.
- **Alternate labels:**
core gravity
- **Source:**
Geoscience Australia, 
SESAR collection method; http://www.whoi.edu/instruments/viewInstrument.do?id=8087  http://www.whoi.edu/instruments/viewInstrument.do?id=1079, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm026
- **Other Properties:**

[]{#sm028}

#####  Multi coring
- **Child of**:
 [`Soft material coring`](#sm005)
- sampling by pushing a device into seafloor sediments that extracts
many tubular samples of sediment at once. The multicore has a cone-
shaped aluminum frame. In the middle are eight plastic tubes. When the
frame settles on the floor  the center of the multicore slowly and
evenly pushes the tubes into the sediment. The tubes are capped at the
top and bottom and the multicore comes back to the surface with eight
samples of sediment.
- **Source:**
SESAR collection method, 
http://polardiscovery.whoi.edu/expedition5/tools_multicore.html , 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm028
- **Other Properties:**

[]{#sm029}

#####  Piston coring
- **Child of**:
 [`Soft material coring`](#sm005)
- Piston corers have a piston mechanism that is triggered when the
corer hits the bottom. As the barrel enters the sediment a special
internal piston creates a vacuum and helps to draw the core into the
barrel. The piston helps to avoid disturbing the sediment. As the
piston corer penetrates the seafloor  the piston inside stops at the
sediment surface. The action of the piston creates a pressure
differential at the top of the sediment column. This allows the soft
material to enter the core liner without disruption. A piston corer
uses a 'free fall' of the coring rig to achieve a greater initial
force on impact than gravity coring  and a sliding piston inside the
core barrel to reduce inside wall friction with the sediment and to
assist in the evacuation of displaced water from the top of the corer.
The piston-coring rig is comprised of a trigger assembly  the coring
weight assembly  core barrels  tip assembly  and piston.
- **Alternate labels:**
Piston corer, 
core piston, 
- **Source:**
SESAR collection method; http://www.whoi.edu/instruments/gallery.do?mainid=17288&iid=8087; http://www.tdi-bi.com/field_services/sge_info/piston_coring.htm, 
https://www.ga.gov.au/scientific-topics/marine/survey-techniques/sedimentary-coring-drilling, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm029
- **Other Properties:**

[]{#sm030}

#####  Probe core
- **Child of**:
 [`Soft material coring`](#sm005)
- Soil or sediment collected by pneumatically pushing or pounding a
sleeve  through soft sediments via a rig mounted on the back of a
pick-up truck or on an ATV.  Note: Sediment in cores commonly is
compressed to 30-50% of the in situ volume. Wildco corer.
- **Source:**
SESAR collection method; http://www.fandm.edu/earth-and-environment/sediment-sampling-methods
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm030
- **Other Properties:**

[]{#sm031}

#####  Vibrator coring
- **Child of**:
 [`Soft material coring`](#sm005)
- A core tube is attached to a source of mechanical vibration (the
power head) and lowered into  sediment. The vibrations provide energy
for rearranging the particles within the sediment in such a way that
the coretube penetrates under the static weight of the vibracoring
apparatus. Samples include stiff and stony clays, soft rock and sands,
and saturated sediments which can not be sampled using gravity or
piston corers. Also know as VIBRA.
- **Alternate labels:**
core vibro, 
vibracore, 
vibrocore, 
- **Source:**
SESAR collection method; http://www.vibracoring.com/vcconcepts.html, 
http://www.pvltech.com, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm031
- **Other Properties:**

[]{#core_sonic}

######  Sonic coring
- **Child of**:
 [`Vibrator coring`](#sm031)
- Similar to the vibro-core technique, the drill stem and barrel are
vibrated vertically at frequencies between 50Hz and 180Hz such that
the sampler barrel advances by slicing through the regolith.
- **Alternate labels:**
rotosonic drilling
- **Source:**
Geoscience Australia, 
https://www.frtr.gov/site/3_1_6.html, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_sonic
- **Other Properties:**

[]{#waxcoring}

#####  Wax coring
- **Child of**:
 [`Soft material coring`](#sm005)
- Samples sediment and volcanic glass at the sea floor by crashing a
weighted core tube that has a ring of sticky wax at the bottom into
the sea floor.  Invented to sample volcanic glass shards in surface
deposits along mid ocean ridges.
- **Source:**
https://ui.adsabs.harvard.edu/abs/2023AGUFMV43B018.1L/abstract, 
https://web.mit.edu/deeparch/www/publications/papers/YoergerEtAl1999.pdf, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/waxcoring
- **Other Properties:**

[]{#sm043}

###  Fluid sampling
- **Child of**:
 [`Sampling method`](#sm100)
- General category for gas and water sampling procedures that obtain a
specimen in a sealed container, or feed directly to analytical
equipment (e.g. autosamplers).
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm043
- **Other Properties:**

[]{#borehole_fluid_sampling}

####  Borehole fluid sampling
- **Child of**:
 [`Fluid sampling`](#sm043)
- Sampling of fluids (oil, gas, or water) from a borehole by an
unspecified method.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/borehole_fluid_sampling
- **Other Properties:**

[]{#airlift}

#####  Airlift water sampling
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
- Compressed air is used to extract groundwater
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/airlift
- **Other Properties:**

[]{#artesian_flow}

#####  Artesian flow sampling
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
- Groundwater sample obtained from flowing artesian bore
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/artesian_flow
- **Other Properties:**

[]{#bailer}

#####  Borehole bailer sampling
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
- Bailer is a hollow tube used to retrieve groundwater samples from
monitoring wells. A bailer is tied to a piece of rope or wire and
lowered into the water column to collect a sample.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bailer
- **Other Properties:**

[]{#in_situ_grab_sampler}

######  Point souce bailer sampling
- **Child of**:
 [`Borehole bailer sampling`](#bailer)
- A point souce bailer that has a check valve at each end of the
bailer allowing sample collection from a discrete depth
- **Alternate labels:**
in situ grab sampler
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/in_situ_grab_sampler
- **Other Properties:**

[]{#borehole_dst_test}

#####  Borehole drill stem test
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
- A sample is collected during drilling by a test using a hydrostatic
head to measure the formation pressures and to bring the formation
fluids to the surface. The test can provide information for
determination of potential petroleum producing formations and their
exact depth.
- **Alternate labels:**
drill stem test
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/borehole_dst_test
- **Other Properties:**

[]{#borehole_prod_test}

#####  Borehole production test
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
- A borehole sampling test similar to DST test, but on a larger scale
and under the production conditions after the well completion is
conducted.
- **Alternate labels:**
well production test
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/borehole_prod_test
- **Other Properties:**

[]{#borehole_wft_test}

#####  Borehole wireline formation test
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
- A sample is taken from a borehole with a wireline formation tester
by inserting a probe into a well wall to withdraw a small amount of
formation fluid and to measure the formation pore pressure. This
measurement can provide formation pressures along the well hole,
thereby giving a measure of pressure with depth or along a horizontal
borehole.
- **Alternate labels:**
wireline formation test
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/borehole_wft_test
- **Other Properties:**

[]{#boreholewaterpump}

#####  Borehole water pumping
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- A pump designed to lift water or other fluid to the surface from a
borehole.  Various designs exist, including electric submersible,
helical coil, jet.  Include pump jacks and windmills that are specific
to pumping fluid from boreholes, as well as pumps design to be placed
inside the borehole
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/boreholewaterpump
- **Other Properties:**

[]{#liquid-gas_separation}

#####  Liquid-gas separation
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
- Separation of natural gas from a liquid phase at a surface separator
to generate samples of both phases.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/liquid-gas_separation
- **Other Properties:**

[]{#pumpsampling}

####  Pump sampling
- **Child of**:
 [`Fluid sampling`](#sm043)
- Sampling a fluid using a pump to move fluid to the sample container
- **Source:**
SESAR sample descriptions
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/pumpsampling
- **Other Properties:**

[]{#ses215}

####  Ghostbuster fluid sampler
- **Child of**:
 [`Fluid sampling`](#sm043)
- Ghostbuster appears to be a device for in situ chemical measurements
in a high temperature/pressure environment (e.g. sea floor black
smoker), designed by Kang Ding/Bill Seyfried of UMN.  The information
found on the web doesn't indicate it returns material samples, just
measurements. (https://www.marine-
geo.org/services/vocab/vocab_device_type).  https://gfd.whoi.edu/wp-
content/uploads/sites/66/2023/08/at11-7-cruise_report.pdf. https://www
.unols.org/sites/default/files/CA_InstrumentationManipulators.pdf
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses215
- **Other Properties:**

[]{#sm013}

####  Gas sampling
- **Child of**:
 [`Fluid sampling`](#sm043)
- general class for gas sampling methods
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm013
- **Other Properties:**

[]{#ses214}

#####  Gas tight bottle sampling
- **Child of**:
 [`Gas sampling`](#sm013)
- Gas collection in a collection bottle that is sealed well enough to
maintain the pressure of the original sample fluid; used to sample
gasses from deep sea sources.  Described technique uses flow-through
gas sampling.
- **Source:**
https://doi.org/10.1016/j.dsr.2020.103282
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses214
- **Other Properties:**

[]{#sm011}

#####  Evacuated bottle gas sampling
- **Child of**:
 [`Gas sampling`](#sm013)
- A chemically inert and durable tube e.g. titanium quartz alumina or
mullite) is inserted into the gas source, and allowed to thermally
equilibrate with the gas; a specially prepared collection bottle with
a high vacuum stopcock and sample port is attached to the collection
tube.   The bottle is prepared with a concentrated aqueous sodium
hydroxide solution, carefully weighed and evacuated with a vacuum
pump. As gas bubbles through the alkaline solution, acid gases such as
CO2 H2S SO2 HCl and HF dissolve into the liquid. The remaining gases
such as N2 O2 H2 CO and He collect in the headspace of the bottle.
Geothermal system gases are typically omposed mostly of water and
condensable acid gases that are absorbed into the alkaline solution,
so many liters of gas can be collected in a single bottle. This method
concentrates gases in the solution and headspace and thereby promotes
better analytical precision. Typically used for hot (volcanic
geothermal) gas collection.
- **Source:**
http://volcanoes.usgs.gov/activity/methods/gas/sample.php, 
https://asgmt.com/wp-content/uploads/2018/10/105.pdf, 
https://pubs.usgs.gov/of/1974/0361/report.pdf, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm011
- **Other Properties:**

[]{#sm008}

######  Inverted funnel to evacuated bottle gas collection
- **Child of**:
 [`Evacuated bottle gas sampling`](#sm011)
- Gas is collected from a bubbling subaqueous gas source by inverting
a suitable size and composition funnel over the gas source connected
by a tube to an evacuated bottle gas collector.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm008
- **Other Properties:**

[]{#sm012}

#####  Flow through bottle gas sampling
- **Child of**:
 [`Gas sampling`](#sm013)
- Insert a suitable chemically inert and durable tube (e.g. titanium
quartz  alumina  or mullite) into gas source. After allowing the tube
to heat until condensation in the tube has reached equilibrium with
the escaping gases  usually about 5 minutes  a specially-designed
flow-through sample bottle with a stopcock at each end and a hand-
operated pump is attached to the collection tubing.  The hand pump
flushes out air and draws the gas into the bottle. This collection
method is faster that the evacuated bottle method. It is used when a
complete gas analysis is not necessary  or where field conditions are
too hazardous to safely make an evacuated-bottle collection. Sulfur
gases are stable for only a short time so this type of sample must be
analyzed within a few hours of collection.
- **Source:**
http://volcanoes.usgs.gov/activity/methods/gas/sample.php
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm012
- **Other Properties:**

[]{#sm009}

######  Inverted funnel to flow through bottle gas collection
- **Child of**:
 [`Flow through bottle gas sampling`](#sm012)
- Gas is collected from a bubbling subaqueous gas source by inverting
a suitable size and composition funnel over the gas source  connected
by a tube to a  flow through bottle gas collector.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm009
- **Other Properties:**

[]{#sm014}

####  Water sampling
- **Child of**:
 [`Fluid sampling`](#sm043)
- Any method used to sample water.
- Generic category for any method off acquiring a water sample. Water
collected into a suitable container from a single sampling point.
Includes grab sample from stream  samples collected by machines that
open and close sampling bottles as the device is lowered through water
column. e.g. Van Dorn bottles,  Kemmerer Water Sampler
- **Source:**
Geoscience Australia, 
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm014
- **Other Properties:**

[]{#airlift}

#####  Airlift water sampling
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
- Compressed air is used to extract groundwater
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/airlift
- **Other Properties:**

[]{#artesian_flow}

#####  Artesian flow sampling
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
- Groundwater sample obtained from flowing artesian bore
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/artesian_flow
- **Other Properties:**

[]{#bailer}

#####  Borehole bailer sampling
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
- Bailer is a hollow tube used to retrieve groundwater samples from
monitoring wells. A bailer is tied to a piece of rope or wire and
lowered into the water column to collect a sample.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bailer
- **Other Properties:**

[]{#in_situ_grab_sampler}

######  Point souce bailer sampling
- **Child of**:
 [`Borehole bailer sampling`](#bailer)
- A point souce bailer that has a check valve at each end of the
bailer allowing sample collection from a discrete depth
- **Alternate labels:**
in situ grab sampler
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/in_situ_grab_sampler
- **Other Properties:**

[]{#boreholewaterpump}

#####  Borehole water pumping
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- A pump designed to lift water or other fluid to the surface from a
borehole.  Various designs exist, including electric submersible,
helical coil, jet.  Include pump jacks and windmills that are specific
to pumping fluid from boreholes, as well as pumps design to be placed
inside the borehole
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/boreholewaterpump
- **Other Properties:**

[]{#bottlesampling}

#####  Container sampling
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- Water is collected in a container that is opened to collect water at
some specific depth in a water body. Includes Niskin bottles, bottles
on Rosette samplers https://en.wikipedia.org/wiki/Rosette_sampler.
Also bottled samples collected by simple bailer or scoop from water
surface. If water is filtered or preserved use the water sampling
-filtere or -preserved categories.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bottlesampling
- **Other Properties:**

[]{#ses225}

######  Niskin bottle
- **Child of**:
 [`Container sampling`](#bottlesampling)
 [`Water sampling`](#sm014)
- Surface water/seawater collection. A device for collection of water
samples from a specific depth in the water column.
- device used to collect water samples at different depths in the
ocean. It consists of a PVC or metal cylinder with two or more hinged
caps at either end that are remotely operated using a wire or cable.
When the sampler is lowered into the ocean, the caps are opened at
predetermined depths, allowing seawater to be trapped inside without
contamination from the surrounding water.
- **Alternate labels:**
Niskin Water Sampler
- **Source:**
Geoscience Australia, 
https://adkinstruments.in/index.php/categories/oceanography/niskin-water-sampler, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses225
- **Other Properties:**

[]{#core_press}

#####  core press
- **Child of**:
 [`Water sampling`](#sm014)
- Pore water is extracted from core material under pressure.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_press
- **Other Properties:**

[]{#lysimeter}

#####  Lysimeter water collection
- **Child of**:
 [`Water sampling`](#sm014)
- A lysimeter is a container used to measure water movement in soil
and the quality of water. They are used in hydrology and water quality
research to study the natural environment and understand how water
moves through soil.
- **Source:**
https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/lysimeters
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/lysimeter
- **Other Properties:**

[]{#rain_gauge}

#####  Rain gauge
- **Child of**:
 [`Water sampling`](#sm014)
- Rainwater is collected using an approved rain gauge/collector
method.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/rain_gauge
- **Other Properties:**

[]{#ses225}

#####  Niskin bottle
- **Child of**:
 [`Container sampling`](#bottlesampling)
 [`Water sampling`](#sm014)
- Surface water/seawater collection. A device for collection of water
samples from a specific depth in the water column.
- device used to collect water samples at different depths in the
ocean. It consists of a PVC or metal cylinder with two or more hinged
caps at either end that are remotely operated using a wire or cable.
When the sampler is lowered into the ocean, the caps are opened at
predetermined depths, allowing seawater to be trapped inside without
contamination from the surrounding water.
- **Alternate labels:**
Niskin Water Sampler
- **Source:**
Geoscience Australia, 
https://adkinstruments.in/index.php/categories/oceanography/niskin-water-sampler, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses225
- **Other Properties:**

[]{#sm010}

#####  Composite water sampling
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- water sample collected through some documented process over an
extended water volume  meant to characterize that volume  e.g. a
profile in a lake  a stream cross section  or some volume in the
ocean. Many different processes may be used to collect subsamples and
aggregate them into a representative single sample.
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm010
- **Other Properties:**

[]{#sm001}

######  Composite water sampling- preserve with reagent
- **Child of**:
 [`Composite water sampling`](#sm010)
- composite water sample  preserved with reagent (e.g. nitric acid
sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm001
- **Other Properties:**

[]{#sm003}

#######  Composite water sampling- filter and preserve with reagent
- **Child of**:
 [`Composite water sampling- preserve with reagent`](#sm001)
 [`Composite water sampling-filter`](#sm002)
- composite filtered water sample  preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm003
- **Other Properties:**

[]{#sm002}

######  Composite water sampling-filter
- **Child of**:
 [`Composite water sampling`](#sm010)
- composite water sample  filtered as part of the sampling process (in
the field or within a very short time period after collection)
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm002
- **Other Properties:**

[]{#sm003}

#######  Composite water sampling- filter and preserve with reagent
- **Child of**:
 [`Composite water sampling- preserve with reagent`](#sm001)
 [`Composite water sampling-filter`](#sm002)
- composite filtered water sample  preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm003
- **Other Properties:**

[]{#sm022}

#####  Water sampling- preserve with reagent
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- water sample  preserved with reagent (e.g. nitric acid  sulfuric
acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm022
- **Other Properties:**

[]{#sm024}

######  Water sampling-filter and preserve with reagent
- **Child of**:
 [`Water sampling- preserve with reagent`](#sm022)
 [`Water sampling-filter`](#sm023)
- water sample is filtered and preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm024
- **Other Properties:**

[]{#sm023}

#####  Water sampling-filter
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- water is filtered as part of the sampling process (in the field or
within a very short time period after collection) Sample is filtrate.
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm023
- **Other Properties:**

[]{#ses206}

######  Cartridge filter filtrate
- **Child of**:
 [`Water sampling-filter`](#sm023)
- liquid that has been passed through a cartridge filter
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses206
- **Other Properties:**

[]{#sm024}

######  Water sampling-filter and preserve with reagent
- **Child of**:
 [`Water sampling- preserve with reagent`](#sm022)
 [`Water sampling-filter`](#sm023)
- water sample is filtered and preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm024
- **Other Properties:**

[]{#vacuumporewatersampling}

#####  Vacuum pore water sampling
- **Child of**:
 [`Water sampling`](#sm014)
- Extraction of pore water from soil or sediment by creating a vacuum.
- **Source:**
https://www.rhizosphere.com/rhizons/, 
https://www.sedgeochem.uni-bremen.de/rhizon.html, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/vacuumporewatersampling
- **Other Properties:**

[]{#sm044}

###  Other sampling procedure
- **Child of**:
 [`Sampling method`](#sm100)
- Specimen obtained using some mechnical process not identified in
this vocabulary
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm044
- **Other Properties:**

[]{#sm045}

###  Processed separation
- **Child of**:
 [`Sampling method`](#sm100)
- separation of part of a sample by some lab technique; have to look
at processing method for details. E.g. density separation  magnetic
separation  insoluble residue  hand picking.  Too many possibilities
to categorize each subsampling method.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm045
- **Other Properties:**

[]{#chemicalseparation}

####  Chemical separation
- **Child of**:
 [`Processed separation`](#sm045)
- sample collection by chemical processing of a sampled material
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/chemicalseparation
- **Other Properties:**

[]{#densityseparation}

####  Density separation
- **Child of**:
 [`Processed separation`](#sm045)
- isolation of a component of an agregate based on particle density,
e.g. heavy liquid
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/densityseparation
- **Other Properties:**

[]{#sm019}

#####  Panned concentrate sampling
- **Child of**:
 [`Density separation`](#densityseparation)
- Use of a gold-miners pan to concentrate heavy minerals from a loose
sediment (typcially stream sediment) sample
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm019
- **Other Properties:**

[]{#grainsize_separation}

####  Grain size separation
- **Child of**:
 [`Processed separation`](#sm045)
- Separation of various size fractions of mineral or rock particles
from the original specimen. For example, by using a seive or particle
settling.
- **Alternate labels:**
seive
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grainsize_separation
- **Other Properties:**

[]{#ses231}

#####  Sieved aggregate
- **Child of**:
 [`Grain size separation`](#grainsize_separation)
- Sample of particular grain size particles using sieves.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses231
- **Other Properties:**

[]{#microanalyticsampling}

####  Microanalytic sampling
- **Child of**:
 [`Processed separation`](#sm045)
- Sampling microscopic regions of a prepared sample by particle
bombardment (electron, ion...) or with electromagneting beams (laser,
x-ray...)
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/microanalyticsampling
- **Other Properties:**

[]{#sm020}

####  Split processed sample
- **Child of**:
 [`Processed separation`](#sm045)
- mechanical separation of part a processed sample; e.g. taking grains
from a mineral separate, splitting a powdered sample  splitting a
crushed sample
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm020
- **Other Properties:**

[]{#sm021}

####  Suspended sediment separate
- **Child of**:
 [`Filtration residue sampling`](#filtration)
 [`Processed separation`](#sm045)
- Suspended sediment separated from containing water by filtration or
centrifuge.
- **Source:**
SESAR collection method; this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm021
- **Other Properties:**

[]{#sm046}

####  Splitting from bulk sample
- **Child of**:
 [`Processed separation`](#sm045)
- mechanical separation of part of a bulk sample. E.g. breaking a hand
sample up with a hammer and taking pieces, cutting peices from a solid
sample, splitting material in a bagged sample
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm046
- **Other Properties:**

[]{#sm047}

###  Surface grab
- **Child of**:
 [`Sampling method`](#sm100)
- Specimen obtained by picking up material from a surface, subaerial
or subaqueous; may involve breaking material away from outcrop  or
picking up loose material on surface
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm047
- **Other Properties:**

[]{#ses202}

####  Backhoe
- **Child of**:
 [`Surface grab`](#sm047)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses202
- **Other Properties:**

[]{#ses222}

####  Mechanical grab from surface
- **Child of**:
 [`Surface grab`](#sm047)
- under water or atmosphere
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses222
- **Other Properties:**

[]{#sm032}

####  Blasting
- **Child of**:
 [`Surface grab`](#sm047)
- sample collected from rock material freed from outcrop by
explosives; similar to surface grab in that precise location of
specimen in the rock body is not precisely known
- **Source:**
SESAR collection method
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm032
- **Other Properties:**

[]{#sm035}

####  Manual grab
- **Child of**:
 [`Surface grab`](#sm047)
- Material sample is obtained by picking up an object by hand
- **Source:**
SESAR collection method
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm035
- **Other Properties:**

[]{#ses218}

#####  Human grab from surface
- **Child of**:
 [`Manual grab`](#sm035)
- Sample collected by picking up some loose material from subaerial
solid earth boundary surface
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses218
- **Other Properties:**

[]{#sm017}

######  Manual surface grab
- **Child of**:
 [`Human grab from surface`](#ses218)
- Specimen obtained from loose material on surface  e.g. from talus,
colluvium, mine heap.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm017
- **Other Properties:**

[]{#sm040}

######  Lag sample
- **Child of**:
 [`Human grab from surface`](#ses218)
- Sample collected by sweeping up surface lag material over some area
and bagging it.  Generally only used in arid or semi-arid environments
where surface lag is representative in some way of underlying bedrock.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm040
- **Other Properties:**

[]{#sm016}

#####  Collected from outcrop
- **Child of**:
 [`Manual grab`](#sm035)
- specimen obtained by breaking piece(s) of rock from rock outcrop  on
surface  or in a subsurface tunnel
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm016
- **Other Properties:**

[]{#ses210}

######  Chip sampling
- **Child of**:
 [`Collected from outcrop`](#sm016)
- sampling over an area of a feature off interest by breaking off
small pieces; produces an aggregate
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses210
- **Other Properties:**

[]{#ses216}

######  Hammer from outcrop
- **Child of**:
 [`Collected from outcrop`](#sm016)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses216
- **Other Properties:**

[]{#sm015}

######  Channel sampling
- **Child of**:
 [`Collected from outcrop`](#sm016)
- sampling material along a channel through a feature of interest.
- **Source:**
, 
USGS Circular; Vernon E. Swanson and Claude Huffman  Jr.  1976  GUIDELINES FOR SAMPLE COLLECTING AND ANALYTICAL METHODS USED IN THE U.S. GEOLOGICAL SURVEY FOR DETERMINING CHEMICAL COMPOSITION OF COAL: U. S. Geological Survey  CIRCULAR 735. accessed at http://energy.er.usgs.gov/products/databases/CoalQual/Docs/c735.pdf, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm015
- **Other Properties:**

[]{#sm034}

#####  Grab from trench or pit
- **Child of**:
 [`Manual grab`](#sm035)
- loose sediment collected into bag from the wall of a trench, stream
bank  or pit--any vertical cut that provides access to a near surface
soil and sediment profile; common for sampling soil horizons.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm034
- **Other Properties:**

[]{#sm037}

####  Stream sediment composite
- **Child of**:
 [`Surface grab`](#sm047)
- composite of several single grab sediment samples collected from a
stream channel agregatted in the field. Sample might be collected from
subaqueous stream bed, or in a dry stream channel.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm037
- **Other Properties:**

[]{#sm038}

####  Stream sediment single grab
- **Child of**:
 [`Surface grab`](#sm047)
- stream sediment collected from bed of a stream at a single location;
Sample might be collected from subaqueous stream bed, or in a dry
stream channel.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm038
- **Other Properties:**

[]{#sm039}

####  Water body bottom grab
- **Child of**:
 [`Surface grab`](#sm047)
 [`Water body survey sampling`](#waterbodysampling)
- renamed from grab SMR 2024-09-11
- Specimens gathered from the bed of a water body by a mechanical grab
primarily for lithogical and petrographical analyses.
- **Alternate labels:**
Submarine grab
- **Source:**
Geoscience Australia, 
SESAR collection method, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm039
- **Other Properties:**

[]{#grab_smith_mcintyre}

#####  Smith Mcintyre grab sampling
- **Child of**:
 [`Water body bottom grab`](#sm039)
- Near surface sediment grab sample. Sample has a surface area of
0.1m2. It is useful for quantitative macrobenthos sampling in either
shallow or deep water.
- **Alternate labels:**
grab Smith Mcintyre
- **Source:**
https://www.ga.gov.au/scientific-topics/marine/survey-techniques/sedimentary-coring-drilling
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_smith_mcintyre
- **Other Properties:**

[]{#ses201}

#####  Submersible grab
- **Child of**:
 [`Water body bottom grab`](#sm039)
- Collect sample from an underwater vehicle, using mechanical arms on
vehicle.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses201
- **Other Properties:**

[]{#ses205}

#####  Campbell grab sampling
- **Child of**:
 [`Water body bottom grab`](#sm039)
- utilizes a pulley arrangement to gain extra purchase to activate a
pair of jaws.  Shepard (1973) reports that  large Petersen grabs have
been known to bring back undisturbed samples that still retain
stratification characteristics.  However, Schlieper (1972) points out
that the tensile closing action from the attached hydrowire creates a
secondary lifting force at the central axis that the two jaws pivot
around, resulting in a shallower bite (5 centimeters (cm) or less),
especially in firmer sediments. photo shows large jaw pincers, bigger
that other grab samplers, dated 1963, so it is likely old technology
no longer in use.
- **Source:**
PSEP, 1997. Recommended Guidelines for Sampling Marine Sediment, Water Column, and Tissue in Puget Sound. 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses205
- **Other Properties:**

[]{#sm036}

#####  Sediment grab
- **Child of**:
 [`Water body bottom grab`](#sm039)
- Sediment grabs come in all shapes and sizes  but they all do much
the same thing  to collect a sample of sediment from the seabed.
Sediment grabs are often named after their inventors. For example  the
Smith-MacIntyre grab is lowered from ships  and on contact with the
seabed a split cylindrical bucket is triggered which scoops up about
10 litres of sediment. Another is the Van-Veen grab like a giant pair
of tongs which closes two halves of the bucket together as the winch
draws the cable in. Sediment is then evenly scooped into the large
buckets. A sediment grab does not attempt to preserve the internal
structure of the sediment  which disginguishes it from soft sediment
coring.
- **Source:**
http://www.deepreef.org/technology/9-grab.html
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm036
- **Other Properties:**

[]{#grab_eckman}

######  grab Eckman
- **Child of**:
 [`Sediment grab`](#sm036)
- The Eckman Bottom Grab sampler is designed for sampling in soft
bottomed lakes and rivers composed of muck, mud or fine peat
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_eckman
- **Other Properties:**

[]{#grab_shipek}

######  grab Shipek
- **Child of**:
 [`Sediment grab`](#sm036)
- When the grab touches the bottom, inertia from a self-contained
weight releases a catch and helical springs rotate the inner half
cylinder by 180°. After turning, the scoop remains closed by the
residual torque of the scoop spring. Because the rotation of the
bucket is extremely rapid, it cuts the sediment cleanly, particularly
in soft clays, muds, silts & sands.  After closing, the sample has
optimum protection from washout during retrieval by the cylindrical
design. https://www.wildco.com/how-does-the-shipek-grab-operate/,
https://www.feritech.com/products/geotechnical/sea-floor-grabs/shipek-
grab/
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_shipek
- **Other Properties:**

[]{#grab_van_veen}

######  Van Veen grab sampling
- **Child of**:
 [`Sediment grab`](#sm036)
- Quantitative sample of the sediment. Van Veen grab has long arms for
levering the clam shell scoop.
- **Alternate labels:**
grab Van Veen
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_van_veen
- **Other Properties:**

[]{#surface_material_sampling}

####  Subaerial surface sampling
- **Child of**:
 [`Surface grab`](#sm047)
- Collection of earth materials at the ground surface on land.
- **Alternate labels:**
Surface material sampling
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/surface_material_sampling
- **Other Properties:**

[]{#outcrop_sampling}

#####  Outcrop sampling
- **Child of**:
 [`Subaerial surface sampling`](#surface_material_sampling)
- Collection of material from a rock outcrop or subcrop at the ground
surface, typically using a hammer, or feathers and wedges.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/outcrop_sampling
- **Other Properties:**

[]{#pit_or_trench_sampling}

#####  Pit or trench sampling
- **Child of**:
 [`Subaerial surface sampling`](#surface_material_sampling)
- Collection of materials, typically regolith, near the ground surface
from a pit, trench, or costean dug by spade, backhoe, or other
mechanical means (not drilling).
- **Alternate labels:**
costean
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/pit_or_trench_sampling
- **Other Properties:**

[]{#ses230}

#####  Shovel
- **Child of**:
 [`Subaerial surface sampling`](#surface_material_sampling)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses230
- **Other Properties:**

[]{#undergound_mine_sampling}

#####  Undergound mine sampling
- **Child of**:
 [`Subaerial surface sampling`](#surface_material_sampling)
- Collection of material from a rock outcrop exposed beneath the
ground surface (eg, a mine), typically using a hammer.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/undergound_mine_sampling
- **Other Properties:**

[]{#sm200}

###  Sediment water incubation sampling
- **Child of**:
 [`Sampling method`](#sm100)
- Samples that include sediment and water, typically from near water
body bottom, collected under controlled conditions to preserve
biological activity, intended to incubate in a lab to observe
metabolic processes.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm200
- **Other Properties:**

[]{#bottle_incubation}

####  bottle incubation
- **Child of**:
 [`Sediment water incubation sampling`](#sm200)
- A method to derive the oxygen consumption rate/respiration rates of
organic matter conducted in a bottle or vial  under controlled light
and temperature conditions.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bottle_incubation
- **Other Properties:**

[]{#bottle_incubation_dark}

#####  bottle incubation dark
- **Child of**:
 [`bottle incubation`](#bottle_incubation)
- A method to derive the oxygen consumption rate/respiration rates of
organic matter conducted in a bottle or vial  under controlled light
and temperature conditions.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bottle_incubation_dark
- **Other Properties:**

[]{#bottle_incubation_light}

#####  bottle incubation light
- **Child of**:
 [`bottle incubation`](#bottle_incubation)
- A method to derive the oxygen consumption rate/respiration rates of
organic matter conducted in a bottle or vial  under controlled light
and temperature conditions.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bottle_incubation_light
- **Other Properties:**

[]{#chamber_incubation}

####  Chamber incubation
- **Child of**:
 [`Sediment water incubation sampling`](#sm200)
- A method that isolates sediment and overlying water in a benthic
chamber. Water samples are collected from the benthic chamber during
the incubation.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/chamber_incubation
- **Other Properties:**

[]{#chamber_incubation_dark}

#####  chamber incubation dark
- **Child of**:
 [`Chamber incubation`](#chamber_incubation)
- A in situ method that isolates sediment and overlying water in a
dark benthic chamber. Incubation water samples are collected from the
benthic chamber during the incubation. The dark chamber restricts
light penetration and therefore stops the process of photosynthesis.
This enables benthic respiration to be measured.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/chamber_incubation_dark
- **Other Properties:**

[]{#chamber_incubation_light}

#####  chamber incubation light
- **Child of**:
 [`Chamber incubation`](#chamber_incubation)
- A in situ method that isolates sediment and overlying water in a
light benthic chamber. Incubation water samples are collected from the
benthic chamber during the incubation. The  transparent walls of the
chamber allow light penetration and enables benthic respiration and
photosynthesis to be measured.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/chamber_incubation_light
- **Other Properties:**

[]{#core_incubation_dark}

####  core incubation dark
- **Child of**:
 [`Sediment water incubation sampling`](#sm200)
- A method whereby a sediment core is collected along with overlying
water. The sediment and water are incubated under no light and
controlled temperature conditions.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_incubation_dark
- **Other Properties:**

[]{#core_incubation_light}

####  core incubation light
- **Child of**:
 [`Sediment water incubation sampling`](#sm200)
- A method whereby a sediment core is collected along with overlying
water. The sediment and water are incubated under controlled light and
temperature conditions.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/core_incubation_light
- **Other Properties:**

[]{#unknown}

###  unknown
- **Child of**:
 [`Sampling method`](#sm100)
- The sampling method is unknown.
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/unknown
- **Other Properties:**

[]{#waterbodysampling}

###  Water body survey sampling
- **Child of**:
 [`Sampling method`](#sm100)
- Collection of materials during a marine, lacustrine, or coastal
survey by any method.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/waterbodysampling
- **Other Properties:**

[]{#epibenthic_sled}

####  Benthic sled sampling
- **Child of**:
 [`Water body survey sampling`](#waterbodysampling)
- A method designed to collect benthic and benthopelagic faunas from
the deep sea. The sled is made from a steel frame consisting of two
skids and stabilizing planes to keep it from sinking too deep into the
mud.
- **Alternate labels:**
epibenthic sled, 
plantobenthic sampler, 
sled benthic, 
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/epibenthic_sled
- **Other Properties:**

[]{#sm033}

####  Dredge sampling
- **Child of**:
 [`Water body survey sampling`](#waterbodysampling)
- samples _grabbed_ from submarine surface by dragging a basket with
an enclosed bottom (solid or open-chain) along the bottom of the water
body.
- **Alternate labels:**
Dredging
- **Source:**
Geoscience Australia, 
SESAR collection method, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm033
- **Other Properties:**

[]{#diamantina_dredge}

#####  dredge diamantina
- **Child of**:
 [`Dredge sampling`](#sm033)
- Used as a spot dredge to quickly ascertain sea bed geology. Samples
give the seabed character unless it is deep when any mud is washed out
during retrieval. In shallow water this dredge will return rock, mud,
benthic samples and any thing else that is on the bottom.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/diamantina_dredge
- **Other Properties:**

[]{#pipe_dredge}

#####  dredge pipe
- **Child of**:
 [`Dredge sampling`](#sm033)
- Sampling of small fragments and mud from the sea floor, using a
metal pipe linked to the tow cable. Total weight of the dredge is
around 25kg.
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/pipe_dredge
- **Other Properties:**

[]{#sm006}

#####  Chain bag dredge
- **Child of**:
 [`Dredge sampling`](#sm033)
- A rock dredge is a large bag made of metal chain links attached to a
simple heavy frame that keeps the bag expanded. The dredge is lowered
off the back of a ship to the seafloor and dragged along to collect
large pieces of rock. Because of the coarse chain links  most of the
finer material is washed out of the bag  leaving behind the larger
rock and gravel pieces within the chain bag. The dredge is then
winched up to the surface and any samples are dumped onto the deck of
the ship to be sorted and preserved.
- Sampling of large rocks from the sea floor using a chain bag
- **Alternate labels:**
dredge chain bag
- **Source:**
Geoscience Australia, 
SESAR collection method; http://www.deepreef.org/technology/79-rock-dredge.html, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm006
- **Other Properties:**

[]{#sm039}

####  Water body bottom grab
- **Child of**:
 [`Surface grab`](#sm047)
 [`Water body survey sampling`](#waterbodysampling)
- renamed from grab SMR 2024-09-11
- Specimens gathered from the bed of a water body by a mechanical grab
primarily for lithogical and petrographical analyses.
- **Alternate labels:**
Submarine grab
- **Source:**
Geoscience Australia, 
SESAR collection method, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm039
- **Other Properties:**

[]{#grab_smith_mcintyre}

#####  Smith Mcintyre grab sampling
- **Child of**:
 [`Water body bottom grab`](#sm039)
- Near surface sediment grab sample. Sample has a surface area of
0.1m2. It is useful for quantitative macrobenthos sampling in either
shallow or deep water.
- **Alternate labels:**
grab Smith Mcintyre
- **Source:**
https://www.ga.gov.au/scientific-topics/marine/survey-techniques/sedimentary-coring-drilling
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_smith_mcintyre
- **Other Properties:**

[]{#ses201}

#####  Submersible grab
- **Child of**:
 [`Water body bottom grab`](#sm039)
- Collect sample from an underwater vehicle, using mechanical arms on
vehicle.
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses201
- **Other Properties:**

[]{#ses205}

#####  Campbell grab sampling
- **Child of**:
 [`Water body bottom grab`](#sm039)
- utilizes a pulley arrangement to gain extra purchase to activate a
pair of jaws.  Shepard (1973) reports that  large Petersen grabs have
been known to bring back undisturbed samples that still retain
stratification characteristics.  However, Schlieper (1972) points out
that the tensile closing action from the attached hydrowire creates a
secondary lifting force at the central axis that the two jaws pivot
around, resulting in a shallower bite (5 centimeters (cm) or less),
especially in firmer sediments. photo shows large jaw pincers, bigger
that other grab samplers, dated 1963, so it is likely old technology
no longer in use.
- **Source:**
PSEP, 1997. Recommended Guidelines for Sampling Marine Sediment, Water Column, and Tissue in Puget Sound. 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses205
- **Other Properties:**

[]{#sm036}

#####  Sediment grab
- **Child of**:
 [`Water body bottom grab`](#sm039)
- Sediment grabs come in all shapes and sizes  but they all do much
the same thing  to collect a sample of sediment from the seabed.
Sediment grabs are often named after their inventors. For example  the
Smith-MacIntyre grab is lowered from ships  and on contact with the
seabed a split cylindrical bucket is triggered which scoops up about
10 litres of sediment. Another is the Van-Veen grab like a giant pair
of tongs which closes two halves of the bucket together as the winch
draws the cable in. Sediment is then evenly scooped into the large
buckets. A sediment grab does not attempt to preserve the internal
structure of the sediment  which disginguishes it from soft sediment
coring.
- **Source:**
http://www.deepreef.org/technology/9-grab.html
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm036
- **Other Properties:**

[]{#grab_eckman}

######  grab Eckman
- **Child of**:
 [`Sediment grab`](#sm036)
- The Eckman Bottom Grab sampler is designed for sampling in soft
bottomed lakes and rivers composed of muck, mud or fine peat
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_eckman
- **Other Properties:**

[]{#grab_shipek}

######  grab Shipek
- **Child of**:
 [`Sediment grab`](#sm036)
- When the grab touches the bottom, inertia from a self-contained
weight releases a catch and helical springs rotate the inner half
cylinder by 180°. After turning, the scoop remains closed by the
residual torque of the scoop spring. Because the rotation of the
bucket is extremely rapid, it cuts the sediment cleanly, particularly
in soft clays, muds, silts & sands.  After closing, the sample has
optimum protection from washout during retrieval by the cylindrical
design. https://www.wildco.com/how-does-the-shipek-grab-operate/,
https://www.feritech.com/products/geotechnical/sea-floor-grabs/shipek-
grab/
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_shipek
- **Other Properties:**

[]{#grab_van_veen}

######  Van Veen grab sampling
- **Child of**:
 [`Sediment grab`](#sm036)
- Quantitative sample of the sediment. Van Veen grab has long arms for
levering the clam shell scoop.
- **Alternate labels:**
grab Van Veen
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/grab_van_veen
- **Other Properties:**

[]{#trawlsampling}

####  Trawl sampling
- **Child of**:
 [`Water body survey sampling`](#waterbodysampling)
- Collection of sample by dragging a net through the water column or
along the bottom of the water column. Connotation is focus on biome in
the water or at the water-sediment interface, but might include
suspended sediment in water or sediment from water body bottom.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/trawlsampling
- **Other Properties:**

[]{#benthic_trawl}

#####  Benthic trawl
- **Child of**:
 [`Trawl sampling`](#trawlsampling)
- Seabed sampling taken over a small area seaward of the continental
shelf. Sample of the upper few cm of rocky sea floor particularly for
biota.
- **Alternate labels:**
benthic dredge
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/benthic_trawl
- **Other Properties:**

[]{#ses200}

#####  Agassiz trawl
- **Child of**:
 [`Trawl sampling`](#trawlsampling)
- Nets towed over the sea floor to sample species living on or near
the bottom, with single rectangular mouth piece, a conical filtering
net, and equipped with closing mouth mechanism.
- **Source:**
<http://vocab.nerc.ac.uk/collection/L22/current/TOOL0991/1>
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses200
- **Other Properties:**

[]{#ses203}

#####  Beam trawl
- **Child of**:
 [`Trawl sampling`](#trawlsampling)
- Nets towed over the sea floor having the horizontal net opening
provided by a wooden or metal beam that disrupts the surface of the
bed.
- **Source:**
<http://vocab.nerc.ac.uk/collection/L05/current/62>
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses203
- **Other Properties:**

[]{#ses204}

#####  Blake trawl
- **Child of**:
 [`Trawl sampling`](#trawlsampling)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses204
- **Other Properties:**

[]{#ses223}

#####  Menzie trawl
- **Child of**:
 [`Trawl sampling`](#trawlsampling)
-
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses223
- **Other Properties:**

[]{#waterbodywatersampling}

####  Water body water sampling
- **Child of**:
 [`Water body survey sampling`](#waterbodysampling)
- Collection of water samples from a water body; includes surface
water, lakes, marine water.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/waterbodywatersampling
- **Other Properties:**

[]{#boreholewaterpump}

#####  Borehole water pumping
- **Child of**:
 [`Borehole fluid sampling`](#borehole_fluid_sampling)
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- A pump designed to lift water or other fluid to the surface from a
borehole.  Various designs exist, including electric submersible,
helical coil, jet.  Include pump jacks and windmills that are specific
to pumping fluid from boreholes, as well as pumps design to be placed
inside the borehole
- **Source:**
Geoscience Australia
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/boreholewaterpump
- **Other Properties:**

[]{#bottlesampling}

#####  Container sampling
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- Water is collected in a container that is opened to collect water at
some specific depth in a water body. Includes Niskin bottles, bottles
on Rosette samplers https://en.wikipedia.org/wiki/Rosette_sampler.
Also bottled samples collected by simple bailer or scoop from water
surface. If water is filtered or preserved use the water sampling
-filtere or -preserved categories.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/bottlesampling
- **Other Properties:**

[]{#ses225}

######  Niskin bottle
- **Child of**:
 [`Container sampling`](#bottlesampling)
 [`Water sampling`](#sm014)
- Surface water/seawater collection. A device for collection of water
samples from a specific depth in the water column.
- device used to collect water samples at different depths in the
ocean. It consists of a PVC or metal cylinder with two or more hinged
caps at either end that are remotely operated using a wire or cable.
When the sampler is lowered into the ocean, the caps are opened at
predetermined depths, allowing seawater to be trapped inside without
contamination from the surrounding water.
- **Alternate labels:**
Niskin Water Sampler
- **Source:**
Geoscience Australia, 
https://adkinstruments.in/index.php/categories/oceanography/niskin-water-sampler, 
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses225
- **Other Properties:**

[]{#sm010}

#####  Composite water sampling
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- water sample collected through some documented process over an
extended water volume  meant to characterize that volume  e.g. a
profile in a lake  a stream cross section  or some volume in the
ocean. Many different processes may be used to collect subsamples and
aggregate them into a representative single sample.
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm010
- **Other Properties:**

[]{#sm001}

######  Composite water sampling- preserve with reagent
- **Child of**:
 [`Composite water sampling`](#sm010)
- composite water sample  preserved with reagent (e.g. nitric acid
sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm001
- **Other Properties:**

[]{#sm003}

#######  Composite water sampling- filter and preserve with reagent
- **Child of**:
 [`Composite water sampling- preserve with reagent`](#sm001)
 [`Composite water sampling-filter`](#sm002)
- composite filtered water sample  preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm003
- **Other Properties:**

[]{#sm002}

######  Composite water sampling-filter
- **Child of**:
 [`Composite water sampling`](#sm010)
- composite water sample  filtered as part of the sampling process (in
the field or within a very short time period after collection)
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm002
- **Other Properties:**

[]{#sm003}

#######  Composite water sampling- filter and preserve with reagent
- **Child of**:
 [`Composite water sampling- preserve with reagent`](#sm001)
 [`Composite water sampling-filter`](#sm002)
- composite filtered water sample  preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm003
- **Other Properties:**

[]{#sm022}

#####  Water sampling- preserve with reagent
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- water sample  preserved with reagent (e.g. nitric acid  sulfuric
acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm022
- **Other Properties:**

[]{#sm024}

######  Water sampling-filter and preserve with reagent
- **Child of**:
 [`Water sampling- preserve with reagent`](#sm022)
 [`Water sampling-filter`](#sm023)
- water sample is filtered and preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm024
- **Other Properties:**

[]{#sm023}

#####  Water sampling-filter
- **Child of**:
 [`Water sampling`](#sm014)
 [`Water body water sampling`](#waterbodywatersampling)
- water is filtered as part of the sampling process (in the field or
within a very short time period after collection) Sample is filtrate.
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm023
- **Other Properties:**

[]{#ses206}

######  Cartridge filter filtrate
- **Child of**:
 [`Water sampling-filter`](#sm023)
- liquid that has been passed through a cartridge filter
- **Source:**

- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/ses206
- **Other Properties:**

[]{#sm024}

######  Water sampling-filter and preserve with reagent
- **Child of**:
 [`Water sampling- preserve with reagent`](#sm022)
 [`Water sampling-filter`](#sm023)
- water sample is filtered and preserved with reagent (e.g. nitric
acid  sulfuric acid) as part of sampling process
- **Source:**
e.g. see http://www.azdeq.gov/environ/water/assessment/download/sampling.pdf
- **Concept URI:** https://w3id.org/sesar/samplingmethods/0.1/sm024
- **Other Properties:**


