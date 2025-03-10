import pyarrow as pa

# Replace with the path to your Arrow file
file_path = "/Users/maha/Documents/GitHub/pixmo-docs/output/generate-movie-reviews/_dataset/data-00000-of-00001.arrow"
table = pa.ipc.open_file(file_path).read_all()

# If you want to convert it to a Pandas DataFrame
df = table.to_pandas()

print(df)

