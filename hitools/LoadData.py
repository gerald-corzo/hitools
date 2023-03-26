import importlib.resources
import pandas as pd
import io


def readObidios():
    # This assumes the data file is in the 'data' subdirectory of your package
    with importlib.resources.open_text('hitools.data', 'discharge_Obidos.csv') as f:
        content = f.read()
          # Assuming the content is in CSV format, read it into a pandas DataFrame
        dataframe = pd.read_csv(io.StringIO(content))
    return dataframe

def readItacoatiara():
    # This assumes the data file is in the 'data' subdirectory of your package
    with importlib.resources.open_text('hitools.data', 'discharge_Obidos.csv') as f:
        content = f.read()
          # Assuming the content is in CSV format, read it into a pandas DataFrame
        dataframe = pd.read_csv(io.StringIO(content))
    return dataframe

def readYuna():
    # This assumes the data file is in the 'data' subdirectory of your package
    with importlib.resources.open_text('hitools.data', 'discharge_Obidos.csv') as f:
        content = f.read()
          # Assuming the content is in CSV format, read it into a pandas DataFrame
        dataframe = pd.read_csv(io.StringIO(content))
    return dataframe

if __name__ == "__main__":
    data_content = readObidios()
    print(data_content)
