from pathlib import Path



def generate_duplicate_report(
    groups,
):

    lines = []

    lines.append(
        "DUPLICATE REPORT"
    )

    lines.append(
        "================"
    )

    lines.append(
        ""
    )


    lines.append(
        f"Duplicate groups: {len(groups)}"
    )


    for index, group in enumerate(
        groups,
        start=1,
    ):

        lines.append(
            ""
        )

        lines.append(
            f"Group {index}:"
        )


        for file in group:

            lines.append(
                f"- {file}"
            )


    return "\n".join(
        lines
    )

