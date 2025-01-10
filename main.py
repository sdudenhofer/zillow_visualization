import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import altair as alt

    data = pd.read_csv('Data/Metro_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv')

    df = pd.DataFrame(data)
    house_dates = [col for col in df if col.startswith('20')]

    interested_cities = df[df['RegionName'].isin(["Eugene, OR"])]#, "Evansville, IN", "Nashville, TN", "Omaha, NE"])]
    region = interested_cities['RegionName'].to_numpy()

    alt.Chart(interested_cities).mark_bar().encode(
        alt.X("RegionName"),
        alt.Y(alt.repeat("layer")),
        color=alt.datum(alt.repeat("layer")),
    ).repeat(
        layer=['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30', '2023-05-31', '2023-06-30', '2023-07-31', '2023-08-31', '2023-09-30', '2023-10-31', '2023-11-30', '2023-12-31', '2024-01-31', '2024-02-29', '2024-03-31', '2024-04-30', '2024-05-31', '2024-06-30', '2024-07-31', '2024-08-31', '2024-09-30', '2024-10-31', '2024-11-30']
    )
    return alt, data, df, house_dates, interested_cities, pd, region


if __name__ == "__main__":
    app.run()
