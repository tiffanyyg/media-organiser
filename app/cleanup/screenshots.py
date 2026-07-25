from pathlib import Path


SCREENSHOT_WORDS = [
    "screenshot",
    "screen shot",
    "screen_shot",
]


def is_screenshot(
    path: Path,
) -> bool:

    name = (
        path.name
        .lower()
    )

    for word in SCREENSHOT_WORDS:

        if word in name:
            return True

    return False

