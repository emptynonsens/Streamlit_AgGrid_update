import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

# DATA
data = pd.read_csv('netflix_titles.csv')
data = data[['show_id', 'type', 'title', 'release_year', 'duration']]

# ST WIDGETS
#selection_mode = st.radio('Selection Type', options = ['single','multiple'])

# GRID CONFIG
gd = GridOptionsBuilder.from_dataframe(data)
gd.configure_pagination(enabled=True)
#gd.configure_default_column(editable = True, groupable = False)
gd.configure_column("type", header_name="First", editable=True)
#gd.configure_default_column('type', editable = True, groupable = False)
gd.configure_selection(selection_mode='single', use_checkbox= False)

gridoptions=gd.build()
#_selectedRowNodeInfo
dataGrid = AgGrid(data, gridOptions=gridoptions,
                #update_mode=GridUpdateMode.SELECTION_CHANGED,
                height = 500,
                allow_unsafe_jscode=True,
                theme='streamlit'
                )

v = dataGrid['selected_rows']

if v:
    st.write('')
    #st.dataframe(v)
    # for key, value in v[0].items():
    #      st.write(key, value)
    show_id =v[0].get('show_id')
    type_ =v[0].get('type')
    #v.get(show_id)
    # for item in v:
    #     st.write(item)
    #     for item2 in item:
    #         st.write(item2)
    
    # HERE TO IMPLEMENT SQL ALCHEMY
    x = "UPDATE dbo.SomeTable SET type = '%s'  WHERE ID = %s" % (type_, show_id)
    #st.write(x)
    dfs = pd.DataFrame(v)

    if st.button('Update in db'):
        st.markdown(x)
        st.write('do tego audyt na sql albo z sqlalchemy')
    else:
        st.write('Click on the button if you want to commit your update')


   