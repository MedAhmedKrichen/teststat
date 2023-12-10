import streamlit as st
import pickle
import joblib


with open('modeldt.pkl', 'rb') as f:
    clf2 = pickle.load(f)

st.title("Machine Learning Deploy (DT Model)")


attributes = ['duration', 'land', 'hot', 'logged_in', 'count', 'srv_count',
       'serror_rate', 'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate',
       'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate',
       'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate',
       'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
       'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
       'dst_host_srv_serror_rate', 'dst_host_rerror_rate',
       'dst_host_srv_rerror_rate']



ranges = [[0, 42908],[0, 1],[0, 77],[0, 1],[0, 511],[0, 163],
 [0.0, 1.0],[0.0, 1.0],[0.0, 1.0],[0.0, 1.0],[0.0, 1.0],[0.0, 1.0],
 [0.0, 1.0],[0, 255],[0, 255],[0.0, 1.0],[0.0, 1.0],[0.0, 1.0],
 [0.0, 1.0],[0.0, 1.0],[0.0, 1.0],[0.0, 1.0],[0.0, 1.0]]

values = []
for i in range(len(attributes)):
    if i ==1 or i == 3:
        val_att = attributes[i]+" ("+str(ranges[i][0])+' or '+str(ranges[i][1])+')'
        values.append(st.text_input(val_att))
        continue
    val_att = attributes[i]+" ("+str(ranges[i][0])+','+str(ranges[i][1])+')'
    values.append(st.text_input(val_att))


Classify = st.button("Classify")
m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: rgb(204, 49, 49);
                
}
    button {
    height: auto;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
    padding-right: 100px !important;
    padding-left: 100px !important;
    font-size: 25px;  
    
}
</style>""", unsafe_allow_html=True)

if Classify:
    res = clf2.predict([values])
    if res[0] ==0:       
        st.markdown('<p color="green"> Normal </p>', unsafe_allow_html=True)
    else:
        st.markdown('<p color="red"> Attack</p>', unsafe_allow_html=True)







# clf2.predict(d_raw_test)