import rdflib
import json

def nt_to_json(nt_file_path, json_file_path):
    """
    Converts an N-Triples file to a JSON file.

    Args:
        nt_file_path (str): The path to the input .nt file.
        json_file_path (str): The path to the output .json file.
    """
    graph = rdflib.Graph()
    try:
        graph.parse(nt_file_path, format="nt")
    except Exception as e:
        print(f"Error parsing NT file: {e}")
        return

    data = []
    for s, p, o in graph:
        triple = {
            "subject": str(s),
            "predicate": str(p),
            "object": str(o)
        }
        data.append(triple)

    try:
        with open(json_file_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Successfully converted {nt_file_path} to {json_file_path}")
    except Exception as e:
        print(f"Error writing JSON file: {e}")


# Example usage:
nt_file = "Wikidata/wdump-4983.nt"
json_file = "/workspaces/ToG-2-v1/Wikidata/wdump-4983.json"
nt_to_json(nt_file, json_file)