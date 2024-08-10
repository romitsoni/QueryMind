import streamlit as st
from langchain_helper import get_few_shot_db_chain

st.set_page_config(page_title="AtliQ T-Shirts Q&A", page_icon="👕", layout="centered")


st.title("AtliQ T-Shirts: Database Q&A 👕")
st.write("Welcome to AtliQ T-Shirts Database Q&A! Ask anything about our T-shirt inventory and get instant answers!")


question = st.text_area("Enter your question here:", height=100)


if st.button("Submit"):
    if question.strip():
        with st.spinner("Processing your query..."):
            chain = get_few_shot_db_chain()
            response = chain.run(question)
        
       
        st.header("Answer")

        
        if isinstance(response, list) and all(isinstance(i, tuple) for i in response):
            
            formatted_data = [{"Color": row[0], "Size": row[1], "Stock Quantity": row[2]} for row in response]
            st.table(formatted_data)
        else:
            st.success(response)
    else:
        st.warning("Please enter a question to get started!")


st.markdown(
    """
    ---
    **Tips:**
    - Be specific with your queries for better results.
    - You can ask about T-shirt quantities, prices, discounts, and more!
    """
)
