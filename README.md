# API-INTEGRATION-AND-DATA-VISUALIZATION

COMPANY: CODTECH IT SOLUTIONS

NAME: TANVI BEJADI

INTERN ID: CT04DH2184

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

Project Overview:
As part of the internship program offered by CodTech, I completed a technical project titled "API Integration and Data Visualization using Python". The objective was to retrieve real-time data from a public API, process it using Python, and generate meaningful visualizations using standard data analysis libraries. This project helped me develop hands-on experience with live data, scripting logic, visualization, and professional reporting.

Editor and Platform Used:
The project was developed using Visual Studio Code (VS Code) on a Windows 10 system. VS Code was chosen for its Python-friendly environment, integrated terminal, and support for extensions. Output files (images and reports) were saved locally and viewed using default system applications. The optional HTML dashboard was viewed in the Google Chrome browser. All commands were executed through the Windows Command Prompt.

Working Procedure:
API Selection and Data Fetching:
I used the COVID-19 public API (https://disease.sh/v3/covid-19/countries) to fetch country-wise live pandemic data. Using the requests library in Python, I sent an HTTP GET request and received a JSON response.

Data Cleaning and Structuring:
The raw JSON was converted into a structured Pandas DataFrame. I selected relevant fields like country, cases, deaths, recovered, and active to work with. The data was then filtered to extract the top 10 countries by total cases.

Data Visualization:
I used Matplotlib and Seaborn to create:

A bar chart displaying the top 10 countries with the highest number of COVID-19 cases.

A scatter plot comparing total deaths vs. recoveries.

These plots were saved as .png image files using plt.savefig().

PDF Report Generation:
Using the reportlab library, I created a professionally formatted PDF report. It included a title, data source, inserted charts, and a brief summary. The file was saved as Covid_Report.pdf.

HTML Dashboard Creation:
I designed a basic HTML dashboard to display both charts within a simple, clean web layout. This provides a browser-friendly view of the visualizations.

Packaging for Submission:
All essential files (.py, .png, .pdf, and .html) were bundled into a ZIP file using Python's zipfile module, making it ready for submission.

Tools and Libraries Used:
Python 3.x

requests – API communication

pandas – Data manipulation

matplotlib, seaborn – Data visualization

reportlab – PDF report generation

HTML/CSS – Web dashboard

zipfile – Packaging

Applications and Relevance:
This workflow is highly applicable in domains like:

Public health monitoring

Financial dashboards

Weather/climate tracking

Business intelligence and reporting

Organizations can use similar tools to automatically pull, analyze, and present live data for decision-making.

Conclusion:
The project effectively integrates API access, data manipulation, visualization, and reporting using Python. It reflects a real-world data pipeline and builds practical skills in scripting, automation, and data presentation. It also meets all requirements of the CodTech internship module and is ready for submission.

#OUTPUT

<img width="1400" height="800" alt="Image" src="https://github.com/user-attachments/assets/d6c02229-ffd7-4bce-978d-d90fb325c781" />

<img width="1400" height="800" alt="Image" src="https://github.com/user-attachments/assets/c3320939-b877-4a73-80ab-b11ef7dc8122" />
