import streamlit as st
import openai

# Set up your OpenAI API key
openai.api_key = st.secrets["openai_api_key"]

# Streamlit App
def main():
    
    # Description
    st.markdown(
        "Ensuring the health of plants is crucial for a thriving garden. "
        "Discover effective remedies and treatments for various plant diseases, "
        "as they play a vital role in safeguarding your plants from harm."
    )

    # User input for plant disease
    disease_name = st.text_input("Enter the name of the plant disease:")

    if st.button("Get Remedies"):
        if disease_name:
            # Call OpenAI API to get a precise answer
            response, additional_requirements = get_openai_response(disease_name)

            # Display the response
            st.markdown(f"**Remedies and Treatments for {disease_name}**")
            st.write(response)

            # Display additional requirements if any
            if additional_requirements:
                st.markdown("**Additional Requirements:**")
                st.write(additional_requirements)
        else:
            st.warning("Please enter the name of the plant disease.")

# Function to get a precise answer from OpenAI
def get_openai_response(disease_name):
    prompt = f"Provide remedies and treatments for {disease_name} in plants."

    # You can adjust the temperature and max tokens for your specific needs
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=150,
        n=1,
        stop=None
    )

    # Placeholder for additional requirements (you can customize this based on your data)
    additional_requirements = ""

    # Add logic to determine additional requirements based on the disease
    if disease_name.lower() == "tomato big bud":
        additional_requirements = (
            "- Apply a specialized fungicide\n"
            "- Ensure proper spacing between plants\n"
            "- Remove infected leaves promptly"
        )

    return response['choices'][0]['text'], additional_requirements

if __name__ == "__main__":
    main()
