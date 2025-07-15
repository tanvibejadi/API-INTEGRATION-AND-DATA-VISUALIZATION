
# covid_dashboard.py

import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet

# Step 1: Fetch Data from API
print("Fetching data from COVID-19 API...")
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
else:
    print("Failed to retrieve data from API. Exiting.")
    exit()

# Step 2: Create DataFrame
df = pd.DataFrame(data)
df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered', 'active']]

# Step 3: Select Top 10 Countries by Total Cases
top_10 = df.sort_values(by='cases', ascending=False).head(10)

# Step 4: Save Visualizations

# Plot 1: Barplot of Total Cases
plt.figure(figsize=(14, 8))
sns.barplot(data=top_10, x='cases', y='country', palette='Reds_r')
plt.title('Top 10 Countries by Total COVID-19 Cases')
plt.xlabel('Total Cases')
plt.ylabel('Country')
plt.tight_layout()
plt.savefig("top10_cases.png")
plt.close()

# Plot 2: Scatterplot of Deaths vs Recovered
plt.figure(figsize=(14, 8))
sns.scatterplot(data=top_10, x='deaths', y='recovered', hue='country', s=100, palette='viridis')
plt.title('Deaths vs Recovered (Top 10 Countries)')
plt.xlabel('Total Deaths')
plt.ylabel('Total Recovered')
plt.grid(True)
plt.tight_layout()
plt.savefig("deaths_vs_recovered.png")
plt.close()

print("Charts saved as images.")

# Step 5: Generate PDF Report
print("Generating PDF report...")
doc = SimpleDocTemplate("Covid_Report.pdf")
styles = getSampleStyleSheet()
elements = []

elements.append(Paragraph("COVID-19 Data Visualization Report", styles['Title']))
elements.append(Spacer(1, 12))
elements.append(Paragraph("Internship Project – CodTech", styles['Heading2']))
elements.append(Spacer(1, 12))
elements.append(Paragraph("API Used: https://disease.sh/v3/covid-19/countries", styles['Normal']))
elements.append(Spacer(1, 24))
elements.append(Paragraph("Figure 1: Top 10 Countries by Total Cases", styles['Heading3']))
elements.append(Image("top10_cases.png", width=500, height=300))
elements.append(Spacer(1, 24))
elements.append(Paragraph("Figure 2: Deaths vs Recovered", styles['Heading3']))
elements.append(Image("deaths_vs_recovered.png", width=500, height=300))
elements.append(Spacer(1, 24))
elements.append(Paragraph("Summary: The above figures highlight the most affected countries, recovery trends, and fatality relationships.", styles['Normal']))

doc.build(elements)
print("PDF Report generated: Covid_Report.pdf")
