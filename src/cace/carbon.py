import pandas as pd

from cace.emissions_factors import EMISSIONS_FACTORS_G_PER_KWH


def compute_carbon_intensity(generation_mix: dict) -> float:
    """
    generation_mix: dict mapping fuel name -> MW output at one timestamp,
      e.g. {"Solar": 18500, "Wind Onshore": 12000, ...}

    Returns: carbon intensity in gCO2/kWh for that single timestamp.
    """
    total_emission = 0.0
    total_generation = 0.0

    total_generation = sum(generation_mix.values()) # sum all generation values
    if total_generation == 0:
        return 0.0

    for fuel, mwh in generation_mix.items():
        emissions_factor = EMISSIONS_FACTORS_G_PER_KWH.get(fuel, 0.0)
        total_emission+= mwh * emissions_factor

    carbon_intensity = total_emission / total_generation

    return carbon_intensity


def _row_to_generation_mix(row: "pd.Series") -> dict:
    mix={}
    suffix="- Actual Aggregated"
    for col,value in row.items():
        if col.endswith(suffix):
            clean_name = col.replace(suffix, "").strip()
            mix[clean_name] = value
    return mix 


def compute_carbon_intensity_series(df: "pd.DataFrame") -> "pd.Series":
    """
    df: the generation-mix DataFrame, one row per timestamp, one column
        per fuel type (as loaded from generation_mix_de_lu_7d.csv).

    Returns: a pd.Series indexed by the same timestamps, one carbon
        intensity value (gCO2/kWh) per row.
    """
    
    intensities = {}
    for timestamp, row in df.iterrows():
        generation_mix = _row_to_generation_mix(row)
        intensities[timestamp] = compute_carbon_intensity(generation_mix)

    return pd.Series(intensities, dtype=float)


if __name__ == "__main__":
    # Same numbers as the worked example from our conversation — if your
    # function is right, this should print close to 289 gCO2/kWh.
    sample_mix = {
        "Solar": 18500,
        "Wind Onshore": 12000,
        "Fossil Brown coal/Lignite": 8000,
        "Fossil Hard coal": 3000,
        "Fossil Gas": 5000,
        "Hydro Run-of-river and poundage": 2000,
        "Biomass": 4000,
    }
    result = compute_carbon_intensity(sample_mix)
    print(f"Carbon intensity: {result:.1f} gCO2/kWh")
