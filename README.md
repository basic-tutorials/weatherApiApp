# Research Proposal Generator

Transform research ideas into professionally formatted proposals with proper academic structure, saving students and researchers 10+ hours of formatting and structuring work.

## 🎯 Purpose

Creating a research proposal is time-consuming and requires specific formatting knowledge. This widget automates the generation of professionally formatted research proposals, allowing researchers to focus on their ideas rather than formatting.

## ✨ Features

- **AI-Enhanced Content**: Generates executive summaries, literature review frameworks, and expanded methodology sections
- **Field-Specific Templates**: Customized formatting for Sciences, Social Sciences, Humanities, Engineering, Medical, and Business
- **Professional PDF Output**: Publication-ready proposals with proper academic structure
- **Timeline Generation**: Automatic project timeline with Gantt chart visualization
- **Budget Breakdown**: Professional budget tables (if budget provided)
- **Multiple Citation Formats**: Support for APA, MLA, Chicago, IEEE, Vancouver
- **Comprehensive Sections**: All 9 standard proposal sections included

## 📥 Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| research_title | Text Area | Yes | Title of your research project |
| research_question | Text Area | Yes | Main research question or problem statement |
| methodology | Text Area | Yes | Brief description of your research methodology |
| expected_outcomes | Text Area | Yes | Expected results and significance |
| researcher_name | Text Field | Yes | Your full name |
| institution | Text Field | No | Your institution/university |
| field_of_study | Select | No | Field: Sciences, Social Sciences, Humanities, Engineering, Medical, Business |
| duration_months | Number | No | Project duration in months (1-60, default: 12) |
| budget | Text Field | No | Estimated budget (e.g., "50000") |
| proposal_type | Radio | No | Grant Application, Thesis Proposal, Research Project, or Conference Abstract |
| references | Text Area | No | Bibliography/references (optional) |
| ai_provider | Radio | No | OpenAI or Anthropic (default: Anthropic) |
| citation_format | Select | No | APA, MLA, Chicago, IEEE, Vancouver (default: APA) |

## 📤 Outputs

| File | Format | Description |
|------|--------|-------------|
| research_proposal.pdf | PDF | Complete professional research proposal (15+ pages) |
| proposal_data.json | JSON | Structured proposal data for reference |
| summary.txt | Text | Generation summary and statistics |

## 🚀 Usage

1. **Enter Research Details**: Fill in your research title, question, methodology, and expected outcomes
2. **Add Personal Info**: Provide your name and institution
3. **Select Options**: Choose field of study, proposal type, duration, and citation format
4. **Optional Enhancements**: Add budget, references, and select AI provider
5. **Generate**: Click run to create your professional proposal
6. **Download**: Receive a complete, formatted PDF proposal

## 📋 Example

**Input:**
```
Title: "Machine Learning Applications in Climate Change Prediction"
Research Question: "How can ensemble machine learning models improve long-term climate prediction accuracy?"
Methodology: "Comparative analysis of neural networks, random forests, and gradient boosting models using historical climate data"
Expected Outcomes: "Development of hybrid model with 15-20% improved accuracy over current methods"
Field: Sciences
Duration: 18 months
Proposal Type: Grant Application
```

**Output:**
- 18-page professional PDF with:
  - Cover page
  - Table of contents
  - Executive summary (AI-generated)
  - Introduction & background
  - Literature review framework
  - Research objectives
  - Expanded methodology
  - Expected outcomes
  - 18-month timeline with Gantt chart
  - Budget breakdown
  - References

## ⚙️ Requirements

### Python Dependencies
- reportlab==4.0.7 (PDF generation)
- PyPDF2==3.0.1 (PDF utilities)
- openai==1.12.0 (OpenAI API)
- anthropic==0.18.1 (Anthropic API)
- python-dateutil==2.8.2 (Date utilities)

### API Keys (Optional but Recommended)
- **OPENAI_API_KEY**: For OpenAI GPT-4 content generation
- **ANTHROPIC_API_KEY**: For Anthropic Claude content generation

**Note**: If no API key is provided, the widget will use template-based generation (still produces professional output, but without AI enhancement).

