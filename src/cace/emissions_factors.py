# Lifecycle carbon intensity per generation type, in grams CO2 per kWh.
# Approximate published values (sources like electricityMaps / IPCC).
# Keys match the human-readable production-type names entsoe-py returns.
EMISSIONS_FACTORS_G_PER_KWH = {
    "Fossil Brown coal/Lignite": 1050,
    "Fossil Hard coal": 820,
    "Fossil Gas": 490,
    "Fossil Oil": 650,
    "Fossil Coal-derived gas": 700,
    "Biomass": 230,
    "Waste": 500,
    "Hydro Run-of-river and poundage": 24,
    "Hydro Water Reservoir": 24,
    "Hydro Pumped Storage": 24,
    "Nuclear": 12,
    "Solar": 41,
    "Wind Onshore": 11,
    "Wind Offshore": 12,
    "Other renewable": 100,
    "Other": 700,
    "Geothermal": 38,
}
