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

[]{#SESARmaterialsampleobjecttypeextension}

# **Concept scheme:** SESAR material sample object type extension

Vocabulary last modified:  2024-12-04

subtitle: 
  Terms to categorize material sample object in more detail than the iSamples vocabularies. This vocabulary extends the iSamples Earth and Environmental Science extension -  Material sample type vocabulary.

Namespace: 
[`https://w3id.org/sesar/objecttype/objecttypevocabulary`](https://w3id.org/sesar/objecttype/objecttypevocabulary)

**History**

* 2024-12-04 SMR add mapping to osiris rex sample types.
* 2024-12-04 SMR generate to account for SESAR sample types, which include some sampling features.

- [Material sample](#materialsample)
    - [Any aggregation material sample](#anyaggregation)
        - [Anthropogenic aggregation](#anthropogenicaggregation)
        - [Biome aggregation sample](#biomeaggregation)
            - [Bundle biome aggregation](#bundlebiomeaggregation)
                - [Cell culture](#cellculture)
                - [Water biome](#waterbiome)
            - [Slurry biome aggregation](#slurrybiomeaggregation)
                - [Soil biome](#soilbiome)
        - [Aggregation](#genericaggregation)
            - [Boxed core](#boxedcore)
            - [Composite sample](#compositesample)
                - [Chip Channel Sample](#chipchannelsample)
                - [High Grade Sample](#highgradesample)
                - [Site composite sample](#sitecompositesample)
            - [Core catcher](#corecatcher)
            - [Cuttings](#cuttings)
            - [Dredge](#dredge)
            - [Material captured in filter](#materialcapturedinfilter)
            - [Mechanical fraction](#mechanicalfraction)
            - [Mineral separate](#mineralseparate)
                - [Magnetic fraction](#magneticfraction)
                - [Non-magnetic fraction](#nonmagneticfraction)
            - [Natural aggregate specimen](#naturalaggregate)
            - [Prepared powder](#preparedpowder)
                - [Prepared rock powder](#preparedrockpowder)
            - [TEM grid](#temgrid)
            - [Trawl](#trawl)
    - [Biological material sample](#biologicalmaterialsample)
        - [Biome aggregation sample](#biomeaggregation)
            - [Bundle biome aggregation](#bundlebiomeaggregation)
                - [Cell culture](#cellculture)
                - [Water biome](#waterbiome)
            - [Slurry biome aggregation](#slurrybiomeaggregation)
                - [Soil biome](#soilbiome)
        - [Organism part](#organismpart)
        - [Organism product](#organismproduct)
        - [Whole organism material sample](#wholeorganism)
        - [Human tissue](#humantissue)
    - [Fluid in container](#fluidincontainer)
        - [Direct fluid sample](#directfluidsample)
        - [Dissolved chemical fraction](#dissolvedchemicalfraction)
            - [Eluate](#eluate)
        - [Processed fluid sample](#processedfluidsample)
            - [Filtrate](#filtrate)
    - [Non biologic solid object](#nonbiologicsolidobject)
        - [Artifact](#artifact)
        - [Fossil](#fossil)
        - [Other solid object](#othersolidobject)
            - [Dust wipe](#dustwipe)
            - [Glass slide smear](#glassslidesmear)
            - [Peel](#peel)
        - [Solid material sample](#solidmaterialsample)
            - [Core](#core)
            - [Core half round](#corehalfround)
            - [Core piece](#corepiece)
            - [Core quarter round](#corequarterround)
            - [Core section](#coresection)
            - [Core subpeice](#coresubpeice)
            - [FIB lamella](#fiblamella)
            - [Individual solid cube](#individualsolidcube)
            - [Individual solid cylinder](#individualsolidcylinder)
            - [Meteorite](#meteorite)
            - [Mineral specimen](#mineralspecimen)
            - [Sectioned specimen](#mountedsection)
                - [Thick section](#thicksection)
                - [Thin section](#thinsection)
                    - [Polished thin section](#polishedthinsection)
                - [Ultra thin section](#ultrathinsection)
            - [Pressed pellet](#pressedpellet)
            - [Rock hand sample](#rockhandsample)
            - [Slab](#slab)
            - [U-channel sample](#uchannelsample)
            - [Atom probe tip](#atomprobetip)
            - [Chip](#chip)
            - [Microtome slice](#microtomeslice)
            - [Mounted specimen](#mountedspecimen)
                - [Polished mounted specimen](#polishedmountedspecimen)
            - [Particle](#particle)
    - [Research product](#researchproduct)
        - [Analytical preparation](#analyticalpreparation)
            - [Cell culture](#cellculture)
            - [Dissolved chemical fraction](#dissolvedchemicalfraction)
                - [Eluate](#eluate)
            - [FIB lamella](#fiblamella)
            - [Glass slide smear](#glassslidesmear)
            - [Individual solid cube](#individualsolidcube)
            - [Magnetic fraction](#magneticfraction)
            - [Mechanical fraction](#mechanicalfraction)
            - [Mineral separate](#mineralseparate)
                - [Magnetic fraction](#magneticfraction)
                - [Non-magnetic fraction](#nonmagneticfraction)
            - [Sectioned specimen](#mountedsection)
                - [Thick section](#thicksection)
                - [Thin section](#thinsection)
                    - [Polished thin section](#polishedthinsection)
                - [Ultra thin section](#ultrathinsection)
            - [Non-magnetic fraction](#nonmagneticfraction)
            - [Peel](#peel)
            - [Prepared powder](#preparedpowder)
                - [Prepared rock powder](#preparedrockpowder)
            - [Pressed pellet](#pressedpellet)
            - [Residual material](#residualmaterial)
            - [Slab](#slab)
            - [Atom probe tip](#atomprobetip)
            - [Squeeze cake](#squeezecake)
        - [Experiment product](#experimentalproduct)

- [Sampling feature](#samplingfeature)
    - [Hole](#hole)
    - [Sampling site](#site)
    - [Terrestrial section](#terrestrialsection)

- [anysampledfeature](#anysampledfeature)

**Concepts**

[]{#materialsample}

##  Material sample
- A material entity that represents an entity of interest in whole or
in part (http://rs.tdwg.org/dwc/terms/MaterialSample). Top concept in
material sample object type hierarchy.  Represents any material sample
object.
- **Alternate labels:**
Physical specimen
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/materialsample
- **Other Properties:**

[]{#anyaggregation}

###  Any aggregation material sample
- **Child of**:
 [`Material sample`](#materialsample)
- Sample consists of a bunch of material fragments, not related to the
same object (e.g. not a bunch of broken pot sherds that might be
reassembled), but taken together representative of the sampled
feature. Examples: loose soil, sediment, crushed rock,  particulate,
bunches of unrelated pot sherd, human production waste, filtrates and
residues. The sample requires some kind of container to keep it
together. Cores of loosely consolidated material are considered 'Solid
material specimen' when preserved such that the internal parts have
spatial relationships (e.g. upper part, lower part, sedimentary
structures).
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/anyaggregation
- **Other Properties:**

[]{#anthropogenicaggregation}

####  Anthropogenic aggregation
- **Child of**:
 [`Any aggregation material sample`](#anyaggregation)
- An aggregate material sample consisting of fragments of material
produced by human activity, not described individually, and generally
not all originating from the same object.  Includes pottery in an
excavation unit that gets an aggregate description, production waste,
production raw-materials, or other residues (broken bits of plaster
from a destroyed wall), synthetic powders.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/anthropogenicaggregation
- **Other Properties:**

[]{#biomeaggregation}

####  Biome aggregation sample
- **Child of**:
 [`Any aggregation material sample`](#anyaggregation)
 [`Biological material sample`](#biologicalmaterialsample)
- Material sample that is an aggregation of whole or fragmentary parts
of multiple organisms, microscopic or megascopic, representative of
some sampled feature.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/biomeaggregation
- **Other Properties:**

[]{#bundlebiomeaggregation}

#####  Bundle biome aggregation
- **Child of**:
 [`Biome aggregation sample`](#biomeaggregation)
- Material sample that is an aggregation of whole organisms
representative of some biome.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/bundlebiomeaggregation
- **Other Properties:**

[]{#cellculture}

######  Cell culture
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Bundle biome aggregation`](#bundlebiomeaggregation)
- a collection of cells are grown under controlled conditions,
generally outside of their natural environment
- **Source:**
https://en.wikipedia.org/wiki/Cell_culture
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/cellculture
- **Other Properties:**

[]{#waterbiome}

######  Water biome
- **Child of**:
 [`Bundle biome aggregation`](#bundlebiomeaggregation)
- sample is water and included microorganisms living in the water.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/waterbiome
- **Other Properties:**

[]{#slurrybiomeaggregation}

#####  Slurry biome aggregation
- **Child of**:
 [`Biome aggregation sample`](#biomeaggregation)
- Material sample that consists of mixed organic and inorganic
material, including whole organisms and organism fragments.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/slurrybiomeaggregation
- **Other Properties:**

[]{#soilbiome}

######  Soil biome
- **Child of**:
 [`Slurry biome aggregation`](#slurrybiomeaggregation)
- Sample is soil with included microorganisms and other organism parts
or products. {@en{}
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/soilbiome
- **Other Properties:**

[]{#genericaggregation}

####  Aggregation
- **Child of**:
 [`Any aggregation material sample`](#anyaggregation)
- An aggregate material sample that is not biogenic or composed of
anthropogenic material fragments.  Examples: loose soil or sediment
(e.g. in a bag), rock chips, particulate filtrate or precipitate; rock
powders.
- An aggregate specimen that is not biogenic or composed of
anthropogenic material fragments.  Examples: loose soil or sediment
(e.g. in a bag), rock chips, particulate filtrate or precipitate; rock
powders.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/genericaggregation
- **Other Properties:**

[]{#boxedcore}

#####  Boxed core
- **Child of**:
 [`Aggregation`](#genericaggregation)
- A collection of core peices that are stored in an individual box.
Typically the box will contain core peices from the same core.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/boxedcore
- **Other Properties:**

[]{#compositesample}

#####  Composite sample
- **Child of**:
 [`Aggregation`](#genericaggregation)
- a sample composed of multiple peices, representative of some
material, or representative of some site. The peices do not all
originate from the same object.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/compositesample
- **Other Properties:**

[]{#chipchannelsample}

######  Chip Channel Sample
- **Child of**:
 [`Composite sample`](#compositesample)
- small chips of rock collected over a specified interval, with the
objective to obtain a representative sample for that interval. Most of
the time chip channel samples are collected in succession along a
sample line which is laid out in advance using a tape.  The freshest
material possible is sampled, preferably chipping directly from
bedrock. Sample intervals are set at a specified width, usually
ranging from 30cm to 7m. Due to the method of sampling, chip channel
samples tend to be rather large (up to 20 pounds for a five foot
interval)
- **Source:**
http://earthsci.org/mineral/rockmin/sampling/sampling.html#Rock%20Sampling
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/chipchannelsample
- **Other Properties:**

[]{#highgradesample}

######  High Grade Sample
- **Child of**:
 [`Composite sample`](#compositesample)
- in mineral exploration, selective pieces of the most highly
mineralized material from a mineralize site, intentionally excluding
less mineralized material. A high grade sample might be collected to
indicate what the best possible values are, or to provide material for
certain types of trace element analyses.
- **Source:**
http://earthsci.org/mineral/rockmin/sampling/sampling.html#Rock%20Sampling
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/highgradesample
- **Other Properties:**

[]{#sitecompositesample}

######  Site composite sample
- **Child of**:
 [`Composite sample`](#compositesample)
- an aggregation of peices of uniform material collected over some
area (generally greater than 2.5m across). These are the ideal
'representative' samples used in mineral exploration. A composite
sample might be collected to determine the background values of trace
elements in a particular type of rock, or to determine if ore grade
mineralization is present over a large area.
- **Source:**
http://earthsci.org/mineral/rockmin/sampling/sampling.html#Rock%20Sampling
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/sitecompositesample
- **Other Properties:**

[]{#corecatcher}

#####  Core catcher
- **Child of**:
 [`Aggregation`](#genericaggregation)
- material recovered from the core catcher of a sedimentary core and
which is treated as a separate section from the core. The core catcher
is a device at the bottom of the core barrel that prevents the core
from sliding out while the barrel is retrieved from the hole.
(http://publications.iodp.org/proceedings/323/102/102_.htm)
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/corecatcher
- **Other Properties:**

[]{#cuttings}

#####  Cuttings
- **Child of**:
 [`Aggregation`](#genericaggregation)
- unconsolidated Earth material produced by the grinding action of a
drill bit during drilling of a borehole.
- **Source:**
http://vocabulary.odm2.org/specimentype/cuttings/
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/cuttings
- **Other Properties:**

[]{#dredge}

#####  Dredge
- **Child of**:
 [`Aggregation`](#genericaggregation)
- an aggregation of material sampled by dragging a collection bucket
(dredge) across the bottom of a water body
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/dredge
- **Other Properties:**

[]{#materialcapturedinfilter}

#####  Material captured in filter
- **Child of**:
 [`Aggregation`](#genericaggregation)
- A material sample captured in filter, for example from a water
sample that was filtered. Must be associated with filter size field.
- **Source:**
https://github.com/ess-dive-community/essdive-sample-id-metadata/blob/master/terms/objectType.md
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/materialcapturedinfilter
- **Other Properties:**

[]{#mechanicalfraction}

#####  Mechanical fraction
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Aggregation`](#genericaggregation)
- defined by sample preparation involving mechanical processing, e.g.
grain size, density, or grain shape separation.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mechanicalfraction
- **Other Properties:**

[]{#mineralseparate}

#####  Mineral separate
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Aggregation`](#genericaggregation)
- an aggregation of particles of the same mineral extracted and
concentrated from a rock.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mineralseparate
- **Other Properties:**

[]{#magneticfraction}

######  Magnetic fraction
- **Child of**:
 [`Mineral separate`](#mineralseparate)
 [`Analytical preparation`](#analyticalpreparation)
- a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/magneticfraction
- **Other Properties:**

[]{#nonmagneticfraction}

######  Non-magnetic fraction
- **Child of**:
 [`Mineral separate`](#mineralseparate)
 [`Analytical preparation`](#analyticalpreparation)
- collection of particles from a crushed rock sample based on their
lack of attraction to a magnet
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/nonmagneticfraction
- **Other Properties:**

[]{#naturalaggregate}

#####  Natural aggregate specimen
- **Child of**:
 [`Aggregation`](#genericaggregation)
- E.g beach sand, soil, river sediment, scoop of regolith.
- Specimen is aggregate of non-consolidated material formed by natural
processes. Particles have not been intentionally modified from the
sampled feature.
- **Alternate labels:**
Aggregate sample
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/naturalaggregate
- **Other Properties:**

[]{#preparedpowder}

#####  Prepared powder
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Aggregation`](#genericaggregation)
- distinguish from particulate in that particulate is sampled as a
micron-size aggregate, whereas this material is ground to a powder for
subsequent analysis; it is a powder as a function of some preparation
process (e.g. chemical precipitation)
- **Alternate labels:**
Powder
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/preparedpowder
- **Other Properties:**

[]{#preparedrockpowder}

######  Prepared rock powder
- **Child of**:
 [`Prepared powder`](#preparedpowder)
- a powder manufactured by pulverizing a rock.
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/preparedrockpowder
- **Other Properties:**

[]{#temgrid}

#####  TEM grid
- **Child of**:
 [`Aggregation`](#genericaggregation)
- FIB sections and microtome slices set onto a small grid for
handling, transport, and analysis using a transmission electron
microscope (TEM). The grid itself can be given a single sample
identifier (similar to how there are multiple grains in a grain
mount). The linkage from the individual samples in the grid to their
parent sample(s) should be documented
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.5-FIB-sections%2C-microtome-slices%2C-atom-probe-tips%2C-TEM-grids, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/temgrid
- **Other Properties:**

[]{#trawl}

#####  Trawl
- **Child of**:
 [`Aggregation`](#genericaggregation)
- an aggregation of biogenic or non-biogenic material extracted from a
water body
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/trawl
- **Other Properties:**

[]{#biologicalmaterialsample}

###  Biological material sample
- **Child of**:
 [`Material sample`](#materialsample)
- Material sample representative of one or more living organisms from
a particular biome context, megascopic or microscopic
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/biologicalmaterialsample
- **Other Properties:**

[]{#biomeaggregation}

####  Biome aggregation sample
- **Child of**:
 [`Any aggregation material sample`](#anyaggregation)
 [`Biological material sample`](#biologicalmaterialsample)
- Material sample that is an aggregation of whole or fragmentary parts
of multiple organisms, microscopic or megascopic, representative of
some sampled feature.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/biomeaggregation
- **Other Properties:**

[]{#bundlebiomeaggregation}

#####  Bundle biome aggregation
- **Child of**:
 [`Biome aggregation sample`](#biomeaggregation)
- Material sample that is an aggregation of whole organisms
representative of some biome.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/bundlebiomeaggregation
- **Other Properties:**

[]{#cellculture}

######  Cell culture
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Bundle biome aggregation`](#bundlebiomeaggregation)
- a collection of cells are grown under controlled conditions,
generally outside of their natural environment
- **Source:**
https://en.wikipedia.org/wiki/Cell_culture
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/cellculture
- **Other Properties:**

[]{#waterbiome}

######  Water biome
- **Child of**:
 [`Bundle biome aggregation`](#bundlebiomeaggregation)
- sample is water and included microorganisms living in the water.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/waterbiome
- **Other Properties:**

[]{#slurrybiomeaggregation}

#####  Slurry biome aggregation
- **Child of**:
 [`Biome aggregation sample`](#biomeaggregation)
- Material sample that consists of mixed organic and inorganic
material, including whole organisms and organism fragments.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/slurrybiomeaggregation
- **Other Properties:**

[]{#soilbiome}

######  Soil biome
- **Child of**:
 [`Slurry biome aggregation`](#slurrybiomeaggregation)
- Sample is soil with included microorganisms and other organism parts
or products. {@en{}
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/soilbiome
- **Other Properties:**

[]{#organismpart}

####  Organism part
- **Child of**:
 [`Biological material sample`](#biologicalmaterialsample)
- Material sample that is part of an organism, e.g. a tissue sample,
plant leaf, flower, bird feather. Include internal parts not composed
of organic material (e.g. teeth, bone), and hard body parts that are
not shed (hoof, horn, tusk, claw).  Hair is tricky, include here for
now.  Does not necessarily imply existance of parent sample. Not
fossilized; generally includes organism parts native to deposits of
Holocene to Recent age.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/organismpart
- **Other Properties:**

[]{#organismproduct}

####  Organism product
- **Child of**:
 [`Biological material sample`](#biologicalmaterialsample)
- Material sample is a thing produced by some organism, generally not
composed of organic material or including biological tissue, e.g.
Shell, antler, egg shell, coral skeleton (organic tissue not
included), fecal matter, cocoon, web.  Consider internal parts not
composed of organic material (e.g. teeth, bone) and hard body parts
that are not shed (hoof, horn, tusk) to be organism parts.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/organismproduct
- **Other Properties:**

[]{#wholeorganism}

####  Whole organism material sample
- **Child of**:
 [`Biological material sample`](#biologicalmaterialsample)
- Material sample consists of the bodies of one or more entire
organisms of the same species, from any kingdom.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/wholeorganism
- **Other Properties:**

[]{#humantissue}

####  Human tissue
- **Child of**:
 [`Biological material sample`](#biologicalmaterialsample)
- Sample is tissue or some body part from a human.
- **Source:**
SESAR sample types
- **Concept URI:** https://w3id.org/sesar/objecttype/humantissue
- **Other Properties:**

[]{#fluidincontainer}

###  Fluid in container
- **Child of**:
 [`Material sample`](#materialsample)
- Material sample is a liquid, gas, or mixed dominantly fluid phase
material that is necessarily inside some container. Fluids might
include minor solid particles. The container is typically human made,
but also includes natural fluid containers, e.g. a fluid inclusion in
a mineral grain.  Fluids might be colloids, foams, gels, or
suspensions. The sample is the fluid substance; fluid samples
collected to analyze the contained biome should be considered 'Biome
aggregation sample'
- Specimen is a container whose contents are liquid, gas, or mixed
dominantly fluid phases that is the actual sample material. Fluid
might include minor solid particles. Container typically human made,
but also includes natural fluid container, e.g. fluid inclusion in a
mineral grain.  Includes colloids, foams, gels, suspensions. The
sample is the fluid substance; fluid samples collected to analyze the
contained biome should be considered 'Biome Aggregation'
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/fluidincontainer
- **Other Properties:**

[]{#directfluidsample}

####  Direct fluid sample
- **Child of**:
 [`Fluid in container`](#fluidincontainer)
- a fluid collected from the sampled feature (e.g. water body,
hydrothermal vent, atmosphere...) with no processing. (e.g.
filtration, addition of preservatives).
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/directfluidsample
- **Other Properties:**

[]{#dissolvedchemicalfraction}

####  Dissolved chemical fraction
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Fluid in container`](#fluidincontainer)
- A fluid concentrating some constituent of interest from a parent
sample. The dissolved constituent is actually the sample material of
interest.
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/dissolvedchemicalfraction
- **Other Properties:**

[]{#eluate}

#####  Eluate
- **Child of**:
 [`Dissolved chemical fraction`](#dissolvedchemicalfraction)
- The fluid product that contains the analyte of interest washed from
a chromatography column
- **Source:**
OSIRIS-Rex Sample types, 
https://en.wikipedia.org/wiki/Elution, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.6-Liquids-and-Washes, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/eluate
- **Other Properties:**

[]{#processedfluidsample}

####  Processed fluid sample
- **Child of**:
 [`Fluid in container`](#fluidincontainer)
- fluid sample that has been processed in some way during or after
collection, e.g. by filtering, addition of preservatives.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/processedfluidsample
- **Other Properties:**

[]{#filtrate}

#####  Filtrate
- **Child of**:
 [`Processed fluid sample`](#processedfluidsample)
- A sample that has gone through a filtration process to separate
solids from fluids (liquids or gases), using a filter medium through
which only the fluid can pass. Must be associated with a filter size.
- **Source:**
https://github.com/ess-dive-community/essdive-sample-id-metadata/blob/master/terms/objectType.md
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/filtrate
- **Other Properties:**

[]{#nonbiologicsolidobject}

###  Non biologic solid object
- **Child of**:
 [`Material sample`](#materialsample)
- Individual solid object, the substance of which is not formed
directly by or part of a living organism
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/nonbiologicsolidobject
- **Other Properties:**

[]{#artifact}

####  Artifact
- **Child of**:
 [`Non biologic solid object`](#nonbiologicsolidobject)
- An object made (manufactured, shaped, modified) by a human being, or
precursor hominid. Include a set of pieces belonging originally to a
single object and treated as a single sample.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/artifact
- **Other Properties:**

[]{#fossil}

####  Fossil
- **Child of**:
 [`Non biologic solid object`](#nonbiologicsolidobject)
- Material sample is the remains or trace of one or more organisms
preserved in rock; includes whole body, body parts (usually bone or
shell), and trace fossils. An organism or organism part becomes a
fossil when it has undergone some fossilization process that entails
physical and chemical changes akin to diagenesis in a sedimentary
rock. Includes trace fossils, which are manifestations of biologic
activity preserved in a rock body (typically sedimentary), without
included preserved body parts.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/fossil
- **Other Properties:**

[]{#othersolidobject}

####  Other solid object
- **Child of**:
 [`Non biologic solid object`](#nonbiologicsolidobject)
- A non-biologic solid object that is not one of the other types.
- Single piece of material not one of the other types.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/othersolidobject
- **Other Properties:**

[]{#dustwipe}

#####  Dust wipe
- **Child of**:
 [`Other solid object`](#othersolidobject)
- a pre-weighed and packaged paper towel (wipe) used to wipe over a
surface to collect particulates from the surface
- **Source:**
https://www.cdc.gov/nceh/lead/docs/publications/Environmental_Sampling.pdf, dust wipe sampling
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/dustwipe
- **Other Properties:**

[]{#glassslidesmear}

#####  Glass slide smear
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Other solid object`](#othersolidobject)
- sample from a cell culture (or other microparticulate suspension)
spread into a thin layer on a glass slide for optical investigation
- **Source:**
https://pubs.usgs.gov/of/2001/of01-041/htmldocs/methods/sslide.htm
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/glassslidesmear
- **Other Properties:**

[]{#peel}

#####  Peel
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Other solid object`](#othersolidobject)
- Acetate peels are made by polishing a planar surface on a sample,
etching it with acid to give it some relief, and then chemically
melting a piece of acetate onto that surface. The acetate is then
pulled off for examination under a microscope. The acetate preserves a
fingerprint of the internal structure of the sample surface. Used in
paleontology to study complex fossils, e.g. bryozoan.
- **Source:**
https://strata.uga.edu/cincy/fauna/bryozoanStudy/acetatePeels.html
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/peel
- **Other Properties:**

[]{#solidmaterialsample}

####  Solid material sample
- **Child of**:
 [`Non biologic solid object`](#nonbiologicsolidobject)
- Individual solid object, not formed directly by or part of a living
organism, that is intended to be representative of some material.
- **Alternate labels:**
Solid material specimen
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/solidmaterialsample
- **Other Properties:**

[]{#core}

#####  Core
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- Cylinder of rock or sediment extracted from within the earth, and
representing the entire sample extracted during a single borehole
drilling event.  Typically using some rotary drilling technology. In
many cases the core is extracted in segments that are 'core sections'.
A core from a single borehole is rarely a continous unbroken object;
commonly parts of the core will break up during drilling or
extraction, leaving gaps or sections that are granular material. Cores
are normally composed of consolidated ('solid') material, but in some
cases loosely consolidated material might be recovered, and considered
sediment or tephra. To be called 'core' the material must be
sufficiently consolidated to maintain a cylindrical shape. A core
hasPart (hasChild) 'Core section'
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/core
- **Other Properties:**

[]{#corehalfround}

#####  Core half round
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- Half-cylindrical peice of consolidated material produced by along-
axis split of a core whole round along a selected diameter .    Has
childOf relation to core section or core, core section, or Core peice
from which is was split
- **Alternate labels:**
Core Section Half
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/corehalfround
- **Other Properties:**

[]{#corepiece}

#####  Core piece
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- A cylindrical peice of consolidated earth material extracted as a
single solid object between breaks in recovery of core from a
borehole. has parent core section
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/corepiece
- **Other Properties:**

[]{#corequarterround}

#####  Core quarter round
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- a partial cylindrical peice of consolidated material created by
along-axis split of a core half round. Has Parent core half round
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/corequarterround
- **Other Properties:**

[]{#coresection}

#####  Core section
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- Segment of a core representing some interval along the well bore.
Child of Core
- **Alternate labels:**
Core Whole Round
- **Source:**
https://www.geosamples.org/vocabularies
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/coresection
- **Other Properties:**

[]{#coresubpeice}

#####  Core subpeice
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- A peice of consolidated material broken from a core peice. has
Parent core peice or core section
- **Source:**
https://www.geosamples.org/vocabularies
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/coresubpeice
- **Other Properties:**

[]{#fiblamella}

#####  FIB lamella
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- very thin sheet of solid material milled from a larger sample using
a focused ion beam. Used for TEM analysis.
- **Source:**
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.5-FIB-sections%2C-microtome-slices%2C-atom-probe-tips%2C-TEM-grids, 
this vocabulary, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/fiblamella
- **Other Properties:**

[]{#individualsolidcube}

#####  Individual solid cube
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- A sample that is a prepared cube of material, intended as a sample
of that material.
- **Source:**
SESAR vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/individualsolidcube
- **Other Properties:**

[]{#individualsolidcylinder}

#####  Individual solid cylinder
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- A cylindrical peice of consolidated material not obtained by
subsurface drilling.  Cores drilled for paleomagnetic analysis are a
common example. Tree ring cores are another...
- **Source:**
SESAR speciment types, ODM 2
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/individualsolidcylinder
- **Other Properties:**

[]{#meteorite}

#####  Meteorite
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- A meteorite is a solid object that originates in interplanetary
space and survives passage through an atmosphere to reach the surface
of a planet or moon.
- **Source:**
https://ares.jsc.nasa.gov/meteorite-falls/what-are-meteorites/, 
https://www.iau.org/static/science/scientific_bodies/commissions/f1/meteordefinitions_approved.pdf, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/meteorite
- **Other Properties:**

[]{#mineralspecimen}

#####  Mineral specimen
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- a solid object consisting of one particular mineral, or several
minerals intended to be representative of one or more of the mineral
species.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mineralspecimen
- **Other Properties:**

[]{#mountedsection}

#####  Sectioned specimen
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- a thin slice of a solid material that has been mounted on a glass
slide for study
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mountedsection
- **Other Properties:**

[]{#thicksection}

######  Thick section
- **Child of**:
 [`Sectioned specimen`](#mountedsection)
- Thick sections are like thin sections, but milled to a greater
thickness. Typcially polished on one or both sides and used for fluid
or melt inclusion studies, Raman analyses, and infrared spectroscopy
analyses, and SEM or electron microprobe. The standard thickness for a
fluid inclusion thick section is 50 micrometers, but thick sections
can be made at any thickness.  Thick sections can be attached to a
glass slide, or can be prepared so that they can be removed from their
mount as a stand-alone slice of rock.
- **Source:**
https://viva.pressbooks.pub/analyticalmethodsingeosciences/chapter/2-2-thin-section-and-thick-section-anatomy/
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/thicksection
- **Other Properties:**

[]{#thinsection}

######  Thin section
- **Child of**:
 [`Sectioned specimen`](#mountedsection)
- thin sliver of rock cut from a sample with a diamond saw and ground
optically flat, and then mounted on a glass slide and ground smooth
using progressively finer abrasive grit until the sample is 30 microns
thick.
- **Source:**
 https://en.wikipedia.org/wiki/Thin_section, 
http://vocabulary.odm2.org/specimentype/thinSection/ , 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/thinsection
- **Other Properties:**

[]{#polishedthinsection}

#######  Polished thin section
- **Child of**:
 [`Thin section`](#thinsection)
- a thin section that has its free surface polished until perfectly
planar and free of pits and scratches. Used for reflected light
petrography and for electron microprobe or SEM investigation.
- **Source:**
http://www.minsocam.org/ammin/AM53/AM53_2070.pdf
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/polishedthinsection
- **Other Properties:**

[]{#ultrathinsection}

######  Ultra thin section
- **Child of**:
 [`Sectioned specimen`](#mountedsection)
- An ordinary thin section that is attached to the glass slide using a
soluble cement such as Canada balsam (soluble in ethanol) to allow
both sides to be worked on. The section is polished on both sides
using a fine diamond paste until it has a thickness in the range of
2-12 microns. This technique has been used to study the microstructure
of very fine-grained carbonate rocks, and also in the preparation of
mineral and rock specimens for transmission electron microscopy.
- **Source:**
http://vocabulary.odm2.org/specimentype/thinSection/  | https://en.wikipedia.org/wiki/Thin_section
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/ultrathinsection
- **Other Properties:**

[]{#pressedpellet}

#####  Pressed pellet
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- a sample prepared by grinding a parent sample to a fine powder,
mixing it with a binder, and pressing the mixture into a die at a
pressure of between 15 and 35 tons to produce a solid disc for
subsequent analysis, typically by X-Ray fluorescence.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/pressedpellet
- **Other Properties:**

[]{#rockhandsample}

#####  Rock hand sample
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- individual peice of rock broken from an outcrop or larger peice of
rock.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/rockhandsample
- **Other Properties:**

[]{#slab}

#####  Slab
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- a relatively planar rock sample, cut from a larger sample to produce
a tabular peice of rock with the irregular outline of the original
sample on the diameter where the cut was made.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/slab
- **Other Properties:**

[]{#uchannelsample}

#####  U-channel sample
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- a rectangular prism of loosely consolidated sediment extracted from
a core segment. has parent core piece or core segment
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/uchannelsample
- **Other Properties:**

[]{#atomprobetip}

#####  Atom probe tip
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- needle-shaped sample milled out of a larger sample with a focused
ion beam (FIB).
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.5-FIB-sections%2C-microtome-slices%2C-atom-probe-tips%2C-TEM-grids, 
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/atomprobetip
- **Other Properties:**

[]{#chip}

#####  Chip
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- Individual solid object intentionally broken off a larger solid
object sample. A Chip must have a documented parent sample.
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138/SAMIS-JSC+Curation+Interface+Control+Document+ICD#6.1-Particles-and-chips, 
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/chip
- **Other Properties:**

[]{#microtomeslice}

#####  Microtome slice
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- Typically from TEM analysis. Slices are commonly deposited in a grid
contain with multiple slices and the grid will be given a single
sample name, not the individual slices within it. The provenance of
the slice from paticle to mounted specimen to slice should be
carefully documented
- A very thin slice cut from a mounted specimen using a mocrotome or
ultramicrotome.
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.5-FIB-sections%2C-microtome-slices%2C-atom-probe-tips%2C-TEM-grids, 
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/microtomeslice
- **Other Properties:**

[]{#mountedspecimen}

#####  Mounted specimen
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- one or more solid objects embedded in a stabilizing matrix,
typically epoxy, metal, or paraffin to allow slicing through the
mounted object(s).
- **Alternate labels:**
Potted butt
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.3-Thin-section%2C-thick-section%2C-grain-mounts-(epoxy%2Fmetal-mounts)%2C-and-potted-butts, 
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/mountedspecimen
- **Other Properties:**

[]{#polishedmountedspecimen}

######  Polished mounted specimen
- **Child of**:
 [`Mounted specimen`](#mountedspecimen)
- Mounted specimen with polished surface exposing mounted material for
analysis
- **Alternate labels:**
Grain mount
- **Source:**
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.3-Thin-section%2C-thick-section%2C-grain-mounts-(epoxy%2Fmetal-mounts)%2C-and-potted-butts, 
this vocabulary, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/polishedmountedspecimen
- **Other Properties:**

[]{#particle}

#####  Particle
- **Child of**:
 [`Solid material sample`](#solidmaterialsample)
- Can also used for small peices broken from a 'Rock hand sample'.
OSIRIS-Rex definition specifies 'competent individual geologic sample
of any size'. 'Competent' interpreted to be equivalent to 'solid', or
'consolidated'.  The definition here is broader in that it includes
materials of any origin, but narrower in that it is restricted to
small objects.
- A small individual solid object that is not one of the other sample
types.
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138/SAMIS-JSC+Curation+Interface+Control+Document+ICD#6.1-Particles-and-chips, 
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/particle
- **Other Properties:**

[]{#researchproduct}

###  Research product
- **Child of**:
 [`Material sample`](#materialsample)
- Material sample is a product of some research workflow, e.g. a thin
section, an XRF pellet, a grain mount, SEM stub, synthetic rock or
mineral ...  In general there should be a link to a parent material
sample from which this was derived.  Might be aggregation (e.g. a
synthetic material powder) or a solid object.
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/researchproduct
- **Other Properties:**

[]{#analyticalpreparation}

####  Analytical preparation
- **Child of**:
 [`Research product`](#researchproduct)
- Material sample is a product of processing required for some
observation procedure, e.g. thin section, XRF bead, SEM stub, rock
powder. If identified separately, this should have a ‘parent’ link to
the original sample
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/analyticalpreparation
- **Other Properties:**

[]{#cellculture}

#####  Cell culture
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Bundle biome aggregation`](#bundlebiomeaggregation)
- a collection of cells are grown under controlled conditions,
generally outside of their natural environment
- **Source:**
https://en.wikipedia.org/wiki/Cell_culture
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/cellculture
- **Other Properties:**

[]{#dissolvedchemicalfraction}

#####  Dissolved chemical fraction
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Fluid in container`](#fluidincontainer)
- A fluid concentrating some constituent of interest from a parent
sample. The dissolved constituent is actually the sample material of
interest.
- **Source:**

- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/dissolvedchemicalfraction
- **Other Properties:**

[]{#eluate}

######  Eluate
- **Child of**:
 [`Dissolved chemical fraction`](#dissolvedchemicalfraction)
- The fluid product that contains the analyte of interest washed from
a chromatography column
- **Source:**
OSIRIS-Rex Sample types, 
https://en.wikipedia.org/wiki/Elution, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.6-Liquids-and-Washes, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/eluate
- **Other Properties:**

[]{#fiblamella}

#####  FIB lamella
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- very thin sheet of solid material milled from a larger sample using
a focused ion beam. Used for TEM analysis.
- **Source:**
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.5-FIB-sections%2C-microtome-slices%2C-atom-probe-tips%2C-TEM-grids, 
this vocabulary, 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/fiblamella
- **Other Properties:**

[]{#glassslidesmear}

#####  Glass slide smear
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Other solid object`](#othersolidobject)
- sample from a cell culture (or other microparticulate suspension)
spread into a thin layer on a glass slide for optical investigation
- **Source:**
https://pubs.usgs.gov/of/2001/of01-041/htmldocs/methods/sslide.htm
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/glassslidesmear
- **Other Properties:**

[]{#individualsolidcube}

#####  Individual solid cube
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- A sample that is a prepared cube of material, intended as a sample
of that material.
- **Source:**
SESAR vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/individualsolidcube
- **Other Properties:**

[]{#magneticfraction}

#####  Magnetic fraction
- **Child of**:
 [`Mineral separate`](#mineralseparate)
 [`Analytical preparation`](#analyticalpreparation)
- a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/magneticfraction
- **Other Properties:**

[]{#mechanicalfraction}

#####  Mechanical fraction
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Aggregation`](#genericaggregation)
- defined by sample preparation involving mechanical processing, e.g.
grain size, density, or grain shape separation.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mechanicalfraction
- **Other Properties:**

[]{#mineralseparate}

#####  Mineral separate
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Aggregation`](#genericaggregation)
- an aggregation of particles of the same mineral extracted and
concentrated from a rock.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mineralseparate
- **Other Properties:**

[]{#magneticfraction}

######  Magnetic fraction
- **Child of**:
 [`Mineral separate`](#mineralseparate)
 [`Analytical preparation`](#analyticalpreparation)
- a collection of particles separated from a crushed rock sample based
on their attraction to a magnet.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/magneticfraction
- **Other Properties:**

[]{#nonmagneticfraction}

######  Non-magnetic fraction
- **Child of**:
 [`Mineral separate`](#mineralseparate)
 [`Analytical preparation`](#analyticalpreparation)
- collection of particles from a crushed rock sample based on their
lack of attraction to a magnet
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/nonmagneticfraction
- **Other Properties:**

[]{#mountedsection}

#####  Sectioned specimen
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- a thin slice of a solid material that has been mounted on a glass
slide for study
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/mountedsection
- **Other Properties:**

[]{#thicksection}

######  Thick section
- **Child of**:
 [`Sectioned specimen`](#mountedsection)
- Thick sections are like thin sections, but milled to a greater
thickness. Typcially polished on one or both sides and used for fluid
or melt inclusion studies, Raman analyses, and infrared spectroscopy
analyses, and SEM or electron microprobe. The standard thickness for a
fluid inclusion thick section is 50 micrometers, but thick sections
can be made at any thickness.  Thick sections can be attached to a
glass slide, or can be prepared so that they can be removed from their
mount as a stand-alone slice of rock.
- **Source:**
https://viva.pressbooks.pub/analyticalmethodsingeosciences/chapter/2-2-thin-section-and-thick-section-anatomy/
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/thicksection
- **Other Properties:**

[]{#thinsection}

######  Thin section
- **Child of**:
 [`Sectioned specimen`](#mountedsection)
- thin sliver of rock cut from a sample with a diamond saw and ground
optically flat, and then mounted on a glass slide and ground smooth
using progressively finer abrasive grit until the sample is 30 microns
thick.
- **Source:**
 https://en.wikipedia.org/wiki/Thin_section, 
http://vocabulary.odm2.org/specimentype/thinSection/ , 
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/thinsection
- **Other Properties:**

[]{#polishedthinsection}

#######  Polished thin section
- **Child of**:
 [`Thin section`](#thinsection)
- a thin section that has its free surface polished until perfectly
planar and free of pits and scratches. Used for reflected light
petrography and for electron microprobe or SEM investigation.
- **Source:**
http://www.minsocam.org/ammin/AM53/AM53_2070.pdf
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/polishedthinsection
- **Other Properties:**

[]{#ultrathinsection}

######  Ultra thin section
- **Child of**:
 [`Sectioned specimen`](#mountedsection)
- An ordinary thin section that is attached to the glass slide using a
soluble cement such as Canada balsam (soluble in ethanol) to allow
both sides to be worked on. The section is polished on both sides
using a fine diamond paste until it has a thickness in the range of
2-12 microns. This technique has been used to study the microstructure
of very fine-grained carbonate rocks, and also in the preparation of
mineral and rock specimens for transmission electron microscopy.
- **Source:**
http://vocabulary.odm2.org/specimentype/thinSection/  | https://en.wikipedia.org/wiki/Thin_section
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/ultrathinsection
- **Other Properties:**

[]{#nonmagneticfraction}

#####  Non-magnetic fraction
- **Child of**:
 [`Mineral separate`](#mineralseparate)
 [`Analytical preparation`](#analyticalpreparation)
- collection of particles from a crushed rock sample based on their
lack of attraction to a magnet
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/nonmagneticfraction
- **Other Properties:**

[]{#peel}

#####  Peel
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Other solid object`](#othersolidobject)
- Acetate peels are made by polishing a planar surface on a sample,
etching it with acid to give it some relief, and then chemically
melting a piece of acetate onto that surface. The acetate is then
pulled off for examination under a microscope. The acetate preserves a
fingerprint of the internal structure of the sample surface. Used in
paleontology to study complex fossils, e.g. bryozoan.
- **Source:**
https://strata.uga.edu/cincy/fauna/bryozoanStudy/acetatePeels.html
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/peel
- **Other Properties:**

[]{#preparedpowder}

#####  Prepared powder
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Aggregation`](#genericaggregation)
- distinguish from particulate in that particulate is sampled as a
micron-size aggregate, whereas this material is ground to a powder for
subsequent analysis; it is a powder as a function of some preparation
process (e.g. chemical precipitation)
- **Alternate labels:**
Powder
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/preparedpowder
- **Other Properties:**

[]{#preparedrockpowder}

######  Prepared rock powder
- **Child of**:
 [`Prepared powder`](#preparedpowder)
- a powder manufactured by pulverizing a rock.
- **Source:**
https://www.geosamples.org/vocabularies/sample-type-object
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/preparedrockpowder
- **Other Properties:**

[]{#pressedpellet}

#####  Pressed pellet
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- a sample prepared by grinding a parent sample to a fine powder,
mixing it with a binder, and pressing the mixture into a die at a
pressure of between 15 and 35 tons to produce a solid disc for
subsequent analysis, typically by X-Ray fluorescence.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/pressedpellet
- **Other Properties:**

[]{#residualmaterial}

#####  Residual material
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
- Sample is material remaining after processing to extract some other
components of interest from the sample.
- **Alternate labels:**
Residue
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/residualmaterial
- **Other Properties:**

[]{#slab}

#####  Slab
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- a relatively planar rock sample, cut from a larger sample to produce
a tabular peice of rock with the irregular outline of the original
sample on the diameter where the cut was made.
- **Source:**
this vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/esmaterialsample/slab
- **Other Properties:**

[]{#atomprobetip}

#####  Atom probe tip
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
 [`Solid material sample`](#solidmaterialsample)
- needle-shaped sample milled out of a larger sample with a focused
ion beam (FIB).
- **Source:**
OSIRIS-Rex Sample types, 
https://osiris-rex.atlassian.net/wiki/spaces/UTDMP/pages/410288138#6.5-FIB-sections%2C-microtome-slices%2C-atom-probe-tips%2C-TEM-grids, 
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/atomprobetip
- **Other Properties:**

[]{#squeezecake}

#####  Squeeze cake
- **Child of**:
 [`Analytical preparation`](#analyticalpreparation)
- Small piece of whole round core after pore water has been extracted.
A 5cm – 15cm piece of core is put in a titanium container and sealed
with a fitted piston. The container is then placed on a hydraulic
press and pressed under up to 35,000 lbs to extract the pore water.
Squeezing destroys the sediment structure
- **Source:**
https://joidesresolution.org/let-them-squeeze-cake-contributor-rachael-gray/
- **Concept URI:** https://w3id.org/sesar/objecttype/squeezecake
- **Other Properties:**

[]{#experimentalproduct}

####  Experiment product
- **Child of**:
 [`Research product`](#researchproduct)
- Material sample that is the product of an experimental procedure
(e.g. synthetic material)
- **Concept URI:** https://w3id.org/isample/vocabulary/materialsampleobjecttype/experimentalproduct
- **Other Properties:**


[]{#samplingfeature}

##  Sampling feature
- An entity that is the locus of sample collection.
- **Source:**
SESAR sample types, 
https://en.wikipedia.org/wiki/Observations_and_Measurements#Sampling_features, 
- **Concept URI:** https://w3id.org/sesar/objecttype/samplingfeature
- **Other Properties:**

[]{#hole}

###  Hole
- **Child of**:
 [`Sampling feature`](#samplingfeature)
- A sampling feature that is drilled or dug into the Earth surface to
obtain material from the subsurface. Boreholes, soil pits, mine shafts
are examples.
- **Source:**
SESAR sample types
- **Concept URI:** https://w3id.org/sesar/objecttype/hole
- **Other Properties:**

[]{#site}

###  Sampling site
- **Child of**:
 [`Sampling feature`](#samplingfeature)
- A registered location at which samples were collected or
observations occurred.
- **Source:**
SESAR sample types
- **Concept URI:** https://w3id.org/sesar/objecttype/site
- **Other Properties:**

[]{#terrestrialsection}

###  Terrestrial section
- **Child of**:
 [`Sampling feature`](#samplingfeature)
- sampling feature is a section of the near-surface Earth, generally
in the critical zone.
- **Source:**
SESAR sample types
- **Concept URI:** https://w3id.org/sesar/objecttype/terrestrialsection
- **Other Properties:**


[]{#anysampledfeature}

##  `https://w3id.org/isample/vocabulary/sampledfeature/anysampledfeature`
- **Concept URI:** https://w3id.org/isample/vocabulary/sampledfeature/anysampledfeature
- **Other Properties:**


