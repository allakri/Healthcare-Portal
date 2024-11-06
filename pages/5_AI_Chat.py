import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import glob

# Initialize session state
if 'db_initialized' not in st.session_state:
    st.session_state.db_initialized = False

# Load and configure API
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
if api_key:
    genai.configure(api_key=api_key)
else:
    st.error("Please set up your Google API key in the .env file")
    st.stop()

# Define paths for data folders
DATA_DIR = "data"
PDF_DIR = os.path.join(DATA_DIR, "pdfs")
CSV_DIR = os.path.join(DATA_DIR, "csvs")
DB_DIR = os.path.join(DATA_DIR, "database")

# Create directories if they don't exist
for dir_path in [PDF_DIR, CSV_DIR, DB_DIR]:
    os.makedirs(dir_path, exist_ok=True)

def get_pdf_text():
    text = ""
    pdf_files = glob.glob(os.path.join(PDF_DIR, "*.pdf"))
    for pdf_path in pdf_files:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PdfReader(file)
            for page in pdf_reader.pages:
                text += page.extract_text()
    return text

def get_csv_text():
    text = ""
    csv_files = glob.glob(os.path.join(CSV_DIR, "*.csv"))
    for csv_path in csv_files:
        df = pd.read_csv(csv_path)
        text += f"\nDataset from {os.path.basename(csv_path)}:\n"
        text += f"Columns: {', '.join(df.columns)}\n"
        text += df.to_string() + "\n\n"
    return text

def initialize_database():
    """Initialize the vector database from documents in the data folders"""
    try:
        # Get text from all documents
        pdf_text = get_pdf_text()
        csv_text = get_csv_text()
        combined_text = pdf_text + "\n" + csv_text

        if not combined_text.strip():
            st.warning("No documents found in the data folders.")
            return False

        # Create text chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=10000,
            chunk_overlap=1000
        )
        text_chunks = text_splitter.split_text(combined_text)

        # Create and save vector store
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
        vector_store.save_local(os.path.join(DB_DIR, "faiss_index"))

        return True

    except Exception as e:
        st.error(f"Error initializing database: {str(e)}")
        return False

def get_conversational_chain():
    prompt_template = """
    You are a helpful AI assistant that provides information based on the healthcare documents and data available.
    Answer the question as accurately as possible using the provided context. If the information isn't available
    in the context, please say "I don't have enough information to answer this question accurately."
    
    Context: {context}
    Question: {question}
    
    Answer:
    """

    try:
        model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
        prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
        return load_qa_chain(model, chain_type="stuff", prompt=prompt)
    except Exception as e:
        st.error(f"Error creating conversation chain: {str(e)}")
        return None

def process_question(user_question):
    try:
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        vector_store = FAISS.load_local(
            os.path.join(DB_DIR, "faiss_index"),
            embeddings,
            allow_dangerous_deserialization=True
        )
        
        docs = vector_store.similarity_search(user_question)
        chain = get_conversational_chain()
        
        if chain:
            response = chain(
                {"input_documents": docs, "question": user_question},
                return_only_outputs=True
            )
            st.markdown("### Response:")
            st.write(response["output_text"])
    except Exception as e:
        st.error(f"Error processing question: {str(e)}")

def main():
    st.set_page_config(page_title="Healthcare AI Assistant", layout="wide")
    
    # Custom CSS
    st.markdown("""
        <style>
        .main-header {
            color: #1e4b7a;
            text-align: center;
            padding: 1rem;
            background: linear-gradient(to right, #f0f9ff, #e6f3ff);
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        .chat-container {
            background-color: #f8fafc;
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 class='main-header'>Healthcare AI Assistant</h1>", unsafe_allow_html=True)

    # Initialize database if not already done
    if not st.session_state.db_initialized:
        with st.spinner("Initializing database from documents..."):
            if initialize_database():
                st.session_state.db_initialized = True
                st.success("Database initialized successfully!")
            else:
                st.warning("Please add documents to the data folders and restart the application.")
                st.stop()

    # Main chat interface
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    st.subheader("Ask Health-Related Questions")
    user_question = st.text_input(
        "What would you like to know?",
        placeholder="Example: What are the common symptoms of diabetes?"
    )

    if user_question:
        process_question(user_question)
    
    st.markdown("</div>", unsafe_allow_html=True)

    # Add information about data locations
    with st.expander("📁 Data Folder Information"):
        st.write(f"""
        - PDF documents should be placed in: `{PDF_DIR}`
        - CSV files should be placed in: `{CSV_DIR}`
        - Database is stored in: `{DB_DIR}`
        """)

if __name__ == "__main__":
    main()
