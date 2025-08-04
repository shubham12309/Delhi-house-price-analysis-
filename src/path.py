import os
import plotly.express as px


WORKING_DIR = os.path.dirname(os.path.dirname(os.path.abspath('..')))

DATA_DIR = os.path.join(WORKING_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")


def get_raw_training_data_path():
    return os.path.join(RAW_DATA_DIR, "Indian_housing_Delhi_data.csv")


def get_box_plot(input_df, plot_parameter="price", **filter_kwargs):
    for key, value in filter_kwargs.items():
        if key in input_df.columns:
            input_df = input_df[input_df[key] == value]
    fig = px.box(input_df, y=plot_parameter)
    return fig