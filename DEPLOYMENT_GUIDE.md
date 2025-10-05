# Deployment Guide for Abyss Platform

Step-by-step guide to deploy the Research Proposal Generator widget to Abyss.

---

## 📦 Pre-Deployment Checklist

### 1. Files to Upload
Ensure these files are ready:

- ✅ `run.py` - Main entry point
- ✅ `requirements.txt` - Python dependencies
- ✅ `output/.gitkeep` - Output directory placeholder
- ✅ `utils/__init__.py` - Utils package init
- ✅ `utils/ai_generator.py` - AI content generator
- ✅ `utils/pdf_builder.py` - PDF builder
- ✅ `utils/templates.py` - Field templates
- ✅ `utils/timeline.py` - Timeline generator
- ✅ `README.md` - Documentation
- ✅ `.gitignore` - Git ignore file

### 2. Local Testing (Optional but Recommended)

```bash
# Install dependencies
pip install -r requirements.txt

# Run test script
./test_local.sh

# Or manually test
export research_title="Test Research"
export research_question="Test question?"
export methodology="Test methodology"
export expected_outcomes="Test outcomes"
export researcher_name="Test User"
python run.py

# Check output
ls -la output/
```

---

## 🚀 Deployment Steps

### Step 1: Create New Widget on Abyss

1. Log into Abyss platform
2. Navigate to "Create Widget" or "My Widgets"
3. Click "New Widget" or "Create New"
4. Select "Python 3.10" as runtime

### Step 2: Upload Files

**Option A: Upload Individual Files**
1. Upload `run.py` to root
2. Upload `requirements.txt` to root
3. Create `utils/` directory
4. Upload all files from `utils/` folder
5. Create `output/` directory
6. Upload `.gitkeep` to `output/` folder

**Option B: Upload as ZIP** (if supported)
1. Create a ZIP file with proper structure:
   ```
   widget.zip
   ├── run.py
   ├── requirements.txt
   ├── output/
   │   └── .gitkeep
   └── utils/
       ├── __init__.py
       ├── ai_generator.py
       ├── pdf_builder.py
       ├── templates.py
       └── timeline.py
   ```
2. Upload ZIP to Abyss

### Step 3: Configure Widget Metadata

**Basic Information:**
- **Widget Name**: Research Proposal Generator
- **Title**: Research Proposal Generator - Professional Academic Proposals in 60 Seconds
- **Short Description**: Transform research ideas into professionally formatted proposals
- **Category**: Education / Productivity / Academic

**Detailed Description:**
```
Transform research ideas into professionally formatted proposals with AI-enhanced content.

✨ Features:
• AI-generated executive summaries and literature reviews
• Field-specific templates (Sciences, Humanities, Engineering, Medical, Business, Social Sciences)
• Professional 15+ page PDF output
• Automatic timeline with Gantt chart
• Budget breakdown tables
• Multiple citation formats (APA, MLA, IEEE, Vancouver, Chicago)

Perfect for grant applications, thesis proposals, and research projects. Save 10+ hours of formatting work!
```

**Tags**: research, academic, pdf, proposal, education

**Visibility**: PUBLIC (or PRIVATE for testing)

**Price**: 0 (free) or set your own

### Step 4: Configure Input Fields

**Copy field configurations from `ABYSS_INTERFACE_CONFIG.md`**

Configure these 13 fields in order:

1. **research_title** - Text Area (Required)
2. **research_question** - Text Area (Required)
3. **methodology** - Text Area (Required)
4. **expected_outcomes** - Text Area (Required)
5. **researcher_name** - Text Field (Required)
6. **institution** - Text Field (Optional)
7. **field_of_study** - Select dropdown (Optional, default: Sciences)
8. **duration_months** - Number (Optional, default: 12, range: 1-60)
9. **budget** - Text Field (Optional)
10. **proposal_type** - Radio Group (Optional, default: Research Project)
11. **references** - Text Area (Optional)
12. **ai_provider** - Radio Group (Optional, default: anthropic)
13. **citation_format** - Select dropdown (Optional, default: APA)

**Important**: Field names must match EXACTLY as shown above (case-sensitive)

### Step 5: Configure Environment Variables (Optional)

Add API keys for AI enhancement:

```
ANTHROPIC_API_KEY=your-anthropic-key-here
OPENAI_API_KEY=your-openai-key-here
```

**Note**: These are optional. Widget works without them using template-based generation.

### Step 6: Test Run

Use this test data:

