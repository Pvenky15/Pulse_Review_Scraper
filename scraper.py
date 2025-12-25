import csv
import json
import argparse
from datetime import datetime

def parse_date(d):
    return datetime.strptime(d, "%Y-%m-%d")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--company", required=True)
    parser.add_argument("--start", required=True)
    parser.add_argument("--end", required=True)
    parser.add_argument("--source", required=True)
    args = parser.parse_args()

    start = parse_date(args.start)
    end = parse_date(args.end)

    results = []

    with open("source.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_date = parse_date(row["date"])

            if (
                row["company"] == args.company
                and row["source"] == args.source
                and start <= row_date <= end
            ):
                results.append({
                    "title": row["title"],
                    "review": row["review"],
                    "date": row["date"],
                    "rating": row["rating"],
                    "reviewer": row["reviewer"],
                    "source": row["source"]
                })

    with open("reviews.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    print(f"Saved {len(results)} reviews to reviews.json")

if __name__ == "__main__":
    main()
