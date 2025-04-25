indicators = {
    'SP.POP.TOTL': {
        'source':      'World Bank',
        'description': 'Population, total',
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
    'NY.GDP.MKTP.CD': {
        'source':       'World Bank',
        'description':  'GDP (current US$)',
        'agg':          'sum'
    },
    'AG.SRF.TOTL.K2': {
        'source':      'World Bank',
        'description': 'Surface area (sq. km)',
        'agg':         'sum',
    },
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
    'DT.ODA.ODAT.GN.ZS': {
        'source':      'World Bank',
        'description': 'ODA received (% of GNI)',
        'agg':         'weighted',
        'weight_by':   'DT.ODA.ODAT.GN.ZS',
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
    'GC.TAX.IMPT.ZS': {
        'source':      'World Bank',
        'description': 'Tax revenue (% of GDP)',
        'agg':         'weighted',
        'weight_by':   'NY.GDP.MKTP.PP.CD',
    },
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
    'SE.PRM.NENR': {
        'source':      'World Bank',
        'description': 'School enrollment, primary (% net)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IT.NET.BBND.P2': {
        'source':      'World Bank',
        'description': 'Fixed broadband subscriptions (per 100 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'IT.CEL.SETS.P2': {
        'source':      'World Bank',
        'description': 'Mobile cellular subscriptions (per 100 people)',
        'agg':         'weighted',
        'weight_by':   'SP.POP.TOTL',
    },
    'SH.DYN.MORT': {
        'source':      'World Bank',
        'description': 'Mortality rate, under-5 (per 1,000 live births)',
        'agg':         'mean',
    },
    'FP.CPI.TOTL.ZG': {
        'source':      'World Bank',
        'description': 'Inflation, consumer prices (annual %)',
        'agg':         'mean',
    },
    'BN.CAB.XOKA.CD': {
        'source':      'World Bank',
        'description': 'Current account balance (BoP, current US$)',
        'agg':         'sum',
    },
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
    'DT.DOD.DECT.CD': {
        'source':      'World Bank',
        'description': 'External debt stocks, total (current US$)',
        'agg':         'sum',
    },
    'FI.RES.TOTL.CD': {
        'source':      'World Bank',
        'description': 'Total reserves (includes gold, current US$)',
        'agg':         'sum',
    },
    'GC.DOD.TOTL.CN': {
        'source':      'World Bank',
        'description': 'Central government debt, total (current LCU)',
        'agg':         'sum',
    },
    'SI.POV.DDAY': {
        'source': 'World Bank',
        'description': 'Poverty headcount ratio at $2.15 a day (2017 PPP) (% of population)',
        'agg': 'weighted',
        'weight_by': 'SP.POP.TOTL'
    },
    'IT.NET.USER.ZS': {
        'source':      'World Bank',
        'description': 'Individuals using the Internet (% of population)',
        'agg': 'weighted',
        'weight_by': 'SP.POP.TOTL'
    },
    'SE.XPD.TOTL.GD.ZS': {
        'source': 'World Bank',
        'description': 'Government expenditure on education, total (% of GDP)',
        'agg': 'weighted',
        'weight_by': 'NY.GDP.MKTP.CD'
    },
    'EG.ELC.ACCS.ZS': {
        'source': 'World Bank',
        'description': 'Access to electricity (% of population)',
        'agg': 'weighted',
        'weight_by': 'SP.POP.TOTL'
    }
}

# Organize codes by topic for display
categorized_indicators = {
    "General": ['SP.POP.TOTL', 'AG.SRF.TOTL.K2'],
    "Economy": ['NY.GDP.MKTP.CD', 'NY.GDP.MKTP.PP.CD', 'NY.GDP.PCAP.PP.CD', 'FP.CPI.TOTL.ZG'],
    "Trade & Finance": ['NE.EXP.GNFS.CD', 'NE.IMP.GNFS.CD', 'NE.TRD.GNFS.CD', 'BN.CAB.XOKA.CD', 'FI.RES.TOTL.CD', 'LP.LPI.OVRL.XQ', 'LP.EXP.DURS.MD'],
    "Investment": ['BX.KLT.DINV.WD.GD.ZS', 'BM.KLT.DINV.WD.GD.ZS'],
    "Debt & Aid": ['DT.DOD.DECT.CD', 'GC.DOD.TOTL.CN', 'DT.ODA.ODAT.GN.ZS'],
    "Government": ['GC.TAX.IMPT.ZS', 'SE.XPD.TOTL.GD.ZS'],
    "Social": ['SL.TLF.CACT.FM.ZS', 'SL.UEM.TOTL.ZS', 'SI.POV.DDAY', 'SH.DYN.MORT', 'SE.PRM.NENR'],
    "Infrastructure & Technology": ['EG.ELC.ACCS.ZS', 'IT.NET.USER.ZS', 'IT.CEL.SETS.P2', 'IT.NET.BBND.P2'],
    "Environment": ['EN.GHG.CO2.MT.CE.AR5', 'EN.GHG.CO2.PC.CE.AR5']
}

# Extract the list of all indicator codes needed for data download
all_indicator_codes = list(indicators.keys())
