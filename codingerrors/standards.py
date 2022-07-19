# The MIT License
#
# Copyright (c) 2022 Keiron O'Shea
#
# Permission is hereby granted, free of charge,
# to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to
# deal in the Software without restriction, including
# without limitation the rights to use, copy, modify,
# merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom
# the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice
# shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR
# ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from .utils import hyph

# &* : Can never be in the primary position
# ^* : Must be in primary or secondary position.
# ? : Applies to the following codes.
# / : never code
# ! : Cannot be coded with
# # : Unless present
# .n: Require's nth character
# { : Must always be coded with
# ~x..y: x character cannot be y
# > : Should not be directly followed by

standards_dict = {
    # Anaemia must not be coded in leukaemia, myeloma and myelodysplasia
    "DChS.II.2:0:W": "?D64:!C90-C95",
    # Sickle cell trait must not be coded with thalassaemia or sickle cell anaemia with or without crisis
    "DCS.III.1:0:W": "?D573:!D56,D570,D571",
    # COPD with Chest infection
    "DCS.X.5:0:W": "?J440:!J22X",
    # Chest infection and pneumonia
    "DCS.X.5:1:W": "?J18:!J22",
    # COPD with pneumonia
    "DCS.X.5:2:W": "?J449:!J12-J18",
    # COPD with Emphysema
    "DCS.X.5:3:W": "?J449:!J439",
    # Respiratory Failure
    "DCS.X.7:0:W": "?J960,J961,J969:.5",
    # Gastritis and duodenitis
    "DCS.XI.4:0:W": "?K297:!K298",
    # Other specified bacterial intestinal infections, is not to be code with K29
    "DCS.XI.4:1:W": "?A048:!K29",
    # Multiple gestation
    "DCS.XV.14:0:W": "?O30:{Z372-Z377",
    # Parastoma hernia
    "DCS.XI.5:0:W": "?K433,K435:{Z93",
    # Delirum and Dementia
    "DCS.V.3:0:W": "?F03X,F01,F02:!F050,F059",
    # F03X should not be coded with F051
    "DCS.V.3:1:W": "?F051:!F03X",
    # Mental and behavioural disorders due to multiple drug use and use of other psychoactive substances not to be coded with f10-f18
    "DCS.V.4:0:W": "?F10-F16,F18:!F17",
    # Amaurosis fugax
    "DCS.VI.2:0:W": "?G453:!H54",
    # I23.- Certain current complications following acute myocardial infarction must not be coded with I21.- or I22.-
    "DCS.IX.6:0:W": "?I21,I22:!I23",
    # I46.9 unspecified cardiac arrest should not be coded with I46.0 or I46.1
    "DCS.IX.8:0:W " : "?I460,I461:!I469",
    # Heart Failure CCF
    "DCS.IX.10:0:W": "?I501,I509:!I500,I50X",
    # Pulmonary Oedema
    "DCS.IX.10:1:W": "?I00-I01,I05-I10,I119,I12,I14-15,I20-I25,I25-I35,I38-I40,I49,I51,I52:!J81X",
    # congestive cardiac failure (CCF) (I50.0) should not be coded with left ventricular failure (LVF) (I50.1) 
    "DCS.IX.10:2:W" : "?I501:!I500",
    # I64.X Stroke, must not be coded with I63.-
    "DCS.IX.11:0:W": "?I64X:!I63",
    # Atherosclerosis 
    "DCS.IX.14:0:W": "?I70:.5",
    # Fifth character in Chapter XIX
    "DCS.XIX.2:0:W": "?S02,S12,S22,S32,S42,S52,S62,S72,S82,S92,T02,T08,T10,T12:.5",
    # Palliative care
    "DCS.XXI.9:0:W": "?Z518:!Z515",
    # DM should be either Type 1/Type 2 or unknown
    "DCS.IV.1:0:W": "?E11,E14:!E10",
    "DCS.IV.1:1:W": "?E11:!E14,E10",
    "DCS.IV.1:2:W": "?E14:!E10,E11",
    # External Causes 
    "DChS.XX.1:0:W": "?V01-V99,Y01-Y98:&*",
    # B972 without U071 
    "DSC.XXII.5:COVID-19:0:W": "?U071:>B972",
    # U071 coded with U072
    "DSC.XXII.5:COVID-19:1:W": "?U071:!U072",
    # U071 must be in primary position
    "DSC.XXII.5:COVID-19:2:W": "?U071:^*",
    # B972 should not directly follow codes in J18_
    "DSC.XXII.5:COVID-19:3:W": "?J18:>B972",
    # U049 SARS should not be coded
    "DSC.XXII.5:COVID-19:4:W": "?U049:/*",
    # B342 or B972 should not directly follow U071 or U072…. This guidence from WHO and NHS Digital
    "DSC.XXII.5:COVID-19:5:W": "?U071,U072:>B342,B972",
    # U072 should not be coded with B342, Z115, Z038
    "DSC.XXII.5:COVID-19:6:W": "?U072:!B342,Z115,Z038",
    # U073 must not be assigned with U071 or U072
    "DSC.XXII.5:COVID-19:7:W": "?U071,U072:!U073",
    # U073 must not be assigned with U074
    "DSC.XXII.5:COVID-19:8:W": "?U074:!U073",
    # Signs, symptoms and abnormal laboratory findings
    "DChS.XVIII:0:W": "?G40,G41:!R568",
    # R10 - abdomen pain should not be coded with appendicitis K35, K36,K37
    "DChS.XVIII:1:W": "?K35-K37:!R10",
    # R07 - chest pain should not be coded with I21, I22
    "DChS.XVIII:2:W": "?I21-I22:!R07",
    # R060 - shortness of breath should not be coded with Pneumonia (J12 - J18) or LRTI (J22) or IECOPD (J440)
    "DChS.XVIII:3:W": "?J12-J18:!R060",
    # R568 should not be coded with either G40 or G41 
    "DChS.XVIII:4:W": "?G40-G41:!R568",
    # R251 should not be coded with either G20 or G21
    "DChS.XVIII:5:W": "?G20-G21:!R251",
    # Constipation with ileus or obstruction
    "DChS.XI.1:0:W": "?K56,K400,K403,K413,K420,K430,K433,K436,K440,K450,K460:!K590",
    # Musculoskeletal 5th Character
    "DChS.XIII.1:0:W": "?M00-M25,M40-M54,M60-M99:~5..9",
    # no need to assign urethral obstruction N368 with N40X
    "DCS.XIV.5:0:W" :"?N40X:!N368",
    # Z72.0 tobacco use must not be coded
    "DSC.V.7:0:W": "?Z720:/*",
    # Z12.1 Special screening examination for neoplasm of intestinal tract 
    "DCS.XXI.1:0:W": "?D12,K55-K64,C18-C21:!Z121",
    # Y838 and Y839 and Y848 and Y849 should not be coded with a code from T80-T88
    "DSC.XIX.7:0:W": "?T80-T88:!Y838,Y839,Y848,Y849",
    # N993 should not be directly followed by Y83/Y84
    "DCS.XIV.12:0:W": "?N993:>Y83,Y84",
    # F80 should not be coded with either F81 or F82
    "DCS.XIV.12:1!W:W": "?F81,F82:!F80",
    # CKD with Renal Failure 
    "DCS.XIV.2:0:W": "?N184,N185:!N19",
    # Chronic kidney disease
    "DCS.XIV.2:1:W": "?N182,N183,N184,N185,N189:!N181",
    "DCS.XIV.2:2:W": "?N181,N183,N184,N185,N189:!N182",
    "DCS.XIV.2:3:W": "?N181,N182,N184,N185,N189:!N183",
    "DCS.XIV.2:4:W": "?N181,N182,N183,N185,N189:!N184",
    "DCS.XIV.2:5:W": "?N181,N182,N183,N184,N189:!N185",
    "DCS.XIV.2:6:W": "?N181,N182,N183,N184,N185:!N189",

    # T29 should not be coded
    "DCS.XIX.5:0:E": "?T29:/*",
    # J95.8 should not be coded  
    "DSC.XIX.7:0:W": "?J958:/*",
    # Codes O95, O96, O97 should never be assigned
    "DCS.XV.29:0:W": "?O95-O97:/*",
    # D649 should not be coded with O990
    "DSC.XV.32:0:W": "?O990:!D649",
    # Geriatric and elderly falls (R296)
    "DCS.XVIII.4:0:W": "?R296:>W00-W19",
    # Sepsis codes should not be followed by B95 or B96
    "DCS.I.4:0:W": "?A40,A41:>B95,B96",
    # R69.X/R96.X/R98.X/R99.X should not be coded is other information is available for code assignment
    "DCS.XVIII.11:0:W": "?R69X,R96X,R98X,R99X:/*",
    # Rare Delivery Codes
    "DCS.XV.28:0:W": "?O801,O802,O808,OS809,O81,O821,O822,O828,O829,O83,O84:/*",
    # Delivery
    "DCS.XV.28:1:W": "?O10-O16,O20-O48,O60-O75,O85-O92,O94-O99:!O800,O820",
    # Code M16.-, M17.-, M18.- AND M19.- must not be coded together, M15.- must be coded instead to indicate multiple areas of osteoarthritis.
    "DCS.XII.2:0:W": "?M16:!M17,M18,M19",
    "DCS.XII.2:1:W": "?M17:!M16,M18,M19",
    "DCS.XII.2:2:W": "?M18:!M16,M17,M19",
    "DCS.XII.2:3:W": "?M19:!M16,M17,M18",
    # I13.- must not be coded with I11.- or I12.-
    "DCS.IX.2:0:W": "?I11-I12:?I13",
    # T795 should not be coded with N179
    "DCS.XIII.3:0:W": "?N179:!T795",
    # Severe Sepsis : R65.1 must always be coded directly following a code from A40._ or A41._or P36._ or O85. or (A207,A217,A227,A239,A267,A282,A327,A391,A427,A548,B377,O753 - have added A394)
    # "DChS.I.1:0:W": "?A40,A41,P36,O85,A207,A217,A227,A239,A267,A282,A327,A391,A427,A548,B377,O753:<R651",
    # Multiple independent primary malignant neoplasm
    "DSC.II.4:0:W": "?C97X:^*",
    # I739 should not be coded with I702,I723,I724,I743,I744,I745
    "DC.IX.15:0:W": "?I702,I723,I724,I743,I744,I745:!I739",
    # K22.2 must not be coded with Q39.4
    "DCS.XI.1:0:W": "?Q394:!K222",
    # Haemorrhoids
    "DCS.XI.10:0:W": "?K641,K642,K643:!K640",
    "DCS.XI.10:1:W": "?K640,K642,K643:!K641",
    "DCS.XI.10:3:W": "?K640,K641,K643:!K642",
    "DCS.XI.10:4:W": "?K640,K641,K642:!K643",
    # Pressure Ulcers 
    "DCS.XII.3:0:W": "?L891,L892,L893,L899:!L890",
    "DCS.XII.3:1:W": "?L890,L892,L893,L899:!L891",
    "DCS.XII.3:2:W": "?L890,L891,L893,L899:!L892",
    "DCS.XII.3:3:W": "?L890,L891,L892,L899:!L893",
    "DCS.XII.3:4:W": "?L890,L891,L892,L893:!L899",
    # Infected Pressure Ulcers
    "DCS.XII.3:5:W": "?L89,L97X:>B95,B96",
    # Arthrosis
    "DChS.XIII.2:0:W": "?M17,M19:!M16",
    "DChS.XIII.2:1:W": "?M19,M16:!M17",
    "DChS.XIII.2:2:W": "?M17,M16:!M19",
    # N20.2  must not be coded with N20.0 or N20.1
    "DCS.XIV.3:0:W": "?N200,N201:!N202",
    # Neoplasia Prostate
    "DCS.XIV.7:0:W": "?D075,C61X:!N423",
    "DCS.XIV.7:1:W": "?N423,C61X:!D075",
    "DCS.XIV.7:2:W": "?D075,N423:!C61X",
    # CIN
    "DCS.XIV.10:0:W": "?N871,N879,D069:!N870",
    "DCS.XIV.10:1:W": "?D069,N870,N879:!N871",
    "DCS.XIV.10:2:W": "?N870,N871,N879:!D069",
    "DCS.XIV.10:3:W": "?N870,N871,D069:!Z879",
    # VAIN
    "DCS.XIV.10:4:W": "?N891,N899,D072:!N890",
    "DCS.XIV.10:5:W": "?D072,N890,N899:!N891",
    "DCS.XIV.10:6:W": "?N890,N891,N899:!D072",
    "DCS.XIV.10:7:W": "?N890,N891,D072:!N899",
    # O20.- must not be coded with O00.-, O01.-, o02.-, o03.-, o04.-, o05.- o06.-, o07.-, o08.-
    "DCS.XV.6:0:W": "?O08-O08:!020",
    # O21.- must not be coded with R11.x
    "DCS.XV.7:0:W": "?021:!R11",
    # Z33.x must not be used with any code from O00.- to O99.-
    "DCS.XXI.5:0:W": "?O00-O99:!Z33",
    # Pregnant state, incidental 
    "DCS.XV.33:0:W": "?Z33X:&*",
    # Dehydration of newborn (P74.1) must not be coded with E86.x
    "DCS.IV.7:0:W": "?E86X:!P741",
    # R68.8 must not be coded with N17.-, k72.9, i50.-, i51.- or any other organ failure code
    "DCS.XVIII.10:0:W": "?N17,K729,I50,I51:!R688",
    # Fetus and newborn affected by maternal factors and by complications of pregnancy, labour and delivery
    "DCS.XVI.1:0:W": "?P00-P04:&*",
    # H54.0 Blindness, binocular (if unspecified or stated of both eyes) must not be coded with H54.4 Blindness, monocular (if stated to be of one eye only).
    "DCS.VII.3:0:W": "?H544:!H540",
    # H91.9 must not be coded with H90.0, h90.1, h90.2, h90.3, h90.4, h90.5, h90.6, h90.7, h90.8, h91.0, h91.1, h91.2, h91.3, h91.8
    "DCS.VIII.1:0:W": "?H90,H910,H911,H912,H913,H918:!H919",

    # Neonatal Jaundice 
    "FSCP:0:W": "?P072,P073:!P599",
    # B95/B96/B97/B98 Never in primary position
    "FSCP:1:W": "?B95-B98:&*",
    # I350 should not be coded with I351
    "FSCP:2:W": "?I351:!I350",
    # I080 coded with codes from I34 and I35
    "FSCP:3:W": "?I34,I35:!I080",
    # M479 should not be coded with 5th character of 2 cervical, 6 lumbar or 8 sacral
    "FSCP:4:W": "?M4792, M4796,M4798:/*",
    # Z722 should not be coded with F55, F19, F11,F12,F13,F14,F15,F16
    "FSCP:5:W": "?F55,F19,F11,F12,F13,F14,F15,F16:!Z722",
    # Z720 should not be coded with F171
    "FSCP:6:W": "?F171:!Z720",
    # I350 should not be coded with I351
    "FSCP:7:W": "?I351:!I350",
    # I830 should not be coded with I831
    "FSCP:8:W": "?I831:!I830",
    # K802 should not be coded with K81
    "FSCP:9:W": "?K81:!K802",
    # Z721 should not be coded with F102
    "FSCP:10:W": "?F102:!Z721",
    # N13.2 Hydronephrosis with N20_
    "FSCP:11:W": "?N132:!N20",
    # I633-I634-I635 should not be coded with I65
    "FSCP:12:W": "?I65:!I633-I635",
    # J852 Abscess of lung without pneumonia should not be coded with pneumonia 
    "FSCP:13:W": "?J12-J18:!J852",
    # I080 coded with codes from I34 and I35
    "FSCP:14:W": "?I34-I35:!I080",
    # codes O640 - O663 should not be coded with O320 - O324/O326 -O329 and O33._
    "FSCP:15:W": "?O320-O324,O326-O329,O33:!O640-O663",
    # Dementia 
    "FSCP:16:W": "?F03:!F01-F02",
    # R251 should not be followed directly by a code between Y40 - Y59
    "FSCP:17:W": "?R251:>Y40-Y59",
    # M109 should not be directly followed by a code from Y40-Y59
    "FSCP:18:W": "?M109:>Y40-Y59",
    # E162 should not be directly followed by a code from Y40-Y59
    "FSCP:19:W": "?E162:>Y40-Y59",
    # R51X should not be directly followed by code from Y40 - Y59
    "FSCP:20:W": "?R51X:>Y40-Y59",
    # S271 should not be coded with S270
    "FSCP:21:W": "?S271:!S270",
    # A09, K520, K522,K523,K528,K529 should not be directly followed by a code from Y40 - Y59
    "FSCP:22:W": "?A09:>K520,K522,K523,K528,K529:>Y40-Y59",
    # M102,E242,M804,L640,E273,E160,G251,G720,N141,D592,E661,M814,K853,L105,M342,E064,G256,G444,M835 should be directly followed by code from Y40 - Y59
    "FSCP:23:W": "?M102,E242,M804,L640,E273,E160,G251,G720,N141,D592,E661,M814,K853,L105,M342,E064,G256,G444,M835:<Y40-Y59",
    # G620 not directly followed by a code from Y40-Y59 or Y880
    "FSCP:24:W": "?G620:>Y40-Y59,Y880",
    # Codes L233/L251/L270/L271 should be followed by a code from Y10-Y599 to state what drug caused the dermatitis
    "FSCP:25:W": "?L233,L251,L270,L271:>Y10-Y58,Y599",
    # Chronic diarrhoea with infective diarrhoea
    "FSCP:26:W": "?A09:!K529",
    # J18 should not be followed by a code by B95 and B96
    "FSCP:27:W": "?J18:>B95,B98",
    # I959 should not be directly followed by a code from Y40-Y59
    "FSCP:28:W": "?I959:>Y40-Y59",
    # K859 should not be directly followed by a code from Y40-Y59
    "FSCP:29:W": "?K859:>Y40-Y59",
    # G629 should not be directly followed by a code from Y40-Y59
    "FSCP:30:W": "?G629:>Y40-Y59",
    # B95 B96 should not directly follow I830
    "FSCP:31:W": "?I830:>B95,B96", 
    # Kidney and Ureter Calculi
    "FSCP:32:W": "?N201,N202:!N200",
    # Codes from L30 should not be directly followed by any codes in the range Y100 - Y599
    "FSCP:33:W": "?L30:>Y10-Y59",
    # Influenza with pneumonia
    "FSCP:34:W": "?J13-J18:!J10-J11",
    # Ankylosis of joint should not be coded with stiffness of joint 
    "FSCP:35:W": "?M256:!M246",
    # K802 Calculus of gallbladder without cholecystitis coded with K81_ Cholecystitis
    "FSCP:36:W": "?K81:!K802",
    # I260 should not be coded with I279
    "FSCP:37:W": "?I279:!I260",
    # I95.2 Hypotension due to drugs should have an additional Y40 - Y59 coded directly beneath
    "FSCP:38:W": "?I952:<Y40-Y59",
    # Z21X coded with symptomatic HIV
    "FSCP:39:W": "?B20-B24:!Z21X",
    # Perineal laceration during delivery
    "FSCP:40:W": "?O701,O704-O709:!O700,0702,0703",
    # Codes from I64 should not be coded with I63
    "FSCP:41:W": "?I63:!I64",
    # I630-I631-I632 should not be coded with I65
    "FSCP:42:W": "?I65:I630-I632"

}


