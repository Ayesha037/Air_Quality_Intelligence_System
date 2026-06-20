import pandas as pd

def get_aqi_category(aqi):
    """Convert AQI number to category label"""
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive"
    elif aqi <= 200:
        return "Unhealthy"
    elif aqi <= 300:
        return "Very Unhealthy"
    else:
        return "Hazardous"


def clean_aqi_data(df):
    """Clean and enrich raw AQI dataframe"""
    print("Cleaning data...")

    df = df.dropna(subset=["aqi"])

    df = df.drop_duplicates(subset=["city_query"])

    df["aqi"] = pd.to_numeric(df["aqi"], errors="coerce")

    df = df.dropna(subset=["aqi"])

    df["timestamp"] = pd.to_datetime(df["timestamp"])

    df["category"] = df["aqi"].apply(get_aqi_category)

    df = df.sort_values("aqi", ascending=False).reset_index(drop=True)

    df["rank"] = df.index + 1

    print(f"Clean data ready: {len(df)} cities")
    return df