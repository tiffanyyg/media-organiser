from pathlib import Path


def generate_cleanup_report(
    results,
):

    lines = []

    lines.append(
        "CLEANUP REPORT"
    )

    lines.append(
        "=============="
    )

    lines.append(
        ""
    )

    lines.append(
        f"Files scanned: {results['scanned']}"
    )

    lines.append(
        ""
    )

    lines.append(
        f"Screenshots: {len(results['screenshots'])}"
    )

    for file in results["screenshots"]:

        lines.append(
            f"- {file}"
        )


    lines.append(
        ""
    )

    lines.append(
        f"Large files: {len(results['large_files'])}"
    )


    for file in results["large_files"]:

        size_mb = (
            file.stat().st_size
            /
            (1024 * 1024)
        )


        lines.append(
            f"- {file} ({size_mb:.2f} MB)"
        )


    return "\n".join(
        lines
    )

