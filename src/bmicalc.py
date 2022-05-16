import numpy as np

def calcBmi(df):

    """
    Function to return a dataframe with calculated BMI, Assessed category and Risk level
    param df - a dataframe
    return: df
    """

    df['BMI'] = round(df['WeightKg'] / (df['HeightCm'] * 0.01), 1)

    cond = [
        (df['BMI'] <= 18.4),
        (df['BMI'] > 18.4) & (df['BMI'] <= 24.9),
        (df['BMI'] > 24.9) & (df['BMI'] <= 29.9),
        (df['BMI'] > 29.9) & (df['BMI'] <= 34.9),
        (df['BMI'] > 34.9) & (df['BMI'] <= 39.9),
        (df['BMI'] >= 40)
    ]

    values = ['Underweight', 'Normal weight ', 'Overweight', 'Moderately obese', 'Severely obese',
              'Very severely obese']
    values1 = ['Malnutrition risk', 'Low risk', 'Enhanced risk', 'Medium risk', 'High risk', 'Very high risk']

    df['BMIcategory'], df['Health risk'] = np.select(cond, values), np.select(cond, values1)

    return df
