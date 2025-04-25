indicators = {
    # General
    'SP.POP.TOTL': {
        'source':      'World Bank',
        'description': 'Population, total',
        'agg':         'sum',
    },
    'SP.POP.GROW': {
        'source':      'World Bank',
        'description': 'Population growth (annual %)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SP.URB.TOTL': {
        'source':      'World Bank',
        'description': 'Urban population',
        'agg':         'sum',
    },
    'SP.URB.TOTL.IN.ZS': {
        'source':      'World Bank',
        'description': 'Urban population (% of total)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SP.RUR.TOTL': {
        'source':      'World Bank',
        'description': 'Rural population',
        'agg':         'sum',
    },
    'SP.DYN.LE00.IN': {
        'source':      'World Bank',
        'description': 'Life expectancy at birth, total (years)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'AG.SRF.TOTL.K2': {
        'source':      'World Bank',
        'description': 'Surface area (sq. km)',
        'agg':         'sum',
    },
    'AG.LND.TOTL.K2': {
        'source':      'World Bank',
        'description': 'Land area (sq. km)',
        'agg':         'sum',
    },

    # Economy
    'NY.GDP.MKTP.PP.CD': {
        'source':      'World Bank',
        'description': 'GDP, PPP (current international $)',
        'agg':         'sum',
    },
    'NY.GDP.PCAP.PP.CD': {
        'source':      'World Bank',
        'description': 'GDP per capita, PPP (current international $)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
    'NY.GDP.MKTP.CD': {
        'source':       'World Bank',
        'description':  'GDP (current US$)',
        'agg':          'sum'
    },
    'NY.GDP.MKTP.KD.ZG': {
        'source':      'World Bank',
        'description': 'GDP growth (annual %)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'NY.GDP.PCAP.CD': {
        'source':      'World Bank',
        'description': 'GDP per capita (current US$)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'NY.GNP.PCAP.PP.CD': {
        'source':      'World Bank',
        'description': 'GNI per capita, PPP (current international $)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FP.CPI.TOTL.ZG': {
        'source':      'World Bank',
        'description': 'Inflation, consumer prices (annual %)',
        'agg':         'mean',
    },
    'PA.NUS.FCRF': {
        'source':      'World Bank',
        'description': 'Official exchange rate (LCU per US$, period average)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'NY.ADJ.NNTY.PC.CD': {
        'source':      'World Bank',
        'description': 'Adjusted net national income per capita (current US$)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Inequality & Poverty
    'SI.POV.DDAY': {
        'source':      'World Bank',
        'description': 'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL'
    },
    'SI.POV.GINI': {
        'source':      'World Bank',
        'description': 'Gini index',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.DST.FRST.20': {
        'source':      'World Bank',
        'description': 'Income share held by lowest 20%',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.DST.10TH.10': {
        'source':      'World Bank',
        'description': 'Income share held by highest 10%',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.POV.LMIC': {
        'source':      'World Bank',
        'description': 'Poverty headcount ratio at $3.65 a day (2017 PPP) (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.POV.NAHC': {
        'source':      'World Bank',
        'description': 'Poverty headcount ratio at national poverty lines (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Trade & Finance
    'NE.EXP.GNFS.CD': {
        'source':      'World Bank',
        'description': 'Exports of goods and services (BoP, current US$)',
        'agg':         'sum',
    },
    'NE.IMP.GNFS.CD': {
        'source':      'World Bank',
        'description': 'Imports of goods and services (BoP, current US$)',
        'agg':         'sum',
    },
    'NE.TRD.GNFS.CD': {
        'source':      'World Bank',
        'description': 'Trade in goods and services (BoP, current US$)',
        'agg':         'sum',
    },
    'NE.TRD.GNFS.ZS': {
        'source':      'World Bank',
        'description': 'Trade (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'BN.CAB.XOKA.CD': {
        'source':      'World Bank',
        'description': 'Current account balance (BoP, current US$)',
        'agg':         'sum',
    },
    'BN.CAB.XOKA.GD.ZS': {
        'source':      'World Bank',
        'description': 'Current account balance (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FI.RES.TOTL.CD': {
        'source':      'World Bank',
        'description': 'Total reserves (includes gold, current US$)',
        'agg':         'sum',
    },
    'FI.RES.TOTL.MO': {
        'source':      'World Bank',
        'description': 'Total reserves in months of imports',
        'agg':         'weighted',
        'weight_by':   'NE.IMP.GNFS.CD',
    },
    'LP.LPI.OVRL.XQ': {
        'source':      'World Bank',
        'description': 'Logistics performance index: Overall (1=low to 5=high)',
        'agg':         'mean',
    },
    'LP.EXP.DURS.MD': {
        'source':      'World Bank',
        'description': 'Time to export, median case (days)',
        'agg':         'mean',
    },
    'BM.GSR.ROYL.CD': {
        'source':      'World Bank',
        'description': 'Charges for the use of intellectual property, payments (BoP, current US$)',
        'agg':         'sum',
    },
    'TX.VAL.TECH.CD': {
        'source':      'World Bank',
        'description': 'High-technology exports (current US$)',
        'agg':         'sum',
    },
    'TX.VAL.TECH.MF.ZS': {
        'source':      'World Bank',
        'description': 'High-technology exports (% of manufactured exports)',
        'agg':         'weighted',
        'weight_by':   'NE.EXP.GNFS.CD',
    },

    # Investment & Financial Sector
    'BX.KLT.DINV.WD.GD.ZS': {
        'source':      'World Bank',
        'description': 'FDI, net inflows (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
    'BM.KLT.DINV.WD.GD.ZS': {
        'source':      'World Bank',
        'description': 'FDI, net outflows (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
    'BX.KLT.DINV.CD.WD': {
        'source':      'World Bank',
        'description': 'Foreign direct investment, net inflows (BoP, current US$)',
        'agg':         'sum',
    },
    'NE.GDI.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Gross capital formation (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FS.AST.PRVT.GD.ZS': {
        'source':      'World Bank',
        'description': 'Domestic credit to private sector (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'CM.MKT.LCAP.CD': {
        'source':      'World Bank',
        'description': 'Market capitalization of listed domestic companies (current US$)',
        'agg':         'sum',
    },
    'CM.MKT.LCAP.GD.ZS': {
        'source':      'World Bank',
        'description': 'Market capitalization of listed domestic companies (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FB.CBK.BRCH.P5': {
        'source':      'World Bank',
        'description': 'Commercial bank branches (per 100,000 adults)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'FR.INR.LEND': {
        'source':      'World Bank',
        'description': 'Lending interest rate (%)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FR.INR.RINR': {
        'source':      'World Bank',
        'description': 'Real interest rate (%)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },

    # Debt & Aid
    'DT.DOD.DECT.CD': {
        'source':      'World Bank',
        'description': 'External debt stocks, total (current US$)',
        'agg':         'sum',
    },
    'DT.DOD.DECT.GN.ZS': {
        'source':      'World Bank',
        'description': 'External debt stocks (% of GNI)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'DT.TDS.DECT.GN.ZS': {
        'source':      'World Bank',
        'description': 'Total debt service (% of GNI)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'GC.DOD.TOTL.CN': {
        'source':      'World Bank',
        'description': 'Central government debt, total (current LCU)',
        'agg':         'sum',
    },
    'GC.DOD.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Central government debt, total (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'DT.ODA.ODAT.GN.ZS': {
        'source':      'World Bank',
        'description': 'ODA received (% of GNI)',
        'agg':         'weighted',
        'weight_by':   'DT.ODA.ODAT.GN.ZS',
    },
    'DT.ODA.ALLD.CD': {
        'source':      'World Bank',
        'description': 'Net official development assistance and official aid received (current US$)',
        'agg':         'sum',
    },
    'DT.ODA.ODAT.PC.ZS': {
        'source':      'World Bank',
        'description': 'Net ODA received per capita (current US$)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'BX.TRF.PWKR.CD.DT': {
        'source':      'World Bank',
        'description': 'Personal remittances, received (current US$)',
        'agg':         'sum',
    },

    # Government & Public Sector
    'GC.TAX.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Tax revenue (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'GC.TAX.IMPT.ZS': {
        'source':      'World Bank',
        'description': 'Tax revenue (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
    'GC.XPN.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Government expenditure (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'MS.MIL.XPND.GD.ZS': {
        'source':      'World Bank',
        'description': 'Military expenditure (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'IC.BUS.EASE.XQ': {
        'source':      'World Bank',
        'description': 'Ease of doing business score (0 = lowest, 100 = best)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'IC.REG.DURS': {
        'source':      'World Bank',
        'description': 'Time required to start a business (days)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },

    # Governance Indicators
    'VA.EST': {
        'source':      'World Bank',
        'description': 'Voice and Accountability: Estimate',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'PV.EST': {
        'source':      'World Bank',
        'description': 'Political Stability and Absence of Violence: Estimate',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'GE.EST': {
        'source':      'World Bank',
        'description': 'Government Effectiveness: Estimate',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'RQ.EST': {
        'source':      'World Bank',
        'description': 'Regulatory Quality: Estimate',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'RL.EST': {
        'source':      'World Bank',
        'description': 'Rule of Law: Estimate',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'CC.EST': {
        'source':      'World Bank',
        'description': 'Control of Corruption: Estimate',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Social - Education
    'SE.PRM.NENR': {
        'source':      'World Bank',
        'description': 'School enrollment, primary (% net)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.SEC.NENR': {
        'source':      'World Bank',
        'description': 'School enrollment, secondary (% net)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.TER.ENRR': {
        'source':      'World Bank',
        'description': 'School enrollment, tertiary (% gross)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.XPD.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Government expenditure on education, total (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD'
    },
    'SE.ADT.LITR.ZS': {
        'source':      'World Bank',
        'description': 'Literacy rate, adult total (% of people ages 15 and above)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.ADT.LITR.FE.ZS': {
        'source':      'World Bank',
        'description': 'Literacy rate, adult female (% of females ages 15 and above)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.PRM.CMPT.ZS': {
        'source':      'World Bank',
        'description': 'Primary completion rate, total (% of relevant age group)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.PRM.ENRR.FE': {
        'source':      'World Bank',
        'description': 'School enrollment, primary, female (% gross)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Social - Health
    'SH.DYN.MORT': {
        'source':      'World Bank',
        'description': 'Mortality rate, under-5 (per 1,000 live births)',
        'agg':         'mean',
    },
    'SH.DYN.NMRT': {
        'source':      'World Bank',
        'description': 'Mortality rate, neonatal (per 1,000 live births)',
        'agg':         'mean',
    },
    'SH.STA.MMRT': {
        'source':      'World Bank',
        'description': 'Maternal mortality ratio (modeled estimate, per 100,000 live births)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.XPD.CHEX.GD.ZS': {
        'source':      'World Bank',
        'description': 'Current health expenditure (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SH.XPD.CHEX.PC.CD': {
        'source':      'World Bank',
        'description': 'Current health expenditure per capita (current US$)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.IMM.MEAS': {
        'source':      'World Bank',
        'description': 'Immunization, measles (% of children ages 12-23 months)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.MED.PHYS.ZS': {
        'source':      'World Bank',
        'description': 'Physicians (per 1,000 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.MED.BEDS.ZS': {
        'source':      'World Bank',
        'description': 'Hospital beds (per 1,000 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.HIV.INCD.ZS': {
        'source':      'World Bank',
        'description': 'Incidence of HIV (% of uninfected population ages 15-49)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.STA.DIAB.ZS': {
        'source':      'World Bank',
        'description': 'Diabetes prevalence (% of population ages 20 to 79)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Social - Labor & Employment
    'SL.TLF.CACT.FM.ZS': {
        'source':      'World Bank',
        'description': 'Female labor force participation (% ages 15+)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.UEM.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Unemployment, total (% of labor force)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.UEM.1524.ZS': {
        'source':      'World Bank',
        'description': 'Unemployment, youth total (% of total labor force ages 15-24)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.EMP.TOTL.SP.ZS': {
        'source':      'World Bank',
        'description': 'Employment to population ratio, 15+, total (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.GDP.PCAP.EM.KD': {
        'source':      'World Bank',
        'description': 'GDP per person employed (constant 2017 PPP $)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SL.TLF.TOTL.IN': {
        'source':      'World Bank',
        'description': 'Labor force, total',
        'agg':         'sum',
    },
    'SL.AGR.EMPL.ZS': {
        'source':      'World Bank',
        'description': 'Employment in agriculture (% of total employment)',
        'agg':         'weighted',
        'weight_by':   'SL.TLF.TOTL.IN',
    },
    'SL.IND.EMPL.ZS': {
        'source':      'World Bank',
        'description': 'Employment in industry (% of total employment)',
        'agg':         'weighted',
        'weight_by':   'SL.TLF.TOTL.IN',
    },
    'SL.SRV.EMPL.ZS': {
        'source':      'World Bank',
        'description': 'Employment in services (% of total employment)',
        'agg':         'weighted',
        'weight_by':   'SL.TLF.TOTL.IN',
    },

    # Social - Gender
    'SG.GEN.PARL.ZS': {
        'source':      'World Bank',
        'description': 'Proportion of seats held by women in national parliaments (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SG.LAW.INDX': {
        'source':      'World Bank',
        'description': 'Women Business and the Law Index Score (1-100)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SP.DYN.SMAM.FE': {
        'source':      'World Bank',
        'description': 'Age at first marriage, female',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SP.DYN.TFRT.IN': {
        'source':      'World Bank',
        'description': 'Fertility rate, total (births per woman)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SG.VAW.ARGU.ZS': {
        'source':      'World Bank',
        'description': 'Women who believe a husband is justified in beating his wife when she argues with him (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SG.GEN.LMGP.MS.ZS': {
        'source':      'World Bank',
        'description': 'Firms with female top manager (% of firms)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SG.GEN.PARL.ZS': {
        'source':      'World Bank',
        'description': 'Proportion of seats held by women in national parliaments (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Infrastructure & Technology
    'EG.ELC.ACCS.ZS': {
        'source':      'World Bank',
        'description': 'Access to electricity (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL'
    },
    'IT.NET.USER.ZS': {
        'source':      'World Bank',
        'description': 'Individuals using the Internet (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL'
    },
    'IT.CEL.SETS.P2': {
        'source':      'World Bank',
        'description': 'Mobile cellular subscriptions (per 100 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IT.NET.BBND.P2': {
        'source':      'World Bank',
        'description': 'Fixed broadband subscriptions (per 100 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IS.RRS.TOTL.KM': {
        'source':      'World Bank',
        'description': 'Rail lines (total route-km)',
        'agg':         'sum',
    },
    'IS.ROD.TOTL.KM': {
        'source':      'World Bank',
        'description': 'Roads, total network (km)',
        'agg':         'sum',
    },
    'IS.ROD.PAVE.ZS': {
        'source':      'World Bank',
        'description': 'Roads, paved (% of total roads)',
        'agg':         'weighted',
        'weight_by':   'IS.ROD.TOTL.KM',
    },
    'IS.AIR.PSGR': {
        'source':      'World Bank',
        'description': 'Air transport, passengers carried',
        'agg':         'sum',
    },
    'IT.NET.SECR.P6': {
        'source':      'World Bank',
        'description': 'Secure Internet servers (per 1 million people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IQ.SCI.OVRL': {
        'source':      'World Bank',
        'description': 'Statistical Capacity score (Overall average)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Energy
    'EG.USE.PCAP.KG.OE': {
        'source':      'World Bank',
        'description': 'Energy use (kg of oil equivalent per capita)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.ELC.PROD.KH': {
        'source':      'World Bank',
        'description': 'Electricity production (kWh)',
        'agg':         'sum',
    },
    'EG.ELC.COAL.ZS': {
        'source':      'World Bank',
        'description': 'Electricity production from coal sources (% of total)',
        'agg':         'weighted',
        'weight_by':   'EG.ELC.PROD.KH',
    },
    'EG.ELC.NUCL.ZS': {
        'source':      'World Bank',
        'description': 'Electricity production from nuclear sources (% of total)',
        'agg':         'weighted',
        'weight_by':   'EG.ELC.PROD.KH',
    },
    'EG.ELC.RNWX.ZS': {
        'source':      'World Bank',
        'description': 'Electricity production from renewable sources, excluding hydroelectric (% of total)',
        'agg':         'weighted',
        'weight_by':   'EG.ELC.PROD.KH',
    },
    'EG.ELC.HYRO.ZS': {
        'source':      'World Bank',
        'description': 'Electricity production from hydroelectric sources (% of total)',
        'agg':         'weighted',
        'weight_by':   'EG.ELC.PROD.KH',
    },
    'EG.ELC.LOSS.ZS': {
        'source':      'World Bank',
        'description': 'Electric power transmission and distribution losses (% of output)',
        'agg':         'weighted',
        'weight_by':   'EG.ELC.PROD.KH',
    },
    'EG.FEC.RNEW.ZS': {
        'source':      'World Bank',
        'description': 'Renewable energy consumption (% of total final energy consumption)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # Environment & Climate
    'EN.GHG.CO2.PC.CE.AR5': {
        'source':      'World Bank',
        'description': 'CO₂ emissions per capita (t CO₂e/capita)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.GHG.CO2.MT.CE.AR5': {
        'source':      'World Bank',
        'description': 'Total CO₂ emissions (Mt CO₂e)',
        'agg':         'sum',
    },
    'EN.ATM.PM25.MC.M3': {
        'source':      'World Bank',
        'description': 'PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.ATM.METH.KT.CE': {
        'source':      'World Bank',
        'description': 'Methane emissions (kt of CO2 equivalent)',
        'agg':         'sum',
    },
    'EN.CLC.GHGR.MT.CE': {
        'source':      'World Bank',
        'description': 'Total greenhouse gas emissions (kt of CO2 equivalent)',
        'agg':         'sum',
    },
    'ER.PTD.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Terrestrial and marine protected areas (% of total territorial area)',
        'agg':         'weighted',
        'weight_by':   'AG.SRF.TOTL.K2',
    },
    'AG.LND.FRST.ZS': {
        'source':      'World Bank',
        'description': 'Forest area (% of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },
    'ER.H2O.FWTL.ZS': {
        'source':      'World Bank',
        'description': 'Annual freshwater withdrawals, total (% of internal resources)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'ER.H2O.FWST.ZS': {
        'source':      'World Bank',
        'description': 'Level of water stress: freshwater withdrawal as a proportion of available freshwater resources',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.POP.DNST': {
        'source':      'World Bank',
        'description': 'Population density (people per sq. km of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },

    # Agriculture
    'AG.LND.AGRI.ZS': {
        'source':      'World Bank',
        'description': 'Agricultural land (% of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },
    'AG.LND.CROP.ZS': {
        'source':      'World Bank',
        'description': 'Arable land (% of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },
    'AG.YLD.CREL.KG': {
        'source':      'World Bank',
        'description': 'Cereal yield (kg per hectare)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.CROP.ZS',
    },
    'AG.PRD.FOOD.XD': {
        'source':      'World Bank',
        'description': 'Food production index (2014-2016 = 100)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'AG.CON.FERT.ZS': {
        'source':      'World Bank',
        'description': 'Fertilizer consumption (kilograms per hectare of arable land)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.CROP.ZS',
    },
    'AG.LND.IRIG.AG.ZS': {
        'source':      'World Bank',
        'description': 'Agricultural irrigated land (% of total agricultural land)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.AGRI.ZS',
    },
    'NV.AGR.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Agriculture, forestry, and fishing, value added (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },

    # Urban Development
    'SP.URB.GROW': {
        'source':      'World Bank',
        'description': 'Urban population growth (annual %)',
        'agg':         'weighted',
        'weight_by':   'SP.URB.TOTL',
    },
    'EN.URB.LCTY': {
        'source':      'World Bank',
        'description': 'Population in largest city',
        'agg':         'sum',
    },
    'EN.URB.LCTY.UR.ZS': {
        'source':      'World Bank',
        'description': 'Population in the largest city (% of urban population)',
        'agg':         'weighted',
        'weight_by':   'SP.URB.TOTL',
    },
    'EN.URB.MCTY': {
        'source':      'World Bank',
        'description': 'Population in urban agglomerations of more than 1 million',
        'agg':         'sum',
    },
    'EN.URB.MCTY.TL.ZS': {
        'source':      'World Bank',
        'description': 'Population in urban agglomerations of more than 1 million (% of total population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.POP.SLUM.UR.ZS': {
        'source':      'World Bank',
        'description': 'Population living in slums (% of urban population)',
        'agg':         'weighted',
        'weight_by':   'SP.URB.TOTL',
    },

    # Water, Sanitation & Waste
    'SH.H2O.SMDW.ZS': {
        'source':      'World Bank',
        'description': 'People using safely managed drinking water services (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.STA.SMSS.ZS': {
        'source':      'World Bank',
        'description': 'People using safely managed sanitation services (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.H2O.BASW.ZS': {
        'source':      'World Bank',
        'description': 'People using at least basic drinking water services (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.STA.BASS.ZS': {
        'source':      'World Bank',
        'description': 'People using at least basic sanitation services (% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.POP.DNST': {
        'source':      'World Bank',
        'description': 'Population density (people per sq. km of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },

    # Science & Innovation
    'IP.PAT.RESD': {
        'source':      'World Bank',
        'description': 'Patent applications, residents',
        'agg':         'sum',
    },
    'IP.PAT.NRES': {
        'source':      'World Bank',
        'description': 'Patent applications, nonresidents',
        'agg':         'sum',
    },
    'IP.JRN.ARTC.SC': {
        'source':      'World Bank',
        'description': 'Scientific and technical journal articles',
        'agg':         'sum',
    },
    'GB.XPD.RSDV.GD.ZS': {
        'source':      'World Bank',
        'description': 'Research and development expenditure (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SP.POP.SCIE.RD.P6': {
        'source':      'World Bank',
        'description': 'Researchers in R&D (per million people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IP.TMK.TOTL': {
        'source':      'World Bank',
        'description': 'Trademark applications, total',
        'agg':         'sum',
    }
}

categorized_indicators = {
    "General": [
        'SP.POP.TOTL',         # Population, total
        'SP.POP.GROW',         # Population growth (annual %)
        'SP.URB.TOTL',         # Urban population
        'SP.URB.TOTL.IN.ZS',   # Urban population (% of total)
        'SP.RUR.TOTL',         # Rural population
        'SP.DYN.LE00.IN',      # Life expectancy at birth, total (years)
        'AG.SRF.TOTL.K2',      # Surface area (sq. km)
        'AG.LND.TOTL.K2',      # Land area (sq. km)
        'EN.POP.DNST'          # Population density (people per sq. km of land area)
    ],

    "Economy": [
        'NY.GDP.MKTP.CD',       # GDP (current US$)
        'NY.GDP.MKTP.PP.CD',    # GDP, PPP (current international $)
        'NY.GDP.PCAP.PP.CD',    # GDP per capita, PPP (current international $)
        'NY.GDP.MKTP.KD.ZG',    # GDP growth (annual %)
        'NY.GDP.PCAP.CD',       # GDP per capita (current US$)
        'NY.GNP.PCAP.PP.CD',    # GNI per capita, PPP (current international $)
        'NY.ADJ.NNTY.PC.CD',    # Adjusted net national income per capita (current US$)
        'FP.CPI.TOTL.ZG',       # Inflation, consumer prices (annual %)
        'PA.NUS.FCRF'           # Official exchange rate (LCU per US$, period average)
    ],

    "Inequality & Poverty": [
        'SI.POV.DDAY',          # Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)
        'SI.POV.LMIC',          # Poverty headcount ratio at $3.65 a day (2017 PPP) (% of population)
        'SI.POV.NAHC',          # Poverty headcount ratio at national poverty lines (% of population)
        'SI.POV.GINI',          # Gini index
        'SI.DST.FRST.20',       # Income share held by lowest 20%
        'SI.DST.10TH.10'        # Income share held by highest 10%
    ],

    "Trade & Finance": [
        'NE.EXP.GNFS.CD',       # Exports of goods and services (BoP, current US$)
        'NE.IMP.GNFS.CD',       # Imports of goods and services (BoP, current US$)
        'NE.TRD.GNFS.CD',       # Trade in goods and services (BoP, current US$)
        'NE.TRD.GNFS.ZS',       # Trade (% of GDP)
        'BN.CAB.XOKA.CD',       # Current account balance (BoP, current US$)
        'BN.CAB.XOKA.GD.ZS',    # Current account balance (% of GDP)
        'FI.RES.TOTL.CD',       # Total reserves (includes gold, current US$)
        'FI.RES.TOTL.MO',       # Total reserves in months of imports
        'LP.LPI.OVRL.XQ',       # Logistics performance index: Overall (1=low to 5=high)
        'LP.EXP.DURS.MD',       # Time to export, median case (days)
        'BM.GSR.ROYL.CD',       # Charges for the use of intellectual property, payments (BoP, current US$)
        'TX.VAL.TECH.CD',       # High-technology exports (current US$)
        'TX.VAL.TECH.MF.ZS'     # High-technology exports (% of manufactured exports)
    ],

    "Investment & Financial Sector": [
        'BX.KLT.DINV.WD.GD.ZS',  # FDI, net inflows (% of GDP)
        'BM.KLT.DINV.WD.GD.ZS',  # FDI, net outflows (% of GDP)
        'BX.KLT.DINV.CD.WD',     # Foreign direct investment, net inflows (BoP, current US$)
        'NE.GDI.TOTL.ZS',        # Gross capital formation (% of GDP)
        'FS.AST.PRVT.GD.ZS',     # Domestic credit to private sector (% of GDP)
        'CM.MKT.LCAP.CD',        # Market capitalization of listed domestic companies (current US$)
        'CM.MKT.LCAP.GD.ZS',     # Market capitalization of listed domestic companies (% of GDP)
        'FB.CBK.BRCH.P5',        # Commercial bank branches (per 100,000 adults)
        'FR.INR.LEND',           # Lending interest rate (%)
        'FR.INR.RINR'            # Real interest rate (%)
    ],

    "Debt & Aid": [
        'DT.DOD.DECT.CD',        # External debt stocks, total (current US$)
        'DT.DOD.DECT.GN.ZS',     # External debt stocks (% of GNI)
        'DT.TDS.DECT.GN.ZS',     # Total debt service (% of GNI)
        'GC.DOD.TOTL.CN',        # Central government debt, total (current LCU)
        'GC.DOD.TOTL.GD.ZS',     # Central government debt, total (% of GDP)
        'DT.ODA.ODAT.GN.ZS',     # ODA received (% of GNI)
        'DT.ODA.ALLD.CD',        # Net official development assistance and official aid received (current US$)
        'DT.ODA.ODAT.PC.ZS',     # Net ODA received per capita (current US$)
        'BX.TRF.PWKR.CD.DT'      # Personal remittances, received (current US$)
    ],

    "Government & Governance": [
        'GC.TAX.TOTL.GD.ZS',     # Tax revenue (% of GDP)
        'GC.TAX.IMPT.ZS',        # Tax revenue (% of GDP)
        'GC.XPN.TOTL.GD.ZS',     # Government expenditure (% of GDP)
        'MS.MIL.XPND.GD.ZS',     # Military expenditure (% of GDP)
        'IC.BUS.EASE.XQ',        # Ease of doing business score (0 = lowest, 100 = best)
        'IC.REG.DURS',           # Time required to start a business (days)
        'VA.EST',                # Voice and Accountability: Estimate
        'PV.EST',                # Political Stability and Absence of Violence: Estimate
        'GE.EST',                # Government Effectiveness: Estimate
        'RQ.EST',                # Regulatory Quality: Estimate
        'RL.EST',                # Rule of Law: Estimate
        'CC.EST'                 # Control of Corruption: Estimate
    ],

    "Education": [
        'SE.PRM.NENR',           # School enrollment, primary (% net)
        'SE.SEC.NENR',           # School enrollment, secondary (% net)
        'SE.TER.ENRR',           # School enrollment, tertiary (% gross)
        'SE.XPD.TOTL.GD.ZS',     # Government expenditure on education, total (% of GDP)
        'SE.ADT.LITR.ZS',        # Literacy rate, adult total (% of people ages 15 and above)
        'SE.ADT.LITR.FE.ZS',     # Literacy rate, adult female (% of females ages 15 and above)
        'SE.PRM.CMPT.ZS',        # Primary completion rate, total (% of relevant age group)
        'SE.PRM.ENRR.FE'         # School enrollment, primary, female (% gross)
    ],

    "Health": [
        'SH.DYN.MORT',           # Mortality rate, under-5 (per 1,000 live births)
        'SH.DYN.NMRT',           # Mortality rate, neonatal (per 1,000 live births)
        'SH.STA.MMRT',           # Maternal mortality ratio (modeled estimate, per 100,000 live births)
        'SH.XPD.CHEX.GD.ZS',     # Current health expenditure (% of GDP)
        'SH.XPD.CHEX.PC.CD',     # Current health expenditure per capita (current US$)
        'SH.IMM.MEAS',           # Immunization, measles (% of children ages 12-23 months)
        'SH.MED.PHYS.ZS',        # Physicians (per 1,000 people)
        'SH.MED.BEDS.ZS',        # Hospital beds (per 1,000 people)
        'SH.HIV.INCD.ZS',        # Incidence of HIV (% of uninfected population ages 15-49)
        'SH.STA.DIAB.ZS'         # Diabetes prevalence (% of population ages 20 to 79)
    ],

    "Labor & Employment": [
        'SL.TLF.CACT.FM.ZS',     # Female labor force participation (% ages 15+)
        'SL.UEM.TOTL.ZS',        # Unemployment, total (% of labor force)
        'SL.UEM.1524.ZS',        # Unemployment, youth total (% of total labor force ages 15-24)
        'SL.EMP.TOTL.SP.ZS',     # Employment to population ratio, 15+, total (%)
        'SL.GDP.PCAP.EM.KD',     # GDP per person employed (constant 2017 PPP $)
        'SL.TLF.TOTL.IN',        # Labor force, total
        'SL.AGR.EMPL.ZS',        # Employment in agriculture (% of total employment)
        'SL.IND.EMPL.ZS',        # Employment in industry (% of total employment)
        'SL.SRV.EMPL.ZS'         # Employment in services (% of total employment)
    ],

    "Gender": [
        'SG.GEN.PARL.ZS',        # Proportion of seats held by women in national parliaments (%)
        'SG.LAW.INDX',           # Women Business and the Law Index Score (1-100)
        'SP.DYN.SMAM.FE',        # Age at first marriage, female
        'SP.DYN.TFRT.IN',        # Fertility rate, total (births per woman)
        'SG.VAW.ARGU.ZS',        # Women who believe a husband is justified in beating his wife when she argues with him (%)
        'SG.GEN.LMGP.MS.ZS',     # Firms with female top manager (% of firms)
        'SL.TLF.CACT.FM.ZS'      # Female labor force participation (% ages 15+)
    ],

    "Infrastructure & Technology": [
        'EG.ELC.ACCS.ZS',        # Access to electricity (% of population)
        'IT.NET.USER.ZS',        # Individuals using the Internet (% of population)
        'IT.CEL.SETS.P2',        # Mobile cellular subscriptions (per 100 people)
        'IT.NET.BBND.P2',        # Fixed broadband subscriptions (per 100 people)
        'IS.RRS.TOTL.KM',        # Rail lines (total route-km)
        'IS.ROD.TOTL.KM',        # Roads, total network (km)
        'IS.ROD.PAVE.ZS',        # Roads, paved (% of total roads)
        'IS.AIR.PSGR',           # Air transport, passengers carried
        'IT.NET.SECR.P6',        # Secure Internet servers (per 1 million people)
        'IQ.SCI.OVRL'            # Statistical Capacity score (Overall average)
    ],

    "Energy": [
        'EG.USE.PCAP.KG.OE',     # Energy use (kg of oil equivalent per capita)
        'EG.ELC.PROD.KH',        # Electricity production (kWh)
        'EG.ELC.COAL.ZS',        # Electricity production from coal sources (% of total)
        'EG.ELC.NUCL.ZS',        # Electricity production from nuclear sources (% of total)
        'EG.ELC.RNWX.ZS',        # Electricity production from renewable sources, excluding hydroelectric (% of total)
        'EG.ELC.HYRO.ZS',        # Electricity production from hydroelectric sources (% of total)
        'EG.ELC.LOSS.ZS',        # Electric power transmission and distribution losses (% of output)
        'EG.FEC.RNEW.ZS'         # Renewable energy consumption (% of total final energy consumption)
    ],

    "Environment & Climate": [
        'EN.GHG.CO2.PC.CE.AR5',  # CO₂ emissions per capita (t CO₂e/capita)
        'EN.GHG.CO2.MT.CE.AR5',  # Total CO₂ emissions (Mt CO₂e)
        'EN.ATM.PM25.MC.M3',     # PM2.5 air pollution, mean annual exposure (micrograms per cubic meter)
        'EN.ATM.METH.KT.CE',     # Methane emissions (kt of CO2 equivalent)
        'EN.CLC.GHGR.MT.CE',     # Total greenhouse gas emissions (kt of CO2 equivalent)
        'ER.PTD.TOTL.ZS',        # Terrestrial and marine protected areas (% of total territorial area)
        'AG.LND.FRST.ZS',        # Forest area (% of land area)
        'ER.H2O.FWTL.ZS',        # Annual freshwater withdrawals, total (% of internal resources)
        'ER.H2O.FWST.ZS'         # Level of water stress: freshwater withdrawal as a proportion of available freshwater resources
    ],

    "Agriculture": [
        'AG.LND.AGRI.ZS',        # Agricultural land (% of land area)
        'AG.LND.CROP.ZS',        # Arable land (% of land area)
        'AG.YLD.CREL.KG',        # Cereal yield (kg per hectare)
        'AG.PRD.FOOD.XD',        # Food production index (2014-2016 = 100)
        'AG.CON.FERT.ZS',        # Fertilizer consumption (kilograms per hectare of arable land)
        'AG.LND.IRIG.AG.ZS',     # Agricultural irrigated land (% of total agricultural land)
        'NV.AGR.TOTL.ZS'         # Agriculture, forestry, and fishing, value added (% of GDP)
    ],

    "Urban Development": [
        'SP.URB.GROW',           # Urban population growth (annual %)
        'EN.URB.LCTY',           # Population in largest city
        'EN.URB.LCTY.UR.ZS',     # Population in the largest city (% of urban population)
        'EN.URB.MCTY',           # Population in urban agglomerations of more than 1 million
        'EN.URB.MCTY.TL.ZS',     # Population in urban agglomerations of more than 1 million (% of total population)
        'EN.POP.SLUM.UR.ZS'      # Population living in slums (% of urban population)
    ],

    "Water, Sanitation & Waste": [
        'SH.H2O.SMDW.ZS',        # People using safely managed drinking water services (% of population)
        'SH.STA.SMSS.ZS',        # People using safely managed sanitation services (% of population)
        'SH.H2O.BASW.ZS',        # People using at least basic drinking water services (% of population)
        'SH.STA.BASS.ZS'         # People using at least basic sanitation services (% of population)
    ],

    "Science & Innovation": [
        'IP.PAT.RESD',           # Patent applications, residents
        'IP.PAT.NRES',           # Patent applications, nonresidents
        'IP.JRN.ARTC.SC',        # Scientific and technical journal articles
        'GB.XPD.RSDV.GD.ZS',     # Research and development expenditure (% of GDP)
        'SP.POP.SCIE.RD.P6',     # Researchers in R&D (per million people)
        'IP.TMK.TOTL'            # Trademark applications, total
    ]
}

# Extract the list of all indicator codes needed for data download
all_indicator_codes = list(indicators.keys())
