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
        'weight_by':   'NY.GDP.MKTP.PP.CD',
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
    }
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
        'EN.GHG.CO2.PC.CE.AR5', 'EN.GHG.CO2.MT.CE.AR5', 'EN.ATM.PM25.MC.M3',
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
    ]
}

# ------------------------------------------------------------------
#  End of file
# ------------------------------------------------------------------

# Extract the list of all indicator codes needed for data download
all_indicator_codes = list(indicators.keys())
