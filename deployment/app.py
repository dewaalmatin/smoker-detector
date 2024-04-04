import streamlit as st
import eda
import prediction as pred

def main():
    st.sidebar.title('Navigation')
    page = st.sidebar.radio("Go to", ('EDA', 'Inference'))

    if page == 'Inference':
        pred.main()
    else:
        eda.main()

if __name__ == "__main__":
    main()