def _build_standards_dict() -> dict:
    compiled_standards_dict = {}
    for key, standard in standards_dict.items():
        standard = standard.split(":")

        primary_icd10s = hyph(standard[0][1:])

        for icd10 in primary_icd10s:

            if icd10 not in compiled_standards_dict:
                compiled_standards_dict[icd10] = {}

            for part in standard[1:]:
                dehyphyed = hyph(part[1:])
                if part.startswith("."):
                    if key not in compiled_standards_dict[icd10]:
                        compiled_standards_dict[icd10][key] = {}
                    compiled_standards_dict[icd10][key]["."] = part[1:]
                elif part[0] in ("&", "/", "^"):
                    if key not in compiled_standards_dict[icd10]:
                        compiled_standards_dict[icd10][key] = {}
                    compiled_standards_dict[icd10][key][part[0]] = icd10
                elif part[0] == "~":
                    character, have = part[1:].split("..")
                    if key not in compiled_standards_dict[icd10]:
                        compiled_standards_dict[icd10][key] = {}
                    compiled_standards_dict[icd10][key][part[0]] = {
                        "character": character,
                        "have": have
                    }
                else:
                    if key not in compiled_standards_dict[icd10]:
                        compiled_standards_dict[icd10][key] = {}
                    compiled_standards_dict[icd10][key][part[0]] = dehyphyed
    return compiled_standards_dict
