# Abyss Widget Interface Configuration

**Simplified version - Only 7 essential fields**

---

## Widget Metadata

**Title:** Research Proposal Generator - Professional Academic Proposals in 60 Seconds

**Tags:**
1. research
2. academic
3. pdf
4. proposal
5. education

**Description:**
Transform research ideas into professionally formatted proposals with AI-enhanced content. Generates complete 15+ page proposals with executive summaries, literature reviews, methodology, timeline, and budget breakdown. Supports 6 fields of study with customized templates. Perfect for grant applications, thesis proposals, and research projects.

**Visibility:** PUBLIC

**Price:** 0 (Free) or set your own

---

## Input Fields Configuration (7 Fields Only)

### Field 1: Research Title
```yaml
Field Name: research_title
Label: Research Title
Type: Text Area
Required: Yes
Placeholder: Enter your research project title...
Description: The main title of your research project
Rows: 2
```

### Field 2: Research Question
```yaml
Field Name: research_question
Label: Research Question / Problem Statement
Type: Text Area
Required: Yes
Placeholder: What is the main research question or problem you are investigating?
Description: Clearly state your primary research question or problem statement
Rows: 3
```

### Field 3: Methodology
```yaml
Field Name: methodology
Label: Methodology
Type: Text Area
Required: Yes
Placeholder: Briefly describe your research methodology and approach...
Description: Provide a brief description of your research methodology (will be expanded by AI)
Rows: 4
```

### Field 4: Expected Outcomes
```yaml
Field Name: expected_outcomes
Label: Expected Outcomes / Significance
Type: Text Area
Required: Yes
Placeholder: What are the expected outcomes and significance of your research?
Description: Describe the anticipated results and why they matter
Rows: 3
```

### Field 5: Researcher Name (Optional)
```yaml
Field Name: researcher_name
Label: Researcher Name (Optional)
Type: Text Field
Required: No
Placeholder: Dr. Jane Smith
Description: Your name (optional, defaults to "Anonymous Researcher")
Default: Anonymous Researcher
```

### Field 6: Field of Study (Optional)
```yaml
Field Name: field_of_study
Label: Field of Study (Optional)
Type: Select
Required: No
Options:
  - value: "Sciences", label: "Sciences"
  - value: "Social Sciences", label: "Social Sciences"
  - value: "Humanities", label: "Humanities"
  - value: "Engineering", label: "Engineering"
  - value: "Medical", label: "Medical"
  - value: "Business", label: "Business"
Default: "Sciences"
Description: Select your field for customized formatting (optional)
```

### Field 7: Duration (Optional)
```yaml
Field Name: duration_months
Label: Project Duration in Months (Optional)
Type: Number
Required: No
Min Value: 1
Max Value: 60
Default Value: 12
Step: 1
Description: Project duration (1-60 months, default: 12)
```

---

## Environment Variables (API Keys)

**Required for AI enhancement:**

```yaml
OPENAI_API_KEY: [Your OpenAI API Key]
```

**Note:** If no API key provided, widget uses template-based generation (still professional output).

---

## Removed Fields (Now Using Fixed Defaults)

These are now handled automatically:
- ❌ Institution → Empty (not shown)
- ❌ Budget → Empty (no budget section)
- ❌ Proposal Type → Fixed to "Research Project"
- ❌ References → Empty (no references section)
- ❌ AI Provider → Fixed to "openai"
- ❌ Citation Format → Fixed to "APA"

---

## Example Test Input

```
research_title: "Machine Learning Applications in Climate Change Prediction"

research_question: "How can ensemble machine learning models improve long-term climate prediction accuracy compared to traditional climate models?"

methodology: "Comparative analysis of neural networks, random forests, and gradient boosting models using 50 years of historical climate data from NOAA."

expected_outcomes: "Development of a hybrid ensemble model with 15-20% improved accuracy over current methods."

researcher_name: "Dr. Jane Smith"

field_of_study: "Sciences"

duration_months: 18
```

---

## Expected Output Files

1. **research_proposal.pdf** - Complete 15+ page professional proposal
2. **proposal_data.json** - Structured data in JSON format
3. **summary.txt** - Generation summary

---

## Deployment Checklist

- [x] Only 7 input fields (4 required, 3 optional)
- [x] Field names match environment variables exactly
- [x] Required fields marked correctly
- [x] Default values set for optional fields
- [x] OpenAI API key set as environment variable
- [ ] Test run successful
- [ ] Example output saved
- [ ] Thumbnail created (16:10 ratio)

---

## Summary: 4 Required + 3 Optional = 7 Total Fields

**Required (4):**
1. research_title
2. research_question
3. methodology
4. expected_outcomes

**Optional (3):**
5. researcher_name (default: "Anonymous Researcher")
6. field_of_study (default: "Sciences")
7. duration_months (default: 12)

**Fixed internally:**
- AI Provider: OpenAI
- Citation Format: APA
- Proposal Type: Research Project
- Institution, Budget, References: Not used

Much simpler! ✨
