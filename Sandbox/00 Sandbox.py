from pandas_profiling import ProfileReport
import pandas as pd

r_cols = ['bi_rads', 'age', 'shape', 'margin', 'density', 'severity']
df = pd.read_csv('./MLCourse/mammographic_masses.data.txt',names=r_cols, na_values='?')

prof = ProfileReport(df)
prof.to_file(output_file='out.html')