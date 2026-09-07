import argparse


def main():
    parser = argparse.ArgumentParser(description="Aggregate game development internship listings.")
    parser.add_argument("--verbose", action="store_true", help="Show more detailed output.")
    args = parser.parse_args()

    if args.verbose:
        print("Verbose mode is ON")
    print("game-job-aggregator — starting up")


if __name__ == "__main__":
    main()