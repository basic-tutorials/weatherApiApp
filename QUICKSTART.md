# Quick Start Guide

Get your Research Proposal Generator widget running in 5 minutes.

## 🚀 Local Testing (Optional)

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run Test Script

```bash
./test_local.sh
```

OR set variables manually:

```bash
export research_title="Your Research Title"
export research_question="Your research question?"
export methodology="Your methodology"
export expected_outcomes="Expected outcomes"
export researcher_name="Your Name"
python run.py
```

### 3. Check Output

```bash
ls output/
# Should see: research_proposal.pdf, proposal_data.json, summary.txt
```

## 📤 Deploy to Abyss

### Quick Deploy Checklist

1. **Upload Files:**
   - run.py
   - requirements.txt
   - utils/ (entire folder)
   - output/.gitkeep

2. **Configure 13 Fields** (see ABYSS_INTERFACE_CONFIG.md)

3. **Test with Sample Data:**
   - Title: "Machine Learning in Climate Prediction"
   - Question: "How can ML improve climate models?"
   - Methodology: "Comparative analysis of ML algorithms"
   - Outcomes: "15-20% improved accuracy"
   - Name: "Dr. Jane Smith"

4. **Verify Output:**
   - PDF generates (15+ pages)
   - All sections present
   - Professional formatting

5. **Deploy!**

## 📁 File Structure

```
research_proposal_generator/
├── run.py                    # ✅ Main entry point
├── requirements.txt          # ✅ Dependencies
├── output/                   # ✅ Output folder
│   └── .gitkeep
├── utils/                    # ✅ Core modules
│   ├── __init__.py
│   ├── ai_generator.py
│   ├── pdf_builder.py
│   ├── templates.py
│   └── timeline.py
├── README.md                 # Documentation
├── ABYSS_INTERFACE_CONFIG.md # Field configs
├── DEPLOYMENT_GUIDE.md       # Full deploy guide
└── test_local.sh            # Test script
```

## 🎯 Minimum Required Fields

For widget to work, user must provide:
1. research_title
2. research_question
3. methodology
4. expected_outcomes
5. researcher_name

All others are optional with defaults.

## 🔑 API Keys (Optional)

For AI enhancement, add:
```
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
```

Without keys: Uses template-based generation (still professional!)

## ⚡ That's It!

You're ready to generate professional research proposals!

See DEPLOYMENT_GUIDE.md for detailed instructions.
