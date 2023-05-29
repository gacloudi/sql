import pandas as pd
import streamlit as st
import sqlite3
conn = sqlite3.connect('college.db', check_same_thread=False)
st.set_page_config(layout="wide")
menu = ["College","Score & Category"]
choice = st.selectbox(":blue[Choose a Selection]",menu)
c = conn.cursor()
q="SELECT * FROM college"
c.execute(q)
data = c.fetchall()
clean_db = pd.DataFrame(data,columns=["College_Code","College_Name","BRANCHCODE","OC","BC","BCM","MBCV","MBCDNC","MBC","SC","SCA","ST"])
dd_list=clean_db.College_Name.unique()
cols1,cols2=st.columns(2)

def highlight_cells(val,color_if_true,color_if_false):
    color=color_if_true if val==1 else color_if_false
    return 'background-color: {}'.format(color)
cell_hover = {
    "selector": "td:hover",
    "props": [("background-color", "#FFFFE0")]
}
headers = {
    "selector": "th:not(.index_name)",
    "props": "background-color: #800000; color: white;"
}

#st.write(clean_db)
#college_db=clean_db[clean_db[]
if choice=="Score & Category":
    with cols1:
        score=st.number_input('Enter Your Score:')
    with cols2:
        category=st.selectbox('Enter Your Category',["OC","BC","BCM","MBCV","MBCDNC","MBC","SC","SCA","ST"])
    score1=score + 5
    score2=score - 5
    college_db=clean_db.loc[:, ['College_Code','College_Name','BRANCHCODE',category]]
    output_db=college_db[college_db[category]<score1]
    op=college_db[(college_db[category] <= score1) & 
                (college_db[category]>=score2)] 
    #st.write(op)

    #st.table(op)
    op=op.style.hide_index()\
                            .set_table_styles([{'selector': 'th','props': [('background-color', '#ADD8E6'),('font-size','7'),('color', '#000005'),('font-weight', 'bold')]}])
                            #.set_table_styles([{'selector': 'th','props': [('font-weight', 'bold')]}])\
                            #set_table_styles([{'selector': 'th','props': [('color', '#000000')]}])
                            #.applymap(highlight_cells,color_if_true='#2E8B57',color_if_false='#CB6D51',subset=['BC'])
    #st.dataframe(op)
    #st.write(op)

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(op)
if choice=="College":
    scollege=st.selectbox('Select the College',dd_list)
    output_db=clean_db[clean_db['College_Name']==scollege]
    op=output_db.style.hide_index()\
                            .set_table_styles([{'selector': 'th','props': [('background-color', '#ADD8E6'),('font-size','7'),('color', '#000005'),('font-weight', 'bold')]}])
                            #.set_table_styles([{'selector': 'th','props': [('font-weight', 'bold')]}])\
                            #set_table_styles([{'selector': 'th','props': [('color', '#000000')]}])
                            #.applymap(highlight_cells,color_if_true='#2E8B57',color_if_false='#CB6D51',subset=['BC'])
    #st.dataframe(op)
    #st.write(op)

    hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                """

    # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)

    st.table(op)

