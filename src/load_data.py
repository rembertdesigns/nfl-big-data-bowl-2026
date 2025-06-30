import pandas as pd
import os

RAW_DATA_PATH = "data/raw"

def load_tracking_data(weeks=range(1, 10)):
    """Load and concatenate pre-snap tracking data for all weeks."""
    tracking_frames = []
    for week in weeks:
        path = os.path.join(RAW_DATA_PATH, f"tracking_week_{week}.csv")
        df = pd.read_csv(path)
        df = df[df["frameType"] == "before_snap"]
        tracking_frames.append(df)
    tracking_all = pd.concat(tracking_frames, ignore_index=True)
    return tracking_all

def load_metadata():
    """Load all static NFL metadata files."""
    plays = pd.read_csv(os.path.join(RAW_DATA_PATH, "plays.csv"))
    player_play = pd.read_csv(os.path.join(RAW_DATA_PATH, "player_play.csv"))
    players = pd.read_csv(os.path.join(RAW_DATA_PATH, "players.csv"))
    return plays, player_play, players

def merge_tracking_with_metadata(tracking_df, plays_df):
    """Join pre-snap tracking data with play metadata."""
    merged = tracking_df.merge(plays_df, on=["gameId", "playId"], how="left")
    return merged