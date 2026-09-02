import pandas as pd
from entsoe import EntsoePandasClient, EntsoeRawClient

from cace import config


def fetch_generation_mix(start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
    client = EntsoePandasClient(api_key=config.ENTSOE_API_TOKEN)
    return client.query_generation(
        config.GERMANY_LUXEMBOURG, start=start, end=end, psr_type=None
    )


def fetch_raw_sample_xml(start: pd.Timestamp, end: pd.Timestamp) -> str:
    client = EntsoeRawClient(api_key=config.ENTSOE_API_TOKEN)
    return client.query_generation(
        config.GERMANY_LUXEMBOURG, start=start, end=end, psr_type=None
    )


def main():
    end = pd.Timestamp.now(tz="Europe/Brussels")
    start = end - pd.Timedelta(days=7)

    config.DATA_RAW_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Fetching Germany-Luxembourg generation mix: {start} -> {end}")
    df = fetch_generation_mix(start, end)

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = [
            " - ".join(str(level) for level in col if level) for col in df.columns
        ]

    csv_path = config.DATA_RAW_DIR / "generation_mix_de_lu_7d.csv"
    df.to_csv(csv_path)
    print(f"Saved {df.shape[0]} rows x {df.shape[1]} columns to {csv_path}")
    print("\nColumns:")
    for col in df.columns:
        print(f"  - {col}")
    print("\nFirst few rows:")
    print(df.head())

    print("\nFetching one raw XML sample (1 hour, from 7 days ago) for inspection...")
    raw_xml = fetch_raw_sample_xml(start, start + pd.Timedelta(hours=1))
    xml_path = config.DATA_RAW_DIR / "generation_mix_sample.xml"
    xml_path.write_text(raw_xml)
    print(f"Saved raw XML sample to {xml_path}")


if __name__ == "__main__":
    main()
