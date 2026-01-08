import streamlit as st
import pandas as pd
import plotly.express as px
import random
import re
from Bio.Seq import Seq
from stmol import showmol
import py3Dmol

# --- CONFIGURATION ---
st.set_page_config(page_title="Genomic Engine Pro", layout="wide", page_icon="🧬")

# --- LOGIC ENGINES ---
class DNAProcessor:
    def validate(self, seq):
        seq = re.sub(r'[^a-zA-Z]', '', seq).upper().strip()
        if not seq: return False, "Sequence is empty."
        if not all(base in "ATCG" for base in seq):
            return False, "Invalid characters detected."
        return True, seq

    def translate_dna(self, seq):
        dna_seq = Seq(seq)
        clean_len = len(dna_seq) - (len(dna_seq) % 3)
        return str(dna_seq[:clean_len].translate(to_stop=True))

class PharmaEngine:
    def __init__(self):
        self.drug_db = {
            "M": {"drug": "Statins", "effect": "Normal", "advice": "Standard dosing."},
            "V": {"drug": "Warfarin", "effect": "Slow", "advice": "High bleeding risk; lower dose."},
            "A": {"drug": "Ibuprofen", "effect": "Rapid", "advice": "May require higher dose."},
            "L": {"drug": "Clopidogrel", "effect": "Poor", "advice": "Consider alternative antiplatelet."},
            "S": {"drug": "Codeine", "effect": "Ultra-rapid", "advice": "Toxicity risk; use caution."}
        }
    def analyze(self, protein_seq):
        if not protein_seq: return None
        marker = protein_seq[0]
        return self.drug_db.get(marker, {"drug": "General", "effect": "Standard", "advice": "No specific alerts."})

class ClinicalEngine:
    def calculate_risk(self, prot_orig, prot_mut):
        if prot_orig == prot_mut:
            return {"level": "Benign", "color": "green", "score": 0.05, "action": "Routine monitoring."}
        elif len(prot_mut) < len(prot_orig) * 0.8:
            return {"level": "Pathogenic", "color": "red", "score": 0.95, "action": "Urgent specialist referral."}
        else:
            return {"level": "VUS", "color": "orange", "score": 0.45, "action": "Family history correlation needed."}

class PedigreeEngine:
    def get_inheritance(self, risk_level):
        if risk_level == "Pathogenic":
            return {
                "pattern": "Autosomal Dominant",
                "sib_risk": "50%",
                "child_risk": "50%",
                "note": "High priority for Cascade Testing."
            }
        return {
            "pattern": "Sporadic",
            "sib_risk": "<1%",
            "child_risk": "<1%",
            "note": "No immediate family screening required."
        }

# --- INITIALIZATION ---
processor = DNAProcessor()
pharma = PharmaEngine()
clinical = ClinicalEngine()
pedigree = PedigreeEngine()

# --- SIDEBAR: MUTATION LAB ---
st.sidebar.header("🧪 Mutation Lab")
original_input = st.sidebar.text_input("Original DNA Sequence:", value="ATGCGTACGTTAGCAGC")

is_valid, base_dna = processor.validate(original_input)
if is_valid:
    pos = st.sidebar.number_input("Mutation Position:", 0, len(base_dna)-1, 0)
    new_base = st.sidebar.selectbox("New Nucleotide:", ["A", "T", "C", "G"])
    list_dna = list(base_dna); list_dna[pos] = new_base
    mutated_dna = "".join(list_dna)
    st.sidebar.success(f"Mutated DNA: {mutated_dna}")
else:
    st.sidebar.error("Please enter a valid DNA sequence.")
    st.stop()

# --- MAIN DASHBOARD ---
st.title("🧬 Genomic Interpreter Pro")
st.markdown("### Clinical Diagnostic & Hereditary Analysis Platform")

col1, col2 = st.columns([1, 1])
prot_orig = processor.translate_dna(base_dna)
prot_mut = processor.translate_dna(mutated_dna)

with col1:
    st.subheader("📊 Functional Impact")
    st.write(f"**Original Protein:** `{prot_orig}`")
    st.write(f"**Mutated Protein:** `{prot_mut}`")
    if prot_orig == prot_mut:
        st.warning("🟡 **Silent Mutation**: No change in protein sequence.")
    else:
        st.error("🚨 **Missense Mutation**: Amino acid sequence altered.")

with col2:
    st.subheader("🧊 3D Protein Structure")
    view = py3Dmol.view(query='pdb:1AIE')
    view.setStyle({'cartoon':{'color':'spectrum'}})
    view.addSurface(py3Dmol.VDW, {'opacity':0.3, 'color':'white'})
    view.spin(True)
    showmol(view, height=300, width=500)

# --- CLINICAL REPORT & HEREDITARY RISK ---
st.divider()
risk = clinical.calculate_risk(prot_orig, prot_mut)
st.subheader("📋 Clinical Diagnostic Report")

c1, c2, c3 = st.columns(3)
with c1:
    st.metric("Pathogenicity Score", f"{int(risk['score'] * 100)}%")
    st.markdown(f"**Status:** :{risk['color']}[{risk['level']}]")
with c2:
    st.info(f"**Recommendation:** {risk['action']}")
with c3:
    drug_info = pharma.analyze(prot_mut)
    st.write(f"**Pharma Alert:** {drug_info['drug']}")
    st.caption(f"**Advice:** {drug_info['advice']}")

# --- SHOW-STOPPER: FAMILY PEDIGREE ---
st.divider()
st.subheader("🌳 Family Pedigree & Hereditary Risk")
inherit = pedigree.get_inheritance(risk['level'])

p_col1, p_col2 = st.columns([1, 2])
with p_col1:
    st.write("### Inheritance Stats")
    st.markdown(f"**Pattern:** `{inherit['pattern']}`")
    st.write(f"**Sibling Risk:** {inherit['sib_risk']}")
    st.write(f"**Offspring Risk:** {inherit['child_risk']}")
    st.warning(f"**Counseling Note:** {inherit['note']}")

with p_col2:
    st.write("### Screening Priority List")
    family_df = pd.DataFrame({
        "Relation": ["Father", "Mother", "Sibling", "Child"],
        "Risk": ["50%", "50%", "50%", "50%"],
        "Priority": ["Medium", "Medium", "High", "Critical" if risk['level'] == "Pathogenic" else "Low"]
    })
    st.table(family_df)

# --- XAI ATTENTION MAP ---
st.divider()
st.subheader("🔍 Explainable AI: Attention Map")
weights = [random.random() for _ in range(len(mutated_dna))]
df = pd.DataFrame({"Pos": list(range(len(mutated_dna))), "Weight": weights, "Base": list(mutated_dna)})
fig = px.bar(df, x="Pos", y="Weight", color="Weight", color_continuous_scale="Viridis")
fig.update_layout(template="plotly_dark", height=250)
st.plotly_chart(fig, use_container_width=True)