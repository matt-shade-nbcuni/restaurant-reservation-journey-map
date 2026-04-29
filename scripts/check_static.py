from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

required_files = [
    ROOT / "index.html",
    ROOT / "styles.css",
    ROOT / "README.md",
    ROOT / "package.json",
]

required_content = [
    "Landing on restaurant page",
    "Selecting a reservation time",
    "Choosing party size",
    "Confirming reservation",
    "Success state",
    "Time slot becomes unavailable",
    "Party size not supported",
    "Authentication required",
    "Payment hold failure",
    "Network timeout",
    "Fully booked to waitlist",
]


def main() -> None:
    missing = [str(path.relative_to(ROOT)) for path in required_files if not path.exists()]
    if missing:
        raise SystemExit(f"Missing required files: {', '.join(missing)}")

    html = (ROOT / "index.html").read_text(encoding="utf-8")
    absent = [item for item in required_content if item not in html]
    if absent:
        raise SystemExit(f"Missing required journey content: {', '.join(absent)}")

    print("Static project check passed.")


if __name__ == "__main__":
    main()
