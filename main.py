import os
import sys
def get_data_path():
    data_path = os.environ.get("DATA_PATH")
    if not data_path:
        sys.exit("ERROR: Variable of path is not setted.")
    return data_path

def main():
    path = get_data_path() # os.environ.get("DATA_PATH")
    data = extract(path)
    transform(data)
    load(data)

if __name__ == "__main__":
    main()