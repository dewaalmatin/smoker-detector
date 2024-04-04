import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import phik

def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.title('Exploratory Data Analysis')
    st.write("On Smoker's Health Dataset")

    data = pd.read_csv('smoking.csv')

    st.subheader('Preview')
    st.write(data.head(10))

    cat_cols = ['hearing(left)', 'hearing(right)', 'dental caries']
    num_cols = ['height(cm)', 'weight(kg)', 'waist(cm)', 'eyesight(left)', 'eyesight(right)', 
            'systolic', 'relaxation', 'fasting blood sugar', 'Cholesterol', 'triglyceride', 'HDL', 
            'LDL', 'hemoglobin', 'Urine protein', 'serum creatinine', 'AST', 'ALT', 'Gtp']

    #set style
    sns.set_style('whitegrid')

    st.subheader('Data Distributions')
    #distribution plot function
    def diagnostic_plots(df, variable):
        # Define figure size
        plt.figure(figsize=(16, 4))

        # Histogram
        plt.subplot(1, 2, 1)
        sns.histplot(df[variable], kde=True)
        plt.title('Histogram')

        # Boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(y=df[variable])
        plt.title('Boxplot')

        st.pyplot()

    #plot the distribution
    for col in num_cols:
        st.write(f'{col}')
        diagnostic_plots(data, col)

    st.subheader('Correlation Analysis')
    df_corr = data.copy()
    df_corr = df_corr.drop(columns='ID')

    #calculating the phi_k correlation matrix
    phi_k_correlation = df_corr.phik_matrix()

    #plot the matrix
    plt.figure(figsize=(12, 10))
    sns.heatmap(phi_k_correlation, annot=True, fmt=".2f", linewidths=.5, cmap='coolwarm')
    plt.title('Phi_k Correlation Matrix Heatmap')
    st.pyplot()

    st.subheader('Smoker by Gender')
    df_gender = data[['gender', 'smoking']]
    plt.figure(figsize=(8, 6))
    sns.countplot(data=df_gender, x='gender', hue='smoking', palette='bright')
    plt.title('Distribution of Smokers and Non-Smokers by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.legend(title='Smoking', loc='upper right')
    st.pyplot()

    st.subheader('Smoker by Age')
    df_age = data[['age', 'smoking']]
    sns.displot(df_age, x='age', hue="smoking", kind="kde", fill=True, palette='bright')
    st.pyplot()

    st.subheader('Demography Body Build')
    #Pairplot
    corr_cols = ['gender', 'age', 'height(cm)', 'weight(kg)', 'waist(cm)']
    sns.pairplot(data[corr_cols])
    st.pyplot()