"""Utility functions for working with FQL queries."""
from os.path import join, dirname

def retrieve_query(file_name: str) -> str:
    """Retrieve the FQL query from the file name."""
    # Get the directory of the current script
    script_dir = dirname(__file__)

    # Construct the full path to the FQL file
    fql_file_path = join(script_dir, f"{file_name}.fql")

    # Read the FQL query from the file
    with open(fql_file_path, "r", encoding="utf-8") as file:
        query_string = file.read().strip()
        return query_string