## 🔒 Privacy

- All processing is done server-side
- No data is stored after generation
- API keys are used only for the current generation
- Research content is not retained

## ⚠️ Limitations

- Maximum duration: 60 months
- PDF size may vary based on content (typically 15-25 pages)
- AI generation requires valid API key (falls back to templates without)
- References must be pre-formatted (not automatically formatted)
- Budget breakdown uses standard allocation percentages

## 📚 Output Structure

### 1. Cover Page
- Title (centered, bold)
- Proposal type
- Researcher name and institution
- Field of study
- Date

### 2. Table of Contents
Auto-generated navigation

### 3. Executive Summary (200-250 words)
AI-generated or template-based summary highlighting significance and innovation

### 4. Introduction & Background
- Problem statement
- Research gap
- Significance

### 5. Literature Review
AI-generated framework or template-based review

### 6. Research Questions & Objectives
- Primary objective
- 3-4 sub-objectives
- Hypotheses (if applicable)

### 7. Methodology
Expanded methodology with:
- Research design
- Data collection methods
- Analysis approach
- Validity considerations

### 8. Expected Outcomes
- Anticipated findings
- Potential impact
- Contribution to field

### 9. Timeline
Professional Gantt chart table with phases and milestones

### 10. Budget Breakdown (Optional)
Professional budget table with categories and percentages

### 11. References (Optional)
Formatted bibliography

## 🎨 Field-Specific Customization

### Sciences
- Emphasis on empirical methods
- IMRAD structure
- APA citation style
- Includes hypothesis testing

### Social Sciences
- Mixed methods focus
- Traditional structure
- APA citation style
- Ethics considerations

### Humanities
- Interpretive approach
- Narrative structure
- MLA citation style
- Critical analysis focus

### Engineering
- Applied/technical emphasis
- Technical structure
- IEEE citation style
- Performance metrics

### Medical
- Clinical focus
- Clinical trial structure
- Vancouver citation style
- Ethics approval section

### Business
- Practical applications
- Executive structure
- APA citation style
- ROI and stakeholder analysis

## 💡 Tips for Best Results

1. **Be Specific**: Provide detailed methodology and outcomes for better AI enhancement
2. **Use Full Sentences**: Write in complete sentences rather than bullet points
3. **Include Context**: Mention why your research is significant
4. **Add References**: Pre-format your references in your chosen citation style
5. **Provide API Key**: For best results, provide an API key for AI enhancement
6. **Choose Correct Field**: Select the appropriate field for proper formatting
7. **Realistic Timeline**: Choose a duration that matches your project scope

## 🛠️ Troubleshooting

### Error: Required field missing
- Ensure all required fields are filled (title, question, methodology, outcomes, name)

### AI generation not working
- Check that API key is provided as environment variable
- Widget will automatically fall back to template-based generation

### PDF formatting issues
- Content is automatically formatted based on field of study
- Very long text may require multiple pages (this is normal)

### Budget not appearing
- Ensure budget is entered as a number (e.g., "50000" not "$50,000")
- Budget section only appears if budget is provided

## 📊 Technical Details

### Processing Time
- Typically 15-30 seconds
- AI-enhanced: 30-45 seconds
- Depends on content length and API response time

### PDF Specifications
- Page size: Letter (8.5" × 11")
- Margins: 1 inch all sides
- Font: Helvetica family
- Line spacing: 1.5
- Professional academic formatting

### AI Models Used
- OpenAI: GPT-4
- Anthropic: Claude 3.5 Sonnet
- Temperature: 0.7 (balanced creativity and accuracy)

## 📝 License

This widget is provided as-is for research and academic purposes.

## 🤝 Support

For issues or questions:
1. Check that all required fields are filled
2. Verify API keys if using AI features
3. Review error.txt in output folder for specific error messages

## 🚀 Future Enhancements

- Multiple language support
- DOCX export option
- Custom template upload
- Collaboration features
- Advanced Gantt chart visualization
- Citation manager integration

---

**From idea to fundable proposal in 60 seconds.**

Stop struggling with formatting—focus on your research.
