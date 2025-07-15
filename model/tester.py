from tqdm import tqdm
class Tester:
    def __init__(self, classifier, test_df, target_name='class'):
        self.classifier = classifier
        self.test_df = test_df
        self.target_name = target_name

    def test(self):
        success_count = 0
        total = len(self.test_df)

        for index, row in tqdm(self.test_df.iterrows(), total=len(self.test_df)):
            data_point = row.drop(self.target_name).to_dict()
            predicted_target = self.classifier.calculate_bayes_score(data_point)

            if predicted_target == row[self.target_name]:
                success_count += 1

        accuracy = (success_count / total) * 100
        return accuracy
