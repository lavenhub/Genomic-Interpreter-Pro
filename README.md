# 🧬 Genomic Interpreter Pro

### *Bridging the Gap Between Genetic Data and Clinical Action*

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![BioPython](https://img.shields.io/badge/BioPython-FFCB42?style=for-the-badge&logo=python&logoColor=black)

---

## 📖 Project Overview
Raw genomic data is often a "black box" for clinicians. **Genomic Interpreter Pro** is an end-to-end diagnostic suite designed to translate 1D DNA sequences into 3D structural impacts and actionable medical reports. 

By integrating **Explainable AI (XAI)** and **Structural Biology**, this tool allows researchers and doctors to simulate mutations and instantly see their effect on protein folding, drug metabolism, and family hereditary risk.

---

## ✨ Key Features

### 🧪 1. Interactive Mutation Lab
* **Real-time Simulation:** Modify nucleotides at specific positions and observe the downstream effects on the protein sequence.
* **Validation Layer:** Robust input cleaning that strips non-genomic characters (numbers/spaces) and ensures data integrity.

### 🧊 2. 3D Molecular Visualization
* **Structural Insight:** Powered by `py3Dmol`, the app renders 3D protein folds to identify if a mutation occurs in a critical region like an alpha-helix or beta-sheet.
* **Dynamic UI:** Interactive rotation and surface rendering to assess "pocket" stability.



### 📋 3. Clinical Diagnostic Suite
* **Pathogenicity Scoring:** Automated classification of variants into **Benign**, **Pathogenic**, or **VUS** (Variant of Uncertain Significance) based on ACMG-inspired logic.
* **Pharmacogenomics (PGx):** Predicts patient response to high-risk drugs like **Warfarin** and **Statins** based on genetic markers.

### 🌳 4. Hereditary Risk & Pedigree Mapper
* **Cascade Testing:** Automatically identifies inheritance patterns (e.g., Autosomal Dominant) and generates a screening priority list for family members.



### 🔍 5. Explainable AI (XAI)
* **Attention Mapping:** Uses a bar-chart visualization to show which nucleotides the AI model prioritizes when calculating risk scores, ensuring the "black box" of AI is transparent.

---

## 🛠️ Technical Stack
* **Frontend:** [Streamlit](https://streamlit.io/) (Data-centric Web Framework)
* **Bioinformatics:** [BioPython](https://biopython.org/) (Sequence Analysis)
* **3D Rendering:** [stmol](https://github.com/napoles-uach/stmol) & [py3Dmol](https://3dmol.csb.pitt.edu/)
* **Data Visualization:** [Plotly Express](https://plotly.com/python/) & [Pandas](https://pandas.pydata.org/)

---

## ⚙️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/genomic-interpreter-pro.git](https://github.com/YOUR_USERNAME/genomic-interpreter-pro.git)
    cd genomic-interpreter-pro
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Application:**
    ```bash
    streamlit run app.py
    ```

---

## 🧠 Technical Challenges & Solutions
* **The 3D Rendering Hurdle:** Overcame WebGL rendering issues in Streamlit by implementing `stmol` with `ipython_genutils` to bridge the IPython-to-Web communication gap.
* **Data Consistency:** Built a custom regex-based validation engine to translate messy user-provided DNA strings into clean biological objects.

---

## 🔮 Future Roadmap
- [ ] **AlphaFold Integration:** Connect to the AlphaFold API for dynamic 3D folding of *any* custom sequence.
- [ ] **ClinVar API:** Live fetching of peer-reviewed clinical data for identified variants.
- [ ] **LLM Counseling:** Integration of a RAG-based LLM to explain results to patients in simple language.

---

## 🤝 Contact & Contributors
* **Lavish** - [www.linkedin.com/in/lavish-patil-283734325]
* **Hackathon Team:** [winn3rz]
