
import streamlit as st

import pandas as pd    #eda pkg
import plotly.express as px

from db_fxns import (create_table,add_data,view_all_data,get_task,view_unique_tasks,edit_task_data,delete_data)

def main():
    st.title("ToDo App SB")

    menu = ["Create","Read","Update","Delete","About"]
    choice = st.sidebar.selectbox("Menu",menu)

    create_table()
    if choice == "Create":
        st.subheader("Add Items")

        col1,col2 = st.beta_columns(2)

        with col1:
            task = st.text_area("Task To Do")

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
        df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
        with st.beta_expander("View All Data"):
            st.dataframe(df)

        with st.beta_expander("Task Status"):
            task_df = df['Status'].value_counts().to_frame()
            
            task_df = task_df.reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df,names='index',values='Status')
            st.plotly_chart(p1)


    elif choice == "Update":
        st.subheader("Edit/Update Items")
        result = view_all_data()
        df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
        with st.beta_expander("Current Data"):
            st.dataframe(df)

        #st.write(view_unique_tasks())
        list_of_task = [i[0] for i in view_unique_tasks()]
        #st.write(list_of_task)

        selected_task = st.selectbox("Task To Edit",list_of_task)

        selected_result = get_task(selected_task)
        st.write(selected_result)
        if selected_result:
            task = selected_result[0][0]
            task_status = selected_result[0][1]
            task_due_date = selected_result[0][2]

            col1,col2 = st.beta_columns(2)

            with col1:
                new_task = st.text_area("Task To Do",task)

            with col2:
                new_task_status = st.selectbox(task_status,["ToDo","Doing","Done"])
                new_task_due_date = st.date_input(task_due_date)

            if st.button("Update Task"):
                edit_task_data(new_task,new_task_status,new_task_due_date,task,task_status,task_due_date)
                st.success("Succesfull Updated:: {} To ::{}".format(task,new_task))

        result2 = view_all_data()
        df2 = pd.DataFrame(result2,columns=['Task','Status','Due Date'])
        with st.beta_expander("Updated Data"):
            st.dataframe(df2)

    elif choice == "Delete":
        st.subheader("Delete Item")
        result = view_all_data()
        df = pd.DataFrame(result,columns=['Task','Status','Due Date'])
        with st.beta_expander("Current Data"):
            st.dataframe(df)

        list_of_task = [i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Delete",list_of_task)
        st.warning("Do you want to Delete ::{}".format(selected_task))
        if st.button("Delete Task"):
            delete_data(selected_task)
            st.success("Task has been succesfully deleted")

        new_result = view_all_data()
        df2 = pd.DataFrame(new_result,columns=['Task','Status','Due Date'])
        with st.beta_expander("Updated Data"):
            st.dataframe(df2)

    else:
        st.subheader("About")
        st.write(" Create, Read, Update, and Delete (CRUD) are the four basic functions that models should be able to do, at most. This ToDo-App is created to test CRUD functionalities by sbali ")

if __name__== '__main__':
    main()