```
research_title: Machine Learning Applications in Climate Change Prediction

research_question: How can ensemble machine learning models improve long-term climate prediction accuracy?

methodology: Comparative analysis of neural networks, random forests, and gradient boosting models using historical climate data

expected_outcomes: Development of hybrid model with 15-20% improved accuracy over current methods

researcher_name: Dr. Jane Smith

institution: MIT Climate Research Lab

field_of_study: Sciences

duration_months: 18

budget: 125000

proposal_type: Grant Application

citation_format: APA
```

**Expected Results:**
- Processing time: 15-45 seconds
- Output files:
  - `research_proposal.pdf` (15+ pages)
  - `proposal_data.json`
  - `summary.txt`
- No errors in logs

### Step 7: Review Output

Download and check:
1. ✅ PDF opens correctly
2. ✅ All sections present (cover, TOC, 9 sections)
3. ✅ Formatting is professional
4. ✅ Timeline table displays
5. ✅ Budget table appears (if budget provided)
6. ✅ No obvious errors or missing content

### Step 8: Create Thumbnail

Create a 16:10 ratio thumbnail showing:
- Widget name
- Key features (AI, PDF, Multiple Fields)
- Professional design
- Recommended size: 1600×1000px

### Step 9: Save Example Output

1. Run widget with test data
2. Download the generated `research_proposal.pdf`
3. Save as example output on Abyss
4. This helps users understand what they'll get

### Step 10: Deploy

1. Review all settings one final time
2. Click "Save and Deploy" or "Publish"
3. Widget is now live!

---

## 🧪 Testing Checklist

Before final deployment, test:

- [ ] All required fields validation works
- [ ] Optional fields work when empty
- [ ] Each field of study generates correctly
- [ ] Each proposal type works
- [ ] Duration validation (1-60 months)
- [ ] Budget breakdown appears when budget provided
- [ ] Timeline generates for various durations
- [ ] PDF downloads correctly
- [ ] Error handling works (try invalid inputs)
- [ ] Works without API keys (template mode)
- [ ] Works with API keys (AI mode)

---

## 🐛 Troubleshooting

### Issue: Import errors
**Solution**: Ensure all files in `utils/` are uploaded and `__init__.py` exists

### Issue: File not found errors
**Solution**: Verify `output/` directory exists with `.gitkeep` file

### Issue: PDF not generating
**Solution**: Check logs for ReportLab errors. Ensure `requirements.txt` installed correctly

### Issue: AI generation not working
**Solution**: Check API keys are set. Widget should fall back to templates automatically

### Issue: Timeline errors
**Solution**: Verify duration_months is between 1-60

### Issue: Budget not appearing
**Solution**: Budget must be numeric string (e.g., "50000" not "$50,000")

---

## 📊 Post-Deployment

### Monitor

1. Check widget analytics
2. Review user feedback
3. Monitor error rates
4. Track usage patterns

### Iterate

Based on feedback:
1. Add requested features
2. Fix any bugs
3. Improve templates
4. Enhance AI prompts
5. Update documentation

### Promote

1. Share on social media
2. Academic communities
3. University forums
4. Research groups
5. Student organizations

---

## 🎯 Success Metrics

Track these KPIs:
- Number of proposals generated
- User satisfaction ratings
- Completion rate
- Error rate
- Average processing time
- Return users

---

## 📝 Maintenance

### Regular Updates

**Monthly:**
- Review error logs
- Update AI prompts if needed
- Check dependency versions

**Quarterly:**
- Update dependencies
- Add new features
- Improve templates based on feedback

**Yearly:**
- Major version updates
- New field templates
- Enhanced AI models

---

## 🆘 Support

Common user questions:

**Q: How long does generation take?**
A: 15-45 seconds depending on AI usage

**Q: Do I need an API key?**
A: No, widget works without API keys using templates

**Q: Can I edit the PDF?**
A: The PDF is read-only, but JSON data is provided for custom processing

**Q: What fields are supported?**
A: Sciences, Social Sciences, Humanities, Engineering, Medical, Business

**Q: How many pages will the proposal be?**
A: Typically 15-25 pages depending on content

---

## ✅ Final Checklist

Before going live:

- [ ] All files uploaded correctly
- [ ] 13 input fields configured
- [ ] Field names match exactly
- [ ] Test run successful
- [ ] PDF generated correctly
- [ ] Example output saved
- [ ] Thumbnail uploaded
- [ ] Description complete
- [ ] Tags added
- [ ] Price set
- [ ] Documentation reviewed
- [ ] Support plan ready

---

**You're ready to deploy! 🚀**

Good luck with your Research Proposal Generator widget!
