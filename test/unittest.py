import unittest


class testBmi(unittest.TestCase):

    def bmiTest(self):
        expected_data = [
            {"Gender": "Male", "HeightCm": 171, "WeightKg": 96, "BMI": 56.1, "BMIcategory": "Very severely obese",
             "Health risk": "Very high risk"},
            {"Gender": "Male", "HeightCm": 161, "WeightKg": 85, "BMI": 52.8, "BMIcategory": "Very severely obese",
             "Health risk": "Very high risk"},
            {"Gender": "Male", "HeightCm": 180, "WeightKg": 77, "BMI": 42.8, "BMIcategory": "Very severely obese",
             "Health risk": "Very high risk"},
            {"Gender": "Female", "HeightCm": 166, "WeightKg": 62, "BMI": 37.3, "BMIcategory": "Severely obese",
             "Health risk": "High risk"},
            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70, "BMI": 46.7, "BMIcategory": "Very severely obese",
             "Health risk": "Very high risk"},
            {"Gender": "Female", "HeightCm": 167, "WeightKg": 82, "BMI": 49.1, "BMIcategory": "Very severely obese",
             "Health risk": "Very high risk"}]

        actual_data = '''
              [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
               { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
               { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
               { "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
               {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
               {"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]
              '''

        json_data = json.loads(actual_data)

        test_df = pd.json_normalize(json_data)

        expected_output = pd.DataFrame(expected_data)

        assert calcBmi(test_df).equals(expected_output)