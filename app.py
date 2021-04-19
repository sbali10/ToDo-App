
import streamlit as st

import pandas as pd    #eda pkg

def main():
    st.title("ToDo App SB")

    menu = ["create","read","update","delete","about"]
    choice = st.sidebar.selectbox("Menu",menu)

    if choice == "create":
        st.subheader("Add Items")

        col1,col2 = st.beta_columns(2)

        with col1:
            task = st.text_area("task to do")

        with col2:
            task_status = st.selectbox("Status",["ToDo","Doing","Done"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            st.success("Succesfull added data:{}".format(task))

    elif choice == "Read":
        st.subheader("view items")

    elif choice == "Update":
        st.subheader("Edit/Update Items")
    elif choice == "Delete":
        st.subheader("Delete Item")

    else:
        st.subheader("About")

if __name__== '__main__':
    main()
