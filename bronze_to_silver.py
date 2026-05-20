import pandas as pd
import re

df = pd.read_csv(
    "output_stream.csv"
)


df = df.dropna()


df["id"] = pd.to_numeric(
    df["id"],
    errors="coerce"
)


df = df.dropna(
    subset=["id"]
)


email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"


df = df[
    df["correo"].str.match(
        email_regex,
        na=False
    )
]


df["id"] = df["id"].astype(int)


df.to_parquet(
    "output_stream.parquet",
    index=False
)


print(
    "Silver Layer generada en Parquet"
)