import streamlit as st

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Side Hustle", page_icon=":tada:", layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", usafe_allow_html=True)

        local_css("style/style.css")

st.markdown("""
<style>
.css-6q9sum.ef3psqc3

{
    visibility:  hidden;
}
            
.css-ch5dnh.ef3psqc4
{
    visibility: hidden;            
}

.css-z3au9t.ea3mdgi2
    {
            visibility: hidden;
    } 
.css-cio0dv.ea3mdgi1
    {
        visibility: hidden;
    }         
            
</style>
""", unsafe_allow_html=True)

# st.container():

st.header("BUSINESS MANAGEMENT",)

st.subheader("Hi, I am Umar Muhammad Tukur :wave:")
st.title("AN Online Business from Nigeria")

st.write("Imagine being able to make hundreds of thousands or even millions by having a profitable side hustle on top of your current business.")
st.image("Image1.jpg", width=700)

# with st.container():
st.write("---")

st.write("Imagine learning the Simple set of skills that business are paying top dollar for")
st.write("Imagine having a skills that businesss realy need and to pay buck for")
st.write("Having one stream of income is a risk becouse that business can fold up, By then your are going to go into financial crisis, but if you have a side hustle and that happened you will easily siwitch to your sidehustle.")
st.image("side-hustle-2.jpg", width=700)
st.write("This is for anyone lookingfor a profitable side hustle, to add on top of jis thier business")
st.write("If you are stay at home num looking for a profitable online side hustle your start from home.")
st.write("You are 9-5 corporate worker looking for lucrative side hustle you can do to increase your revenue.")


with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")


# Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
contact_form = """
<form action="https://formsubmit.co/umartukur55@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="You gmail" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
