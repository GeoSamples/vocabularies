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

[]{#SESAR-Rockandsedimentmaterialsvocabulary}

# **Concept scheme:** SESAR - Rock and sediment materials vocabulary

Vocabulary last modified:  2024-09-26

subtitle: 
  Rock and sediment categories for SESAR materialType classification. Extends the iSamples Earth and Environment rock and sediment extension, which extends the base iSamples Material Type vocabulary.

Namespace: 
[`https://w3id.org/sesar/rocksediment/0.1/rocksedimentvocabulary`](https://w3id.org/sesar/rocksediment/0.1/rocksedimentvocabulary)

**History**

* 2024-08-19 SMR generate vocabulary by merging with GSO Rock_Material vocabulary .

- [Rock or sediment](#rockorsediment)
    - [Breccia](#breccia)
    - [Rock](#rock)
        - [Aphanite](#aphanite)
        - [Breccia](#breccia)
        - [Fault related material](#fault_related_material)
            - [cataclasite series](#cataclasite_series)
            - [mylonitic rock](#mylonitic_rock)
                - [phyllonite](#phyllonite)
            - [breccia gouge series](#breccia_gouge_series)
        - [fragmental igneous rock](#fragmental_igneous_rock)
            - [pyroclastic rock](#pyroclastic_rock)
                - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
        - [Igneous rock](#igneous_rock)
            - [acidic igneous rock](#acidic_igneous_rock)
                - [dacite](#dacite)
                - [granitoid](#granitoid)
                    - [alkali feldspar granite](#alkali_feldspar_granite)
                    - [granite](#granite)
                        - [monzogranite](#monzogranite)
                        - [syenogranite](#syenogranite)
                    - [granodiorite](#granodiorite)
                    - [tonalite](#tonalite)
                - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                - [rhyolitoid](#rhyolitoid)
                    - [alkali feldspar rhyolite](#alkali_feldspar_rhyolite)
                    - [rhyolite](#rhyolite)
            - [basic igneous rock](#basic_igneous_rock)
                - [basalt](#basalt)
                    - [alkali olivine basalt](#alkali-olivine_basalt)
                    - [tholeiitic basalt](#tholeiitic_basalt)
                - [gabbroic rock](#gabbroic_rock)
                    - [foid bearing gabbro](#foid_bearing_gabbro)
                    - [gabbro](#gabbro)
                    - [quartz gabbro](#quartz_gabbro)
            - [doleritic rock](#doleritic_rock)
            - [exotic composition igneous rock](#exotic_composition_igneous_rock)
                - [carbonatite](#carbonatite)
                - [exotic alkaline rock](#exotic_alkaline_rock)
                - [kalsilitic and melilitic rocks](#kalsilitic_and_melilitic_rock)
            - [fine grained igneous rock](#fine_grained_igneous_rock)
                - [andesite](#andesite)
                    - [boninite](#boninite)
                - [basalt](#basalt)
                    - [alkali olivine basalt](#alkali-olivine_basalt)
                    - [tholeiitic basalt](#tholeiitic_basalt)
                - [dacite](#dacite)
                - [foiditoid](#foiditoid)
                    - [basanitic foidite](#basanitic_foidite)
                    - [foidite](#foidite)
                    - [phonolitic foidite](#phonolitic_foidite)
                    - [tephritic foidite](#tephritic_foidite)
                - [high magnesium fine grained igneous rock](#high_magnesium_fine_grained_igneous_rock)
                    - [boninite](#boninite)
                    - [komatiitic rock](#komatiitic_rock)
                - [phonolitoid](#phonolitoid)
                    - [phonolite](#phonolilte)
                    - [tephritic phonolite](#tephritic_phonolite)
                - [rhyolitoid](#rhyolitoid)
                    - [alkali feldspar rhyolite](#alkali_feldspar_rhyolite)
                    - [rhyolite](#rhyolite)
                - [tephritoid](#tephritoid)
                    - [basanite](#basanite)
                    - [phonolitic basanite](#phonolitic_basanite)
                    - [phonolitic tephrite](#phonolitic_tephrite)
                    - [tephrite](#tephrite)
                - [trachytoid](#trachytoid)
                    - [alkali feldspar trachytic rock](#alkali_feldspar_trachytic_rock)
                        - [alkali feldspar trachyte](#alkali_feldspar_trachyte)
                        - [foid bearing alkali feldspar trachyte](#foid_bearing_alkali_feldspar_trachyte)
                        - [quartz alkali feldspar trachyte](#quartz_alkali_feldspar_trachyte)
                    - [latitic rock](#latitic_rock)
                        - [foid bearing latite](#foid_bearing_latite)
                        - [latite](#latite)
                        - [quartz latite](#quartz_latite)
                    - [trachytic rock](#trachytic_rock)
                        - [foid bearing trachyte](#foid_bearing_trachyte)
                        - [quartz trachyte](#quartz_trachyte)
                        - [trachyte](#trachyte)
            - [fragmental igneous rock](#fragmental_igneous_rock)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
            - [glass rich igneous rock](#glass_rich_igneous_rock)
                - [glassy igneous rock](#glassy_igneous_rock)
            - [hypabyssal intrusive rock](#hypabyssal_intrusive_rock)
            - [intermediate composition igneous rock](#intermediate_composition_igneous_rock)
                - [andesite](#andesite)
                    - [boninite](#boninite)
                - [dioritoid](#dioritoid)
                    - [dioritic rock](#dioritic_rock)
                        - [diorite](#diorite)
                        - [foid bearing diorite](#foid_bearing_diorite)
                        - [quartz diorite](#quartz_diorite)
                    - [monzodioritic rock](#monzodioritic_rock)
                        - [foid bearing monzodiorite](#foid_bearing_monzodiorite)
                        - [monzodiorite](#monzodiorite)
                        - [quartz monzodiorite](#quartz_monzodiorite)
            - [phaneritic igneous rock](#phaneritic_igneous_rock)
                - [anorthositic rock](#anorthositic_rock)
                    - [anorthosite](#anorthosite)
                    - [foid bearing anorthosite](#foid_bearing_anorthosite)
                    - [quartz anorthosite](#quartz_anorthosite)
                - [aplite](#aplite)
                - [dioritoid](#dioritoid)
                    - [dioritic rock](#dioritic_rock)
                        - [diorite](#diorite)
                        - [foid bearing diorite](#foid_bearing_diorite)
                        - [quartz diorite](#quartz_diorite)
                    - [monzodioritic rock](#monzodioritic_rock)
                        - [foid bearing monzodiorite](#foid_bearing_monzodiorite)
                        - [monzodiorite](#monzodiorite)
                        - [quartz monzodiorite](#quartz_monzodiorite)
                - [foid dioritoid](#foid_dioritoid)
                    - [foid diorite](#foid_diorite)
                    - [foid monzodiorite](#foid_monzodiorite)
                - [foid gabbroid](#foid_gabbroid)
                    - [foid gabbro](#foid_gabbro)
                    - [foid monzogabbro](#foid_monzogabbro)
                - [foid syenitoid](#foid_syenitoid)
                    - [foid monzosyenite](#foid_monzosyenite)
                    - [foid syenite](#foid_syenite)
                - [foidolite](#foidolite)
                - [gabbroid](#gabbroid)
                    - [gabbroic rock](#gabbroic_rock)
                        - [foid bearing gabbro](#foid_bearing_gabbro)
                        - [gabbro](#gabbro)
                        - [quartz gabbro](#quartz_gabbro)
                    - [monzogabbroic rock](#monzogabbroic_rock)
                        - [foid bearing monzogabbro](#foid_bearing_monzogabbro)
                        - [monzogabbro](#monzogabbro)
                        - [quartz monzogabbro](#quartz_monzogabbro)
                - [granitoid](#granitoid)
                    - [alkali feldspar granite](#alkali_feldspar_granite)
                    - [granite](#granite)
                        - [monzogranite](#monzogranite)
                        - [syenogranite](#syenogranite)
                    - [granodiorite](#granodiorite)
                    - [tonalite](#tonalite)
                - [hornblendite](#hornblendite)
                - [pegmatite](#pegmatite)
                - [peridotite](#peridotite)
                - [pyroxenite](#pyroxenite)
                - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                - [syenitoid](#syenitoid)
                    - [alkali feldspar syenitic rock](#alkali_feldspar_syenitic_rock)
                        - [alkali feldspar syenite](#alkali_feldspar_syenite)
                        - [foid bearing alkali feldspar syenite](#foid_bearing_alkali_feldspar_syenite)
                        - [quartz alkali feldspar syenite](#quartz_alkali_feldspar_syenite)
                    - [monzonitic rock](#monzonitic_rock)
                        - [foid bearing monzonite](#foid_bearing_monzonite)
                        - [monzonite](#monzonite)
                        - [quartz monzonite](#quartz_monzonite)
                    - [syenitic rock](#syenitic_rock)
                        - [foid bearing syenite](#foid_bearing_syenite)
                        - [quartz syenite](#quartz_syenite)
                        - [syenite](#syenite)
            - [plutonic rock](#plutonic_igneous_rock)
            - [porphyry](#porphyry)
            - [ultrabasic igneous rock](#ultrabasic_igneous_rock)
            - [ultramafic igneous rock](#ultramafic_igneous_rock)
                - [hornblendite](#hornblendite)
                - [peridotite](#peridotite)
                - [pyroxenite](#pyroxenite)
                - [komatiitic rock](#komatiitic_rock)
            - [Volcanic rock](#volcanic_rock)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
                - [Lava](#lava)
        - [Impact generated material](#impact_generated_material)
        - [Massive sulphide](#massive_sulphide)
            - [Hydrothermal Massive Sulphide](#hydrothermal_massive_sulphide)
            - [Sedimentary Massive Sulphide](#sedimentary_massive_sulphide)
        - [Metamorphic rock](#metamorphic_rock)
            - [amphibolite](#amphibolite)
            - [Argillite ](#argillite)
            - [calc silicate metamorphic rock](#calcsilicate_metamorphic_rock)
            - [chlorite actinolite epidote metamorphic rock](#chlorite_actinolite_epidote_metamorphic_rock)
            - [eclogite](#eclogite)
            - [foliated metamorphic rock](#foliated_metamorphic_rock)
                - [mylonitic rock](#mylonitic_rock)
                    - [phyllonite](#phyllonite)
                - [gneiss](#gneiss)
                    - [orthogneiss](#orthogneiss)
                    - [paragneiss](#paragneiss)
                - [phyllite](#phyllite)
                - [schist](#schist)
                    - [mica schist](#mica_schist)
                - [slate](#slate)
            - [glaucophane lawsonite epidote metamorphic rock](#glaucophane_lawsonite_epidote_metamorphic_rock)
            - [granofels](#granofels)
                - [hornfels](#hornfels)
            - [granulite](#granulite)
            - [marble](#marble)
            - [metaplutonic rock](#metaplutonic_rock)
            - [metasedimentary rock](#metasedimentary_rock)
            - [metavolcanic rock](#metavolcanic_rock)
            - [migmatite](#migmatite)
            - [quartzite](#quartzite)
            - [serpentinite](#serpentinite)
        - [metasomatic rock](#metasomatic_rock)
            - [Altered, type not specified ](#altered_rock)
                - [advanced argillic altered rock](#advanced_argillic_altered_rock)
                - [albitic altered rock](#albitic_altered_rock)
                - [alunitic altered rock](#alunitic_altered_rock)
                - [argillic altered rock](#argillic_altered_rock)
                - [calcsilicate altered rock](#calcsilicate_altered_rock)
                - [carbonate altered rock](#carbonate_altered_rock)
                - [chloritic altered rock](#chloritic_altered_rock)
                - [deuteric altered rock](#deuteric_altered_rock)
                - [epidote altered rock](#epidote_altered_rock)
                - [hematitic altered rock](#hematitic_altered_rock)
                - [kaolinitic altered rock](#kaolinitic_altered_rock)
                - [phyllic altered rock](#phyllic_altered_rock)
                - [potassic altered rock](#potassic_altered_rock)
                - [propylitic altered rock](#propylitic_altered_rock)
                - [pyritic altered rock](#pyritic_altered_rock)
                - [saussuritised rock](#saussuritised_rock)
                - [sericitic altered rock](#sericitic_altered_rock)
                - [serpentinised rock](#serpentinised_rock)
                - [silicificed rock](#silicified_rock)
                - [uralitised rock](#uralitised_rock)
                - [zeolitic altered rock](#zeolitic_altered_rock)
            - [Greisen](#greisen)
            - [Hydrothermal Massive Sulphide](#hydrothermal_massive_sulphide)
            - [skarn](#skarn)
            - [spilite](#spilite)
        - [Sedimentary rock](#sedimentary_rock)
            - [carbonate sedimentary rock](#carbonate_sedimentary_rock)
                - [boundstone](#boundstone)
                - [calcareous carbonate sedimentary rock](#calcareous_carbonate_sedimentary_rock)
                    - [impure limestone](#impure_limestone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
                - [carbonate mudstone](#carbonate_mudstone)
                - [carbonate wackestone](#carbonate_wackestone)
                - [crystalline carbonate](#crystalline_carbonate)
                - [dolomitic or magnesian sedimentary rock](#dolomitic_or_magnesian_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [impure dolomite](#impure_dolostone)
                - [framestone](#framestone)
                - [grainstone](#grainstone)
                - [impure carbonate sedimentary rock](#impure_carbonate_sedimentary_rock)
                    - [impure dolomite](#impure_dolostone)
                    - [impure limestone](#impure_limestone)
                - [packstone](#packstone)
                - [pure carbonate sedimentary rock](#pure_carbonate_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
                    - [pure carbonate mudstone](#pure_carbonate_mudstone)
            - [clastic sedimentary rock](#clastic_sedimentary_rock)
                - [diamictite](#diamictite)
                - [conglomerate](#clastic_conglomerate)
                - [mudstone](#clastic_mudstone)
                    - [claystone](#claystone)
                    - [shale](#shale)
                    - [siltstone](#siltstone)
                - [sandstone](#clastic_sandstone)
                    - [arenit](#arenite)
                    - [wacke](#wacke)
            - [generic conglomerate](#generic_conglomerate)
                - [conglomerate](#clastic_conglomerate)
            - [generic mudstone](#generic_mudstone)
                - [carbonate mudstone](#carbonate_mudstone)
                - [carbonate rich mudstone](#carbonate_rich_mudstone)
                - [mudstone](#clastic_mudstone)
                    - [claystone](#claystone)
                    - [shale](#shale)
                    - [siltstone](#siltstone)
                - [organic bearing mudstone](#organic_bearing_mudstone)
                - [pure carbonate mudstone](#pure_carbonate_mudstone)
                - [silicate mudstone](#silicate_mudstone)
            - [Generic sandstone](#generic_sandstone)
                - [sandstone](#clastic_sandstone)
                    - [arenit](#arenite)
                    - [wacke](#wacke)
            - [hybrid sedimentary rock](#hybrid_sedimentary_rock)
            - [iron rich sedimentary rock](#iron_rich_sedimentary_rock)
            - [non clastic siliceous sedimentary rock](#non_clastic_siliceous_sedimentary_rock)
                - [biogenic silica sedimentary rock](#biogenic_silica_sedimentary_rock)
            - [organic rich sedimentary rock](#organic_rich_sedimentary_rock)
                - [coal](#coal)
                    - [anthracite](#anthracite_coal)
                    - [bituminous coal](#bituminous_coal)
                    - [lignite](#lignite)
            - [phosphorite](#phosphorite)
        - [Tuffite](#tuffite)
        - [residual material](#residual_material)
        - [Composite genesis rock](#composite_genesis_rock)
            - [cataclasite series](#cataclasite_series)
            - [Metamorphic rock](#metamorphic_rock)
                - [amphibolite](#amphibolite)
                - [Argillite ](#argillite)
                - [calc silicate metamorphic rock](#calcsilicate_metamorphic_rock)
                - [chlorite actinolite epidote metamorphic rock](#chlorite_actinolite_epidote_metamorphic_rock)
                - [eclogite](#eclogite)
                - [foliated metamorphic rock](#foliated_metamorphic_rock)
                    - [mylonitic rock](#mylonitic_rock)
                        - [phyllonite](#phyllonite)
                    - [gneiss](#gneiss)
                        - [orthogneiss](#orthogneiss)
                        - [paragneiss](#paragneiss)
                    - [phyllite](#phyllite)
                    - [schist](#schist)
                        - [mica schist](#mica_schist)
                    - [slate](#slate)
                - [glaucophane lawsonite epidote metamorphic rock](#glaucophane_lawsonite_epidote_metamorphic_rock)
                - [granofels](#granofels)
                    - [hornfels](#hornfels)
                - [granulite](#granulite)
                - [marble](#marble)
                - [metaplutonic rock](#metaplutonic_rock)
                - [metasedimentary rock](#metasedimentary_rock)
                - [metavolcanic rock](#metavolcanic_rock)
                - [migmatite](#migmatite)
                - [quartzite](#quartzite)
                - [serpentinite](#serpentinite)
            - [metasomatic rock](#metasomatic_rock)
                - [Altered, type not specified ](#altered_rock)
                    - [advanced argillic altered rock](#advanced_argillic_altered_rock)
                    - [albitic altered rock](#albitic_altered_rock)
                    - [alunitic altered rock](#alunitic_altered_rock)
                    - [argillic altered rock](#argillic_altered_rock)
                    - [calcsilicate altered rock](#calcsilicate_altered_rock)
                    - [carbonate altered rock](#carbonate_altered_rock)
                    - [chloritic altered rock](#chloritic_altered_rock)
                    - [deuteric altered rock](#deuteric_altered_rock)
                    - [epidote altered rock](#epidote_altered_rock)
                    - [hematitic altered rock](#hematitic_altered_rock)
                    - [kaolinitic altered rock](#kaolinitic_altered_rock)
                    - [phyllic altered rock](#phyllic_altered_rock)
                    - [potassic altered rock](#potassic_altered_rock)
                    - [propylitic altered rock](#propylitic_altered_rock)
                    - [pyritic altered rock](#pyritic_altered_rock)
                    - [saussuritised rock](#saussuritised_rock)
                    - [sericitic altered rock](#sericitic_altered_rock)
                    - [serpentinised rock](#serpentinised_rock)
                    - [silicificed rock](#silicified_rock)
                    - [uralitised rock](#uralitised_rock)
                    - [zeolitic altered rock](#zeolitic_altered_rock)
                - [Greisen](#greisen)
                - [Hydrothermal Massive Sulphide](#hydrothermal_massive_sulphide)
                - [skarn](#skarn)
                - [spilite](#spilite)
            - [Duricrust](#duricrust)
    - [Composite genesis material](#composite_genesis_material)
        - [Fault related material](#fault_related_material)
            - [cataclasite series](#cataclasite_series)
            - [mylonitic rock](#mylonitic_rock)
                - [phyllonite](#phyllonite)
            - [breccia gouge series](#breccia_gouge_series)
        - [Impact generated material](#impact_generated_material)
        - [Composite genesis rock](#composite_genesis_rock)
            - [cataclasite series](#cataclasite_series)
            - [Metamorphic rock](#metamorphic_rock)
                - [amphibolite](#amphibolite)
                - [Argillite ](#argillite)
                - [calc silicate metamorphic rock](#calcsilicate_metamorphic_rock)
                - [chlorite actinolite epidote metamorphic rock](#chlorite_actinolite_epidote_metamorphic_rock)
                - [eclogite](#eclogite)
                - [foliated metamorphic rock](#foliated_metamorphic_rock)
                    - [mylonitic rock](#mylonitic_rock)
                        - [phyllonite](#phyllonite)
                    - [gneiss](#gneiss)
                        - [orthogneiss](#orthogneiss)
                        - [paragneiss](#paragneiss)
                    - [phyllite](#phyllite)
                    - [schist](#schist)
                        - [mica schist](#mica_schist)
                    - [slate](#slate)
                - [glaucophane lawsonite epidote metamorphic rock](#glaucophane_lawsonite_epidote_metamorphic_rock)
                - [granofels](#granofels)
                    - [hornfels](#hornfels)
                - [granulite](#granulite)
                - [marble](#marble)
                - [metaplutonic rock](#metaplutonic_rock)
                - [metasedimentary rock](#metasedimentary_rock)
                - [metavolcanic rock](#metavolcanic_rock)
                - [migmatite](#migmatite)
                - [quartzite](#quartzite)
                - [serpentinite](#serpentinite)
            - [metasomatic rock](#metasomatic_rock)
                - [Altered, type not specified ](#altered_rock)
                    - [advanced argillic altered rock](#advanced_argillic_altered_rock)
                    - [albitic altered rock](#albitic_altered_rock)
                    - [alunitic altered rock](#alunitic_altered_rock)
                    - [argillic altered rock](#argillic_altered_rock)
                    - [calcsilicate altered rock](#calcsilicate_altered_rock)
                    - [carbonate altered rock](#carbonate_altered_rock)
                    - [chloritic altered rock](#chloritic_altered_rock)
                    - [deuteric altered rock](#deuteric_altered_rock)
                    - [epidote altered rock](#epidote_altered_rock)
                    - [hematitic altered rock](#hematitic_altered_rock)
                    - [kaolinitic altered rock](#kaolinitic_altered_rock)
                    - [phyllic altered rock](#phyllic_altered_rock)
                    - [potassic altered rock](#potassic_altered_rock)
                    - [propylitic altered rock](#propylitic_altered_rock)
                    - [pyritic altered rock](#pyritic_altered_rock)
                    - [saussuritised rock](#saussuritised_rock)
                    - [sericitic altered rock](#sericitic_altered_rock)
                    - [serpentinised rock](#serpentinised_rock)
                    - [silicificed rock](#silicified_rock)
                    - [uralitised rock](#uralitised_rock)
                    - [zeolitic altered rock](#zeolitic_altered_rock)
                - [Greisen](#greisen)
                - [Hydrothermal Massive Sulphide](#hydrothermal_massive_sulphide)
                - [skarn](#skarn)
                - [spilite](#spilite)
            - [Duricrust](#duricrust)
        - [material formed in surficial environment](#material_formed_in_surficial_environment)
            - [residual material](#residual_material)
            - [Soil](#soil)
            - [bauxite](#bauxite)
            - [Duricrust](#duricrust)
    - [Igneous material](#igneous_material)
        - [Igneous rock](#igneous_rock)
            - [acidic igneous rock](#acidic_igneous_rock)
                - [dacite](#dacite)
                - [granitoid](#granitoid)
                    - [alkali feldspar granite](#alkali_feldspar_granite)
                    - [granite](#granite)
                        - [monzogranite](#monzogranite)
                        - [syenogranite](#syenogranite)
                    - [granodiorite](#granodiorite)
                    - [tonalite](#tonalite)
                - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                - [rhyolitoid](#rhyolitoid)
                    - [alkali feldspar rhyolite](#alkali_feldspar_rhyolite)
                    - [rhyolite](#rhyolite)
            - [basic igneous rock](#basic_igneous_rock)
                - [basalt](#basalt)
                    - [alkali olivine basalt](#alkali-olivine_basalt)
                    - [tholeiitic basalt](#tholeiitic_basalt)
                - [gabbroic rock](#gabbroic_rock)
                    - [foid bearing gabbro](#foid_bearing_gabbro)
                    - [gabbro](#gabbro)
                    - [quartz gabbro](#quartz_gabbro)
            - [doleritic rock](#doleritic_rock)
            - [exotic composition igneous rock](#exotic_composition_igneous_rock)
                - [carbonatite](#carbonatite)
                - [exotic alkaline rock](#exotic_alkaline_rock)
                - [kalsilitic and melilitic rocks](#kalsilitic_and_melilitic_rock)
            - [fine grained igneous rock](#fine_grained_igneous_rock)
                - [andesite](#andesite)
                    - [boninite](#boninite)
                - [basalt](#basalt)
                    - [alkali olivine basalt](#alkali-olivine_basalt)
                    - [tholeiitic basalt](#tholeiitic_basalt)
                - [dacite](#dacite)
                - [foiditoid](#foiditoid)
                    - [basanitic foidite](#basanitic_foidite)
                    - [foidite](#foidite)
                    - [phonolitic foidite](#phonolitic_foidite)
                    - [tephritic foidite](#tephritic_foidite)
                - [high magnesium fine grained igneous rock](#high_magnesium_fine_grained_igneous_rock)
                    - [boninite](#boninite)
                    - [komatiitic rock](#komatiitic_rock)
                - [phonolitoid](#phonolitoid)
                    - [phonolite](#phonolilte)
                    - [tephritic phonolite](#tephritic_phonolite)
                - [rhyolitoid](#rhyolitoid)
                    - [alkali feldspar rhyolite](#alkali_feldspar_rhyolite)
                    - [rhyolite](#rhyolite)
                - [tephritoid](#tephritoid)
                    - [basanite](#basanite)
                    - [phonolitic basanite](#phonolitic_basanite)
                    - [phonolitic tephrite](#phonolitic_tephrite)
                    - [tephrite](#tephrite)
                - [trachytoid](#trachytoid)
                    - [alkali feldspar trachytic rock](#alkali_feldspar_trachytic_rock)
                        - [alkali feldspar trachyte](#alkali_feldspar_trachyte)
                        - [foid bearing alkali feldspar trachyte](#foid_bearing_alkali_feldspar_trachyte)
                        - [quartz alkali feldspar trachyte](#quartz_alkali_feldspar_trachyte)
                    - [latitic rock](#latitic_rock)
                        - [foid bearing latite](#foid_bearing_latite)
                        - [latite](#latite)
                        - [quartz latite](#quartz_latite)
                    - [trachytic rock](#trachytic_rock)
                        - [foid bearing trachyte](#foid_bearing_trachyte)
                        - [quartz trachyte](#quartz_trachyte)
                        - [trachyte](#trachyte)
            - [fragmental igneous rock](#fragmental_igneous_rock)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
            - [glass rich igneous rock](#glass_rich_igneous_rock)
                - [glassy igneous rock](#glassy_igneous_rock)
            - [hypabyssal intrusive rock](#hypabyssal_intrusive_rock)
            - [intermediate composition igneous rock](#intermediate_composition_igneous_rock)
                - [andesite](#andesite)
                    - [boninite](#boninite)
                - [dioritoid](#dioritoid)
                    - [dioritic rock](#dioritic_rock)
                        - [diorite](#diorite)
                        - [foid bearing diorite](#foid_bearing_diorite)
                        - [quartz diorite](#quartz_diorite)
                    - [monzodioritic rock](#monzodioritic_rock)
                        - [foid bearing monzodiorite](#foid_bearing_monzodiorite)
                        - [monzodiorite](#monzodiorite)
                        - [quartz monzodiorite](#quartz_monzodiorite)
            - [phaneritic igneous rock](#phaneritic_igneous_rock)
                - [anorthositic rock](#anorthositic_rock)
                    - [anorthosite](#anorthosite)
                    - [foid bearing anorthosite](#foid_bearing_anorthosite)
                    - [quartz anorthosite](#quartz_anorthosite)
                - [aplite](#aplite)
                - [dioritoid](#dioritoid)
                    - [dioritic rock](#dioritic_rock)
                        - [diorite](#diorite)
                        - [foid bearing diorite](#foid_bearing_diorite)
                        - [quartz diorite](#quartz_diorite)
                    - [monzodioritic rock](#monzodioritic_rock)
                        - [foid bearing monzodiorite](#foid_bearing_monzodiorite)
                        - [monzodiorite](#monzodiorite)
                        - [quartz monzodiorite](#quartz_monzodiorite)
                - [foid dioritoid](#foid_dioritoid)
                    - [foid diorite](#foid_diorite)
                    - [foid monzodiorite](#foid_monzodiorite)
                - [foid gabbroid](#foid_gabbroid)
                    - [foid gabbro](#foid_gabbro)
                    - [foid monzogabbro](#foid_monzogabbro)
                - [foid syenitoid](#foid_syenitoid)
                    - [foid monzosyenite](#foid_monzosyenite)
                    - [foid syenite](#foid_syenite)
                - [foidolite](#foidolite)
                - [gabbroid](#gabbroid)
                    - [gabbroic rock](#gabbroic_rock)
                        - [foid bearing gabbro](#foid_bearing_gabbro)
                        - [gabbro](#gabbro)
                        - [quartz gabbro](#quartz_gabbro)
                    - [monzogabbroic rock](#monzogabbroic_rock)
                        - [foid bearing monzogabbro](#foid_bearing_monzogabbro)
                        - [monzogabbro](#monzogabbro)
                        - [quartz monzogabbro](#quartz_monzogabbro)
                - [granitoid](#granitoid)
                    - [alkali feldspar granite](#alkali_feldspar_granite)
                    - [granite](#granite)
                        - [monzogranite](#monzogranite)
                        - [syenogranite](#syenogranite)
                    - [granodiorite](#granodiorite)
                    - [tonalite](#tonalite)
                - [hornblendite](#hornblendite)
                - [pegmatite](#pegmatite)
                - [peridotite](#peridotite)
                - [pyroxenite](#pyroxenite)
                - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                - [syenitoid](#syenitoid)
                    - [alkali feldspar syenitic rock](#alkali_feldspar_syenitic_rock)
                        - [alkali feldspar syenite](#alkali_feldspar_syenite)
                        - [foid bearing alkali feldspar syenite](#foid_bearing_alkali_feldspar_syenite)
                        - [quartz alkali feldspar syenite](#quartz_alkali_feldspar_syenite)
                    - [monzonitic rock](#monzonitic_rock)
                        - [foid bearing monzonite](#foid_bearing_monzonite)
                        - [monzonite](#monzonite)
                        - [quartz monzonite](#quartz_monzonite)
                    - [syenitic rock](#syenitic_rock)
                        - [foid bearing syenite](#foid_bearing_syenite)
                        - [quartz syenite](#quartz_syenite)
                        - [syenite](#syenite)
            - [plutonic rock](#plutonic_igneous_rock)
            - [porphyry](#porphyry)
            - [ultrabasic igneous rock](#ultrabasic_igneous_rock)
            - [ultramafic igneous rock](#ultramafic_igneous_rock)
                - [hornblendite](#hornblendite)
                - [peridotite](#peridotite)
                - [pyroxenite](#pyroxenite)
                - [komatiitic rock](#komatiitic_rock)
            - [Volcanic rock](#volcanic_rock)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
                - [Lava](#lava)
        - [acidic igneous material](#acidic_igneous_material)
            - [acidic igneous rock](#acidic_igneous_rock)
                - [dacite](#dacite)
                - [granitoid](#granitoid)
                    - [alkali feldspar granite](#alkali_feldspar_granite)
                    - [granite](#granite)
                        - [monzogranite](#monzogranite)
                        - [syenogranite](#syenogranite)
                    - [granodiorite](#granodiorite)
                    - [tonalite](#tonalite)
                - [quartz rich igneous rock](#quartz_rich_igneous_rock)
                - [rhyolitoid](#rhyolitoid)
                    - [alkali feldspar rhyolite](#alkali_feldspar_rhyolite)
                    - [rhyolite](#rhyolite)
        - [basic igneous material](#basic_igneous_material)
            - [basic igneous rock](#basic_igneous_rock)
                - [basalt](#basalt)
                    - [alkali olivine basalt](#alkali-olivine_basalt)
                    - [tholeiitic basalt](#tholeiitic_basalt)
                - [gabbroic rock](#gabbroic_rock)
                    - [foid bearing gabbro](#foid_bearing_gabbro)
                    - [gabbro](#gabbro)
                    - [quartz gabbro](#quartz_gabbro)
        - [fragmental igneous material](#fragmental_igneous_material)
            - [fragmental igneous rock](#fragmental_igneous_rock)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
            - [pyroclastic material](#pyroclastic_material)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
                - [Tephra](#tephra)
                    - [ash and lapilli](#ash_and_lapilli)
                    - [ash breccia bomb or block tephra](#ash_breccia_bomb_or_block_tephra)
        - [intermediate composition igneous material](#intermediate_composition_igneous_material)
            - [intermediate composition igneous rock](#intermediate_composition_igneous_rock)
                - [andesite](#andesite)
                    - [boninite](#boninite)
                - [dioritoid](#dioritoid)
                    - [dioritic rock](#dioritic_rock)
                        - [diorite](#diorite)
                        - [foid bearing diorite](#foid_bearing_diorite)
                        - [quartz diorite](#quartz_diorite)
                    - [monzodioritic rock](#monzodioritic_rock)
                        - [foid bearing monzodiorite](#foid_bearing_monzodiorite)
                        - [monzodiorite](#monzodiorite)
                        - [quartz monzodiorite](#quartz_monzodiorite)
        - [Volcanic Material](#volcanic_material)
            - [Volcanic rock](#volcanic_rock)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
                - [Lava](#lava)
            - [pyroclastic material](#pyroclastic_material)
                - [pyroclastic rock](#pyroclastic_rock)
                    - [ash tuff lapillistone and lapilli tuff](#ash_tuff_lapillistone_and_lapilli_tuff)
                    - [tuff breccia agglomerate or pyroclastic breccia](#tuff_breccia_agglomerate_or_pyroclastic_breccia)
                - [Tephra](#tephra)
                    - [ash and lapilli](#ash_and_lapilli)
                    - [ash breccia bomb or block tephra](#ash_breccia_bomb_or_block_tephra)
    - [Sedimentary material](#sedimentary_material)
        - [chemical sedimentary material](#chemical_sedimentary_material)
            - [evaporite](#evaporite)
                - [exotic evaporite](#exotic_evaporite)
                - [gypsum or anhydrite](#rock_gypsum_or_anhydrite)
                - [rock salt](#rock_salt)
            - [iron rich sedimentary material](#iron_rich_sedimentary_material)
                - [iron rich sediment](#iron_rich_sediment)
                - [iron rich sedimentary rock](#iron_rich_sedimentary_rock)
            - [Sedimentary Massive Sulphide](#sedimentary_massive_sulphide)
            - [travertine](#travertine)
        - [Sedimentary rock](#sedimentary_rock)
            - [carbonate sedimentary rock](#carbonate_sedimentary_rock)
                - [boundstone](#boundstone)
                - [calcareous carbonate sedimentary rock](#calcareous_carbonate_sedimentary_rock)
                    - [impure limestone](#impure_limestone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
                - [carbonate mudstone](#carbonate_mudstone)
                - [carbonate wackestone](#carbonate_wackestone)
                - [crystalline carbonate](#crystalline_carbonate)
                - [dolomitic or magnesian sedimentary rock](#dolomitic_or_magnesian_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [impure dolomite](#impure_dolostone)
                - [framestone](#framestone)
                - [grainstone](#grainstone)
                - [impure carbonate sedimentary rock](#impure_carbonate_sedimentary_rock)
                    - [impure dolomite](#impure_dolostone)
                    - [impure limestone](#impure_limestone)
                - [packstone](#packstone)
                - [pure carbonate sedimentary rock](#pure_carbonate_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
                    - [pure carbonate mudstone](#pure_carbonate_mudstone)
            - [clastic sedimentary rock](#clastic_sedimentary_rock)
                - [diamictite](#diamictite)
                - [conglomerate](#clastic_conglomerate)
                - [mudstone](#clastic_mudstone)
                    - [claystone](#claystone)
                    - [shale](#shale)
                    - [siltstone](#siltstone)
                - [sandstone](#clastic_sandstone)
                    - [arenit](#arenite)
                    - [wacke](#wacke)
            - [generic conglomerate](#generic_conglomerate)
                - [conglomerate](#clastic_conglomerate)
            - [generic mudstone](#generic_mudstone)
                - [carbonate mudstone](#carbonate_mudstone)
                - [carbonate rich mudstone](#carbonate_rich_mudstone)
                - [mudstone](#clastic_mudstone)
                    - [claystone](#claystone)
                    - [shale](#shale)
                    - [siltstone](#siltstone)
                - [organic bearing mudstone](#organic_bearing_mudstone)
                - [pure carbonate mudstone](#pure_carbonate_mudstone)
                - [silicate mudstone](#silicate_mudstone)
            - [Generic sandstone](#generic_sandstone)
                - [sandstone](#clastic_sandstone)
                    - [arenit](#arenite)
                    - [wacke](#wacke)
            - [hybrid sedimentary rock](#hybrid_sedimentary_rock)
            - [iron rich sedimentary rock](#iron_rich_sedimentary_rock)
            - [non clastic siliceous sedimentary rock](#non_clastic_siliceous_sedimentary_rock)
                - [biogenic silica sedimentary rock](#biogenic_silica_sedimentary_rock)
            - [organic rich sedimentary rock](#organic_rich_sedimentary_rock)
                - [coal](#coal)
                    - [anthracite](#anthracite_coal)
                    - [bituminous coal](#bituminous_coal)
                    - [lignite](#lignite)
            - [phosphorite](#phosphorite)
        - [Sediment](#sediment)
            - [biogenic sediment](#biogenic_sediment)
                - [ooze](#ooze)
                    - [carbonate ooze](#carbonate_ooze)
                    - [siliceous ooze](#siliceous_ooze)
                - [organic rich sediment](#organic_rich_sediment)
                    - [peat](#peat)
                    - [sapropel](#sapropel)
            - [carbonate sediment](#carbonate_sediment)
                - [calcareous carbonate sediment](#calcareous_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                - [carbonate mud](#carbonate_mud)
                    - [carbonate ooze](#carbonate_ooze)
                - [dolomitic sediment](#dolomitic_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
                - [impure carbonate sediment](#impure_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                - [pure carbonate sediment](#pure_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
            - [chemical sedimentary material](#chemical_sedimentary_material)
                - [evaporite](#evaporite)
                    - [exotic evaporite](#exotic_evaporite)
                    - [gypsum or anhydrite](#rock_gypsum_or_anhydrite)
                    - [rock salt](#rock_salt)
                - [iron rich sedimentary material](#iron_rich_sedimentary_material)
                    - [iron rich sediment](#iron_rich_sediment)
                    - [iron rich sedimentary rock](#iron_rich_sedimentary_rock)
                - [Sedimentary Massive Sulphide](#sedimentary_massive_sulphide)
                - [travertine](#travertine)
            - [clastic sediment](#clastic_sediment)
                - [diamicton](#diamicton)
                - [gravel](#gravel)
                - [mud](#mud)
                    - [clay](#clay)
                    - [silt](#silt)
                - [sand](#sand)
            - [gravel size sediment](#gravel_size_sediment)
                - [boulder gravel size sediment](#boulder_gravel_size_sediment)
                - [cobble gravel size sediment](#cobble_gravel_size_sediment)
                - [gravel](#gravel)
                - [pebble gravel size sediment](#pebble_gravel_size_sediment)
            - [Hybrid sediment](#hybrid_sediment)
            - [iron rich sediment](#iron_rich_sediment)
            - [mud size sediment](#mud_size_sediment)
                - [carbonate mud](#carbonate_mud)
                    - [carbonate ooze](#carbonate_ooze)
                - [carbonate rich mud](#carbonate_rich_mud)
                - [mud](#mud)
                    - [clay](#clay)
                    - [silt](#silt)
                - [ooze](#ooze)
                    - [carbonate ooze](#carbonate_ooze)
                    - [siliceous ooze](#siliceous_ooze)
                - [silicate mud](#silicate_mud)
                    - [siliceous ooze](#siliceous_ooze)
            - [non clastic siliceous sediment](#non_clastic_siliceous_sediment)
            - [phosphate rich sediment](#phosphate_rich_sediment)
            - [sand size sediment](#sand_size_sediment)
                - [sand](#sand)
            - [Tephra](#tephra)
                - [ash and lapilli](#ash_and_lapilli)
                - [ash breccia bomb or block tephra](#ash_breccia_bomb_or_block_tephra)
        - [Carbonate sedimentary material](#carbonate_sedimentary_material)
            - [carbonate sediment](#carbonate_sediment)
                - [calcareous carbonate sediment](#calcareous_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                - [carbonate mud](#carbonate_mud)
                    - [carbonate ooze](#carbonate_ooze)
                - [dolomitic sediment](#dolomitic_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
                - [impure carbonate sediment](#impure_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                - [pure carbonate sediment](#pure_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
            - [carbonate sedimentary rock](#carbonate_sedimentary_rock)
                - [boundstone](#boundstone)
                - [calcareous carbonate sedimentary rock](#calcareous_carbonate_sedimentary_rock)
                    - [impure limestone](#impure_limestone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
                - [carbonate mudstone](#carbonate_mudstone)
                - [carbonate wackestone](#carbonate_wackestone)
                - [crystalline carbonate](#crystalline_carbonate)
                - [dolomitic or magnesian sedimentary rock](#dolomitic_or_magnesian_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [impure dolomite](#impure_dolostone)
                - [framestone](#framestone)
                - [grainstone](#grainstone)
                - [impure carbonate sedimentary rock](#impure_carbonate_sedimentary_rock)
                    - [impure dolomite](#impure_dolostone)
                    - [impure limestone](#impure_limestone)
                - [packstone](#packstone)
                - [pure carbonate sedimentary rock](#pure_carbonate_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
                    - [pure carbonate mudstone](#pure_carbonate_mudstone)
            - [calcareous carbonate sedimentary material](#calcareous_carbonate_sedimentary_material)
                - [calcareous carbonate sediment](#calcareous_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                - [calcareous carbonate sedimentary rock](#calcareous_carbonate_sedimentary_rock)
                    - [impure limestone](#impure_limestone)
                    - [limestone](#limestone)
                        - [chalk](#chalk)
                        - [travertine](#travertine)
            - [dolomitic or magnesian sedimentary material](#dolomitic_or_magnesian_sedimentary_material)
                - [dolomitic or magnesian sedimentary rock](#dolomitic_or_magnesian_sedimentary_rock)
                    - [dolomite](#dolostone)
                    - [impure dolomite](#impure_dolostone)
                - [dolomitic sediment](#dolomitic_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
        - [clastic sedimentary material](#clastic_sedimentary_material)
            - [clastic sediment](#clastic_sediment)
                - [diamicton](#diamicton)
                - [gravel](#gravel)
                - [mud](#mud)
                    - [clay](#clay)
                    - [silt](#silt)
                - [sand](#sand)
            - [clastic sedimentary rock](#clastic_sedimentary_rock)
                - [diamictite](#diamictite)
                - [conglomerate](#clastic_conglomerate)
                - [mudstone](#clastic_mudstone)
                    - [claystone](#claystone)
                    - [shale](#shale)
                    - [siltstone](#siltstone)
                - [sandstone](#clastic_sandstone)
                    - [arenit](#arenite)
                    - [wacke](#wacke)
        - [non clastic siliceous sedimentary material](#non_clastic_siliceous_sedimentary_material)
            - [non clastic siliceous sediment](#non_clastic_siliceous_sediment)
            - [non clastic siliceous sedimentary rock](#non_clastic_siliceous_sedimentary_rock)
                - [biogenic silica sedimentary rock](#biogenic_silica_sedimentary_rock)
        - [organic rich sedimentary material](#organic_rich_sedimentary_material)
            - [organic rich sedimentary rock](#organic_rich_sedimentary_rock)
                - [coal](#coal)
                    - [anthracite](#anthracite_coal)
                    - [bituminous coal](#bituminous_coal)
                    - [lignite](#lignite)
            - [organic rich sediment](#organic_rich_sediment)
                - [peat](#peat)
                - [sapropel](#sapropel)
        - [phosphate rich sedimentary material](#phosphate_rich_sedimentary_material)
            - [phosphate rich sediment](#phosphate_rich_sediment)
            - [phosphorite](#phosphorite)

- [Anthropogenic material](#anthropogenic_material)
    - [Anthropogenic unconsolidated material](#anthropogenic_unconsolidated_material)
    - [Concrete](#concrete)
    - [Manufactured chemical substance](#manufactured_chemical_substance)
    - [Mineral processing product](#mineral_processing_product)
        - [Matte ](#matte)
        - [Slag ](#slag)

- [Unconsolidated material](#unconsolidated_material)
    - [Anthropogenic unconsolidated material](#anthropogenic_unconsolidated_material)
    - [Natural unconsolidated material](#natural_unconsolidated_material)
        - [Sediment](#sediment)
            - [biogenic sediment](#biogenic_sediment)
                - [ooze](#ooze)
                    - [carbonate ooze](#carbonate_ooze)
                    - [siliceous ooze](#siliceous_ooze)
                - [organic rich sediment](#organic_rich_sediment)
                    - [peat](#peat)
                    - [sapropel](#sapropel)
            - [carbonate sediment](#carbonate_sediment)
                - [calcareous carbonate sediment](#calcareous_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                - [carbonate mud](#carbonate_mud)
                    - [carbonate ooze](#carbonate_ooze)
                - [dolomitic sediment](#dolomitic_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
                - [impure carbonate sediment](#impure_carbonate_sediment)
                    - [impure calcareous carbonate sediment](#impure_calcareous_carbonate_sediment)
                    - [impure dolomitic sediment](#impure_dolomitic_sediment)
                - [pure carbonate sediment](#pure_carbonate_sediment)
                    - [pure calcareous carbonate sediment](#pure_calcareous_carbonate_sediment)
                    - [pure dolomitic sediment](#pure_dolomitic_sediment)
            - [chemical sedimentary material](#chemical_sedimentary_material)
                - [evaporite](#evaporite)
                    - [exotic evaporite](#exotic_evaporite)
                    - [gypsum or anhydrite](#rock_gypsum_or_anhydrite)
                    - [rock salt](#rock_salt)
                - [iron rich sedimentary material](#iron_rich_sedimentary_material)
                    - [iron rich sediment](#iron_rich_sediment)
                    - [iron rich sedimentary rock](#iron_rich_sedimentary_rock)
                - [Sedimentary Massive Sulphide](#sedimentary_massive_sulphide)
                - [travertine](#travertine)
            - [clastic sediment](#clastic_sediment)
                - [diamicton](#diamicton)
                - [gravel](#gravel)
                - [mud](#mud)
                    - [clay](#clay)
                    - [silt](#silt)
                - [sand](#sand)
            - [gravel size sediment](#gravel_size_sediment)
                - [boulder gravel size sediment](#boulder_gravel_size_sediment)
                - [cobble gravel size sediment](#cobble_gravel_size_sediment)
                - [gravel](#gravel)
                - [pebble gravel size sediment](#pebble_gravel_size_sediment)
            - [Hybrid sediment](#hybrid_sediment)
            - [iron rich sediment](#iron_rich_sediment)
            - [mud size sediment](#mud_size_sediment)
                - [carbonate mud](#carbonate_mud)
                    - [carbonate ooze](#carbonate_ooze)
                - [carbonate rich mud](#carbonate_rich_mud)
                - [mud](#mud)
                    - [clay](#clay)
                    - [silt](#silt)
                - [ooze](#ooze)
                    - [carbonate ooze](#carbonate_ooze)
                    - [siliceous ooze](#siliceous_ooze)
                - [silicate mud](#silicate_mud)
                    - [siliceous ooze](#siliceous_ooze)
            - [non clastic siliceous sediment](#non_clastic_siliceous_sediment)
            - [phosphate rich sediment](#phosphate_rich_sediment)
            - [sand size sediment](#sand_size_sediment)
                - [sand](#sand)
            - [Tephra](#tephra)
                - [ash and lapilli](#ash_and_lapilli)
                - [ash breccia bomb or block tephra](#ash_breccia_bomb_or_block_tephra)
        - [Soil](#soil)

**Concepts**

[]{#rockorsediment}

##  Rock or sediment
- Material is rock or sediment.  For example core from boreholes that
likely penetrate sediment near the surface and rock at greater depth,
with descriptions that do not clearly distinguish non-consolidated
sediment from rock.
- **Concept URI:** https://w3id.org/isample/vocabulary/material/1.0/rockorsediment
- **Other Properties:**

[]{#breccia}

###  Breccia
- **Child of**:
 [`Rock`](#rock)
 [`Rock or sediment`](#rockorsediment)
- Coarse-grained material composed of angular broken rock fragments;
the fragments typically have sharp edges and unworn corners. The
fragments may be held together by a mineral cement or in a fine-
grained matrix, and consolidated or nonconsolidated. Clasts may be of
any composition or origin. In sedimentary environments, breccia is
used for material that consists entirely of angular fragments, mostly
derived from a single source rock body, as in a rock avalanche
deposit, and matrix is interpreted to be the product of comminution of
clasts during transport. Diamictite or diamicton is used when the
material reflects mixing of rock from a variety of sources, some sub
angular or subrounded clasts may be present, and matrix is pre-
existing fine grained material that is not a direct product of the
brecciation/deposition process.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Breccia
- **Other Properties:**

[]{#rock}

###  Rock
- **Child of**:
 [`Rock or sediment`](#rockorsediment)
- Consolidated aggregate of one or more EarthMaterials, or a body of
undifferentiated mineral matter, or of solid organic material.
Includes mineral aggregates such as granite, shale, marble; glassy
matter such as obsidian; and organic material such a coal. Excludes
unconsolidated materials.
- Consolidated aggregate of particles (grains) of rock, mineral
(including native elements), mineraloid, or solid organic material.
Includes mineral aggregates such as granite, shale, marble; natural
glass such as obsidian; organic material formed by geologic processes
such a coal;  extraterrestrial material in meteorites; and  crushed
rock fragments like drill cuttings from rock.  (based on
http://resource.geosciml.org/classifier/cgi/lithology/rock, same as
http://purl.obolibrary.org/obo/ENVO_00001995)
- **Source:**
Jackson, 1997; NADM C1 2004; Neuendorf et al 2005
- **Concept URI:** https://w3id.org/isample/vocabulary/material/1.0/rock
- **Other Properties:**

[]{#aphanite}

####  Aphanite
- **Child of**:
 [`Rock`](#rock)
- Rock that is too fine grained to categorize in more detail.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Aphanite
- **Other Properties:**

[]{#breccia}

####  Breccia
- **Child of**:
 [`Rock`](#rock)
 [`Rock or sediment`](#rockorsediment)
- Coarse-grained material composed of angular broken rock fragments;
the fragments typically have sharp edges and unworn corners. The
fragments may be held together by a mineral cement or in a fine-
grained matrix, and consolidated or nonconsolidated. Clasts may be of
any composition or origin. In sedimentary environments, breccia is
used for material that consists entirely of angular fragments, mostly
derived from a single source rock body, as in a rock avalanche
deposit, and matrix is interpreted to be the product of comminution of
clasts during transport. Diamictite or diamicton is used when the
material reflects mixing of rock from a variety of sources, some sub
angular or subrounded clasts may be present, and matrix is pre-
existing fine grained material that is not a direct product of the
brecciation/deposition process.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Breccia
- **Other Properties:**

[]{#fault_related_material}

####  Fault related material
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis material`](#composite_genesis_material)
- Material formed as a result brittle faulting, composed of greater
than 10 percent matrix; matrix is fine-grained material caused by
tectonic grainsize reduction. Includes cohesive (cataclasite series,
mylonitic rocks) and non-cohesive (breccia-gouge series) material.
- **Source:**
This vocabulary; SLTTm 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fault_Related_Material
- **Other Properties:**

[]{#cataclasite_series}

#####  cataclasite series
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`Composite genesis rock`](#composite_genesis_rock)
- Fault-related rock that maintained primary cohesion during
deformation, with matrix comprising greater than 10 percent of rock
mass; matrix is fine-grained material formed through grain size
reduction by fracture as opposed to crystal plastic process that
operate in mylonitic rock. Includes cataclasite, protocataclasite and
ultracataclasite.
- **Source:**
Sibson, 1977; Scholz, 1990; Snoke and Tullis, 1998; Barker, 1998 Appendix II; NADM SLTTm, 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Cataclasite_Series
- **Other Properties:**

[]{#mylonitic_rock}

#####  mylonitic rock
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Metamorphic rock characterised by a foliation resulting from
tectonic grain size reduction, in which more than 10 percent of the
rock volume has undergone grain size reduction. Includes
protomylonite, mylonite, ultramylonite, and blastomylonite.
- **Source:**
Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mylonitic_Rock
- **Other Properties:**

[]{#phyllonite}

######  phyllonite
- **Child of**:
 [`mylonitic rock`](#mylonitic_rock)
- Mylonitic rock composed largely of fine-grained mica that imparts a
sheen to foliation surfaces; may have flaser lamination, isoclinal
folding, and deformed veins, which indicate significant shearing.
Macroscopically resembles phyllite, but formed by mechanical
degradation of initially coarser rock.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllonite
- **Other Properties:**

[]{#breccia_gouge_series}

#####  breccia gouge series
- **Child of**:
 [`Fault related material`](#fault_related_material)
- Fault-related material with features such as void spaces (filled or
unfilled), or unconsolidated matrix material between fragments,
indicating loss of cohesion during deformation. Includes fault-related
breccia and gouge.
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/breccia_gouge_series
- **Other Properties:**

[]{#fragmental_igneous_rock}

####  fragmental igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Rock`](#rock)
 [`fragmental igneous material`](#fragmental_igneous_material)
- Igneous rock in which greater than 75 percent of the rock consists
of fragments produced as a result of igneous rock-forming process.
Includes pyroclastic rocks, autobreccia associated with lava flows and
intrusive breccias. Excludes deposits reworked by epiclastic processes
(see Tuffite)
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fragmental_Igneous_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

#####  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#igneous_rock}

####  Igneous rock
- **Child of**:
 [`Rock`](#rock)
 [`Igneous material`](#igneous_material)
- rock formed as a result of igneous processes, for example intrusion
and cooling of magma in the crust, or volcanic eruption.
- **Source:**
Neuendorf et al 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Igneous_Rock
- **Other Properties:**

[]{#acidic_igneous_rock}

#####  acidic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`acidic igneous material`](#acidic_igneous_material)
- Igneous rock with more than 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Acidic_Igneous_Rock
- **Other Properties:**

[]{#dacite}

######  dacite
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dacite
- **Other Properties:**

[]{#granitoid}

######  granitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.
- **Alternate labels:**
granitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granitoid
- **Other Properties:**

[]{#alkali_feldspar_granite}

#######  alkali feldspar granite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitic rock that has a plagioclase to total feldspar ratio less
than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Alkali_Feldspar_Granite
- **Other Properties:**

[]{#granite}

#######  granite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting of quartz, alkali feldspar
and plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granite
- **Other Properties:**

[]{#monzogranite}

########  monzogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.35
and 0.65. QAPF field 3b.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogranite
- **Other Properties:**

[]{#syenogranite}

########  syenogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.10
and 0.35. QAPF field 3a.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenogranite
- **Other Properties:**

[]{#granodiorite}

#######  granodiorite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granodiorite
- **Other Properties:**

[]{#tonalite}

#######  tonalite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tonalite
- **Other Properties:**

[]{#quartz_rich_igneous_rock}

######  quartz rich igneous rock
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals and contains greater than 60 percent quartz in
the QAPF fraction.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Quartz_Rich_Igneous_Rock
- **Other Properties:**

[]{#rhyolitoid}

######  rhyolitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Note that technical definition, based on modal mineralogy plotted in
a QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
- fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.
- **Alternate labels:**
rhyolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Rhyolitoid
- **Other Properties:**

[]{#alkali_feldspar_rhyolite}

#######  alkali feldspar rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- Rhyolitoid in which the ratio of plagioclase to total feldspar is
less than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Rhyolite
- **Other Properties:**

[]{#rhyolite}

#######  rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- rhyolitoid in which the ratio of plagioclase to total feldspar is
between 0.1 and 0.65.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rhyolite
- **Other Properties:**

[]{#basic_igneous_rock}

#####  basic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`basic igneous material`](#basic_igneous_material)
- Igneous rock with between 45 and 52 percent SiO2.
- **Source:**
Neuendorf et al 2005; LeMaitre et al. 2002; Gillespie and Styles 1999, 
after LeMaitre et al. 2002, 
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basic_Igneous_Rock
- **Other Properties:**

[]{#basalt}

######  basalt
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basalt
- **Other Properties:**

[]{#alkali-olivine_basalt}

#######  alkali olivine basalt
- **Child of**:
 [`basalt`](#basalt)
- The definition of tholeiite and alkali basalt here are more
prescriptive than those found in most reference authorities. This is
to actually provide some descriptive criteria to allow assignment of
rocks on a hand sample basis to the tholeiite or alkali basalt
categories if detailed petrographic or chemical data are available.
- Alkali olivine basalt is silica-undersaturated, characterized by the
absence of orthopyroxene, absence of quartz, presence of olivine, and
typically contains some feldspathoid mineral, alkali feldspar or
phlogopite in the groundmass. Feldspar phenocrysts typically are
labradorite to andesine in composition. Augite is rich in titanium
compared to augite in tholeiitic basalt. Alkali olivine basalt is
relatively rich in sodium.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali-Olivine_Basalt
- **Other Properties:**

[]{#tholeiitic_basalt}

#######  tholeiitic basalt
- **Child of**:
 [`basalt`](#basalt)
- Definition of tholeiite and alkali basalt here are more proscriptive
than those found in most reference authorities. This is to actually
provide some descriptive criteria to allow assignment of rocks on a
hand sample basis to the tholeiite or alkali basalt categories if
detailed petrographic or chemical data are available.
- Tholeiitic basalt is defined here to contain 2 pyroxene phases and
interstitial quartz or tridymite or cristobalite in the groundmass.
Pyroxene (augite and orthopyroxene or pigeonite) and calcium-rich
plagioclase are common phenocryst minerals. Olivine may also be a
phenocryst, and when present, may have rims of pigeonite. Only in
tholeiitic basalt is olivine in reaction relationship with melt.
Interstitial siliceous residue may be present, and is often glassy.
Tholeiitic basalt is relatively poor in sodium. This category includes
most basalts of the ocean floor, most large oceanic islands, and
continental flood basalts such as the Columbia River Plateau.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tholeiitic_Basalt
- **Other Properties:**

[]{#gabbroic_rock}

######  gabbroic rock
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`gabbroid`](#gabbroid)
- Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_gabbro}

#######  foid bearing gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains 0-10 percent feldspathoid minerals and
no quartz in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Gabbro
- **Other Properties:**

[]{#gabbro}

#######  gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Note that this category includes gabbro (sensu stricto) of LeMaitre
et al. 2002, but is broader, including the other rock types defined by
orthopyroxene-clinopyroxene-olivine-hornblende mineral ratios.
- Gabbroic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF Field 10 as gabbro.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gabbro
- **Other Properties:**

[]{#quartz_gabbro}

#######  quartz gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Gabbro
- **Other Properties:**

[]{#doleritic_rock}

#####  doleritic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Dark colored gabbroic (basaltic) or dioritic (andesitic) rock
intermediate in grain size between basalt and gabbro and composed of
plagioclase, pyroxene and opaque minerals; often with ophitic texture.
Typically occurs as hypabyssal intrusions. Includes dolerite,
microdiorite, diabase and microgabbro.
- **Source:**
Neuendorf et al 2005; LeMaitre et al. 2002; Gillespie and Styles 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Doleritic_Rock
- **Other Properties:**

[]{#exotic_composition_igneous_rock}

#####  exotic composition igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Rock with 'exotic' mineralogical, textural or field setting
characteristics; typically dark colored, with abundant phenocrysts.
Criteria include: presence of greater than 10 percent melilite or
leucite, or presence of kalsilite, or greater than 50 percent
carbonate minerals. Includes Carbonatite, Melilitic rock, Kalsilitic
rocks, Kimberlite, Lamproite, Leucitic rock and Lamprophyres.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Exotic_Composition_Igneous_Rock
- **Other Properties:**

[]{#carbonatite}

######  carbonatite
- **Child of**:
 [`exotic composition igneous rock`](#exotic_composition_igneous_rock)
- Igneous rock composed of more than 50 percent modal carbonate
minerals.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonatite
- **Other Properties:**

[]{#exotic_alkaline_rock}

######  exotic alkaline rock
- **Child of**:
 [`exotic composition igneous rock`](#exotic_composition_igneous_rock)
- Kimberlite, lamproite, or lamprophyre. Generally are potassic, mafic
or ultramafic rocks. Olivine (commonly serpentinized in kimberlite),
and phlogopite are significant constituents.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Exotic_Alkaline_Rock
- **Other Properties:**

[]{#kalsilitic_and_melilitic_rock}

######  kalsilitic and melilitic rocks
- **Child of**:
 [`exotic composition igneous rock`](#exotic_composition_igneous_rock)
- Igneous rock containing greater than 10 percent melilite or
kalsilite. Typically undersaturated, ultrapotassic (kalsilitic rocks)
or calcium-rich (melilitic rocks) mafic or ultramafic rocks.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Kalsilitic_And_Melilitic_Rock
- **Other Properties:**

[]{#fine_grained_igneous_rock}

#####  fine grained igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Need to make decision as to whether devitrified glass should be
considered glass or microcrystalline framework for purposes of
categorization
- Igneous rock in which the framework of the rock consists of crystals
that are too small to determine mineralogy with the unaided eye;
framework may include up to 50 percent glass. A significant percentage
of the rock by volume may be phenocrysts. Includes rocks that are
generally called volcanic rocks.
- **Alternate labels:**
volcanic rock
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fine_Grained_Igneous_Rock
- **Other Properties:**

[]{#andesite}

######  andesite
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
- Note the mela-andesite and leuco-basalt categories are not
recommended in this system. If chemical analytical data are available
to constrain the silica content, the basalt or andesite category
should be used.
- Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Andesite
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#basalt}

######  basalt
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basalt
- **Other Properties:**

[]{#alkali-olivine_basalt}

#######  alkali olivine basalt
- **Child of**:
 [`basalt`](#basalt)
- The definition of tholeiite and alkali basalt here are more
prescriptive than those found in most reference authorities. This is
to actually provide some descriptive criteria to allow assignment of
rocks on a hand sample basis to the tholeiite or alkali basalt
categories if detailed petrographic or chemical data are available.
- Alkali olivine basalt is silica-undersaturated, characterized by the
absence of orthopyroxene, absence of quartz, presence of olivine, and
typically contains some feldspathoid mineral, alkali feldspar or
phlogopite in the groundmass. Feldspar phenocrysts typically are
labradorite to andesine in composition. Augite is rich in titanium
compared to augite in tholeiitic basalt. Alkali olivine basalt is
relatively rich in sodium.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali-Olivine_Basalt
- **Other Properties:**

[]{#tholeiitic_basalt}

#######  tholeiitic basalt
- **Child of**:
 [`basalt`](#basalt)
- Definition of tholeiite and alkali basalt here are more proscriptive
than those found in most reference authorities. This is to actually
provide some descriptive criteria to allow assignment of rocks on a
hand sample basis to the tholeiite or alkali basalt categories if
detailed petrographic or chemical data are available.
- Tholeiitic basalt is defined here to contain 2 pyroxene phases and
interstitial quartz or tridymite or cristobalite in the groundmass.
Pyroxene (augite and orthopyroxene or pigeonite) and calcium-rich
plagioclase are common phenocryst minerals. Olivine may also be a
phenocryst, and when present, may have rims of pigeonite. Only in
tholeiitic basalt is olivine in reaction relationship with melt.
Interstitial siliceous residue may be present, and is often glassy.
Tholeiitic basalt is relatively poor in sodium. This category includes
most basalts of the ocean floor, most large oceanic islands, and
continental flood basalts such as the Columbia River Plateau.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tholeiitic_Basalt
- **Other Properties:**

[]{#dacite}

######  dacite
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dacite
- **Other Properties:**

[]{#foiditoid}

######  foiditoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained crystalline rock containing less than 90 percent mafic
minerals and more than 60 percent feldspathoid minerals in the QAPF
fraction. Includes rocks defined modally in QAPF field 15 or
chemically in TAS field F.
- **Alternate labels:**
foidite (sensu lato), 
foiditic rock, 
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foiditoid
- **Other Properties:**

[]{#basanitic_foidite}

#######  basanitic foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains less than 90 percent feldspathoid minerals
in the QAPF fraction, and has a plagioclase to total feldspar ratio
that is greater than 0.5, with greater than 10 percent normative
olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Basanitic_Foidite
- **Other Properties:**

[]{#foidite}

#######  foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains greater than 90 percent feldspathoid
minerals in the QAPF fraction.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foidite
- **Other Properties:**

[]{#phonolitic_foidite}

#######  phonolitic foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains less than 90 percent feldspathoid minerals
in the QAPF fraction, and has a plagioclase to total feldspar ratio
that is less than 0.5
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolitic_Foidite
- **Other Properties:**

[]{#tephritic_foidite}

#######  tephritic foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains less than 90 percent feldspathoid minerals
in the QAPF fraction, and has a plagioclase to total feldspar ratio
that is greater than 0.5, with less than 10 percent normative olivine
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tephritic_Foidite
- **Other Properties:**

[]{#high_magnesium_fine_grained_igneous_rock}

######  high magnesium fine grained igneous rock
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- fine-grained igneous rock that contains unusually high concentration
of MgO. For rocks that contain greater than 52 percent silica, MgO
must be greater than 8 percent. For rocks containing less than 52
percent silica, MgO must be greater than 12 percent.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/High_Magnesium_Fine_Grained_Igneous_Rock
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#komatiitic_rock}

#######  komatiitic rock
- **Child of**:
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic, magnesium-rich volcanic rock, typically with spinifex
texture of intergrown skeletal and bladed olivine and pyroxene
crystals set in abundant glass. Includes komatiite and meimechite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Komatiitic_Rock
- **Other Properties:**

[]{#phonolitoid}

######  phonolitoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained igneous rock than contains less than 90 percent mafic
minerals, between 10 and 60 percent feldspathoid mineral in the QAPF
fraction and has a plagioclase to total feldspar ratio less than 0.5.
Includes rocks defined modally in QAPF fields 11 and 12, and TAS field
Ph.
- **Alternate labels:**
phonolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phonolitoid
- **Other Properties:**

[]{#phonolilte}

#######  phonolite
- **Child of**:
 [`phonolitoid`](#phonolitoid)
- Phonolitoid in which the plagioclase to total feldspar ratio is less
than 0.1. Rock consists of alkali feldspar, feldspathoid minerals, and
mafic minerals.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolilte
- **Other Properties:**

[]{#tephritic_phonolite}

#######  tephritic phonolite
- **Child of**:
 [`phonolitoid`](#phonolitoid)
- Phonolitoid that has a plagioclase to total feldspar ratio between
0.1 and 0.5. Broadly corresponds to TAS tephriphonolite of TAS field
U3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tephritic_Phonolite
- **Other Properties:**

[]{#rhyolitoid}

######  rhyolitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Note that technical definition, based on modal mineralogy plotted in
a QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
- fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.
- **Alternate labels:**
rhyolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Rhyolitoid
- **Other Properties:**

[]{#alkali_feldspar_rhyolite}

#######  alkali feldspar rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- Rhyolitoid in which the ratio of plagioclase to total feldspar is
less than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Rhyolite
- **Other Properties:**

[]{#rhyolite}

#######  rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- rhyolitoid in which the ratio of plagioclase to total feldspar is
between 0.1 and 0.65.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rhyolite
- **Other Properties:**

[]{#tephritoid}

######  tephritoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained igneous rock than contains less than 90 percent mafic
minerals, between 10 and 60 percent feldspathoid mineral in the QAPF
fraction and has a plagioclase to total feldspar ratio greater than
0.5. Includes rocks classified in QAPF field 13 and 14 or chemically
in TAS field U1 as basanite or tephrite.
- **Alternate labels:**
tephritic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tephritoid
- **Other Properties:**

[]{#basanite}

#######  basanite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio greater
than 0.9, and contains more than 10 percent normative (CIPW) olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Basanite
- **Other Properties:**

[]{#phonolitic_basanite}

#######  phonolitic basanite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio between
0.5 and 0.9, and contains more than 10 percent normative (CIPW)
olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolitic_Basanite
- **Other Properties:**

[]{#phonolitic_tephrite}

#######  phonolitic tephrite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio between
0.5 and 0.9, and contains less than 10 percent normative (CIPW)
olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolitic_Tephrite
- **Other Properties:**

[]{#tephrite}

#######  tephrite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio greater
than 0.9, and contains less than 10 percent normative (CIPW) olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tephrite
- **Other Properties:**

[]{#trachytoid}

######  trachytoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained igneous rock than contains less than 90 percent mafic
minerals, less than 10 percent feldspathoid mineral and less than 20
percent quartz in the QAPF fraction and has a plagioclase to total
feldspar ratio less than 0.65. Mafic minerals typically include
amphibole or mica; typically porphyritic. Includes rocks defined
modally in QAPF fields 6, 7 and 8 (with subdivisions) or chemically in
TAS Field T as trachyte or latite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Trachytoid
- **Other Properties:**

[]{#alkali_feldspar_trachytic_rock}

#######  alkali feldspar trachytic rock
- **Child of**:
 [`trachytoid`](#trachytoid)
- Trachytoid that has a plagioclase to total feldspar ratio less than
0.1. QAPF fields 6, 6', and 6*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Trachytic_Rock
- **Other Properties:**

[]{#alkali_feldspar_trachyte}

########  alkali feldspar trachyte
- **Child of**:
 [`alkali feldspar trachytic rock`](#alkali_feldspar_trachytic_rock)
- Trachytoid that has a plagioclase to total feldspar ratio less than
0.1, between 0 and 5 percent quartz in the QAPF fraction, and no
feldspathoid minerals. QAPF field 6.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Trachyte
- **Other Properties:**

[]{#foid_bearing_alkali_feldspar_trachyte}

########  foid bearing alkali feldspar trachyte
- **Child of**:
 [`alkali feldspar trachytic rock`](#alkali_feldspar_trachytic_rock)
- Alkali feldspar trachytic rock that contains no quartz and between 0
and 10 percent feldspathoid mineral in the QAPF fraction. QAPF field
6'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Alkali_Feldspar_Trachyte
- **Other Properties:**

[]{#quartz_alkali_feldspar_trachyte}

########  quartz alkali feldspar trachyte
- **Child of**:
 [`alkali feldspar trachytic rock`](#alkali_feldspar_trachytic_rock)
- Alkali feldspar trachytic rock that contains and between 5 and 20
percent quartz mineral in the QAPF fraction. QAPF field 6*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Alkali_Feldspar_Trachyte
- **Other Properties:**

[]{#latitic_rock}

#######  latitic rock
- **Child of**:
 [`trachytoid`](#trachytoid)
- Trachytoid that has a plagioclase to total feldspar ratio between
0.35 and 0.65. QAPF fields 8, 8' and 8*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Latitic_Rock
- **Other Properties:**

[]{#foid_bearing_latite}

########  foid bearing latite
- **Child of**:
 [`latitic rock`](#latitic_rock)
- Latitic rock that contains no quartz and between 0 and 10 percent
feldspathoid minerals in the QAPF fraction. QAPF field 8'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Latite
- **Other Properties:**

[]{#latite}

########  latite
- **Child of**:
 [`latitic rock`](#latitic_rock)
- Latitic rock that contains between 0 and 5 percent quartz and no
feldspathoid in the QAPF fraction. QAPF field 8.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Latite
- **Other Properties:**

[]{#quartz_latite}

########  quartz latite
- **Child of**:
 [`latitic rock`](#latitic_rock)
- Latitic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 8*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Latite
- **Other Properties:**

[]{#trachytic_rock}

#######  trachytic rock
- **Child of**:
 [`trachytoid`](#trachytoid)
- LeMaitre et al. (2002) used 'trachyte' to refer to QAPF fields 7,
7', and 7* in the text (p. 30) as well as to the more restrictive
category (QAPF field 7 only). The term Trachytic rock is introduced
here to label this more general category of trachyte.
- Trachytoid that has a plagioclase to total feldspar ratio between
0.1 and 0.35. QAPF fields 7, 7', and 7*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Trachytic_Rock
- **Other Properties:**

[]{#foid_bearing_trachyte}

########  foid bearing trachyte
- **Child of**:
 [`trachytic rock`](#trachytic_rock)
- Trachytic rock that contains between 0 and 10 percent feldspathoid
in the QAPF fraction, and no quartz. QAPF field 7'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Trachyte
- **Other Properties:**

[]{#quartz_trachyte}

########  quartz trachyte
- **Child of**:
 [`trachytic rock`](#trachytic_rock)
- Trachytic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 7*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Trachyte
- **Other Properties:**

[]{#trachyte}

########  trachyte
- **Child of**:
 [`trachytic rock`](#trachytic_rock)
- Trachytoid that has a plagioclase to total feldspar ratio between
0.1 and 0.35, between 0 and 5 percent quartz in the QAPF fraction, and
no feldspathoid minerals. QAPF field 7.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Trachyte
- **Other Properties:**

[]{#fragmental_igneous_rock}

#####  fragmental igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Rock`](#rock)
 [`fragmental igneous material`](#fragmental_igneous_material)
- Igneous rock in which greater than 75 percent of the rock consists
of fragments produced as a result of igneous rock-forming process.
Includes pyroclastic rocks, autobreccia associated with lava flows and
intrusive breccias. Excludes deposits reworked by epiclastic processes
(see Tuffite)
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fragmental_Igneous_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#glass_rich_igneous_rock}

#####  glass rich igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock that contains greater than 50 percent massive glass.
- **Source:**
This vocabulary, based on Gillespie and Styles 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Glass_Rich_Igneous_Rock
- **Other Properties:**

[]{#glassy_igneous_rock}

######  glassy igneous rock
- **Child of**:
 [`glass rich igneous rock`](#glass_rich_igneous_rock)
- Note that this category is used for massive glassy rocks. Much of
the pyroclastic material in a pyroclastic rock may be composed of
glass, but the rock is named based on its fragmental nature.
- Igneous rock that consists of greater than 80 percent massive glass.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Glassy_Igneous_Rock
- **Other Properties:**

[]{#hypabyssal_intrusive_rock}

#####  hypabyssal intrusive rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rocks formed by crystallisation close to the Earth's
surface, characterized by more rapid cooling than plutonic setting to
produce generally fine-grained intrusive igneous rock, commonly
associated with co-magmatic volcanic rocks.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hypabyssal_Intrusive_Rock
- **Other Properties:**

[]{#intermediate_composition_igneous_rock}

#####  intermediate composition igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`intermediate composition igneous material`](#intermediate_composition_igneous_material)
- Igneous rock with between 52 and 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Intermediate_Composition_Igneous_Rock
- **Other Properties:**

[]{#andesite}

######  andesite
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
- Note the mela-andesite and leuco-basalt categories are not
recommended in this system. If chemical analytical data are available
to constrain the silica content, the basalt or andesite category
should be used.
- Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Andesite
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#dioritoid}

######  dioritoid
- **Child of**:
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
of intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dioritoid
- **Other Properties:**

[]{#dioritic_rock}

#######  dioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. A dioritoid with a plagioclase to total feldspar
ratio (in the QAPF fraction) greater than 0.9. Includes rocks defined
modally in QAPF fields 10, 10' and 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dioritic_Rock
- **Other Properties:**

[]{#diorite}

########  diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Phaneritic crystalline rock consisting of intermediate plagioclase,
commonly with hornblende and often with biotite or augite; colour
index M less than 90, sodic plagioclase (An0-An50), no feldspathoid,
and between 0 and 5 percent quartz. Includes rocks defined modally in
QAPF field 10 as diorite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Diorite
- **Other Properties:**

[]{#foid_bearing_diorite}

########  foid bearing diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 0 and 10 percent feldspathoid
minerals in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Diorite
- **Other Properties:**

[]{#quartz_diorite}

########  quartz diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 5 to 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Diorite
- **Other Properties:**

[]{#monzodioritic_rock}

#######  monzodioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 10 percent feldspathoid or 0 to 20 percent
quartz in the QAPF fraction. Plagioclase to total feldspar ratio in
the QAPF fraction is between 0.65 and 0.9. Includes rocks defined
modally in QAPF field 9, 9' and 9* as monzodiorite, foid-beaing
monzodiorite, and quartz monzodiorite.
- **Source:**
This vocabulary; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodioritic_Rock
- **Other Properties:**

[]{#foid_bearing_monzodiorite}

########  foid bearing monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 0 and 10 percent
feldspathoid mineral.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzodiorite
- **Other Properties:**

[]{#monzodiorite}

########  monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 5 percent quartz. Includes rocks defined
modally in QAPF field 9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodiorite
- **Other Properties:**

[]{#quartz_monzodiorite}

########  quartz monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 5 and 20 percent quartz.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzodiorite
- **Other Properties:**

[]{#phaneritic_igneous_rock}

#####  phaneritic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock in which the framework of the rock consists of
individual crystals that can be discerned with the unaided eye.
Bounding grain size is on the order of 32 to 100 microns. Igneous
rocks with 'exotic' composition are excluded from this concept.
- **Alternate labels:**
coarse grained crystalline igneous rock, 
plutonic rock, 
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phaneritic_Igneous_Rock
- **Other Properties:**

[]{#anorthositic_rock}

######  anorthositic rock
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Anorthositic rock term invented to label the combined QAPF fields
10, 10*, and 10', in order to construct hierarchy in this vocabulary.
- Leucocratic phaneritic crystalline igneous rock consisting
essentially of plagioclase, often with small amounts of pyroxene. By
definition, colour index M is less than 10, and plagiclase to total
feldspar ratio is greater than 0.9. Less than 20 percent quartz and
less than 10 percent feldspathoid in the QAPF fraction. QAPF field 10,
10*, and 10'.
- Anorthositic rock term invented to label the combined QAPF fields
10, 10*, and 10', in order to construct hierarchy in this vocabulary.
- Leucocratic phaneritic crystalline igneous rock consisting
essentially of plagioclase, often with small amounts of pyroxene. By
definition, colour index M is less than 10, and plagiclase to total
feldspar ratio is greater than 0.9. Less than 20 percent quartz and
less than 10 percent feldspathoid in the QAPF fraction. QAPF field 10,
10*, and 10'.
- **Source:**
LeMaitre et al. 2002; This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Anorthositic_Rock
- **Other Properties:**

[]{#anorthosite}

#######  anorthosite
- **Child of**:
 [`anorthositic rock`](#anorthositic_rock)
- Anorthositic rock that contains between 0 and 5 percent quartz and
no feldspathoid mineral in the QAPF fraction. QAPF field 10.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anorthosite
- **Other Properties:**

[]{#foid_bearing_anorthosite}

#######  foid bearing anorthosite
- **Child of**:
 [`anorthositic rock`](#anorthositic_rock)
- Anorthositic rock that contains between 0 and 10 percent
feldspathoid mineral and no quartz in the QAPF fraction. QAPF field
10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Anorthosite
- **Other Properties:**

[]{#quartz_anorthosite}

#######  quartz anorthosite
- **Child of**:
 [`anorthositic rock`](#anorthositic_rock)
- Anorthositic rock that contains between 5 and 20 percent quartz in
the QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Anorthosite
- **Other Properties:**

[]{#aplite}

######  aplite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Light coloured crystalline rock, characterized by a fine grained
allotriomorphic-granular (aplitic, saccharoidal or xenomorphic)
texture; typically granitic composition, consisting of quartz, alkali
feldspar and sodic plagioclase.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Aplite
- **Other Properties:**

[]{#dioritoid}

######  dioritoid
- **Child of**:
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
of intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dioritoid
- **Other Properties:**

[]{#dioritic_rock}

#######  dioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. A dioritoid with a plagioclase to total feldspar
ratio (in the QAPF fraction) greater than 0.9. Includes rocks defined
modally in QAPF fields 10, 10' and 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dioritic_Rock
- **Other Properties:**

[]{#diorite}

########  diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Phaneritic crystalline rock consisting of intermediate plagioclase,
commonly with hornblende and often with biotite or augite; colour
index M less than 90, sodic plagioclase (An0-An50), no feldspathoid,
and between 0 and 5 percent quartz. Includes rocks defined modally in
QAPF field 10 as diorite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Diorite
- **Other Properties:**

[]{#foid_bearing_diorite}

########  foid bearing diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 0 and 10 percent feldspathoid
minerals in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Diorite
- **Other Properties:**

[]{#quartz_diorite}

########  quartz diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 5 to 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Diorite
- **Other Properties:**

[]{#monzodioritic_rock}

#######  monzodioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 10 percent feldspathoid or 0 to 20 percent
quartz in the QAPF fraction. Plagioclase to total feldspar ratio in
the QAPF fraction is between 0.65 and 0.9. Includes rocks defined
modally in QAPF field 9, 9' and 9* as monzodiorite, foid-beaing
monzodiorite, and quartz monzodiorite.
- **Source:**
This vocabulary; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodioritic_Rock
- **Other Properties:**

[]{#foid_bearing_monzodiorite}

########  foid bearing monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 0 and 10 percent
feldspathoid mineral.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzodiorite
- **Other Properties:**

[]{#monzodiorite}

########  monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 5 percent quartz. Includes rocks defined
modally in QAPF field 9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodiorite
- **Other Properties:**

[]{#quartz_monzodiorite}

########  quartz monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 5 and 20 percent quartz.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzodiorite
- **Other Properties:**

[]{#foid_dioritoid}

######  foid dioritoid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock in which M is less than 90, the
plagioclase to total feldspar ratio is greater than 0.5, feldspathoid
minerals form 10-60 percent of the QAPF fraction, plagioclase has
anorthite content less than 50 percent. These rocks typically contain
large amounts of mafic minerals. Includes rocks defined modally in
QAPF fields 13 and 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foid_Dioritoid
- **Other Properties:**

[]{#foid_diorite}

#######  foid diorite
- **Child of**:
 [`foid dioritoid`](#foid_dioritoid)
- Foid dioritoid in which the plagioclase to total feldspar ratio is
greater than 0.9. Includes rocks defined modally in QAPF field 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Diorite
- **Other Properties:**

[]{#foid_monzodiorite}

#######  foid monzodiorite
- **Child of**:
 [`foid dioritoid`](#foid_dioritoid)
- Foid dioritoid in which the plagioclase to total feldspar ratio is
between 0.1 and 0.9. Includes rocks defined modally in QAPF field 13.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Monzodiorite
- **Other Properties:**

[]{#foid_gabbroid}

######  foid gabbroid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock in which M is less than 90, the
plagioclase to total feldspar ratio is greater than 0.5, feldspathoids
form 10-60 percent of the QAPF fraction, and plagioclase has anorthite
content greater than 50 percent. These rocks typically contain large
amounts of mafic minerals. Includes rocks defined modally in QAPF
fields 13 and 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foid_Gabbroid
- **Other Properties:**

[]{#foid_gabbro}

#######  foid gabbro
- **Child of**:
 [`foid gabbroid`](#foid_gabbroid)
- Foid gabbroid that has a plagioclase to total feldspar ratio greater
than 0.9. Includes rocks defined modally in QAPF field 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Gabbro
- **Other Properties:**

[]{#foid_monzogabbro}

#######  foid monzogabbro
- **Child of**:
 [`foid gabbroid`](#foid_gabbroid)
- Foid gabbroid that has a plagioclase to total feldspar ratio between
0.5 and 0.9. Includes rocks defined modally in QAPF field 13.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Monzogabbro
- **Other Properties:**

[]{#foid_syenitoid}

######  foid syenitoid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, contains
between 10 and 60 percent feldspathoid mineral in the QAPF fraction,
and has a plagioclase to total feldspar ratio less than 0.5. Includes
QAPF fields 11 and 12.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foid_Syenitoid
- **Other Properties:**

[]{#foid_monzosyenite}

#######  foid monzosyenite
- **Child of**:
 [`foid syenitoid`](#foid_syenitoid)
- Foid syenitoid rock that has a plagioclase to total feldspar ratio
of between 0.1 and 0.5. Includes rocks defined modally in QAPF Field
12.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Monzosyenite
- **Other Properties:**

[]{#foid_syenite}

#######  foid syenite
- **Child of**:
 [`foid syenitoid`](#foid_syenitoid)
- Foid syenitoid that has a plagioclase to total feldspar ratio of
less than 0.1. Includes rocks defined modally in QAPF field 11.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Syenite
- **Other Properties:**

[]{#foidolite}

######  foidolite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline rock containing more than 60 percent
feldspathoid minerals in the QAPF fraction. Includes rocks defined
modally in QAPF field 15
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foidolite
- **Other Properties:**

[]{#gabbroid}

######  gabbroid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals, and up to 20 percent quartz or up to 10
percent feldspathoid in the QAPF fraction. The ratio of plagioclase to
total feldspar is greater than 0.65, and anorthite content of the
plagioclase is greater than 50 percent. Includes rocks defined modally
in QAPF fields 9 and 10 and their subdivisions.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroid
- **Other Properties:**

[]{#gabbroic_rock}

#######  gabbroic rock
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`gabbroid`](#gabbroid)
- Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_gabbro}

########  foid bearing gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains 0-10 percent feldspathoid minerals and
no quartz in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Gabbro
- **Other Properties:**

[]{#gabbro}

########  gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Note that this category includes gabbro (sensu stricto) of LeMaitre
et al. 2002, but is broader, including the other rock types defined by
orthopyroxene-clinopyroxene-olivine-hornblende mineral ratios.
- Gabbroic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF Field 10 as gabbro.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gabbro
- **Other Properties:**

[]{#quartz_gabbro}

########  quartz gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Gabbro
- **Other Properties:**

[]{#monzogabbroic_rock}

#######  monzogabbroic rock
- **Child of**:
 [`gabbroid`](#gabbroid)
- Gabbroid with a plagioclase to total feldspar ratio between 0.65 and
0.9. QAPF field 9, 9 prime and 9 asterisk
- **Source:**
LeMaitre et al. 2002, This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Monzogabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_monzogabbro}

########  foid bearing monzogabbro
- **Child of**:
 [`monzogabbroic rock`](#monzogabbroic_rock)
- Monzogabbroic rock that contains 0 to 10 percent feldspathoid
mineral in the QAPF fraction. QAPF field 9'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzogabbro
- **Other Properties:**

[]{#monzogabbro}

########  monzogabbro
- **Child of**:
 [`monzogabbroic rock`](#monzogabbroic_rock)
- Monzogabbroic rock that contains between 0 an 5 percent quartz and
no feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF field 9 .
- **Source:**
LeMaitre et al. 2002, This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogabbro
- **Other Properties:**

[]{#quartz_monzogabbro}

########  quartz monzogabbro
- **Child of**:
 [`monzogabbroic rock`](#monzogabbroic_rock)
- Monzogabbroic rock that contains between 5 and 20 percent quartz in
the QAPF fraction. QAPF field 9*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzogabbro
- **Other Properties:**

[]{#granitoid}

######  granitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.
- **Alternate labels:**
granitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granitoid
- **Other Properties:**

[]{#alkali_feldspar_granite}

#######  alkali feldspar granite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitic rock that has a plagioclase to total feldspar ratio less
than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Alkali_Feldspar_Granite
- **Other Properties:**

[]{#granite}

#######  granite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting of quartz, alkali feldspar
and plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granite
- **Other Properties:**

[]{#monzogranite}

########  monzogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.35
and 0.65. QAPF field 3b.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogranite
- **Other Properties:**

[]{#syenogranite}

########  syenogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.10
and 0.35. QAPF field 3a.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenogranite
- **Other Properties:**

[]{#granodiorite}

#######  granodiorite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granodiorite
- **Other Properties:**

[]{#tonalite}

#######  tonalite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tonalite
- **Other Properties:**

[]{#hornblendite}

######  hornblendite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock that consists of greater than 40 percent hornblende
plus pyroxene and has a hornblende to pyroxene ratio greater than 1.
Includes olivine hornblendite, olivine-pyroxene hornblendite, pyroxene
hornblendite, and hornblendite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hornblendite
- **Other Properties:**

[]{#pegmatite}

######  pegmatite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Exceptionally coarse grained crystalline rock with interlocking
crystals; most grains are 1cm or more diameter; composition is
generally that of granite, but the term may refer to the coarse
grained facies of any type of igneous rock;usually found as irregular
dikes, lenses, or veins associated with plutons or batholiths.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pegmatite
- **Other Properties:**

[]{#peridotite}

######  peridotite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock consisting of more than 40 percent (by volume)
olivine with pyroxene and/or amphibole and little or no feldspar.
commonly altered to serpentinite. Includes rocks defined modally in
the ultramafic rock classification as dunite, harzburgite, lherzolite,
wehrlite, olivinite, pyroxene peridotite, pyroxene hornblende
peridotite or hornblende peridotite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Peridotite
- **Other Properties:**

[]{#pyroxenite}

######  pyroxenite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic phaneritic igneous rock composed almost entirely of one
or more pyroxenes and occasionally biotite, hornblende and olivine.
Includes rocks defined modally in the ultramafic rock classification
as olivine pyroxenite, olivine-hornblende pyroxenite, pyroxenite,
orthopyroxenite, clinopyroxenite and websterite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroxenite
- **Other Properties:**

[]{#quartz_rich_igneous_rock}

######  quartz rich igneous rock
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals and contains greater than 60 percent quartz in
the QAPF fraction.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Quartz_Rich_Igneous_Rock
- **Other Properties:**

[]{#syenitoid}

######  syenitoid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
mainly of alkali feldspar and plagioclase; minor quartz or nepheline
may be present, along with pyroxene, amphibole or biotite. Ratio of
plagioclase to total feldspar is less than 0.65, quartz forms less
than 20 percent of QAPF fraction, and feldspathoid minerals form less
than 10 percent of QAPF fraction. Includes rocks classified in QAPF
fields 6, 7 and 8 and their subdivisions.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Syenitoid
- **Other Properties:**

[]{#alkali_feldspar_syenitic_rock}

#######  alkali feldspar syenitic rock
- **Child of**:
 [`syenitoid`](#syenitoid)
- Syenitoid with a plagioclase to total feldspar ratio of less than
0.1. QAPF fields 6, 6*, and 6'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Syenitic_Rock
- **Other Properties:**

[]{#alkali_feldspar_syenite}

########  alkali feldspar syenite
- **Child of**:
 [`alkali feldspar syenitic rock`](#alkali_feldspar_syenitic_rock)
- Alkali feldspar syenitic rock that contains 0-5 percent quartz and
no feldspathoid in the QAPF fraction. QAPF field 6.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Syenite
- **Other Properties:**

[]{#foid_bearing_alkali_feldspar_syenite}

########  foid bearing alkali feldspar syenite
- **Child of**:
 [`alkali feldspar syenitic rock`](#alkali_feldspar_syenitic_rock)
- Alkali feldspar syenitic rock that contains 0-10 percent
feldspathoid mineral and no quartz in the QAPF fraction. QAPF field
6'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Alkali_Feldspar_Syenite
- **Other Properties:**

[]{#quartz_alkali_feldspar_syenite}

########  quartz alkali feldspar syenite
- **Child of**:
 [`alkali feldspar syenitic rock`](#alkali_feldspar_syenitic_rock)
- Alkali feldspar syenitic rock that contains 5 to 20 percent quartz
and no feldspathoid in the QAPF fraction. QAPF field 6*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Alkali_Feldspar_Syenite
- **Other Properties:**

[]{#monzonitic_rock}

#######  monzonitic rock
- **Child of**:
 [`syenitoid`](#syenitoid)
- Syenitoid with a plagioclase to total feldspar ratio between 0.35
and 0.65. Includes rocks in QAPF fields 8, 8*, and 8'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzonitic_Rock
- **Other Properties:**

[]{#foid_bearing_monzonite}

########  foid bearing monzonite
- **Child of**:
 [`monzonitic rock`](#monzonitic_rock)
- Monzonitic rock that contains 0-10 percent feldspathoid mineral and
no quartz in the QAPF fraction. Includes rocks defined modally in QAPF
Field 8'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzonite
- **Other Properties:**

[]{#monzonite}

########  monzonite
- **Child of**:
 [`monzonitic rock`](#monzonitic_rock)
- Monzonitic rock that contains 0-5 percent quartz and no feldspathoid
mineral in the QAPF fraction. Includes rocks defined modally in QAPF
Field 8.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzonite
- **Other Properties:**

[]{#quartz_monzonite}

########  quartz monzonite
- **Child of**:
 [`monzonitic rock`](#monzonitic_rock)
- Monzonitic rock that contains 5-20 percent quartz iin the QAPF
fraction. Includes rocks defined modally in QAPF Field 8*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzonite
- **Other Properties:**

[]{#syenitic_rock}

#######  syenitic rock
- **Child of**:
 [`syenitoid`](#syenitoid)
- Syenitoid with a plagioclase to total feldspar ratio between 0.1 and
0.35. Includes rocks in QAPF fields 7, 7*, and 7'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenitic_Rock
- **Other Properties:**

[]{#foid_bearing_syenite}

########  foid bearing syenite
- **Child of**:
 [`syenitic rock`](#syenitic_rock)
- Syenitic rock that contains between 0 and 10 percent feldspathoid
mineral and no quartz in the QAPF fraction. Defined modally in QAPF
Field 7'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Syenite
- **Other Properties:**

[]{#quartz_syenite}

########  quartz syenite
- **Child of**:
 [`syenitic rock`](#syenitic_rock)
- Syenitic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. Defined modally in QAPF Field 7*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Syenite
- **Other Properties:**

[]{#syenite}

########  syenite
- **Child of**:
 [`syenitic rock`](#syenitic_rock)
- Syenitic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Defined modally in QAPF
Field 7.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenite
- **Other Properties:**

[]{#plutonic_igneous_rock}

#####  plutonic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Instrusive igneous rock formed by crystallisation of magma far
enough below Earth surface that complete crystallization of magma
bodies forms holocrystalline medium to coarse grained igneous rock,
wall rocks generally do not include volcanic products related to the
magma, and some contact metamorphism is tyypically developed at
intrusive contacts.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Plutonic_Igneous_Rock
- **Other Properties:**

[]{#porphyry}

#####  porphyry
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock that contains conspicuous phenocrysts in a finer
grained groundmass; groundmass itself may be phaneritic or fine-
grained.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Porphyry
- **Other Properties:**

[]{#ultrabasic_igneous_rock}

#####  ultrabasic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock with less than 45 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Ultrabasic_Igneous_Rock
- **Other Properties:**

[]{#ultramafic_igneous_rock}

#####  ultramafic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock that consists of greater than 90 percent mafic
minerals.
- **Source:**
LeMaitre et al. 2002; Gillespie and Styles 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Ultramafic_Igneous_Rock
- **Other Properties:**

[]{#hornblendite}

######  hornblendite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock that consists of greater than 40 percent hornblende
plus pyroxene and has a hornblende to pyroxene ratio greater than 1.
Includes olivine hornblendite, olivine-pyroxene hornblendite, pyroxene
hornblendite, and hornblendite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hornblendite
- **Other Properties:**

[]{#peridotite}

######  peridotite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock consisting of more than 40 percent (by volume)
olivine with pyroxene and/or amphibole and little or no feldspar.
commonly altered to serpentinite. Includes rocks defined modally in
the ultramafic rock classification as dunite, harzburgite, lherzolite,
wehrlite, olivinite, pyroxene peridotite, pyroxene hornblende
peridotite or hornblende peridotite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Peridotite
- **Other Properties:**

[]{#pyroxenite}

######  pyroxenite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic phaneritic igneous rock composed almost entirely of one
or more pyroxenes and occasionally biotite, hornblende and olivine.
Includes rocks defined modally in the ultramafic rock classification
as olivine pyroxenite, olivine-hornblende pyroxenite, pyroxenite,
orthopyroxenite, clinopyroxenite and websterite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroxenite
- **Other Properties:**

[]{#komatiitic_rock}

######  komatiitic rock
- **Child of**:
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic, magnesium-rich volcanic rock, typically with spinifex
texture of intergrown skeletal and bladed olivine and pyroxene
crystals set in abundant glass. Includes komatiite and meimechite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Komatiitic_Rock
- **Other Properties:**

[]{#volcanic_rock}

#####  Volcanic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Volcanic Material`](#volcanic_material)
- Rock that exhibits direct evidence of extrusive igneous processes in
its genesis.
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Volcanic_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#lava}

######  Lava
- **Child of**:
 [`Volcanic rock`](#volcanic_rock)
- Volcanic Rock with features indicating origin by extrusive lava
flow.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Lava
- **Other Properties:**

[]{#impact_generated_material}

####  Impact generated material
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis material`](#composite_genesis_material)
- Material that contains features indicative of shock metamorphism,
such as microscopic planar deformation features within grains or
shatter cones, interpreted to be the result of extraterrestrial bolide
impact. Includes breccias and melt rocks.
- **Source:**
Stöffler and Grieve 2007; Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Impact_Generated_Material
- **Other Properties:**

[]{#massive_sulphide}

####  Massive sulphide
- **Child of**:
 [`Rock`](#rock)
- rock consisting of greater than 50% sulphide or sulfosalt minerals
formed by any processes. Includes hydrothermal and sedimentary
ehalative sulfide.
- **Alternate labels:**
Massive Sulfide
- **Source:**
Provisional SMR 2020-06-07
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Massive_Sulphide
- **Other Properties:**

[]{#hydrothermal_massive_sulphide}

#####  Hydrothermal Massive Sulphide
- **Child of**:
 [`Massive sulphide`](#massive_sulphide)
 [`metasomatic rock`](#metasomatic_rock)
- Rock consisting of greater that 50% sulphide or sulfosalt minerals
formed by hydrothermal mineralization processes.
- **Alternate labels:**
Hydrothermal Massive Sulfide
- **Source:**
provisional by SMR 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hydrothermal_Massive_Sulphide
- **Other Properties:**

[]{#sedimentary_massive_sulphide}

#####  Sedimentary Massive Sulphide
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`Massive sulphide`](#massive_sulphide)
- rock consisting of greater than 50% sulphide or sulfosalt minerals
formed by sedimentary exhalative processes.
- **Alternate labels:**
Sedimentary Massive Sulfide
- **Source:**
smr provisional 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sedimentary_Massive_Sulphide
- **Other Properties:**

[]{#metamorphic_rock}

####  Metamorphic rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis rock`](#composite_genesis_rock)
- Robertson (1999, Classification of metamorphic rocks: British
Geological Survey Research Report, RR 99–02) defines the boundary
between diagenesis and metamorphism in sedimentary rocks as follows:
“…the boundary between diagenesis and metamorphism is somewhat
arbitrary and strongly dependent on the lithologies involved. For
example changes take place in organic materials at lower temperatures
than in rocks dominated by silicate minerals. In mudrocks, a white
mica (illite) crystallinity value of less than 0.42 Delta 2 Theta
obtained by X-ray diffraction analysis, is used to define the onset of
metamorphism (Kisch, 1991). In this scheme, the first appearance of
glaucophane, lawsonite, paragonite, prehnite, pumpellyite or
stilpnomelane is taken to indicate the lower limit of metamorphism
(Frey and Kisch, 1987; Bucher and Frey, 1994; Frey and Robinson,
1998). Most workers agree that such mineral growth starts at 150 +/-
50° C in silicate rocks. Many lithologies may show no change in
mineralogy under these conditions and hence the recognition of the
onset of metamorphism will vary with bulk composition.”
- Rock formed by solid-state mineralogical, chemical and/or structural
changes to a pre-existing rock, in response to marked changes in
temperature, pressure, shearing stress and chemical environment.
- **Source:**
Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Metamorphic_Rock
- **Other Properties:**

[]{#amphibolite}

#####  amphibolite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock mainly consisting of green, brown or black
amphibole and plagioclase (including albite), which combined form 75
percent or more of the rock, and both of which are present as major
constituents. The amphibole constitutes 50 percent or more of the
total mafic constituents and is present in an amount of 30 percent or
more; other common minerals include quartz, clinopyroxene, garnet,
epidote-group minerals, biotite, titanite and scapolite.
- **Source:**
Coutinho et al. 2007, IUGS SCMR chapter 8 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Amphibolite
- **Other Properties:**

[]{#argillite}

#####  Argillite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- A weakly metamorphosed argillaceous rock (Flawn, 1953, AAPG Bull v37
p.563-664).  Rock is very fine-grained to aphanitic, compact,
indurated, and massive (lacks fissility or cleavage) (Neuendorf et al,
2004). Claystone and Siltstone are related, non-metamorphosed
sedimentary rocks. Like Aphanite but sedimentary protolith is
determined. In contact metamorphic environments would be Hornfels.
- **Source:**
Neuendorf et al, 2004, provisional SMR 2020-06-11
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Argillite
- **Other Properties:**

[]{#calcsilicate_metamorphic_rock}

#####  calc silicate metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Overlaps into metasomatic rocks because of high mobility of Ca
carbonates. Typically rich in epidote, diopside, tremolite, calcic-
amphibole, talc, with quartz and calcite. Might be gneiss or
granofels; lower metamorphic grade than granulite.
- metamorphic rock containing abundant calcium-silicate minerals
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcsilicate_Metamorphic_Rock
- **Other Properties:**

[]{#chlorite_actinolite_epidote_metamorphic_rock}

#####  chlorite actinolite epidote metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock classified as Greenschist is difficult to categorize in the CGI
SimpleLithology scheme. This stems in part from the variation in usage
and the general fuzzy definition of the term. The definition of
greenschist is generally something along the lines of 'metamorphosed
rock with a greenish colour, characterized by the presence of
actinolite, chlorite and epidote, and containing a planar or linear
fabric. The presence or absence of schistose fabric in rocks called
'greenschist' is problematic. The fabric present in many rocks called
greenschist is too weak or variably developed to meet the definition
of 'schist' per CGI SimpleLithology. Generally if the rock has
achieved metamorphic grade such that the term 'gneiss' is applicable,
it would not be called greenschist. Thus, 'greenschist' would
correspond most closely to a chlorite + actinolite rich 'Foliated
metamorphic rock', but if it actually meets the definition of 'Schist'
it would be a chlorite + actinolite 'Schist'.
- Metamorphic rock characterized by 50 percent or more of combined
chlorite, actinolite and epidote. Category for rocks generally named
greenschist or greenstone.
- **Alternate labels:**
greenstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chlorite_Actinolite_Epidote_Metamorphic_Rock
- **Other Properties:**

[]{#eclogite}

#####  eclogite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock composed of 75 percent or more (by volume)
omphacite and garnet, both of which are present as major constituents,
the amount of neither of them being higher than 75 percent (by
volume); the presence of plagioclase precludes classification as an
eclogite.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Eclogite
- **Other Properties:**

[]{#foliated_metamorphic_rock}

#####  foliated metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock in which 10 percent or more of the contained
mineral grains are elements in a planar or linear fabric. Cataclastic
or glassy character precludes classification with this concept.
- **Source:**
based on NADM SLTT metamorphic
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foliated_Metamorphic_Rock
- **Other Properties:**

[]{#mylonitic_rock}

######  mylonitic rock
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Metamorphic rock characterised by a foliation resulting from
tectonic grain size reduction, in which more than 10 percent of the
rock volume has undergone grain size reduction. Includes
protomylonite, mylonite, ultramylonite, and blastomylonite.
- **Source:**
Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mylonitic_Rock
- **Other Properties:**

[]{#phyllonite}

#######  phyllonite
- **Child of**:
 [`mylonitic rock`](#mylonitic_rock)
- Mylonitic rock composed largely of fine-grained mica that imparts a
sheen to foliation surfaces; may have flaser lamination, isoclinal
folding, and deformed veins, which indicate significant shearing.
Macroscopically resembles phyllite, but formed by mechanical
degradation of initially coarser rock.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllonite
- **Other Properties:**

[]{#gneiss}

######  gneiss
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Foliated metamorphic rock with bands or lenticles rich in granular
minerals alternating with bands or lenticles rich in minerals with a
flaky or elongate prismatic habit. Mylonitic foliation or well
developed, continuous schistosity (greater than 50 percent of the rock
consists of grains participate in a planar or linear fabric) precludes
classification with this concept.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gneiss
- **Other Properties:**

[]{#orthogneiss}

#######  orthogneiss
- **Child of**:
 [`gneiss`](#gneiss)
- A gneiss with mineralogy and texture indicating derivation from a
phaneritic igneous rock protolith. Typically consists of abundant
feldspar, with quartz, and variable hornblende, biotite, and
muscovite, with a relatively homogeneous character.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Orthogneiss
- **Other Properties:**

[]{#paragneiss}

#######  paragneiss
- **Child of**:
 [`gneiss`](#gneiss)
- A gneiss with mineralogy and texture indicating derivation from a
sedimentary rock protolith. Typically consists of abundant quartz,
mica, or calcsilicate minerals; aluminosilicate minerals or garnet
commonly present. composition of rock tends to be more variable on a
decimetric scale that in orthogneiss.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Paragneiss
- **Other Properties:**

[]{#phyllite}

######  phyllite
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Rock with a well developed, continuous schistosity, an average grain
size between 0.1 and 0.5 millimeters, and a silvery sheen on cleavage
surfaces. Individual phyllosilicate grains are barely visible with the
unaided eye.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllite
- **Other Properties:**

[]{#schist}

######  schist
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Foliated phaneritic metamorphic rock with well developed, continuous
schistosity, meaning that greater than 50 percent of the rock by
volume is mineral grains with a thin tabular, lamellar, or acicular
prismatic crystallographic habit that are oriented in a continuous
planar or linear fabric.
- **Source:**
SLTTm 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Schist
- **Other Properties:**

[]{#mica_schist}

#######  mica schist
- **Child of**:
 [`schist`](#schist)
- Include single subcategory of schist to indicate this common kind of
schist. 'Mica rich metamorphic rock' for compound use with schist
fabric term would be more compatible with treatment of blueschist
(Glaucophane lawsonite epidote metamorphic rock) and greenschist
(Chlorite actinolite epidote metamorphic rock), but based on the
assumption that schist is the only rock type that will meet the mica-
rich criteria, it seems reasonable to include as a subtype of schist.
- A schist that consists of more than 50 percent mica minerals,
typically muscovite or biotite. Special type included to distinguish
this common variety of schist.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mica_Schist
- **Other Properties:**

[]{#slate}

######  slate
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- compact, fine grained rock with an average grain size less than
0.032 millimeter and a well developed schistosity (slaty cleavage),
and hence can be split into slabs or thin plates.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Slate
- **Other Properties:**

[]{#glaucophane_lawsonite_epidote_metamorphic_rock}

#####  glaucophane lawsonite epidote metamorphic rock
* `glaukophanschiefer`
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Fabric is weakly developed in this rock in many cases, so the fabric
categories 'foliated metamorphic rock, 'schist' or 'granofels' may
apply.
- A metamorphic rock of roughly basaltic composition, defined by the
presence of glaucophane with lawsonite or epidote. Other minerals that
may be present include jadeite, albite, chlorite, garnet, and
muscovite (phengitic white mica). Typically fine-grained, dark
colored. Category for rocks commonly referred to as blueschist.
- **Alternate labels:**
blauschiefer, 
blueschist, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Glaucophane_Lawsonite_Epidote_Metamorphic_Rock
- **Other Properties:**

[]{#granofels}

#####  granofels
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock with granoblastic fabric and very little or no
foliation (less than 10 percent of the mineral grains in the rock are
elements in a planar or linear fabric). Grainsize not specified.
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Granofels
- **Other Properties:**

[]{#hornfels}

######  hornfels
- **Child of**:
 [`granofels`](#granofels)
- Granofels formed by contact metamorphism, composed of a mosaic of
equidimensional grains in a characteristically granoblastic or
decussate matrix; porphyroblasts or relict phenocrysts may be present.
Typically fine grained.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hornfels
- **Other Properties:**

[]{#granulite}

#####  granulite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Wimmenauer (1985) requires granulite to consist of at least 20
percent feldspar. Garnet is frequently present; some hornblende or
biotite may be present. The rock has a granoblastic texture and
gneissose to massive structure; grain size and fabric may be variable
on a decimetric scale. Foliation is less well developed than in rock
that would typically be called gneiss. The minerals present in a
granulite vary depending on the protolith and the temperature and
pressure conditions experienced during metamorphism. According to
Fettes and Desmons (2007) the main calc-silicate minerals are calcic
garnet, calcic plagioclase, calcic scapolite, diopside-hedenbergite,
epidote group minerals, hydrogrossular, johannsenite, prehnite,
pumpellyite, titanite, vesuvianite, wollastonite. Note that the shale
and siltstone categories may apply to any of the mineralogically
defined mudstone categories.
- Metamorphic rock of high metamorphic grade in which Fe-Mg silicate
minerals are dominantly hydroxl-free; feldspar must be present, and
muscovite is absent; rock contains less than 90 percent mafic
minerals, less than 75 percent calcite and/or dolomite, less than 75
percent quartz, less than 50 percent iron-bearing minerals (hematite,
magnetite, limonite-group, siderite, iron-sulfides), and less than 50
percent calc-silicate minerals.
- **Source:**
Fettes and Desmons (2007). See also Wimmenauer (1985), Winkler (1979) (D.R. Bowes (1989), The Encyclopedia of Igneous and Metamorphic Petrology; Van Nostrand Reinhold ISBN: 0-442-20623-2 ; wikipedia, http://en.wikipedia.org/wiki/Granulite accessed 5/30/09
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Granulite
- **Other Properties:**

[]{#marble}

#####  marble
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock consisting of greater than 75 percent fine- to
coarse-grained recrystallized calcite and/or dolomite; usually with a
granoblastic, saccharoidal texture.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/), SLTTm1.0 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Marble
- **Other Properties:**

[]{#metaplutonic_rock}

#####  metaplutonic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of a plutonic igneous protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metaplutonic_Rock
- **Other Properties:**

[]{#metasedimentary_rock}

#####  metasedimentary rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of a sedimentary protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metasedimentary_Rock
- **Other Properties:**

[]{#metavolcanic_rock}

#####  metavolcanic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of an extrusive igneous protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metavolcanic_Rock
- **Other Properties:**

[]{#migmatite}

#####  migmatite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Silicate metamorphic rock that is pervasively heterogeneous on a
decimeter to meter scale that typically consists of darker and lighter
parts; the darker parts usually exhibit features of metamorphic rocks
whereas the lighter parts are of igneous-looking appearance.
- **Source:**
Fette and Desmons (2007) (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Migmatite
- **Other Properties:**

[]{#quartzite}

#####  quartzite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock consisting of greater than or equal to 75 percent
quartz; typically granoblastic texture.
- **Source:**
after Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartzite
- **Other Properties:**

[]{#serpentinite}

#####  serpentinite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock consisting of more than 75 percent serpentine-group minerals,
eg. antigorite, chrysotile or lizardite; accessory chlorite, talc and
magnetite may be present; derived from hydration of ferromagnesian
silicate minerals such as olivine and pyroxene.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Serpentinite
- **Other Properties:**

[]{#metasomatic_rock}

####  metasomatic rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis rock`](#composite_genesis_rock)
- SLTTm (2004) proposed the following criteria to distinguish
hydrothermally altered or metasomatic rock from igneous rock. "The
rock is classified as metamorphic if (1) the texture has been modified
such that it can no longer be considered igneous, (2) the bulk
composition of the rock is inconsistent with compositions that can be
derived purely from a magma and associated processes such as
assimilation and differentiation, or (3) minerals inconsistent with
magmatic crystallization are present."
- Rock that has fabric and composition indicating open-system
mineralogical and chemical changes in response to interaction with a
fluid phase, typically water rich.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Metasomatic_Rock
- **Other Properties:**

[]{#altered_rock}

#####  Altered, type not specified
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Rock material has been changed by some subsurface alteration
process, but the nature of the alteration is not specified.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Altered_Rock
- **Other Properties:**

[]{#advanced_argillic_altered_rock}

######  advanced argillic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Advanced argillic alteration occurs under lower pH and higher
temperature conditions than argillic alteration. Kaolinite and dickite
occur at lower temperatures whereas pyrophyllite and andalusite occur
under high temperature conditions (T > 300°C). Quartz deposition is
common. Alunite, topaz, zunyite, tourmaline, enargite and tennantite
may also occur. In many cases, advanced argillic alteration zones, or
“lithocaps”, develop at shallow levels above porphyry Cu–Au deposits
(e.g., Lepanto-Far Southeast, Philippines; Maricunga, Chile). Advanced
argillic alteration mineral assemblages precipitate from SO2- and HCl-
rich magmatic vapor, which arises from an underlying intrusive source,
and can also form in supergene environments, due to post-hydrothermal
weathering and oxidation of pyrite, locally creating pH<1 liquid due
to high concentrations of H2SO4 within the vadose zone, where
kaolinite and alunite plus Fe hydroxides form.
- **Source:**
Antonio Arribas, Jeffrey Hedenquist, 2019, Environments of advanced argillic alteration: II) steam-heated, and exploration implications: Conference: Society of Resource Geology Annual SymposiumAt: University of Tokyo, Tokyo (Japan)Volume: 69, accessed at https://www.researchgate.net/publication/334230797_Environments_of_advanced_argillic_alteration_II_steam-heated_and_exploration_implications#fullTextFileContent; Constantinos Mavrogonatos et al., 2018, Mineralogical Study of the Advanced Argillic Alteration Zone at the Konos Hill Mo–Cu–Re–Au Porphyry Prospect, NE Greece: Minerals, 8, 479; doi:10.3390/min8110479;  https://en.wikipedia.org/wiki/Argillic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/advanced_argillic_altered_rock
- **Other Properties:**

[]{#albitic_altered_rock}

######  albitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/albitic_altered_rock
- **Other Properties:**

[]{#alunitic_altered_rock}

######  alunitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/alunitic_altered_rock
- **Other Properties:**

[]{#argillic_altered_rock}

######  argillic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Argillic alteration is hydrothermal alteration of wall rock which
introduces clay minerals including kaolinite, smectite and illite. The
process generally occurs at low temperatures and may occur in
atmospheric conditions. Argillic alteration is representative of
supergene environments where low temperature groundwater becomes
acidic. Argillic assemblages include kaolinite replacing plagioclase
and montmorillonite replacing amphibole and plagioclase. Orthoclase is
generally stable and unaffected. Argillic grades into phyllic
alteration at higher temperatures in an ore deposit hydrothermal
system.
- **Source:**
https://en.wikipedia.org/wiki/Argillic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/argillic_altered_rock
- **Other Properties:**

[]{#calcsilicate_altered_rock}

######  calcsilicate altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/calcsilicate_altered_rock
- **Other Properties:**

[]{#carbonate_altered_rock}

######  carbonate altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/carbonate_altered_rock
- **Other Properties:**

[]{#chloritic_altered_rock}

######  chloritic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/chloritic_altered_rock
- **Other Properties:**

[]{#deuteric_altered_rock}

######  deuteric altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/deuteric_altered_rock
- **Other Properties:**

[]{#epidote_altered_rock}

######  epidote altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/epidote_altered_rock
- **Other Properties:**

[]{#hematitic_altered_rock}

######  hematitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Alteration characterized by finely dispersed hematite
- **Alternate labels:**
red rock altered rock
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24, 
Williams, P.J., 1994, Aust. J. Earth Science, v41, p381-382, 
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/hematitic_altered_rock
- **Other Properties:**

[]{#kaolinitic_altered_rock}

######  kaolinitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/kaolinitic_altered_rock
- **Other Properties:**

[]{#phyllic_altered_rock}

######  phyllic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Altered rock characterised by the assemblage of quartz + sericite +
pyrite, and occurs at high temperatures and moderately acidic (low pH)
conditions. Typically associated with copper porphyry ore deposits in
calc-alkaline rocks.
- **Source:**
https://en.wikipedia.org/wiki/Phyllic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/phyllic_altered_rock
- **Other Properties:**

[]{#potassic_altered_rock}

######  potassic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/potassic_altered_rock
- **Other Properties:**

[]{#propylitic_altered_rock}

######  propylitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/propylitic_altered_rock
- **Other Properties:**

[]{#pyritic_altered_rock}

######  pyritic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/pyritic_altered_rock
- **Other Properties:**

[]{#saussuritised_rock}

######  saussuritised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Rock in which calcium-bearing plagioclase feldspar is altered to an
assemblage of minerals called saussurite, typically including zoisite,
chlorite, amphibole, and carbonate minerals. Residual fluids present
during the late stages of magmatic crystallization can react with
previously formed plagioclase feldspar to form saussurite; the
saussurite will be spread through the plagioclase or located near its
outer margin. The plagioclase may be reconstituted into a more sodium-
rich variety (albite), although the original form of the crystal is
retained. Later hydrothermal alteration can produce the same result.
Mafic rocks are especially susceptible to saussuritization owing to
their high calcium content; the more calcium-rich portions of
plagioclase in acidic rocks also are often saussuritized.
- **Source:**
https://www.britannica.com/science/saussuritization
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/saussuritised_rock
- **Other Properties:**

[]{#sericitic_altered_rock}

######  sericitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Rock in which plagioclase feldspar has been converted to sericite,
an informal term for  fine-grained white phyllosilicate minerals.
Commonly associated with phyllic altered rocks, used to describe less
intense alteration.
- **Source:**
https://en.wikipedia.org/wiki/Sericitic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/sericitic_altered_rock
- **Other Properties:**

[]{#serpentinised_rock}

######  serpentinised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/serpentinised_rock
- **Other Properties:**

[]{#silicified_rock}

######  silicificed rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/silicified_rock
- **Other Properties:**

[]{#uralitised_rock}

######  uralitised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/uralitised_rock
- **Other Properties:**

[]{#zeolitic_altered_rock}

######  zeolitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/zeolitic_altered_rock
- **Other Properties:**

[]{#greisen}

#####  Greisen
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Greisen is a class of endoskarn,  formed by self-generated
alteration of a granite. Greisens appear as partly coarse, crystalline
granite, partly vuggy with miarolitic cavities, disseminated halide
minerals such as fluorite, and occasionally metallic oxide and sulfide
ore minerals, borate minerals (tourmaline) and accessory phases such
as sphene, beryl or topaz.
- **Source:**
https://en.wikipedia.org/wiki/Greisen
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Greisen
- **Other Properties:**

[]{#hydrothermal_massive_sulphide}

#####  Hydrothermal Massive Sulphide
- **Child of**:
 [`Massive sulphide`](#massive_sulphide)
 [`metasomatic rock`](#metasomatic_rock)
- Rock consisting of greater that 50% sulphide or sulfosalt minerals
formed by hydrothermal mineralization processes.
- **Alternate labels:**
Hydrothermal Massive Sulfide
- **Source:**
provisional by SMR 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hydrothermal_Massive_Sulphide
- **Other Properties:**

[]{#skarn}

#####  skarn
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Metasomatic rock consisting mainly of Ca-, Mg-, Fe-, or Mn-silicate
minerals, which are free from or poor in water. Typically formed at
the contact between a silicate rock or magma and a carbonate rock.
- **Alternate labels:**
exoskarn, 
tactite, 
- **Source:**
Fettes and Desmons, 2007, p195
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Skarn
- **Other Properties:**

[]{#spilite}

#####  spilite
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Altered basic to intermediate composition fine-grained igneous rock
in which the feldspar is partially or completely composed of of
albite, typically accompanied by chlorite, calcite, quartz, epidote,
prehnite, and low-tempaerature hydrous crystallization products.
Preservation of eruptive volcanic features is typical.
- **Source:**
Fettes and Desmon, 2007; Best, M.G., 1982, Igneous and metamorphic petrology: New York, W.H. Freeman and company, p. 398; Neuendorf et al. 2005, p. 619.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Spilite
- **Other Properties:**

[]{#sedimentary_rock}

####  Sedimentary rock
- **Child of**:
 [`Rock`](#rock)
 [`Sedimentary material`](#sedimentary_material)
- Rock formed by accumulation and cementation of solid fragmental
material deposited by air, water or ice, or as a result of other
natural agents, such as precipitation from solution, the accumulation
of organic material, or from biogenic processes, including secretion
by organisms. Includes epiclastic deposits.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Sedimentary_Rock
- **Other Properties:**

[]{#carbonate_sedimentary_rock}

#####  carbonate sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Particularly for fine-grained sedimentary rocks, distinction of
'intrabasinal' versus 'clastic' genesis can be very interpretive. In
practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored. Carbonate
rock subcatgories are defined on two orthogonal dimensions--mineralogy
(calcitic vs. dolomitic vs non-carbonate impurities), and texture. The
texture categories used here are those of Dunham (1962), and involve
grain size (matrix vs. grains/allochems), fabric (matrix vs. grain
supported), and genesis (bound, frame, or fragmental). The textural
approach used for carbonate rocks is conceptually incompatible with
that used for clastic sedimentary rocks, which is solely grain size or
mineralogy based. This leads to problems in the vocabulary for rocks
of mixed siliclastic/carbonate mineralogy (grainstone vs. sandstone,
carbonate mudstone vs. carbonate rich mudstone, how to accomodate
marlstone...).
- Sedimentary rock in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite, magnesite or dolomite.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#boundstone}

######  boundstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary carbonate rock with preserved biogenic texture, whose
original components were bound and encrusted together during
deposition by the action of plants and animals during deposition, and
remained substantially in the position of growth.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boundstone
- **Other Properties:**

[]{#calcareous_carbonate_sedimentary_rock}

######  calcareous carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
SLTTs 2004; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#carbonate_mudstone}

######  carbonate mudstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Not a subcategory of carbonate sedimentary rock because definition
does not specify 'carbonate minerals of intrabasinal origin', but is
agnostic on origin of carbonate. Schnurrenberger et al. 2003 point out
that it is very difficult (at least in lacustrine rocks) to
distinguish chemically precipitated or diagenetic carbonate from
primary biogenic carbonate. This distinction between biogenic,
detrital, and pedogenic or authigenic carbonate material is thus not a
good one to use in a general purpose classification system.
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Mudstone that consists of greater than 50 percent carbonate minerals
of any origin in the mud size fraction.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mudstone
- **Other Properties:**

[]{#carbonate_wackestone}

######  carbonate wackestone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate sedimentary rock with discernible mud supported
depositional texture and containing greater than 10 percent allochems,
and constituent particles are of intrabasinal origin. If particles are
not intrabasinal, categorization as a mudstone or wackestone should be
considered.
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Wackestone
- **Other Properties:**

[]{#crystalline_carbonate}

######  crystalline carbonate
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate rock of indeterminate mineralogy in which diagenetic
processes have obliterated any original depositional texture.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Crystalline_Carbonate
- **Other Properties:**

[]{#dolomitic_or_magnesian_sedimentary_rock}

######  dolomitic or magnesian sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sedimentary rock with a ratio of magnesium carbonate to
calcite (plus aragonite) greater than 1 to 1. Includes dolostone, lime
dolostone and magnesite-stone.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Or_Magnesian_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#framestone}

######  framestone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate reef rock consisting of a rigid framework of colonies,
shells or skeletons, with internal cavities filled with fine sediment;
usually created through the activities of colonial organisms.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004, Table 15-3-1
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Framestone
- **Other Properties:**

[]{#grainstone}

######  grainstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate sedimentary rock with recognizable depositional fabric
that is grain-supported, and constituent particles are of intrabasinal
origin; contains little or no mud matrix. Distinction from sandstone
is based on interpretation of intrabasinal origin of clasts and grain-
supported fabric, but grainstone definition does not include a grain
size criteria.
- **Alternate labels:**
carbonate grainstone
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Grainstone
- **Other Properties:**

[]{#impure_carbonate_sedimentary_rock}

######  impure carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary rock in which between 50 and 90 percent of the primary
and/or recrystallized constituents are composed of carbonate minerals.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#packstone}

######  packstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Note that this category overlaps with 'carbonate mudstone'.
- Carbonate sedimentary rock with discernible grain supported
depositional texture, containing greater than 10 percent grains, and
constituent particles are of intrabasinal origin; intergranular spaces
are filled by matrix.
- **Source:**
Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Packstone
- **Other Properties:**

[]{#pure_carbonate_sedimentary_rock}

######  pure carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary rock in which greater than 90 percent of the primary
and/or recrystallized constituents are carbonate minerals.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#pure_carbonate_mudstone}

#######  pure carbonate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Mudstone that consists of greater than 90 percent carbonate minerals
of intrabasinal orign in the mud fraction, and contains less than 10
percent allochems. The original depositional texture is preserved and
fabric is matrix supported. Carbonate mudstone of Dunham (1962)
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Mudstone
- **Other Properties:**

[]{#clastic_sedimentary_rock}

#####  clastic sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`clastic sedimentary material`](#clastic_sedimentary_material)
- The conglomerate, sandstone, mudstone, and wackestone categories are
not defined as kinds of clastic sedimentary rocks because rocks
meeting their purely grainsize based definitions might also be iron-
rich, phosphatic, or carbonate. This is based on GeoSciML allowance to
assign rocks to more than one lithology category. For example to
categorize a rock as a clastic conglomerate requires assignment ot the
'clastic sedimentary rock' category and to the 'conglomerate'
category. Particularly for fine-grained sedimentary rocks, distinction
of 'intrabasinal' versus 'clastic' genesis can be very interpretive.
In practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored.
- Sedimentary rock in which at least 50 percent of the constituent
particles were derived from erosion, weathering, or mass-wasting of
pre-existing earth materials, and transported to the place of
deposition by mechanical agents such as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Clastic_Sedimentary_Rock
- **Other Properties:**

[]{#diamictite}

######  diamictite
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
- Unsorted or poorly sorted, clastic sedimentary rock with a wide
range of particle sizes including a muddy matrix. Biogenic materials
that have such texture are excluded. Distinguished from conglomerate,
sandstone, mudstone based on polymodality and lack of structures
related to transport and deposition of sediment by moving air or
water. If more than 10 percent of the fine grained matrix is of
indeterminant clastic or diagenetic origin and the fabric is matrix
supported, may also be categorized as wacke.
- **Source:**
Fairbridge and Bourgeois 1978
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Diamictite
- **Other Properties:**

[]{#clastic_conglomerate}

######  conglomerate
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic conglomerate`](#generic_conglomerate)
- Note this category is equivalent to category labeled 'Conglomeratic
rock in SLTTs (2004), not to the category labeled 'Conglomerate' in
that system.
- Clastic sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Alternate labels:**
conglomeratic rock
- **Source:**
Neuendorf et al. 2005; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Conglomerate
- **Other Properties:**

[]{#clastic_mudstone}

######  mudstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is interpretive in many cases. If
there is uncertainty on the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system, it is recommended to
use the generic_mudstone category. This category is the union of the
various fields labeled 'mudstone' with various qualifiers in Folk,
1954, Figure 1a, although Folk's (1954) category labeled 'mudstone' is
a much more restricted category. The CGI category is equivalent to
category labeled 'Mudrock' in SLTTs (2004), not to the category
labeled 'Mudstone' adopted by that system from Folk (1954).
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Clastic sedimentary rock consisting of less than 30 percent gravel-
size (2 mm) particles and with a mud to sand ratio greater than 1.
- **Alternate labels:**
clastic mudstone, 
mudrock, 
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Mudstone
- **Other Properties:**

[]{#claystone}

#######  claystone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Mudstone that contains no detectable silt, inferred to consist
virtually entirely of clay-size particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Claystone
- **Other Properties:**

[]{#shale}

#######  shale
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Note definition does not specify carbonate vs. siliclastic nature of
mud.
- Laminated mudstone that will part or break along thin, closely
spaced layers parallel to stratification.
- **Source:**
NADM SLTT sedimentary, 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Shale
- **Other Properties:**

[]{#siltstone}

#######  siltstone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Use of 'detectable silt' in the criteria for this category is based
on the observation that in practice, distinction of claystone from
'siltstone' is typically based on a qualitative assessment of
'grittiness' (e.g. rubbing with fingers, or chewing); the property
that these tests can determine is the presence or absence of silty
particles in the material. Quantitative grain size analysis in the the
clay/silt fraction of a lithified sediment is difficult at best, and
of questionable significance because diagensis has altered the size
and mineralogy of original sedimentary particles.
- Mudstone that contains detectable silt. (see comments)
- **Alternate labels:**
Silt bearing mudstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siltstone
- **Other Properties:**

[]{#clastic_sandstone}

######  sandstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`Generic sandstone`](#generic_sandstone)
- Note this category is equivalent to cagetory labeled 'sandy rock' in
SLTTs (2004), not to the much more restricted category labeled
'Sandstone' in that system.
- Clastic sedimentary rock in which less than 30 percent of particles
are greater than 2 mm in diameter (gravel) and the sand to mud ratio
is at least 1.
- **Alternate labels:**
clastic sandstone, 
sandy rock, 
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Sandstone
- **Other Properties:**

[]{#arenite}

#######  arenit
* `arenite`
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Clastic sandstone that contains less than 10 percent matrix. Matrix
is mud-size silicate minerals (clay, feldspar, quartz, rock fragments,
and alteration products) of detrital or diagenetic nature.
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Arenite
- **Other Properties:**

[]{#wacke}

#######  wacke
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Distinction from mudstone is based on inference that less that 50
percent of the mud size fraction (matrix) is original mud size
detrital particles. May also grade into diamictite or conglomerate
based on size distribution of discernible particles. If more than 50
percent of rock is detrital particles of intrabasinal orgin and
carbonate composition, categorize as carbonate wackestone. Term is
typically applied to diagenetically altered volcanic-lithic clastic
rocks in which the definition of the original clasts has been
obscured. Suggested boundaries between wacke and arenite range from 5
to 15 percent matrix. See Dickinson (1970) for discussion of
interpretation of undiscernible matrix in diagenetically altered
lithic clastic rocks. Dickinson, W.R., 1970, Interpreting detrital
modes of graywacke and arkose: Journal of Sedimentary Petrology, v.
40, p. 695-707.
- Clastic sandstone with more than 10 percent matrix of indeterminate
detrital or diagenetic nature. Matrix is mud size silicate minerals
(clay, feldspar, quartz, rock fragments, and alteration products).
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Wacke
- **Other Properties:**

[]{#generic_conglomerate}

#####  generic conglomerate
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Source:**
Neuendorf et al. 2005; SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Generic_Conglomerate
- **Other Properties:**

[]{#clastic_conglomerate}

######  conglomerate
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic conglomerate`](#generic_conglomerate)
- Note this category is equivalent to category labeled 'Conglomeratic
rock in SLTTs (2004), not to the category labeled 'Conglomerate' in
that system.
- Clastic sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Alternate labels:**
conglomeratic rock
- **Source:**
Neuendorf et al. 2005; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Conglomerate
- **Other Properties:**

[]{#generic_mudstone}

#####  generic mudstone
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is so interpretive that it is proposed
to not define the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system. Schnurrenberger, D.,
Russell, J. and Kelts, K., 2003, Classification of lacustrine
sediments based on sedimentary components: Journal of Paleolimnology,
v.29, p141-154.
- Sedimentary rock consisting of less than 30 percent gravel-size (2
mm) particles and with a mud to sand ratio greater than 1. Clasts may
be of any composition or origin.
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999; extrapolated from Folk, 1954, Figure 1a; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Generic_Mudstone
- **Other Properties:**

[]{#carbonate_mudstone}

######  carbonate mudstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Not a subcategory of carbonate sedimentary rock because definition
does not specify 'carbonate minerals of intrabasinal origin', but is
agnostic on origin of carbonate. Schnurrenberger et al. 2003 point out
that it is very difficult (at least in lacustrine rocks) to
distinguish chemically precipitated or diagenetic carbonate from
primary biogenic carbonate. This distinction between biogenic,
detrital, and pedogenic or authigenic carbonate material is thus not a
good one to use in a general purpose classification system.
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Mudstone that consists of greater than 50 percent carbonate minerals
of any origin in the mud size fraction.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mudstone
- **Other Properties:**

[]{#carbonate_rich_mudstone}

######  carbonate rich mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
- Carbonate-rich mudstone' definition limits carbonate to mud-size
fraction to avoid overlap with 'impure carbonate sedimentary rock'. If
carbonate minerals are in sand or gravel size fractions, use 'impure
carbonate sedimentary rock'. The operational test typically used to
identify this category is if the rock fizzes when hydrochloric acid is
applied. The '10 percent carbonate' criteria is a fuzzy boundary.
- Mudstone that contains between 10 and 50 percent carbonate minerals
in the mud size fraction. Carbonate origin is not specified.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Rich_Mudstone
- **Other Properties:**

[]{#clastic_mudstone}

######  mudstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is interpretive in many cases. If
there is uncertainty on the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system, it is recommended to
use the generic_mudstone category. This category is the union of the
various fields labeled 'mudstone' with various qualifiers in Folk,
1954, Figure 1a, although Folk's (1954) category labeled 'mudstone' is
a much more restricted category. The CGI category is equivalent to
category labeled 'Mudrock' in SLTTs (2004), not to the category
labeled 'Mudstone' adopted by that system from Folk (1954).
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Clastic sedimentary rock consisting of less than 30 percent gravel-
size (2 mm) particles and with a mud to sand ratio greater than 1.
- **Alternate labels:**
clastic mudstone, 
mudrock, 
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Mudstone
- **Other Properties:**

[]{#claystone}

#######  claystone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Mudstone that contains no detectable silt, inferred to consist
virtually entirely of clay-size particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Claystone
- **Other Properties:**

[]{#shale}

#######  shale
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Note definition does not specify carbonate vs. siliclastic nature of
mud.
- Laminated mudstone that will part or break along thin, closely
spaced layers parallel to stratification.
- **Source:**
NADM SLTT sedimentary, 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Shale
- **Other Properties:**

[]{#siltstone}

#######  siltstone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Use of 'detectable silt' in the criteria for this category is based
on the observation that in practice, distinction of claystone from
'siltstone' is typically based on a qualitative assessment of
'grittiness' (e.g. rubbing with fingers, or chewing); the property
that these tests can determine is the presence or absence of silty
particles in the material. Quantitative grain size analysis in the the
clay/silt fraction of a lithified sediment is difficult at best, and
of questionable significance because diagensis has altered the size
and mineralogy of original sedimentary particles.
- Mudstone that contains detectable silt. (see comments)
- **Alternate labels:**
Silt bearing mudstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siltstone
- **Other Properties:**

[]{#organic_bearing_mudstone}

######  organic bearing mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
- Mudstone that contains a significant amount of organic carbon,
typically kerogen. commonly finely laminated, brown or black in color.
- **Alternate labels:**
oil shale
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Oil_shale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Organic_Bearing_Mudstone
- **Other Properties:**

[]{#pure_carbonate_mudstone}

######  pure carbonate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Mudstone that consists of greater than 90 percent carbonate minerals
of intrabasinal orign in the mud fraction, and contains less than 10
percent allochems. The original depositional texture is preserved and
fabric is matrix supported. Carbonate mudstone of Dunham (1962)
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Mudstone
- **Other Properties:**

[]{#silicate_mudstone}

######  silicate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
- Operational distinction of this category will typically be based on
whether or not the rock fizzes when hydrochloric acid is applied--the
rock is silicate mudstone if it does not fizz. The quantitative '10
percent' criteria is fuzzy.
- Mudstone that contains less than 10 percent carbonate minerals.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silicate_Mudstone
- **Other Properties:**

[]{#generic_sandstone}

#####  Generic sandstone
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Sedimentary rock in which less than 30 percent of particles are
greater than 2 mm in diameter (gravel) and the sand to mud ratio is at
least 1.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Generic_Sandstone
- **Other Properties:**

[]{#clastic_sandstone}

######  sandstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`Generic sandstone`](#generic_sandstone)
- Note this category is equivalent to cagetory labeled 'sandy rock' in
SLTTs (2004), not to the much more restricted category labeled
'Sandstone' in that system.
- Clastic sedimentary rock in which less than 30 percent of particles
are greater than 2 mm in diameter (gravel) and the sand to mud ratio
is at least 1.
- **Alternate labels:**
clastic sandstone, 
sandy rock, 
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Sandstone
- **Other Properties:**

[]{#arenite}

#######  arenit
* `arenite`
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Clastic sandstone that contains less than 10 percent matrix. Matrix
is mud-size silicate minerals (clay, feldspar, quartz, rock fragments,
and alteration products) of detrital or diagenetic nature.
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Arenite
- **Other Properties:**

[]{#wacke}

#######  wacke
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Distinction from mudstone is based on inference that less that 50
percent of the mud size fraction (matrix) is original mud size
detrital particles. May also grade into diamictite or conglomerate
based on size distribution of discernible particles. If more than 50
percent of rock is detrital particles of intrabasinal orgin and
carbonate composition, categorize as carbonate wackestone. Term is
typically applied to diagenetically altered volcanic-lithic clastic
rocks in which the definition of the original clasts has been
obscured. Suggested boundaries between wacke and arenite range from 5
to 15 percent matrix. See Dickinson (1970) for discussion of
interpretation of undiscernible matrix in diagenetically altered
lithic clastic rocks. Dickinson, W.R., 1970, Interpreting detrital
modes of graywacke and arkose: Journal of Sedimentary Petrology, v.
40, p. 695-707.
- Clastic sandstone with more than 10 percent matrix of indeterminate
detrital or diagenetic nature. Matrix is mud size silicate minerals
(clay, feldspar, quartz, rock fragments, and alteration products).
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Wacke
- **Other Properties:**

[]{#hybrid_sedimentary_rock}

#####  hybrid sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Sedimentary rock that does not fit any of the other
composition/genesis categories. Sedimentary rock consisting of three
or more components which form more than 5 percent but less than 50
precent of the material.
- **Source:**
Hallsworth and Knox, 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hybrid_Sedimentary_Rock
- **Other Properties:**

[]{#iron_rich_sedimentary_rock}

#####  iron rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sedimentary rock that consists of at least 50 percent iron-bearing
minerals (hematite, magnetite, limonite-group, siderite, iron-
sulfides), as determined by hand-lens or petrographic analysis.
Corresponds to a rock typically containing 15 percent iron by weight.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#non_clastic_siliceous_sedimentary_rock}

#####  non clastic siliceous sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`non clastic siliceous sedimentary material`](#non_clastic_siliceous_sedimentary_material)
- Definition updated to include chert, flint SMR 2020-09-21
- Sedimentary rock that consists of at least 50 percent silicate
mineral material, deposited directly by chemical or biological
processes at the depositional surface, in particles formed by chemical
or biological processes within the basin of deposition, or formed by
diagenetic processes. Includes chert and flint found in carbonate
rocks.
- **Source:**
modified from SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Non_Clastic_Siliceous_Sedimentary_Rock
- **Other Properties:**

[]{#biogenic_silica_sedimentary_rock}

######  biogenic silica sedimentary rock
- **Child of**:
 [`non clastic siliceous sedimentary rock`](#non_clastic_siliceous_sedimentary_rock)
- Sedimentary rock that consists of at least 50 percent silicate
mineral material, deposited directly by biological processes at the
depositional surface, or in particles formed by biological processes
within the basin of deposition. Includes radiolarian chert, diatomite,
novaculite.
- **Source:**
based on NADM SLTT sedimentary; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Biogenic_Silica_Sedimentary_Rock
- **Other Properties:**

[]{#organic_rich_sedimentary_rock}

#####  organic rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`organic rich sedimentary material`](#organic_rich_sedimentary_material)
- Sapropelic coal, and asphaltite are not differentiated in This
vocabulary
- Sedimentary rock with color, composition, texture and apparent
density indicating greater than 50 percent organic content by weight
on a moisture-free basis.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Organic_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#coal}

######  coal
* `kohle`
- **Child of**:
 [`organic rich sedimentary rock`](#organic_rich_sedimentary_rock)
- A consolidated organic sedimentary material having less than 75%
moisture. This category includes low, medium, and high rank coals
according to International Classification of In-Seam Coal (United
Nations, 1998), thus including lignite. Sapropelic coal is not
distinguished in this category from humic coals. Formed from the
compaction or induration of variously altered plant remains similar to
those of peaty deposits.
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp.
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Coal
- **Other Properties:**

[]{#anthracite_coal}

#######  anthracite
* `anthrazit`
- **Child of**:
 [`coal`](#coal)
- Coal that has vitrinite mean random reflectance greater than 2.0%
(determined in conformance with ISO 7404-5). Less than 12-14 percent
volatiles (dry, ash free), greater than 91 percent fixed carbon (dry,
ash free basis). The highest rank coal; very hard, glossy, black, with
semimetallic luster, semi conchoidal fracture.
- **Alternate labels:**
High rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp; see also Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Coal#Types_of_coal; Eberhard Lindner; Chemie für Ingenieure; Lindner Verlag Karlsruhe, S. 258
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anthracite_Coal
- **Other Properties:**

[]{#bituminous_coal}

#######  bituminous coal
- **Child of**:
 [`coal`](#coal)
- Coal that has vitrinite mean random reflectance greater than 0.6%
and less than 2.0% (determined in conformance with ISO 7404-5), or has
a gross calorific value greater than 24 MJ/kg (determined in
conformance with ISO 1928). Hard, black, organic rich sedimentary
rock; contains less than 91 percent fixed carbon on a dry, mineral-
matter-free basis, and greater than 13-14 percent volatiles (dry, ash
free). Formed from the compaction or induration of variously altered
plant remains similar to those of peaty deposits.
- **Alternate labels:**
medium rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp; see also http://en.wikipedia.org/wiki/Coal#Types_of_coal; Eberhard Lindner; Chemie für Ingenieure; Lindner Verlag Karlsruhe, S. 258
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Bituminous_Coal
- **Other Properties:**

[]{#lignite}

#######  lignite
- **Child of**:
 [`coal`](#coal)
- Coal that has a gross calorific value less than 24 MJ/kg (determined
in conformance with ISO 1928), and vitrinite mean random reflectance
less than 0.6% (determined in conformance with ISO 7404-5). Gross
calorific value is recalculated to a moist, ash free basis using bed
moisture (determined according to ISO 1015 or ISO 5068). Includes all
low-rank coals, including sub-bitiminous coal. A consolidated, dull,
soft brown to black coal having many readily discernible plant
fragments set in a finer grained organic matrix. Tends to crack and
fall apart on drying. Operationally sub-bituminous and bitiminous coal
are qualitatively distinguished based on brown streak for sub-
bitiminous coal and black streak for bituminous coal.
- **Alternate labels:**
low rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Lignite
- **Other Properties:**

[]{#phosphorite}

#####  phosphorite
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`phosphate rich sedimentary material`](#phosphate_rich_sedimentary_material)
- Sedimentary rock in which at least 50 percent of the primary or
recrystallized constituents are phosphate minerals. Most commonly
occurs as a bedded primary or reworked secondary marine rock, composed
of microcrystalline carbonate fluorapatite in the form of lamina,
pellets, oolites and nodules, and skeletal, shell and bone fragments.
- **Source:**
HallsworthandKnox 1999, Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phosphorite
- **Other Properties:**

[]{#tuffite}

####  Tuffite
* `tuffit`
- **Child of**:
 [`Rock`](#rock)
- In practice, it is likely that any rock for which there is suspicion
that it may consist of redeposited pyroclastic material, usually based
on sedimentary structures, irrespective of the presence or percentage
of clearly epiclastic particles, would be called a tuffite. 50 percent
cutoff with epiclastic rock is in contrast with LeMaitre et al., but
is used for consistentency with other sedimentary rock categories
following the pattern that the rock name reflects the predominant
constituent.
- synonym: volcaniclastic rock
- Rock consists of more than 50 percent particles of indeterminate
pyroclastic or epiclastic origin and less than 75 percent particles of
clearly pyroclastic origin. commonly the rock is laminated or exhibits
size grading. (based on LeMaitre et al. 2002; Murawski and Meyer
1998).
- **Alternate labels:**
Volcaniclastic rock
- **Source:**
LeMaitre et al. 2002; Murawski and Meyer 1998
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tuffite
- **Other Properties:**

[]{#residual_material}

####  residual material
- **Child of**:
 [`Rock`](#rock)
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
- Material of composite origin resulting from weathering processes at
the Earth's surface, with genesis dominated by removal of chemical
constituents by aqueous leaching. Minor clastic, chemical, or organic
input may also contribute. Consolidation state is not inherent in
definition, but typically material is unconsolidated or weakly
consolidated.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/residual_material
- **Other Properties:**

[]{#composite_genesis_rock}

####  Composite genesis rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis material`](#composite_genesis_material)
- Rock formed by geological modification of pre-existing rocks outside
the realm of igneous and sedimentary processes. Includes rocks formed
by impact metamorphism, standard dynamothermal metamorphism, brittle
deformation, weathering, metasomatism and hydrothermal alteration
(diagenesis is a sedimentary process in this context).
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Composite_Genesis_Rock
- **Other Properties:**

[]{#cataclasite_series}

#####  cataclasite series
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`Composite genesis rock`](#composite_genesis_rock)
- Fault-related rock that maintained primary cohesion during
deformation, with matrix comprising greater than 10 percent of rock
mass; matrix is fine-grained material formed through grain size
reduction by fracture as opposed to crystal plastic process that
operate in mylonitic rock. Includes cataclasite, protocataclasite and
ultracataclasite.
- **Source:**
Sibson, 1977; Scholz, 1990; Snoke and Tullis, 1998; Barker, 1998 Appendix II; NADM SLTTm, 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Cataclasite_Series
- **Other Properties:**

[]{#metamorphic_rock}

#####  Metamorphic rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis rock`](#composite_genesis_rock)
- Robertson (1999, Classification of metamorphic rocks: British
Geological Survey Research Report, RR 99–02) defines the boundary
between diagenesis and metamorphism in sedimentary rocks as follows:
“…the boundary between diagenesis and metamorphism is somewhat
arbitrary and strongly dependent on the lithologies involved. For
example changes take place in organic materials at lower temperatures
than in rocks dominated by silicate minerals. In mudrocks, a white
mica (illite) crystallinity value of less than 0.42 Delta 2 Theta
obtained by X-ray diffraction analysis, is used to define the onset of
metamorphism (Kisch, 1991). In this scheme, the first appearance of
glaucophane, lawsonite, paragonite, prehnite, pumpellyite or
stilpnomelane is taken to indicate the lower limit of metamorphism
(Frey and Kisch, 1987; Bucher and Frey, 1994; Frey and Robinson,
1998). Most workers agree that such mineral growth starts at 150 +/-
50° C in silicate rocks. Many lithologies may show no change in
mineralogy under these conditions and hence the recognition of the
onset of metamorphism will vary with bulk composition.”
- Rock formed by solid-state mineralogical, chemical and/or structural
changes to a pre-existing rock, in response to marked changes in
temperature, pressure, shearing stress and chemical environment.
- **Source:**
Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Metamorphic_Rock
- **Other Properties:**

[]{#amphibolite}

######  amphibolite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock mainly consisting of green, brown or black
amphibole and plagioclase (including albite), which combined form 75
percent or more of the rock, and both of which are present as major
constituents. The amphibole constitutes 50 percent or more of the
total mafic constituents and is present in an amount of 30 percent or
more; other common minerals include quartz, clinopyroxene, garnet,
epidote-group minerals, biotite, titanite and scapolite.
- **Source:**
Coutinho et al. 2007, IUGS SCMR chapter 8 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Amphibolite
- **Other Properties:**

[]{#argillite}

######  Argillite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- A weakly metamorphosed argillaceous rock (Flawn, 1953, AAPG Bull v37
p.563-664).  Rock is very fine-grained to aphanitic, compact,
indurated, and massive (lacks fissility or cleavage) (Neuendorf et al,
2004). Claystone and Siltstone are related, non-metamorphosed
sedimentary rocks. Like Aphanite but sedimentary protolith is
determined. In contact metamorphic environments would be Hornfels.
- **Source:**
Neuendorf et al, 2004, provisional SMR 2020-06-11
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Argillite
- **Other Properties:**

[]{#calcsilicate_metamorphic_rock}

######  calc silicate metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Overlaps into metasomatic rocks because of high mobility of Ca
carbonates. Typically rich in epidote, diopside, tremolite, calcic-
amphibole, talc, with quartz and calcite. Might be gneiss or
granofels; lower metamorphic grade than granulite.
- metamorphic rock containing abundant calcium-silicate minerals
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcsilicate_Metamorphic_Rock
- **Other Properties:**

[]{#chlorite_actinolite_epidote_metamorphic_rock}

######  chlorite actinolite epidote metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock classified as Greenschist is difficult to categorize in the CGI
SimpleLithology scheme. This stems in part from the variation in usage
and the general fuzzy definition of the term. The definition of
greenschist is generally something along the lines of 'metamorphosed
rock with a greenish colour, characterized by the presence of
actinolite, chlorite and epidote, and containing a planar or linear
fabric. The presence or absence of schistose fabric in rocks called
'greenschist' is problematic. The fabric present in many rocks called
greenschist is too weak or variably developed to meet the definition
of 'schist' per CGI SimpleLithology. Generally if the rock has
achieved metamorphic grade such that the term 'gneiss' is applicable,
it would not be called greenschist. Thus, 'greenschist' would
correspond most closely to a chlorite + actinolite rich 'Foliated
metamorphic rock', but if it actually meets the definition of 'Schist'
it would be a chlorite + actinolite 'Schist'.
- Metamorphic rock characterized by 50 percent or more of combined
chlorite, actinolite and epidote. Category for rocks generally named
greenschist or greenstone.
- **Alternate labels:**
greenstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chlorite_Actinolite_Epidote_Metamorphic_Rock
- **Other Properties:**

[]{#eclogite}

######  eclogite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock composed of 75 percent or more (by volume)
omphacite and garnet, both of which are present as major constituents,
the amount of neither of them being higher than 75 percent (by
volume); the presence of plagioclase precludes classification as an
eclogite.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Eclogite
- **Other Properties:**

[]{#foliated_metamorphic_rock}

######  foliated metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock in which 10 percent or more of the contained
mineral grains are elements in a planar or linear fabric. Cataclastic
or glassy character precludes classification with this concept.
- **Source:**
based on NADM SLTT metamorphic
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foliated_Metamorphic_Rock
- **Other Properties:**

[]{#mylonitic_rock}

#######  mylonitic rock
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Metamorphic rock characterised by a foliation resulting from
tectonic grain size reduction, in which more than 10 percent of the
rock volume has undergone grain size reduction. Includes
protomylonite, mylonite, ultramylonite, and blastomylonite.
- **Source:**
Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mylonitic_Rock
- **Other Properties:**

[]{#phyllonite}

########  phyllonite
- **Child of**:
 [`mylonitic rock`](#mylonitic_rock)
- Mylonitic rock composed largely of fine-grained mica that imparts a
sheen to foliation surfaces; may have flaser lamination, isoclinal
folding, and deformed veins, which indicate significant shearing.
Macroscopically resembles phyllite, but formed by mechanical
degradation of initially coarser rock.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllonite
- **Other Properties:**

[]{#gneiss}

#######  gneiss
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Foliated metamorphic rock with bands or lenticles rich in granular
minerals alternating with bands or lenticles rich in minerals with a
flaky or elongate prismatic habit. Mylonitic foliation or well
developed, continuous schistosity (greater than 50 percent of the rock
consists of grains participate in a planar or linear fabric) precludes
classification with this concept.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gneiss
- **Other Properties:**

[]{#orthogneiss}

########  orthogneiss
- **Child of**:
 [`gneiss`](#gneiss)
- A gneiss with mineralogy and texture indicating derivation from a
phaneritic igneous rock protolith. Typically consists of abundant
feldspar, with quartz, and variable hornblende, biotite, and
muscovite, with a relatively homogeneous character.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Orthogneiss
- **Other Properties:**

[]{#paragneiss}

########  paragneiss
- **Child of**:
 [`gneiss`](#gneiss)
- A gneiss with mineralogy and texture indicating derivation from a
sedimentary rock protolith. Typically consists of abundant quartz,
mica, or calcsilicate minerals; aluminosilicate minerals or garnet
commonly present. composition of rock tends to be more variable on a
decimetric scale that in orthogneiss.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Paragneiss
- **Other Properties:**

[]{#phyllite}

#######  phyllite
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Rock with a well developed, continuous schistosity, an average grain
size between 0.1 and 0.5 millimeters, and a silvery sheen on cleavage
surfaces. Individual phyllosilicate grains are barely visible with the
unaided eye.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllite
- **Other Properties:**

[]{#schist}

#######  schist
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Foliated phaneritic metamorphic rock with well developed, continuous
schistosity, meaning that greater than 50 percent of the rock by
volume is mineral grains with a thin tabular, lamellar, or acicular
prismatic crystallographic habit that are oriented in a continuous
planar or linear fabric.
- **Source:**
SLTTm 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Schist
- **Other Properties:**

[]{#mica_schist}

########  mica schist
- **Child of**:
 [`schist`](#schist)
- Include single subcategory of schist to indicate this common kind of
schist. 'Mica rich metamorphic rock' for compound use with schist
fabric term would be more compatible with treatment of blueschist
(Glaucophane lawsonite epidote metamorphic rock) and greenschist
(Chlorite actinolite epidote metamorphic rock), but based on the
assumption that schist is the only rock type that will meet the mica-
rich criteria, it seems reasonable to include as a subtype of schist.
- A schist that consists of more than 50 percent mica minerals,
typically muscovite or biotite. Special type included to distinguish
this common variety of schist.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mica_Schist
- **Other Properties:**

[]{#slate}

#######  slate
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- compact, fine grained rock with an average grain size less than
0.032 millimeter and a well developed schistosity (slaty cleavage),
and hence can be split into slabs or thin plates.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Slate
- **Other Properties:**

[]{#glaucophane_lawsonite_epidote_metamorphic_rock}

######  glaucophane lawsonite epidote metamorphic rock
* `glaukophanschiefer`
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Fabric is weakly developed in this rock in many cases, so the fabric
categories 'foliated metamorphic rock, 'schist' or 'granofels' may
apply.
- A metamorphic rock of roughly basaltic composition, defined by the
presence of glaucophane with lawsonite or epidote. Other minerals that
may be present include jadeite, albite, chlorite, garnet, and
muscovite (phengitic white mica). Typically fine-grained, dark
colored. Category for rocks commonly referred to as blueschist.
- **Alternate labels:**
blauschiefer, 
blueschist, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Glaucophane_Lawsonite_Epidote_Metamorphic_Rock
- **Other Properties:**

[]{#granofels}

######  granofels
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock with granoblastic fabric and very little or no
foliation (less than 10 percent of the mineral grains in the rock are
elements in a planar or linear fabric). Grainsize not specified.
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Granofels
- **Other Properties:**

[]{#hornfels}

#######  hornfels
- **Child of**:
 [`granofels`](#granofels)
- Granofels formed by contact metamorphism, composed of a mosaic of
equidimensional grains in a characteristically granoblastic or
decussate matrix; porphyroblasts or relict phenocrysts may be present.
Typically fine grained.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hornfels
- **Other Properties:**

[]{#granulite}

######  granulite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Wimmenauer (1985) requires granulite to consist of at least 20
percent feldspar. Garnet is frequently present; some hornblende or
biotite may be present. The rock has a granoblastic texture and
gneissose to massive structure; grain size and fabric may be variable
on a decimetric scale. Foliation is less well developed than in rock
that would typically be called gneiss. The minerals present in a
granulite vary depending on the protolith and the temperature and
pressure conditions experienced during metamorphism. According to
Fettes and Desmons (2007) the main calc-silicate minerals are calcic
garnet, calcic plagioclase, calcic scapolite, diopside-hedenbergite,
epidote group minerals, hydrogrossular, johannsenite, prehnite,
pumpellyite, titanite, vesuvianite, wollastonite. Note that the shale
and siltstone categories may apply to any of the mineralogically
defined mudstone categories.
- Metamorphic rock of high metamorphic grade in which Fe-Mg silicate
minerals are dominantly hydroxl-free; feldspar must be present, and
muscovite is absent; rock contains less than 90 percent mafic
minerals, less than 75 percent calcite and/or dolomite, less than 75
percent quartz, less than 50 percent iron-bearing minerals (hematite,
magnetite, limonite-group, siderite, iron-sulfides), and less than 50
percent calc-silicate minerals.
- **Source:**
Fettes and Desmons (2007). See also Wimmenauer (1985), Winkler (1979) (D.R. Bowes (1989), The Encyclopedia of Igneous and Metamorphic Petrology; Van Nostrand Reinhold ISBN: 0-442-20623-2 ; wikipedia, http://en.wikipedia.org/wiki/Granulite accessed 5/30/09
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Granulite
- **Other Properties:**

[]{#marble}

######  marble
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock consisting of greater than 75 percent fine- to
coarse-grained recrystallized calcite and/or dolomite; usually with a
granoblastic, saccharoidal texture.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/), SLTTm1.0 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Marble
- **Other Properties:**

[]{#metaplutonic_rock}

######  metaplutonic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of a plutonic igneous protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metaplutonic_Rock
- **Other Properties:**

[]{#metasedimentary_rock}

######  metasedimentary rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of a sedimentary protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metasedimentary_Rock
- **Other Properties:**

[]{#metavolcanic_rock}

######  metavolcanic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of an extrusive igneous protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metavolcanic_Rock
- **Other Properties:**

[]{#migmatite}

######  migmatite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Silicate metamorphic rock that is pervasively heterogeneous on a
decimeter to meter scale that typically consists of darker and lighter
parts; the darker parts usually exhibit features of metamorphic rocks
whereas the lighter parts are of igneous-looking appearance.
- **Source:**
Fette and Desmons (2007) (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Migmatite
- **Other Properties:**

[]{#quartzite}

######  quartzite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock consisting of greater than or equal to 75 percent
quartz; typically granoblastic texture.
- **Source:**
after Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartzite
- **Other Properties:**

[]{#serpentinite}

######  serpentinite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock consisting of more than 75 percent serpentine-group minerals,
eg. antigorite, chrysotile or lizardite; accessory chlorite, talc and
magnetite may be present; derived from hydration of ferromagnesian
silicate minerals such as olivine and pyroxene.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Serpentinite
- **Other Properties:**

[]{#metasomatic_rock}

#####  metasomatic rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis rock`](#composite_genesis_rock)
- SLTTm (2004) proposed the following criteria to distinguish
hydrothermally altered or metasomatic rock from igneous rock. "The
rock is classified as metamorphic if (1) the texture has been modified
such that it can no longer be considered igneous, (2) the bulk
composition of the rock is inconsistent with compositions that can be
derived purely from a magma and associated processes such as
assimilation and differentiation, or (3) minerals inconsistent with
magmatic crystallization are present."
- Rock that has fabric and composition indicating open-system
mineralogical and chemical changes in response to interaction with a
fluid phase, typically water rich.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Metasomatic_Rock
- **Other Properties:**

[]{#altered_rock}

######  Altered, type not specified
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Rock material has been changed by some subsurface alteration
process, but the nature of the alteration is not specified.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Altered_Rock
- **Other Properties:**

[]{#advanced_argillic_altered_rock}

#######  advanced argillic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Advanced argillic alteration occurs under lower pH and higher
temperature conditions than argillic alteration. Kaolinite and dickite
occur at lower temperatures whereas pyrophyllite and andalusite occur
under high temperature conditions (T > 300°C). Quartz deposition is
common. Alunite, topaz, zunyite, tourmaline, enargite and tennantite
may also occur. In many cases, advanced argillic alteration zones, or
“lithocaps”, develop at shallow levels above porphyry Cu–Au deposits
(e.g., Lepanto-Far Southeast, Philippines; Maricunga, Chile). Advanced
argillic alteration mineral assemblages precipitate from SO2- and HCl-
rich magmatic vapor, which arises from an underlying intrusive source,
and can also form in supergene environments, due to post-hydrothermal
weathering and oxidation of pyrite, locally creating pH<1 liquid due
to high concentrations of H2SO4 within the vadose zone, where
kaolinite and alunite plus Fe hydroxides form.
- **Source:**
Antonio Arribas, Jeffrey Hedenquist, 2019, Environments of advanced argillic alteration: II) steam-heated, and exploration implications: Conference: Society of Resource Geology Annual SymposiumAt: University of Tokyo, Tokyo (Japan)Volume: 69, accessed at https://www.researchgate.net/publication/334230797_Environments_of_advanced_argillic_alteration_II_steam-heated_and_exploration_implications#fullTextFileContent; Constantinos Mavrogonatos et al., 2018, Mineralogical Study of the Advanced Argillic Alteration Zone at the Konos Hill Mo–Cu–Re–Au Porphyry Prospect, NE Greece: Minerals, 8, 479; doi:10.3390/min8110479;  https://en.wikipedia.org/wiki/Argillic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/advanced_argillic_altered_rock
- **Other Properties:**

[]{#albitic_altered_rock}

#######  albitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/albitic_altered_rock
- **Other Properties:**

[]{#alunitic_altered_rock}

#######  alunitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/alunitic_altered_rock
- **Other Properties:**

[]{#argillic_altered_rock}

#######  argillic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Argillic alteration is hydrothermal alteration of wall rock which
introduces clay minerals including kaolinite, smectite and illite. The
process generally occurs at low temperatures and may occur in
atmospheric conditions. Argillic alteration is representative of
supergene environments where low temperature groundwater becomes
acidic. Argillic assemblages include kaolinite replacing plagioclase
and montmorillonite replacing amphibole and plagioclase. Orthoclase is
generally stable and unaffected. Argillic grades into phyllic
alteration at higher temperatures in an ore deposit hydrothermal
system.
- **Source:**
https://en.wikipedia.org/wiki/Argillic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/argillic_altered_rock
- **Other Properties:**

[]{#calcsilicate_altered_rock}

#######  calcsilicate altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/calcsilicate_altered_rock
- **Other Properties:**

[]{#carbonate_altered_rock}

#######  carbonate altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/carbonate_altered_rock
- **Other Properties:**

[]{#chloritic_altered_rock}

#######  chloritic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/chloritic_altered_rock
- **Other Properties:**

[]{#deuteric_altered_rock}

#######  deuteric altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/deuteric_altered_rock
- **Other Properties:**

[]{#epidote_altered_rock}

#######  epidote altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/epidote_altered_rock
- **Other Properties:**

[]{#hematitic_altered_rock}

#######  hematitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Alteration characterized by finely dispersed hematite
- **Alternate labels:**
red rock altered rock
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24, 
Williams, P.J., 1994, Aust. J. Earth Science, v41, p381-382, 
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/hematitic_altered_rock
- **Other Properties:**

[]{#kaolinitic_altered_rock}

#######  kaolinitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/kaolinitic_altered_rock
- **Other Properties:**

[]{#phyllic_altered_rock}

#######  phyllic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Altered rock characterised by the assemblage of quartz + sericite +
pyrite, and occurs at high temperatures and moderately acidic (low pH)
conditions. Typically associated with copper porphyry ore deposits in
calc-alkaline rocks.
- **Source:**
https://en.wikipedia.org/wiki/Phyllic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/phyllic_altered_rock
- **Other Properties:**

[]{#potassic_altered_rock}

#######  potassic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/potassic_altered_rock
- **Other Properties:**

[]{#propylitic_altered_rock}

#######  propylitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/propylitic_altered_rock
- **Other Properties:**

[]{#pyritic_altered_rock}

#######  pyritic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/pyritic_altered_rock
- **Other Properties:**

[]{#saussuritised_rock}

#######  saussuritised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Rock in which calcium-bearing plagioclase feldspar is altered to an
assemblage of minerals called saussurite, typically including zoisite,
chlorite, amphibole, and carbonate minerals. Residual fluids present
during the late stages of magmatic crystallization can react with
previously formed plagioclase feldspar to form saussurite; the
saussurite will be spread through the plagioclase or located near its
outer margin. The plagioclase may be reconstituted into a more sodium-
rich variety (albite), although the original form of the crystal is
retained. Later hydrothermal alteration can produce the same result.
Mafic rocks are especially susceptible to saussuritization owing to
their high calcium content; the more calcium-rich portions of
plagioclase in acidic rocks also are often saussuritized.
- **Source:**
https://www.britannica.com/science/saussuritization
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/saussuritised_rock
- **Other Properties:**

[]{#sericitic_altered_rock}

#######  sericitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Rock in which plagioclase feldspar has been converted to sericite,
an informal term for  fine-grained white phyllosilicate minerals.
Commonly associated with phyllic altered rocks, used to describe less
intense alteration.
- **Source:**
https://en.wikipedia.org/wiki/Sericitic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/sericitic_altered_rock
- **Other Properties:**

[]{#serpentinised_rock}

#######  serpentinised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/serpentinised_rock
- **Other Properties:**

[]{#silicified_rock}

#######  silicificed rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/silicified_rock
- **Other Properties:**

[]{#uralitised_rock}

#######  uralitised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/uralitised_rock
- **Other Properties:**

[]{#zeolitic_altered_rock}

#######  zeolitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/zeolitic_altered_rock
- **Other Properties:**

[]{#greisen}

######  Greisen
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Greisen is a class of endoskarn,  formed by self-generated
alteration of a granite. Greisens appear as partly coarse, crystalline
granite, partly vuggy with miarolitic cavities, disseminated halide
minerals such as fluorite, and occasionally metallic oxide and sulfide
ore minerals, borate minerals (tourmaline) and accessory phases such
as sphene, beryl or topaz.
- **Source:**
https://en.wikipedia.org/wiki/Greisen
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Greisen
- **Other Properties:**

[]{#hydrothermal_massive_sulphide}

######  Hydrothermal Massive Sulphide
- **Child of**:
 [`Massive sulphide`](#massive_sulphide)
 [`metasomatic rock`](#metasomatic_rock)
- Rock consisting of greater that 50% sulphide or sulfosalt minerals
formed by hydrothermal mineralization processes.
- **Alternate labels:**
Hydrothermal Massive Sulfide
- **Source:**
provisional by SMR 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hydrothermal_Massive_Sulphide
- **Other Properties:**

[]{#skarn}

######  skarn
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Metasomatic rock consisting mainly of Ca-, Mg-, Fe-, or Mn-silicate
minerals, which are free from or poor in water. Typically formed at
the contact between a silicate rock or magma and a carbonate rock.
- **Alternate labels:**
exoskarn, 
tactite, 
- **Source:**
Fettes and Desmons, 2007, p195
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Skarn
- **Other Properties:**

[]{#spilite}

######  spilite
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Altered basic to intermediate composition fine-grained igneous rock
in which the feldspar is partially or completely composed of of
albite, typically accompanied by chlorite, calcite, quartz, epidote,
prehnite, and low-tempaerature hydrous crystallization products.
Preservation of eruptive volcanic features is typical.
- **Source:**
Fettes and Desmon, 2007; Best, M.G., 1982, Igneous and metamorphic petrology: New York, W.H. Freeman and company, p. 398; Neuendorf et al. 2005, p. 619.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Spilite
- **Other Properties:**

[]{#duricrust}

#####  Duricrust
- **Child of**:
 [`Composite genesis rock`](#composite_genesis_rock)
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
- Rock forming a hard crust or layer at or near the Earth's surface at
the time of formation, e.g. in the upper horizons of a soil,
characterized by structures indicative of pedogenic origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Duricrust
- **Other Properties:**

[]{#composite_genesis_material}

###  Composite genesis material
- **Child of**:
 [`Rock or sediment`](#rockorsediment)
- Material of unspecified consolidation state formed by geological
modification of pre-existing materials outside the realm of igneous
and sedimentary processes. Includes rocks formed by impact
metamorphism, standard dynamothermal metamorphism, brittle
deformation, weathering, metasomatism and hydrothermal alteration
(diagenesis is a sedimentary process in this context).
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Composite_Genesis_Material
- **Other Properties:**

[]{#fault_related_material}

####  Fault related material
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis material`](#composite_genesis_material)
- Material formed as a result brittle faulting, composed of greater
than 10 percent matrix; matrix is fine-grained material caused by
tectonic grainsize reduction. Includes cohesive (cataclasite series,
mylonitic rocks) and non-cohesive (breccia-gouge series) material.
- **Source:**
This vocabulary; SLTTm 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fault_Related_Material
- **Other Properties:**

[]{#cataclasite_series}

#####  cataclasite series
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`Composite genesis rock`](#composite_genesis_rock)
- Fault-related rock that maintained primary cohesion during
deformation, with matrix comprising greater than 10 percent of rock
mass; matrix is fine-grained material formed through grain size
reduction by fracture as opposed to crystal plastic process that
operate in mylonitic rock. Includes cataclasite, protocataclasite and
ultracataclasite.
- **Source:**
Sibson, 1977; Scholz, 1990; Snoke and Tullis, 1998; Barker, 1998 Appendix II; NADM SLTTm, 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Cataclasite_Series
- **Other Properties:**

[]{#mylonitic_rock}

#####  mylonitic rock
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Metamorphic rock characterised by a foliation resulting from
tectonic grain size reduction, in which more than 10 percent of the
rock volume has undergone grain size reduction. Includes
protomylonite, mylonite, ultramylonite, and blastomylonite.
- **Source:**
Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mylonitic_Rock
- **Other Properties:**

[]{#phyllonite}

######  phyllonite
- **Child of**:
 [`mylonitic rock`](#mylonitic_rock)
- Mylonitic rock composed largely of fine-grained mica that imparts a
sheen to foliation surfaces; may have flaser lamination, isoclinal
folding, and deformed veins, which indicate significant shearing.
Macroscopically resembles phyllite, but formed by mechanical
degradation of initially coarser rock.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllonite
- **Other Properties:**

[]{#breccia_gouge_series}

#####  breccia gouge series
- **Child of**:
 [`Fault related material`](#fault_related_material)
- Fault-related material with features such as void spaces (filled or
unfilled), or unconsolidated matrix material between fragments,
indicating loss of cohesion during deformation. Includes fault-related
breccia and gouge.
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/breccia_gouge_series
- **Other Properties:**

[]{#impact_generated_material}

####  Impact generated material
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis material`](#composite_genesis_material)
- Material that contains features indicative of shock metamorphism,
such as microscopic planar deformation features within grains or
shatter cones, interpreted to be the result of extraterrestrial bolide
impact. Includes breccias and melt rocks.
- **Source:**
Stöffler and Grieve 2007; Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Impact_Generated_Material
- **Other Properties:**

[]{#composite_genesis_rock}

####  Composite genesis rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis material`](#composite_genesis_material)
- Rock formed by geological modification of pre-existing rocks outside
the realm of igneous and sedimentary processes. Includes rocks formed
by impact metamorphism, standard dynamothermal metamorphism, brittle
deformation, weathering, metasomatism and hydrothermal alteration
(diagenesis is a sedimentary process in this context).
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Composite_Genesis_Rock
- **Other Properties:**

[]{#cataclasite_series}

#####  cataclasite series
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`Composite genesis rock`](#composite_genesis_rock)
- Fault-related rock that maintained primary cohesion during
deformation, with matrix comprising greater than 10 percent of rock
mass; matrix is fine-grained material formed through grain size
reduction by fracture as opposed to crystal plastic process that
operate in mylonitic rock. Includes cataclasite, protocataclasite and
ultracataclasite.
- **Source:**
Sibson, 1977; Scholz, 1990; Snoke and Tullis, 1998; Barker, 1998 Appendix II; NADM SLTTm, 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Cataclasite_Series
- **Other Properties:**

[]{#metamorphic_rock}

#####  Metamorphic rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis rock`](#composite_genesis_rock)
- Robertson (1999, Classification of metamorphic rocks: British
Geological Survey Research Report, RR 99–02) defines the boundary
between diagenesis and metamorphism in sedimentary rocks as follows:
“…the boundary between diagenesis and metamorphism is somewhat
arbitrary and strongly dependent on the lithologies involved. For
example changes take place in organic materials at lower temperatures
than in rocks dominated by silicate minerals. In mudrocks, a white
mica (illite) crystallinity value of less than 0.42 Delta 2 Theta
obtained by X-ray diffraction analysis, is used to define the onset of
metamorphism (Kisch, 1991). In this scheme, the first appearance of
glaucophane, lawsonite, paragonite, prehnite, pumpellyite or
stilpnomelane is taken to indicate the lower limit of metamorphism
(Frey and Kisch, 1987; Bucher and Frey, 1994; Frey and Robinson,
1998). Most workers agree that such mineral growth starts at 150 +/-
50° C in silicate rocks. Many lithologies may show no change in
mineralogy under these conditions and hence the recognition of the
onset of metamorphism will vary with bulk composition.”
- Rock formed by solid-state mineralogical, chemical and/or structural
changes to a pre-existing rock, in response to marked changes in
temperature, pressure, shearing stress and chemical environment.
- **Source:**
Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Metamorphic_Rock
- **Other Properties:**

[]{#amphibolite}

######  amphibolite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock mainly consisting of green, brown or black
amphibole and plagioclase (including albite), which combined form 75
percent or more of the rock, and both of which are present as major
constituents. The amphibole constitutes 50 percent or more of the
total mafic constituents and is present in an amount of 30 percent or
more; other common minerals include quartz, clinopyroxene, garnet,
epidote-group minerals, biotite, titanite and scapolite.
- **Source:**
Coutinho et al. 2007, IUGS SCMR chapter 8 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Amphibolite
- **Other Properties:**

[]{#argillite}

######  Argillite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- A weakly metamorphosed argillaceous rock (Flawn, 1953, AAPG Bull v37
p.563-664).  Rock is very fine-grained to aphanitic, compact,
indurated, and massive (lacks fissility or cleavage) (Neuendorf et al,
2004). Claystone and Siltstone are related, non-metamorphosed
sedimentary rocks. Like Aphanite but sedimentary protolith is
determined. In contact metamorphic environments would be Hornfels.
- **Source:**
Neuendorf et al, 2004, provisional SMR 2020-06-11
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Argillite
- **Other Properties:**

[]{#calcsilicate_metamorphic_rock}

######  calc silicate metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Overlaps into metasomatic rocks because of high mobility of Ca
carbonates. Typically rich in epidote, diopside, tremolite, calcic-
amphibole, talc, with quartz and calcite. Might be gneiss or
granofels; lower metamorphic grade than granulite.
- metamorphic rock containing abundant calcium-silicate minerals
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcsilicate_Metamorphic_Rock
- **Other Properties:**

[]{#chlorite_actinolite_epidote_metamorphic_rock}

######  chlorite actinolite epidote metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock classified as Greenschist is difficult to categorize in the CGI
SimpleLithology scheme. This stems in part from the variation in usage
and the general fuzzy definition of the term. The definition of
greenschist is generally something along the lines of 'metamorphosed
rock with a greenish colour, characterized by the presence of
actinolite, chlorite and epidote, and containing a planar or linear
fabric. The presence or absence of schistose fabric in rocks called
'greenschist' is problematic. The fabric present in many rocks called
greenschist is too weak or variably developed to meet the definition
of 'schist' per CGI SimpleLithology. Generally if the rock has
achieved metamorphic grade such that the term 'gneiss' is applicable,
it would not be called greenschist. Thus, 'greenschist' would
correspond most closely to a chlorite + actinolite rich 'Foliated
metamorphic rock', but if it actually meets the definition of 'Schist'
it would be a chlorite + actinolite 'Schist'.
- Metamorphic rock characterized by 50 percent or more of combined
chlorite, actinolite and epidote. Category for rocks generally named
greenschist or greenstone.
- **Alternate labels:**
greenstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chlorite_Actinolite_Epidote_Metamorphic_Rock
- **Other Properties:**

[]{#eclogite}

######  eclogite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock composed of 75 percent or more (by volume)
omphacite and garnet, both of which are present as major constituents,
the amount of neither of them being higher than 75 percent (by
volume); the presence of plagioclase precludes classification as an
eclogite.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Eclogite
- **Other Properties:**

[]{#foliated_metamorphic_rock}

######  foliated metamorphic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock in which 10 percent or more of the contained
mineral grains are elements in a planar or linear fabric. Cataclastic
or glassy character precludes classification with this concept.
- **Source:**
based on NADM SLTT metamorphic
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foliated_Metamorphic_Rock
- **Other Properties:**

[]{#mylonitic_rock}

#######  mylonitic rock
- **Child of**:
 [`Fault related material`](#fault_related_material)
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Metamorphic rock characterised by a foliation resulting from
tectonic grain size reduction, in which more than 10 percent of the
rock volume has undergone grain size reduction. Includes
protomylonite, mylonite, ultramylonite, and blastomylonite.
- **Source:**
Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mylonitic_Rock
- **Other Properties:**

[]{#phyllonite}

########  phyllonite
- **Child of**:
 [`mylonitic rock`](#mylonitic_rock)
- Mylonitic rock composed largely of fine-grained mica that imparts a
sheen to foliation surfaces; may have flaser lamination, isoclinal
folding, and deformed veins, which indicate significant shearing.
Macroscopically resembles phyllite, but formed by mechanical
degradation of initially coarser rock.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Marshak and Mitra 1988
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllonite
- **Other Properties:**

[]{#gneiss}

#######  gneiss
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Foliated metamorphic rock with bands or lenticles rich in granular
minerals alternating with bands or lenticles rich in minerals with a
flaky or elongate prismatic habit. Mylonitic foliation or well
developed, continuous schistosity (greater than 50 percent of the rock
consists of grains participate in a planar or linear fabric) precludes
classification with this concept.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gneiss
- **Other Properties:**

[]{#orthogneiss}

########  orthogneiss
- **Child of**:
 [`gneiss`](#gneiss)
- A gneiss with mineralogy and texture indicating derivation from a
phaneritic igneous rock protolith. Typically consists of abundant
feldspar, with quartz, and variable hornblende, biotite, and
muscovite, with a relatively homogeneous character.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Orthogneiss
- **Other Properties:**

[]{#paragneiss}

########  paragneiss
- **Child of**:
 [`gneiss`](#gneiss)
- A gneiss with mineralogy and texture indicating derivation from a
sedimentary rock protolith. Typically consists of abundant quartz,
mica, or calcsilicate minerals; aluminosilicate minerals or garnet
commonly present. composition of rock tends to be more variable on a
decimetric scale that in orthogneiss.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Paragneiss
- **Other Properties:**

[]{#phyllite}

#######  phyllite
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Rock with a well developed, continuous schistosity, an average grain
size between 0.1 and 0.5 millimeters, and a silvery sheen on cleavage
surfaces. Individual phyllosilicate grains are barely visible with the
unaided eye.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phyllite
- **Other Properties:**

[]{#schist}

#######  schist
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- Foliated phaneritic metamorphic rock with well developed, continuous
schistosity, meaning that greater than 50 percent of the rock by
volume is mineral grains with a thin tabular, lamellar, or acicular
prismatic crystallographic habit that are oriented in a continuous
planar or linear fabric.
- **Source:**
SLTTm 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Schist
- **Other Properties:**

[]{#mica_schist}

########  mica schist
- **Child of**:
 [`schist`](#schist)
- Include single subcategory of schist to indicate this common kind of
schist. 'Mica rich metamorphic rock' for compound use with schist
fabric term would be more compatible with treatment of blueschist
(Glaucophane lawsonite epidote metamorphic rock) and greenschist
(Chlorite actinolite epidote metamorphic rock), but based on the
assumption that schist is the only rock type that will meet the mica-
rich criteria, it seems reasonable to include as a subtype of schist.
- A schist that consists of more than 50 percent mica minerals,
typically muscovite or biotite. Special type included to distinguish
this common variety of schist.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mica_Schist
- **Other Properties:**

[]{#slate}

#######  slate
- **Child of**:
 [`foliated metamorphic rock`](#foliated_metamorphic_rock)
- compact, fine grained rock with an average grain size less than
0.032 millimeter and a well developed schistosity (slaty cleavage),
and hence can be split into slabs or thin plates.
- **Source:**
NADM metamorphic rock vocabulary SLTTm1.0; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Slate
- **Other Properties:**

[]{#glaucophane_lawsonite_epidote_metamorphic_rock}

######  glaucophane lawsonite epidote metamorphic rock
* `glaukophanschiefer`
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Fabric is weakly developed in this rock in many cases, so the fabric
categories 'foliated metamorphic rock, 'schist' or 'granofels' may
apply.
- A metamorphic rock of roughly basaltic composition, defined by the
presence of glaucophane with lawsonite or epidote. Other minerals that
may be present include jadeite, albite, chlorite, garnet, and
muscovite (phengitic white mica). Typically fine-grained, dark
colored. Category for rocks commonly referred to as blueschist.
- **Alternate labels:**
blauschiefer, 
blueschist, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Glaucophane_Lawsonite_Epidote_Metamorphic_Rock
- **Other Properties:**

[]{#granofels}

######  granofels
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock with granoblastic fabric and very little or no
foliation (less than 10 percent of the mineral grains in the rock are
elements in a planar or linear fabric). Grainsize not specified.
- **Source:**
SLTTm 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Granofels
- **Other Properties:**

[]{#hornfels}

#######  hornfels
- **Child of**:
 [`granofels`](#granofels)
- Granofels formed by contact metamorphism, composed of a mosaic of
equidimensional grains in a characteristically granoblastic or
decussate matrix; porphyroblasts or relict phenocrysts may be present.
Typically fine grained.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hornfels
- **Other Properties:**

[]{#granulite}

######  granulite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Wimmenauer (1985) requires granulite to consist of at least 20
percent feldspar. Garnet is frequently present; some hornblende or
biotite may be present. The rock has a granoblastic texture and
gneissose to massive structure; grain size and fabric may be variable
on a decimetric scale. Foliation is less well developed than in rock
that would typically be called gneiss. The minerals present in a
granulite vary depending on the protolith and the temperature and
pressure conditions experienced during metamorphism. According to
Fettes and Desmons (2007) the main calc-silicate minerals are calcic
garnet, calcic plagioclase, calcic scapolite, diopside-hedenbergite,
epidote group minerals, hydrogrossular, johannsenite, prehnite,
pumpellyite, titanite, vesuvianite, wollastonite. Note that the shale
and siltstone categories may apply to any of the mineralogically
defined mudstone categories.
- Metamorphic rock of high metamorphic grade in which Fe-Mg silicate
minerals are dominantly hydroxl-free; feldspar must be present, and
muscovite is absent; rock contains less than 90 percent mafic
minerals, less than 75 percent calcite and/or dolomite, less than 75
percent quartz, less than 50 percent iron-bearing minerals (hematite,
magnetite, limonite-group, siderite, iron-sulfides), and less than 50
percent calc-silicate minerals.
- **Source:**
Fettes and Desmons (2007). See also Wimmenauer (1985), Winkler (1979) (D.R. Bowes (1989), The Encyclopedia of Igneous and Metamorphic Petrology; Van Nostrand Reinhold ISBN: 0-442-20623-2 ; wikipedia, http://en.wikipedia.org/wiki/Granulite accessed 5/30/09
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Granulite
- **Other Properties:**

[]{#marble}

######  marble
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock consisting of greater than 75 percent fine- to
coarse-grained recrystallized calcite and/or dolomite; usually with a
granoblastic, saccharoidal texture.
- **Source:**
IUGS SCMR 2007 (http://www.bgs.ac.uk/SCMR/), SLTTm1.0 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Marble
- **Other Properties:**

[]{#metaplutonic_rock}

######  metaplutonic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of a plutonic igneous protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metaplutonic_Rock
- **Other Properties:**

[]{#metasedimentary_rock}

######  metasedimentary rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of a sedimentary protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metasedimentary_Rock
- **Other Properties:**

[]{#metavolcanic_rock}

######  metavolcanic rock
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock formed by metamorphism of an extrusive igneous protolith.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Metavolcanic_Rock
- **Other Properties:**

[]{#migmatite}

######  migmatite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Silicate metamorphic rock that is pervasively heterogeneous on a
decimeter to meter scale that typically consists of darker and lighter
parts; the darker parts usually exhibit features of metamorphic rocks
whereas the lighter parts are of igneous-looking appearance.
- **Source:**
Fette and Desmons (2007) (http://www.bgs.ac.uk/SCMR/)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Migmatite
- **Other Properties:**

[]{#quartzite}

######  quartzite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Metamorphic rock consisting of greater than or equal to 75 percent
quartz; typically granoblastic texture.
- **Source:**
after Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartzite
- **Other Properties:**

[]{#serpentinite}

######  serpentinite
- **Child of**:
 [`Metamorphic rock`](#metamorphic_rock)
- Rock consisting of more than 75 percent serpentine-group minerals,
eg. antigorite, chrysotile or lizardite; accessory chlorite, talc and
magnetite may be present; derived from hydration of ferromagnesian
silicate minerals such as olivine and pyroxene.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Serpentinite
- **Other Properties:**

[]{#metasomatic_rock}

#####  metasomatic rock
- **Child of**:
 [`Rock`](#rock)
 [`Composite genesis rock`](#composite_genesis_rock)
- SLTTm (2004) proposed the following criteria to distinguish
hydrothermally altered or metasomatic rock from igneous rock. "The
rock is classified as metamorphic if (1) the texture has been modified
such that it can no longer be considered igneous, (2) the bulk
composition of the rock is inconsistent with compositions that can be
derived purely from a magma and associated processes such as
assimilation and differentiation, or (3) minerals inconsistent with
magmatic crystallization are present."
- Rock that has fabric and composition indicating open-system
mineralogical and chemical changes in response to interaction with a
fluid phase, typically water rich.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Metasomatic_Rock
- **Other Properties:**

[]{#altered_rock}

######  Altered, type not specified
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Rock material has been changed by some subsurface alteration
process, but the nature of the alteration is not specified.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Altered_Rock
- **Other Properties:**

[]{#advanced_argillic_altered_rock}

#######  advanced argillic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Advanced argillic alteration occurs under lower pH and higher
temperature conditions than argillic alteration. Kaolinite and dickite
occur at lower temperatures whereas pyrophyllite and andalusite occur
under high temperature conditions (T > 300°C). Quartz deposition is
common. Alunite, topaz, zunyite, tourmaline, enargite and tennantite
may also occur. In many cases, advanced argillic alteration zones, or
“lithocaps”, develop at shallow levels above porphyry Cu–Au deposits
(e.g., Lepanto-Far Southeast, Philippines; Maricunga, Chile). Advanced
argillic alteration mineral assemblages precipitate from SO2- and HCl-
rich magmatic vapor, which arises from an underlying intrusive source,
and can also form in supergene environments, due to post-hydrothermal
weathering and oxidation of pyrite, locally creating pH<1 liquid due
to high concentrations of H2SO4 within the vadose zone, where
kaolinite and alunite plus Fe hydroxides form.
- **Source:**
Antonio Arribas, Jeffrey Hedenquist, 2019, Environments of advanced argillic alteration: II) steam-heated, and exploration implications: Conference: Society of Resource Geology Annual SymposiumAt: University of Tokyo, Tokyo (Japan)Volume: 69, accessed at https://www.researchgate.net/publication/334230797_Environments_of_advanced_argillic_alteration_II_steam-heated_and_exploration_implications#fullTextFileContent; Constantinos Mavrogonatos et al., 2018, Mineralogical Study of the Advanced Argillic Alteration Zone at the Konos Hill Mo–Cu–Re–Au Porphyry Prospect, NE Greece: Minerals, 8, 479; doi:10.3390/min8110479;  https://en.wikipedia.org/wiki/Argillic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/advanced_argillic_altered_rock
- **Other Properties:**

[]{#albitic_altered_rock}

#######  albitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/albitic_altered_rock
- **Other Properties:**

[]{#alunitic_altered_rock}

#######  alunitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/alunitic_altered_rock
- **Other Properties:**

[]{#argillic_altered_rock}

#######  argillic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Argillic alteration is hydrothermal alteration of wall rock which
introduces clay minerals including kaolinite, smectite and illite. The
process generally occurs at low temperatures and may occur in
atmospheric conditions. Argillic alteration is representative of
supergene environments where low temperature groundwater becomes
acidic. Argillic assemblages include kaolinite replacing plagioclase
and montmorillonite replacing amphibole and plagioclase. Orthoclase is
generally stable and unaffected. Argillic grades into phyllic
alteration at higher temperatures in an ore deposit hydrothermal
system.
- **Source:**
https://en.wikipedia.org/wiki/Argillic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/argillic_altered_rock
- **Other Properties:**

[]{#calcsilicate_altered_rock}

#######  calcsilicate altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/calcsilicate_altered_rock
- **Other Properties:**

[]{#carbonate_altered_rock}

#######  carbonate altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/carbonate_altered_rock
- **Other Properties:**

[]{#chloritic_altered_rock}

#######  chloritic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/chloritic_altered_rock
- **Other Properties:**

[]{#deuteric_altered_rock}

#######  deuteric altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/deuteric_altered_rock
- **Other Properties:**

[]{#epidote_altered_rock}

#######  epidote altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/epidote_altered_rock
- **Other Properties:**

[]{#hematitic_altered_rock}

#######  hematitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Alteration characterized by finely dispersed hematite
- **Alternate labels:**
red rock altered rock
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24, 
Williams, P.J., 1994, Aust. J. Earth Science, v41, p381-382, 
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/hematitic_altered_rock
- **Other Properties:**

[]{#kaolinitic_altered_rock}

#######  kaolinitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/kaolinitic_altered_rock
- **Other Properties:**

[]{#phyllic_altered_rock}

#######  phyllic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Altered rock characterised by the assemblage of quartz + sericite +
pyrite, and occurs at high temperatures and moderately acidic (low pH)
conditions. Typically associated with copper porphyry ore deposits in
calc-alkaline rocks.
- **Source:**
https://en.wikipedia.org/wiki/Phyllic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/phyllic_altered_rock
- **Other Properties:**

[]{#potassic_altered_rock}

#######  potassic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/potassic_altered_rock
- **Other Properties:**

[]{#propylitic_altered_rock}

#######  propylitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/propylitic_altered_rock
- **Other Properties:**

[]{#pyritic_altered_rock}

#######  pyritic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/pyritic_altered_rock
- **Other Properties:**

[]{#saussuritised_rock}

#######  saussuritised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Rock in which calcium-bearing plagioclase feldspar is altered to an
assemblage of minerals called saussurite, typically including zoisite,
chlorite, amphibole, and carbonate minerals. Residual fluids present
during the late stages of magmatic crystallization can react with
previously formed plagioclase feldspar to form saussurite; the
saussurite will be spread through the plagioclase or located near its
outer margin. The plagioclase may be reconstituted into a more sodium-
rich variety (albite), although the original form of the crystal is
retained. Later hydrothermal alteration can produce the same result.
Mafic rocks are especially susceptible to saussuritization owing to
their high calcium content; the more calcium-rich portions of
plagioclase in acidic rocks also are often saussuritized.
- **Source:**
https://www.britannica.com/science/saussuritization
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/saussuritised_rock
- **Other Properties:**

[]{#sericitic_altered_rock}

#######  sericitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- Rock in which plagioclase feldspar has been converted to sericite,
an informal term for  fine-grained white phyllosilicate minerals.
Commonly associated with phyllic altered rocks, used to describe less
intense alteration.
- **Source:**
https://en.wikipedia.org/wiki/Sericitic_alteration
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/sericitic_altered_rock
- **Other Properties:**

[]{#serpentinised_rock}

#######  serpentinised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/serpentinised_rock
- **Other Properties:**

[]{#silicified_rock}

#######  silicificed rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/silicified_rock
- **Other Properties:**

[]{#uralitised_rock}

#######  uralitised rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/uralitised_rock
- **Other Properties:**

[]{#zeolitic_altered_rock}

#######  zeolitic altered rock
- **Child of**:
 [`Altered, type not specified`](#altered_rock)
- definition missing
- **Source:**
CGI alterationtype SKOS vocabulary 2012-11-24
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/zeolitic_altered_rock
- **Other Properties:**

[]{#greisen}

######  Greisen
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Greisen is a class of endoskarn,  formed by self-generated
alteration of a granite. Greisens appear as partly coarse, crystalline
granite, partly vuggy with miarolitic cavities, disseminated halide
minerals such as fluorite, and occasionally metallic oxide and sulfide
ore minerals, borate minerals (tourmaline) and accessory phases such
as sphene, beryl or topaz.
- **Source:**
https://en.wikipedia.org/wiki/Greisen
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Greisen
- **Other Properties:**

[]{#hydrothermal_massive_sulphide}

######  Hydrothermal Massive Sulphide
- **Child of**:
 [`Massive sulphide`](#massive_sulphide)
 [`metasomatic rock`](#metasomatic_rock)
- Rock consisting of greater that 50% sulphide or sulfosalt minerals
formed by hydrothermal mineralization processes.
- **Alternate labels:**
Hydrothermal Massive Sulfide
- **Source:**
provisional by SMR 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Hydrothermal_Massive_Sulphide
- **Other Properties:**

[]{#skarn}

######  skarn
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Metasomatic rock consisting mainly of Ca-, Mg-, Fe-, or Mn-silicate
minerals, which are free from or poor in water. Typically formed at
the contact between a silicate rock or magma and a carbonate rock.
- **Alternate labels:**
exoskarn, 
tactite, 
- **Source:**
Fettes and Desmons, 2007, p195
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Skarn
- **Other Properties:**

[]{#spilite}

######  spilite
- **Child of**:
 [`metasomatic rock`](#metasomatic_rock)
- Altered basic to intermediate composition fine-grained igneous rock
in which the feldspar is partially or completely composed of of
albite, typically accompanied by chlorite, calcite, quartz, epidote,
prehnite, and low-tempaerature hydrous crystallization products.
Preservation of eruptive volcanic features is typical.
- **Source:**
Fettes and Desmon, 2007; Best, M.G., 1982, Igneous and metamorphic petrology: New York, W.H. Freeman and company, p. 398; Neuendorf et al. 2005, p. 619.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Spilite
- **Other Properties:**

[]{#duricrust}

#####  Duricrust
- **Child of**:
 [`Composite genesis rock`](#composite_genesis_rock)
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
- Rock forming a hard crust or layer at or near the Earth's surface at
the time of formation, e.g. in the upper horizons of a soil,
characterized by structures indicative of pedogenic origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Duricrust
- **Other Properties:**

[]{#material_formed_in_surficial_environment}

####  material formed in surficial environment
- **Child of**:
 [`Composite genesis material`](#composite_genesis_material)
- Material that is the product of weathering processes operating on
pre-existing rocks or deposits, analogous to hydrothermal or
metasomatic rocks, but formed at ambient Earth surface temperature and
pressure.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Material_Formed_In_Surficial_Environment
- **Other Properties:**

[]{#residual_material}

#####  residual material
- **Child of**:
 [`Rock`](#rock)
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
- Material of composite origin resulting from weathering processes at
the Earth's surface, with genesis dominated by removal of chemical
constituents by aqueous leaching. Minor clastic, chemical, or organic
input may also contribute. Consolidation state is not inherent in
definition, but typically material is unconsolidated or weakly
consolidated.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/residual_material
- **Other Properties:**

[]{#soil}

#####  Soil
- **Child of**:
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
 [`Natural unconsolidated material`](#natural_unconsolidated_material)
- Mixed granular mineral and organic matter modified by interaction
between earth material, biosphere, and atmosphere, consisting of
varying proportions of sand, silt, and clay, organic material such as
humus, gases, liquids, and a broad range of resident micro- and
macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of
horizons near the Earth's surface that, in contrast to the underlying
parent material, have been altered by the interactions of climate,
relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/
portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
(http://purl.obolibrary.org/obo/ENVO_00001998)
- **See Also**:
* [<http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280>](http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
- **Concept URI:** https://w3id.org/isample/vocabulary/material/1.0/soil
- **Other Properties:**

[]{#bauxite}

#####  bauxite
- **Child of**:
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
- Highly aluminous material containing abundant aluminium hydroxides
(gibbsite, less commonly boehmite, diaspore) and aluminium-substituted
iron oxides or hydroxides and generally minor or negligible kaolin
minerals; may contain up to 20 percent quartz. commonly has a
pisolitic or nodular texture, and may be cemented.
- **Source:**
Eggleton 2001
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Bauxite
- **Other Properties:**

[]{#duricrust}

#####  Duricrust
- **Child of**:
 [`Composite genesis rock`](#composite_genesis_rock)
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
- Rock forming a hard crust or layer at or near the Earth's surface at
the time of formation, e.g. in the upper horizons of a soil,
characterized by structures indicative of pedogenic origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Duricrust
- **Other Properties:**

[]{#igneous_material}

###  Igneous material
- **Child of**:
 [`Rock or sediment`](#rockorsediment)
- Earth material formed as a result of igneous processes, eg.
intrusion and cooling of magma in the crust, volcanic eruption.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Igneous_Material
- **Other Properties:**

[]{#igneous_rock}

####  Igneous rock
- **Child of**:
 [`Rock`](#rock)
 [`Igneous material`](#igneous_material)
- rock formed as a result of igneous processes, for example intrusion
and cooling of magma in the crust, or volcanic eruption.
- **Source:**
Neuendorf et al 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Igneous_Rock
- **Other Properties:**

[]{#acidic_igneous_rock}

#####  acidic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`acidic igneous material`](#acidic_igneous_material)
- Igneous rock with more than 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Acidic_Igneous_Rock
- **Other Properties:**

[]{#dacite}

######  dacite
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dacite
- **Other Properties:**

[]{#granitoid}

######  granitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.
- **Alternate labels:**
granitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granitoid
- **Other Properties:**

[]{#alkali_feldspar_granite}

#######  alkali feldspar granite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitic rock that has a plagioclase to total feldspar ratio less
than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Alkali_Feldspar_Granite
- **Other Properties:**

[]{#granite}

#######  granite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting of quartz, alkali feldspar
and plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granite
- **Other Properties:**

[]{#monzogranite}

########  monzogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.35
and 0.65. QAPF field 3b.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogranite
- **Other Properties:**

[]{#syenogranite}

########  syenogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.10
and 0.35. QAPF field 3a.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenogranite
- **Other Properties:**

[]{#granodiorite}

#######  granodiorite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granodiorite
- **Other Properties:**

[]{#tonalite}

#######  tonalite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tonalite
- **Other Properties:**

[]{#quartz_rich_igneous_rock}

######  quartz rich igneous rock
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals and contains greater than 60 percent quartz in
the QAPF fraction.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Quartz_Rich_Igneous_Rock
- **Other Properties:**

[]{#rhyolitoid}

######  rhyolitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Note that technical definition, based on modal mineralogy plotted in
a QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
- fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.
- **Alternate labels:**
rhyolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Rhyolitoid
- **Other Properties:**

[]{#alkali_feldspar_rhyolite}

#######  alkali feldspar rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- Rhyolitoid in which the ratio of plagioclase to total feldspar is
less than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Rhyolite
- **Other Properties:**

[]{#rhyolite}

#######  rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- rhyolitoid in which the ratio of plagioclase to total feldspar is
between 0.1 and 0.65.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rhyolite
- **Other Properties:**

[]{#basic_igneous_rock}

#####  basic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`basic igneous material`](#basic_igneous_material)
- Igneous rock with between 45 and 52 percent SiO2.
- **Source:**
Neuendorf et al 2005; LeMaitre et al. 2002; Gillespie and Styles 1999, 
after LeMaitre et al. 2002, 
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basic_Igneous_Rock
- **Other Properties:**

[]{#basalt}

######  basalt
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basalt
- **Other Properties:**

[]{#alkali-olivine_basalt}

#######  alkali olivine basalt
- **Child of**:
 [`basalt`](#basalt)
- The definition of tholeiite and alkali basalt here are more
prescriptive than those found in most reference authorities. This is
to actually provide some descriptive criteria to allow assignment of
rocks on a hand sample basis to the tholeiite or alkali basalt
categories if detailed petrographic or chemical data are available.
- Alkali olivine basalt is silica-undersaturated, characterized by the
absence of orthopyroxene, absence of quartz, presence of olivine, and
typically contains some feldspathoid mineral, alkali feldspar or
phlogopite in the groundmass. Feldspar phenocrysts typically are
labradorite to andesine in composition. Augite is rich in titanium
compared to augite in tholeiitic basalt. Alkali olivine basalt is
relatively rich in sodium.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali-Olivine_Basalt
- **Other Properties:**

[]{#tholeiitic_basalt}

#######  tholeiitic basalt
- **Child of**:
 [`basalt`](#basalt)
- Definition of tholeiite and alkali basalt here are more proscriptive
than those found in most reference authorities. This is to actually
provide some descriptive criteria to allow assignment of rocks on a
hand sample basis to the tholeiite or alkali basalt categories if
detailed petrographic or chemical data are available.
- Tholeiitic basalt is defined here to contain 2 pyroxene phases and
interstitial quartz or tridymite or cristobalite in the groundmass.
Pyroxene (augite and orthopyroxene or pigeonite) and calcium-rich
plagioclase are common phenocryst minerals. Olivine may also be a
phenocryst, and when present, may have rims of pigeonite. Only in
tholeiitic basalt is olivine in reaction relationship with melt.
Interstitial siliceous residue may be present, and is often glassy.
Tholeiitic basalt is relatively poor in sodium. This category includes
most basalts of the ocean floor, most large oceanic islands, and
continental flood basalts such as the Columbia River Plateau.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tholeiitic_Basalt
- **Other Properties:**

[]{#gabbroic_rock}

######  gabbroic rock
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`gabbroid`](#gabbroid)
- Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_gabbro}

#######  foid bearing gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains 0-10 percent feldspathoid minerals and
no quartz in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Gabbro
- **Other Properties:**

[]{#gabbro}

#######  gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Note that this category includes gabbro (sensu stricto) of LeMaitre
et al. 2002, but is broader, including the other rock types defined by
orthopyroxene-clinopyroxene-olivine-hornblende mineral ratios.
- Gabbroic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF Field 10 as gabbro.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gabbro
- **Other Properties:**

[]{#quartz_gabbro}

#######  quartz gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Gabbro
- **Other Properties:**

[]{#doleritic_rock}

#####  doleritic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Dark colored gabbroic (basaltic) or dioritic (andesitic) rock
intermediate in grain size between basalt and gabbro and composed of
plagioclase, pyroxene and opaque minerals; often with ophitic texture.
Typically occurs as hypabyssal intrusions. Includes dolerite,
microdiorite, diabase and microgabbro.
- **Source:**
Neuendorf et al 2005; LeMaitre et al. 2002; Gillespie and Styles 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Doleritic_Rock
- **Other Properties:**

[]{#exotic_composition_igneous_rock}

#####  exotic composition igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Rock with 'exotic' mineralogical, textural or field setting
characteristics; typically dark colored, with abundant phenocrysts.
Criteria include: presence of greater than 10 percent melilite or
leucite, or presence of kalsilite, or greater than 50 percent
carbonate minerals. Includes Carbonatite, Melilitic rock, Kalsilitic
rocks, Kimberlite, Lamproite, Leucitic rock and Lamprophyres.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Exotic_Composition_Igneous_Rock
- **Other Properties:**

[]{#carbonatite}

######  carbonatite
- **Child of**:
 [`exotic composition igneous rock`](#exotic_composition_igneous_rock)
- Igneous rock composed of more than 50 percent modal carbonate
minerals.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonatite
- **Other Properties:**

[]{#exotic_alkaline_rock}

######  exotic alkaline rock
- **Child of**:
 [`exotic composition igneous rock`](#exotic_composition_igneous_rock)
- Kimberlite, lamproite, or lamprophyre. Generally are potassic, mafic
or ultramafic rocks. Olivine (commonly serpentinized in kimberlite),
and phlogopite are significant constituents.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Exotic_Alkaline_Rock
- **Other Properties:**

[]{#kalsilitic_and_melilitic_rock}

######  kalsilitic and melilitic rocks
- **Child of**:
 [`exotic composition igneous rock`](#exotic_composition_igneous_rock)
- Igneous rock containing greater than 10 percent melilite or
kalsilite. Typically undersaturated, ultrapotassic (kalsilitic rocks)
or calcium-rich (melilitic rocks) mafic or ultramafic rocks.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Kalsilitic_And_Melilitic_Rock
- **Other Properties:**

[]{#fine_grained_igneous_rock}

#####  fine grained igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Need to make decision as to whether devitrified glass should be
considered glass or microcrystalline framework for purposes of
categorization
- Igneous rock in which the framework of the rock consists of crystals
that are too small to determine mineralogy with the unaided eye;
framework may include up to 50 percent glass. A significant percentage
of the rock by volume may be phenocrysts. Includes rocks that are
generally called volcanic rocks.
- **Alternate labels:**
volcanic rock
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fine_Grained_Igneous_Rock
- **Other Properties:**

[]{#andesite}

######  andesite
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
- Note the mela-andesite and leuco-basalt categories are not
recommended in this system. If chemical analytical data are available
to constrain the silica content, the basalt or andesite category
should be used.
- Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Andesite
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#basalt}

######  basalt
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basalt
- **Other Properties:**

[]{#alkali-olivine_basalt}

#######  alkali olivine basalt
- **Child of**:
 [`basalt`](#basalt)
- The definition of tholeiite and alkali basalt here are more
prescriptive than those found in most reference authorities. This is
to actually provide some descriptive criteria to allow assignment of
rocks on a hand sample basis to the tholeiite or alkali basalt
categories if detailed petrographic or chemical data are available.
- Alkali olivine basalt is silica-undersaturated, characterized by the
absence of orthopyroxene, absence of quartz, presence of olivine, and
typically contains some feldspathoid mineral, alkali feldspar or
phlogopite in the groundmass. Feldspar phenocrysts typically are
labradorite to andesine in composition. Augite is rich in titanium
compared to augite in tholeiitic basalt. Alkali olivine basalt is
relatively rich in sodium.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali-Olivine_Basalt
- **Other Properties:**

[]{#tholeiitic_basalt}

#######  tholeiitic basalt
- **Child of**:
 [`basalt`](#basalt)
- Definition of tholeiite and alkali basalt here are more proscriptive
than those found in most reference authorities. This is to actually
provide some descriptive criteria to allow assignment of rocks on a
hand sample basis to the tholeiite or alkali basalt categories if
detailed petrographic or chemical data are available.
- Tholeiitic basalt is defined here to contain 2 pyroxene phases and
interstitial quartz or tridymite or cristobalite in the groundmass.
Pyroxene (augite and orthopyroxene or pigeonite) and calcium-rich
plagioclase are common phenocryst minerals. Olivine may also be a
phenocryst, and when present, may have rims of pigeonite. Only in
tholeiitic basalt is olivine in reaction relationship with melt.
Interstitial siliceous residue may be present, and is often glassy.
Tholeiitic basalt is relatively poor in sodium. This category includes
most basalts of the ocean floor, most large oceanic islands, and
continental flood basalts such as the Columbia River Plateau.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tholeiitic_Basalt
- **Other Properties:**

[]{#dacite}

######  dacite
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dacite
- **Other Properties:**

[]{#foiditoid}

######  foiditoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained crystalline rock containing less than 90 percent mafic
minerals and more than 60 percent feldspathoid minerals in the QAPF
fraction. Includes rocks defined modally in QAPF field 15 or
chemically in TAS field F.
- **Alternate labels:**
foidite (sensu lato), 
foiditic rock, 
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foiditoid
- **Other Properties:**

[]{#basanitic_foidite}

#######  basanitic foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains less than 90 percent feldspathoid minerals
in the QAPF fraction, and has a plagioclase to total feldspar ratio
that is greater than 0.5, with greater than 10 percent normative
olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Basanitic_Foidite
- **Other Properties:**

[]{#foidite}

#######  foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains greater than 90 percent feldspathoid
minerals in the QAPF fraction.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foidite
- **Other Properties:**

[]{#phonolitic_foidite}

#######  phonolitic foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains less than 90 percent feldspathoid minerals
in the QAPF fraction, and has a plagioclase to total feldspar ratio
that is less than 0.5
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolitic_Foidite
- **Other Properties:**

[]{#tephritic_foidite}

#######  tephritic foidite
- **Child of**:
 [`foiditoid`](#foiditoid)
- Foiditoid that contains less than 90 percent feldspathoid minerals
in the QAPF fraction, and has a plagioclase to total feldspar ratio
that is greater than 0.5, with less than 10 percent normative olivine
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tephritic_Foidite
- **Other Properties:**

[]{#high_magnesium_fine_grained_igneous_rock}

######  high magnesium fine grained igneous rock
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- fine-grained igneous rock that contains unusually high concentration
of MgO. For rocks that contain greater than 52 percent silica, MgO
must be greater than 8 percent. For rocks containing less than 52
percent silica, MgO must be greater than 12 percent.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/High_Magnesium_Fine_Grained_Igneous_Rock
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#komatiitic_rock}

#######  komatiitic rock
- **Child of**:
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic, magnesium-rich volcanic rock, typically with spinifex
texture of intergrown skeletal and bladed olivine and pyroxene
crystals set in abundant glass. Includes komatiite and meimechite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Komatiitic_Rock
- **Other Properties:**

[]{#phonolitoid}

######  phonolitoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained igneous rock than contains less than 90 percent mafic
minerals, between 10 and 60 percent feldspathoid mineral in the QAPF
fraction and has a plagioclase to total feldspar ratio less than 0.5.
Includes rocks defined modally in QAPF fields 11 and 12, and TAS field
Ph.
- **Alternate labels:**
phonolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phonolitoid
- **Other Properties:**

[]{#phonolilte}

#######  phonolite
- **Child of**:
 [`phonolitoid`](#phonolitoid)
- Phonolitoid in which the plagioclase to total feldspar ratio is less
than 0.1. Rock consists of alkali feldspar, feldspathoid minerals, and
mafic minerals.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolilte
- **Other Properties:**

[]{#tephritic_phonolite}

#######  tephritic phonolite
- **Child of**:
 [`phonolitoid`](#phonolitoid)
- Phonolitoid that has a plagioclase to total feldspar ratio between
0.1 and 0.5. Broadly corresponds to TAS tephriphonolite of TAS field
U3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tephritic_Phonolite
- **Other Properties:**

[]{#rhyolitoid}

######  rhyolitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Note that technical definition, based on modal mineralogy plotted in
a QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
- fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.
- **Alternate labels:**
rhyolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Rhyolitoid
- **Other Properties:**

[]{#alkali_feldspar_rhyolite}

#######  alkali feldspar rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- Rhyolitoid in which the ratio of plagioclase to total feldspar is
less than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Rhyolite
- **Other Properties:**

[]{#rhyolite}

#######  rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- rhyolitoid in which the ratio of plagioclase to total feldspar is
between 0.1 and 0.65.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rhyolite
- **Other Properties:**

[]{#tephritoid}

######  tephritoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained igneous rock than contains less than 90 percent mafic
minerals, between 10 and 60 percent feldspathoid mineral in the QAPF
fraction and has a plagioclase to total feldspar ratio greater than
0.5. Includes rocks classified in QAPF field 13 and 14 or chemically
in TAS field U1 as basanite or tephrite.
- **Alternate labels:**
tephritic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tephritoid
- **Other Properties:**

[]{#basanite}

#######  basanite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio greater
than 0.9, and contains more than 10 percent normative (CIPW) olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Basanite
- **Other Properties:**

[]{#phonolitic_basanite}

#######  phonolitic basanite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio between
0.5 and 0.9, and contains more than 10 percent normative (CIPW)
olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolitic_Basanite
- **Other Properties:**

[]{#phonolitic_tephrite}

#######  phonolitic tephrite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio between
0.5 and 0.9, and contains less than 10 percent normative (CIPW)
olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phonolitic_Tephrite
- **Other Properties:**

[]{#tephrite}

#######  tephrite
- **Child of**:
 [`tephritoid`](#tephritoid)
- Tephritoid that has a plagioclase to total feldspar ratio greater
than 0.9, and contains less than 10 percent normative (CIPW) olivine.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tephrite
- **Other Properties:**

[]{#trachytoid}

######  trachytoid
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained igneous rock than contains less than 90 percent mafic
minerals, less than 10 percent feldspathoid mineral and less than 20
percent quartz in the QAPF fraction and has a plagioclase to total
feldspar ratio less than 0.65. Mafic minerals typically include
amphibole or mica; typically porphyritic. Includes rocks defined
modally in QAPF fields 6, 7 and 8 (with subdivisions) or chemically in
TAS Field T as trachyte or latite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Trachytoid
- **Other Properties:**

[]{#alkali_feldspar_trachytic_rock}

#######  alkali feldspar trachytic rock
- **Child of**:
 [`trachytoid`](#trachytoid)
- Trachytoid that has a plagioclase to total feldspar ratio less than
0.1. QAPF fields 6, 6', and 6*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Trachytic_Rock
- **Other Properties:**

[]{#alkali_feldspar_trachyte}

########  alkali feldspar trachyte
- **Child of**:
 [`alkali feldspar trachytic rock`](#alkali_feldspar_trachytic_rock)
- Trachytoid that has a plagioclase to total feldspar ratio less than
0.1, between 0 and 5 percent quartz in the QAPF fraction, and no
feldspathoid minerals. QAPF field 6.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Trachyte
- **Other Properties:**

[]{#foid_bearing_alkali_feldspar_trachyte}

########  foid bearing alkali feldspar trachyte
- **Child of**:
 [`alkali feldspar trachytic rock`](#alkali_feldspar_trachytic_rock)
- Alkali feldspar trachytic rock that contains no quartz and between 0
and 10 percent feldspathoid mineral in the QAPF fraction. QAPF field
6'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Alkali_Feldspar_Trachyte
- **Other Properties:**

[]{#quartz_alkali_feldspar_trachyte}

########  quartz alkali feldspar trachyte
- **Child of**:
 [`alkali feldspar trachytic rock`](#alkali_feldspar_trachytic_rock)
- Alkali feldspar trachytic rock that contains and between 5 and 20
percent quartz mineral in the QAPF fraction. QAPF field 6*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Alkali_Feldspar_Trachyte
- **Other Properties:**

[]{#latitic_rock}

#######  latitic rock
- **Child of**:
 [`trachytoid`](#trachytoid)
- Trachytoid that has a plagioclase to total feldspar ratio between
0.35 and 0.65. QAPF fields 8, 8' and 8*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Latitic_Rock
- **Other Properties:**

[]{#foid_bearing_latite}

########  foid bearing latite
- **Child of**:
 [`latitic rock`](#latitic_rock)
- Latitic rock that contains no quartz and between 0 and 10 percent
feldspathoid minerals in the QAPF fraction. QAPF field 8'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Latite
- **Other Properties:**

[]{#latite}

########  latite
- **Child of**:
 [`latitic rock`](#latitic_rock)
- Latitic rock that contains between 0 and 5 percent quartz and no
feldspathoid in the QAPF fraction. QAPF field 8.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Latite
- **Other Properties:**

[]{#quartz_latite}

########  quartz latite
- **Child of**:
 [`latitic rock`](#latitic_rock)
- Latitic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 8*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Latite
- **Other Properties:**

[]{#trachytic_rock}

#######  trachytic rock
- **Child of**:
 [`trachytoid`](#trachytoid)
- LeMaitre et al. (2002) used 'trachyte' to refer to QAPF fields 7,
7', and 7* in the text (p. 30) as well as to the more restrictive
category (QAPF field 7 only). The term Trachytic rock is introduced
here to label this more general category of trachyte.
- Trachytoid that has a plagioclase to total feldspar ratio between
0.1 and 0.35. QAPF fields 7, 7', and 7*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Trachytic_Rock
- **Other Properties:**

[]{#foid_bearing_trachyte}

########  foid bearing trachyte
- **Child of**:
 [`trachytic rock`](#trachytic_rock)
- Trachytic rock that contains between 0 and 10 percent feldspathoid
in the QAPF fraction, and no quartz. QAPF field 7'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Trachyte
- **Other Properties:**

[]{#quartz_trachyte}

########  quartz trachyte
- **Child of**:
 [`trachytic rock`](#trachytic_rock)
- Trachytic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 7*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Trachyte
- **Other Properties:**

[]{#trachyte}

########  trachyte
- **Child of**:
 [`trachytic rock`](#trachytic_rock)
- Trachytoid that has a plagioclase to total feldspar ratio between
0.1 and 0.35, between 0 and 5 percent quartz in the QAPF fraction, and
no feldspathoid minerals. QAPF field 7.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Trachyte
- **Other Properties:**

[]{#fragmental_igneous_rock}

#####  fragmental igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Rock`](#rock)
 [`fragmental igneous material`](#fragmental_igneous_material)
- Igneous rock in which greater than 75 percent of the rock consists
of fragments produced as a result of igneous rock-forming process.
Includes pyroclastic rocks, autobreccia associated with lava flows and
intrusive breccias. Excludes deposits reworked by epiclastic processes
(see Tuffite)
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fragmental_Igneous_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#glass_rich_igneous_rock}

#####  glass rich igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock that contains greater than 50 percent massive glass.
- **Source:**
This vocabulary, based on Gillespie and Styles 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Glass_Rich_Igneous_Rock
- **Other Properties:**

[]{#glassy_igneous_rock}

######  glassy igneous rock
- **Child of**:
 [`glass rich igneous rock`](#glass_rich_igneous_rock)
- Note that this category is used for massive glassy rocks. Much of
the pyroclastic material in a pyroclastic rock may be composed of
glass, but the rock is named based on its fragmental nature.
- Igneous rock that consists of greater than 80 percent massive glass.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Glassy_Igneous_Rock
- **Other Properties:**

[]{#hypabyssal_intrusive_rock}

#####  hypabyssal intrusive rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rocks formed by crystallisation close to the Earth's
surface, characterized by more rapid cooling than plutonic setting to
produce generally fine-grained intrusive igneous rock, commonly
associated with co-magmatic volcanic rocks.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hypabyssal_Intrusive_Rock
- **Other Properties:**

[]{#intermediate_composition_igneous_rock}

#####  intermediate composition igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`intermediate composition igneous material`](#intermediate_composition_igneous_material)
- Igneous rock with between 52 and 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Intermediate_Composition_Igneous_Rock
- **Other Properties:**

[]{#andesite}

######  andesite
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
- Note the mela-andesite and leuco-basalt categories are not
recommended in this system. If chemical analytical data are available
to constrain the silica content, the basalt or andesite category
should be used.
- Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Andesite
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#dioritoid}

######  dioritoid
- **Child of**:
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
of intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dioritoid
- **Other Properties:**

[]{#dioritic_rock}

#######  dioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. A dioritoid with a plagioclase to total feldspar
ratio (in the QAPF fraction) greater than 0.9. Includes rocks defined
modally in QAPF fields 10, 10' and 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dioritic_Rock
- **Other Properties:**

[]{#diorite}

########  diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Phaneritic crystalline rock consisting of intermediate plagioclase,
commonly with hornblende and often with biotite or augite; colour
index M less than 90, sodic plagioclase (An0-An50), no feldspathoid,
and between 0 and 5 percent quartz. Includes rocks defined modally in
QAPF field 10 as diorite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Diorite
- **Other Properties:**

[]{#foid_bearing_diorite}

########  foid bearing diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 0 and 10 percent feldspathoid
minerals in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Diorite
- **Other Properties:**

[]{#quartz_diorite}

########  quartz diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 5 to 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Diorite
- **Other Properties:**

[]{#monzodioritic_rock}

#######  monzodioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 10 percent feldspathoid or 0 to 20 percent
quartz in the QAPF fraction. Plagioclase to total feldspar ratio in
the QAPF fraction is between 0.65 and 0.9. Includes rocks defined
modally in QAPF field 9, 9' and 9* as monzodiorite, foid-beaing
monzodiorite, and quartz monzodiorite.
- **Source:**
This vocabulary; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodioritic_Rock
- **Other Properties:**

[]{#foid_bearing_monzodiorite}

########  foid bearing monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 0 and 10 percent
feldspathoid mineral.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzodiorite
- **Other Properties:**

[]{#monzodiorite}

########  monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 5 percent quartz. Includes rocks defined
modally in QAPF field 9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodiorite
- **Other Properties:**

[]{#quartz_monzodiorite}

########  quartz monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 5 and 20 percent quartz.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzodiorite
- **Other Properties:**

[]{#phaneritic_igneous_rock}

#####  phaneritic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock in which the framework of the rock consists of
individual crystals that can be discerned with the unaided eye.
Bounding grain size is on the order of 32 to 100 microns. Igneous
rocks with 'exotic' composition are excluded from this concept.
- **Alternate labels:**
coarse grained crystalline igneous rock, 
plutonic rock, 
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phaneritic_Igneous_Rock
- **Other Properties:**

[]{#anorthositic_rock}

######  anorthositic rock
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Anorthositic rock term invented to label the combined QAPF fields
10, 10*, and 10', in order to construct hierarchy in this vocabulary.
- Leucocratic phaneritic crystalline igneous rock consisting
essentially of plagioclase, often with small amounts of pyroxene. By
definition, colour index M is less than 10, and plagiclase to total
feldspar ratio is greater than 0.9. Less than 20 percent quartz and
less than 10 percent feldspathoid in the QAPF fraction. QAPF field 10,
10*, and 10'.
- Anorthositic rock term invented to label the combined QAPF fields
10, 10*, and 10', in order to construct hierarchy in this vocabulary.
- Leucocratic phaneritic crystalline igneous rock consisting
essentially of plagioclase, often with small amounts of pyroxene. By
definition, colour index M is less than 10, and plagiclase to total
feldspar ratio is greater than 0.9. Less than 20 percent quartz and
less than 10 percent feldspathoid in the QAPF fraction. QAPF field 10,
10*, and 10'.
- **Source:**
LeMaitre et al. 2002; This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Anorthositic_Rock
- **Other Properties:**

[]{#anorthosite}

#######  anorthosite
- **Child of**:
 [`anorthositic rock`](#anorthositic_rock)
- Anorthositic rock that contains between 0 and 5 percent quartz and
no feldspathoid mineral in the QAPF fraction. QAPF field 10.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anorthosite
- **Other Properties:**

[]{#foid_bearing_anorthosite}

#######  foid bearing anorthosite
- **Child of**:
 [`anorthositic rock`](#anorthositic_rock)
- Anorthositic rock that contains between 0 and 10 percent
feldspathoid mineral and no quartz in the QAPF fraction. QAPF field
10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Anorthosite
- **Other Properties:**

[]{#quartz_anorthosite}

#######  quartz anorthosite
- **Child of**:
 [`anorthositic rock`](#anorthositic_rock)
- Anorthositic rock that contains between 5 and 20 percent quartz in
the QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Anorthosite
- **Other Properties:**

[]{#aplite}

######  aplite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Light coloured crystalline rock, characterized by a fine grained
allotriomorphic-granular (aplitic, saccharoidal or xenomorphic)
texture; typically granitic composition, consisting of quartz, alkali
feldspar and sodic plagioclase.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Aplite
- **Other Properties:**

[]{#dioritoid}

######  dioritoid
- **Child of**:
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
of intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dioritoid
- **Other Properties:**

[]{#dioritic_rock}

#######  dioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. A dioritoid with a plagioclase to total feldspar
ratio (in the QAPF fraction) greater than 0.9. Includes rocks defined
modally in QAPF fields 10, 10' and 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dioritic_Rock
- **Other Properties:**

[]{#diorite}

########  diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Phaneritic crystalline rock consisting of intermediate plagioclase,
commonly with hornblende and often with biotite or augite; colour
index M less than 90, sodic plagioclase (An0-An50), no feldspathoid,
and between 0 and 5 percent quartz. Includes rocks defined modally in
QAPF field 10 as diorite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Diorite
- **Other Properties:**

[]{#foid_bearing_diorite}

########  foid bearing diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 0 and 10 percent feldspathoid
minerals in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Diorite
- **Other Properties:**

[]{#quartz_diorite}

########  quartz diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 5 to 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Diorite
- **Other Properties:**

[]{#monzodioritic_rock}

#######  monzodioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 10 percent feldspathoid or 0 to 20 percent
quartz in the QAPF fraction. Plagioclase to total feldspar ratio in
the QAPF fraction is between 0.65 and 0.9. Includes rocks defined
modally in QAPF field 9, 9' and 9* as monzodiorite, foid-beaing
monzodiorite, and quartz monzodiorite.
- **Source:**
This vocabulary; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodioritic_Rock
- **Other Properties:**

[]{#foid_bearing_monzodiorite}

########  foid bearing monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 0 and 10 percent
feldspathoid mineral.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzodiorite
- **Other Properties:**

[]{#monzodiorite}

########  monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 5 percent quartz. Includes rocks defined
modally in QAPF field 9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodiorite
- **Other Properties:**

[]{#quartz_monzodiorite}

########  quartz monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 5 and 20 percent quartz.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzodiorite
- **Other Properties:**

[]{#foid_dioritoid}

######  foid dioritoid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock in which M is less than 90, the
plagioclase to total feldspar ratio is greater than 0.5, feldspathoid
minerals form 10-60 percent of the QAPF fraction, plagioclase has
anorthite content less than 50 percent. These rocks typically contain
large amounts of mafic minerals. Includes rocks defined modally in
QAPF fields 13 and 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foid_Dioritoid
- **Other Properties:**

[]{#foid_diorite}

#######  foid diorite
- **Child of**:
 [`foid dioritoid`](#foid_dioritoid)
- Foid dioritoid in which the plagioclase to total feldspar ratio is
greater than 0.9. Includes rocks defined modally in QAPF field 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Diorite
- **Other Properties:**

[]{#foid_monzodiorite}

#######  foid monzodiorite
- **Child of**:
 [`foid dioritoid`](#foid_dioritoid)
- Foid dioritoid in which the plagioclase to total feldspar ratio is
between 0.1 and 0.9. Includes rocks defined modally in QAPF field 13.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Monzodiorite
- **Other Properties:**

[]{#foid_gabbroid}

######  foid gabbroid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock in which M is less than 90, the
plagioclase to total feldspar ratio is greater than 0.5, feldspathoids
form 10-60 percent of the QAPF fraction, and plagioclase has anorthite
content greater than 50 percent. These rocks typically contain large
amounts of mafic minerals. Includes rocks defined modally in QAPF
fields 13 and 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foid_Gabbroid
- **Other Properties:**

[]{#foid_gabbro}

#######  foid gabbro
- **Child of**:
 [`foid gabbroid`](#foid_gabbroid)
- Foid gabbroid that has a plagioclase to total feldspar ratio greater
than 0.9. Includes rocks defined modally in QAPF field 14.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Gabbro
- **Other Properties:**

[]{#foid_monzogabbro}

#######  foid monzogabbro
- **Child of**:
 [`foid gabbroid`](#foid_gabbroid)
- Foid gabbroid that has a plagioclase to total feldspar ratio between
0.5 and 0.9. Includes rocks defined modally in QAPF field 13.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Monzogabbro
- **Other Properties:**

[]{#foid_syenitoid}

######  foid syenitoid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, contains
between 10 and 60 percent feldspathoid mineral in the QAPF fraction,
and has a plagioclase to total feldspar ratio less than 0.5. Includes
QAPF fields 11 and 12.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foid_Syenitoid
- **Other Properties:**

[]{#foid_monzosyenite}

#######  foid monzosyenite
- **Child of**:
 [`foid syenitoid`](#foid_syenitoid)
- Foid syenitoid rock that has a plagioclase to total feldspar ratio
of between 0.1 and 0.5. Includes rocks defined modally in QAPF Field
12.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Monzosyenite
- **Other Properties:**

[]{#foid_syenite}

#######  foid syenite
- **Child of**:
 [`foid syenitoid`](#foid_syenitoid)
- Foid syenitoid that has a plagioclase to total feldspar ratio of
less than 0.1. Includes rocks defined modally in QAPF field 11.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Syenite
- **Other Properties:**

[]{#foidolite}

######  foidolite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline rock containing more than 60 percent
feldspathoid minerals in the QAPF fraction. Includes rocks defined
modally in QAPF field 15
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Foidolite
- **Other Properties:**

[]{#gabbroid}

######  gabbroid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals, and up to 20 percent quartz or up to 10
percent feldspathoid in the QAPF fraction. The ratio of plagioclase to
total feldspar is greater than 0.65, and anorthite content of the
plagioclase is greater than 50 percent. Includes rocks defined modally
in QAPF fields 9 and 10 and their subdivisions.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroid
- **Other Properties:**

[]{#gabbroic_rock}

#######  gabbroic rock
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`gabbroid`](#gabbroid)
- Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_gabbro}

########  foid bearing gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains 0-10 percent feldspathoid minerals and
no quartz in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Gabbro
- **Other Properties:**

[]{#gabbro}

########  gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Note that this category includes gabbro (sensu stricto) of LeMaitre
et al. 2002, but is broader, including the other rock types defined by
orthopyroxene-clinopyroxene-olivine-hornblende mineral ratios.
- Gabbroic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF Field 10 as gabbro.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gabbro
- **Other Properties:**

[]{#quartz_gabbro}

########  quartz gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Gabbro
- **Other Properties:**

[]{#monzogabbroic_rock}

#######  monzogabbroic rock
- **Child of**:
 [`gabbroid`](#gabbroid)
- Gabbroid with a plagioclase to total feldspar ratio between 0.65 and
0.9. QAPF field 9, 9 prime and 9 asterisk
- **Source:**
LeMaitre et al. 2002, This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Monzogabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_monzogabbro}

########  foid bearing monzogabbro
- **Child of**:
 [`monzogabbroic rock`](#monzogabbroic_rock)
- Monzogabbroic rock that contains 0 to 10 percent feldspathoid
mineral in the QAPF fraction. QAPF field 9'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzogabbro
- **Other Properties:**

[]{#monzogabbro}

########  monzogabbro
- **Child of**:
 [`monzogabbroic rock`](#monzogabbroic_rock)
- Monzogabbroic rock that contains between 0 an 5 percent quartz and
no feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF field 9 .
- **Source:**
LeMaitre et al. 2002, This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogabbro
- **Other Properties:**

[]{#quartz_monzogabbro}

########  quartz monzogabbro
- **Child of**:
 [`monzogabbroic rock`](#monzogabbroic_rock)
- Monzogabbroic rock that contains between 5 and 20 percent quartz in
the QAPF fraction. QAPF field 9*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzogabbro
- **Other Properties:**

[]{#granitoid}

######  granitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.
- **Alternate labels:**
granitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granitoid
- **Other Properties:**

[]{#alkali_feldspar_granite}

#######  alkali feldspar granite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitic rock that has a plagioclase to total feldspar ratio less
than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Alkali_Feldspar_Granite
- **Other Properties:**

[]{#granite}

#######  granite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting of quartz, alkali feldspar
and plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granite
- **Other Properties:**

[]{#monzogranite}

########  monzogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.35
and 0.65. QAPF field 3b.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogranite
- **Other Properties:**

[]{#syenogranite}

########  syenogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.10
and 0.35. QAPF field 3a.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenogranite
- **Other Properties:**

[]{#granodiorite}

#######  granodiorite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granodiorite
- **Other Properties:**

[]{#tonalite}

#######  tonalite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tonalite
- **Other Properties:**

[]{#hornblendite}

######  hornblendite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock that consists of greater than 40 percent hornblende
plus pyroxene and has a hornblende to pyroxene ratio greater than 1.
Includes olivine hornblendite, olivine-pyroxene hornblendite, pyroxene
hornblendite, and hornblendite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hornblendite
- **Other Properties:**

[]{#pegmatite}

######  pegmatite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Exceptionally coarse grained crystalline rock with interlocking
crystals; most grains are 1cm or more diameter; composition is
generally that of granite, but the term may refer to the coarse
grained facies of any type of igneous rock;usually found as irregular
dikes, lenses, or veins associated with plutons or batholiths.
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pegmatite
- **Other Properties:**

[]{#peridotite}

######  peridotite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock consisting of more than 40 percent (by volume)
olivine with pyroxene and/or amphibole and little or no feldspar.
commonly altered to serpentinite. Includes rocks defined modally in
the ultramafic rock classification as dunite, harzburgite, lherzolite,
wehrlite, olivinite, pyroxene peridotite, pyroxene hornblende
peridotite or hornblende peridotite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Peridotite
- **Other Properties:**

[]{#pyroxenite}

######  pyroxenite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic phaneritic igneous rock composed almost entirely of one
or more pyroxenes and occasionally biotite, hornblende and olivine.
Includes rocks defined modally in the ultramafic rock classification
as olivine pyroxenite, olivine-hornblende pyroxenite, pyroxenite,
orthopyroxenite, clinopyroxenite and websterite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroxenite
- **Other Properties:**

[]{#quartz_rich_igneous_rock}

######  quartz rich igneous rock
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals and contains greater than 60 percent quartz in
the QAPF fraction.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Quartz_Rich_Igneous_Rock
- **Other Properties:**

[]{#syenitoid}

######  syenitoid
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
mainly of alkali feldspar and plagioclase; minor quartz or nepheline
may be present, along with pyroxene, amphibole or biotite. Ratio of
plagioclase to total feldspar is less than 0.65, quartz forms less
than 20 percent of QAPF fraction, and feldspathoid minerals form less
than 10 percent of QAPF fraction. Includes rocks classified in QAPF
fields 6, 7 and 8 and their subdivisions.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Syenitoid
- **Other Properties:**

[]{#alkali_feldspar_syenitic_rock}

#######  alkali feldspar syenitic rock
- **Child of**:
 [`syenitoid`](#syenitoid)
- Syenitoid with a plagioclase to total feldspar ratio of less than
0.1. QAPF fields 6, 6*, and 6'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Syenitic_Rock
- **Other Properties:**

[]{#alkali_feldspar_syenite}

########  alkali feldspar syenite
- **Child of**:
 [`alkali feldspar syenitic rock`](#alkali_feldspar_syenitic_rock)
- Alkali feldspar syenitic rock that contains 0-5 percent quartz and
no feldspathoid in the QAPF fraction. QAPF field 6.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Syenite
- **Other Properties:**

[]{#foid_bearing_alkali_feldspar_syenite}

########  foid bearing alkali feldspar syenite
- **Child of**:
 [`alkali feldspar syenitic rock`](#alkali_feldspar_syenitic_rock)
- Alkali feldspar syenitic rock that contains 0-10 percent
feldspathoid mineral and no quartz in the QAPF fraction. QAPF field
6'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Alkali_Feldspar_Syenite
- **Other Properties:**

[]{#quartz_alkali_feldspar_syenite}

########  quartz alkali feldspar syenite
- **Child of**:
 [`alkali feldspar syenitic rock`](#alkali_feldspar_syenitic_rock)
- Alkali feldspar syenitic rock that contains 5 to 20 percent quartz
and no feldspathoid in the QAPF fraction. QAPF field 6*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Alkali_Feldspar_Syenite
- **Other Properties:**

[]{#monzonitic_rock}

#######  monzonitic rock
- **Child of**:
 [`syenitoid`](#syenitoid)
- Syenitoid with a plagioclase to total feldspar ratio between 0.35
and 0.65. Includes rocks in QAPF fields 8, 8*, and 8'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzonitic_Rock
- **Other Properties:**

[]{#foid_bearing_monzonite}

########  foid bearing monzonite
- **Child of**:
 [`monzonitic rock`](#monzonitic_rock)
- Monzonitic rock that contains 0-10 percent feldspathoid mineral and
no quartz in the QAPF fraction. Includes rocks defined modally in QAPF
Field 8'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzonite
- **Other Properties:**

[]{#monzonite}

########  monzonite
- **Child of**:
 [`monzonitic rock`](#monzonitic_rock)
- Monzonitic rock that contains 0-5 percent quartz and no feldspathoid
mineral in the QAPF fraction. Includes rocks defined modally in QAPF
Field 8.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzonite
- **Other Properties:**

[]{#quartz_monzonite}

########  quartz monzonite
- **Child of**:
 [`monzonitic rock`](#monzonitic_rock)
- Monzonitic rock that contains 5-20 percent quartz iin the QAPF
fraction. Includes rocks defined modally in QAPF Field 8*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzonite
- **Other Properties:**

[]{#syenitic_rock}

#######  syenitic rock
- **Child of**:
 [`syenitoid`](#syenitoid)
- Syenitoid with a plagioclase to total feldspar ratio between 0.1 and
0.35. Includes rocks in QAPF fields 7, 7*, and 7'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenitic_Rock
- **Other Properties:**

[]{#foid_bearing_syenite}

########  foid bearing syenite
- **Child of**:
 [`syenitic rock`](#syenitic_rock)
- Syenitic rock that contains between 0 and 10 percent feldspathoid
mineral and no quartz in the QAPF fraction. Defined modally in QAPF
Field 7'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Syenite
- **Other Properties:**

[]{#quartz_syenite}

########  quartz syenite
- **Child of**:
 [`syenitic rock`](#syenitic_rock)
- Syenitic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. Defined modally in QAPF Field 7*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Syenite
- **Other Properties:**

[]{#syenite}

########  syenite
- **Child of**:
 [`syenitic rock`](#syenitic_rock)
- Syenitic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Defined modally in QAPF
Field 7.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenite
- **Other Properties:**

[]{#plutonic_igneous_rock}

#####  plutonic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Instrusive igneous rock formed by crystallisation of magma far
enough below Earth surface that complete crystallization of magma
bodies forms holocrystalline medium to coarse grained igneous rock,
wall rocks generally do not include volcanic products related to the
magma, and some contact metamorphism is tyypically developed at
intrusive contacts.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Plutonic_Igneous_Rock
- **Other Properties:**

[]{#porphyry}

#####  porphyry
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock that contains conspicuous phenocrysts in a finer
grained groundmass; groundmass itself may be phaneritic or fine-
grained.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Porphyry
- **Other Properties:**

[]{#ultrabasic_igneous_rock}

#####  ultrabasic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock with less than 45 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Ultrabasic_Igneous_Rock
- **Other Properties:**

[]{#ultramafic_igneous_rock}

#####  ultramafic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
- Igneous rock that consists of greater than 90 percent mafic
minerals.
- **Source:**
LeMaitre et al. 2002; Gillespie and Styles 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Ultramafic_Igneous_Rock
- **Other Properties:**

[]{#hornblendite}

######  hornblendite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock that consists of greater than 40 percent hornblende
plus pyroxene and has a hornblende to pyroxene ratio greater than 1.
Includes olivine hornblendite, olivine-pyroxene hornblendite, pyroxene
hornblendite, and hornblendite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hornblendite
- **Other Properties:**

[]{#peridotite}

######  peridotite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic rock consisting of more than 40 percent (by volume)
olivine with pyroxene and/or amphibole and little or no feldspar.
commonly altered to serpentinite. Includes rocks defined modally in
the ultramafic rock classification as dunite, harzburgite, lherzolite,
wehrlite, olivinite, pyroxene peridotite, pyroxene hornblende
peridotite or hornblende peridotite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Peridotite
- **Other Properties:**

[]{#pyroxenite}

######  pyroxenite
- **Child of**:
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic phaneritic igneous rock composed almost entirely of one
or more pyroxenes and occasionally biotite, hornblende and olivine.
Includes rocks defined modally in the ultramafic rock classification
as olivine pyroxenite, olivine-hornblende pyroxenite, pyroxenite,
orthopyroxenite, clinopyroxenite and websterite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroxenite
- **Other Properties:**

[]{#komatiitic_rock}

######  komatiitic rock
- **Child of**:
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
 [`ultramafic igneous rock`](#ultramafic_igneous_rock)
- Ultramafic, magnesium-rich volcanic rock, typically with spinifex
texture of intergrown skeletal and bladed olivine and pyroxene
crystals set in abundant glass. Includes komatiite and meimechite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Komatiitic_Rock
- **Other Properties:**

[]{#volcanic_rock}

#####  Volcanic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Volcanic Material`](#volcanic_material)
- Rock that exhibits direct evidence of extrusive igneous processes in
its genesis.
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Volcanic_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#lava}

######  Lava
- **Child of**:
 [`Volcanic rock`](#volcanic_rock)
- Volcanic Rock with features indicating origin by extrusive lava
flow.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Lava
- **Other Properties:**

[]{#acidic_igneous_material}

####  acidic igneous material
- **Child of**:
 [`Igneous material`](#igneous_material)
- Igneous material with more than 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Acidic_Igneous_Material
- **Other Properties:**

[]{#acidic_igneous_rock}

#####  acidic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`acidic igneous material`](#acidic_igneous_material)
- Igneous rock with more than 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Acidic_Igneous_Rock
- **Other Properties:**

[]{#dacite}

######  dacite
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine grained or porphyritic crystalline rock that contains less than
90 percent mafic minerals, between 20 and 60 percent quartz in the
QAPF fraction, and has a plagioclase to total feldspar ratio greater
than 0.65. Includes rocks defined modally in QAPF fields 4 and 5 or
chemically in TAS Field O3. Typically composed of quartz and sodic
plagioclase with minor amounts of biotite and/or hornblende and/or
pyroxene; fine-grained equivalent of granodiorite and tonalite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dacite
- **Other Properties:**

[]{#granitoid}

######  granitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock consisting of quartz, alkali
feldspar and/or plagioclase. Includes rocks defined modally in QAPF
fields 2, 3, 4 and 5 as alkali feldspar granite, granite, granodiorite
or tonalite.
- **Alternate labels:**
granitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granitoid
- **Other Properties:**

[]{#alkali_feldspar_granite}

#######  alkali feldspar granite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitic rock that has a plagioclase to total feldspar ratio less
than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Alkali_Feldspar_Granite
- **Other Properties:**

[]{#granite}

#######  granite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting of quartz, alkali feldspar
and plagioclase (typically sodic) in variable amounts, usually with
biotite and/or hornblende. Includes rocks defined modally in QAPF
Field 3.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granite
- **Other Properties:**

[]{#monzogranite}

########  monzogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.35
and 0.65. QAPF field 3b.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzogranite
- **Other Properties:**

[]{#syenogranite}

########  syenogranite
- **Child of**:
 [`granite`](#granite)
- Granite that has a plagiolcase to total feldspar ratio between 0.10
and 0.35. QAPF field 3a.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Syenogranite
- **Other Properties:**

[]{#granodiorite}

#######  granodiorite
- **Child of**:
 [`granitoid`](#granitoid)
- Phaneritic crystalline rock consisting essentially of quartz, sodic
plagioclase and lesser amounts of alkali feldspar with minor
hornblende and biotite. Includes rocks defined modally in QAPF field
4.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Granodiorite
- **Other Properties:**

[]{#tonalite}

#######  tonalite
- **Child of**:
 [`granitoid`](#granitoid)
- Granitoid consisting of quartz and intermediate plagioclase, usually
with biotite and amphibole. Includes rocks defined modally in QAPF
field 5; ratio of plagioclase to total feldspar is greater than 0.9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tonalite
- **Other Properties:**

[]{#quartz_rich_igneous_rock}

######  quartz rich igneous rock
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Occurrence of igneous rocks meeting this criteria seems to be
vanishingly rare, thus subdividing the category does not seem
warranted for the purposes of This vocabulary. Future usage of the
vocabulary may motivate including quatzolite and quartz-rich granitoid
in future revisions
- Phaneritic crystalline igneous rock that contains less than 90
percent mafic minerals and contains greater than 60 percent quartz in
the QAPF fraction.
- **Source:**
Gillespie and Styles 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Quartz_Rich_Igneous_Rock
- **Other Properties:**

[]{#rhyolitoid}

######  rhyolitoid
- **Child of**:
 [`acidic igneous rock`](#acidic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Note that technical definition, based on modal mineralogy plotted in
a QAPF triangle may be applied qualitatively, based on phenocryst
mineralogy when ground mass mineralogy can not be determined
optically, or based on CIPW norm. Although TAS categories are defined
based on chemical analyses, the correspondence with the QAPF defined
categories is generally close enough that QAPF categories are commonly
used interchangeably with TAS categories. It is important to note the
basis for assignment of fine-grained igneous rocks to a specifice
lithology category.
- fine_grained_igneous_rock consisting of quartz and alkali feldspar,
with minor plagioclase and biotite, in a microcrystalline,
cryptocrystalline or glassy groundmass. Flow texture is common.
Includes rocks defined modally in QAPF fields 2 and 3 or chemically in
TAS Field R as rhyolite. QAPF normative definition is based on modal
mineralogy thus: less than 90 percent mafic minerals, between 20 and
60 percent quartz in the QAPF fraction, and ratio of plagioclse to
total feldspar is less than 0.65.
- **Alternate labels:**
rhyolitic rock
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Rhyolitoid
- **Other Properties:**

[]{#alkali_feldspar_rhyolite}

#######  alkali feldspar rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- Rhyolitoid in which the ratio of plagioclase to total feldspar is
less than 0.1. QAPF field 2.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali_Feldspar_Rhyolite
- **Other Properties:**

[]{#rhyolite}

#######  rhyolite
- **Child of**:
 [`rhyolitoid`](#rhyolitoid)
- rhyolitoid in which the ratio of plagioclase to total feldspar is
between 0.1 and 0.65.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rhyolite
- **Other Properties:**

[]{#basic_igneous_material}

####  basic igneous material
- **Child of**:
 [`Igneous material`](#igneous_material)
- Igneous material with between 45 and 52 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Basic_Igneous_Material
- **Other Properties:**

[]{#basic_igneous_rock}

#####  basic igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`basic igneous material`](#basic_igneous_material)
- Igneous rock with between 45 and 52 percent SiO2.
- **Source:**
Neuendorf et al 2005; LeMaitre et al. 2002; Gillespie and Styles 1999, 
after LeMaitre et al. 2002, 
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basic_Igneous_Rock
- **Other Properties:**

[]{#basalt}

######  basalt
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
- Fine-grained or porphyritic igneous rock with less than 20 percent
quartz, and less than 10 percent feldspathoid minerals, in which the
ratio of plagioclase to total feldspar is greater 0.65. Typically
composed of calcic plagioclase and clinopyroxene; phenocrysts
typically include one or more of calcic plagioclase, clinopyroxene,
orthopyroxene, and olivine. Includes rocks defined modally in QAPF
fields 9 and 10 or chemically in TAS field B as basalt. Basalt and
andesite are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Basalt
- **Other Properties:**

[]{#alkali-olivine_basalt}

#######  alkali olivine basalt
- **Child of**:
 [`basalt`](#basalt)
- The definition of tholeiite and alkali basalt here are more
prescriptive than those found in most reference authorities. This is
to actually provide some descriptive criteria to allow assignment of
rocks on a hand sample basis to the tholeiite or alkali basalt
categories if detailed petrographic or chemical data are available.
- Alkali olivine basalt is silica-undersaturated, characterized by the
absence of orthopyroxene, absence of quartz, presence of olivine, and
typically contains some feldspathoid mineral, alkali feldspar or
phlogopite in the groundmass. Feldspar phenocrysts typically are
labradorite to andesine in composition. Augite is rich in titanium
compared to augite in tholeiitic basalt. Alkali olivine basalt is
relatively rich in sodium.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Alkali-Olivine_Basalt
- **Other Properties:**

[]{#tholeiitic_basalt}

#######  tholeiitic basalt
- **Child of**:
 [`basalt`](#basalt)
- Definition of tholeiite and alkali basalt here are more proscriptive
than those found in most reference authorities. This is to actually
provide some descriptive criteria to allow assignment of rocks on a
hand sample basis to the tholeiite or alkali basalt categories if
detailed petrographic or chemical data are available.
- Tholeiitic basalt is defined here to contain 2 pyroxene phases and
interstitial quartz or tridymite or cristobalite in the groundmass.
Pyroxene (augite and orthopyroxene or pigeonite) and calcium-rich
plagioclase are common phenocryst minerals. Olivine may also be a
phenocryst, and when present, may have rims of pigeonite. Only in
tholeiitic basalt is olivine in reaction relationship with melt.
Interstitial siliceous residue may be present, and is often glassy.
Tholeiitic basalt is relatively poor in sodium. This category includes
most basalts of the ocean floor, most large oceanic islands, and
continental flood basalts such as the Columbia River Plateau.
- **Source:**
http://en.wikipedia.org/wiki/Basalt; Carmichael, I.S. Turner, F.J., Verhoogen, John, 1974, Igneous petrology: New York, McGraw HIll Book Co., p.42-43.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tholeiitic_Basalt
- **Other Properties:**

[]{#gabbroic_rock}

######  gabbroic rock
- **Child of**:
 [`basic igneous rock`](#basic_igneous_rock)
 [`gabbroid`](#gabbroid)
- Gabbroid that has a plagioclase to total feldspar ratio greater than
0.9 in the QAPF fraction. Includes QAPF fields 10*, 10, and 10'. This
category includes the various categories defined in LeMaitre et al.
(2002) based on the mafic mineralogy, but apparently not subdivided
based on the quartz/feldspathoid content.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gabbroic_Rock
- **Other Properties:**

[]{#foid_bearing_gabbro}

#######  foid bearing gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains 0-10 percent feldspathoid minerals and
no quartz in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Gabbro
- **Other Properties:**

[]{#gabbro}

#######  gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Note that this category includes gabbro (sensu stricto) of LeMaitre
et al. 2002, but is broader, including the other rock types defined by
orthopyroxene-clinopyroxene-olivine-hornblende mineral ratios.
- Gabbroic rock that contains between 0 and 5 percent quartz and no
feldspathoid mineral in the QAPF fraction. Includes rocks defined
modally in QAPF Field 10 as gabbro.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gabbro
- **Other Properties:**

[]{#quartz_gabbro}

#######  quartz gabbro
- **Child of**:
 [`gabbroic rock`](#gabbroic_rock)
- Gabbroic rock that contains between 5 and 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Gabbro
- **Other Properties:**

[]{#fragmental_igneous_material}

####  fragmental igneous material
- **Child of**:
 [`Igneous material`](#igneous_material)
- igneous_material of unspecified consolidation state in which greater
than 75 percent of the rock consists of fragments produced as a result
of igneous rock-forming process.
- **Source:**
CGI concept definition task group
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Fragmental_Igneous_Material
- **Other Properties:**

[]{#fragmental_igneous_rock}

#####  fragmental igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Rock`](#rock)
 [`fragmental igneous material`](#fragmental_igneous_material)
- Igneous rock in which greater than 75 percent of the rock consists
of fragments produced as a result of igneous rock-forming process.
Includes pyroclastic rocks, autobreccia associated with lava flows and
intrusive breccias. Excludes deposits reworked by epiclastic processes
(see Tuffite)
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Fragmental_Igneous_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#pyroclastic_material}

#####  pyroclastic material
- **Child of**:
 [`fragmental igneous material`](#fragmental_igneous_material)
 [`Volcanic Material`](#volcanic_material)
- Fragmental igneous material that consists of more than 75 percent of
particles formed by disruption as a direct result of volcanic action.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pyroclastic_Material
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#tephra}

######  Tephra
- **Child of**:
 [`Sediment`](#sediment)
 [`pyroclastic material`](#pyroclastic_material)
- Unconsolidated pyroclastic material in which greater than 75 percent
of the fragments are deposited as a direct result of volcanic
processes and the deposit has not been reworked by epiclastic
processes. Includes ash, lapilli tephra, bomb tephra, block tephra and
unconsolidated agglomerate.
- **Source:**
Hallsworth and Knox 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tephra
- **Other Properties:**

[]{#ash_and_lapilli}

#######  ash and lapilli
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which less than 25 percent of fragments are greater than
64 mm in longest dimension
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_And_Lapilli
- **Other Properties:**

[]{#ash_breccia_bomb_or_block_tephra}

#######  ash breccia bomb or block tephra
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which more than 25 percent of particles are greater than
64 mm in largest dimension. Includes ash breccia, bomb tephra and
block tephra of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Breccia_Bomb_Or_Block_Tephra
- **Other Properties:**

[]{#intermediate_composition_igneous_material}

####  intermediate composition igneous material
- **Child of**:
 [`Igneous material`](#igneous_material)
- Igneous material with between 52 and 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Intermediate_Composition_Igneous_Material
- **Other Properties:**

[]{#intermediate_composition_igneous_rock}

#####  intermediate composition igneous rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`intermediate composition igneous material`](#intermediate_composition_igneous_material)
- Igneous rock with between 52 and 63 percent SiO2.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Intermediate_Composition_Igneous_Rock
- **Other Properties:**

[]{#andesite}

######  andesite
- **Child of**:
 [`fine grained igneous rock`](#fine_grained_igneous_rock)
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
- Note the mela-andesite and leuco-basalt categories are not
recommended in this system. If chemical analytical data are available
to constrain the silica content, the basalt or andesite category
should be used.
- Fine-grained igneous rock with less than 20 percent quartz and less
than 10 percent feldspathoid minerals in the QAPF fraction, in which
the ratio of plagioclase to total feldspar is greater 0.65. Includes
rocks defined modally in QAPF fields 9 and 10 or chemically in TAS
field O2 as andesite. Basalt and andesite, which share the same QAPF
fields, are distinguished chemically based on silica content, with
basalt defined to contain less than 52 weight percent silica. If
chemical data are not available, the color index is used to
distinguish the categories, with basalt defined to contain greater
than 35 percent mafic minerals by volume or greater than 40 percent
mafic minerals by weight. Typically consists of plagioclase
(frequently zoned from labradorite to oligoclase), pyroxene,
hornblende and/or biotite. Fine grained equivalent of dioritic rock.
- **Source:**
after LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Andesite
- **Other Properties:**

[]{#boninite}

#######  boninite
- **Child of**:
 [`andesite`](#andesite)
 [`high magnesium fine grained igneous rock`](#high_magnesium_fine_grained_igneous_rock)
- andesitic rock that contains more than 8 percent MgO. Typically
consists of phenocrysts of protoenstatite, orthopyroxene,
clinopyroxene, and olivine in a glassy base full of crystallites, and
exhibits textures characterisitc of rapid crystal growth.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boninite
- **Other Properties:**

[]{#dioritoid}

######  dioritoid
- **Child of**:
 [`intermediate composition igneous rock`](#intermediate_composition_igneous_rock)
 [`phaneritic igneous rock`](#phaneritic_igneous_rock)
- Phaneritic crystalline igneous rock with M less than 90, consisting
of intermediate plagioclase, commonly with hornblende and often with
biotite or augite. Plagioclase to total feldspar ratio is greater that
0.65, and anorthite content of plagioclase is less than 50 percent.
Less than 10 percent feldspathoid mineral and less than 20 percent
quartz in the QAPF fraction. Includes rocks defined modally in QAPF
fields 9 and 10 (and their subdivisions).
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Dioritoid
- **Other Properties:**

[]{#dioritic_rock}

#######  dioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline rock with M less than 90, consisting of
intermediate plagioclase, commonly with hornblende and often with
biotite or augite. A dioritoid with a plagioclase to total feldspar
ratio (in the QAPF fraction) greater than 0.9. Includes rocks defined
modally in QAPF fields 10, 10' and 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dioritic_Rock
- **Other Properties:**

[]{#diorite}

########  diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Phaneritic crystalline rock consisting of intermediate plagioclase,
commonly with hornblende and often with biotite or augite; colour
index M less than 90, sodic plagioclase (An0-An50), no feldspathoid,
and between 0 and 5 percent quartz. Includes rocks defined modally in
QAPF field 10 as diorite.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Diorite
- **Other Properties:**

[]{#foid_bearing_diorite}

########  foid bearing diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 0 and 10 percent feldspathoid
minerals in the QAPF fraction. QAPF field 10'.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Diorite
- **Other Properties:**

[]{#quartz_diorite}

########  quartz diorite
- **Child of**:
 [`dioritic rock`](#dioritic_rock)
- Dioritic rock that contains between 5 to 20 percent quartz in the
QAPF fraction. QAPF field 10*.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Diorite
- **Other Properties:**

[]{#monzodioritic_rock}

#######  monzodioritic rock
- **Child of**:
 [`dioritoid`](#dioritoid)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 10 percent feldspathoid or 0 to 20 percent
quartz in the QAPF fraction. Plagioclase to total feldspar ratio in
the QAPF fraction is between 0.65 and 0.9. Includes rocks defined
modally in QAPF field 9, 9' and 9* as monzodiorite, foid-beaing
monzodiorite, and quartz monzodiorite.
- **Source:**
This vocabulary; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodioritic_Rock
- **Other Properties:**

[]{#foid_bearing_monzodiorite}

########  foid bearing monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 0 and 10 percent
feldspathoid mineral.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Foid_Bearing_Monzodiorite
- **Other Properties:**

[]{#monzodiorite}

########  monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Phaneritic crystalline igneous rock consisting of sodic plagioclase
(An0 to An50), alkali feldspar, hornblende and biotite, with or
without pyroxene, and 0 to 5 percent quartz. Includes rocks defined
modally in QAPF field 9.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Monzodiorite
- **Other Properties:**

[]{#quartz_monzodiorite}

########  quartz monzodiorite
- **Child of**:
 [`monzodioritic rock`](#monzodioritic_rock)
- Monzodioritic rock that contains between 5 and 20 percent quartz.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Quartz_Monzodiorite
- **Other Properties:**

[]{#volcanic_material}

####  Volcanic Material
- **Child of**:
 [`Igneous material`](#igneous_material)
- Material exhibiting features demonstrating an extrusive igneous
origin. Consolidated or non-consolidated
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Volcanic_Material
- **Other Properties:**

[]{#volcanic_rock}

#####  Volcanic rock
- **Child of**:
 [`Igneous rock`](#igneous_rock)
 [`Volcanic Material`](#volcanic_material)
- Rock that exhibits direct evidence of extrusive igneous processes in
its genesis.
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Volcanic_Rock
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#lava}

######  Lava
- **Child of**:
 [`Volcanic rock`](#volcanic_rock)
- Volcanic Rock with features indicating origin by extrusive lava
flow.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Lava
- **Other Properties:**

[]{#pyroclastic_material}

#####  pyroclastic material
- **Child of**:
 [`fragmental igneous material`](#fragmental_igneous_material)
 [`Volcanic Material`](#volcanic_material)
- Fragmental igneous material that consists of more than 75 percent of
particles formed by disruption as a direct result of volcanic action.
- **Source:**
LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pyroclastic_Material
- **Other Properties:**

[]{#pyroclastic_rock}

######  pyroclastic rock
- **Child of**:
 [`fragmental igneous rock`](#fragmental_igneous_rock)
 [`Volcanic rock`](#volcanic_rock)
 [`pyroclastic material`](#pyroclastic_material)
- Fragmental igneous rock that consists of greater than 75 percent
fragments produced as a direct result of eruption or extrusion of
magma from within the earth onto its surface. Includes autobreccia
associated with lava flows and excludes deposits reworked by
epiclastic processes.
- **Source:**
based on LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Pyroclastic_Rock
- **Other Properties:**

[]{#ash_tuff_lapillistone_and_lapilli_tuff}

#######  ash tuff lapillistone and lapilli tuff
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which less than 25 percent of rock by volume are
more than 64 mm in longest diameter. Includes tuff, lapilli tuff, and
lapillistone.
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Tuff_Lapillistone_And_Lapilli_Tuff
- **Other Properties:**

[]{#tuff_breccia_agglomerate_or_pyroclastic_breccia}

#######  tuff breccia agglomerate or pyroclastic breccia
- **Child of**:
 [`pyroclastic rock`](#pyroclastic_rock)
- Pyroclastic rock in which greater than 25 percent of particles are
greater than 64 mm in largest dimension. Includes agglomerate,
pyroclastic breccia of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Tuff_Breccia_Agglomerate_Or_Pyroclastic_Breccia
- **Other Properties:**

[]{#tephra}

######  Tephra
- **Child of**:
 [`Sediment`](#sediment)
 [`pyroclastic material`](#pyroclastic_material)
- Unconsolidated pyroclastic material in which greater than 75 percent
of the fragments are deposited as a direct result of volcanic
processes and the deposit has not been reworked by epiclastic
processes. Includes ash, lapilli tephra, bomb tephra, block tephra and
unconsolidated agglomerate.
- **Source:**
Hallsworth and Knox 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tephra
- **Other Properties:**

[]{#ash_and_lapilli}

#######  ash and lapilli
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which less than 25 percent of fragments are greater than
64 mm in longest dimension
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_And_Lapilli
- **Other Properties:**

[]{#ash_breccia_bomb_or_block_tephra}

#######  ash breccia bomb or block tephra
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which more than 25 percent of particles are greater than
64 mm in largest dimension. Includes ash breccia, bomb tephra and
block tephra of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Breccia_Bomb_Or_Block_Tephra
- **Other Properties:**

[]{#sedimentary_material}

###  Sedimentary material
- **Child of**:
 [`Rock or sediment`](#rockorsediment)
- Material formed by accumulation of solid fragmental material
deposited by air, water or ice, or material that accumulated by other
natural agents such as chemical precipitation from solution or
secretion by organisms. Includes both sediment and sedimentary rock.
Includes epiclastic deposits. All stated composition criteria are
based on the mineral/ compound material (GeoSciML term)/particulate
fraction of the material, irrespective of porosity or the pore-fluid.
No distinctions are made based on porosity or pore fluid composition
(except organic rich sediment in which liquid hydrocarbon content may
be considered).
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sedimentary_Material
- **Other Properties:**

[]{#chemical_sedimentary_material}

####  chemical sedimentary material
- **Child of**:
 [`Sediment`](#sediment)
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material that consists of at least 50 percent material
produced by inorganic chemical processes within the basin of
deposition. Includes inorganic siliceous, carbonate, evaporite, iron-
rich, and phosphatic sediment classes, as well as chemical sediments
associated with submarine hot springs ('black smokers'). Note that
these sediments might crystallize as a solid as they are deposited,
thus similar to rock....
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Chemical_Sedimentary_Material
- **Other Properties:**

[]{#evaporite}

#####  evaporite
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
- Nonclastic sedimentary rock composed of at least 50 percent non-
carbonate salts, including chloride, sulfate or borate minerals;
formed through precipitation of mineral salts from a saline solution
(non-carbonate salt rock).
- **Source:**
Jackson 1997; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Evaporite
- **Other Properties:**

[]{#exotic_evaporite}

######  exotic evaporite
- **Child of**:
 [`evaporite`](#evaporite)
- Category represents evaporite material that is not mostly
gypsum/anhydrite or halite. These are generally not very common, thus
the 'exotic' name
- Evaporite that is not 50 percent halite or 50 percent gypsum or
anhydrite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Exotic_Evaporite
- **Other Properties:**

[]{#rock_gypsum_or_anhydrite}

######  gypsum or anhydrite
- **Child of**:
 [`evaporite`](#evaporite)
- Evaporite composed of at least 50 percent gypsum or anhydrite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rock_Gypsum_Or_Anhydrite
- **Other Properties:**

[]{#rock_salt}

######  rock salt
- **Child of**:
 [`evaporite`](#evaporite)
- Evaporite composed of at least 50 percent halite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rock_Salt
- **Other Properties:**

[]{#iron_rich_sedimentary_material}

#####  iron rich sedimentary material
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
- Sedimentary material of unspecified consolidation state that
consists of at least 50 percent iron-bearing minerals (hematite,
magnetite, limonite-group, siderite, iron-sulfides), as determined by
hand-lens or petrographic analysis. Corresponds to a rock typically
containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Iron_Rich_Sedimentary_Material
- **Other Properties:**

[]{#iron_rich_sediment}

######  iron rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sediment that consists of at least 50 percent iron-bearing minerals
(hematite, magnetite, limonite-group, siderite, iron-sulfides), as
determined by hand-lens or petrographic analysis. Corresponds to a
rock typically containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sediment
- **Other Properties:**

[]{#iron_rich_sedimentary_rock}

######  iron rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sedimentary rock that consists of at least 50 percent iron-bearing
minerals (hematite, magnetite, limonite-group, siderite, iron-
sulfides), as determined by hand-lens or petrographic analysis.
Corresponds to a rock typically containing 15 percent iron by weight.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#sedimentary_massive_sulphide}

#####  Sedimentary Massive Sulphide
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`Massive sulphide`](#massive_sulphide)
- rock consisting of greater than 50% sulphide or sulfosalt minerals
formed by sedimentary exhalative processes.
- **Alternate labels:**
Sedimentary Massive Sulfide
- **Source:**
smr provisional 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sedimentary_Massive_Sulphide
- **Other Properties:**

[]{#travertine}

#####  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#sedimentary_rock}

####  Sedimentary rock
- **Child of**:
 [`Rock`](#rock)
 [`Sedimentary material`](#sedimentary_material)
- Rock formed by accumulation and cementation of solid fragmental
material deposited by air, water or ice, or as a result of other
natural agents, such as precipitation from solution, the accumulation
of organic material, or from biogenic processes, including secretion
by organisms. Includes epiclastic deposits.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Sedimentary_Rock
- **Other Properties:**

[]{#carbonate_sedimentary_rock}

#####  carbonate sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Particularly for fine-grained sedimentary rocks, distinction of
'intrabasinal' versus 'clastic' genesis can be very interpretive. In
practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored. Carbonate
rock subcatgories are defined on two orthogonal dimensions--mineralogy
(calcitic vs. dolomitic vs non-carbonate impurities), and texture. The
texture categories used here are those of Dunham (1962), and involve
grain size (matrix vs. grains/allochems), fabric (matrix vs. grain
supported), and genesis (bound, frame, or fragmental). The textural
approach used for carbonate rocks is conceptually incompatible with
that used for clastic sedimentary rocks, which is solely grain size or
mineralogy based. This leads to problems in the vocabulary for rocks
of mixed siliclastic/carbonate mineralogy (grainstone vs. sandstone,
carbonate mudstone vs. carbonate rich mudstone, how to accomodate
marlstone...).
- Sedimentary rock in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite, magnesite or dolomite.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#boundstone}

######  boundstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary carbonate rock with preserved biogenic texture, whose
original components were bound and encrusted together during
deposition by the action of plants and animals during deposition, and
remained substantially in the position of growth.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boundstone
- **Other Properties:**

[]{#calcareous_carbonate_sedimentary_rock}

######  calcareous carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
SLTTs 2004; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#carbonate_mudstone}

######  carbonate mudstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Not a subcategory of carbonate sedimentary rock because definition
does not specify 'carbonate minerals of intrabasinal origin', but is
agnostic on origin of carbonate. Schnurrenberger et al. 2003 point out
that it is very difficult (at least in lacustrine rocks) to
distinguish chemically precipitated or diagenetic carbonate from
primary biogenic carbonate. This distinction between biogenic,
detrital, and pedogenic or authigenic carbonate material is thus not a
good one to use in a general purpose classification system.
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Mudstone that consists of greater than 50 percent carbonate minerals
of any origin in the mud size fraction.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mudstone
- **Other Properties:**

[]{#carbonate_wackestone}

######  carbonate wackestone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate sedimentary rock with discernible mud supported
depositional texture and containing greater than 10 percent allochems,
and constituent particles are of intrabasinal origin. If particles are
not intrabasinal, categorization as a mudstone or wackestone should be
considered.
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Wackestone
- **Other Properties:**

[]{#crystalline_carbonate}

######  crystalline carbonate
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate rock of indeterminate mineralogy in which diagenetic
processes have obliterated any original depositional texture.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Crystalline_Carbonate
- **Other Properties:**

[]{#dolomitic_or_magnesian_sedimentary_rock}

######  dolomitic or magnesian sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sedimentary rock with a ratio of magnesium carbonate to
calcite (plus aragonite) greater than 1 to 1. Includes dolostone, lime
dolostone and magnesite-stone.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Or_Magnesian_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#framestone}

######  framestone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate reef rock consisting of a rigid framework of colonies,
shells or skeletons, with internal cavities filled with fine sediment;
usually created through the activities of colonial organisms.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004, Table 15-3-1
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Framestone
- **Other Properties:**

[]{#grainstone}

######  grainstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate sedimentary rock with recognizable depositional fabric
that is grain-supported, and constituent particles are of intrabasinal
origin; contains little or no mud matrix. Distinction from sandstone
is based on interpretation of intrabasinal origin of clasts and grain-
supported fabric, but grainstone definition does not include a grain
size criteria.
- **Alternate labels:**
carbonate grainstone
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Grainstone
- **Other Properties:**

[]{#impure_carbonate_sedimentary_rock}

######  impure carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary rock in which between 50 and 90 percent of the primary
and/or recrystallized constituents are composed of carbonate minerals.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#packstone}

######  packstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Note that this category overlaps with 'carbonate mudstone'.
- Carbonate sedimentary rock with discernible grain supported
depositional texture, containing greater than 10 percent grains, and
constituent particles are of intrabasinal origin; intergranular spaces
are filled by matrix.
- **Source:**
Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Packstone
- **Other Properties:**

[]{#pure_carbonate_sedimentary_rock}

######  pure carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary rock in which greater than 90 percent of the primary
and/or recrystallized constituents are carbonate minerals.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#pure_carbonate_mudstone}

#######  pure carbonate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Mudstone that consists of greater than 90 percent carbonate minerals
of intrabasinal orign in the mud fraction, and contains less than 10
percent allochems. The original depositional texture is preserved and
fabric is matrix supported. Carbonate mudstone of Dunham (1962)
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Mudstone
- **Other Properties:**

[]{#clastic_sedimentary_rock}

#####  clastic sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`clastic sedimentary material`](#clastic_sedimentary_material)
- The conglomerate, sandstone, mudstone, and wackestone categories are
not defined as kinds of clastic sedimentary rocks because rocks
meeting their purely grainsize based definitions might also be iron-
rich, phosphatic, or carbonate. This is based on GeoSciML allowance to
assign rocks to more than one lithology category. For example to
categorize a rock as a clastic conglomerate requires assignment ot the
'clastic sedimentary rock' category and to the 'conglomerate'
category. Particularly for fine-grained sedimentary rocks, distinction
of 'intrabasinal' versus 'clastic' genesis can be very interpretive.
In practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored.
- Sedimentary rock in which at least 50 percent of the constituent
particles were derived from erosion, weathering, or mass-wasting of
pre-existing earth materials, and transported to the place of
deposition by mechanical agents such as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Clastic_Sedimentary_Rock
- **Other Properties:**

[]{#diamictite}

######  diamictite
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
- Unsorted or poorly sorted, clastic sedimentary rock with a wide
range of particle sizes including a muddy matrix. Biogenic materials
that have such texture are excluded. Distinguished from conglomerate,
sandstone, mudstone based on polymodality and lack of structures
related to transport and deposition of sediment by moving air or
water. If more than 10 percent of the fine grained matrix is of
indeterminant clastic or diagenetic origin and the fabric is matrix
supported, may also be categorized as wacke.
- **Source:**
Fairbridge and Bourgeois 1978
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Diamictite
- **Other Properties:**

[]{#clastic_conglomerate}

######  conglomerate
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic conglomerate`](#generic_conglomerate)
- Note this category is equivalent to category labeled 'Conglomeratic
rock in SLTTs (2004), not to the category labeled 'Conglomerate' in
that system.
- Clastic sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Alternate labels:**
conglomeratic rock
- **Source:**
Neuendorf et al. 2005; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Conglomerate
- **Other Properties:**

[]{#clastic_mudstone}

######  mudstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is interpretive in many cases. If
there is uncertainty on the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system, it is recommended to
use the generic_mudstone category. This category is the union of the
various fields labeled 'mudstone' with various qualifiers in Folk,
1954, Figure 1a, although Folk's (1954) category labeled 'mudstone' is
a much more restricted category. The CGI category is equivalent to
category labeled 'Mudrock' in SLTTs (2004), not to the category
labeled 'Mudstone' adopted by that system from Folk (1954).
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Clastic sedimentary rock consisting of less than 30 percent gravel-
size (2 mm) particles and with a mud to sand ratio greater than 1.
- **Alternate labels:**
clastic mudstone, 
mudrock, 
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Mudstone
- **Other Properties:**

[]{#claystone}

#######  claystone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Mudstone that contains no detectable silt, inferred to consist
virtually entirely of clay-size particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Claystone
- **Other Properties:**

[]{#shale}

#######  shale
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Note definition does not specify carbonate vs. siliclastic nature of
mud.
- Laminated mudstone that will part or break along thin, closely
spaced layers parallel to stratification.
- **Source:**
NADM SLTT sedimentary, 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Shale
- **Other Properties:**

[]{#siltstone}

#######  siltstone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Use of 'detectable silt' in the criteria for this category is based
on the observation that in practice, distinction of claystone from
'siltstone' is typically based on a qualitative assessment of
'grittiness' (e.g. rubbing with fingers, or chewing); the property
that these tests can determine is the presence or absence of silty
particles in the material. Quantitative grain size analysis in the the
clay/silt fraction of a lithified sediment is difficult at best, and
of questionable significance because diagensis has altered the size
and mineralogy of original sedimentary particles.
- Mudstone that contains detectable silt. (see comments)
- **Alternate labels:**
Silt bearing mudstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siltstone
- **Other Properties:**

[]{#clastic_sandstone}

######  sandstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`Generic sandstone`](#generic_sandstone)
- Note this category is equivalent to cagetory labeled 'sandy rock' in
SLTTs (2004), not to the much more restricted category labeled
'Sandstone' in that system.
- Clastic sedimentary rock in which less than 30 percent of particles
are greater than 2 mm in diameter (gravel) and the sand to mud ratio
is at least 1.
- **Alternate labels:**
clastic sandstone, 
sandy rock, 
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Sandstone
- **Other Properties:**

[]{#arenite}

#######  arenit
* `arenite`
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Clastic sandstone that contains less than 10 percent matrix. Matrix
is mud-size silicate minerals (clay, feldspar, quartz, rock fragments,
and alteration products) of detrital or diagenetic nature.
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Arenite
- **Other Properties:**

[]{#wacke}

#######  wacke
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Distinction from mudstone is based on inference that less that 50
percent of the mud size fraction (matrix) is original mud size
detrital particles. May also grade into diamictite or conglomerate
based on size distribution of discernible particles. If more than 50
percent of rock is detrital particles of intrabasinal orgin and
carbonate composition, categorize as carbonate wackestone. Term is
typically applied to diagenetically altered volcanic-lithic clastic
rocks in which the definition of the original clasts has been
obscured. Suggested boundaries between wacke and arenite range from 5
to 15 percent matrix. See Dickinson (1970) for discussion of
interpretation of undiscernible matrix in diagenetically altered
lithic clastic rocks. Dickinson, W.R., 1970, Interpreting detrital
modes of graywacke and arkose: Journal of Sedimentary Petrology, v.
40, p. 695-707.
- Clastic sandstone with more than 10 percent matrix of indeterminate
detrital or diagenetic nature. Matrix is mud size silicate minerals
(clay, feldspar, quartz, rock fragments, and alteration products).
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Wacke
- **Other Properties:**

[]{#generic_conglomerate}

#####  generic conglomerate
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Source:**
Neuendorf et al. 2005; SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Generic_Conglomerate
- **Other Properties:**

[]{#clastic_conglomerate}

######  conglomerate
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic conglomerate`](#generic_conglomerate)
- Note this category is equivalent to category labeled 'Conglomeratic
rock in SLTTs (2004), not to the category labeled 'Conglomerate' in
that system.
- Clastic sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Alternate labels:**
conglomeratic rock
- **Source:**
Neuendorf et al. 2005; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Conglomerate
- **Other Properties:**

[]{#generic_mudstone}

#####  generic mudstone
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is so interpretive that it is proposed
to not define the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system. Schnurrenberger, D.,
Russell, J. and Kelts, K., 2003, Classification of lacustrine
sediments based on sedimentary components: Journal of Paleolimnology,
v.29, p141-154.
- Sedimentary rock consisting of less than 30 percent gravel-size (2
mm) particles and with a mud to sand ratio greater than 1. Clasts may
be of any composition or origin.
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999; extrapolated from Folk, 1954, Figure 1a; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Generic_Mudstone
- **Other Properties:**

[]{#carbonate_mudstone}

######  carbonate mudstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Not a subcategory of carbonate sedimentary rock because definition
does not specify 'carbonate minerals of intrabasinal origin', but is
agnostic on origin of carbonate. Schnurrenberger et al. 2003 point out
that it is very difficult (at least in lacustrine rocks) to
distinguish chemically precipitated or diagenetic carbonate from
primary biogenic carbonate. This distinction between biogenic,
detrital, and pedogenic or authigenic carbonate material is thus not a
good one to use in a general purpose classification system.
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Mudstone that consists of greater than 50 percent carbonate minerals
of any origin in the mud size fraction.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mudstone
- **Other Properties:**

[]{#carbonate_rich_mudstone}

######  carbonate rich mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
- Carbonate-rich mudstone' definition limits carbonate to mud-size
fraction to avoid overlap with 'impure carbonate sedimentary rock'. If
carbonate minerals are in sand or gravel size fractions, use 'impure
carbonate sedimentary rock'. The operational test typically used to
identify this category is if the rock fizzes when hydrochloric acid is
applied. The '10 percent carbonate' criteria is a fuzzy boundary.
- Mudstone that contains between 10 and 50 percent carbonate minerals
in the mud size fraction. Carbonate origin is not specified.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Rich_Mudstone
- **Other Properties:**

[]{#clastic_mudstone}

######  mudstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is interpretive in many cases. If
there is uncertainty on the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system, it is recommended to
use the generic_mudstone category. This category is the union of the
various fields labeled 'mudstone' with various qualifiers in Folk,
1954, Figure 1a, although Folk's (1954) category labeled 'mudstone' is
a much more restricted category. The CGI category is equivalent to
category labeled 'Mudrock' in SLTTs (2004), not to the category
labeled 'Mudstone' adopted by that system from Folk (1954).
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Clastic sedimentary rock consisting of less than 30 percent gravel-
size (2 mm) particles and with a mud to sand ratio greater than 1.
- **Alternate labels:**
clastic mudstone, 
mudrock, 
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Mudstone
- **Other Properties:**

[]{#claystone}

#######  claystone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Mudstone that contains no detectable silt, inferred to consist
virtually entirely of clay-size particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Claystone
- **Other Properties:**

[]{#shale}

#######  shale
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Note definition does not specify carbonate vs. siliclastic nature of
mud.
- Laminated mudstone that will part or break along thin, closely
spaced layers parallel to stratification.
- **Source:**
NADM SLTT sedimentary, 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Shale
- **Other Properties:**

[]{#siltstone}

#######  siltstone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Use of 'detectable silt' in the criteria for this category is based
on the observation that in practice, distinction of claystone from
'siltstone' is typically based on a qualitative assessment of
'grittiness' (e.g. rubbing with fingers, or chewing); the property
that these tests can determine is the presence or absence of silty
particles in the material. Quantitative grain size analysis in the the
clay/silt fraction of a lithified sediment is difficult at best, and
of questionable significance because diagensis has altered the size
and mineralogy of original sedimentary particles.
- Mudstone that contains detectable silt. (see comments)
- **Alternate labels:**
Silt bearing mudstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siltstone
- **Other Properties:**

[]{#organic_bearing_mudstone}

######  organic bearing mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
- Mudstone that contains a significant amount of organic carbon,
typically kerogen. commonly finely laminated, brown or black in color.
- **Alternate labels:**
oil shale
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Oil_shale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Organic_Bearing_Mudstone
- **Other Properties:**

[]{#pure_carbonate_mudstone}

######  pure carbonate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Mudstone that consists of greater than 90 percent carbonate minerals
of intrabasinal orign in the mud fraction, and contains less than 10
percent allochems. The original depositional texture is preserved and
fabric is matrix supported. Carbonate mudstone of Dunham (1962)
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Mudstone
- **Other Properties:**

[]{#silicate_mudstone}

######  silicate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
- Operational distinction of this category will typically be based on
whether or not the rock fizzes when hydrochloric acid is applied--the
rock is silicate mudstone if it does not fizz. The quantitative '10
percent' criteria is fuzzy.
- Mudstone that contains less than 10 percent carbonate minerals.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silicate_Mudstone
- **Other Properties:**

[]{#generic_sandstone}

#####  Generic sandstone
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Sedimentary rock in which less than 30 percent of particles are
greater than 2 mm in diameter (gravel) and the sand to mud ratio is at
least 1.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Generic_Sandstone
- **Other Properties:**

[]{#clastic_sandstone}

######  sandstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`Generic sandstone`](#generic_sandstone)
- Note this category is equivalent to cagetory labeled 'sandy rock' in
SLTTs (2004), not to the much more restricted category labeled
'Sandstone' in that system.
- Clastic sedimentary rock in which less than 30 percent of particles
are greater than 2 mm in diameter (gravel) and the sand to mud ratio
is at least 1.
- **Alternate labels:**
clastic sandstone, 
sandy rock, 
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Sandstone
- **Other Properties:**

[]{#arenite}

#######  arenit
* `arenite`
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Clastic sandstone that contains less than 10 percent matrix. Matrix
is mud-size silicate minerals (clay, feldspar, quartz, rock fragments,
and alteration products) of detrital or diagenetic nature.
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Arenite
- **Other Properties:**

[]{#wacke}

#######  wacke
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Distinction from mudstone is based on inference that less that 50
percent of the mud size fraction (matrix) is original mud size
detrital particles. May also grade into diamictite or conglomerate
based on size distribution of discernible particles. If more than 50
percent of rock is detrital particles of intrabasinal orgin and
carbonate composition, categorize as carbonate wackestone. Term is
typically applied to diagenetically altered volcanic-lithic clastic
rocks in which the definition of the original clasts has been
obscured. Suggested boundaries between wacke and arenite range from 5
to 15 percent matrix. See Dickinson (1970) for discussion of
interpretation of undiscernible matrix in diagenetically altered
lithic clastic rocks. Dickinson, W.R., 1970, Interpreting detrital
modes of graywacke and arkose: Journal of Sedimentary Petrology, v.
40, p. 695-707.
- Clastic sandstone with more than 10 percent matrix of indeterminate
detrital or diagenetic nature. Matrix is mud size silicate minerals
(clay, feldspar, quartz, rock fragments, and alteration products).
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Wacke
- **Other Properties:**

[]{#hybrid_sedimentary_rock}

#####  hybrid sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
- Sedimentary rock that does not fit any of the other
composition/genesis categories. Sedimentary rock consisting of three
or more components which form more than 5 percent but less than 50
precent of the material.
- **Source:**
Hallsworth and Knox, 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hybrid_Sedimentary_Rock
- **Other Properties:**

[]{#iron_rich_sedimentary_rock}

#####  iron rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sedimentary rock that consists of at least 50 percent iron-bearing
minerals (hematite, magnetite, limonite-group, siderite, iron-
sulfides), as determined by hand-lens or petrographic analysis.
Corresponds to a rock typically containing 15 percent iron by weight.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#non_clastic_siliceous_sedimentary_rock}

#####  non clastic siliceous sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`non clastic siliceous sedimentary material`](#non_clastic_siliceous_sedimentary_material)
- Definition updated to include chert, flint SMR 2020-09-21
- Sedimentary rock that consists of at least 50 percent silicate
mineral material, deposited directly by chemical or biological
processes at the depositional surface, in particles formed by chemical
or biological processes within the basin of deposition, or formed by
diagenetic processes. Includes chert and flint found in carbonate
rocks.
- **Source:**
modified from SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Non_Clastic_Siliceous_Sedimentary_Rock
- **Other Properties:**

[]{#biogenic_silica_sedimentary_rock}

######  biogenic silica sedimentary rock
- **Child of**:
 [`non clastic siliceous sedimentary rock`](#non_clastic_siliceous_sedimentary_rock)
- Sedimentary rock that consists of at least 50 percent silicate
mineral material, deposited directly by biological processes at the
depositional surface, or in particles formed by biological processes
within the basin of deposition. Includes radiolarian chert, diatomite,
novaculite.
- **Source:**
based on NADM SLTT sedimentary; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Biogenic_Silica_Sedimentary_Rock
- **Other Properties:**

[]{#organic_rich_sedimentary_rock}

#####  organic rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`organic rich sedimentary material`](#organic_rich_sedimentary_material)
- Sapropelic coal, and asphaltite are not differentiated in This
vocabulary
- Sedimentary rock with color, composition, texture and apparent
density indicating greater than 50 percent organic content by weight
on a moisture-free basis.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Organic_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#coal}

######  coal
* `kohle`
- **Child of**:
 [`organic rich sedimentary rock`](#organic_rich_sedimentary_rock)
- A consolidated organic sedimentary material having less than 75%
moisture. This category includes low, medium, and high rank coals
according to International Classification of In-Seam Coal (United
Nations, 1998), thus including lignite. Sapropelic coal is not
distinguished in this category from humic coals. Formed from the
compaction or induration of variously altered plant remains similar to
those of peaty deposits.
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp.
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Coal
- **Other Properties:**

[]{#anthracite_coal}

#######  anthracite
* `anthrazit`
- **Child of**:
 [`coal`](#coal)
- Coal that has vitrinite mean random reflectance greater than 2.0%
(determined in conformance with ISO 7404-5). Less than 12-14 percent
volatiles (dry, ash free), greater than 91 percent fixed carbon (dry,
ash free basis). The highest rank coal; very hard, glossy, black, with
semimetallic luster, semi conchoidal fracture.
- **Alternate labels:**
High rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp; see also Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Coal#Types_of_coal; Eberhard Lindner; Chemie für Ingenieure; Lindner Verlag Karlsruhe, S. 258
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anthracite_Coal
- **Other Properties:**

[]{#bituminous_coal}

#######  bituminous coal
- **Child of**:
 [`coal`](#coal)
- Coal that has vitrinite mean random reflectance greater than 0.6%
and less than 2.0% (determined in conformance with ISO 7404-5), or has
a gross calorific value greater than 24 MJ/kg (determined in
conformance with ISO 1928). Hard, black, organic rich sedimentary
rock; contains less than 91 percent fixed carbon on a dry, mineral-
matter-free basis, and greater than 13-14 percent volatiles (dry, ash
free). Formed from the compaction or induration of variously altered
plant remains similar to those of peaty deposits.
- **Alternate labels:**
medium rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp; see also http://en.wikipedia.org/wiki/Coal#Types_of_coal; Eberhard Lindner; Chemie für Ingenieure; Lindner Verlag Karlsruhe, S. 258
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Bituminous_Coal
- **Other Properties:**

[]{#lignite}

#######  lignite
- **Child of**:
 [`coal`](#coal)
- Coal that has a gross calorific value less than 24 MJ/kg (determined
in conformance with ISO 1928), and vitrinite mean random reflectance
less than 0.6% (determined in conformance with ISO 7404-5). Gross
calorific value is recalculated to a moist, ash free basis using bed
moisture (determined according to ISO 1015 or ISO 5068). Includes all
low-rank coals, including sub-bitiminous coal. A consolidated, dull,
soft brown to black coal having many readily discernible plant
fragments set in a finer grained organic matrix. Tends to crack and
fall apart on drying. Operationally sub-bituminous and bitiminous coal
are qualitatively distinguished based on brown streak for sub-
bitiminous coal and black streak for bituminous coal.
- **Alternate labels:**
low rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Lignite
- **Other Properties:**

[]{#phosphorite}

#####  phosphorite
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`phosphate rich sedimentary material`](#phosphate_rich_sedimentary_material)
- Sedimentary rock in which at least 50 percent of the primary or
recrystallized constituents are phosphate minerals. Most commonly
occurs as a bedded primary or reworked secondary marine rock, composed
of microcrystalline carbonate fluorapatite in the form of lamina,
pellets, oolites and nodules, and skeletal, shell and bone fragments.
- **Source:**
HallsworthandKnox 1999, Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phosphorite
- **Other Properties:**

[]{#sediment}

####  Sediment
- **Child of**:
 [`Natural unconsolidated material`](#natural_unconsolidated_material)
 [`Sedimentary material`](#sedimentary_material)
- Solid granular material transported by wind, water, or gravity, not
modified by interaction with biosphere or atmosphere (to differentiate
from soil). Particles derived by erosion of pre-existing rock, from
shell or other body parts from organisms, precipitated chemically in
the surficial environment, or generated by explosive volcanic
activity.
(http://resource.geosciml.org/classifier/cgi/lithology/sediment).
Sediment is not consolidated, i.e. Particulate constituents of a
compound material do not adhere to each other strongly enough that the
aggregate can be considered a solid material in its own right. Similar
to http://purl.obolibrary.org/obo/ENVO_00002007
- Unconsolidated material consisting of an aggregation of particles
transported or deposited by air, water or ice, or that accumulated by
other natural agents, such as chemical precipitation, and that forms
in layers on the Earth's surface. Includes epiclastic deposits.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/vocabulary/material/1.0/sediment
- **Other Properties:**

[]{#biogenic_sediment}

#####  biogenic sediment
- **Child of**:
 [`Sediment`](#sediment)
- Corresponding biogenic sedimentary material and biogenic sedimentary
rock categories are not included based on the interpretation that
biogenic sedimentary rock will be in a different category, e.g.
carbonate sedimentary rock or organic rich sedimentary rock.
- Sediment composed of greater than 50 percent material of biogenic
origin. Because the biogenic material may be skeletal remains that are
not organic, all biogenic sediment is not necessarily organic-rich.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Biogenic_Sediment
- **Other Properties:**

[]{#ooze}

######  ooze
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Neuendorf et al. 2005 put cutoff at 30 percent skeletal remains;
this is raised to 50 percent in This vocabulary for consistency with
definition of other Biogenic sediment category
- Biogenic sediment consisting of less than 1 percent gravel-size
(greater than or equal to 2 mm) particles, with a sand to mud ratio
less than 1 to 9, and less than 50 percent carbonate minerals.
- **Alternate labels:**
biogenic mud
- **Source:**
based on Bates and Jackson 1987 and Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ooze
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#siliceous_ooze}

#######  siliceous ooze
- **Child of**:
 [`ooze`](#ooze)
 [`silicate mud`](#silicate_mud)
- Ooze that consists of more than 50 percent siliceous skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siliceous_Ooze
- **Other Properties:**

[]{#organic_rich_sediment}

######  organic rich sediment
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`organic rich sedimentary material`](#organic_rich_sedimentary_material)
- The broader relation from organic rich sediment to biogenic sediment
is based on the inference that organic rich material is always
biogenic in origin. Biogenic is a broader category because not all
biogenic materials are organic rich, for example shells or phosphatic
bone.
- Sediment with color, composition, texture and apparent density
indicating greater than 50 percent organic content by weight on a
moisture-free basis.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Organic_Rich_Sediment
- **Other Properties:**

[]{#peat}

#######  peat
- **Child of**:
 [`organic rich sediment`](#organic_rich_sediment)
- Unconsolidated organic-rich sediment composed of at least 50 percent
semi-carbonised plant remains; individual remains commonly seen with
unaided eye; yellowish brown to brownish black; generally fibrous
texture; can be plastic or friable. In its natural state it can be
readily cut and has a very high moisture content, generally greater
than 90 percent. Liptinite to Inertinite ratio is less than one
(Economic commission for Europe, committee on Sustainable Energy-
United Nations (ECE-UN), 1998, International Classification of in-Seam
Coals: Energy 19, 41 pp.)
- **Source:**
Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Peat
- **Other Properties:**

[]{#sapropel}

#######  sapropel
- **Child of**:
 [`organic rich sediment`](#organic_rich_sediment)
- Jelly like organic rich sediment composed of plant remains, usually
algal. Liptinite to Inertinite ratio is greater than one (Economic
commission for Europe, committee on Sustainable Energy- United Nations
(ECE-UN), 1998, International Classification of in-Seam Coals: Energy
19, 41 pp.)
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sapropel
- **Other Properties:**

[]{#carbonate_sediment}

#####  carbonate sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite and dolomite, in particles of
intrabasinal origin.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Carbonate_Sediment
- **Other Properties:**

[]{#calcareous_carbonate_sediment}

######  calcareous carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sediment with a calcite (plus aragonite) to dolomite ratio
greater than 1 to 1. Includes lime-sediments.
- **Source:**
after Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#carbonate_mud}

######  carbonate mud
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Carbonate sediment composed of less than 25 percent clasts that have
a maximum diameter more than 2 mm, and the ratio of sand size to mud
size clasts is less than one.
- **Alternate labels:**
marl
- **Source:**
follow pattern used for clastic sand and mud categories, based on SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mud
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#dolomitic_sediment}

######  dolomitic sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sediment with a ratio of magnesium carbonate to calcite
(plus aragonite) greater than 1 to 1.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#impure_carbonate_sediment}

######  impure carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin.
- **Alternate labels:**
marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_carbonate_sediment}

######  pure carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#chemical_sedimentary_material}

#####  chemical sedimentary material
- **Child of**:
 [`Sediment`](#sediment)
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material that consists of at least 50 percent material
produced by inorganic chemical processes within the basin of
deposition. Includes inorganic siliceous, carbonate, evaporite, iron-
rich, and phosphatic sediment classes, as well as chemical sediments
associated with submarine hot springs ('black smokers'). Note that
these sediments might crystallize as a solid as they are deposited,
thus similar to rock....
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Chemical_Sedimentary_Material
- **Other Properties:**

[]{#evaporite}

######  evaporite
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
- Nonclastic sedimentary rock composed of at least 50 percent non-
carbonate salts, including chloride, sulfate or borate minerals;
formed through precipitation of mineral salts from a saline solution
(non-carbonate salt rock).
- **Source:**
Jackson 1997; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Evaporite
- **Other Properties:**

[]{#exotic_evaporite}

#######  exotic evaporite
- **Child of**:
 [`evaporite`](#evaporite)
- Category represents evaporite material that is not mostly
gypsum/anhydrite or halite. These are generally not very common, thus
the 'exotic' name
- Evaporite that is not 50 percent halite or 50 percent gypsum or
anhydrite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Exotic_Evaporite
- **Other Properties:**

[]{#rock_gypsum_or_anhydrite}

#######  gypsum or anhydrite
- **Child of**:
 [`evaporite`](#evaporite)
- Evaporite composed of at least 50 percent gypsum or anhydrite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rock_Gypsum_Or_Anhydrite
- **Other Properties:**

[]{#rock_salt}

#######  rock salt
- **Child of**:
 [`evaporite`](#evaporite)
- Evaporite composed of at least 50 percent halite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rock_Salt
- **Other Properties:**

[]{#iron_rich_sedimentary_material}

######  iron rich sedimentary material
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
- Sedimentary material of unspecified consolidation state that
consists of at least 50 percent iron-bearing minerals (hematite,
magnetite, limonite-group, siderite, iron-sulfides), as determined by
hand-lens or petrographic analysis. Corresponds to a rock typically
containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Iron_Rich_Sedimentary_Material
- **Other Properties:**

[]{#iron_rich_sediment}

#######  iron rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sediment that consists of at least 50 percent iron-bearing minerals
(hematite, magnetite, limonite-group, siderite, iron-sulfides), as
determined by hand-lens or petrographic analysis. Corresponds to a
rock typically containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sediment
- **Other Properties:**

[]{#iron_rich_sedimentary_rock}

#######  iron rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sedimentary rock that consists of at least 50 percent iron-bearing
minerals (hematite, magnetite, limonite-group, siderite, iron-
sulfides), as determined by hand-lens or petrographic analysis.
Corresponds to a rock typically containing 15 percent iron by weight.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#sedimentary_massive_sulphide}

######  Sedimentary Massive Sulphide
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`Massive sulphide`](#massive_sulphide)
- rock consisting of greater than 50% sulphide or sulfosalt minerals
formed by sedimentary exhalative processes.
- **Alternate labels:**
Sedimentary Massive Sulfide
- **Source:**
smr provisional 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sedimentary_Massive_Sulphide
- **Other Properties:**

[]{#travertine}

######  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#clastic_sediment}

#####  clastic sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`clastic sedimentary material`](#clastic_sedimentary_material)
- Choice of 'clastic' is purposful. Other suggested labels for this
category include siliciclastic and terrigineous clastic. Siliciclastic
is considered too limiting because the category includes rocks that
consists clasts of carbonate minerals, e.g. epiclastic detritus eroded
from carbonate rock. Terrigineous clastic was considered and rejected
first because it is considered redundant, anything that is
terrigineous is clastic. Second, it is questionable if clastic
sediment derived by submarine processes (fragementation by gravity
sliding, faulting, or volcanic activity, with transport by sediment
gravity flow or submarine currents) is terrigineous, but it is clastic
and is meant to be included in this category.
- Sediment in which at least 50 percent of the constituent particles
were derived from erosion, weathering, or mass-wasting of pre-existing
earth materials, and transported to the place of deposition by
mechanical agents such as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Clastic_Sediment
- **Other Properties:**

[]{#diamicton}

######  diamicton
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
- definition amplified to help distinguish diamicton, conglomerate and
wackestone in this version
- Unsorted or poorly sorted, clastic sediment with a wide range of
particle sizes, including a muddy matrix. Biogenic materials that have
such texture are excluded. Distinguished from conglomerate, sandstone,
mudstone based on polymodality and lack of structures related to
transport and deposition of sediment by moving air or water.
Assignment to an other size class can be used in conjunction to
indicate the dominant grain size.
- **Source:**
Fairbridge and Bourgeois 1978
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Diamicton
- **Other Properties:**

[]{#gravel}

######  gravel
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`gravel size sediment`](#gravel_size_sediment)
- Clastic sediment containing greater than 30 percent gravel-size
particles (greater than 2.0 mm diameter). Gravel in which more than
half of the particles are of epiclastic origin
- **Source:**
definition of gravel from SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gravel
- **Other Properties:**

[]{#mud}

######  mud
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Clastic sediment consisting of less than 30 percent gravel-size (2
mm) particles and with a mud-size to sand-size particle ratio greater
than 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of mud from SLTTs 2004 muddy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mud
- **Other Properties:**

[]{#clay}

#######  clay
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent particles with grain
size less than 0.004 mm
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clay
- **Other Properties:**

[]{#silt}

#######  silt
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent silt-size grains.
- **Alternate labels:**
loess
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silt
- **Other Properties:**

[]{#sand}

######  sand
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`sand size sediment`](#sand_size_sediment)
- Clastic sediment in which less than 30 percent of particles are
gravel (greater than 2 mm in diameter) and the sand to mud ratio is at
least 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of sand from SLTTs 2004 sandy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sand
- **Other Properties:**

[]{#gravel_size_sediment}

#####  gravel size sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment containing greater than 30 percent gravel-size particles
(greater than 2.0 mm diameter). Composition or gensis of clasts not
specified.
- **Source:**
SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gravel_Size_Sediment
- **Other Properties:**

[]{#boulder_gravel_size_sediment}

######  boulder gravel size sediment
- **Child of**:
 [`gravel size sediment`](#gravel_size_sediment)
- Sediment containing greater than 30 percent boulder-size particles
(greater than 256 mm in diameter)
- **Source:**
Wentworth size scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boulder_Gravel_Size_Sediment
- **Other Properties:**

[]{#cobble_gravel_size_sediment}

######  cobble gravel size sediment
- **Child of**:
 [`gravel size sediment`](#gravel_size_sediment)
- Sediment containing greater than 30 percent cobble-size particles
(64-256 mm in diameter)
- **Source:**
Wentworth size scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Cobble_Gravel_Size_Sediment
- **Other Properties:**

[]{#gravel}

######  gravel
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`gravel size sediment`](#gravel_size_sediment)
- Clastic sediment containing greater than 30 percent gravel-size
particles (greater than 2.0 mm diameter). Gravel in which more than
half of the particles are of epiclastic origin
- **Source:**
definition of gravel from SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gravel
- **Other Properties:**

[]{#pebble_gravel_size_sediment}

######  pebble gravel size sediment
- **Child of**:
 [`gravel size sediment`](#gravel_size_sediment)
- Sediment containing greater than 30 percent pebble-size particles
(2.0 -64 mm in diameter)
- **Source:**
Wentworth size scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pebble_Gravel_Size_Sediment
- **Other Properties:**

[]{#hybrid_sediment}

#####  Hybrid sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment that does not fit any of the other sediment
composition/genesis categories. Sediment consisting of three or more
components which form more than 5 percent but less than 50 precent of
the material.
- **Source:**
Hallsworth and Knox, 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hybrid_Sediment
- **Other Properties:**

[]{#iron_rich_sediment}

#####  iron rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sediment that consists of at least 50 percent iron-bearing minerals
(hematite, magnetite, limonite-group, siderite, iron-sulfides), as
determined by hand-lens or petrographic analysis. Corresponds to a
rock typically containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sediment
- **Other Properties:**

[]{#mud_size_sediment}

#####  mud size sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment consisting of less than 30 percent gravel-size (2 mm)
particles and with a mud-size to sand-size particle ratio greater than
1. Clasts may be of any composition or origin.  BGS  (Hallsworth and
Knox, 1999, p. 9) define the  'upper size limit of mud ... at 32
micrometers (.032 mm)', but Wentworth scale and Krumbein scale put
boundary at .064 or .062 mm (inidistinguishable difference in
rocks...) BGS 'mud-grade sediment' or sedimentary rock definition is
'over 75% of the clasts smaller than  .032 mm', which is narrower than
the definition here.
- Sediment consisting of less than 30 percent gravel-size (2 mm)
particles and with a mud-size to sand-size particle ratio greater than
1. Clasts may be of any composition or origin.
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mud_Size_Sediment
- **Other Properties:**

[]{#carbonate_mud}

######  carbonate mud
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Carbonate sediment composed of less than 25 percent clasts that have
a maximum diameter more than 2 mm, and the ratio of sand size to mud
size clasts is less than one.
- **Alternate labels:**
marl
- **Source:**
follow pattern used for clastic sand and mud categories, based on SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mud
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#carbonate_rich_mud}

######  carbonate rich mud
- **Child of**:
 [`mud size sediment`](#mud_size_sediment)
- Mud size sediment that contains between 10 and 50 percent carbonate
minerals in any size fraction. Carbonate origin is not specified.
- **Alternate labels:**
carbonate rich loess, 
marl, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Rich_Mud
- **Other Properties:**

[]{#mud}

######  mud
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Clastic sediment consisting of less than 30 percent gravel-size (2
mm) particles and with a mud-size to sand-size particle ratio greater
than 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of mud from SLTTs 2004 muddy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mud
- **Other Properties:**

[]{#clay}

#######  clay
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent particles with grain
size less than 0.004 mm
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clay
- **Other Properties:**

[]{#silt}

#######  silt
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent silt-size grains.
- **Alternate labels:**
loess
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silt
- **Other Properties:**

[]{#ooze}

######  ooze
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Neuendorf et al. 2005 put cutoff at 30 percent skeletal remains;
this is raised to 50 percent in This vocabulary for consistency with
definition of other Biogenic sediment category
- Biogenic sediment consisting of less than 1 percent gravel-size
(greater than or equal to 2 mm) particles, with a sand to mud ratio
less than 1 to 9, and less than 50 percent carbonate minerals.
- **Alternate labels:**
biogenic mud
- **Source:**
based on Bates and Jackson 1987 and Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ooze
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#siliceous_ooze}

#######  siliceous ooze
- **Child of**:
 [`ooze`](#ooze)
 [`silicate mud`](#silicate_mud)
- Ooze that consists of more than 50 percent siliceous skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siliceous_Ooze
- **Other Properties:**

[]{#silicate_mud}

######  silicate mud
- **Child of**:
 [`mud size sediment`](#mud_size_sediment)
- Mud size sediment that consists of less than 50 percent carbonate
minerals and less than 50 percent clastic particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silicate_Mud
- **Other Properties:**

[]{#siliceous_ooze}

#######  siliceous ooze
- **Child of**:
 [`ooze`](#ooze)
 [`silicate mud`](#silicate_mud)
- Ooze that consists of more than 50 percent siliceous skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siliceous_Ooze
- **Other Properties:**

[]{#non_clastic_siliceous_sediment}

#####  non clastic siliceous sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`non clastic siliceous sedimentary material`](#non_clastic_siliceous_sedimentary_material)
- Sediment that consists of at least 50 percent silicate mineral
material, deposited directly by chemical or biological processes at
the depositional surface, or in particles formed by chemical or
biological processes within the basin of deposition.
- **Source:**
NGMDB 2008; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Non_Clastic_Siliceous_Sediment
- **Other Properties:**

[]{#phosphate_rich_sediment}

#####  phosphate rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`phosphate rich sedimentary material`](#phosphate_rich_sedimentary_material)
- Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are phosphate minerals.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phosphate_Rich_Sediment
- **Other Properties:**

[]{#sand_size_sediment}

#####  sand size sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment in which less than 30 percent of particles are gravel
(greater than 2 mm in diameter) and the sand to mud ratio is at least
1. composition or genesis of clasts not specified.
- **Source:**
Neuendorf et al. 2005 ; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Sand_Size_Sediment
- **Other Properties:**

[]{#sand}

######  sand
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`sand size sediment`](#sand_size_sediment)
- Clastic sediment in which less than 30 percent of particles are
gravel (greater than 2 mm in diameter) and the sand to mud ratio is at
least 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of sand from SLTTs 2004 sandy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sand
- **Other Properties:**

[]{#tephra}

#####  Tephra
- **Child of**:
 [`Sediment`](#sediment)
 [`pyroclastic material`](#pyroclastic_material)
- Unconsolidated pyroclastic material in which greater than 75 percent
of the fragments are deposited as a direct result of volcanic
processes and the deposit has not been reworked by epiclastic
processes. Includes ash, lapilli tephra, bomb tephra, block tephra and
unconsolidated agglomerate.
- **Source:**
Hallsworth and Knox 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tephra
- **Other Properties:**

[]{#ash_and_lapilli}

######  ash and lapilli
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which less than 25 percent of fragments are greater than
64 mm in longest dimension
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_And_Lapilli
- **Other Properties:**

[]{#ash_breccia_bomb_or_block_tephra}

######  ash breccia bomb or block tephra
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which more than 25 percent of particles are greater than
64 mm in largest dimension. Includes ash breccia, bomb tephra and
block tephra of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Breccia_Bomb_Or_Block_Tephra
- **Other Properties:**

[]{#carbonate_sedimentary_material}

####  Carbonate sedimentary material
- **Child of**:
 [`Sedimentary material`](#sedimentary_material)
- Should carbonate sedimentary material be considered a kind of
chemical sedimentary material? Is biogenic precipitation a chemical
sedimentary process?
- Sedimentary material in which at least 50 percent of the primary
and/or recrystallized constituents are composed of one (or more) of
the carbonate minerals calcite, aragonite and dolomite, in particles
of intrabasinal origin.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Sedimentary_Material
- **Other Properties:**

[]{#carbonate_sediment}

#####  carbonate sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite and dolomite, in particles of
intrabasinal origin.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Carbonate_Sediment
- **Other Properties:**

[]{#calcareous_carbonate_sediment}

######  calcareous carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sediment with a calcite (plus aragonite) to dolomite ratio
greater than 1 to 1. Includes lime-sediments.
- **Source:**
after Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#carbonate_mud}

######  carbonate mud
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Carbonate sediment composed of less than 25 percent clasts that have
a maximum diameter more than 2 mm, and the ratio of sand size to mud
size clasts is less than one.
- **Alternate labels:**
marl
- **Source:**
follow pattern used for clastic sand and mud categories, based on SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mud
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#dolomitic_sediment}

######  dolomitic sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sediment with a ratio of magnesium carbonate to calcite
(plus aragonite) greater than 1 to 1.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#impure_carbonate_sediment}

######  impure carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin.
- **Alternate labels:**
marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_carbonate_sediment}

######  pure carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#carbonate_sedimentary_rock}

#####  carbonate sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Particularly for fine-grained sedimentary rocks, distinction of
'intrabasinal' versus 'clastic' genesis can be very interpretive. In
practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored. Carbonate
rock subcatgories are defined on two orthogonal dimensions--mineralogy
(calcitic vs. dolomitic vs non-carbonate impurities), and texture. The
texture categories used here are those of Dunham (1962), and involve
grain size (matrix vs. grains/allochems), fabric (matrix vs. grain
supported), and genesis (bound, frame, or fragmental). The textural
approach used for carbonate rocks is conceptually incompatible with
that used for clastic sedimentary rocks, which is solely grain size or
mineralogy based. This leads to problems in the vocabulary for rocks
of mixed siliclastic/carbonate mineralogy (grainstone vs. sandstone,
carbonate mudstone vs. carbonate rich mudstone, how to accomodate
marlstone...).
- Sedimentary rock in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite, magnesite or dolomite.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#boundstone}

######  boundstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary carbonate rock with preserved biogenic texture, whose
original components were bound and encrusted together during
deposition by the action of plants and animals during deposition, and
remained substantially in the position of growth.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boundstone
- **Other Properties:**

[]{#calcareous_carbonate_sedimentary_rock}

######  calcareous carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
SLTTs 2004; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#carbonate_mudstone}

######  carbonate mudstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Not a subcategory of carbonate sedimentary rock because definition
does not specify 'carbonate minerals of intrabasinal origin', but is
agnostic on origin of carbonate. Schnurrenberger et al. 2003 point out
that it is very difficult (at least in lacustrine rocks) to
distinguish chemically precipitated or diagenetic carbonate from
primary biogenic carbonate. This distinction between biogenic,
detrital, and pedogenic or authigenic carbonate material is thus not a
good one to use in a general purpose classification system.
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Mudstone that consists of greater than 50 percent carbonate minerals
of any origin in the mud size fraction.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mudstone
- **Other Properties:**

[]{#carbonate_wackestone}

######  carbonate wackestone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate sedimentary rock with discernible mud supported
depositional texture and containing greater than 10 percent allochems,
and constituent particles are of intrabasinal origin. If particles are
not intrabasinal, categorization as a mudstone or wackestone should be
considered.
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Wackestone
- **Other Properties:**

[]{#crystalline_carbonate}

######  crystalline carbonate
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate rock of indeterminate mineralogy in which diagenetic
processes have obliterated any original depositional texture.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Crystalline_Carbonate
- **Other Properties:**

[]{#dolomitic_or_magnesian_sedimentary_rock}

######  dolomitic or magnesian sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sedimentary rock with a ratio of magnesium carbonate to
calcite (plus aragonite) greater than 1 to 1. Includes dolostone, lime
dolostone and magnesite-stone.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Or_Magnesian_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#framestone}

######  framestone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate reef rock consisting of a rigid framework of colonies,
shells or skeletons, with internal cavities filled with fine sediment;
usually created through the activities of colonial organisms.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004, Table 15-3-1
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Framestone
- **Other Properties:**

[]{#grainstone}

######  grainstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Carbonate sedimentary rock with recognizable depositional fabric
that is grain-supported, and constituent particles are of intrabasinal
origin; contains little or no mud matrix. Distinction from sandstone
is based on interpretation of intrabasinal origin of clasts and grain-
supported fabric, but grainstone definition does not include a grain
size criteria.
- **Alternate labels:**
carbonate grainstone
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Grainstone
- **Other Properties:**

[]{#impure_carbonate_sedimentary_rock}

######  impure carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary rock in which between 50 and 90 percent of the primary
and/or recrystallized constituents are composed of carbonate minerals.
- **Alternate labels:**
marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#packstone}

######  packstone
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Note that this category overlaps with 'carbonate mudstone'.
- Carbonate sedimentary rock with discernible grain supported
depositional texture, containing greater than 10 percent grains, and
constituent particles are of intrabasinal origin; intergranular spaces
are filled by matrix.
- **Source:**
Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Packstone
- **Other Properties:**

[]{#pure_carbonate_sedimentary_rock}

######  pure carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
- Sedimentary rock in which greater than 90 percent of the primary
and/or recrystallized constituents are carbonate minerals.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#pure_carbonate_mudstone}

#######  pure carbonate mudstone
- **Child of**:
 [`generic mudstone`](#generic_mudstone)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Mudstone that consists of greater than 90 percent carbonate minerals
of intrabasinal orign in the mud fraction, and contains less than 10
percent allochems. The original depositional texture is preserved and
fabric is matrix supported. Carbonate mudstone of Dunham (1962)
- **Source:**
Dunham 1962
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Mudstone
- **Other Properties:**

[]{#calcareous_carbonate_sedimentary_material}

#####  calcareous carbonate sedimentary material
- **Child of**:
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Carbonate sedimentary material of unspecified consolidation state
with a calcite (plus aragonite) to dolomite ratio greater than 1 to 1.
Includes lime-sediments, limestone and dolomitic limestone.
- **Source:**
after Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sedimentary_Material
- **Other Properties:**

[]{#calcareous_carbonate_sediment}

######  calcareous carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sediment with a calcite (plus aragonite) to dolomite ratio
greater than 1 to 1. Includes lime-sediments.
- **Source:**
after Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#calcareous_carbonate_sedimentary_rock}

######  calcareous carbonate sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
SLTTs 2004; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sedimentary_Rock
- **Other Properties:**

[]{#impure_limestone}

#######  impure limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marlstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Limestone
- **Other Properties:**

[]{#limestone}

#######  limestone
- **Child of**:
 [`calcareous carbonate sedimentary rock`](#calcareous_carbonate_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1. Includes limestone and dolomitic
limestone.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Limestone
- **Other Properties:**

[]{#chalk}

########  chalk
- **Child of**:
 [`limestone`](#limestone)
- A generally soft, white, very fine-grained, extremely pure, porous
limestone. It forms under marine conditions from the gradual
accumulation of skeletal elements from minute planktonic green algae
(cocoliths), associated with varying proportions of larger microscopic
fragments of bivalves, foraminifera and ostracods. It is common to
find flint and chert nodules embedded in chalk.
- **Source:**
http://en.wikipedia.org/wiki/Chalk; C.S. Harris, 2009, unpublished web page, http://www.geologyshop.co.uk/chalk.htm
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Chalk
- **Other Properties:**

[]{#travertine}

########  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#dolomitic_or_magnesian_sedimentary_material}

#####  dolomitic or magnesian sedimentary material
- **Child of**:
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Carbonate sedimentary material of unspecified consolidation degree
with a ratio of magnesium carbonate to calcite (plus aragonite)
greater than 1 to 1. Includes dolomite sediment, dolostone, lime
dolostone and magnesite-stone.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Or_Magnesian_Sedimentary_Material
- **Other Properties:**

[]{#dolomitic_or_magnesian_sedimentary_rock}

######  dolomitic or magnesian sedimentary rock
- **Child of**:
 [`carbonate sedimentary rock`](#carbonate_sedimentary_rock)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sedimentary rock with a ratio of magnesium carbonate to
calcite (plus aragonite) greater than 1 to 1. Includes dolostone, lime
dolostone and magnesite-stone.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Or_Magnesian_Sedimentary_Rock
- **Other Properties:**

[]{#dolostone}

#######  dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`pure carbonate sedimentary rock`](#pure_carbonate_sedimentary_rock)
- Pure carbonate sedimentary rock with a ratio of magnesium carbonate
to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolostone, 
pure dolomitic or magnesian carbonate sedimentary rock, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolostone
- **Other Properties:**

[]{#impure_dolostone}

#######  impure dolomite
- **Child of**:
 [`dolomitic or magnesian sedimentary rock`](#dolomitic_or_magnesian_sedimentary_rock)
 [`impure carbonate sedimentary rock`](#impure_carbonate_sedimentary_rock)
- Impure carbonate sedimentary rock with a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marlstone, 
impure dolomitic or magnesian carbonate sedimentary rock, 
impure dolostone, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolostone
- **Other Properties:**

[]{#dolomitic_sediment}

######  dolomitic sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sediment with a ratio of magnesium carbonate to calcite
(plus aragonite) greater than 1 to 1.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#clastic_sedimentary_material}

####  clastic sedimentary material
- **Child of**:
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material of unspecified consolidation state in which at
least 50 percent of the constituent particles were derived from
erosion, weathering, or mass-wasting of pre-existing earth materials,
and transported to the place of deposition by mechanical agents such
as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Sedimentary_Material
- **Other Properties:**

[]{#clastic_sediment}

#####  clastic sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`clastic sedimentary material`](#clastic_sedimentary_material)
- Choice of 'clastic' is purposful. Other suggested labels for this
category include siliciclastic and terrigineous clastic. Siliciclastic
is considered too limiting because the category includes rocks that
consists clasts of carbonate minerals, e.g. epiclastic detritus eroded
from carbonate rock. Terrigineous clastic was considered and rejected
first because it is considered redundant, anything that is
terrigineous is clastic. Second, it is questionable if clastic
sediment derived by submarine processes (fragementation by gravity
sliding, faulting, or volcanic activity, with transport by sediment
gravity flow or submarine currents) is terrigineous, but it is clastic
and is meant to be included in this category.
- Sediment in which at least 50 percent of the constituent particles
were derived from erosion, weathering, or mass-wasting of pre-existing
earth materials, and transported to the place of deposition by
mechanical agents such as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Clastic_Sediment
- **Other Properties:**

[]{#diamicton}

######  diamicton
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
- definition amplified to help distinguish diamicton, conglomerate and
wackestone in this version
- Unsorted or poorly sorted, clastic sediment with a wide range of
particle sizes, including a muddy matrix. Biogenic materials that have
such texture are excluded. Distinguished from conglomerate, sandstone,
mudstone based on polymodality and lack of structures related to
transport and deposition of sediment by moving air or water.
Assignment to an other size class can be used in conjunction to
indicate the dominant grain size.
- **Source:**
Fairbridge and Bourgeois 1978
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Diamicton
- **Other Properties:**

[]{#gravel}

######  gravel
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`gravel size sediment`](#gravel_size_sediment)
- Clastic sediment containing greater than 30 percent gravel-size
particles (greater than 2.0 mm diameter). Gravel in which more than
half of the particles are of epiclastic origin
- **Source:**
definition of gravel from SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gravel
- **Other Properties:**

[]{#mud}

######  mud
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Clastic sediment consisting of less than 30 percent gravel-size (2
mm) particles and with a mud-size to sand-size particle ratio greater
than 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of mud from SLTTs 2004 muddy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mud
- **Other Properties:**

[]{#clay}

#######  clay
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent particles with grain
size less than 0.004 mm
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clay
- **Other Properties:**

[]{#silt}

#######  silt
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent silt-size grains.
- **Alternate labels:**
loess
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silt
- **Other Properties:**

[]{#sand}

######  sand
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`sand size sediment`](#sand_size_sediment)
- Clastic sediment in which less than 30 percent of particles are
gravel (greater than 2 mm in diameter) and the sand to mud ratio is at
least 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of sand from SLTTs 2004 sandy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sand
- **Other Properties:**

[]{#clastic_sedimentary_rock}

#####  clastic sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`clastic sedimentary material`](#clastic_sedimentary_material)
- The conglomerate, sandstone, mudstone, and wackestone categories are
not defined as kinds of clastic sedimentary rocks because rocks
meeting their purely grainsize based definitions might also be iron-
rich, phosphatic, or carbonate. This is based on GeoSciML allowance to
assign rocks to more than one lithology category. For example to
categorize a rock as a clastic conglomerate requires assignment ot the
'clastic sedimentary rock' category and to the 'conglomerate'
category. Particularly for fine-grained sedimentary rocks, distinction
of 'intrabasinal' versus 'clastic' genesis can be very interpretive.
In practice the use of clastic mudstone terminology as opposed to
carbonate mudstone terminology may be dermined by a priori knowledge
about the rock being categorized. If it is associated with other
clastic rocks, the clastic categories will be favored, if with
cabonate rocks, the carbonate categories will be favored.
- Sedimentary rock in which at least 50 percent of the constituent
particles were derived from erosion, weathering, or mass-wasting of
pre-existing earth materials, and transported to the place of
deposition by mechanical agents such as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Clastic_Sedimentary_Rock
- **Other Properties:**

[]{#diamictite}

######  diamictite
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
- Unsorted or poorly sorted, clastic sedimentary rock with a wide
range of particle sizes including a muddy matrix. Biogenic materials
that have such texture are excluded. Distinguished from conglomerate,
sandstone, mudstone based on polymodality and lack of structures
related to transport and deposition of sediment by moving air or
water. If more than 10 percent of the fine grained matrix is of
indeterminant clastic or diagenetic origin and the fabric is matrix
supported, may also be categorized as wacke.
- **Source:**
Fairbridge and Bourgeois 1978
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Diamictite
- **Other Properties:**

[]{#clastic_conglomerate}

######  conglomerate
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic conglomerate`](#generic_conglomerate)
- Note this category is equivalent to category labeled 'Conglomeratic
rock in SLTTs (2004), not to the category labeled 'Conglomerate' in
that system.
- Clastic sedimentary rock composed of at least 30 percent rounded to
subangular fragments larger than 2 mm in diameter; typically contains
finer grained material in interstices between larger fragments. If
more than 15 percent of the fine grained matrix is of indeterminant
clastic or diagenetic origin and the fabric is matrix supported, may
also be categorized as wackestone. If rock has unsorted or poorly
sorted texture with a wide range of particle sizes, may also be
categorized as diamictite.
- **Alternate labels:**
conglomeratic rock
- **Source:**
Neuendorf et al. 2005; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Conglomerate
- **Other Properties:**

[]{#clastic_mudstone}

######  mudstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`generic mudstone`](#generic_mudstone)
- Distinction of intrabasinal, diagenetic, or clastic genesis for very
fine-grained carbonate minerals is interpretive in many cases. If
there is uncertainty on the mudstone category based on intrabasinal vs
epiclastic distinction required for clastic sedimentary rock-carbonate
sedimentary rock categorization in this system, it is recommended to
use the generic_mudstone category. This category is the union of the
various fields labeled 'mudstone' with various qualifiers in Folk,
1954, Figure 1a, although Folk's (1954) category labeled 'mudstone' is
a much more restricted category. The CGI category is equivalent to
category labeled 'Mudrock' in SLTTs (2004), not to the category
labeled 'Mudstone' adopted by that system from Folk (1954).
Schnurrenberger, D., Russell, J. and Kelts, K., 2003, Classification
of lacustrine sediments based on sedimentary components: Journal of
Paleolimnology, v.29, p141-154.
- Clastic sedimentary rock consisting of less than 30 percent gravel-
size (2 mm) particles and with a mud to sand ratio greater than 1.
- **Alternate labels:**
clastic mudstone, 
mudrock, 
- **Source:**
Pettijohn et al. 1987 referenced in Hallsworth and Knox 1999.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Mudstone
- **Other Properties:**

[]{#claystone}

#######  claystone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Mudstone that contains no detectable silt, inferred to consist
virtually entirely of clay-size particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Claystone
- **Other Properties:**

[]{#shale}

#######  shale
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Note definition does not specify carbonate vs. siliclastic nature of
mud.
- Laminated mudstone that will part or break along thin, closely
spaced layers parallel to stratification.
- **Source:**
NADM SLTT sedimentary, 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Shale
- **Other Properties:**

[]{#siltstone}

#######  siltstone
- **Child of**:
 [`mudstone`](#clastic_mudstone)
- Use of 'detectable silt' in the criteria for this category is based
on the observation that in practice, distinction of claystone from
'siltstone' is typically based on a qualitative assessment of
'grittiness' (e.g. rubbing with fingers, or chewing); the property
that these tests can determine is the presence or absence of silty
particles in the material. Quantitative grain size analysis in the the
clay/silt fraction of a lithified sediment is difficult at best, and
of questionable significance because diagensis has altered the size
and mineralogy of original sedimentary particles.
- Mudstone that contains detectable silt. (see comments)
- **Alternate labels:**
Silt bearing mudstone
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siltstone
- **Other Properties:**

[]{#clastic_sandstone}

######  sandstone
- **Child of**:
 [`clastic sedimentary rock`](#clastic_sedimentary_rock)
 [`Generic sandstone`](#generic_sandstone)
- Note this category is equivalent to cagetory labeled 'sandy rock' in
SLTTs (2004), not to the much more restricted category labeled
'Sandstone' in that system.
- Clastic sedimentary rock in which less than 30 percent of particles
are greater than 2 mm in diameter (gravel) and the sand to mud ratio
is at least 1.
- **Alternate labels:**
clastic sandstone, 
sandy rock, 
- **Source:**
SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clastic_Sandstone
- **Other Properties:**

[]{#arenite}

#######  arenit
* `arenite`
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Clastic sandstone that contains less than 10 percent matrix. Matrix
is mud-size silicate minerals (clay, feldspar, quartz, rock fragments,
and alteration products) of detrital or diagenetic nature.
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Arenite
- **Other Properties:**

[]{#wacke}

#######  wacke
- **Child of**:
 [`sandstone`](#clastic_sandstone)
- Distinction from mudstone is based on inference that less that 50
percent of the mud size fraction (matrix) is original mud size
detrital particles. May also grade into diamictite or conglomerate
based on size distribution of discernible particles. If more than 50
percent of rock is detrital particles of intrabasinal orgin and
carbonate composition, categorize as carbonate wackestone. Term is
typically applied to diagenetically altered volcanic-lithic clastic
rocks in which the definition of the original clasts has been
obscured. Suggested boundaries between wacke and arenite range from 5
to 15 percent matrix. See Dickinson (1970) for discussion of
interpretation of undiscernible matrix in diagenetically altered
lithic clastic rocks. Dickinson, W.R., 1970, Interpreting detrital
modes of graywacke and arkose: Journal of Sedimentary Petrology, v.
40, p. 695-707.
- Clastic sandstone with more than 10 percent matrix of indeterminate
detrital or diagenetic nature. Matrix is mud size silicate minerals
(clay, feldspar, quartz, rock fragments, and alteration products).
- **Source:**
Pettijohn, Potter, Siever, 1972, Sand and Sandstone: New York, Springer Verlag, 681 p.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Wacke
- **Other Properties:**

[]{#non_clastic_siliceous_sedimentary_material}

####  non clastic siliceous sedimentary material
- **Child of**:
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material that consists of at least 50 percent silicate
mineral material, deposited directly by chemical or biological
processes at the depositional surface, or in particles formed by
chemical or biological processes within the basin of deposition.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Non_Clastic_Siliceous_Sedimentary_Material
- **Other Properties:**

[]{#non_clastic_siliceous_sediment}

#####  non clastic siliceous sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`non clastic siliceous sedimentary material`](#non_clastic_siliceous_sedimentary_material)
- Sediment that consists of at least 50 percent silicate mineral
material, deposited directly by chemical or biological processes at
the depositional surface, or in particles formed by chemical or
biological processes within the basin of deposition.
- **Source:**
NGMDB 2008; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Non_Clastic_Siliceous_Sediment
- **Other Properties:**

[]{#non_clastic_siliceous_sedimentary_rock}

#####  non clastic siliceous sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`non clastic siliceous sedimentary material`](#non_clastic_siliceous_sedimentary_material)
- Definition updated to include chert, flint SMR 2020-09-21
- Sedimentary rock that consists of at least 50 percent silicate
mineral material, deposited directly by chemical or biological
processes at the depositional surface, in particles formed by chemical
or biological processes within the basin of deposition, or formed by
diagenetic processes. Includes chert and flint found in carbonate
rocks.
- **Source:**
modified from SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Non_Clastic_Siliceous_Sedimentary_Rock
- **Other Properties:**

[]{#biogenic_silica_sedimentary_rock}

######  biogenic silica sedimentary rock
- **Child of**:
 [`non clastic siliceous sedimentary rock`](#non_clastic_siliceous_sedimentary_rock)
- Sedimentary rock that consists of at least 50 percent silicate
mineral material, deposited directly by biological processes at the
depositional surface, or in particles formed by biological processes
within the basin of deposition. Includes radiolarian chert, diatomite,
novaculite.
- **Source:**
based on NADM SLTT sedimentary; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Biogenic_Silica_Sedimentary_Rock
- **Other Properties:**

[]{#organic_rich_sedimentary_material}

####  organic rich sedimentary material
- **Child of**:
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material in which 50 percent or more of the primary
sedimentary material is organic carbon.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Organic_Rich_Sedimentary_Material
- **Other Properties:**

[]{#organic_rich_sedimentary_rock}

#####  organic rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`organic rich sedimentary material`](#organic_rich_sedimentary_material)
- Sapropelic coal, and asphaltite are not differentiated in This
vocabulary
- Sedimentary rock with color, composition, texture and apparent
density indicating greater than 50 percent organic content by weight
on a moisture-free basis.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Organic_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#coal}

######  coal
* `kohle`
- **Child of**:
 [`organic rich sedimentary rock`](#organic_rich_sedimentary_rock)
- A consolidated organic sedimentary material having less than 75%
moisture. This category includes low, medium, and high rank coals
according to International Classification of In-Seam Coal (United
Nations, 1998), thus including lignite. Sapropelic coal is not
distinguished in this category from humic coals. Formed from the
compaction or induration of variously altered plant remains similar to
those of peaty deposits.
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp.
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Coal
- **Other Properties:**

[]{#anthracite_coal}

#######  anthracite
* `anthrazit`
- **Child of**:
 [`coal`](#coal)
- Coal that has vitrinite mean random reflectance greater than 2.0%
(determined in conformance with ISO 7404-5). Less than 12-14 percent
volatiles (dry, ash free), greater than 91 percent fixed carbon (dry,
ash free basis). The highest rank coal; very hard, glossy, black, with
semimetallic luster, semi conchoidal fracture.
- **Alternate labels:**
High rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp; see also Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Coal#Types_of_coal; Eberhard Lindner; Chemie für Ingenieure; Lindner Verlag Karlsruhe, S. 258
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anthracite_Coal
- **Other Properties:**

[]{#bituminous_coal}

#######  bituminous coal
- **Child of**:
 [`coal`](#coal)
- Coal that has vitrinite mean random reflectance greater than 0.6%
and less than 2.0% (determined in conformance with ISO 7404-5), or has
a gross calorific value greater than 24 MJ/kg (determined in
conformance with ISO 1928). Hard, black, organic rich sedimentary
rock; contains less than 91 percent fixed carbon on a dry, mineral-
matter-free basis, and greater than 13-14 percent volatiles (dry, ash
free). Formed from the compaction or induration of variously altered
plant remains similar to those of peaty deposits.
- **Alternate labels:**
medium rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp; see also http://en.wikipedia.org/wiki/Coal#Types_of_coal; Eberhard Lindner; Chemie für Ingenieure; Lindner Verlag Karlsruhe, S. 258
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Bituminous_Coal
- **Other Properties:**

[]{#lignite}

#######  lignite
- **Child of**:
 [`coal`](#coal)
- Coal that has a gross calorific value less than 24 MJ/kg (determined
in conformance with ISO 1928), and vitrinite mean random reflectance
less than 0.6% (determined in conformance with ISO 7404-5). Gross
calorific value is recalculated to a moist, ash free basis using bed
moisture (determined according to ISO 1015 or ISO 5068). Includes all
low-rank coals, including sub-bitiminous coal. A consolidated, dull,
soft brown to black coal having many readily discernible plant
fragments set in a finer grained organic matrix. Tends to crack and
fall apart on drying. Operationally sub-bituminous and bitiminous coal
are qualitatively distinguished based on brown streak for sub-
bitiminous coal and black streak for bituminous coal.
- **Alternate labels:**
low rank coal
- **Source:**
Economic commission for Europe, committee on Sustainable Energy- United Nations (ECE-UN), 1998, International Classification of in-Seam Coals: Energy 19, 41 pp.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Lignite
- **Other Properties:**

[]{#organic_rich_sediment}

#####  organic rich sediment
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`organic rich sedimentary material`](#organic_rich_sedimentary_material)
- The broader relation from organic rich sediment to biogenic sediment
is based on the inference that organic rich material is always
biogenic in origin. Biogenic is a broader category because not all
biogenic materials are organic rich, for example shells or phosphatic
bone.
- Sediment with color, composition, texture and apparent density
indicating greater than 50 percent organic content by weight on a
moisture-free basis.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Organic_Rich_Sediment
- **Other Properties:**

[]{#peat}

######  peat
- **Child of**:
 [`organic rich sediment`](#organic_rich_sediment)
- Unconsolidated organic-rich sediment composed of at least 50 percent
semi-carbonised plant remains; individual remains commonly seen with
unaided eye; yellowish brown to brownish black; generally fibrous
texture; can be plastic or friable. In its natural state it can be
readily cut and has a very high moisture content, generally greater
than 90 percent. Liptinite to Inertinite ratio is less than one
(Economic commission for Europe, committee on Sustainable Energy-
United Nations (ECE-UN), 1998, International Classification of in-Seam
Coals: Energy 19, 41 pp.)
- **Source:**
Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Peat
- **Other Properties:**

[]{#sapropel}

######  sapropel
- **Child of**:
 [`organic rich sediment`](#organic_rich_sediment)
- Jelly like organic rich sediment composed of plant remains, usually
algal. Liptinite to Inertinite ratio is greater than one (Economic
commission for Europe, committee on Sustainable Energy- United Nations
(ECE-UN), 1998, International Classification of in-Seam Coals: Energy
19, 41 pp.)
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sapropel
- **Other Properties:**

[]{#phosphate_rich_sedimentary_material}

####  phosphate rich sedimentary material
- **Child of**:
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material in which at least 50 percent of the primary
and/or recrystallized constituents are phosphate minerals.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Phosphate_Rich_Sedimentary_Material
- **Other Properties:**

[]{#phosphate_rich_sediment}

#####  phosphate rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`phosphate rich sedimentary material`](#phosphate_rich_sedimentary_material)
- Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are phosphate minerals.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phosphate_Rich_Sediment
- **Other Properties:**

[]{#phosphorite}

#####  phosphorite
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`phosphate rich sedimentary material`](#phosphate_rich_sedimentary_material)
- Sedimentary rock in which at least 50 percent of the primary or
recrystallized constituents are phosphate minerals. Most commonly
occurs as a bedded primary or reworked secondary marine rock, composed
of microcrystalline carbonate fluorapatite in the form of lamina,
pellets, oolites and nodules, and skeletal, shell and bone fragments.
- **Source:**
HallsworthandKnox 1999, Jackson 1997
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phosphorite
- **Other Properties:**


[]{#anthropogenic_material}

##  Anthropogenic material
- Material known to have artificial (human-related) origin;
insufficient information to classify in more detail.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anthropogenic_Material
- **Other Properties:**

[]{#anthropogenic_unconsolidated_material}

###  Anthropogenic unconsolidated material
- **Child of**:
 [`Anthropogenic material`](#anthropogenic_material)
 [`Unconsolidated material`](#unconsolidated_material)
- Unconsolidated material known to have artificial (human-related)
origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anthropogenic_Unconsolidated_Material
- **Other Properties:**

[]{#concrete}

###  Concrete
- **Child of**:
 [`Anthropogenic material`](#anthropogenic_material)
-
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Concrete
- **Other Properties:**

[]{#manufactured_chemical_substance}

###  Manufactured chemical substance
- **Child of**:
 [`Anthropogenic material`](#anthropogenic_material)
- material is an artifically produced sustance consisting of a single
chemical entity
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Manufactured_Chemical_Substance
- **Other Properties:**

[]{#mineral_processing_product}

###  Mineral processing product
- **Child of**:
 [`Anthropogenic material`](#anthropogenic_material)
- Includes tailings, slag, matte, concentrate etc, materials resulting
from mineral processing for resource extraction
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mineral_Processing_Product
- **Other Properties:**

[]{#matte}

####  Matte
- **Child of**:
 [`Mineral processing product`](#mineral_processing_product)
- molten metal sulfide phases typically formed during smelting of
copper, nickel, and other base metals
(https://en.wikipedia.org/wiki/Matte_(metallurgy) )
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Matte
- **Other Properties:**

[]{#slag}

####  Slag
- **Child of**:
 [`Mineral processing product`](#mineral_processing_product)
-
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Slag
- **Other Properties:**


[]{#unconsolidated_material}

##  Unconsolidated material
- compoundMaterial composed of an aggregation of particles that do not
adhere to each other strongly enough that the aggregate can be
considered a solid in its own right.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Unconsolidated_Material
- **Other Properties:**

[]{#anthropogenic_unconsolidated_material}

###  Anthropogenic unconsolidated material
- **Child of**:
 [`Anthropogenic material`](#anthropogenic_material)
 [`Unconsolidated material`](#unconsolidated_material)
- Unconsolidated material known to have artificial (human-related)
origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Anthropogenic_Unconsolidated_Material
- **Other Properties:**

[]{#natural_unconsolidated_material}

###  Natural unconsolidated material
- **Child of**:
 [`Unconsolidated material`](#unconsolidated_material)
- Unconsolidated material known to have natural, ie. not human-made,
origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Natural_Unconsolidated_Material
- **Other Properties:**

[]{#sediment}

####  Sediment
- **Child of**:
 [`Natural unconsolidated material`](#natural_unconsolidated_material)
 [`Sedimentary material`](#sedimentary_material)
- Solid granular material transported by wind, water, or gravity, not
modified by interaction with biosphere or atmosphere (to differentiate
from soil). Particles derived by erosion of pre-existing rock, from
shell or other body parts from organisms, precipitated chemically in
the surficial environment, or generated by explosive volcanic
activity.
(http://resource.geosciml.org/classifier/cgi/lithology/sediment).
Sediment is not consolidated, i.e. Particulate constituents of a
compound material do not adhere to each other strongly enough that the
aggregate can be considered a solid material in its own right. Similar
to http://purl.obolibrary.org/obo/ENVO_00002007
- Unconsolidated material consisting of an aggregation of particles
transported or deposited by air, water or ice, or that accumulated by
other natural agents, such as chemical precipitation, and that forms
in layers on the Earth's surface. Includes epiclastic deposits.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/vocabulary/material/1.0/sediment
- **Other Properties:**

[]{#biogenic_sediment}

#####  biogenic sediment
- **Child of**:
 [`Sediment`](#sediment)
- Corresponding biogenic sedimentary material and biogenic sedimentary
rock categories are not included based on the interpretation that
biogenic sedimentary rock will be in a different category, e.g.
carbonate sedimentary rock or organic rich sedimentary rock.
- Sediment composed of greater than 50 percent material of biogenic
origin. Because the biogenic material may be skeletal remains that are
not organic, all biogenic sediment is not necessarily organic-rich.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Biogenic_Sediment
- **Other Properties:**

[]{#ooze}

######  ooze
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Neuendorf et al. 2005 put cutoff at 30 percent skeletal remains;
this is raised to 50 percent in This vocabulary for consistency with
definition of other Biogenic sediment category
- Biogenic sediment consisting of less than 1 percent gravel-size
(greater than or equal to 2 mm) particles, with a sand to mud ratio
less than 1 to 9, and less than 50 percent carbonate minerals.
- **Alternate labels:**
biogenic mud
- **Source:**
based on Bates and Jackson 1987 and Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ooze
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#siliceous_ooze}

#######  siliceous ooze
- **Child of**:
 [`ooze`](#ooze)
 [`silicate mud`](#silicate_mud)
- Ooze that consists of more than 50 percent siliceous skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siliceous_Ooze
- **Other Properties:**

[]{#organic_rich_sediment}

######  organic rich sediment
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`organic rich sedimentary material`](#organic_rich_sedimentary_material)
- The broader relation from organic rich sediment to biogenic sediment
is based on the inference that organic rich material is always
biogenic in origin. Biogenic is a broader category because not all
biogenic materials are organic rich, for example shells or phosphatic
bone.
- Sediment with color, composition, texture and apparent density
indicating greater than 50 percent organic content by weight on a
moisture-free basis.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Organic_Rich_Sediment
- **Other Properties:**

[]{#peat}

#######  peat
- **Child of**:
 [`organic rich sediment`](#organic_rich_sediment)
- Unconsolidated organic-rich sediment composed of at least 50 percent
semi-carbonised plant remains; individual remains commonly seen with
unaided eye; yellowish brown to brownish black; generally fibrous
texture; can be plastic or friable. In its natural state it can be
readily cut and has a very high moisture content, generally greater
than 90 percent. Liptinite to Inertinite ratio is less than one
(Economic commission for Europe, committee on Sustainable Energy-
United Nations (ECE-UN), 1998, International Classification of in-Seam
Coals: Energy 19, 41 pp.)
- **Source:**
Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Peat
- **Other Properties:**

[]{#sapropel}

#######  sapropel
- **Child of**:
 [`organic rich sediment`](#organic_rich_sediment)
- Jelly like organic rich sediment composed of plant remains, usually
algal. Liptinite to Inertinite ratio is greater than one (Economic
commission for Europe, committee on Sustainable Energy- United Nations
(ECE-UN), 1998, International Classification of in-Seam Coals: Energy
19, 41 pp.)
- **Source:**
Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sapropel
- **Other Properties:**

[]{#carbonate_sediment}

#####  carbonate sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`Carbonate sedimentary material`](#carbonate_sedimentary_material)
- Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are composed of one (or more) of the
carbonate minerals calcite, aragonite and dolomite, in particles of
intrabasinal origin.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Carbonate_Sediment
- **Other Properties:**

[]{#calcareous_carbonate_sediment}

######  calcareous carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`calcareous carbonate sedimentary material`](#calcareous_carbonate_sedimentary_material)
- Carbonate sediment with a calcite (plus aragonite) to dolomite ratio
greater than 1 to 1. Includes lime-sediments.
- **Source:**
after Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#carbonate_mud}

######  carbonate mud
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Carbonate sediment composed of less than 25 percent clasts that have
a maximum diameter more than 2 mm, and the ratio of sand size to mud
size clasts is less than one.
- **Alternate labels:**
marl
- **Source:**
follow pattern used for clastic sand and mud categories, based on SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mud
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#dolomitic_sediment}

######  dolomitic sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`dolomitic or magnesian sedimentary material`](#dolomitic_or_magnesian_sedimentary_material)
- Carbonate sediment with a ratio of magnesium carbonate to calcite
(plus aragonite) greater than 1 to 1.
- **Source:**
after SLTTs 2004, Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Dolomitic_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#impure_carbonate_sediment}

######  impure carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin.
- **Alternate labels:**
marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Carbonate_Sediment
- **Other Properties:**

[]{#impure_calcareous_carbonate_sediment}

#######  impure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
calcareous marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#impure_dolomitic_sediment}

#######  impure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`impure carbonate sediment`](#impure_carbonate_sediment)
- Carbonate sediment in which between 50 and 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and the ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Alternate labels:**
dolomitic marl
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Impure_Dolomitic_Sediment
- **Other Properties:**

[]{#pure_carbonate_sediment}

######  pure carbonate sediment
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Carbonate_Sediment
- **Other Properties:**

[]{#pure_calcareous_carbonate_sediment}

#######  pure calcareous carbonate sediment
- **Child of**:
 [`calcareous carbonate sediment`](#calcareous_carbonate_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a calcite (plus aragonite) to
dolomite ratio greater than 1 to 1.
- **Alternate labels:**
lime sediment
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Calcareous_Carbonate_Sediment
- **Other Properties:**

[]{#pure_dolomitic_sediment}

#######  pure dolomitic sediment
- **Child of**:
 [`dolomitic sediment`](#dolomitic_sediment)
 [`pure carbonate sediment`](#pure_carbonate_sediment)
- Carbonate sediment in which greater than 90 percent of the
constituents are composed of one (or more) of the carbonate minerals
in particles of intrabasinal origin, and a ratio of magnesium
carbonate to calcite (plus aragonite) greater than 1 to 1.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pure_Dolomitic_Sediment
- **Other Properties:**

[]{#chemical_sedimentary_material}

#####  chemical sedimentary material
- **Child of**:
 [`Sediment`](#sediment)
 [`Sedimentary material`](#sedimentary_material)
- Sedimentary material that consists of at least 50 percent material
produced by inorganic chemical processes within the basin of
deposition. Includes inorganic siliceous, carbonate, evaporite, iron-
rich, and phosphatic sediment classes, as well as chemical sediments
associated with submarine hot springs ('black smokers'). Note that
these sediments might crystallize as a solid as they are deposited,
thus similar to rock....
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Chemical_Sedimentary_Material
- **Other Properties:**

[]{#evaporite}

######  evaporite
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
- Nonclastic sedimentary rock composed of at least 50 percent non-
carbonate salts, including chloride, sulfate or borate minerals;
formed through precipitation of mineral salts from a saline solution
(non-carbonate salt rock).
- **Source:**
Jackson 1997; SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Evaporite
- **Other Properties:**

[]{#exotic_evaporite}

#######  exotic evaporite
- **Child of**:
 [`evaporite`](#evaporite)
- Category represents evaporite material that is not mostly
gypsum/anhydrite or halite. These are generally not very common, thus
the 'exotic' name
- Evaporite that is not 50 percent halite or 50 percent gypsum or
anhydrite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Exotic_Evaporite
- **Other Properties:**

[]{#rock_gypsum_or_anhydrite}

#######  gypsum or anhydrite
- **Child of**:
 [`evaporite`](#evaporite)
- Evaporite composed of at least 50 percent gypsum or anhydrite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rock_Gypsum_Or_Anhydrite
- **Other Properties:**

[]{#rock_salt}

#######  rock salt
- **Child of**:
 [`evaporite`](#evaporite)
- Evaporite composed of at least 50 percent halite.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Rock_Salt
- **Other Properties:**

[]{#iron_rich_sedimentary_material}

######  iron rich sedimentary material
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
- Sedimentary material of unspecified consolidation state that
consists of at least 50 percent iron-bearing minerals (hematite,
magnetite, limonite-group, siderite, iron-sulfides), as determined by
hand-lens or petrographic analysis. Corresponds to a rock typically
containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Iron_Rich_Sedimentary_Material
- **Other Properties:**

[]{#iron_rich_sediment}

#######  iron rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sediment that consists of at least 50 percent iron-bearing minerals
(hematite, magnetite, limonite-group, siderite, iron-sulfides), as
determined by hand-lens or petrographic analysis. Corresponds to a
rock typically containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sediment
- **Other Properties:**

[]{#iron_rich_sedimentary_rock}

#######  iron rich sedimentary rock
- **Child of**:
 [`Sedimentary rock`](#sedimentary_rock)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sedimentary rock that consists of at least 50 percent iron-bearing
minerals (hematite, magnetite, limonite-group, siderite, iron-
sulfides), as determined by hand-lens or petrographic analysis.
Corresponds to a rock typically containing 15 percent iron by weight.
- **Source:**
Hallsworth and Knox 1999; SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sedimentary_Rock
- **Other Properties:**

[]{#sedimentary_massive_sulphide}

######  Sedimentary Massive Sulphide
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`Massive sulphide`](#massive_sulphide)
- rock consisting of greater than 50% sulphide or sulfosalt minerals
formed by sedimentary exhalative processes.
- **Alternate labels:**
Sedimentary Massive Sulfide
- **Source:**
smr provisional 2020-06-07
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sedimentary_Massive_Sulphide
- **Other Properties:**

[]{#travertine}

######  travertine
- **Child of**:
 [`chemical sedimentary material`](#chemical_sedimentary_material)
 [`limestone`](#limestone)
- Biotically or abiotically precipitated calcium carbonate, from
spring-fed, heated, or ambient-temperature water. May be white and
spongy, various shades of orange, tan or gray, and ranges to dense,
banded or laminated rock. Macrophytes, bryophytes, algae,
cyanobacteria and other organisms often colonize the surface of
travertine and may be preserved, to produce the porous varieties.
- **Source:**
Neuendorf et al. 2005; http://en.wikipedia.org/wiki/Travertine; Chafetz, H.S., and Folk, R.L., 1984, Travertine: Depositional morphology an dthe bacterially constructed constituents: J. Sed. Petrology, v. 126, p.57-74.
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Travertine
- **Other Properties:**

[]{#clastic_sediment}

#####  clastic sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`clastic sedimentary material`](#clastic_sedimentary_material)
- Choice of 'clastic' is purposful. Other suggested labels for this
category include siliciclastic and terrigineous clastic. Siliciclastic
is considered too limiting because the category includes rocks that
consists clasts of carbonate minerals, e.g. epiclastic detritus eroded
from carbonate rock. Terrigineous clastic was considered and rejected
first because it is considered redundant, anything that is
terrigineous is clastic. Second, it is questionable if clastic
sediment derived by submarine processes (fragementation by gravity
sliding, faulting, or volcanic activity, with transport by sediment
gravity flow or submarine currents) is terrigineous, but it is clastic
and is meant to be included in this category.
- Sediment in which at least 50 percent of the constituent particles
were derived from erosion, weathering, or mass-wasting of pre-existing
earth materials, and transported to the place of deposition by
mechanical agents such as water, wind, ice and gravity.
- **Source:**
SLTTs 2004; Neuendorf et al. 2005
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Clastic_Sediment
- **Other Properties:**

[]{#diamicton}

######  diamicton
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
- definition amplified to help distinguish diamicton, conglomerate and
wackestone in this version
- Unsorted or poorly sorted, clastic sediment with a wide range of
particle sizes, including a muddy matrix. Biogenic materials that have
such texture are excluded. Distinguished from conglomerate, sandstone,
mudstone based on polymodality and lack of structures related to
transport and deposition of sediment by moving air or water.
Assignment to an other size class can be used in conjunction to
indicate the dominant grain size.
- **Source:**
Fairbridge and Bourgeois 1978
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Diamicton
- **Other Properties:**

[]{#gravel}

######  gravel
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`gravel size sediment`](#gravel_size_sediment)
- Clastic sediment containing greater than 30 percent gravel-size
particles (greater than 2.0 mm diameter). Gravel in which more than
half of the particles are of epiclastic origin
- **Source:**
definition of gravel from SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gravel
- **Other Properties:**

[]{#mud}

######  mud
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Clastic sediment consisting of less than 30 percent gravel-size (2
mm) particles and with a mud-size to sand-size particle ratio greater
than 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of mud from SLTTs 2004 muddy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mud
- **Other Properties:**

[]{#clay}

#######  clay
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent particles with grain
size less than 0.004 mm
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clay
- **Other Properties:**

[]{#silt}

#######  silt
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent silt-size grains.
- **Alternate labels:**
loess
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silt
- **Other Properties:**

[]{#sand}

######  sand
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`sand size sediment`](#sand_size_sediment)
- Clastic sediment in which less than 30 percent of particles are
gravel (greater than 2 mm in diameter) and the sand to mud ratio is at
least 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of sand from SLTTs 2004 sandy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sand
- **Other Properties:**

[]{#gravel_size_sediment}

#####  gravel size sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment containing greater than 30 percent gravel-size particles
(greater than 2.0 mm diameter). Composition or gensis of clasts not
specified.
- **Source:**
SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Gravel_Size_Sediment
- **Other Properties:**

[]{#boulder_gravel_size_sediment}

######  boulder gravel size sediment
- **Child of**:
 [`gravel size sediment`](#gravel_size_sediment)
- Sediment containing greater than 30 percent boulder-size particles
(greater than 256 mm in diameter)
- **Source:**
Wentworth size scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Boulder_Gravel_Size_Sediment
- **Other Properties:**

[]{#cobble_gravel_size_sediment}

######  cobble gravel size sediment
- **Child of**:
 [`gravel size sediment`](#gravel_size_sediment)
- Sediment containing greater than 30 percent cobble-size particles
(64-256 mm in diameter)
- **Source:**
Wentworth size scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Cobble_Gravel_Size_Sediment
- **Other Properties:**

[]{#gravel}

######  gravel
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`gravel size sediment`](#gravel_size_sediment)
- Clastic sediment containing greater than 30 percent gravel-size
particles (greater than 2.0 mm diameter). Gravel in which more than
half of the particles are of epiclastic origin
- **Source:**
definition of gravel from SLTTs 2004; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Gravel
- **Other Properties:**

[]{#pebble_gravel_size_sediment}

######  pebble gravel size sediment
- **Child of**:
 [`gravel size sediment`](#gravel_size_sediment)
- Sediment containing greater than 30 percent pebble-size particles
(2.0 -64 mm in diameter)
- **Source:**
Wentworth size scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Pebble_Gravel_Size_Sediment
- **Other Properties:**

[]{#hybrid_sediment}

#####  Hybrid sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment that does not fit any of the other sediment
composition/genesis categories. Sediment consisting of three or more
components which form more than 5 percent but less than 50 precent of
the material.
- **Source:**
Hallsworth and Knox, 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Hybrid_Sediment
- **Other Properties:**

[]{#iron_rich_sediment}

#####  iron rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`iron rich sedimentary material`](#iron_rich_sedimentary_material)
- Sediment that consists of at least 50 percent iron-bearing minerals
(hematite, magnetite, limonite-group, siderite, iron-sulfides), as
determined by hand-lens or petrographic analysis. Corresponds to a
rock typically containing 15 percent iron by weight.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Iron_Rich_Sediment
- **Other Properties:**

[]{#mud_size_sediment}

#####  mud size sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment consisting of less than 30 percent gravel-size (2 mm)
particles and with a mud-size to sand-size particle ratio greater than
1. Clasts may be of any composition or origin.  BGS  (Hallsworth and
Knox, 1999, p. 9) define the  'upper size limit of mud ... at 32
micrometers (.032 mm)', but Wentworth scale and Krumbein scale put
boundary at .064 or .062 mm (inidistinguishable difference in
rocks...) BGS 'mud-grade sediment' or sedimentary rock definition is
'over 75% of the clasts smaller than  .032 mm', which is narrower than
the definition here.
- Sediment consisting of less than 30 percent gravel-size (2 mm)
particles and with a mud-size to sand-size particle ratio greater than
1. Clasts may be of any composition or origin.
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Mud_Size_Sediment
- **Other Properties:**

[]{#carbonate_mud}

######  carbonate mud
- **Child of**:
 [`carbonate sediment`](#carbonate_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Carbonate sediment composed of less than 25 percent clasts that have
a maximum diameter more than 2 mm, and the ratio of sand size to mud
size clasts is less than one.
- **Alternate labels:**
marl
- **Source:**
follow pattern used for clastic sand and mud categories, based on SLTTs 2004
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Mud
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#carbonate_rich_mud}

######  carbonate rich mud
- **Child of**:
 [`mud size sediment`](#mud_size_sediment)
- Mud size sediment that contains between 10 and 50 percent carbonate
minerals in any size fraction. Carbonate origin is not specified.
- **Alternate labels:**
carbonate rich loess, 
marl, 
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Rich_Mud
- **Other Properties:**

[]{#mud}

######  mud
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Clastic sediment consisting of less than 30 percent gravel-size (2
mm) particles and with a mud-size to sand-size particle ratio greater
than 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of mud from SLTTs 2004 muddy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Mud
- **Other Properties:**

[]{#clay}

#######  clay
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent particles with grain
size less than 0.004 mm
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Clay
- **Other Properties:**

[]{#silt}

#######  silt
- **Child of**:
 [`mud`](#mud)
- Mud that consists of greater than 50 percent silt-size grains.
- **Alternate labels:**
loess
- **Source:**
based on SLTTs 2004; Neuendorf et al. 2005; particle size from Wentworth grade scale
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silt
- **Other Properties:**

[]{#ooze}

######  ooze
- **Child of**:
 [`biogenic sediment`](#biogenic_sediment)
 [`mud size sediment`](#mud_size_sediment)
- Neuendorf et al. 2005 put cutoff at 30 percent skeletal remains;
this is raised to 50 percent in This vocabulary for consistency with
definition of other Biogenic sediment category
- Biogenic sediment consisting of less than 1 percent gravel-size
(greater than or equal to 2 mm) particles, with a sand to mud ratio
less than 1 to 9, and less than 50 percent carbonate minerals.
- **Alternate labels:**
biogenic mud
- **Source:**
based on Bates and Jackson 1987 and Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ooze
- **Other Properties:**

[]{#carbonate_ooze}

#######  carbonate ooze
- **Child of**:
 [`carbonate mud`](#carbonate_mud)
 [`ooze`](#ooze)
- ooze that consists of more than 50 percent carbonate skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Carbonate_Ooze
- **Other Properties:**

[]{#siliceous_ooze}

#######  siliceous ooze
- **Child of**:
 [`ooze`](#ooze)
 [`silicate mud`](#silicate_mud)
- Ooze that consists of more than 50 percent siliceous skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siliceous_Ooze
- **Other Properties:**

[]{#silicate_mud}

######  silicate mud
- **Child of**:
 [`mud size sediment`](#mud_size_sediment)
- Mud size sediment that consists of less than 50 percent carbonate
minerals and less than 50 percent clastic particles.
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Silicate_Mud
- **Other Properties:**

[]{#siliceous_ooze}

#######  siliceous ooze
- **Child of**:
 [`ooze`](#ooze)
 [`silicate mud`](#silicate_mud)
- Ooze that consists of more than 50 percent siliceous skeletal
remains
- **Source:**
This vocabulary
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Siliceous_Ooze
- **Other Properties:**

[]{#non_clastic_siliceous_sediment}

#####  non clastic siliceous sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`non clastic siliceous sedimentary material`](#non_clastic_siliceous_sedimentary_material)
- Sediment that consists of at least 50 percent silicate mineral
material, deposited directly by chemical or biological processes at
the depositional surface, or in particles formed by chemical or
biological processes within the basin of deposition.
- **Source:**
NGMDB 2008; Hallsworth and Knox 1999
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Non_Clastic_Siliceous_Sediment
- **Other Properties:**

[]{#phosphate_rich_sediment}

#####  phosphate rich sediment
- **Child of**:
 [`Sediment`](#sediment)
 [`phosphate rich sedimentary material`](#phosphate_rich_sedimentary_material)
- Sediment in which at least 50 percent of the primary and/or
recrystallized constituents are phosphate minerals.
- **Source:**
SLTTs 2004
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Phosphate_Rich_Sediment
- **Other Properties:**

[]{#sand_size_sediment}

#####  sand size sediment
- **Child of**:
 [`Sediment`](#sediment)
- Sediment in which less than 30 percent of particles are gravel
(greater than 2 mm in diameter) and the sand to mud ratio is at least
1. composition or genesis of clasts not specified.
- **Source:**
Neuendorf et al. 2005 ; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Sand_Size_Sediment
- **Other Properties:**

[]{#sand}

######  sand
- **Child of**:
 [`clastic sediment`](#clastic_sediment)
 [`sand size sediment`](#sand_size_sediment)
- Clastic sediment in which less than 30 percent of particles are
gravel (greater than 2 mm in diameter) and the sand to mud ratio is at
least 1. More than half of the particles are of epiclastic origin.
- **Source:**
definition of sand from SLTTs 2004 sandy sediment; particle sizes defined from Krumbein phi scale (W C Krumbein and L L Sloss, Stratigraphy and Sedimentation, 2nd edition, Freeman, San Francisco, 1963; Krumbein and Pettijohn, 1938, Manual of Sedimentary Petrography: New York, Appleton Century Co., Inc.)
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Sand
- **Other Properties:**

[]{#tephra}

#####  Tephra
- **Child of**:
 [`Sediment`](#sediment)
 [`pyroclastic material`](#pyroclastic_material)
- Unconsolidated pyroclastic material in which greater than 75 percent
of the fragments are deposited as a direct result of volcanic
processes and the deposit has not been reworked by epiclastic
processes. Includes ash, lapilli tephra, bomb tephra, block tephra and
unconsolidated agglomerate.
- **Source:**
Hallsworth and Knox 1999; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/isample/earthenv/rocksediment/1.0/Tephra
- **Other Properties:**

[]{#ash_and_lapilli}

######  ash and lapilli
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which less than 25 percent of fragments are greater than
64 mm in longest dimension
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_And_Lapilli
- **Other Properties:**

[]{#ash_breccia_bomb_or_block_tephra}

######  ash breccia bomb or block tephra
- **Child of**:
 [`Tephra`](#tephra)
- Tephra in which more than 25 percent of particles are greater than
64 mm in largest dimension. Includes ash breccia, bomb tephra and
block tephra of Gillespie and Styles (1999)
- **Source:**
Schmid 1981; LeMaitre et al. 2002
- **Concept URI:** https://w3id.org/sesar/rocksediment/0.1/Ash_Breccia_Bomb_Or_Block_Tephra
- **Other Properties:**

[]{#soil}

####  Soil
- **Child of**:
 [`material formed in surficial environment`](#material_formed_in_surficial_environment)
 [`Natural unconsolidated material`](#natural_unconsolidated_material)
- Mixed granular mineral and organic matter modified by interaction
between earth material, biosphere, and atmosphere, consisting of
varying proportions of sand, silt, and clay, organic material such as
humus, gases, liquids, and a broad range of resident micro- and
macroorganisms. (https://en.wikipedia.org/wiki/Soil) Soil consists of
horizons near the Earth's surface that, in contrast to the underlying
parent material, have been altered by the interactions of climate,
relief, and living organisms over time. (http://www.nrcs.usda.gov/wps/
portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
(http://purl.obolibrary.org/obo/ENVO_00001998)
- **See Also**:
* [<http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280>](http://www.nrcs.usda.gov/wps/portal/nrcs/detail/soils/edu/?cid=nrcs142p2_054280)
- **Concept URI:** https://w3id.org/isample/vocabulary/material/1.0/soil
- **Other Properties:**


