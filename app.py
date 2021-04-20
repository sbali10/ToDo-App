
import streamlit as st

import pandas as pd    #eda pkg

from db_fxns import create_table,add_data,view_all_data

def main():
    st.title("ToDo App SB")

    menu = ["Create","Read","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    create_table()
    if choice == "create":
        st.subheader("Add Items")

        col1,col2 = st.beta_columns(2)

        with col1:
            task = st.text_area("task to do")

        with col2:
            task_status = st.selectbox("Status",["ToDo","Doing","Done"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            add_data(task,task_status,task_due_date)
            st.success("Succesfull added data:{}".format(task))

    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_data()
        st.write(result)

    elif choice == "Update":
        st.subheader("Edit/Update Items")
    elif choice == "Delete":
        st.subheader("Delete Item")

    else:
        st.subheader("About")

if __name__== '__main__':
    main()
