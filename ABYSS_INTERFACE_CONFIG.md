# Abyss Widget Interface Configuration

Copy these field configurations when setting up the widget on Abyss platform.

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

## Input Fields Configuration

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

### Field 5: Researcher Name
```yaml
Field Name: researcher_name
Label: Researcher Name
Type: Text Field
Required: Yes
Placeholder: John Doe
Description: Your full name
```

### Field 6: Institution
```yaml
Field Name: institution
Label: Institution / University
Type: Text Field
Required: No
Placeholder: University of Example
Description: Your institution or university (optional)
```

### Field 7: Field of Study
```yaml
Field Name: field_of_study
Label: Field of Study
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
Description: Select your field of study for customized formatting
```

### Field 8: Duration (Months)
```yaml
Field Name: duration_months
Label: Project Duration (Months)
Type: Number
Required: No
Min Value: 1
Max Value: 60
Default Value: 12
Step: 1
Description: Proposed project duration in months (1-60)
```

### Field 9: Budget
```yaml
Field Name: budget
Label: Estimated Budget (Optional)
Type: Text Field
Required: No
Placeholder: 50000
Description: Estimated budget in dollars (enter number only, e.g., 50000)
```

### Field 10: Proposal Type
```yaml
Field Name: proposal_type
Label: Proposal Type
Type: Radio Group
Required: No
Options:
  - value: "Grant Application", label: "Grant Application"
  - value: "Thesis Proposal", label: "Thesis Proposal"
  - value: "Research Project", label: "Research Project"
  - value: "Conference Abstract", label: "Conference Abstract"
Default: "Research Project"
Description: Type of research proposal you are creating
```

### Field 11: References
```yaml
Field Name: references
Label: References / Bibliography (Optional)
Type: Text Area
Required: No
Placeholder: Enter your references in your chosen citation format...
Description: Optional: Add your references/bibliography (one per line)
Rows: 4
```

### Field 12: AI Provider
```yaml
Field Name: ai_provider
Label: AI Provider
Type: Radio Group
Required: No
Options:
  - value: "anthropic", label: "Anthropic Claude (Recommended)"
  - value: "openai", label: "OpenAI GPT-4"
Default: "anthropic"
Description: Select AI provider for content generation (requires API key)
```

### Field 13: Citation Format
```yaml
Field Name: citation_format
Label: Citation Format
Type: Select
Required: No
Options:
  - value: "APA", label: "APA (American Psychological Association)"
  - value: "MLA", label: "MLA (Modern Language Association)"
  - value: "Chicago", label: "Chicago"
  - value: "IEEE", label: "IEEE"
  - value: "Vancouver", label: "Vancouver"
Default: "APA"
Description: Preferred citation format for references
```

---

## Environment Variables (API Keys)

These should be set in the Abyss platform settings:

```yaml
OPENAI_API_KEY: [Your OpenAI API Key - Optional]
ANTHROPIC_API_KEY: [Your Anthropic API Key - Optional]
```

**Note:** API keys are optional. Without them, the widget will use template-based generation (still produces professional output).

---

## Example Test Input

Use this for testing the widget:

```
research_title: "Machine Learning Applications in Climate Change Prediction"

research_question: "How can ensemble machine learning models improve long-term climate prediction accuracy compared to traditional climate models?"

methodology: "Comparative analysis of neural networks, random forests, and gradient boosting models using 50 years of historical climate data from NOAA. Models will be trained, validated, and tested using cross-validation techniques."

expected_outcomes: "Development of a hybrid ensemble model with 15-20% improved accuracy over current methods. Results will contribute to better climate policy decisions and disaster preparedness strategies."

researcher_name: "Dr. Jane Smith"

institution: "MIT Climate Research Lab"

field_of_study: "Sciences"

duration_months: 18

budget: 125000

proposal_type: "Grant Application"

references: "Smith, J. (2023). Climate modeling approaches. Nature Climate Change, 13(2), 145-160.\nDoe, R. (2022). Machine learning in meteorology. Science, 375(6580), 421-425."

ai_provider: "anthropic"

citation_format: "APA"
```

---

## Expected Output Files

1. **research_proposal.pdf** - Complete 15+ page professional proposal
2. **proposal_data.json** - Structured data in JSON format
3. **summary.txt** - Generation summary

---

## Deployment Checklist

- [x] All 13 input fields configured
- [x] Field names match environment variables exactly
- [x] Required fields marked correctly
- [x] Default values set
- [x] Descriptions are clear and helpful
- [x] Test data prepared
- [x] README.md complete
- [x] requirements.txt ready
- [ ] Test run successful
- [ ] Example output saved
- [ ] Thumbnail created (16:10 ratio)

---

## Support Notes

If users encounter issues:
1. Check that all required fields are filled
2. Verify duration is between 1-60 months
3. Budget should be numbers only (no $ or commas)
4. API keys are optional but recommended
5. Check error.txt in output for specific errors
