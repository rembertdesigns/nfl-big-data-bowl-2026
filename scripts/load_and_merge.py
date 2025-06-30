# scripts/load_and_merge.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.load_data import load_tracking_data, load_metadata, merge_tracking_with_metadata

def main():
    print("Loading tracking data...")
    tracking = load_tracking_data()

    print("Loading metadata...")
    plays, player_play, players = load_metadata()

    print("Merging data...")
    merged_presnap = merge_tracking_with_metadata(tracking, plays)

    print("Preview of merged pre-snap data:")
    print(merged_presnap.head())

if __name__ == "__main__":
    main()
