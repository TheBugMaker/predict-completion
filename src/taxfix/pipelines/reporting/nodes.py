import pandas as pd

# This function uses plotly.express
def generate_diagram_data(inference_results: pd.DataFrame) -> pd.DataFrame:
    """Generate a scatter plot."""
    inference_results["error"] = inference_results["completed_filing"] != inference_results["pred"]
    return inference_results.groupby("age").agg({"error": "mean"}).reset_index()
