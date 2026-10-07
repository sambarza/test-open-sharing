import delta_sharing
from IPython.display import display

# Point to the profile file. It can be a file on the local file system or a file on a remote storage.
profile_file = "config.share"

# Create a SharingClient.
client = delta_sharing.SharingClient(profile_file)

# List all shared tables.
tables = client.list_all_tables()

print(tables)

# Create a url to access a shared table.
# A table path is the profile file path following with `#` and the fully qualified name of a table 
# (`<share-name>.<schema-name>.<table-name>`).
table_url = profile_file + "#test_share.default.sample_trips_sep_13_1948"

# Fetch 10 rows from a table and convert it to a Pandas DataFrame. This can be used to read sample data 
# from a table that cannot fit in the memory.
df_sample_trips_sep_13_1948 = delta_sharing.load_as_pandas(table_url, limit=10)

display(df_sample_trips_sep_13_1948)
# # Load a table as a Pandas DataFrame. This can be used to process tables that can fit in the memory.
# delta_sharing.load_as_pandas(table_url)

# # Load a table as a Pandas DataFrame explicitly using Delta Format
# delta_sharing.load_as_pandas(table_url, use_delta_format=True)

# # Load a table as a Pandas DataFrame, using batch conversion to potentially reduce memory usage.
# delta_sharing.load_as_pandas(table_url, convert_in_batches=True)

# # Load a table as a Pandas DataFrame explicitly using jsonPredicateHints
# hintOnHireDate = '''{
#   "op": "equal",
#   "children": [
#     {"op": "column", "name":"hireDate", "valueType":"date"},
#     {"op":"literal","value":"2021-04-29","valueType":"date"}
#   ]
# }'''
# delta_sharing.load_as_pandas(table_url, jsonPredicateHints = hintOnHireDate)

# # If the code is running with PySpark, you can use `load_as_spark` to load the table as a Spark DataFrame.
# delta_sharing.load_as_spark(table_url)