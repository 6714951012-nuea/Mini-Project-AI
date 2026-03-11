import streamlit as st
import requests

st.title("AI English Grammar Checker")

text = st.text_area("Enter your sentence")

if st.button("Check Grammar"):

    url = "https://api.languagetool.org/v2/check"

    data = {
        "text": text,
        "language": "en-US"
    }

    response = requests.post(url, data=data)
    result = response.json()

    matches = result["matches"]

    if len(matches) == 0:
        st.success("No grammar mistakes found!")
    else:
        for match in matches:
            st.caption("Mini Project AI + Cloud | Grammar Checker using LanguageTool API")
            st.error("Grammar Issue:")
            st.write(match["message"])
            suggestions = [r["value"] for r in match["replacements"]]
            st.success("Suggestions:")
            st.write(", ".join(suggestions))