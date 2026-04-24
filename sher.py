import streamlit as st

# عنوان الموقع
st.title("اهلا بك في موقع الطاهر")

# خانات الإدخال (الواجهة)
name = st.text_input("What is your name?")
age = st.text_input("What is your age?")

# زرار لتنفيذ الكود
if st.button("اضغط هنا"):
    if name and age:
        # عرض النتيجة بشكل شيك بدل print
        st.success(f"fuck you {name}!")
        st.info(f"You are baby {age} .")
    else:
        st.warning("من فضلك ادخل اسمك وعمرك الأول")
