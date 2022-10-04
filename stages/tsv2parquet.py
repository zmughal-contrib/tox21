import pandas as pd
import sys
import pyarrow as pyarrow
import fastparquet as fastparquet

InFileName = sys.argv[1]
OutFileName = sys.argv[2]

print(f"tsv2parquet: Converting file {InFileName}")
DF = pd.read_csv(InFileName, sep='\t')
DF.to_parquet(OutFileName)
