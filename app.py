# ---------------------------------------------------------------
# Average Calculator - a beginner-friendly Streamlit app
# ---------------------------------------------------------------

# SECTION 1: Import the library
# Streamlit turns Python code into a web page. "st" is a short nickname.
import streamlit as st


# SECTION 2: Helper function that turns the user's text into numbers
def parse_numbers(text):
    """
    Takes the text typed by the user (like "10, 20 30") and returns
    two things:
      - a list of valid numbers
      - a list of any "words" that were NOT valid numbers
    """
    # Replace commas with spaces so users can separate numbers with
    # commas, spaces, or new lines. split() then breaks the text into pieces.
    pieces = text.replace(",", " ").split()

    numbers = []   # will hold the valid numbers
    invalid = []   # will hold anything that isn't a number

    for piece in pieces:
        try:
            # float() converts text like "3.5" into the number 3.5
            numbers.append(float(piece))
        except ValueError:
            # If float() fails, the piece wasn't a number
            invalid.append(piece)

    return numbers, invalid


# SECTION 3: Page title and instructions
st.title("🧮 Average Calculator")

st.write("Find the average (mean) of any list of numbers.")

st.subheader("How to use this app")
st.markdown(
    """
1. Type your numbers in the box below.
2. Separate them with **commas**, **spaces**, or **new lines**
   (for example: `10, 20, 30` or `4.5 7 9`).
3. Click the **Calculate Average** button.
4. Your result will appear underneath.
"""
)

# SECTION 4: Input box
# text_area gives the user a large box to type in.
user_input = st.text_area(
    "Enter your numbers here:",
    placeholder="Example: 85, 90, 78, 92",
)

# SECTION 5: Button and calculation
# st.button returns True only at the moment the user clicks it.
if st.button("Calculate Average"):

    numbers, invalid = parse_numbers(user_input)

    # Case 1: The user typed something that isn't a number
    if invalid:
        st.error(
            "These entries are not valid numbers: "
            + ", ".join(invalid)
            + ". Please fix them and try again."
        )

    # Case 2: The box was empty (no numbers at all)
    elif len(numbers) == 0:
        st.warning("Please enter at least one number.")

    # Case 3: Everything is fine, so calculate the average
    else:
        total = sum(numbers)        # add all the numbers together
        count = len(numbers)        # how many numbers there are
        average = total / count     # average = sum divided by count

        # SECTION 6: Show the result in a clean format
        st.success("Calculation complete!")

        # st.metric shows a big, clean number
        st.metric(label="Average", value=f"{average:,.2f}")

        # Show the details so the user can double-check the work
        st.write(f"**Numbers entered:** {count}")
        st.write(f"**Sum:** {total:,.2f}")
        st.write(f"**Formula:** {total:,.2f} ÷ {count} = {average:,.2f}")
