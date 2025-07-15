from model.tester import  Tester
from model.classifier import Classifier
from load_data import LoadData
from clean_data import CleanData
class ModelManager:
    def __init__(self, file_path, index_name = "Index", target_name='class'):
        df = LoadData.load_csv(file_path)
        self.df = CleanData.clean(df,index_name)

        self.target_name = target_name

        self.split_train_test()
        self.training_dict = self.create_training_dict()
        self.target_counts = self.train_df[target_name].value_counts()

        self.classifier = Classifier(
            training_dict=self.training_dict,
            target_counts=self.target_counts,
            df=self.df,
            target_name=self.target_name
        )


    def split_train_test(self, train_percent=0.7):
        df_shuffled = self.df.sample(frac=1, random_state=67).reset_index(drop=True)
        split_idx = int(len(df_shuffled) * train_percent)
        self.train_df = df_shuffled.iloc[:split_idx]
        self.test_df = df_shuffled.iloc[split_idx:]

    def create_training_dict(self):
        if self.target_name not in self.train_df:
            raise Exception(f"Target column '{self.target_name}' not found in the data")

        result_data = {}
        unique_targets = self.train_df[self.target_name].unique()

        for target in unique_targets:
            relevant_data = self.train_df[self.train_df[self.target_name] == target]
            features_dict = {
                feature: relevant_data[feature].value_counts().to_dict()
                for feature in relevant_data.columns if feature != self.target_name
            }
            result_data[target] = features_dict

        return result_data

    def test(self):
        tester = Tester(self.classifier, self.test_df, self.target_name)
        score = tester.test()
        return score

    def check_data_point(self, data_point):
        predicted_target = self.classifier.calculate_bayes_score(data_point)
        return predicted_target
