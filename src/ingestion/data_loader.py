import polars as pl


def load_data(csv_path: str):
    """
    Load aqicn.org air quality data

    :param csv_path:
        Path to airquaility-wekerom.csv
    :return:
        Polar dataframe with columns:
            - date (yyyy-mm-dd)
            - pm25_daily_mean

    """
    df = pl.read_csv(csv_path)

    df = df.rename({col: col.strip() for col in df.columns})

    df = df.with_columns(
        pl.col("pm25")
        .str.strip_chars()
    )

    df = df.filter(
        (pl.col("pm25").is_not_null()) &
        (pl.col("pm25").str.strip_chars() != "")
    )

    df = df.select([
        pl.col("date"),
        pl.col("pm25")
        .str.strip_chars()
        .cast(pl.Int32)
        .alias("pm25_daily_mean")
    ])

    print(df.head())
    return df
