import glob
import pandas as pd
import xml.etree.ElementTree as ET
# import seaborn as sns
# import matplotlib.pyplot as plt


# Get paths for all XML files in a directory
xml_files = glob.glob(r"D:\kiran\medicalQA_chatbot\dataset\**\*.xml", recursive=True)
# print(xml_files)
data = []

for file in xml_files:
    # Parse the XML file
    tree = ET.parse(file)
    root = tree.getroot()
    # print(root[2])

    # Extract relevant information based on XML structure
    # Here, assume each XML file has 'question' and 'answer' elements
    for qa_pair in root[2].findall("QAPair"):
        question = qa_pair.find("Question").text
        # print(question)
        answer = qa_pair.find("Answer").text
        # print(answer)
        data.append({"question": question, "answer": answer})

# Convert to DataFrame for further processing or analysis
df = pd.DataFrame(data)
# print(df.head(20))
# print(df.isnull)
# print(df.info)
# null_counts = df.isnull().sum()
# print(null_counts)
# print(df.info())
# rows_with_nulls = df[df.isnull().any(axis=1)]
# print(rows_with_nulls)

# sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
# plt.show()
