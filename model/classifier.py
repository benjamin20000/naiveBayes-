class Classifier:
    def __init__(self, training_dict, target_counts, df, target_name='class'):
        self.training_dict = training_dict
        self.target_counts = target_counts
        self.df = df
        self.target_name = target_name

    def calculate_likelihood(self, data_point, target):
        likelihood = 1
        for feature in data_point.keys():
            k = self.df[feature].nunique()
            value = data_point[feature]

            if value in self.training_dict[target][feature]:
                numerator = self.training_dict[target][feature][value] + 1
            else:
                numerator = 1

            denominator = self.target_counts[target] + k
            likelihood *= numerator / denominator

        return likelihood

    def calculate_bayes_score(self, data_point):
        total_records = len(self.df)
        scores = {}

        for target in self.training_dict.keys():
            prior = self.target_counts[target] / total_records
            likelihood = self.calculate_likelihood(data_point, target)
            scores[target] = prior * likelihood

        return max(scores, key=scores.get)