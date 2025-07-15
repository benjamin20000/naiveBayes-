from model.manager import ModelManager
class Cli:
    def display(self):
        self.main_menu()

    def main_menu(self):
        exit = True
        while exit:
            print("1. enter data")
            print("2. exit")
            client_choice = input()
            if client_choice == '1':
                self.enter_data()
                exit = False
            elif client_choice == '2':
                exit = False
            else:
                print("no valid input...")

    def enter_data(self):
        file_path = input("enter file path")
        index_name = input("enter index col name")
        target_name = input("enter target col name")

        self.model_manager = ModelManager(file_path,index_name,target_name)
        self.model_menu()


    def model_menu(self):
        exit = True
        while exit:
            client_choice = input("""
                        1. test the model
                        2. enter data point
                        3. exit
                           """)
            if client_choice == '1':
                self.test()
            elif client_choice == '2':
                self.ask_model()
            elif client_choice == '3':
                exit = False




    def test(self):
        score = self.model_manager.test()
        print(f"the score is {score}%")

    def ask_model(self):
        data_point = {}
        for feature in self.model_manager.df.columns:
            if feature == self.model_manager.target_name:
                continue
            print(f"Choose a value for feature '{feature}':")
            chosen_feature = input()
            data_point[feature] = chosen_feature
        predicted_class = self.model_manager.check_data_point(data_point)
        print(f" your data is probably {predicted_class}")




