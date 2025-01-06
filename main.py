import marimo

__generated_with = "0.10.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import polars as pl


    return (pl,)


if __name__ == "__main__":
    app.run()
