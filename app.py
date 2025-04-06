import streamlit as st
from recommender import SHLRecommender

st.set_page_config(page_title="SHL Assessment Recommender", layout="wide")
recommender = SHLRecommender()

st.title("🔍 SHL Assessment Recommender")
query = st.text_area("Enter Job Description or Requirement", "")

if st.button("Get Recommendations") and query:
    with st.spinner("Finding best assessments..."):
        results = recommender.recommend(query, top_k=10)

    st.subheader("Top Recommendations")
    for res in results:
        st.markdown(f"### [{res['name']}]({res['url']})")
        st.write(f"- Duration: {res['duration']}")
        st.write(f"- Remote Testing: {res['remote']}")
        st.write(f"- Adaptive/IRT: {res['adaptive']}")
        st.write(f"- Type: {res['type']}")
        st.markdown("---")
