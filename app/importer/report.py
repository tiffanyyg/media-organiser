from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class ImportReport:

    scanned: int = 0

    imported: list[Path] = field(
        default_factory=list
    )

    duplicates: list[Path] = field(
        default_factory=list
    )

    errors: list[str] = field(
        default_factory=list
    )


    @property
    def imported_count(self):
        return len(self.imported)


    @property
    def duplicate_count(self):
        return len(self.duplicates)


    @property
    def error_count(self):
        return len(self.errors)


    def summary(self):

        return (
            "\n"
            "MEDIA IMPORT REPORT\n"
            "===================\n\n"
            f"Scanned:              {self.scanned}\n"
            f"Imported:             {self.imported_count}\n"
            f"Duplicates skipped:   {self.duplicate_count}\n"
            f"Failed:               {self.error_count}\n"
        )

