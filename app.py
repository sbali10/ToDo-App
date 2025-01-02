import streamlit as st
import pandas as pd  # EDA package
import plotly.express as px

from db_fxns import (
    create_table,
    add_data,
    view_all_data,
    get_task,
    view_unique_tasks,
    edit_task_data,
    delete_data
)

def main():
    st.title("ToDo App SB")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == "Create":
        st.subheader("Add Items")

        col1, col2 = st.columns(2)

        with col1:
            task = st.text_area("Task To Do")

        with col2:
            task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"])
            task_due_date = st.date_input("Due Date")

        if st.button("Add Task"):
            add_data(task, task_status, task_due_date)
            st.success("Successfully added data: {}".format(task))

    elif choice == "Read":
        st.subheader("View Items")
        result = view_all_data()
        st.write(result)
        df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])

        with st.expander("View All Data"):
            st.dataframe(df)

        with st.expander("Task Status"):
            task_df = df['Status'].value_counts().to_frame().reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df, names='index', values='Status')
            st.plotly_chart(p1)

    elif choice == "Update":
        st.subheader("Edit/Update Items")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])

        with st.expander("Current Data"):
            st.dataframe(df)

        list_of_task = [i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Edit", list_of_task)

        selected_result = get_task(selected_task)
        if selected_result:
            task, task_status, task_due_date = selected_result[0]

            col1, col2 = st.columns(2)

            with col1:
                new_task = st.text_area("Task To Do", task)

            with col2:
                new_task_status = st.selectbox("Status", ["ToDo", "Doing", "Done"], index=["ToDo", "Doing", "Done"].index(task_status))
                new_task_due_date = st.date_input("Due Date", task_due_date)

            if st.button("Update Task"):
                edit_task_data(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
                st.success(f"Successfully Updated: {task} To: {new_task}")

        result2 = view_all_data()
        df2 = pd.DataFrame(result2, columns=['Task', 'Status', 'Due Date'])

        with st.expander("Updated Data"):
            st.dataframe(df2)

    elif choice == "Delete":
        st.subheader("Delete Item")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['Task', 'Status', 'Due Date'])

        with st.expander("Current Data"):
            st.dataframe(df)

        list_of_task = [i[0] for i in view_unique_tasks()]
        selected_task = st.selectbox("Task To Delete", list_of_task)
        st.warning(f"Do you want to delete: {selected_task}?")

        if st.button("Delete Task"):
            delete_data(selected_task)
            st.success("Task has been successfully deleted")

        new_result = view_all_data()
        df2 = pd.DataFrame(new_result, columns=['Task', 'Status', 'Due Date'])

        with st.expander("Updated Data"):
            st.dataframe(df2)

    else:
        st.subheader("About")
        st.write("Create, Read, Update, and Delete (CRUD) are the four basic functions that models should be able to do. This ToDo App is created to test CRUD functionalities by sbali.")

if __name__ == '__main__':
    main()
