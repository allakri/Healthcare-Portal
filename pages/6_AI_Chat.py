import streamlit as st
from PyPDF2 import PdfReader
import pandas as pd
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS  # Updated import
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def load_csv_data(folder_path):
    """Load all CSV files from the specified folder and return the combined text."""
    text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".csv"):
            file_path = os.path.join(folder_path, filename)
            df = pd.read_csv(file_path)
            # Convert the data to a single text block
            text += df.to_string(index=False)
    return text

def get_text_chunks(text):
    """Split text into manageable chunks for embedding."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return text_splitter.split_text(text)

def get_vector_store(text_chunks):
    """Embed text chunks and save them into a FAISS vector store."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")
    return vector_store

def get_conversational_chain():
    """Set up a conversational chain with prompt for health and general advice."""
    prompt_template = """
    Answer the question using information from the provided context. If the answer is not available in the context, 
    respond with general advice on health, food, or fitness. Be as accurate as possible.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    return load_qa_chain(model, chain_type="stuff", prompt=prompt)

def user_input(user_question):
    """Handle user input, retrieve relevant documents, and respond."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = vector_store.similarity_search(user_question)

    chain = get_conversational_chain()
    response = chain({"input_documents": docs, "question": user_question}, return_only_outputs=True)
    st.write("Reply: ", response["output_text"])

def main():
    st.set_page_config("Health Chatbot")
    st.header("Health Prediction and Advice Chatbot 🤖")

    user_question = st.text_input("Ask a question about health, body functions, or fitness")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Info")
        if st.button("Initialize Data"):
            with st.spinner("Loading and processing health data..."):
                # Load and process all CSV data from a predefined directory
                raw_text = load_csv_data("data/csv_files")
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Data loaded and processed.")

if __name__ == "__main__":
    main()
