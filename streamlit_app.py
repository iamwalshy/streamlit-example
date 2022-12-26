import streamlit as st

# Create a dictionary to store our projects
projects = {}

# Define a function to create a new project
def create_project(name, description):
    project = {
        'name': name,
        'description': description,
        'tasks': []
    }
    projects[name] = project

# Define a function to create a new task
def create_task(project, name, description):
    task = {
        'name': name,
        'description': description,
        'completed': False
    }
    projects[project]['tasks'].append(task)

# Define a function to mark a task as complete
def complete_task(project, task):
    for t in projects[project]['tasks']:
        if t['name'] == task:
            t['completed'] = True
            break

# Create a Streamlit sidebar to allow users to create and view projects
st.sidebar.title('Projects')

# Add a button to create a new project
if st.sidebar.button('Create Project'):
    name = st.sidebar.text_input('Name')
    description = st.sidebar.text_input('Description')
    create_project(name, description)

# Add a dropdown menu to select a project
selected_project = st.sidebar.selectbox('Select a project', list(projects.keys()))

# Display the tasks for the selected project
if selected_project:
    st.title(selected_project)
    st.write(projects[selected_project]['description'])
    st.write('Tasks:')
    for task in projects[selected_project]['tasks']:
        if task['completed']:
            st.write(f'[x] {task["name"]}')
        else:
            st.write(f'[ ] {task["name"]}')
    # Add a button to create a new task
    if st.button('Create Task'):
        task_name = st.text_input('Name')
        task_description = st.text_input('Description')
        create_task(selected_project, task_name, task_description)
    # Add a button to mark a task as complete
    if st.button('Complete Task'):
        task = st.selectbox('Select a task', [t['name'] for t in projects[selected_project]['tasks']])
        complete_task(selected_project, task)
