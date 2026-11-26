import os

ENTRY = (
    "When the train braked, a dozen strangers' coffees leaned forward in unison — "
    "for one stop, we were islands in a single small ocean, sharing one brief tide."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
