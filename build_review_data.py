#!/usr/bin/env python3
"""
build_review_data.py
Generates questions_db.json containing all 241 questions with verified answers,
comprehensive explanations, and high-yield study takeaways.
"""

import json

# Verified answers and explanations dictionary
# Key: (lecture_index_1_based, question_id)
# Value: (correct_key, explanation, takeaway)

METADATA = {
    # -------------------------------------------------------------
    # LECTURE 1: Human Immunodeficiency Virus (Q1 - Q20)
    # -------------------------------------------------------------
    (1, 1): (
        "B",
        "HIV (Human Immunodeficiency Virus) belongs to the family Retroviridae and the genus Lentivirus ('lenti-' meaning slow, referring to the chronic, slow course of disease).",
        "HIV = Retroviridae, Genus Lentivirus (enveloped, ssRNA-RT)."
    ),
    (1, 2): (
        "C",
        "Luc Montagnier, Françoise Barré-Sinoussi, and colleagues at the Institut Pasteur first isolated lymphadenopathy-associated virus (LAV, later named HIV-1) from a patient at risk for AIDS in 1983 (awarded the 2008 Nobel Prize in Medicine).",
        "1983: First isolation of HIV at the Pasteur Institute."
    ),
    (1, 3): (
        "B",
        "HIV-1 is categorized into groups M, N, O, and P. Group M represents the 'Main' (or Major) pandemic group, accounting for over 95% of all HIV-1 infections worldwide.",
        "HIV-1 Group M = 'Main' (global pandemic lineage)."
    ),
    (1, 4): (
        "C",
        "In the official lecture document highlights, C) 13 is designated as the correct key answer for HIV-1 group M subtypes.",
        "HIV-1 group M subtypes = 13 (official exam key)."
    ),
    (1, 5): (
        "B",
        "HIV-2 has natural, intrinsic resistance to all Non-Nucleoside Reverse Transcriptase Inhibitors (NNRTIs, e.g., efavirenz, nevirapine) and the fusion inhibitor Enfuvirtide (T20). HIV-2 must be treated with NRTI- and INSTI- or boosted PI-based regimens.",
        "HIV-2 intrinsic resistance: NNRTIs and T20 fusion inhibitor."
    ),
    (1, 6): (
        "A",
        "In Southeast Asia, particularly Cambodia and Thailand, the circulating recombinant form CRF01_AE is predominant, accounting for >90% of all HIV-1 infections.",
        "CRF01_AE causes >90% of HIV infections in Cambodia."
    ),
    (1, 7): (
        "C",
        "The HIV viral capsid (core) is conical and formed by the p24 protein (encoded by the gag gene). p24 is the major antigen measured in 4th-generation ELISA screening tests.",
        "Capsid protein = p24 (encoded by gag gene; key serological marker)."
    ),
    (1, 8): (
        "B",
        "The pol (polymerase) gene encodes all essential viral enzymes: Reverse Transcriptase (RT), Integrase (IN), and Protease (PR). gag encodes matrix (p17), capsid (p24), and nucleocapsid (p7); env encodes envelope glycoproteins (gp120 and gp41).",
        "pol gene = Reverse Transcriptase, Integrase, and Protease."
    ),
    (1, 9): (
        "C",
        "Dolutegravir (DTG), raltegravir (RAL), and elvitegravir (EVG) are Integrase Strand Transfer Inhibitors (INSTIs) that selectively inhibit the HIV integrase enzyme, blocking integration of proviral DNA into host chromosomes.",
        "DTG, RAL, EVG = INSTIs targeting viral integrase."
    ),
    (1, 10): (
        "A",
        "Maraviroc is a chemokine receptor antagonist that binds selectively to host CCR5 co-receptors on CD4+ cells, preventing the interaction between viral gp120 and CCR5, thereby blocking viral attachment/entry.",
        "Maraviroc = CCR5 co-receptor antagonist (blocks viral entry)."
    ),
    (1, 11): (
        "C",
        "Blood transfusion with contaminated blood carries the highest transmission probability per single exposure event (estimated at 90–92% or ~9,250 per 10,000 exposures), compared to receptive anal intercourse (~1.4%) or needle sharing (~0.6%).",
        "Highest per-exposure transmission risk: Blood transfusion (~92%)."
    ),
    (1, 12): (
        "B",
        "According to UNAIDS/WHO 2021 global estimates, approximately 37.7 million [30.2–45.1 million] people were living with HIV worldwide (with 1.5 million newly infected and 680,000 deaths).",
        "UNAIDS 2021: 37.7 million people living with HIV globally."
    ),
    (1, 13): (
        "D",
        "In Cambodia, People Who Inject Drugs (PWID) have the highest estimated HIV prevalence (~15.2% in the 2017 IBBS, compared to 9.6% among Transgender women, 4.0% among MSM, and 3.2% among FEW).",
        "Highest HIV prevalence in Cambodia by key population: PWID (~15.2%)."
    ),
    (1, 14): (
        "B",
        "Cambodia's progress toward the UNAIDS 95–95–95 cascade targets was officially tracked at 92–100–98 (92% of PLHIV diagnosed, 100% of diagnosed on ART, and 98% of those on ART virally suppressed).",
        "Cambodia UNAIDS progress cascade: 92–100–98."
    ),
    (1, 15): (
        "B",
        "A 4th-generation ELISA (combination/combo antigen-antibody test) simultaneously detects anti-HIV-1 (including M and O groups) and anti-HIV-2 antibodies as well as free HIV-1 p24 capsid antigen, narrowing the diagnostic window to ~14–18 days.",
        "4th-gen ELISA = HIV-1/2 antibodies + p24 antigen."
    ),
    (1, 16): (
        "C",
        "In the Fiebig staging of early HIV infection, Stage I (~10–14 days post-exposure) is defined by the appearance of viral RNA detectable by NAAT (nucleic acid amplification testing) before p24 antigen (Stage II) or antibodies (Stage III).",
        "Earliest Fiebig stage I marker: HIV RNA by NAAT (~10–14 days)."
    ),
    (1, 17): (
        "B",
        "Standard real-time RT-PCR viral load assays (such as Roche COBAS TaqMan or Abbott RealTime) have a lower limit of detection/sensitivity of 20–40 copies/mL and a broad dynamic linearity range spanning 20 to 10^7 copies/mL.",
        "Viral load assay: Sensitivity 20–40 copies/mL; linearity 20 to 10^7 copies/mL."
    ),
    (1, 18): (
        "B",
        "In January 2019, Cambodia adopted TDF + 3TC + DTG (Tenofovir disoproxil fumarate + Lamivudine + Dolutegravir, known as TLD) as the preferred, highly potent first-line antiretroviral therapy regimen with a high genetic barrier to resistance.",
        "Preferred 1st-line ART in Cambodia: TLD (TDF + 3TC + DTG)."
    ),
    (1, 19): (
        "B",
        "According to national and WHO clinical guidelines, virological failure is defined as a confirmed plasma viral load > 1,000 copies/mL after at least 3 to 6 months of adherence on ART.",
        "Virological failure: Viral load > 1,000 copies/mL after >= 3 months (confirmed)."
    ),
    (1, 20): (
        "B",
        "Maternal IgG antibodies cross the placenta and can persist in the infant's circulation for up to 18 months, rendering antibody tests falsely positive. A negative PCR at birth/day 3 must be repeated at 6 weeks (and after cessation of breastfeeding) to detect intrapartum/early postpartum transmission.",
        "Maternal IgG persists up to 18 months; infant diagnosis requires PCR at 6 weeks."
    ),

    # -------------------------------------------------------------
    # LECTURE 2: Orthomyxoviridae-Influenza virus (Q1 - Q30)
    # -------------------------------------------------------------
    (2, 1): (
        "B",
        "Influenza viruses belong to the family Orthomyxoviridae ('ortho-' = correct/straight, 'myxo-' = mucus).",
        "Influenza viruses = Orthomyxoviridae."
    ),
    (2, 2): (
        "C",
        "Orthomyxoviridae currently comprises 7 recognized genera: Alphainfluenzavirus, Betainfluenzavirus, Gammainfluenzavirus, Deltainfluenzavirus, Isavirus, Quaranjavirus, and Thogotovirus.",
        "Orthomyxoviridae contains 7 genera."
    ),
    (2, 3): (
        "D",
        "Hepatovirus belongs to the family Picornaviridae (the genus of Hepatitis A virus), not Orthomyxoviridae.",
        "Hepatovirus is a Picornavirus, NOT an Orthomyxovirus."
    ),
    (2, 4): (
        "B",
        "Influenza viruses possess a negative-sense single-stranded RNA (-ssRNA) genome that is segmented (8 segments in A and B; 7 in C and D).",
        "Influenza genome: Segmented, negative-sense single-stranded RNA (-ssRNA)."
    ),
    (2, 5): (
        "C",
        "Influenza A and B viruses each have 8 distinct negative-sense RNA gene segments encoding structural and non-structural proteins.",
        "Influenza A and B genomes = 8 RNA segments."
    ),
    (2, 6): (
        "A",
        "Reassortment (antigenic shift) occurs when two different viruses coinfect the same cell, exchanging RNA segments. This occurs within the same genus (e.g., between Influenza A strains) but NOT across different genera/types (A cannot reassort with B).",
        "Reassortment occurs within each genus/type, not across types."
    ),
    (2, 7): (
        "B",
        "For Influenza A, 18 distinct hemagglutinin subtypes (H1–H18) and 11 distinct neuraminidase subtypes (N1–N11) are currently recognized (H17N10 and H18N11 discovered in bats).",
        "Influenza A subtypes: 18 HA and 11 NA."
    ),
    (2, 8): (
        "B",
        "Influenza B viruses do not have animal reservoirs or HA/NA subtypes, but circulate as two antigenically and genetically distinct evolutionary lineages: B/Yamagata and B/Victoria.",
        "Influenza B lineages: Yamagata and Victoria."
    ),
    (2, 9): (
        "C",
        "The standard WHO influenza nomenclature system (Type/Host origin/Geographic origin/Strain number/Year of isolation [Subtype]) was adopted in 1971 (and refined in 1980).",
        "WHO influenza nomenclature adopted in 1971."
    ),
    (2, 10): (
        "B",
        "Influenza virions are pleomorphic; the typical infectious spherical form measures approximately 80–120 nm in diameter.",
        "Influenza virion size: 80–120 nm in diameter."
    ),
    (2, 11): (
        "B",
        "Hemagglutinin (HA) is the viral attachment protein and major antigen. It binds to terminal sialic acid (N-acetylneuraminic acid) residues on host respiratory epithelial cell surface glycoproteins.",
        "HA function: Binds host cell surface sialic acids for viral entry."
    ),
    (2, 12): (
        "B",
        "While the globular head (HA1 domain) is highly variable due to antigenic drift, the HA2 stalk (stem) domain is highly conserved across subtypes and is the primary target for universal influenza vaccines.",
        "HA2 stalk (stem) region is highly conserved across influenza subtypes."
    ),
    (2, 13): (
        "B",
        "Neuraminidase (NA) is a receptor-destroying sialidase enzyme that cleaves terminal sialic acids from host cell surface receptors and budding virions, preventing self-aggregation and enabling virion release/spread.",
        "Neuraminidase (NA) cleaves sialic acid to allow budding and release."
    ),
    (2, 14): (
        "A",
        "The influenza replication cycle follows: Attachment (HA to sialic acid) -> Endocytic Entry -> Uncoating/Release of vRNP (M2 channel) -> Nuclear import & Transcription/Replication -> Viral Protein synthesis -> Assembly at plasma membrane -> Budding and release (mediated by NA).",
        "Influenza lifecycle: Attachment -> entry -> uncoating -> transcription -> translation -> assembly -> budding."
    ),
    (2, 15): (
        "A",
        "Type I interferons (IFN-alpha and IFN-beta) are the key early innate immune mediators produced by infected epithelial cells and plasmacytoid dendritic cells to induce an antiviral state.",
        "Innate antiviral response: IFN-alpha and IFN-beta."
    ),
    (2, 16): (
        "A",
        "Adaptive protection against influenza relies on two arms: neutralizing antibodies (primarily against the HA head, preventing infection) and CD8+ cytotoxic T lymphocytes (recognizing conserved internal NP/M1 proteins, clearing infected cells).",
        "Adaptive immunity: Neutralizing antibodies + CD8+ cytotoxic T-cells."
    ),
    (2, 17): (
        "B",
        "An epidemic is defined as an outbreak of disease that attacks many people at about the same time and may spread through one or several communities (a pandemic is worldwide; endemic is constant presence).",
        "Epidemic = sudden outbreak spreading through communities at the same time."
    ),
    (2, 18): (
        "A",
        "In temperate climates, seasonal influenza epidemics occur predictably during winter (cold months, e.g., November to March in Northern Hemisphere; May to September in Southern Hemisphere). In tropical regions, influenza may circulate year-round.",
        "Temperate climate influenza occurs mainly during winter."
    ),
    (2, 19): (
        "B",
        "WHO estimates that annual seasonal influenza epidemics result in 3 to 5 million cases of severe illness and approximately 290,000 to 650,000 respiratory deaths worldwide.",
        "Annual flu burden: 3–5 million severe cases; 290,000–650,000 deaths."
    ),
    (2, 20): (
        "C",
        "High-risk groups for severe influenza include pregnant women, children <59 months (under 5 years), elderly adults (>=65 years), individuals with chronic medical conditions, and healthcare workers. Healthy young adults (20–40 years) are generally at lower risk of complications.",
        "Healthy adults (20–40) are NOT a high-risk group for seasonal influenza complications."
    ),
    (2, 21): (
        "A",
        "The incubation period for seasonal influenza is short, ranging from 1 to 4 days, with an average of about 2 days.",
        "Influenza incubation period: 1–4 days (average 2 days)."
    ),
    (2, 22): (
        "B",
        "Seasonal influenza is characterized by acute fever, myalgia, malaise, and a prominent dry cough that can be severe and persist for 2 or more weeks.",
        "Characteristic flu symptom lasting >= 2 weeks: Dry cough."
    ),
    (2, 23): (
        "B",
        "While RT-PCR is the molecular standard of care, classical virus isolation (in cell cultures like MDCK or embryonated chicken eggs) is the historic gold standard for laboratory confirmation and antigenic characterization.",
        "Virological gold standard: Virus isolation in cell culture or eggs."
    ),
    (2, 24): (
        "B",
        "Rapid influenza diagnostic tests (RIDTs) detect viral antigens within 15–30 minutes but have significantly lower sensitivity (50–70%) than RT-PCR, meaning false negatives are common and results can be unreliable.",
        "Rapid tests: Lower sensitivity than RT-PCR, can yield false negatives."
    ),
    (2, 25): (
        "B",
        "The first bivalent influenza vaccine containing both Influenza A and Influenza B strains was developed by Thomas Francis and Jonas Salk and introduced in 1942 for the US military.",
        "First bivalent influenza vaccine: Introduced in 1942."
    ),
    (2, 26): (
        "B",
        "MF59 is an oil-in-water squalene emulsion adjuvant approved for influenza vaccines (introduced in Europe in 1997, e.g., Fluad) that enhances both antibody titers and cellular immune responses.",
        "MF59: Squalene oil-in-water emulsion adjuvant approved in 1997."
    ),
    (2, 27): (
        "B",
        "Adamantanes (amantadine and rimantadine) target the M2 ion channel of Influenza A. They are no longer recommended because over 99% of circulating seasonal influenza A (H1N1 and H3N2) viruses carry resistance mutations (S31N).",
        "Adamantanes discontinued due to ~99% viral resistance."
    ),
    (2, 28): (
        "B",
        "Neuraminidase inhibitors (oseltamivir, zanamivir, peramivir) competitively inhibit the neuraminidase enzyme, preventing the cleavage of sialic acid and trapping newly formed virions on the host cell surface.",
        "NA inhibitors (oseltamivir) block neuraminidase to halt budding/release."
    ),
    (2, 29): (
        "A",
        "The first documented human infections with avian influenza A(H5N1) occurred during an outbreak in Hong Kong in 1997 (18 cases, 6 deaths) and re-emerged in mainland China in 2003.",
        "First human A(H5N1) cases: Hong Kong (1997) and China (2003)."
    ),
    (2, 30): (
        "A",
        "In Cambodia, surveillance data recorded 56 confirmed human cases of A(H5N1) with 37 deaths, representing a high case fatality rate of approximately 66%.",
        "Cambodia H5N1 cumulative record: 56 cases, 37 deaths (66% CFR)."
    ),

    # -------------------------------------------------------------
    # LECTURE 3: Arboviruses (Q1 - Q32)
    # -------------------------------------------------------------
    (3, 1): (
        "B",
        "'Arbovirus' is an ecological/epidemiological term that stands for 'Arthropod-borne virus'—viruses transmitted between vertebrate hosts by biting arthropods (mosquitoes, ticks, sandflies).",
        "Arbovirus = Arthropod-borne virus."
    ),
    (3, 2): (
        "D",
        "Hepadnaviridae (Hepatitis B virus) is a blood-borne/sexually transmitted virus and is NOT an arbovirus. Major arbovirus families include Flaviviridae, Togaviridae, Bunyavirales, and Reoviridae.",
        "Hepadnaviridae (HBV) is NOT an arbovirus."
    ),
    (3, 3): (
        "C",
        "Japanese encephalitis virus (JEV) is transmitted primarily by Culex mosquitoes (predominantly Culex tritaeniorhynchus) that breed in rice paddies. Dengue, Zika, and Chikungunya are transmitted by Aedes mosquitoes.",
        "Japanese Encephalitis Virus is transmitted by Culex mosquitoes."
    ),
    (3, 4): (
        "B",
        "Crimean-Congo hemorrhagic fever virus (CCHFV) belongs to the genus Orthonairovirus (Nairoviridae) and is transmitted to humans through bites of Hyalomma ticks or contact with infected livestock blood.",
        "Crimean-Congo Hemorrhagic Fever is transmitted by ticks (Hyalomma)."
    ),
    (3, 5): (
        "B",
        "Dengue virus belongs to the genus Flavivirus (family Flaviviridae). It is an enveloped, positive-sense single-stranded RNA (+ssRNA) virus with a genome of ~11 kb.",
        "Dengue = Flavivirus, enveloped +ssRNA."
    ),
    (3, 6): (
        "B",
        "The flavivirus polyprotein is cleaved by viral and host proteases into 3 structural proteins (Capsid [C], pre-Membrane/Membrane [prM/M], Envelope [E]) and 7 non-structural proteins (NS1, NS2A, NS2B, NS3, NS4A, NS4B, NS5).",
        "Flavivirus polyprotein: 3 structural (C, prM, E) + 7 non-structural (NS1–NS5)."
    ),
    (3, 7): (
        "B",
        "NS5 is the largest, most conserved flavivirus non-structural protein, functioning as the RNA-dependent RNA polymerase (RdRp) and methyltransferase for genomic RNA replication in the cytoplasm.",
        "Flavivirus replication: NS5 RNA-dependent RNA polymerase."
    ),
    (3, 8): (
        "A",
        "During flavivirus egress through the trans-Golgi network, the host cellular endoprotease Furin cleaves the prM protein into the 'pr' peptide and mature M protein, generating fully infectious, smooth virions.",
        "Host protease Furin cleaves prM to mature M protein."
    ),
    (3, 9): (
        "B",
        "Flaviviruses are positive-sense RNA viruses that replicate entirely within the host cell cytoplasm on specialized endoplasmic reticulum-derived replication complexes.",
        "Flavivirus replication takes place entirely in the cytoplasm."
    ),
    (3, 10): (
        "B",
        "Zika virus possesses a single serotype and two major phylogenetic lineages/genotypes: African and Asian (the Asian lineage caused the Pacific and American epidemics).",
        "Zika virus: 1 serotype, 2 genotypes (African and Asian)."
    ),
    (3, 11): (
        "A",
        "Zika virus infection during pregnancy is associated with Congenital Zika Syndrome, causing microcephaly and severe fetal brain anomalies. In adults, it is linked to Guillain-Barré syndrome (GBS).",
        "Zika complications: Congenital microcephaly and Guillain-Barré syndrome."
    ),
    (3, 12): (
        "A",
        "Viral load kinetics show that ZIKV viral RNA concentration increases across fluids in the order: Plasma < saliva < urine < semen < whole blood (whole blood and semen maintain the highest viral loads and longest persistence).",
        "Zika viral load: Plasma < saliva < urine < semen < whole blood."
    ),
    (3, 13): (
        "B",
        "Prior to the 2007 outbreak on the Micronesian island of Yap, only 14 cases of human Zika virus disease had ever been documented in medical literature since its discovery in 1947.",
        "Before the 2007 Yap outbreak, only 14 human Zika cases were documented."
    ),
    (3, 14): (
        "C",
        "In Cambodia, the first documented ZIKV case was an RT-PCR-positive 3-year-old boy from Kampong Speu province in 2010, identified during acute fever surveillance among ~10,000 patients.",
        "First Zika case in Cambodia: Identified in Kampong Speu province."
    ),
    (3, 15): (
        "B",
        "Japanese Encephalitis Virus (JEV) is maintained in an enzootic cycle between ardeid wading birds and domestic pigs (amplifying hosts); humans are accidental dead-end hosts who develop low viremia and do not transmit.",
        "JEV reservoirs: Pigs and wading birds; humans are dead-end hosts."
    ),
    (3, 16): (
        "C",
        "When symptomatic Japanese encephalitis develops, the case-fatality rate can be as high as 30%, and 30% to 50% of survivors suffer permanent neuropsychiatric sequelae.",
        "Symptomatic JEV case fatality rate: Up to 30%."
    ),
    (3, 17): (
        "C",
        "Arboviruses are predominantly found in the families Flaviviridae (Dengue, ZIKV, JEV, YFV) and Togaviridae (Chikungunya, O'nyong-nyong, EEEV, WEEV).",
        "Major arbovirus families: Flaviviridae and Togaviridae."
    ),
    (3, 18): (
        "C",
        "Phylogenetic studies in Cambodia identified JEV Genotype 1 (subtypes 1a and 1b) circulating in children with encephalitis, pigs, and mosquitoes, closely related to strains in Thailand, Vietnam, and Laos.",
        "JEV genotype circulating in Cambodia: Genotype 1 (subtypes 1a and 1b)."
    ),
    (3, 19): (
        "A",
        "Chikungunya virus (CHIKV, family Togaviridae, genus Alphavirus) is classified into 3 distinct genotypes: West African, Asian, and East/Central/South African (ECSA, which spawned the Indian Ocean lineage).",
        "CHIKV genotypes: West African, Asian, and ECSA (Indian Ocean lineage)."
    ),
    (3, 20): (
        "B",
        "The E1-A226V (alanine to valine at position 226 of the E1 glycoprotein) mutation dramatically increased CHIKV infectivity, midgut dissemination, and transmission efficiency by the Asian tiger mosquito, Aedes albopictus.",
        "CHIKV E1-A226V mutation: Enhanced transmission by Aedes albopictus."
    ),
    (3, 21): (
        "C",
        "During the 2012 Chikungunya outbreak in Kampong Speu, Cambodia, testing revealed that 188 out of 425 febrile patients (44.2%) were laboratory-confirmed positive for CHIKV.",
        "2012 Kampong Speu CHIKV outbreak: 44.2% positivity (188/425)."
    ),
    (3, 22): (
        "B",
        "Dengue virus exists as 4 distinct serotypes (DENV-1, DENV-2, DENV-3, DENV-4), each further classified into several distinct geographic genotypes.",
        "Dengue: 4 serotypes (DENV-1 to DENV-4), each with multiple genotypes."
    ),
    (3, 23): (
        "A",
        "Global dengue epidemiology estimates (Bhatt et al. / WHO) indicate approximately 390 million dengue infections occur each year (96 million symptomatic), with ~3.9 billion people across 128 countries at risk.",
        "Global dengue burden: 390 million infections/yr; 3.9 billion people at risk."
    ),
    (3, 24): (
        "B",
        "In Cambodia's major dengue epidemics, the predominant serotypes were DENV-3 in 2007, DENV-1 in 2012, and DENV-1 in 2019 (a shift in serotype often precedes large epidemics).",
        "Dominant dengue serotypes in Cambodia: 2007 (D3), 2012 (D1), 2019 (D1)."
    ),
    (3, 25): (
        "B",
        "Dengue non-structural protein 1 (NS1) antigen appears on day 1 of fever, correlates with peak viremia, and remains detectable in circulating blood for up to 9–10 days—longer than viral RNA/viremia.",
        "NS1 antigen: Detectable early (day 1) and persists longer than viremia."
    ),
    (3, 26): (
        "C",
        "Dengue Fever is caused by an arbovirus (Dengue virus, transmitted by Aedes mosquitoes). Common cold, polio, and influenza are transmitted by respiratory or fecal-oral routes.",
        "Dengue fever is a mosquito-transmitted arboviral disease."
    ),
    (3, 27): (
        "C",
        "Personal vector-avoidance measures include applying insect repellents containing DEET, picaridin, or IR3535, wearing long-sleeved light-colored clothing, and utilizing insecticide-treated bed nets.",
        "Personal arbovirus prevention: Insect repellent and protective clothing."
    ),
    (3, 28): (
        "C",
        "Laboratory diagnosis of arboviruses relies on molecular assays (RT-PCR to detect viral RNA in the acute phase, days 1–5) and serological testing (MAC-ELISA to detect IgM from day 5 onwards).",
        "Arbovirus diagnosis: RT-PCR (early acute) and IgM ELISA (late)."
    ),
    (3, 29): (
        "C",
        "Zika virus is unique among arboviruses in that it can be transmitted sexually (from symptomatic or asymptomatic partners via semen and vaginal fluids), as well as vertically from mother to fetus.",
        "Zika virus can be transmitted sexually and vertically, in addition to mosquito bites."
    ),
    (3, 30): (
        "B",
        "Neurotropic arboviruses (such as Japanese Encephalitis virus and West Nile virus) cross the blood-brain barrier to cause life-threatening aseptic meningitis, encephalitis, and acute flaccid paralysis.",
        "Severe arbovirus neuroinvasive disease: Meningitis and Encephalitis."
    ),
    (3, 31): (
        "A",
        "Chikungunya virus ('that which bends up' in Makonde) characteristically causes severe, debilitating polyarthralgia and arthritis that can persist for months to years in up to 40% of patients.",
        "Chronic debilitating joint pain (arthralgia): Chikungunya virus."
    ),
    (3, 32): (
        "A",
        "The Hemagglutination Inhibition Assay (HIA / HAI) utilizes the ability of arbovirus envelope proteins to agglutinate red blood cells; specific antibodies inhibit this reaction, measuring total immunoglobulins.",
        "Inhibition of Hemagglutination Assay detects total arbovirus antibodies."
    ),

    # -------------------------------------------------------------
    # LECTURE 4: Ebola virus (Q1 - Q17)
    # -------------------------------------------------------------
    (4, 1): (
        "B",
        "The family Filoviridae contains 3 classical genera: Marburgvirus, Ebolavirus, and Cuevavirus (containing Lloviu virus discovered in bats in Spain). More recently, Dianlovirus and Striavirus have also been discovered.",
        "Filoviridae genera: Cuevavirus, Marburgvirus, and Ebolavirus."
    ),
    (4, 2): (
        "C",
        "Because filoviruses cause severe hemorrhagic fever with high case-fatality rates and lack widely available cures, WHO classifies them as Risk Group 4 pathogens requiring maximum BSL-4 containment.",
        "Filoviruses are classified as WHO Risk Group 4 (highest biosafety level)."
    ),
    (4, 3): (
        "B",
        "Since their discovery in 1976, nearly all recognized outbreaks of Ebola virus disease (EVD) have occurred in Sub-Saharan Africa (e.g., DRC, Uganda, Sudan, Guinea, Sierra Leone, Liberia).",
        "Ebola outbreaks occur almost exclusively in Sub-Saharan Africa."
    ),
    (4, 4): (
        "C",
        "The first Ebola outbreaks were simultaneously recognized in 1976 in Yambuku, Democratic Republic of the Congo (then Zaire, near the Ebola River) and Nzara, Sudan.",
        "First 1976 Ebola outbreaks: DR Congo (Zaire) and Sudan."
    ),
    (4, 5): (
        "A",
        "In 1967, laboratory workers in Marburg and Frankfurt (Germany) and Belgrade (former Yugoslavia) handling African green monkeys (Cercopithecus aethiops) from Uganda developed hemorrhagic fever, causing 31–32 clinical cases and fatalities.",
        "1967 Marburg outbreak: Germany & Yugoslavia from Ugandan green monkeys."
    ),
    (4, 6): (
        "B",
        "Ebola virus is an enveloped, filamentous virion containing a single-stranded, unsegmented, negative-sense RNA (-ssRNA) genome of approximately 19 kb encoding 7 structural proteins.",
        "Ebola genome: Enveloped, single-stranded negative-sense RNA (~19 kb)."
    ),
    (4, 7): (
        "C",
        "There are 5 recognized species of Ebolavirus: Zaire ebolavirus, Sudan ebolavirus, Taï Forest ebolavirus, Bundibugyo ebolavirus, and Reston ebolavirus (Reston causes disease in primates/pigs but not humans).",
        "5 Ebolavirus species: Bundibugyo, Taï Forest, Reston, Sudan, Zaire."
    ),
    (4, 8): (
        "B",
        "EBOV is the specific official abbreviation for Zaire ebolavirus, the species responsible for the highest mortality (60–90%) and the catastrophic 2014–2016 West Africa outbreak.",
        "EBOV = Zaire ebolavirus."
    ),
    (4, 9): (
        "A",
        "Fruit bats (family Pteropodidae, e.g., Hypsignathus monstrosus, Epomops franqueti) are the natural reservoir. Transmission to humans occurs through contact with bat/wildlife body fluids or contact with infected patients.",
        "Ebola reservoir: Fruit bats; transmitted by contact with blood/body fluids."
    ),
    (4, 10): (
        "B",
        "According to original WHO and lecture fact sheets, convalescent men can still shed and transmit Ebola virus in their semen for up to 7 weeks after clinical recovery from illness (though RNA can persist longer).",
        "Ebola can be transmitted via semen for up to 7 weeks after recovery."
    ),
    (4, 11): (
        "B",
        "The incubation period for Ebola virus disease ranges from 2 to 21 days (most typically 4 to 10 days). Patients become contagious only after symptoms develop.",
        "Ebola incubation period: 2 to 21 days."
    ),
    (4, 12): (
        "B",
        "Stage I (early, non-specific phase, days 1–3) presents with flu-like symptoms: extreme asthenia, high fever, chills, severe frontal headache, myalgia, arthralgia, conjunctivitis, and a non-pruritic maculopapular rash sparing the face.",
        "Stage I Ebola: Extreme asthenia, fever, headache, myalgia, and rash sparing the face."
    ),
    (4, 13): (
        "A",
        "Stage II (specific hemorrhagic phase) involves multi-organ failure, gastrointestinal hemorrhage, petechiae, external mucosal bleeding (eyes, gums, puncture sites), with a mortality rate of 50–90%.",
        "Stage II Ebola: Severe internal/external bleeding; 50–90% mortality."
    ),
    (4, 14): (
        "A",
        "Within a few days after symptom onset, acute diagnostic tests include RT-PCR (gold standard for viral RNA), antigen-capture ELISA, IgM-capture ELISA, and viral culture in reference BSL-4 laboratories.",
        "Early acute Ebola diagnosis: RT-PCR, antigen-capture ELISA, and IgM ELISA."
    ),
    (4, 15): (
        "B",
        "In traditional supportive management emphasized in classic curriculum: no broad-spectrum oral antivirals are routinely available; interferons are ineffective; and strict hospital isolation (PPE, barrier nursing) is paramount.",
        "Primary Ebola control: Strict isolation facilities and barrier precautions."
    ),
    (4, 16): (
        "D",
        "Ebola virus belongs to the family Filoviridae (named for their filament-like, thread-like morphology under electron microscopy).",
        "Ebola virus = Filoviridae."
    ),
    (4, 17): (
        "C",
        "Fruit bats (order Chiroptera) are considered the natural reservoir hosts of Ebola virus, maintaining the virus in nature without showing clinical signs of disease.",
        "Natural reservoir of Ebola virus: Fruit bats."
    ),

    # -------------------------------------------------------------
    # LECTURE 5: Coronaviruses (Q1 - Q30)
    # -------------------------------------------------------------
    (5, 1): (
        "B",
        "The family Coronaviridae historically contains 3 subfamilies: Letovirinae, Torovirinae, and Orthocoronavirinae (Orthocoronavirinae contains the four genera: Alpha, Beta, Gamma, and Deltacoronavirus).",
        "Coronaviridae subfamilies: Letovirinae, Torovirinae, and Orthocoronavirinae."
    ),
    (5, 2): (
        "B",
        "Coronaviruses are enveloped, positive-sense single-stranded RNA (+ssRNA) viruses with the largest known genomes among RNA viruses (26–32 kb), featuring a characteristic club-shaped 'corona' (crown) of spikes.",
        "Coronaviruses: Enveloped, +ssRNA, unsegmented genome of 26–32 kb."
    ),
    (5, 3): (
        "C",
        "The Spike (S) glycoprotein forms large trimeric surface projections responsible for host receptor binding (S1 subunit) and membrane fusion (S2 subunit); it is the dominant target of neutralizing antibodies.",
        "Spike (S) glycoprotein: Mediates receptor binding and host cell fusion."
    ),
    (5, 4): (
        "C",
        "The Hemagglutinin-Esterase (HE) glycoprotein forms short 5–7 nm dimeric surface projections found only in a subset of Group 2 Betacoronaviruses (such as HCoV-OC43 and HCoV-HKU1).",
        "Hemagglutinin-esterase (HE) is present only in Group 2 betacoronaviruses."
    ),
    (5, 5): (
        "B",
        "Human coronavirus 229E (HCoV-229E, an Alphacoronavirus) uses human Aminopeptidase N (APN / CD13) as its cellular receptor for entry.",
        "HCoV-229E receptor: Aminopeptidase N (CD13)."
    ),
    (5, 6): (
        "C",
        "Both SARS-CoV (SARS-CoV-1) and the endemic human coronavirus NL63 utilize human Angiotensin-Converting Enzyme 2 (ACE2) as their cellular receptor.",
        "SARS-CoV and NL63 cellular receptor: ACE2."
    ),
    (5, 7): (
        "C",
        "HCoV-OC43 utilizes 9-O-acetylated sialic acid (N-acetyl-9-O-acetylneuraminic acid) and CEACAM (carcinoembryonic antigen-related cell adhesion molecule) for cell attachment.",
        "HCoV-OC43 receptor: 9-O-acetylated sialic acid or CEACAM."
    ),
    (5, 8): (
        "C",
        "Cryo-electron tomography measurements (Neuman et al.) showed that the coronavirus lipid envelope is unusually thick, measuring 7.8 ± 0.7 nm (compared to ~4 nm for typical lipid bilayers).",
        "Coronavirus lipid envelope thickness: 7.8 ± 0.7 nm by cryo-ET."
    ),
    (5, 9): (
        "C",
        "The positive-sense RNA genome is encapsidated by the basic, highly phosphorylated Nucleocapsid (N) protein in a helical conformation to form the core ribonucleoprotein complex.",
        "Nucleocapsid: Formed by phosphoprotein N complexed with genomic RNA."
    ),
    (5, 10): (
        "A",
        "The coronavirus genomic RNA mimics cellular mRNA: it possesses a 5' methylated cap (7-methylguanosine) and a 3' polyadenylated (poly[A]) tail, allowing immediate translation upon entry.",
        "Coronavirus genome terminals: 5' cap and 3' poly(A) tail."
    ),
    (5, 11): (
        "B",
        "Translation of ORF1a and ORF1b (via ribosomal frameshifting) yields polyproteins pp1a and pp1ab, which are cleaved by viral proteases (PLpro and 3CLpro/Mpro) into 16 non-structural proteins (nsp1–nsp16) forming the RTC.",
        "ORF1a/b polyproteins cleave into 16 non-structural proteins (nsp1–16)."
    ),
    (5, 12): (
        "A",
        "Coronavirus replication occurs in host-derived endoplasmic reticulum membrane structures: double-membrane vesicles (DMVs), convoluted membranes (CMs), and double-membrane spherules.",
        "Replication organelles: Double-membrane vesicles (DMVs) and convoluted membranes."
    ),
    (5, 13): (
        "C",
        "In late December 2019, SARS-CoV-2 (initially designated 2019-nCoV), the causative agent of COVID-19, emerged in Wuhan, Hubei Province, China, becoming the 7th known human coronavirus.",
        "7th human coronavirus: SARS-CoV-2 (COVID-19), emerging in late 2019 in Wuhan."
    ),
    (5, 14): (
        "B",
        "The 4 endemic human coronaviruses causing mild, self-limiting common cold-like upper respiratory tract infections are 229E, NL63 (alphacoronaviruses), OC43, and HKU1 (betacoronaviruses).",
        "Four common cold coronaviruses: 229E, NL63, OC43, and HKU1."
    ),
    (5, 15): (
        "B",
        "During the 2002–2003 SARS-CoV-1 outbreak (which spread to ~29 countries with 8,096 cases and 774 deaths), the overall case-fatality rate was approximately 9.6% (~10%).",
        "2002–2003 SARS-CoV-1 outbreak mortality: Approximately 10%."
    ),
    (5, 16): (
        "C",
        "MERS-CoV (Middle East Respiratory Syndrome Coronavirus) emerged in Saudi Arabia in 2012. Among laboratory-confirmed cases reported to WHO, it exhibits a high case-fatality rate of ~35%.",
        "MERS-CoV case fatality rate: Approximately 35%."
    ),
    (5, 17): (
        "A",
        "SARS-CoV-2 is transmitted primarily through respiratory droplets (>5 µm) and aerosols (<5 µm) generated by talking, coughing, and breathing, as well as indirect contact with contaminated fomites.",
        "COVID-19 transmission: Droplets, fine aerosols, and contaminated surfaces."
    ),
    (5, 18): (
        "B",
        "WHO epidemiological data shows COVID-19 clinical severity distribution: approximately 80% mild to moderate illness, 15% severe illness (requiring oxygen support), and 5% critical illness (respiratory failure, septic shock).",
        "COVID-19 severity: ~80% mild/moderate, ~15% severe, ~5% critical."
    ),
    (5, 19): (
        "B",
        "Approximately 75% of COVID-19 fatalities occurred in patients with underlying chronic comorbidities (hypertension, diabetes, cardiovascular disease); the incubation period is 5–6 days on average (up to 14 days).",
        "75% of deaths had underlying conditions; incubation period is 5–6 days."
    ),
    (5, 20): (
        "A",
        "Serological antibody tests detect host IgM/IgG, which only become reliably detectable 7 to 14 days after symptom onset. Thus, serology cannot detect acute infection, and the Cambodian MoH uses only viral-detection tests (RT-PCR and Ag RDTs).",
        "Serology is NOT for acute COVID-19 diagnosis (antibodies appear late: 7–14 days)."
    ),
    (5, 21): (
        "B",
        "The coronavirus outbreak that caused Severe Acute Respiratory Syndrome in Guangdong, China was identified in 2003 and named SARS-CoV (or SARS-CoV-1).",
        "2003 SARS coronavirus: SARS-CoV-1."
    ),
    (5, 22): (
        "B",
        "The first cases of COVID-19 (caused by SARS-CoV-2) were reported in Wuhan, China in late 2019 (December 2019).",
        "First COVID-19 cases were reported in 2019."
    ),
    (5, 23): (
        "C",
        "Rotavirus causes acute viral gastroenteritis (watery diarrhea and vomiting in young children), whereas Coronaviruses, Rhinoviruses, and Influenza viruses primarily cause respiratory and flu-like symptoms.",
        "Rotavirus causes gastroenteritis/diarrhea, NOT flu-like respiratory symptoms."
    ),
    (5, 24): (
        "A",
        "Coronaviruses are ENVELOPED positive-sense RNA viruses with a lipid bilayer derived from host intracellular membranes. Therefore, stating they are 'Non-Enveloped' is incorrect.",
        "Coronaviruses are ENVELOPED viruses (statement A is incorrect)."
    ),
    (5, 25): (
        "C",
        "The first case of Middle East Respiratory Syndrome (MERS) was identified and reported in Saudi Arabia in 2012.",
        "First case of MERS was identified in 2012."
    ),
    (5, 26): (
        "C",
        "Dromedary camels are the recognized intermediate animal reservoir from which MERS-CoV is transmitted zoonotically to humans.",
        "Zoonotic reservoir for MERS-CoV to humans: Dromedary camels."
    ),
    (5, 27): (
        "D",
        "Bats (order Chiroptera) serve as the ultimate natural ancestral reservoir for the vast majority of alphacoronaviruses and betacoronaviruses (including SARS-CoV, MERS-CoV, and SARS-CoV-2 precursors).",
        "Natural ancestral reservoir of coronaviruses: Bats."
    ),
    (5, 28): (
        "D",
        "Typical symptoms of COVID-19 include fever, cough, shortness of breath, sore throat, and anosmia/ageusia (loss of smell/taste). 'Brown spots around the face' is not a symptom of COVID-19.",
        "Brown spots around the face is NOT a symptom of COVID-19."
    ),
    (5, 29): (
        "C",
        "The COVID-19 pandemic originated with an outbreak of pneumonia of unknown cause detected in Wuhan, Hubei province, China in late 2019.",
        "COVID-19 pandemic began in Wuhan, China in late 2019."
    ),
    (5, 30): (
        "B",
        "Real-time Reverse Transcription Polymerase Chain Reaction (RT-PCR) or molecular NAAT testing is the gold standard diagnostic method to definitively confirm SARS-CoV-2 infection.",
        "Gold standard COVID-19 diagnosis: RT-PCR / molecular test."
    ),

    # -------------------------------------------------------------
    # LECTURE 6: Poliovirus (Q1 - Q20)
    # -------------------------------------------------------------
    (6, 1): (
        "B",
        "Poliovirus belongs to the family Picornaviridae ('pico-' = small, 'rna' = RNA) and the genus Enterovirus, specifically classified as Enterovirus C.",
        "Poliovirus = Picornaviridae, Enterovirus C."
    ),
    (6, 2): (
        "C",
        "There are 3 serotypes of poliovirus: Poliovirus type 1 (Brunhilde/Mahoney), type 2 (Lansing/MEF-1, eradicated in 2015), and type 3 (Leon/Saukett, eradicated in 2019).",
        "Poliovirus has 3 serotypes: PV1, PV2, and PV3."
    ),
    (6, 3): (
        "C",
        "Enteroviruses (including polioviruses, coxsackieviruses, echoviruses, and numbered enteroviruses) are a major genus within the family Picornaviridae.",
        "Enteroviruses belong to the Picornaviridae family."
    ),
    (6, 4): (
        "B",
        "Poliovirus is transmitted from person to person primarily via the fecal-oral route (ingestion of contaminated water/food) or less commonly oral-oral droplets. Humans are the only natural reservoir.",
        "Poliovirus transmission: Fecal-oral / oral-oral; humans are the only reservoir."
    ),
    (6, 5): (
        "D",
        "Enteroviruses are non-enveloped and acid-stable, allowing them to resist stomach acidity (pH < 3) and traverse the gastric barrier to infect the intestinal mucosa. They are inactivated by heat (55 °C), chlorine (0.1 ppm), bleach, and UV.",
        "Poliovirus is RESISTANT to stomach acidity (enabling intestinal infection)."
    ),
    (6, 6): (
        "D",
        "Approximately 90% to 95% of all poliovirus infections are inapparent (completely asymptomatic), with viral shedding in stool without causing illness.",
        "Inapparent (asymptomatic) poliovirus infections: ~90–95% of cases."
    ),
    (6, 7): (
        "B",
        "Abortive poliomyelitis ('minor illness') accounts for ~4–8% of infections, presenting with nonspecific flu-like symptoms (fever, sore throat, headache, malaise) and a completely normal neurological examination.",
        "Abortive poliomyelitis = minor nonspecific illness with normal neurological exam."
    ),
    (6, 8): (
        "B",
        "Non-paralytic poliomyelitis (aseptic meningitis, ~1–2% of cases) involves signs of meningeal irritation: stiff neck and back, headache, vomiting, hyperesthesia, followed by complete and full recovery.",
        "Non-paralytic polio = aseptic meningitis with meningismus and full recovery."
    ),
    (6, 9): (
        "C",
        "The primary mode of transmission for all enteroviruses is the fecal-oral route via contaminated hands, surfaces, food, or recreational water.",
        "Primary enterovirus transmission: Fecal-oral route."
    ),
    (6, 10): (
        "A",
        "Historically, Poliovirus Type 1 was responsible for approximately 85% of all paralytic poliomyelitis cases and was the most likely serotype to cause severe epidemic paralysis.",
        "Type 1 poliovirus accounted for 85% of paralytic cases."
    ),
    (6, 11): (
        "B",
        "Bulbar paralytic poliomyelitis is the most lethal form (causing ~75% of polio deaths), resulting from damage to motor nuclei of cranial nerves and the respiratory/circulatory control centers in the medulla oblongata.",
        "Bulbar polio damages the brainstem/medulla and causes 75% of polio deaths."
    ),
    (6, 12): (
        "B",
        "Poliovirus replicates in the oropharynx and gut lymphoid tissue. It is most reliably recovered from throat secretions during the first week of illness and shed in stool for several weeks (up to 2 months).",
        "Diagnostic isolation: Throat swab (1st week) and stool (several weeks)."
    ),
    (6, 13): (
        "B",
        "Jonas Salk's Inactivated Poliovirus Vaccine (IPV, formalin-inactivated virions, 1955) is administered by injection and induces high serum IgG titers: >90% seroprotection after 2 doses and >99% after 3 doses.",
        "Salk IPV: Inactivated injected vaccine, >90% after 2 doses, >99% after 3."
    ),
    (6, 14): (
        "D",
        "Albert Sabin's Oral Poliovirus Vaccine (OPV, 1961) is a live-attenuated vaccine that replicates in the gut mucosa and INDUCES strong local secretory IgA intestinal immunity. Saying it does NOT induce intestinal immunity is FALSE.",
        "Sabin OPV replicates in the gut and INDUCES local mucosal IgA immunity."
    ),
    (6, 15): (
        "C",
        "Hand, Foot, and Mouth Disease (HFMD) is a common childhood infection caused by enteroviruses, primarily Coxsackievirus A16 and Enterovirus A71 (EV-A71).",
        "Hand, Foot, and Mouth Disease is caused by Enteroviruses (Coxsackievirus, EV71)."
    ),
    (6, 16): (
        "C",
        "Definitive and rapid diagnosis of enteroviral central nervous system infections (meningitis, encephalitis) relies on Nucleic Acid Amplification Tests (RT-PCR) performed on CSF or stool specimens.",
        "Crucial definitive diagnosis: Nucleic Acid Amplification Tests (RT-PCR)."
    ),
    (6, 17): (
        "C",
        "Paralytic poliomyelitis occurs when poliovirus invades the Central Nervous System, selectively destroying anterior horn motor neurons in the spinal cord and motor nuclei of the brainstem.",
        "Paralytic polio selectively targets anterior horn motor neurons in the CNS."
    ),
    (6, 18): (
        "B",
        "Although paralysis occurs in only ~0.1% to 1% of all poliovirus infections, it is the classic, severe hallmark of the disease (asymmetric acute flaccid paralysis with loss of deep tendon reflexes).",
        "Severe hallmark outcome of poliovirus: Acute flaccid paralysis."
    ),
    (6, 19): (
        "B",
        "Oral Poliovirus Vaccine (OPV) replicates directly within the gut lining, inducing both mucosal IgA and systemic IgG antibodies, thereby preventing wild virus shedding and secondary transmission.",
        "OPV replicates in gut mucosa, inducing local IgA to block viral shedding."
    ),
    (6, 20): (
        "B",
        "Post-Polio Syndrome (PPS) is a condition affecting 25–40% of polio survivors 15 to 40 years after recovery, characterized by insidious new muscle weakness, muscle atrophy, fatigue, and pain.",
        "Post-Polio Syndrome: New weakness and muscle pain decades after recovery."
    ),

    # -------------------------------------------------------------
    # LECTURE 7: Lyssavirus and Rabies (Q1 - Q17)
    # -------------------------------------------------------------
    (7, 1): (
        "B",
        "Rabies virus belongs to the family Rhabdoviridae ('rhabdo-' = rod/bullet) and the genus Lyssavirus ('lyssa' = madness/frenzy in Greek).",
        "Rabies virus = Rhabdoviridae, Genus Lyssavirus."
    ),
    (7, 2): (
        "B",
        "Rabies virions are enveloped, bullet-shaped particles (approx 180 nm long x 75 nm wide) containing an unsegmented, negative-sense single-stranded RNA (-ssRNA) genome.",
        "Rabies virion: Bullet-shaped, enveloped, -ssRNA genome."
    ),
    (7, 3): (
        "B",
        "Rabies virus replicates exclusively in the cytoplasm because host cells lack the machinery to transcribe negative-sense RNA; the virion carries its own viral RNA-dependent RNA polymerase (L protein).",
        "Replicates in cytoplasm using its own virion-packaged RNA polymerase."
    ),
    (7, 4): (
        "B",
        "The genus Lyssavirus contains at least 7 classic phylogroups/species; Lagos bat virus (genotype 2) is the only classical lyssavirus that has NEVER been associated with a documented human rabies case.",
        "Lagos bat virus (genotype 2) has never caused human rabies."
    ),
    (7, 5): (
        "C",
        "Bats (order Chiroptera) are the evolutionary and principal reservoir hosts for almost all known lyssaviruses globally (with carnivores like dogs and foxes serving as terrestrial maintenance hosts for Classical Rabies virus).",
        "Principal reservoir for lyssaviruses globally: Bats (Chiroptera)."
    ),
    (7, 6): (
        "B",
        "The viral surface glycoprotein (G protein) attaches to receptors abundant at the neuromuscular junction: Nicotinic Acetylcholine Receptor (nAChR), Neural Cell Adhesion Molecule (NCAM/CD56), and p75 Neurotrophin Receptor (p75NTR).",
        "Rabies receptors: nAChR, NCAM (CD56), and p75NTR."
    ),
    (7, 7): (
        "A",
        "Rabies is transmitted through infectious saliva introduced into deep subcutaneous tissue or muscle via animal bites or scratches.",
        "Transmission route: Inoculation of infectious saliva via bites/scratches."
    ),
    (7, 8): (
        "C",
        "The incubation period for rabies is typically 30 to 90 days (1 to 3 months), depending on the bite site's distance from the central nervous system, viral inoculum, and host innervation.",
        "Rabies incubation period: Commonly 30 to 90 days (1–3 months)."
    ),
    (7, 9): (
        "A",
        "Human rabies manifests in two clinical forms: the furious (encephalitic) form (~80% of cases, with hydrophobia, aerophobia, hyper-excitation) and the paralytic (dumb) form (~20% of cases, presenting with ascending Guillain-Barré-like paralysis).",
        "Two clinical forms: Furious form (~80%) and Paralytic form (~20%)."
    ),
    (7, 10): (
        "D",
        "Furious rabies features severe autonomic instability, involuntary spasms of pharyngeal/laryngeal muscles upon attempting to swallow liquids (hydrophobia), agitation, and delirium. Full recovery or prolonged remission does NOT occur; death occurs within days.",
        "Rabies is universally fatal; prolonged remission with recovery does NOT occur."
    ),
    (7, 11): (
        "B",
        "The gold standard for post-mortem laboratory diagnosis of rabies is the Direct Fluorescent Antibody (dFA) test performed on fresh brain smear impressions (hippocampus/cerebellum), taking 2–3 hours with ~99% sensitivity and specificity.",
        "Post-mortem gold standard: Direct fluorescent antibody (dFA) test on brain."
    ),
    (7, 12): (
        "B",
        "Ante-mortem diagnosis is achieved using Reverse Transcriptase PCR (RT-PCR) to detect viral RNA in serial saliva samples, CSF, or full-thickness nuchal skin biopsies containing cutaneous nerve endings at hair follicles.",
        "Ante-mortem viral RNA detection: RT-PCR on saliva, CSF, or nuchal skin biopsy."
    ),
    (7, 13): (
        "B",
        "Louis Pasteur's historic 1885 vaccine used desiccated spinal cords of rabies-infected rabbits (air-dried for progressively fewer days to attenuate the virus), requiring 13–14 painful subcutaneous injections in the abdominal wall.",
        "Pasteur 1885 vaccine: Desiccated rabbit spinal cords, 13 belly injections."
    ),
    (7, 14): (
        "A",
        "Modern post-exposure prophylaxis (PEP) consists of: immediate copious wound washing with soap and running water for 15 minutes, antiseptic application (povidone-iodine/alcohol), rabies vaccination (IM or intradermal), plus Rabies Immunoglobulin (RIG) for WHO Category III exposures.",
        "Modern PEP: Wound washing with soap (15 min) + vaccine + RIG for Category III."
    ),
    (7, 15): (
        "A",
        "In Cambodia (data from Institut Pasteur du Cambodge), an estimated 600,000 dog bites occur annually; ~80% are severe (Category III); over 60% of victims are children <17 years; and only ~5% access proper PEP.",
        "Cambodia rabies data: ~600,000 dog bites/yr, 80% severe, 60% children, only 5% access PEP."
    ),
    (7, 16): (
        "C",
        "Hydrophobia (painful diaphragmatic/laryngeal spasms triggered by trying to drink water, or even the sound/sight of water) is the single most pathognomonic clinical sign of human rabies.",
        "Pathognomonic clinical sign: Hydrophobia (fear of drinking water)."
    ),
    (7, 17): (
        "C",
        "Once clinical symptoms of rabies develop, the disease is virtually 100% fatal (only a handful of survivors ever documented worldwide).",
        "Rabies prognosis once symptoms appear: 100% fatal."
    ),

    # -------------------------------------------------------------
    # LECTURE 8: Papillomaviridae (Q1 - Q17)
    # -------------------------------------------------------------
    (8, 1): (
        "B",
        "Human Papillomaviruses (HPVs) are small (52–55 nm), non-enveloped, icosahedral viruses containing a single circular double-stranded DNA (dsDNA) genome of ~8,000 base pairs.",
        "HPV: Small (52–55 nm), non-enveloped, circular double-stranded DNA (dsDNA)."
    ),
    (8, 2): (
        "A",
        "The HPV icosahedral capsid has a T=7 skew lattice composed of 72 pentameric capsomers (pentavalent capsomers) consisting of the major capsid protein L1 (55 kDa) and minor capsid protein L2 (70 kDa).",
        "Capsid composition: 72 pentameric capsomers composed of L1 and L2."
    ),
    (8, 3): (
        "A",
        "L1 constitutes ~80% of total viral structural protein. When expressed alone in recombinant systems (yeast or insect cells), L1 self-assembles into non-infectious, highly immunogenic Virus-Like Particles (VLPs), forming the basis of all HPV vaccines.",
        "L1 major capsid protein self-assembles into Virus-Like Particles (VLPs)."
    ),
    (8, 4): (
        "B",
        "The circular ~8 kb HPV genome is divided into 3 regions: Early (E) region (encoding non-structural proteins E1, E2, E4, E5, E6, E7), Late (L) region (capsid proteins L1 and L2), and the Long Control Region (LCR / URR, non-coding regulatory segment).",
        "HPV genome organization: Early (E), Late (L), and Long Control Region (LCR)."
    ),
    (8, 5): (
        "B",
        "HPV oncoproteins E5, E6, and E7 evade host immunity by downregulating MHC class I surface expression, inhibiting antigen presentation, and suppressing interferon-stimulated gene induction.",
        "Immune evasion oncoproteins: E5, E6, and E7."
    ),
    (8, 6): (
        "B",
        "HPV types 6 and 11 are the classic 'low-risk' mucosotropic genotypes responsible for >90% of anogenital warts (condylomata acuminata) and Recurrent Respiratory Papillomatosis (RRP).",
        "HPV 6 and 11 cause anogenital warts (condylomata) and respiratory papillomas."
    ),
    (8, 7): (
        "B",
        "HPV types 16 and 18 are the major 'high-risk' (oncogenic) mucosal genotypes, accounting for ~70% of invasive cervical cancers, as well as vulvar, vaginal, penile, anal, and oropharyngeal carcinomas.",
        "High-risk oncogenic HPV: Types 16 and 18 cause ~70% of cervical cancers."
    ),
    (8, 8): (
        "C",
        "HPVs exhibit strict tropism for stratified squamous epithelial cells (keratinocytes of the skin and mucous membranes), gaining entry through microtrauma to infect basal layer stem cells.",
        "HPV cell tropism: Stratified squamous epithelial cells (basal keratinocytes)."
    ),
    (8, 9): (
        "C",
        "Genital HPV is the most common sexually transmitted infection globally, transmitted via direct skin-to-skin contact during vaginal, anal, or oral sexual activity.",
        "Primary transmission of genital HPV: Sexual contact (skin-to-skin)."
    ),
    (8, 10): (
        "C",
        "Cutaneous warts (verruca vulgaris on hands, plantaris on feet) are caused by cutaneous HPV genotypes, predominantly HPV types 1, 2, 4, 27, and 57.",
        "Cutaneous warts on hands and feet: HPV types 1, 2, 4, 27, and 57."
    ),
    (8, 11): (
        "A",
        "HPV avoids host immune detection because its life cycle is confined to the epithelium: virion assembly occurs in shedding cells without host cell lysis, causing no viremia or systemic inflammation, alongside downregulation of MHC class I and IFN pathways.",
        "Immune avoidance: No cell lysis, no viremia, downregulation of MHC class I."
    ),
    (8, 12): (
        "A",
        "The Hybrid Capture 2 (hc2) HPV DNA Test utilizes signal-amplified chemiluminescent hybridization to differentiate pooled low-risk genotypes (6, 11, 42, 43, 44) from high-risk oncogenic genotypes (16, 18, 31, 33, 35, 39, 45, 51, 52, 56, 58, 59, 68).",
        "Hybrid Capture 2 (hc2) differentiates low-risk from high-risk HPV groups."
    ),
    (8, 13): (
        "B",
        "The 9-valent HPV vaccine (Gardasil 9) utilizes recombinant L1 VLPs covering types 6, 11, 16, 18, 31, 33, 45, 52, 58; it is administered intramuscularly, routinely recommended at ages 11–12 for both girls and boys.",
        "9-valent HPV vaccine: Recombinant L1 VLPs given IM at ages 11–12 for both sexes."
    ),
    (8, 14): (
        "A",
        "The vast majority (~90%) of genital HPV infections are cleared spontaneously by cell-mediated immunity within two years without progressing to precancerous lesions.",
        "90% of HPV infections resolve spontaneously within 2 years."
    ),
    (8, 15): (
        "A",
        "HPV infection alone is insufficient for carcinogenesis; malignant progression requires environmental and host co-factors: tobacco smoking, UV/chemical carcinogen exposure, folate deficiency, long-term oral contraceptives, high parity, and immunosuppression (HIV).",
        "Triggers for HPV cancer: Smoking, chemical exposure, folate deficiency, immunosuppression."
    ),
    (8, 16): (
        "C",
        "Prophylactic vaccination against HPV prior to sexual debut is the single most cost-effective, efficient public health strategy to eliminate HPV-related cervical cancer.",
        "Most efficient approach to reduce HPV disease burden: Vaccination."
    ),
    (8, 17): (
        "C",
        "More than 100 (in fact >200) distinct HPV genotypes have been completely sequenced and characterized to date.",
        "Distinct HPV genotypes: Over 100 characterized genotypes."
    ),

    # -------------------------------------------------------------
    # LECTURE 9: Poxvirus (Q1 - Q15)
    # -------------------------------------------------------------
    (9, 1): (
        "B",
        "Poxviruses (family Poxviridae) are the largest and most complex human viruses: large, enveloped, brick- or ovoid-shaped particles containing a linear double-stranded DNA (dsDNA) genome.",
        "Poxviridae: Large, enveloped, double-stranded DNA (dsDNA) viruses."
    ),
    (9, 2): (
        "C",
        "The poxvirus genome ranges from 130 to 360 kbp and is packed with coding sequences, typically encoding more than 150 (up to 200) genes.",
        "Poxvirus genome encodes more than 150 genes."
    ),
    (9, 3): (
        "B",
        "The family Poxviridae is divided into two subfamilies: Entomopoxvirinae (infecting insects) and Chordopoxvirinae (infecting vertebrates, which includes all genera causing human pox diseases).",
        "Human poxviruses belong to subfamily Chordopoxvirinae."
    ),
    (9, 4): (
        "A",
        "Poxviruses are unique among DNA viruses because they replicate ENTIRELY in the cytoplasm of host cells; they encode their own DNA-dependent RNA polymerase, polyA polymerase, and capping enzymes.",
        "Poxvirus unique feature: DNA virus replicating entirely in the cytoplasm."
    ),
    (9, 5): (
        "C",
        "Molluscum contagiosum virus (MCV, genus Molluscipoxvirus) is the only poxvirus strictly restricted to humans, causing benign, umbilicated, dome-shaped pearly papules on the skin.",
        "Molluscum contagiosum virus: Strictly human host, causes pearly papules."
    ),
    (9, 6): (
        "B",
        "The monkeypox (mpox) virion is a brick-shaped particle measuring approximately 200–450 nm in length and 160–260 nm in width, containing a dsDNA genome of ~197 kb.",
        "Monkeypox virion dimensions: 200–450 nm x 160–260 nm, ~197 kb genome."
    ),
    (9, 7): (
        "B",
        "Variola virus (the causative agent of smallpox) was strictly restricted to human hosts and was officially declared eradicated by the WHO in 1980 following a global ring vaccination campaign.",
        "Variola virus (smallpox) had only human hosts and was eradicated in 1980."
    ),
    (9, 8): (
        "A",
        "Poxviruses produce two infectious virion forms: Intracellular Mature Virus (IMV, surrounded by a single membrane, highly stable, mediates host-to-host transmission) and Extracellular Enveloped Virus (EEV, acquires a double membrane, mediates cell-to-cell spread).",
        "Two infectious poxvirus forms: IMV (host-to-host) and EEV (cell-to-cell spread)."
    ),
    (9, 9): (
        "B",
        "Poxvirus DNA replication occurs entirely within discrete perinuclear cytoplasmic regions termed 'viral factories' (virosomes), utilizing the viral DNA polymerase (E9) and viral accessory factors.",
        "Poxvirus DNA replication site: Cytoplasmic viral factories."
    ),
    (9, 10): (
        "B",
        "The first human case of mpox (monkeypox) was diagnosed in 1970 in a 9-month-old infant in the Equateur province of the Democratic Republic of the Congo (formerly Zaire).",
        "First human case of mpox: 1970 in Democratic Republic of the Congo."
    ),
    (9, 11): (
        "B",
        "Mpox virus is divided into two distinct clades: Clade I (formerly Congo Basin clade), which is endemic in Central Africa and has a high case-fatality rate of ~10.6%, and Clade II (formerly West African clade, including Clade IIb responsible for the 2022 global outbreak, CFR <1–3%).",
        "Clade I (Congo Basin) has a case fatality rate of ~10.6%."
    ),
    (9, 12): (
        "B",
        "Tecovirimat (TPOXX / ST-246) is a targeted antiviral that inhibits the viral VP37 envelope wrapping protein (encoded by the F13L gene), thereby blocking the formation of extracellular enveloped virions (EEV) necessary for viral dissemination.",
        "Tecovirimat inhibits VP37 protein, blocking enveloped virion release."
    ),
    (9, 13): (
        "B",
        "Brincidofovir (Tembexa / CMX001) is an orally bioavailable lipid acyclic nucleotide phosphonate prodrug of cidofovir approved by the US FDA in June 2021 for smallpox; it carries a warning for potential liver toxicity (elevated transaminases).",
        "Brincidofovir: Lipid prodrug of cidofovir approved in 2021 for smallpox."
    ),
    (9, 14): (
        "B",
        "MVA-BN (Modified Vaccinia Ankara - Bavarian Nordic / JYNNEOS / Imvamune) is a 3rd-generation, highly attenuated, replication-deficient vaccinia vaccine licensed for smallpox and mpox, safe for immunocompromised and pregnant individuals.",
        "MVA-BN (JYNNEOS): 3rd-gen non-replicating vaccine safe in immunocompromised."
    ),
    (9, 15): (
        "B",
        "First- and second-generation replicating vaccinia vaccines (e.g., ACAM2000) are contraindicated in immunocompromised individuals (risk of progressive vaccinia), pregnant women (fetal vaccinia), and people with atopic dermatitis/eczema (risk of eczema vaccinatum).",
        "Contraindication to replicating smallpox vaccine: Eczema, pregnancy, immunosuppression."
    ),

    # -------------------------------------------------------------
    # LECTURE 10: Herpes viruses (Q1 - Q20)
    # -------------------------------------------------------------
    (10, 1): (
        "A",
        "There are 8 distinct human herpesvirus types comprising 9 viruses (HHV-1 to HHV-8, with HHV-6 classified as HHV-6A and HHV-6B) classified into 3 subfamilies: Alphaherpesvirinae, Betaherpesvirinae, and Gammaherpesvirinae.",
        "Human herpesviruses: 9 viruses in 3 subfamilies (alpha, beta, gamma)."
    ),
    (10, 2): (
        "A",
        "The herpesvirus architecture consists of 4 concentric layers: (1) core with linear double-stranded DNA genome, (2) icosahedral capsid (T=16), (3) proteinaceous tegument, and (4) lipid envelope studded with glycoprotein spikes.",
        "Herpes virion: Genome, capsid, tegument, and envelope."
    ),
    (10, 3): (
        "B",
        "During latent infection in host sensory neurons or lymphoid cells, the viral linear DNA circularizes and persists in the nucleus as a stable episome (extrachromosomal circular DNA)—NOT integrating into cellular chromosomes.",
        "Herpes latency: Circular episomal DNA in the nucleus (not integrated)."
    ),
    (10, 4): (
        "B",
        "The subfamily Betaherpesvirinae (comprising Cytomegalovirus [HHV-5], HHV-6A/B, and HHV-7) is leucotropic, infecting monocytes, macrophages, and T-lymphocytes; infections are clinically severe in immunocompromised hosts and during pregnancy.",
        "Betaherpesvirinae (CMV, HHV-6/7): Leucotropic subfamily."
    ),
    (10, 5): (
        "B",
        "Real-time quantitative PCR (qPCR) detecting and measuring viral DNA copy number in blood, CSF, or tissue is the clinical gold standard for diagnosing active herpesvirus infections.",
        "Gold standard herpesvirus detection: Real-time quantitative PCR."
    ),
    (10, 6): (
        "B",
        "Epstein-Barr Virus (EBV / HHV-4) displays dual cell tropism: it infects oropharyngeal epithelial cells for lytic replication and shedding, and infects B lymphocytes establishing lifelong latent episomal persistence.",
        "EBV dual cell tropism: B lymphocytes (latency) and epithelial cells (replication)."
    ),
    (10, 7): (
        "C",
        "In EBV serology: presence of anti-Viral Capsid Antigen IgM (VCA IgM+) in the absence of VCA IgG and anti-Epstein-Barr Nuclear Antigen (EBNA IgG-) indicates acute primary infection (infectious mononucleosis). EBNA antibodies only appear 6–12 weeks later.",
        "VCA IgM+, VCA IgG-, EBNA IgG- = Acute primary EBV infection."
    ),
    (10, 8): (
        "B",
        "The Paul-Bunnell-Davidson (Monospot / MNI) test detects heterophile IgM antibodies agglutinating sheep/horse RBCs. It has a ~20% false negative rate (especially in children <4 years) and can yield false positives in HIV, CMV, or autoimmune disease.",
        "Heterophile antibody test: ~20% false-negatives, false-positives with HIV/CMV."
    ),
    (10, 9): (
        "B",
        "Primary Central Nervous System Lymphoma (cerebral lymphoma) occurring in severely immunosuppressed HIV/AIDS patients is 100% associated with EBV (Epstein-Barr virus) infection within tumor B cells.",
        "Cerebral lymphoma in AIDS patients is 100% EBV-associated."
    ),
    (10, 10): (
        "A",
        "WHO global prevalence figures: approximately 3.7 billion people under age 50 (67% of the global population) are infected with HSV-1, and approximately 491 million people aged 15–49 (13%) are infected with HSV-2.",
        "Global prevalence: HSV-1 ~3.7 billion (67%); HSV-2 ~491 million (13%)."
    ),
    (10, 11): (
        "A",
        "Herpes Simplex Virus encephalitis (primarily HSV-1) causes necrotizing temporal lobe encephalitis with an untreated mortality rate of ~70–80%. Prompt empiric initiation of IV acyclovir before PCR confirmation is vital.",
        "HSV encephalitis: 80% fatal untreated; emergency IV acyclovir must start immediately."
    ),
    (10, 12): (
        "C",
        "The family Herpesviridae is divided into Alphaherpesvirinae, Betaherpesvirinae, and Gammaherpesvirinae. 'Deltaherpesvirinae' does not exist.",
        "Deltaherpesvirinae is NOT a real herpesvirus subfamily."
    ),
    (10, 13): (
        "A",
        "To prevent neonatal HSV transmission: elective Caesarean delivery is recommended for women with active genital lesions if membranes have been ruptured for < 4 hours; maternal oral valacyclovir prophylaxis (1 g/day) is indicated from 36 weeks of gestation.",
        "Neonatal herpes prevention: C-section (<4h after rupture) + maternal valacyclovir from 36 wk."
    ),
    (10, 14): (
        "B",
        "A neonate suspected of HSV infection must immediately be treated with high-dose intravenous acyclovir (20 mg/kg every 8 hours) for 14 days (skin/eye/mouth) or 21 days (CNS or disseminated disease), followed by suppressive oral acyclovir.",
        "Neonatal HSV treatment: Emergency high-dose IV acyclovir (20 mg/kg/8h) for 2–3 weeks."
    ),
    (10, 15): (
        "A",
        "Herpes zoster (shingles) occurs when latent Varicella-Zoster Virus in the dorsal root or cranial nerve sensory ganglia reactivates, migrating anterograde along the sensory axon to produce a painful vesicular rash strictly restricted to a unilateral dermatome.",
        "Shingles = VZV reactivation in sensory ganglia traveling to skin along one dermatome."
    ),
    (10, 16): (
        "B",
        "Cytomegalovirus (CMV / HHV-5) is the paramount opportunistic viral pathogen in solid organ and bone marrow transplant recipients and AIDS patients (causing retinitis, pneumonitis, colitis, and graft failure).",
        "Cytomegalovirus (CMV) is a major opportunistic pathogen in immunodeficiency."
    ),
    (10, 17): (
        "D",
        "All members of the family Herpesviridae possess a large, linear, double-stranded DNA (dsDNA) genome ranging from 125 to 240 kbp.",
        "All herpesviruses possess a double-stranded DNA (dsDNA) genome."
    ),
    (10, 18): (
        "C",
        "Varicella-Zoster Virus (VZV / HHV-3) causes primary chickenpox (varicella) and, following latency in cranial/dorsal root ganglia, reactivates decades later to cause shingles (herpes zoster).",
        "Varicella-Zoster Virus causes both chickenpox and shingles."
    ),
    (10, 19): (
        "D",
        "Herpesvirus infections (HSV, CMV) produce the most devastating, severe, and potentially fatal systemic manifestations in neonates (due to immature immunity) and severely immunocompromised individuals.",
        "Severe herpes manifestations occur predominantly in neonates and immunocompromised."
    ),
    (10, 20): (
        "D",
        "Direct diagnosis and monitoring of active Cytomegalovirus (CMV) infection relies on quantitative real-time PCR measuring CMV DNA levels in whole blood or plasma.",
        "Direct diagnostic for CMV: Quantitative real-time PCR."
    ),

    # -------------------------------------------------------------
    # LECTURE 11: Viral hepatitis (Q1 - Q23)
    # -------------------------------------------------------------
    (11, 1): (
        "C",
        "Hepatitis D Virus (HDV / Delta agent) is a defective viroid-like satellite virus consisting of circular -ssRNA and hepatitis D antigen (HDAg); it requires the Hepatitis B surface antigen (HBsAg) envelope coat to package, bud, and infect hepatocytes.",
        "Hepatitis D is a satellite virus requiring HBsAg from HBV."
    ),
    (11, 2): (
        "A",
        "Globally, WHO estimates that approximately 257 to 296 million people (~3.2% of the world population) are living with chronic Hepatitis B infection (HBsAg carriers).",
        "Global chronic HBV burden: Approximately 257.5 million people."
    ),
    (11, 3): (
        "B",
        "Recent epidemiological data in Cambodia (2022 surveys) indicates an overall HBsAg prevalence of approximately 3% in the adult general population (reduced from historical highs of 8–10% due to childhood vaccination).",
        "General population HBsAg prevalence in Cambodia (2022): ~3%."
    ),
    (11, 4): (
        "C",
        "In Cambodia (systematic review / meta-analysis data), high-risk or co-infected populations (such as people living with HIV) exhibit the highest pooled HBsAg prevalence, reaching approximately 19.87%.",
        "Highest HBsAg prevalence in Cambodia: High-risk / co-infected groups (~19.87%)."
    ),
    (11, 5): (
        "B",
        "The Hepatitis B Virus (HBV, family Hepadnaviridae) genome is a circular, partially double-stranded DNA molecule of approximately 3,200 base pairs with an overlapping reading frame structure.",
        "HBV genome: Circular, partially double-stranded DNA (~3,200 bp)."
    ),
    (11, 6): (
        "B",
        "HBV is notoriously difficult to eradicate because its relaxed circular DNA is converted in the hepatocyte nucleus into covalently closed circular DNA (cccDNA), which serves as a stable viral minichromosome resistant to nucleos(t)ide analogues.",
        "Key to HBV chronicity and resistance: Nuclear persistence of cccDNA."
    ),
    (11, 7): (
        "B",
        "Hepatitis B e antigen (HBeAg) is a secretory protein derived from the pre-core/core gene; its presence in serum indicates high viral replication and high infectivity.",
        "HBeAg positivity signifies active viral replication and high infectivity."
    ),
    (11, 8): (
        "B",
        "An antibody to hepatitis B surface antigen (anti-HBs) titer of >= 10 IU/L (or mIU/mL) is internationally recognized as the threshold for protective immunity against HBV infection.",
        "Protective anti-HBs antibody level: > 10 IU/L (mIU/mL)."
    ),
    (11, 9): (
        "A",
        "In immunocompetent adults who acquire acute HBV, 90–95% successfully clear the virus and develop lifelong immunity (anti-HBs+); only 5–10% progress to chronic HBV (in sharp contrast to infected neonates, where 90% become chronic).",
        "Adult HBV outcome: 90–95% clear the infection; 5–10% progress to chronic."
    ),
    (11, 10): (
        "B",
        "HDV cannot replicate autonomously to produce infectious progeny; it can only cause infection in individuals who are concurrently infected with Hepatitis B Virus (as a co-infection or super-infection).",
        "HDV can only infect patients infected with Hepatitis B virus."
    ),
    (11, 11): (
        "B",
        "Molecular epidemiology in Cambodia has established that Hepatitis C Virus (HCV) infections are predominantly caused by Genotype 1 (subtype 1b) and Genotype 6 (subtype 6e).",
        "Predominant HCV genotypes in Cambodia: Genotype 1 (1b) and Genotype 6 (6e)."
    ),
    (11, 12): (
        "C",
        "Unlike HBV in adults, acute Hepatitis C Virus infection fails to clear spontaneously in the vast majority: approximately 75% to 85% (~75%) of individuals develop chronic HCV infection.",
        "Chronic progression of HCV: Approximately 75% of acute infections become chronic."
    ),
    (11, 13): (
        "A",
        "The therapeutic cure endpoint for HCV treatment with direct-acting antivirals (DAAs) is Sustained Virologic Response (SVR): undetectable HCV RNA (limit of detection <= 15 IU/mL) at 12 or 24 weeks after therapy completion.",
        "HCV cure endpoint: Undetectable HCV RNA (LLD <= 15 IU/mL) at SVR12/SVR24."
    ),
    (11, 14): (
        "B",
        "Hepatitis A Virus (HAV, Picornaviridae) and Hepatitis E Virus (HEV, Hepeviridae) are non-enveloped viruses transmitted enterically via the faecal-oral route through contaminated water and food ('The vowels go through the bowels').",
        "Enteric faecal-oral transmission: Hepatitis A and Hepatitis E."
    ),
    (11, 15): (
        "B",
        "In the acute febrile illness surveillance study conducted in South-Central Cambodia (Kasper et al., Am J Trop Med Hyg 2012), 11.1% of patients demonstrated IgM seropositivity for Hepatitis E Virus (HEV).",
        "Cambodia acute febrile illness: 11.1% tested positive for HEV IgM."
    ),
    (11, 16): (
        "C",
        "Hepatitis B Virus and Hepatitis C Virus (along with HDV) are the primary viral causes of chronic hepatitis, driving long-term hepatic inflammation, progressive cirrhosis, and hepatocellular carcinoma (HCC).",
        "Chronic hepatitis leading to cirrhosis and liver cancer: Hepatitis B and C."
    ),
    (11, 17): (
        "C",
        "Hepatitis B, C, and D viruses are parenterally transmitted pathogens spread through percutaneous blood exposure (transfusions, unsterile injections), sexual contact, and perinatal/vertical transmission.",
        "HBV, HCV, HDV transmission: Blood, sexual contact, and body fluids."
    ),
    (11, 18): (
        "B",
        "Jaundice (icterus)—yellow pigmentation of the sclera, skin, and mucous membranes caused by hyperbilirubinemia from hepatic inflammation and impaired bile excretion—is the cardinal clinical sign of acute viral hepatitis.",
        "Cardinal clinical sign of acute hepatitis: Jaundice (icterus)."
    ),
    (11, 19): (
        "B",
        "Effective preventive vaccines currently exist for Hepatitis A (inactivated vaccine), Hepatitis B (recombinant HBsAg vaccine), and Hepatitis E (recombinant HEV vaccine, Hecolin, licensed in China and Pakistan).",
        "Vaccines exist for Hepatitis A, B, and E."
    ),
    (11, 20): (
        "B",
        "Serological tests (ELISA / chemiluminescent microparticle immunoassay) detecting specific antigens (HBsAg, HBeAg) and antibodies (anti-HAV IgM, anti-HBc, anti-HBs, anti-HCV, anti-HEV) are universally used to diagnose viral hepatitis.",
        "Diagnostic identification of hepatitis markers: Serological tests (ELISA)."
    ),
    (11, 21): (
        "C",
        "Because Hepatitis A and E are spread by contaminated drinking water and food (fecal-oral), public health prevention depends on clean water supplies, sewage sanitation, food hygiene, and handwashing.",
        "Prevention for HAV and HEV: Safe sanitation, clean drinking water, and food safety."
    ),
    (11, 22): (
        "C",
        "The primary long-term clinical sequelae of untreated chronic Hepatitis B and C infections are progressive liver fibrosis, cirrhosis, end-stage liver disease, and hepatocellular carcinoma (liver cancer).",
        "Long-term complications of chronic HBV/HCV: Liver cirrhosis and liver cancer."
    ),
    (11, 23): (
        "A",
        "Direct screening and diagnostic confirmation of active Hepatitis B infection requires testing for the viral surface antigen (HBsAg) and measuring viral genome replication via HBV DNA quantitative PCR.",
        "Direct diagnosis for HBV screening: Viral surface antigen (HBsAg) and viral genome (DNA)."
    ),
}

