import pandas as pd

def reconcile(df_1c, df_ext, keys, tolerance=0):
    merged = df_1c.merge(df_ext, on=keys, how='outer',
                         suffixes=('_1c', '_ext'), indicator=True)
    only_1c = merged[merged['_merge'] == 'left_only']
    only_ext = merged[merged['_merge'] == 'right_only']
    diff = merged[(merged['_merge'] == 'both') &
                  ((merged['amount_1c'] - merged['amount_ext']).abs() > tolerance)]
    return {'only_1c': only_1c, 'only_ext': only_ext, 'diff': diff}
