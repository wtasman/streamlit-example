# Import necessary libraries
import openai
import streamlit as st

# Setup OpenAI
openai.api_key = "Enter OpenAi api key here"


# Define a method to get responses from GPT-3
def get_response(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        return response.choices[0].text.strip()

    except openai.error.APIError as e:
        st.error(f"OpenAI API Error occurred: {e}")
        return "I'm sorry, something went wrong."

    except Exception as e:
        st.error(f"Error occurred: {e}")
        return "I'm sorry, something went wrong."


# Define the Streamlit app
def chatbot():
    st.title("Welcome to the Chatbot")
    st.subheader("Please enter your message below:")

    # Create an input box to get user's text input
    user_input = st.text_input("", "")

    if len(user_input) > 0:
        # Format user's input for prompt
        formatted_input = f"User: {user_input}\nAI:"

        # Get AI response
        response = get_response(formatted_input)

        # Display AI response
        st.text_area("AI:", value=response, height=200, max_chars=None, key=None)

    else:
        # Display initial prompt message
        response = get_response("Hello! How may I assist you today?\nAI:")
        st.text_area("AI:", value=response, height=200, max_chars=None, key=None)


# Run the app
if __name__ == "__main__":
    try:
        # Make an initial call to the API to check the API connection and load the authentication credentials
        openai.Completion.create(
            engine="text-davinci-002",
            prompt="",
            temperature=0,
            max_tokens=0,
            top_p=0,
            frequency_penalty=0,
            presence_penalty=0,
        )

        chatbot()

    except openai.error.AuthenticationError:
        st.error("Please enter your OpenAI API key in the code.")

    except openai.error.APIError as e:
        st.error(f"OpenAI API Error occurred: {e}")

    except Exception as e:
        st.error(f"Error occurred: {e}")

        # Display error message
        st.text_area("AI:", value="I'm sorry, something went wrong.", height=200, max_chars=None, key=None)