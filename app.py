import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(
    page_title="Iron Lady – Internal Enrollment Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------------
# SESSION STATE INIT
# -------------------------------
if "enrollments" not in st.session_state:
    st.session_state.enrollments = []

# -------------------------------
# CUSTOM CSS (UNIQUE UI)
# -------------------------------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
h1, h2, h3 {
    color: #ffffff;
}
label {
    color: #cfd8dc !important;
}
.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 10px;
    height: 45px;
    font-weight: 600;
}
.stButton>button:hover {
    transform: scale(1.03);
}
.card {
    background: rgba(255,255,255,0.06);
    padding: 25px;
    border-radius: 16px;
    margin-bottom: 25px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.3);
}
.success {
    background-color: #1b5e20;
    padding: 12px;
    border-radius: 8px;
    color: #c8e6c9;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<h1>🛡️ Iron Lady – Internal Enrollment Dashboard</h1>
<p style="color:#b0bec5;">
Internal system to manage program enrollments efficiently
</p>
""", unsafe_allow_html=True)

# ===============================
# ADD ENROLLMENT
# ===============================
# st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📋 Add New Enrollment")

name = st.text_input("Candidate Name")
email = st.text_input("Email Address")
program = st.selectbox(
    "Program",
    ["Skill Development Program", "Leadership Program", "Career Readiness Program"]
)
status = st.selectbox("Status", ["Pending", "Approved", "Rejected"])

if st.button("Add Enrollment"):
    if name and email:
        st.session_state.enrollments.append({
            "Name": name,
            "Email": email,
            "Program": program,
            "Status": status
        })
        st.success("Enrollment added successfully")
        st.rerun()
    else:
        st.warning("Please fill all required fields")

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# MANAGE ENROLLMENTS
# ===============================
# st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("### 📊 Manage Enrollments")

if st.session_state.enrollments:
    df = pd.DataFrame(st.session_state.enrollments)
    st.dataframe(df, use_container_width=True)
else:
    st.info("No enrollments yet")

st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# UPDATE STATUS
# ===============================
if st.session_state.enrollments:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🔄 Update Enrollment Status")

    email_list = [e["Email"] for e in st.session_state.enrollments]

    selected_email = st.selectbox("Select Enrollment (by Email)", email_list)
    new_status = st.selectbox("New Status", ["Pending", "Approved", "Rejected"])

    if st.button("Update Status"):
        for e in st.session_state.enrollments:
            if e["Email"] == selected_email:
                e["Status"] = new_status
        st.success("Status updated successfully")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ===============================
# DELETE ENROLLMENT
# ===============================
if st.session_state.enrollments:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🗑️ Delete Enrollment")

    delete_email = st.selectbox("Select Enrollment to Delete", email_list)

    if st.button("Delete Enrollment"):
        st.session_state.enrollments = [
            e for e in st.session_state.enrollments
            if e["Email"] != delete_email
        ]
        st.success("Enrollment deleted successfully")
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
