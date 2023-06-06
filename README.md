# **Paper2Post**
![Screenshot from 2023-06-06 20-56-55](https://github.com/SalehAhmad1/Paper2Post/assets/74538266/a00dcc8e-dbc3-4da4-84a1-f31444bdbb1f)


Paper2Post is a GitHub repository that allows you to get top research papers from [Papers with Code](https://paperswithcode.com/), select the highest-rated paper, summarize its abstract using the 
OpenAI API, and send a personalized prompt-based message to chosen WhatsApp contacts. The integration of Langchain in Paper2Post has significantly improved its functionality, seamlessly combining the power of prompting and OpenAI GPT. This repository is inspired by [LinkedInGPT](https://github.com/FrancescoSaverioZuppichini/LinkedInGPT)
which served as the basis for building this project. 👏

## **Table of Contents**
1. Introduction
2. Features
3. Installation
4. Usage
5. Contribution
6. Acknowledgements

### **Introduction** 📜

Computer science research papers often contain valuable insights and knowledge, but finding and summarizing relevant papers can be time-consuming. 
Paper2Post utilizes LangChain and automates this process by scraping the top research papers from [Papers with Code](https://paperswithcode.com/), selecting the highest-rated paper, and summarizing its abstract using the OpenAI API. Additionally, it provides the functionality to send personalized prompt-based messages to chosen WhatsApp contacts, allowing you to share the summarized information conveniently. All of this has been 💡

**Features** 🚀

1. Scrapes top research papers from "Papers with Code" 📚
2. Selects the highest rated paper based on user preferences 🏆
3. Utilizes the OpenAI API to summarize the abstract of the chosen paper 🧪
4. Generates personalized prompt-based messages to be sent via WhatsApp ✉️
5. Integrates with WhatsApp to send messages to chosen contacts 📲

### **Installation** 💻

To use Paper2Post, follow these steps:
Clone the repository:
```
git clone https://github.com/SalehAhmad1/Paper2Post.git
```
Navigate to the project directory:
```
cd Paper2Post
```
Install the required dependencies:
```
pip install -r requirements
```

### **Usage** 💻
- Create a **Credentials.env** file in the main directory and write your OpenAI API in it.
- Create a **PhoneNumbers.txt** in the main directory and write all the receiving whatsapp numbers (with zipcode) there.
Run the application:
```
python Main.py
```

### **Contribution** 🤝

Contributions to Paper2Post are welcome and appreciated. If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository. If you would like to contribute directly, feel free to fork the repository and submit a pull request.

### **Acknowledgements** 🙌

I would like to express my sincere gratitude to [Francesco Saverio Zuppichini](https://github.com/FrancescoSaverioZuppichini) for creating the LinkedInGPT repository, which served as the foundation for this project. His work and dedication have been instrumental in developing Paper2Post. Special thanks to the OpenAI team for providing the powerful language models and APIs that make this project possible. 👍
