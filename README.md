
# Lumi Python PDF Scrapper


Lumi PDF Scrapper is a Python project designed to extract data from PDF files, particularly related to energy invoices. The project utilizes PyPDF2 for PDF parsing and SQLAlchemy for interacting with a PostgreSQL database. By extracting relevant information from PDFs, the data is structured and stored in a PostgreSQL database for further analysis and reporting.

# Features


- **PDF Data Extraction:**
    Utilizes PyPDF2 to extract data from energy invoices in PDF format.

- **Database Integration:** 
    Uses SQLAlchemy to interact with a PostgreSQL database for efficient data storage.

- **Structured Data:** 
    Organizes extracted data into a structured format, facilitating easy querying and reporting.

- **Modular Design:** 
    Follows a modular design pattern, allowing for easy extension and maintenance.
## Setup Instructions


**Dependencies Installation:** 

    pip install -r requirements.txt

**Database Configuration:**

Set up your PostgreSQL database and provide the connection details in the project configuration.

You can use the same configuration as the project

Open a terminal and run the following command to start a PostgreSQL container.

    docker run -d --name postgresLumi -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=lumi -p 5432:5432 postgres:latest

This command will create a new PostgreSQL container with the specified user, password, and database. The container will be accessible on port 5432.    

- **Run the Project:**

Execute the main script to start extracting PDF data and populating the database.

    python src/__main__.py
