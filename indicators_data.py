# ------------------------------------------------------------------
# 1. Master indicator catalogue
#    (keys = World-Bank series codes; values = metadata + aggregation)
# ------------------------------------------------------------------
indicators = {
    # -----------------------------  GENERAL  -----------------------------
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
    'EN.POP.DNST': {
        'source':      'World Bank',
        'description': 'Population density (people / sq km of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },

    # ------------------------------  ECONOMY  -----------------------------
    'NY.GDP.MKTP.CD': {
        'source':      'World Bank',
        'description': 'GDP (current US$)',
        'agg':         'sum',
    },
    'NY.GDP.MKTP.PP.CD': {
        'source':      'World Bank',
        'description': 'GDP, PPP (current international $)',
        'agg':         'sum',
    },
    'NY.GDP.PCAP.PP.CD': {
        'source':      'World Bank',
        'description': 'GDP per capita, PPP (current international $)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
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
        'weight_by':   'SP.POP.TOTL',
    },
    'NY.GNP.PCAP.PP.CD': {
        'source':      'World Bank',
        'description': 'GNI per capita, PPP (current international $)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'NY.ADJ.NNTY.PC.CD': {
        'source':      'World Bank',
        'description': 'Adjusted net national income per capita (current US$)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'FP.CPI.TOTL.ZG': {
        'source':      'World Bank',
        'description': 'Inflation, consumer prices (annual %)',
        'agg':         'mean',
    },
    'PA.NUS.FCRF': {
        'source':      'World Bank',
        'description': 'Official exchange rate (LCU / US$, period avg.)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },

    # ---------------------  INEQUALITY & POVERTY  ------------------------
    'SI.POV.DDAY': {
        'source':      'World Bank',
        'description': 'Poverty headcount ($2.15 / day, 2017 PPP, % of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.POV.LMIC': {
        'source':      'World Bank',
        'description': 'Poverty headcount ($3.65 / day, 2017 PPP, % of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.POV.NAHC': {
        'source':      'World Bank',
        'description': 'Poverty headcount at national line (% of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.POV.GINI': {
        'source':      'World Bank',
        'description': 'Gini index',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.DST.FRST.20': {
        'source':      'World Bank',
        'description': 'Income share held by lowest 20 %',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SI.DST.10TH.10': {
        'source':      'World Bank',
        'description': 'Income share held by highest 10 %',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ------------------------  TRADE & FINANCE  --------------------------
    'NE.EXP.GNFS.CD': {
        'source':      'World Bank',
        'description': 'Exports of goods & services (current US$)',
        'agg':         'sum',
    },
    'NE.IMP.GNFS.CD': {
        'source':      'World Bank',
        'description': 'Imports of goods & services (current US$)',
        'agg':         'sum',
    },
    'NE.TRD.GNFS.CD': {
        'source':      'World Bank',
        'description': 'Trade in goods & services (current US$)',
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
        'description': 'Current-account balance (current US$)',
        'agg':         'sum',
    },
    'BN.CAB.XOKA.GD.ZS': {
        'source':      'World Bank',
        'description': 'Current-account balance (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FI.RES.TOTL.CD': {
        'source':      'World Bank',
        'description': 'Total reserves incl. gold (current US$)',
        'agg':         'sum',
    },
    'FI.RES.TOTL.MO': {
        'source':      'World Bank',
        'description': 'Total reserves (months of imports)',
        'agg':         'weighted',
        'weight_by':   'NE.IMP.GNFS.CD',
    },
    'LP.LPI.OVRL.XQ': {
        'source':      'World Bank',
        'description': 'Logistics Performance Index (1–5)',
        'agg':         'mean',
    },
    'LP.EXP.DURS.MD': {
        'source':      'World Bank',
        'description': 'Time to export, median case (days)',
        'agg':         'mean',
    },
    'BM.GSR.ROYL.CD': {
        'source':      'World Bank',
        'description': 'Royalty payments for IP (current US$)',
        'agg':         'sum',
    },
    'TX.VAL.TECH.CD': {
        'source':      'World Bank',
        'description': 'High-tech exports (current US$)',
        'agg':         'sum',
    },
    'TX.VAL.TECH.MF.ZS': {
        'source':      'World Bank',
        'description': 'High-tech exports (% of manufactured exports)',
        'agg':         'weighted',
        'weight_by':   'NE.EXP.GNFS.CD',
    },

    # -----------------  INVESTMENT & FINANCIAL SECTOR  ------------------
    'BX.KLT.DINV.WD.GD.ZS': {
        'source':      'World Bank',
        'description': 'FDI net inflows (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
    'BM.KLT.DINV.WD.GD.ZS': {
        'source':      'World Bank',
        'description': 'FDI net outflows (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
    'BX.KLT.DINV.CD.WD': {
        'source':      'World Bank',
        'description': 'FDI net inflows (current US$)',
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
        'description': 'Market cap. of listed firms (current US$)',
        'agg':         'sum',
    },
    'CM.MKT.LCAP.GD.ZS': {
        'source':      'World Bank',
        'description': 'Market cap. of listed firms (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'FB.CBK.BRCH.P5': {
        'source':      'World Bank',
        'description': 'Commercial bank branches (per 100 k adults)',
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

    # -------------------------  DEBT & AID  -----------------------------
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
        'description': 'Central-govt. debt, total (current LCU)',
        'agg':         'sum',
    },
    'GC.DOD.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Central-govt. debt, total (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'DT.ODA.ODAT.GN.ZS': {
        'source':      'World Bank',
        'description': 'ODA received (% of GNI)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'DT.ODA.ALLD.CD': {
        'source':      'World Bank',
        'description': 'Net ODA & official aid (current US$)',
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
        'description': 'Personal remittances received (current US$)',
        'agg':         'sum',
    },

    # ------------------  GOVERNMENT & GOVERNANCE  -----------------------
    'GC.TAX.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Tax revenue (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'GC.TAX.IMPT.ZS': {
        'source':      'World Bank',
        'description': 'Taxes on imports (% of GDP)',
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
    'VA.EST': {
        'source':      'World Bank',
        'description': 'Voice & Accountability (estimate)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'PV.EST': {
        'source':      'World Bank',
        'description': 'Political Stability / No Violence (estimate)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'GE.EST': {
        'source':      'World Bank',
        'description': 'Government Effectiveness (estimate)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'RQ.EST': {
        'source':      'World Bank',
        'description': 'Regulatory Quality (estimate)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'RL.EST': {
        'source':      'World Bank',
        'description': 'Rule of Law (estimate)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'CC.EST': {
        'source':      'World Bank',
        'description': 'Control of Corruption (estimate)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ---------------------------  EDUCATION  ----------------------------
    'SE.PRM.NENR': {
        'source':      'World Bank',
        'description': 'Primary school enrollment (% net)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.SEC.NENR': {
        'source':      'World Bank',
        'description': 'Secondary school enrollment (% net)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.TER.ENRR': {
        'source':      'World Bank',
        'description': 'Tertiary enrollment (% gross)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.XPD.TOTL.GD.ZS': {
        'source':      'World Bank',
        'description': 'Government education outlays (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SE.ADT.LITR.ZS': {
        'source':      'World Bank',
        'description': 'Adult literacy rate (%% ages 15+)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.ADT.LITR.FE.ZS': {
        'source':      'World Bank',
        'description': 'Adult literacy, female (%% ages 15+)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.PRM.CMPT.ZS': {
        'source':      'World Bank',
        'description': 'Primary completion rate (%% of cohort)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SE.PRM.ENRR.FE': {
        'source':      'World Bank',
        'description': 'Primary enrollment, female (%% gross)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ----------------------------  HEALTH  ------------------------------
    'SH.DYN.MORT': {
        'source':      'World Bank',
        'description': 'Under-5 mortality (per 1 000 births)',
        'agg':         'mean',
    },
    'SH.DYN.NMRT': {
        'source':      'World Bank',
        'description': 'Neonatal mortality (per 1 000 births)',
        'agg':         'mean',
    },
    'SH.STA.MMRT': {
        'source':      'World Bank',
        'description': 'Maternal mortality ratio (per 100 000 births)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.XPD.CHEX.GD.ZS': {
        'source':      'World Bank',
        'description': 'Current health outlays (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SH.XPD.CHEX.PC.CD': {
        'source':      'World Bank',
        'description': 'Health expenditure per capita (current US$)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.IMM.MEAS': {
        'source':      'World Bank',
        'description': 'Measles immunization (%% of children)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.MED.PHYS.ZS': {
        'source':      'World Bank',
        'description': 'Physicians (per 1 000 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.MED.BEDS.ZS': {
        'source':      'World Bank',
        'description': 'Hospital beds (per 1 000 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.HIV.INCD.ZS': {
        'source':      'World Bank',
        'description': 'HIV incidence (%% ages 15-49)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.STA.DIAB.ZS': {
        'source':      'World Bank',
        'description': 'Diabetes prevalence (%% ages 20-79)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ---------------------  LABOUR / EMPLOYMENT  ------------------------
    'SL.TLF.CACT.FM.ZS': {
        'source':      'World Bank',
        'description': 'Female labour-force participation (%% 15+)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.UEM.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Unemployment (%% of labour force)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.UEM.1524.ZS': {
        'source':      'World Bank',
        'description': 'Youth unemployment (%% ages 15-24)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SL.EMP.TOTL.SP.ZS': {
        'source':      'World Bank',
        'description': 'Employment-to-population ratio (%%, 15+)',
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
        'description': 'Labour force, total',
        'agg':         'sum',
    },
    'SL.AGR.EMPL.ZS': {
        'source':      'World Bank',
        'description': 'Employment in agriculture (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SL.TLF.TOTL.IN',
    },
    'SL.IND.EMPL.ZS': {
        'source':      'World Bank',
        'description': 'Employment in industry (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SL.TLF.TOTL.IN',
    },
    'SL.SRV.EMPL.ZS': {
        'source':      'World Bank',
        'description': 'Employment in services (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SL.TLF.TOTL.IN',
    },

    # ----------------------------  GENDER  ------------------------------
    'SG.GEN.PARL.ZS': {
        'source':      'World Bank',
        'description': 'Parliament seats held by women (%%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SG.LAW.INDX': {
        'source':      'World Bank',
        'description': 'Women, Business & Law Index (1–100)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SP.DYN.SMAM.FE': {
        'source':      'World Bank',
        'description': 'Mean age at first marriage – women',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SP.DYN.TFRT.IN': {
        'source':      'World Bank',
        'description': 'Total fertility rate (births / woman)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SG.VAW.ARGU.ZS': {
        'source':      'World Bank',
        'description': 'Women who justify wife-beating when argued with husband (%%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ------------------  INFRASTRUCTURE & TECHNOLOGY  ------------------
    'EG.ELC.ACCS.ZS': {
        'source':      'World Bank',
        'description': 'Access to electricity (%% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IT.NET.USER.ZS': {
        'source':      'World Bank',
        'description': 'Internet users (%% of population)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
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
        'description': 'Rail lines (route-km)',
        'agg':         'sum',
    },
    'IS.ROD.TOTL.KM': {
        'source':      'World Bank',
        'description': 'Road network length (km)',
        'agg':         'sum',
    },
    'IS.ROD.PAVE.ZS': {
        'source':      'World Bank',
        'description': 'Roads paved (%% of total)',
        'agg':         'weighted',
        'weight_by':   'IS.ROD.TOTL.KM',
    },
    'IS.AIR.PSGR': {
        'source':      'World Bank',
        'description': 'Air passengers carried',
        'agg':         'sum',
    },
    'IT.NET.SECR.P6': {
        'source':      'World Bank',
        'description': 'Secure Internet servers (per 1 M people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ------------------------------  ENERGY  ----------------------------
    'EG.USE.PCAP.KG.OE': {
        'source':      'World Bank',
        'description': 'Energy use (kg oil eq. per capita)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.ELC.COAL.ZS': {
        'source':      'World Bank',
        'description': 'Electricity from coal sources (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.ELC.NUCL.ZS': {
        'source':      'World Bank',
        'description': 'Electricity from nuclear sources (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.ELC.RNWX.ZS': {
        'source':      'World Bank',
        'description': 'Electricity from renewables excl. hydro (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.ELC.HYRO.ZS': {
        'source':      'World Bank',
        'description': 'Electricity from hydro sources (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.ELC.LOSS.ZS': {
        'source':      'World Bank',
        'description': 'Power transmission & distribution losses (%% of output)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EG.FEC.RNEW.ZS': {
        'source':      'World Bank',
        'description': 'Renewable energy consumption (%% of final use)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # --------------------  ENVIRONMENT & CLIMATE  -----------------------
    'EN.ATM.CO2E.PC': {
        'source':      'World Bank',
        'description': 'CO₂ emissions (metric tons per capita)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.GHG.CO2.MT.CE.AR5': {
        'source':      'World Bank',
        'description': 'Total CO₂ emissions (Mt CO₂-eq, AR5)',
        'agg':         'sum',
    },
    'EN.GHG.CO2.PC.CE.AR5': {
        'source':      'World Bank',
        'description': 'CO₂ emissions per capita (t CO₂-eq, AR5)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.ATM.PM25.MC.M3': {
        'source':      'World Bank',
        'description': 'PM 2.5, mean exposure (µg / m³)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'ER.PTD.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Protected areas (%% of territory)',
        'agg':         'weighted',
        'weight_by':   'AG.SRF.TOTL.K2',
    },
    'AG.LND.FRST.ZS': {
        'source':      'World Bank',
        'description': 'Forest area (%% of land)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },
    'ER.H2O.FWTL.ZS': {
        'source':      'World Bank',
        'description': 'Freshwater withdrawals (%% of resources)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'ER.H2O.FWST.ZS': {
        'source':      'World Bank',
        'description': 'Water stress (withdrawal / available, %%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ---------------------------  AGRICULTURE  --------------------------
    'AG.LND.AGRI.ZS': {
        'source':      'World Bank',
        'description': 'Agricultural land (%% of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },
    'AG.LND.CROP.ZS': {
        'source':      'World Bank',
        'description': 'Arable land (%% of land area)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
    },
    'AG.YLD.CREL.KG': {
        'source':      'World Bank',
        'description': 'Cereal yield (kg / ha)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.CROP.ZS',
    },
    'AG.PRD.FOOD.XD': {
        'source':      'World Bank',
        'description': 'Food Production Index (2014-16 = 100)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'AG.CON.FERT.ZS': {
        'source':      'World Bank',
        'description': 'Fertilizer use (kg / ha arable)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.CROP.ZS',
    },
    'AG.LND.IRIG.AG.ZS': {
        'source':      'World Bank',
        'description': 'Irrigated land (%% of agricultural land)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.AGRI.ZS',
    },
    'NV.AGR.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Agriculture, forestry & fishing VA (%% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },

    # -----------------------  URBAN DEVELOPMENT  ------------------------
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
        'description': 'Largest-city population (%% of urban)',
        'agg':         'weighted',
        'weight_by':   'SP.URB.TOTL',
    },
    'EN.URB.MCTY': {
        'source':      'World Bank',
        'description': 'Population in ≥1 M agglomerations',
        'agg':         'sum',
    },
    'EN.URB.MCTY.TL.ZS': {
        'source':      'World Bank',
        'description': 'Population in ≥1 M agglomerations (%% of total)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'EN.POP.SLUM.UR.ZS': {
        'source':      'World Bank',
        'description': 'Population in slums (%% of urban pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.URB.TOTL',
    },

    # ------------------  WATER, SANITATION & WASTE  ---------------------
    'SH.H2O.SMDW.ZS': {
        'source':      'World Bank',
        'description': 'Safely managed drinking water (%% of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.STA.SMSS.ZS': {
        'source':      'World Bank',
        'description': 'Safely managed sanitation (%% of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.H2O.BASW.ZS': {
        'source':      'World Bank',
        'description': 'Basic drinking water (%% of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.STA.BASS.ZS': {
        'source':      'World Bank',
        'description': 'Basic sanitation (%% of pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # --------------------  SCIENCE & INNOVATION  ------------------------
    'IP.PAT.RESD': {
        'source':      'World Bank',
        'description': 'Patent applications, residents',
        'agg':         'sum',
    },
    'IP.PAT.NRES': {
        'source':      'World Bank',
        'description': 'Patent applications, non-residents',
        'agg':         'sum',
    },
    'IP.JRN.ARTC.SC': {
        'source':      'World Bank',
        'description': 'Scientific & technical journal articles',
        'agg':         'sum',
    },
    'GB.XPD.RSDV.GD.ZS': {
        'source':      'World Bank',
        'description': 'R&D expenditure (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
    },
    'SP.POP.SCIE.RD.P6': {
        'source':      'World Bank',
        'description': 'Researchers in R&D (per million people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },

    # ====================================================================
    #  UN SDG INDICATORS
    # ====================================================================
    'SI_POV_DAY1': {
        'source':      'UN SDG',
        'description': 'Population below $2.15/day poverty line (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Proportion of the population living below the international poverty line of $2.15 per day, measured at 2017 PPP.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SI_POV_EMP1': {
        'source':      'UN SDG',
        'description': 'Employed population below poverty line (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Proportion of employed population living below the international poverty line.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SH_STA_STNT': {
        'source':      'UN SDG',
        'description': 'Stunting among children under 5 (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Prevalence of stunting (height for age < -2 SD from median) among children under 5 years of age.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SH_STA_WAST': {
        'source':      'UN SDG',
        'description': 'Wasting among children under 5 (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Prevalence of wasting (weight for height < -2 SD from median) among children under 5 years of age.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SH_DYN_MORT': {
        'source':      'UN SDG',
        'description': 'Under-5 mortality rate (per 1,000 live births)',
        'agg':         'mean',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Probability of dying between birth and age 5, expressed per 1,000 live births.',
        'unit':        'per 1,000 live births',
        'source_db':   'UN SDG Global Database',
    },
    'SH_STA_MMR': {
        'source':      'UN SDG',
        'description': 'Maternal mortality ratio (per 100,000 live births)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Number of maternal deaths per 100,000 live births during a given time period.',
        'unit':        'per 100,000 live births',
        'source_db':   'UN SDG Global Database',
    },
    'SE_GPI_PRIM': {
        'source':      'UN SDG',
        'description': 'Gender parity index, primary education',
        'agg':         'mean',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Ratio of female to male values of a given indicator. A GPI of 1 indicates parity.',
        'unit':        'index',
        'source_db':   'UN SDG Global Database',
    },
    'SH_H2O_SAFE': {
        'source':      'UN SDG',
        'description': 'Safely managed drinking water (% pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Population using drinking water from an improved source that is accessible on premises, available when needed, and free from contamination.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SH_SAN_SAFE': {
        'source':      'UN SDG',
        'description': 'Safely managed sanitation (% pop.)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Population using an improved sanitation facility that is not shared and where excreta are safely disposed of in situ or treated off site.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'EG_EGY_RNEW': {
        'source':      'UN SDG',
        'description': 'Renewable energy share (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Renewable energy share in total final energy consumption.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'EN_ATM_CO2': {
        'source':      'UN SDG',
        'description': 'CO2 per unit of GDP (kg/$PPP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Carbon dioxide emissions per unit of GDP (PPP).',
        'unit':        'kg CO2/$ PPP GDP',
        'source_db':   'UN SDG Global Database',
    },
    'DC_ODA_TOTL': {
        'source':      'UN SDG',
        'description': 'Net ODA received (% of GNI)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Net official development assistance (ODA) received as a proportion of gross national income.',
        'unit':        '% of GNI',
        'source_db':   'UN SDG Global Database',
    },
    'IT_NET_BBP2': {
        'source':      'UN SDG',
        'description': 'Fixed broadband per 100 inhabitants',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Fixed broadband subscriptions per 100 inhabitants.',
        'unit':        'per 100 inhabitants',
        'source_db':   'UN SDG Global Database',
    },
    'SL_TLF_UEM': {
        'source':      'UN SDG',
        'description': 'Unemployment rate (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Unemployment rate as a percentage of the total labour force.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'ER_PTD_TERR': {
        'source':      'UN SDG',
        'description': 'Protected terrestrial KBA coverage (%)',
        'agg':         'weighted',
        'weight_by':   'AG.SRF.TOTL.K2',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'Average proportion of terrestrial Key Biodiversity Areas covered by protected areas.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },

    # ====================================================================
    #  FAOSTAT INDICATORS
    # ====================================================================
    'FAO.FS.UNDR': {
        'source':      'FAOSTAT',
        'description': 'Prevalence of undernourishment (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/FS',
        'methodology': 'Prevalence of undernourishment: share of population whose habitual food consumption is insufficient to provide the dietary energy levels required to maintain a normal active and healthy life.',
        'unit':        '%',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'FS', 'item': '210011', 'element': '6121'},
    },
    'FAO.FS.SEVI': {
        'source':      'FAOSTAT',
        'description': 'Severe food insecurity (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/FS',
        'methodology': 'Prevalence of severe food insecurity in the total population based on the Food Insecurity Experience Scale (FIES).',
        'unit':        '%',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'FS', 'item': '210091', 'element': '6121'},
    },
    'FAO.FS.PCFS': {
        'source':      'FAOSTAT',
        'description': 'Per capita food supply (kcal/day)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/FS',
        'methodology': 'Average dietary energy supply adequacy measured in kilocalories per capita per day.',
        'unit':        'kcal/capita/day',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'FS', 'item': '210041', 'element': '6132'},
    },
    'FAO.FS.PCPR': {
        'source':      'FAOSTAT',
        'description': 'Per capita protein supply (g/day)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/FS',
        'methodology': 'Average protein supply in grams per capita per day.',
        'unit':        'g/capita/day',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'FS', 'item': '210042', 'element': '6132'},
    },
    'FAO.QCL.CERPROD': {
        'source':      'FAOSTAT',
        'description': 'Cereals production (tonnes)',
        'agg':         'sum',
        'source_url':  'https://www.fao.org/faostat/en/#data/QCL',
        'methodology': 'Total production quantity of cereals in metric tonnes.',
        'unit':        'tonnes',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'QCL', 'item': '1717', 'element': '5510'},
    },
    'FAO.QCL.CERYLD': {
        'source':      'FAOSTAT',
        'description': 'Cereal yield (hg/ha)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
        'source_url':  'https://www.fao.org/faostat/en/#data/QCL',
        'methodology': 'Cereal yield measured in hectograms per hectare.',
        'unit':        'hg/ha',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'QCL', 'item': '1717', 'element': '5419'},
    },
    'FAO.QI.FOOD': {
        'source':      'FAOSTAT',
        'description': 'Food production index (2014-16=100)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/QI',
        'methodology': 'Food production index covers food crops that are considered edible and nutritious. Base period 2014-2016.',
        'unit':        'index (2014-16=100)',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'QI', 'item': '2051', 'element': '432'},
    },
    'FAO.QI.AGRI': {
        'source':      'FAOSTAT',
        'description': 'Agriculture production index (2014-16=100)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/QI',
        'methodology': 'Gross agriculture production index including all crops and livestock products. Base period 2014-2016.',
        'unit':        'index (2014-16=100)',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'QI', 'item': '2050', 'element': '432'},
    },
    'FAO.QV.AGVAL': {
        'source':      'FAOSTAT',
        'description': 'Gross agricultural production value (M US$)',
        'agg':         'sum',
        'source_url':  'https://www.fao.org/faostat/en/#data/QV',
        'methodology': 'Gross production value of agriculture in constant 2014-2016 million US dollars.',
        'unit':        'million US$',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'QV', 'item': '2056', 'element': '154'},
    },
    'FAO.FS.IMPDEP': {
        'source':      'FAOSTAT',
        'description': 'Cereal import dependency ratio (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/FS',
        'methodology': 'Cereal import dependency ratio: proportion of domestic cereal supply that is imported.',
        'unit':        '%',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'FS', 'item': '210071', 'element': '6121'},
    },
    'FAO.EF.FERTUSE': {
        'source':      'FAOSTAT',
        'description': 'Nitrogen fertilizer use (tonnes)',
        'agg':         'sum',
        'source_url':  'https://www.fao.org/faostat/en/#data/EF',
        'methodology': 'Agricultural use of nitrogen fertilizers in metric tonnes of nutrients.',
        'unit':        'tonnes',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'EF', 'item': '3102', 'element': '5157'},
    },
    'FAO.RL.AGLAND': {
        'source':      'FAOSTAT',
        'description': 'Agricultural land (1000 ha)',
        'agg':         'sum',
        'source_url':  'https://www.fao.org/faostat/en/#data/RL',
        'methodology': 'Total agricultural land area in thousand hectares.',
        'unit':        '1000 ha',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'RL', 'item': '6610', 'element': '5110'},
    },
    'FAO.RL.FOREST': {
        'source':      'FAOSTAT',
        'description': 'Forest land (1000 ha)',
        'agg':         'sum',
        'source_url':  'https://www.fao.org/faostat/en/#data/RL',
        'methodology': 'Total forest area in thousand hectares.',
        'unit':        '1000 ha',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'RL', 'item': '6661', 'element': '5110'},
    },
    'FAO.FS.POLINS': {
        'source':      'FAOSTAT',
        'description': 'Political stability index',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.fao.org/faostat/en/#data/FS',
        'methodology': 'Political stability and absence of violence/terrorism index, ranging from approximately -2.5 (weak) to 2.5 (strong).',
        'unit':        'index',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'FS', 'item': '210081', 'element': '6176'},
    },
    'FAO.TCL.FOODEXP': {
        'source':      'FAOSTAT',
        'description': 'Food exports value (1000 US$)',
        'agg':         'sum',
        'source_url':  'https://www.fao.org/faostat/en/#data/TCL',
        'methodology': 'Value of food exports in thousand US dollars.',
        'unit':        '1000 US$',
        'source_db':   'FAOSTAT',
        '_fao_params': {'domain': 'TCL', 'item': '2901', 'element': '5922'},
    },

    # ====================================================================
    #  APoA MONITORING FRAMEWORK — WORLD BANK INDICATORS
    # ====================================================================

    # -- Priority 1: Structural transformation --
    'NV.SRV.TOTL.ZS': {
        'source':      'World Bank',
        'description': 'Services value added (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_db':   'World Development Indicators',
        'unit':        '% of GDP',
    },
    'IC.BUS.NDNS.ZS': {
        'source':      'World Bank',
        'description': 'New business density (new registrations per 1,000 working-age people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_db':   'World Development Indicators',
        'unit':        'per 1,000 people ages 15-64',
    },
    'NV.IND.MANF.ZS': {
        'source':      'World Bank',
        'description': 'Manufacturing value added (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_db':   'World Development Indicators',
        'unit':        '% of GDP',
    },
    'NV.IND.MANF.CD': {
        'source':      'World Bank',
        'description': 'Manufacturing value added (current US$)',
        'agg':         'sum',
        'source_db':   'World Development Indicators',
        'unit':        'current US$',
    },
    'TX.VAL.MANF.ZS.UN': {
        'source':      'World Bank',
        'description': 'Manufactures exports (% of merchandise exports)',
        'agg':         'weighted',
        'weight_by':   'NE.EXP.GNFS.CD',
        'source_db':   'World Development Indicators',
        'unit':        '%',
    },

    # -- Priority 2: Trade --
    'BG.GSR.NFSV.GD.ZS': {
        'source':      'World Bank',
        'description': 'Trade in services (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_db':   'World Development Indicators',
        'unit':        '% of GDP',
    },

    # -- Priority 3: Transport & connectivity --
    'IE.PPI.ENGY.CD': {
        'source':      'World Bank',
        'description': 'Investment commitments in energy with private participation (current US$)',
        'agg':         'sum',
        'source_db':   'World Development Indicators',
        'unit':        'current US$',
    },
    'IE.PPI.ICTI.CD': {
        'source':      'World Bank',
        'description': 'Investment commitments in ICT with private participation (current US$)',
        'agg':         'sum',
        'source_db':   'World Development Indicators',
        'unit':        'current US$',
    },

    # -- Priority 5: Means of implementation --
    'GC.REV.XGRT.GD.ZS': {
        'source':      'World Bank',
        'description': 'Revenue, excluding grants (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_db':   'World Development Indicators',
        'unit':        '% of GDP',
    },
    'DT.TDS.DECT.EX.ZS': {
        'source':      'World Bank',
        'description': 'Total debt service (% of exports of goods, services and primary income)',
        'agg':         'weighted',
        'weight_by':   'NE.EXP.GNFS.CD',
        'source_db':   'World Development Indicators',
        'unit':        '%',
    },

    # ====================================================================
    #  APoA MONITORING FRAMEWORK — UN SDG INDICATORS
    # ====================================================================

    # -- Priority 1: Structural transformation --
    'SL_EMP_PCAP': {
        'source':      'UN SDG',
        'description': 'Annual growth rate of real GDP per employed person (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 8.2.1 — Annual growth rate of real GDP per employed person, measuring labour productivity growth.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'ST_GDP_ZS': {
        'source':      'UN SDG',
        'description': 'Tourism direct GDP as proportion of total GDP (%)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 8.9.1 — Tourism direct GDP as a proportion of total GDP and in growth rate.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SE_TOT_CPLR': {
        'source':      'UN SDG',
        'description': 'Completion rate, primary/lower secondary/upper secondary (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 4.1.2 — Completion rate for primary, lower secondary and upper secondary education.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SE_ADT_ACTS': {
        'source':      'UN SDG',
        'description': 'Youth/adults with ICT skills, by type of skill (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 4.4.1 — Proportion of youth and adults with information and communications technology skills.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'NV_IND_MANF': {
        'source':      'UN SDG',
        'description': 'Manufacturing value added as proportion of GDP (%)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 9.2.1 — Manufacturing value added as a proportion of GDP and per capita.',
        'unit':        '% of GDP',
        'source_db':   'UN SDG Global Database',
    },
    'NV_IND_TECH': {
        'source':      'UN SDG',
        'description': 'Medium and high-tech industry value added (% of total manufacturing)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 9.b.1 — Proportion of medium and high-tech industry value added in total value added.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'DC_TOF_AGRL': {
        'source':      'UN SDG',
        'description': 'Total official flows to agriculture sector (million US$)',
        'agg':         'sum',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 2.a.2 — Total official flows (ODA plus other official flows) to the agriculture sector.',
        'unit':        'million US$',
        'source_db':   'UN SDG Global Database',
    },

    # -- Priority 3: Transport & connectivity --
    'IS_RDP_FRGVOL': {
        'source':      'UN SDG',
        'description': 'Freight volume, by mode of transport (tonne-km)',
        'agg':         'sum',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 9.1.2 — Passenger and freight volumes, by mode of transport.',
        'unit':        'tonne-km',
        'source_db':   'UN SDG Global Database',
    },
    'IT_MOB_2GNTWK': {
        'source':      'UN SDG',
        'description': 'Population covered by at least a 2G mobile network (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 9.c.1 — Proportion of population covered by a mobile network, by technology.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'EG_ACS_ELEC': {
        'source':      'UN SDG',
        'description': 'Population with primary reliance on clean fuels and technology (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 7.1.2 — Proportion of population with primary reliance on clean fuels and technology.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'EG_EGY_PRIM': {
        'source':      'UN SDG',
        'description': 'Energy intensity (MJ per constant 2017 PPP GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 7.3.1 — Energy intensity measured in terms of primary energy and GDP.',
        'unit':        'MJ/$ PPP GDP',
        'source_db':   'UN SDG Global Database',
    },

    # -- Priority 4: Climate & disasters --
    'VC_DSR_MORT': {
        'source':      'UN SDG',
        'description': 'Disaster-related deaths per 100,000 population',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 13.1.1 / 11.5.1 — Number of deaths and missing persons attributed to disasters, per 100,000 population.',
        'unit':        'per 100,000',
        'source_db':   'UN SDG Global Database',
    },
    'VC_DSR_GDPLS': {
        'source':      'UN SDG',
        'description': 'Direct economic loss from disasters (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 11.5.2 — Direct economic loss attributed to disasters in relation to global GDP.',
        'unit':        '% of GDP',
        'source_db':   'UN SDG Global Database',
    },
    'SG_DSR_LGRGSR': {
        'source':      'UN SDG',
        'description': 'Countries with national DRR strategies aligned with Sendai Framework',
        'agg':         'sum',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 13.1.2 — Number of countries that adopt and implement national disaster risk reduction strategies.',
        'unit':        'score',
        'source_db':   'UN SDG Global Database',
    },
    'ER_RSK_LST': {
        'source':      'UN SDG',
        'description': 'Red List Index',
        'agg':         'weighted',
        'weight_by':   'AG.SRF.TOTL.K2',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 15.5.1 — Red List Index measuring trends in species extinction risk.',
        'unit':        'index (0–1)',
        'source_db':   'UN SDG Global Database',
    },
    'DC_ODA_BDVL': {
        'source':      'UN SDG',
        'description': 'ODA for biodiversity conservation (million US$)',
        'agg':         'sum',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 15.a.1 — Official development assistance on conservation and sustainable use of biodiversity.',
        'unit':        'million US$',
        'source_db':   'UN SDG Global Database',
    },
    'AG_LND_DGRD': {
        'source':      'UN SDG',
        'description': 'Proportion of land that is degraded (%)',
        'agg':         'weighted',
        'weight_by':   'AG.LND.TOTL.K2',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 15.3.1 — Proportion of land that is degraded over total land area.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },

    # -- Priority 5: Means of implementation --
    'GF_XPD_GBPC': {
        'source':      'UN SDG',
        'description': 'Total government revenue as proportion of GDP (%)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 17.1.1 — Total government revenue as a proportion of GDP, by source.',
        'unit':        '% of GDP',
        'source_db':   'UN SDG Global Database',
    },
    'SI_RMT_COST': {
        'source':      'UN SDG',
        'description': 'Remittance costs as proportion of amount remitted (%)',
        'agg':         'mean',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 10.c.1 — Remittance costs as a proportion of the amount remitted.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'FB_BNK_ACCSS': {
        'source':      'UN SDG',
        'description': 'Adults with a bank account or mobile-money provider (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 8.10.2 — Proportion of adults (15+) with an account at a financial institution or mobile-money provider.',
        'unit':        '%',
        'source_db':   'UN SDG Global Database',
    },
    'SG_STT_CAPTY': {
        'source':      'UN SDG',
        'description': 'Statistical capacity indicator score',
        'agg':         'mean',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 17.18.1 — Statistical capacity indicators for monitoring progress.',
        'unit':        'score',
        'source_db':   'UN SDG Global Database',
    },
    'FI_FSI_FSERA': {
        'source':      'UN SDG',
        'description': 'Number of commercial bank branches per 100,000 adults',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://unstats.un.org/sdgs/dataportal/database',
        'methodology': 'SDG 8.10.1 — Number of commercial bank branches and ATMs per 100,000 adults.',
        'unit':        'per 100,000 adults',
        'source_db':   'UN SDG Global Database',
    },

    # ====================================================================
    #  IMF DATAMAPPER INDICATORS
    # ====================================================================

    # -- WEO: World Economic Outlook --
    'IMF.NGDP_RPCH': {
        'source':      'IMF',
        'description': 'Real GDP growth (annual % change)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/NGDP_RPCH',
        'methodology': 'IMF WEO — Annual percentage change of real GDP. Includes IMF staff projections.',
        'unit':        '% change',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'NGDP_RPCH',
    },
    'IMF.NGDPD': {
        'source':      'IMF',
        'description': 'GDP, current prices (billions US$)',
        'agg':         'sum',
        'source_url':  'https://www.imf.org/external/datamapper/NGDPD',
        'methodology': 'IMF WEO — Gross domestic product at current prices in billions of U.S. dollars. Includes projections.',
        'unit':        'billions US$',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'NGDPD',
    },
    'IMF.NGDPDPC': {
        'source':      'IMF',
        'description': 'GDP per capita, current prices (US$)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.imf.org/external/datamapper/NGDPDPC',
        'methodology': 'IMF WEO — GDP per capita at current prices in U.S. dollars. Includes projections.',
        'unit':        'US$ per capita',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'NGDPDPC',
    },
    'IMF.PPPPC': {
        'source':      'IMF',
        'description': 'GDP per capita, PPP (current intl $)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.imf.org/external/datamapper/PPPPC',
        'methodology': 'IMF WEO — GDP per capita based on purchasing power parity. Includes projections.',
        'unit':        'intl $ per capita',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'PPPPC',
    },
    'IMF.PCPIPCH': {
        'source':      'IMF',
        'description': 'Inflation, average consumer prices (annual % change)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.imf.org/external/datamapper/PCPIPCH',
        'methodology': 'IMF WEO — Inflation as measured by annual percentage change of average consumer prices. Includes projections.',
        'unit':        '% change',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'PCPIPCH',
    },
    'IMF.BCA_NGDPD': {
        'source':      'IMF',
        'description': 'Current account balance (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/BCA_NGDPD',
        'methodology': 'IMF WEO — Current account balance as a percentage of GDP. Includes projections.',
        'unit':        '% of GDP',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'BCA_NGDPD',
    },
    'IMF.GGXWDG_NGDP': {
        'source':      'IMF',
        'description': 'General government gross debt (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/GGXWDG_NGDP',
        'methodology': 'IMF WEO — General government gross debt as a percentage of GDP. Includes projections.',
        'unit':        '% of GDP',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'GGXWDG_NGDP',
    },
    'IMF.GGXCNL_NGDP': {
        'source':      'IMF',
        'description': 'General govt net lending/borrowing (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/GGXCNL_NGDP',
        'methodology': 'IMF WEO — General government net lending/borrowing (overall fiscal balance) as a percentage of GDP. Includes projections.',
        'unit':        '% of GDP',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'GGXCNL_NGDP',
    },
    'IMF.LUR': {
        'source':      'IMF',
        'description': 'Unemployment rate (%)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
        'source_url':  'https://www.imf.org/external/datamapper/LUR',
        'methodology': 'IMF WEO — Unemployment rate as a percentage of total labor force. Includes projections.',
        'unit':        '%',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'LUR',
    },
    'IMF.PPPSH': {
        'source':      'IMF',
        'description': 'GDP based on PPP, share of world (%)',
        'agg':         'sum',
        'source_url':  'https://www.imf.org/external/datamapper/PPPSH',
        'methodology': 'IMF WEO — GDP based on purchasing power parity as share of world total. Includes projections.',
        'unit':        '% of world',
        'source_db':   'IMF World Economic Outlook',
        '_imf_code':   'PPPSH',
    },

    # -- Fiscal Monitor --
    'IMF.GGR_G01_GDP_PT': {
        'source':      'IMF',
        'description': 'General government revenue (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/GGR_G01_GDP_PT',
        'methodology': 'IMF Fiscal Monitor — General government revenue as a percentage of GDP.',
        'unit':        '% of GDP',
        'source_db':   'IMF Fiscal Monitor',
        '_imf_code':   'GGR_G01_GDP_PT',
    },
    'IMF.G_X_G01_GDP_PT': {
        'source':      'IMF',
        'description': 'General government expenditure (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/G_X_G01_GDP_PT',
        'methodology': 'IMF Fiscal Monitor — General government total expenditure as a percentage of GDP.',
        'unit':        '% of GDP',
        'source_db':   'IMF Fiscal Monitor',
        '_imf_code':   'G_X_G01_GDP_PT',
    },
    'IMF.G_XWDG_G01_GDP_PT': {
        'source':      'IMF',
        'description': 'General government gross debt (% of GDP, Fiscal Monitor)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/G_XWDG_G01_GDP_PT',
        'methodology': 'IMF Fiscal Monitor — Gross debt position of general government as a percentage of GDP.',
        'unit':        '% of GDP',
        'source_db':   'IMF Fiscal Monitor',
        '_imf_code':   'G_XWDG_G01_GDP_PT',
    },
    'IMF.GGXCNL_G01_GDP_PT': {
        'source':      'IMF',
        'description': 'General govt overall fiscal balance (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/GGXCNL_G01_GDP_PT',
        'methodology': 'IMF Fiscal Monitor — General government net lending/borrowing (overall fiscal balance) as a percentage of GDP.',
        'unit':        '% of GDP',
        'source_db':   'IMF Fiscal Monitor',
        '_imf_code':   'GGXCNL_G01_GDP_PT',
    },
    'IMF.GGXONLB_G01_GDP_PT': {
        'source':      'IMF',
        'description': 'General govt primary fiscal balance (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/GGXONLB_G01_GDP_PT',
        'methodology': 'IMF Fiscal Monitor — General government primary net lending/borrowing as a percentage of GDP.',
        'unit':        '% of GDP',
        'source_db':   'IMF Fiscal Monitor',
        '_imf_code':   'GGXONLB_G01_GDP_PT',
    },

    # -- Global Debt Database --
    'IMF.CG_DEBT_GDP': {
        'source':      'IMF',
        'description': 'Central government debt (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.CD',
        'source_url':  'https://www.imf.org/external/datamapper/CG_DEBT_GDP',
        'methodology': 'IMF Global Debt Database — Central government debt as a percentage of GDP.',
        'unit':        '% of GDP',
        'source_db':   'IMF Global Debt Database',
        '_imf_code':   'CG_DEBT_GDP',
    },
}

# ------------------------------------------------------------------
# 2. Indicator category mapping (lists must reference existing codes)
# ------------------------------------------------------------------
categorized_indicators = {
    "General": [
        'SP.POP.TOTL', 'SP.POP.GROW', 'SP.URB.TOTL', 'SP.URB.TOTL.IN.ZS',
        'SP.RUR.TOTL', 'SP.DYN.LE00.IN', 'AG.SRF.TOTL.K2', 'AG.LND.TOTL.K2',
        'EN.POP.DNST'
    ],

    "Economy": [
        'NY.GDP.MKTP.CD', 'NY.GDP.MKTP.PP.CD', 'NY.GDP.PCAP.PP.CD',
        'NY.GDP.MKTP.KD.ZG', 'NY.GDP.PCAP.CD', 'NY.GNP.PCAP.PP.CD',
        'NY.ADJ.NNTY.PC.CD', 'FP.CPI.TOTL.ZG', 'PA.NUS.FCRF'
    ],

    "Inequality & Poverty": [
        'SI.POV.DDAY', 'SI.POV.LMIC', 'SI.POV.NAHC',
        'SI.POV.GINI', 'SI.DST.FRST.20', 'SI.DST.10TH.10'
    ],

    "Trade & Finance": [
        'NE.EXP.GNFS.CD', 'NE.IMP.GNFS.CD', 'NE.TRD.GNFS.CD', 'NE.TRD.GNFS.ZS',
        'BN.CAB.XOKA.CD', 'BN.CAB.XOKA.GD.ZS', 'FI.RES.TOTL.CD', 'FI.RES.TOTL.MO',
        'LP.LPI.OVRL.XQ', 'LP.EXP.DURS.MD', 'BM.GSR.ROYL.CD',
        'TX.VAL.TECH.CD', 'TX.VAL.TECH.MF.ZS'
    ],

    "Investment & Financial Sector": [
        'BX.KLT.DINV.WD.GD.ZS', 'BM.KLT.DINV.WD.GD.ZS', 'BX.KLT.DINV.CD.WD',
        'NE.GDI.TOTL.ZS', 'FS.AST.PRVT.GD.ZS', 'CM.MKT.LCAP.CD',
        'CM.MKT.LCAP.GD.ZS', 'FB.CBK.BRCH.P5', 'FR.INR.LEND', 'FR.INR.RINR'
    ],

    "Debt & Aid": [
        'DT.DOD.DECT.CD', 'DT.DOD.DECT.GN.ZS', 'DT.TDS.DECT.GN.ZS',
        'GC.DOD.TOTL.CN', 'GC.DOD.TOTL.GD.ZS', 'DT.ODA.ODAT.GN.ZS',
        'DT.ODA.ALLD.CD', 'DT.ODA.ODAT.PC.ZS', 'BX.TRF.PWKR.CD.DT'
    ],

    "Government & Governance": [
        'GC.TAX.TOTL.GD.ZS', 'GC.TAX.IMPT.ZS', 'GC.XPN.TOTL.GD.ZS',
        'MS.MIL.XPND.GD.ZS', 'VA.EST', 'PV.EST', 'GE.EST',
        'RQ.EST', 'RL.EST', 'CC.EST'
    ],

    "Education": [
        'SE.PRM.NENR', 'SE.SEC.NENR', 'SE.TER.ENRR', 'SE.XPD.TOTL.GD.ZS',
        'SE.ADT.LITR.ZS', 'SE.ADT.LITR.FE.ZS', 'SE.PRM.CMPT.ZS', 'SE.PRM.ENRR.FE'
    ],

    "Health": [
        'SH.DYN.MORT', 'SH.DYN.NMRT', 'SH.STA.MMRT', 'SH.XPD.CHEX.GD.ZS',
        'SH.XPD.CHEX.PC.CD', 'SH.IMM.MEAS', 'SH.MED.PHYS.ZS',
        'SH.MED.BEDS.ZS', 'SH.HIV.INCD.ZS', 'SH.STA.DIAB.ZS'
    ],

    "Labor & Employment": [
        'SL.TLF.CACT.FM.ZS', 'SL.UEM.TOTL.ZS', 'SL.UEM.1524.ZS',
        'SL.EMP.TOTL.SP.ZS', 'SL.GDP.PCAP.EM.KD', 'SL.TLF.TOTL.IN',
        'SL.AGR.EMPL.ZS', 'SL.IND.EMPL.ZS', 'SL.SRV.EMPL.ZS'
    ],

    "Gender": [
        'SG.GEN.PARL.ZS', 'SG.LAW.INDX', 'SP.DYN.SMAM.FE',
        'SP.DYN.TFRT.IN', 'SG.VAW.ARGU.ZS', 'SL.TLF.CACT.FM.ZS'
    ],

    "Infrastructure & Technology": [
        'EG.ELC.ACCS.ZS', 'IT.NET.USER.ZS', 'IT.CEL.SETS.P2', 'IT.NET.BBND.P2',
        'IS.RRS.TOTL.KM', 'IS.ROD.TOTL.KM', 'IS.ROD.PAVE.ZS',
        'IS.AIR.PSGR', 'IT.NET.SECR.P6'
    ],

    "Energy": [
        'EG.USE.PCAP.KG.OE', 'EG.ELC.COAL.ZS', 'EG.ELC.NUCL.ZS',
        'EG.ELC.RNWX.ZS', 'EG.ELC.HYRO.ZS', 'EG.ELC.LOSS.ZS',
        'EG.FEC.RNEW.ZS'
    ],

    "Environment & Climate": [
        'EN.ATM.CO2E.PC', 'EN.GHG.CO2.PC.CE.AR5', 'EN.GHG.CO2.MT.CE.AR5', 'EN.ATM.PM25.MC.M3',
        'ER.PTD.TOTL.ZS', 'AG.LND.FRST.ZS', 'ER.H2O.FWTL.ZS',
        'ER.H2O.FWST.ZS'
    ],

    "Agriculture": [
        'AG.LND.AGRI.ZS', 'AG.LND.CROP.ZS', 'AG.YLD.CREL.KG',
        'AG.PRD.FOOD.XD', 'AG.CON.FERT.ZS', 'AG.LND.IRIG.AG.ZS',
        'NV.AGR.TOTL.ZS'
    ],

    "Urban Development": [
        'SP.URB.GROW', 'EN.URB.LCTY', 'EN.URB.LCTY.UR.ZS',
        'EN.URB.MCTY', 'EN.URB.MCTY.TL.ZS', 'EN.POP.SLUM.UR.ZS'
    ],

    "Water, Sanitation & Waste": [
        'SH.H2O.SMDW.ZS', 'SH.STA.SMSS.ZS', 'SH.H2O.BASW.ZS', 'SH.STA.BASS.ZS'
    ],

    "Science & Innovation": [
        'IP.PAT.RESD', 'IP.PAT.NRES', 'IP.JRN.ARTC.SC',
        'GB.XPD.RSDV.GD.ZS', 'SP.POP.SCIE.RD.P6'
    ],

    "SDG Indicators": [
        'SI_POV_DAY1', 'SI_POV_EMP1', 'SH_STA_STNT', 'SH_STA_WAST',
        'SH_DYN_MORT', 'SH_STA_MMR', 'SE_GPI_PRIM', 'SH_H2O_SAFE',
        'SH_SAN_SAFE', 'EG_EGY_RNEW', 'EN_ATM_CO2', 'DC_ODA_TOTL',
        'IT_NET_BBP2', 'SL_TLF_UEM', 'ER_PTD_TERR'
    ],

    "Food Security & Agriculture (FAO)": [
        'FAO.FS.UNDR', 'FAO.FS.SEVI', 'FAO.FS.PCFS', 'FAO.FS.PCPR',
        'FAO.QCL.CERPROD', 'FAO.QCL.CERYLD', 'FAO.QI.FOOD', 'FAO.QI.AGRI',
        'FAO.QV.AGVAL', 'FAO.FS.IMPDEP', 'FAO.EF.FERTUSE', 'FAO.RL.AGLAND',
        'FAO.RL.FOREST', 'FAO.FS.POLINS', 'FAO.TCL.FOODEXP'
    ],

    "IMF Economic Outlook": [
        'IMF.NGDP_RPCH', 'IMF.NGDPD', 'IMF.NGDPDPC', 'IMF.PPPPC',
        'IMF.PCPIPCH', 'IMF.BCA_NGDPD', 'IMF.GGXWDG_NGDP',
        'IMF.GGXCNL_NGDP', 'IMF.LUR', 'IMF.PPPSH',
        'IMF.GGR_G01_GDP_PT', 'IMF.G_X_G01_GDP_PT',
        'IMF.G_XWDG_G01_GDP_PT', 'IMF.GGXCNL_G01_GDP_PT',
        'IMF.GGXONLB_G01_GDP_PT', 'IMF.CG_DEBT_GDP',
    ],

    # ---- APoA Monitoring Framework Priority Areas ----

    "APoA 1: Structural Transformation": [
        'NY.GDP.MKTP.KD.ZG', 'NY.GDP.PCAP.CD', 'SL.GDP.PCAP.EM.KD',
        'NV.IND.MANF.ZS', 'NV.IND.MANF.CD', 'NV.SRV.TOTL.ZS',
        'NV.AGR.TOTL.ZS', 'TX.VAL.MANF.ZS.UN', 'IC.BUS.NDNS.ZS',
        'SL_EMP_PCAP', 'NV_IND_MANF', 'NV_IND_TECH', 'ST_GDP_ZS',
        'SE_TOT_CPLR', 'SE_ADT_ACTS', 'DC_TOF_AGRL',
        'BX.KLT.DINV.WD.GD.ZS', 'EG.ELC.ACCS.ZS', 'IT.NET.USER.ZS',
        'SE.PRM.NENR', 'SE.SEC.NENR', 'SE.TER.ENRR', 'SE.ADT.LITR.ZS',
        'SL.UEM.TOTL.ZS', 'SL.UEM.1524.ZS',
        'IMF.NGDP_RPCH', 'IMF.NGDPDPC',
    ],

    "APoA 2: Trade & Regional Integration": [
        'NE.EXP.GNFS.CD', 'NE.IMP.GNFS.CD', 'NE.TRD.GNFS.ZS',
        'BG.GSR.NFSV.GD.ZS', 'TX.VAL.TECH.CD', 'TX.VAL.TECH.MF.ZS',
        'TX.VAL.MANF.ZS.UN', 'LP.LPI.OVRL.XQ',
    ],

    "APoA 3: Transport, Transit & Connectivity": [
        'IS.RRS.TOTL.KM', 'IS.ROD.TOTL.KM', 'IS.AIR.PSGR',
        'IS_RDP_FRGVOL', 'IT.CEL.SETS.P2', 'IT.NET.BBND.P2',
        'IT_MOB_2GNTWK', 'IE.PPI.ENGY.CD', 'IE.PPI.ICTI.CD',
        'EG_ACS_ELEC', 'EG_EGY_PRIM', 'EG.FEC.RNEW.ZS',
    ],

    "APoA 4: Climate, Resilience & Environment": [
        'VC_DSR_MORT', 'VC_DSR_GDPLS', 'SG_DSR_LGRGSR',
        'EN.ATM.CO2E.PC', 'EN.GHG.CO2.MT.CE.AR5', 'EG_EGY_RNEW',
        'ER_RSK_LST', 'DC_ODA_BDVL', 'AG_LND_DGRD',
        'ER.PTD.TOTL.ZS', 'AG.LND.FRST.ZS',
    ],

    "APoA 5: Means of Implementation": [
        'GC.REV.XGRT.GD.ZS', 'GC.TAX.TOTL.GD.ZS', 'GF_XPD_GBPC',
        'DT.ODA.ODAT.GN.ZS', 'DT.ODA.ALLD.CD', 'DC_ODA_TOTL',
        'BX.TRF.PWKR.CD.DT', 'SI_RMT_COST', 'FB_BNK_ACCSS',
        'FI_FSI_FSERA', 'DT.DOD.DECT.CD', 'DT.TDS.DECT.EX.ZS',
        'SG_STT_CAPTY',
        'IMF.GGR_G01_GDP_PT', 'IMF.GGXWDG_NGDP', 'IMF.CG_DEBT_GDP',
    ],
}

# ------------------------------------------------------------------
#  End of file
# ------------------------------------------------------------------

# Extract the list of all indicator codes needed for data download
all_indicator_codes = list(indicators.keys())
