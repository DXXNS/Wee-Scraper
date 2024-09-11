import requests
from bs4 import BeautifulSoup
import streamlit as st


st.title(":green[Wee Scraper]")

url = st.text_input("Enter the URL of the website")

filtering = st.checkbox("Enable filtering by HTML class/type")


if filtering:
  html_class = st.text_input("Enter the HTML class/type to filter")


if st.button("Scrape"):
  if url:

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")


    if filtering:
      elements = soup.find_all("div", class_=html_class)
    else:
      elements = soup.find_all(True)

    
    tab1, tab2, tab3 = st.tabs(["Text", "Images", "Links"])

    with tab1:
      st.subheader("Text")
      #
      text_content = "\n".join(
          [element.get_text() for element in elements if element.get_text()])
      st.text_area("Scraped Text", text_content)

    with tab2:
      st.subheader("Images")
      
      image_elements = soup.find_all("img")
      for img in image_elements:
        img_url = img.get("src")
        if img_url:
          st.image(img_url)

    with tab3:
      st.subheader("Links")
      
      link_elements = soup.find_all("a", href=True)
      for link in link_elements:
        href = link.get("href")
        link_text = link.get_text() or href
        st.markdown(f"[{link_text}]({href})")
  else:
    st.error("Please enter a valid URL.")

footer = """
    <style>
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            
            color: white;
            text-align: center;
            padding: 10px;
        }
        .footer a {
            color: lightblue;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
    </style>
    <div class="footer">
        <a href="https://www.example.com" target="_blank">Made by Reifensepp - All Rights Reserved</a>
    </div>
"""
st.markdown(footer, unsafe_allow_html=True)
