import pandas as pd
import numpy as np


class SpreadsheetComparator:

    def __init__(
        self,
        old_df,
        new_df,
        key_column,
        ignore_case=True,
        ignore_spaces=True
    ):

        self.old_df = old_df.copy()
        self.new_df = new_df.copy()

        self.key_column = key_column

        self.ignore_case = ignore_case
        self.ignore_spaces = ignore_spaces

    def normalize_value(self, value):

        if pd.isna(value):
            return ""

        if isinstance(value, str):

            if self.ignore_spaces:
                value = value.strip()

            if self.ignore_case:
                value = value.lower()

        return value

    def prepare_dataframes(self):

        self.old_df.columns = [
            str(col).strip()
            for col in self.old_df.columns
        ]

        self.new_df.columns = [
            str(col).strip()
            for col in self.new_df.columns
        ]

        self.old_df.set_index(
            self.key_column,
            inplace=True
        )

        self.new_df.set_index(
            self.key_column,
            inplace=True
        )

    def compare(self):

        self.prepare_dataframes()

        old_index = set(self.old_df.index)
        new_index = set(self.new_df.index)

        added_ids = new_index - old_index
        removed_ids = old_index - new_index
        common_ids = old_index & new_index

        added = self.new_df.loc[list(added_ids)].reset_index()

        removed = self.old_df.loc[list(removed_ids)].reset_index()

        changed_rows = []

        total_changes = 0

        for row_id in common_ids:

            old_row = self.old_df.loc[row_id]
            new_row = self.new_df.loc[row_id]

            row_changes = []

            all_columns = set(
                self.old_df.columns
            ) | set(
                self.new_df.columns
            )

            for col in all_columns:

                old_value = (
                    old_row[col]
                    if col in old_row
                    else None
                )

                new_value = (
                    new_row[col]
                    if col in new_row
                    else None
                )

                normalized_old = self.normalize_value(
                    old_value
                )

                normalized_new = self.normalize_value(
                    new_value
                )

                if normalized_old != normalized_new:

                    difference_type = "Texto"

                    if (
                        isinstance(old_value, (int, float))
                        and
                        isinstance(new_value, (int, float))
                    ):

                        difference_type = "Numérico"

                    row_changes.append({
                        "coluna": col,
                        "valor_antigo": old_value,
                        "valor_novo": new_value,
                        "tipo": difference_type
                    })

                    total_changes += 1

            if row_changes:

                changed_rows.append({
                    "id": row_id,
                    "alteracoes": row_changes
                })

        summary = {
            "total_antigo": len(self.old_df),
            "total_novo": len(self.new_df),
            "novos_registros": len(added),
            "removidos": len(removed),
            "linhas_alteradas": len(changed_rows),
            "total_alteracoes": total_changes
        }

        return {
            "summary": summary,
            "added": added,
            "removed": removed,
            "changed": changed_rows
        }
