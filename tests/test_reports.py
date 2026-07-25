from app.importer.report import ImportReport


def test_report_counts():

    report = ImportReport()


    report.scanned = 5


    report.imported.append(
        "photo.jpg"
    )


    report.duplicates.append(
        "duplicate.jpg"
    )


    report.errors.append(
        "broken.jpg"
    )


    assert report.scanned == 5

    assert report.imported_count == 1

    assert report.duplicate_count == 1

    assert report.error_count == 1

