import pandas as pd
import kagglehub
from kagglehub import KaggleDatasetAdapter


class LoadData:
    @staticmethod
    def load_csv(path):
        try:
            df = pd.read_csv(path)
            return df
        except Exception as e:
            raise RuntimeError("file not opening") from e


    @staticmethod
    def load_phishing_data_by_api():
        file_path = "phishing.csv"
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "eswarchandt/phishing-website-detector",
            file_path,
        )
        # print("First 5 records:", df.head())
        return df

