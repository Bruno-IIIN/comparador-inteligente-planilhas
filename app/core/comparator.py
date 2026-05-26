import pandas as pd


class SpreadsheetComparator:

    def __init__(self, old_df, new_df, key_column):
        self.old_df = old_df
        self.new_df = new_df
        self.key_column = key_column

    def compare(self):
        old = self.old_df.copy()
        new = self.new_df.copy()

        old.set_index(self.key_column, inplace=True)
        new.set_index(self.key_column, inplace=True)

        added = new.loc[new.index.difference(old.index)]
        removed = old.loc[old.index.difference(new.index)]

        common = old.index.intersection(new.index)

        changes = []

        for idx in common:
            old_row = old.loc[idx]
            new_row = new.loc[idx]

            differences = {}

            for col in old.columns:
                if str(old_row[col]) != str(new_row[col]):
                    differences[col] = {
                        'old': old_row[col],
                        'new': new_row[col]
                    }

            if differences:
                changes.append({
                    'id': idx,
                    'changes': differences
                })

        return {
            'added': added,
            'removed': removed,
            'changed': changes
        }
