import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl

    df = pl.read_csv('Data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')

    df2000 = df[['RegionName', '2000-01-31', '2000-02-29', '2000-03-31', '2000-04-30', '2000-05-31', '2000-06-30', '2000-07-31', '2000-08-31', '2000-09-30', '2000-10-31', '2000-11-30', '2000-12-31']]

    print(df2000)
    return df, df2000, pl


if __name__ == "__main__":
    app.run()