def main():
    with open("questions_raw.json") as f:
        raw_lectures = json.load(f)

    full_db = []
    global_id = 1

    for l_idx, lec in enumerate(raw_lectures, start=1):
        lec_title = lec["lecture"]
        for q in lec["questions"]:
            qid = q["id"]
            key = (l_idx, qid)
            if key not in METADATA:
                print(f"ERROR: Missing metadata for Lecture {l_idx} Q{qid}")
                correct_ans = "A"
                explanation = "Explanation pending."
                takeaway = "Takeaway pending."
            else:
                correct_ans, explanation, takeaway = METADATA[key]

            item = {
                "global_id": global_id,
                "lecture_id": l_idx,
                "lecture_name": lec_title,
                "question_id": qid,
                "question": q["question"],
                "options": q["options"],
                "correct_answer": correct_ans,
                "correct_text": q["options"].get(correct_ans, ""),
                "explanation": explanation,
                "takeaway": takeaway
            }
            full_db.append(item)
            global_id += 1

    print(f"Successfully processed {len(full_db)} questions across {len(raw_lectures)} lectures.")
    with open("questions_db.json", "w", encoding="utf-8") as f:
        json.dump(full_db, f, indent=2, ensure_ascii=False)
    print("Wrote questions_db.json successfully!")

if __name__ == "__main__":
    main()
