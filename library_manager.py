import streamlit as st
from streamlit_lottie import st_lottie
import requests
import random

# Function to load Lottie JSON from a URL
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Set up the page config
st.set_page_config(page_title="Library Manager", page_icon=":books:", layout="wide")

# Custom CSS with color change animations
st.markdown("""
    <style>
        /* Animation for background color change */
        @keyframes backgroundColorChange {
            0% {background-color: #ff6347;}
            25% {background-color: #ffcc00;}
            50% {background-color: #32cd32;}
            75% {background-color: #00bfff;}
            100% {background-color: #ff6347;}
        }

        /* Background color animation on page change */
        .stApp {
            animation: backgroundColorChange 10s infinite;
        }

        /* Title and Header Color */
        h1 {
            color: #ff6347;  /* Bright Red */
        }

        .stHeader, .stSubheader {
            color: #32cd32;  /* Bright Green */
        }

        /* Sidebar style */
        .sidebar .sidebar-content {
            background-color: #ffebcd; /* Light Beige */
        }

        /* Button color */
        .stButton>button {
            background-color: #ff6347; /* Bright Red */
            color: white;
            border-radius: 5px;
            padding: 10px;
        }

        /* Hover effect for buttons */
        .stButton>button:hover {
            background-color: #ff4500;  /* Bright Orange-Red */
        }

        /* Text input and number input fields */
        .stTextInput>div>input, .stNumberInput>div>input {
            background-color: #ffffe0;  /* Light Yellow */
            border-radius: 5px;
            padding: 10px;
        }

    </style>
""", unsafe_allow_html=True)

# Title of the app
st.title("Welcome to the Library Manager!")

# Load Lottie animation for the landing page
lottie_url = "https://assets1.lottiefiles.com/packages/lf20_wf61twgm.json"  # Your Lottie animation URL
lottie_json = load_lottie_url(lottie_url)

if lottie_json:
    st_lottie(lottie_json, speed=1, width=600, height=600, key="landing_animation")

# Introductory text
st.header("Manage Your Library Effectively")
st.write("""
    This is a simple Library Manager app where you can manage your book collection.
    Use the features below to add, view, and remove books from the library.
""")

# Navigation Menu (Sidebar)
st.sidebar.title("Navigation")
options = ["Home", "Add Book", "View Books", "Remove Book", "Search Books"]
choice = st.sidebar.radio("Go to", options)

# Implementing different sections based on sidebar choice
if choice == "Home":
    st.subheader("Welcome to the Library Manager")
    st.write("""
        This application allows you to manage a collection of books.
        You can add new books, remove them, and search through the existing collection.
    """)
    st.write("Explore the other sections using the sidebar.")

elif choice == "Add Book":
    st.subheader("Add a New Book")
    book_title = st.text_input("Book Title")
    author_name = st.text_input("Author Name")
    
    # Updated Genre Input with easy words in brackets
    genre = st.text_input("Genre (e.g., Fiction, Mystery, Romance, Fantasy, Non-fiction, Science Fiction, Biography)")

    year = st.number_input("Year of Publication", min_value=1900, max_value=2100, value=2023)

    if st.button("Add Book"):
        if book_title and author_name and genre and year:
            # Add book logic (e.g., store in a database or list)
            st.success(f"Book '{book_title}' by {author_name} added successfully!")
        else:
            st.warning("Please fill in all the fields!")

elif choice == "View Books":
    st.subheader("All Books in the Library")
    # Example list of books (this could be fetched from a database or a file)
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "year": 1925},
        {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "year": 1949},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year": 1960},
    ]

    # Display books in a table format
    st.write("Here are the books in the library:")
    for book in books:
        st.write(f"**{book['title']}** by {book['author']} ({book['genre']}, {book['year']})")

elif choice == "Remove Book":
    st.subheader("Remove a Book from the Library")
    book_to_remove = st.text_input("Enter Book Title to Remove")

    if st.button("Remove Book"):
        # Logic to remove the book (example: from a list or database)
        if book_to_remove:
            st.success(f"Book '{book_to_remove}' has been removed successfully!")
        else:
            st.warning("Please enter a valid book title!")

elif choice == "Search Books":
    st.subheader("Search for a Book")
    search_query = st.text_input("Enter Book Title or Author")

    if st.button("Search"):
        # Example search logic (searching in a list or database)
        books = [
            {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Fiction", "year": 1925},
            {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "year": 1949},
            {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Fiction", "year": 1960},
        ]

        found_books = [book for book in books if search_query.lower() in book['title'].lower() or search_query.lower() in book['author'].lower()]

        if found_books:
            st.write("Found the following books:")
            for book in found_books:
                st.write(f"**{book['title']}** by {book['author']} ({book['genre']}, {book['year']})")
        else:
            st.write("No books found based on your search query.")
