def format_results(
    results,
):
    """
    Format search results for CLI output.
    """

    if not results:

        return (
            "SEARCH RESULTS\n"
            "===============\n\n"
            "No files found."
        )


    output = [
        "SEARCH RESULTS",
        "==============",
        "",
        f"Found: {len(results)} files",
        "",
    ]


    for index, media in enumerate(
        results,
        start=1,
    ):

        output.extend(
            [
                f"{index}.",
                f"Filename: {media.filename}",
                f"Path: {media.path}",
                f"Type: {media.media_type}",
                f"Imported: {media.imported_at}",
                "",
            ]
        )


    return "\n".join(output)

