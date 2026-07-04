import logic
import pandas as pd
import streamlit as st

st.secrets = {
    "google_sheets": {
        "URL_DASHBOARD": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQja_fR8Af6b1e41kdaGWvmiP5M-NDfJLvCGSL0jv38ZXpATigAhZCBTu2Xq1tV6kVrjuGfacPZVSle/pub?gid=40883231&single=true&output=csv",
        "URL_ACCOUNT": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQja_fR8Af6b1e41kdaGWvmiP5M-NDfJLvCGSL0jv38ZXpATigAhZCBTu2Xq1tV6kVrjuGfacPZVSle/pub?gid=2038053740&single=true&output=csv",
        "URL_CALENDAR": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQja_fR8Af6b1e41kdaGWvmiP5M-NDfJLvCGSL0jv38ZXpATigAhZCBTu2Xq1tV6kVrjuGfacPZVSle/pub?gid=712389288&single=true&output=csv",
        "URL_RECORDS": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQja_fR8Af6b1e41kdaGWvmiP5M-NDfJLvCGSL0jv38ZXpATigAhZCBTu2Xq1tV6kVrjuGfacPZVSle/pub?gid=1476127016&single=true&output=csv",
        "URL_PNL_DAILY": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQja_fR8Af6b1e41kdaGWvmiP5M-NDfJLvCGSL0jv38ZXpATigAhZCBTu2Xq1tV6kVrjuGfacPZVSle/pub?gid=1294893673&single=true&output=csv",
        "URL_PNL_MONTHLY": "https://docs.google.com/spreadsheets/d/e/2PACX-1vQja_fR8Af6b1e41kdaGWvmiP5M-NDfJLvCGSL0jv38ZXpATigAhZCBTu2Xq1tV6kVrjuGfacPZVSle/pub?gid=502396230&single=true&output=csv"
    }
}

try:
    all_data = logic.load_all_data(st.secrets["google_sheets"])
    print("DASHBOARD SHAPE:", all_data["URL_DASHBOARD"].shape)
    print(all_data["URL_DASHBOARD"].head(20))
except Exception as e:
    import traceback
    traceback.print_exc()
