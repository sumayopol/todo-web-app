import streamlit as st
import function

st.title("My ToDo App")
st.subheader("My Daily Todo List")

#fetched the contents of todo.txt in a list format
todos = function.get_todos()

#Add new todo to the file todo.txt thru the write_todo function
def add_todo():
    todo = st.session_state["new_todo"] + "\n" #Captures the text inside the text box to a variable
    todos.append(todo)
    function.write_todos(todos)
    st.session_state["new_todo"] = "" #clears the text input box

# check if any checkbox is checked. if so the specific todo is removed
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos) #changes are written to todo.txt
        del st.session_state[todo]
        st.rerun()


st.text_input(label="", placeholder="Enter a todo", on_change=add_todo, key="new_todo")

