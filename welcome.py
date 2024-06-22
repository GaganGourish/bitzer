import streamlit as st


def main():
    """welcome page"""
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Welcome to PulseLang Web App! 👋")

    st.sidebar.success("Select a web page above ☝️")

    st.markdown(
        """
        Pet_Bot is an innovative digital companion designed to bring the joy and responsibilities of pet ownership into the virtual world. 
        With Pet_Bot, users can experience the delights of caring for a pet, all from the comfort of their devices. Here's a closer look at 
        what makes Pet_Bot a unique and engaging experience:
        
        Pet_Bot is more than just a digital pet; it's a companion that brings the joys and challenges of pet ownership into the 
        virtual realm. Whether you're looking for an educational tool, a convenient pet alternative, or simply a fun and engaging 
        experience, Pet_Bot is designed to meet your needs. Embrace the future of pet care with Pet_Bot, and enjoy the unique bond 
        that comes with nurturing your very own digital companion.
        
        ### Want to know about project's gitHub repository?
        - Check out [PulseLang](https://github.com/anirudh-hegde/pulselang)
    
    """
    )
    st.snow()


if __name__ == "__main__":
    main()
