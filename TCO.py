import pandas as pd
import streamlit as st
import sqlite3
def main():
   
    conn = sqlite3.connect('college.db', check_same_thread=False)
    c = conn.cursor()

    c.execute('CREATE TABLE IF NOT EXISTS college (COLLEGECODE Text,COLLEGENAME Text,BRANCHCODE Text,OC number,BC number,BCM number,MBCV number,MBCDNC number,MBC number,SC number,SCA number,ST number)')
    #"COLLEGECODE"	COLLEGE NAME	BRANCH CODE	OC	BC	BCM	MBC	SC	SCA	ST
    conn.commit()
    f=st.file_uploader(":green[Upload a Invoice file]")
    if f is not None:
        df=pd.read_csv(f,encoding='cp1252')
    st.write(df)
    df.to_sql('college',conn,if_exists='append',index=False)
    

if __name__ == '__main__':
	main()
