# Widget Quick-Start Template

**Copy this template for each new widget you create**

---

## 📋 Planning Checklist

### Widget Information
- **Widget Name**: ____________________
- **Purpose**: ____________________
- **Input Type**: [ ] Text  [ ] File  [ ] Both
- **Output Type**: [ ] Text  [ ] File  [ ] JSON  [ ] CSV
- **AI Required**: [ ] Yes  [ ] No
- **Estimated Time**: ______ seconds

### Resource Requirements
- **Memory**: < 512 MB
- **Python Version**: 3.10
- **Special Dependencies**: ____________________

---

## 🗂️ File Structure

Create these files:

```
my-widget-name/
├── run.py                 ✅
├── requirements.txt       ✅
├── requirements.system    ⚠️ (if needed)
├── output/               ✅
│   └── .gitkeep
├── .gitignore            ✅
└── README.md             ✅
```

---

## 💻 Code Template

### 1. `run.py`

```python
"""
[WIDGET NAME] - [ONE LINE DESCRIPTION]

Author: Your Name
Date: YYYY-MM-DD
"""

import os
import sys
from pathlib import Path

def setup_output_directory() -> Path:
    """Create and return output directory."""
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    return output_dir

def get_inputs() -> dict:
    """Get inputs from environment variables."""
    return {
        # TODO: Add your input fields
        'input1': os.environ.get('input1', 'default'),
        'input2': os.environ.get('input2', ''),
    }

def validate_inputs(inputs: dict) -> None:
    """Validate required inputs."""
    # TODO: Add validation logic
    required = ['input1']  # List required fields

    for field in required:
        if not inputs.get(field):
            raise ValueError(f"Required field '{field}' is missing")

def process_data(inputs: dict) -> dict:
    """Main processing logic."""
    # TODO: Implement your widget logic here

    result = {
        'status': 'success',
        'data': 'processed_value'
    }

    return result

def save_outputs(data: dict, output_dir: Path) -> None:
    """Save results to output directory."""
    # TODO: Customize output format

    # Text output
    with open(output_dir / 'result.txt', 'w', encoding='utf-8') as f:
        f.write(str(data))

    # JSON output (optional)
    import json
    with open(output_dir / 'result.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

def save_error(error: Exception, output_dir: Path) -> None:
    """Save error information."""
    with open(output_dir / 'error.txt', 'w', encoding='utf-8') as f:
        f.write(f"❌ Error: {str(error)}\n\n")
        f.write("Troubleshooting:\n")
        f.write("1. Check your inputs\n")
        f.write("2. Ensure all required fields are filled\n")
        f.write("3. Try again\n")

def main():
    """Main execution function."""
    try:
        # Setup
        output_dir = setup_output_directory()

        # Get and validate inputs
        inputs = get_inputs()
        validate_inputs(inputs)

        # Process
        print("🚀 Processing...")
        result = process_data(inputs)

        # Save outputs
        save_outputs(result, output_dir)

        print("✅ Processing complete!")
        return 0

    except Exception as e:
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)
        save_error(e, output_dir)

        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### 2. `requirements.txt`

```txt
# TODO: Add your dependencies with versions

# Example dependencies:
# requests==2.31.0
# pandas==2.0.3
# openai==1.12.0
# anthropic==0.18.1
# Pillow==10.0.0
# python-dotenv==1.0.0

# Testing (optional)
# pytest==7.4.3
```

### 3. `requirements.system` (if needed)

```txt
# TODO: Add system packages if needed

# Common examples:
# poppler-utils
# tesseract-ocr
# ffmpeg
# pandoc
```

### 4. `.gitignore`

```
# Environment
.env
.env.local

# Python
__pycache__/
*.py[cod]
*.so
.Python
*.egg-info/

# Virtual environments
venv/
env/
.venv

# IDE
.vscode/
.idea/
.DS_Store

# Testing
.pytest_cache/
.coverage
htmlcov/

# Output files
output/*.txt
output/*.csv
output/*.json
output/*.pdf
!output/.gitkeep
```

### 5. `README.md`

```markdown
# [Widget Name]

[Brief description of what this widget does]

## 🎯 Purpose

[Explain the problem this widget solves]

## ✨ Features

- Feature 1
- Feature 2
- Feature 3

## 📥 Inputs

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| input1 | Text | Yes | Description of input1 |
| input2 | File | No | Description of input2 |

## 📤 Outputs

| File | Format | Description |
|------|--------|-------------|
| result.txt | Text | Main result |
| result.json | JSON | Structured data |

## 🚀 Usage

1. [Step 1]
2. [Step 2]
3. [Step 3]

## 📋 Example

**Input:**
```
input1: "example value"
input2: "another value"
```

**Output:**
```
Result: Processed example value
Status: Success
```

## ⚙️ Requirements

- Python 3.10
- [List any API keys needed]
- [List file format requirements]

## 🔒 Privacy

[Explain how data is handled]

## ⚠️ Limitations

- Limitation 1
- Limitation 2

## 📝 License

[Your license information]
```

---

## 🎨 Interface Configuration

### Fields to Configure on Abyss

Copy this format for each field:

#### Field 1: [Field Name]
```yaml
Field Name: field_name
Label: User-Friendly Label
Type: [Text Field|Text Area|Number|Select|Radio|Checkbox|File|Date]
Required: [Yes|No]
Default: "default_value"
Placeholder: "example input..."
Description: "Helper text for users"
```

#### Field 2: [Field Name]
```yaml
Field Name: field_name
Label: User-Friendly Label
Type: [Type]
Required: [Yes|No]
Options: (if Select/Radio/Checkbox)
  - value1: "Label 1"
  - value2: "Label 2"
Default: "value1"
Description: "Helper text"
```

### Complete Interface Checklist

- [ ] Field 1 configured
- [ ] Field 2 configured
- [ ] Field 3 configured
- [ ] All field names match environment variables
- [ ] All required fields marked
- [ ] All descriptions added
- [ ] Default values set

---

## 📝 Widget Metadata

### Title
```
[Widget Name] - [Short Description]
```
*(Max 96 characters)*

### Tags (5 max)
```
1. tag1
2. tag2
3. tag3
4. tag4
5. tag5
```

### Description
```
[Write 150-500 character description]

What it does, who it's for, key features, requirements.
```

### Visibility
- [ ] PUBLIC
- [ ] PRIVATE

### Price
```
[0 for free, or credit amount]
```

---

## ✅ Testing Checklist

### Local Testing
```bash
# 1. Set environment variables
export input1="test value"
export input2="test value 2"

# 2. Run widget
python run.py

# 3. Check output
ls -la output/
cat output/result.txt
```

### Pre-Deployment Testing
- [ ] Runs without errors
- [ ] Creates output files
- [ ] Handles invalid inputs gracefully
- [ ] Memory usage < 512MB
- [ ] Execution time reasonable
- [ ] All edge cases tested

### Abyss Platform Testing
- [ ] Files uploaded correctly
- [ ] Interface fields working
- [ ] Test run successful
- [ ] Output files generated
- [ ] Error handling works
- [ ] Example output saved

---

## 🚀 Deployment Steps

1. **Upload Files**
   - [ ] All files in root directory
   - [ ] output/ folder exists
   - [ ] No unnecessary files

2. **Configure Interface**
   - [ ] All fields added
   - [ ] Labels clear
   - [ ] Descriptions helpful
   - [ ] Defaults set

3. **Add Metadata**
   - [ ] Title (≤96 chars)
   - [ ] Tags (5)
   - [ ] Description (≥150 chars)
   - [ ] Thumbnail (16:10)
   - [ ] Visibility
   - [ ] Price

4. **Test Run**
   - [ ] Upload test data
   - [ ] Run widget
   - [ ] Verify output
   - [ ] Check logs

5. **Deploy**
   - [ ] Review everything
   - [ ] Click "Share and Deploy"
   - [ ] Save example output
   - [ ] Test live widget

---

## 📊 Common Patterns Reference

### Pattern 1: Text Processor
```python
text = os.environ.get('input_text', '')
processed = process_text(text)
save_text(processed, 'output/result.txt')
```

### Pattern 2: File Processor
```python
file_path = find_file(os.environ.get('input_file'))
data = process_file(file_path)
save_data(data, 'output/result.json')
```

### Pattern 3: AI Integration
```python
api_key = os.environ.get('OPENAI_API_KEY')
if api_key:
    result = ai_process(data, api_key)
else:
    result = basic_process(data)
```

### Pattern 4: Multi-Output
```python
# Save multiple formats
save_json(data, 'output/data.json')
save_csv(data, 'output/data.csv')
save_summary(data, 'output/summary.txt')
```

---

## 🐛 Common Issues

### Issue 1: File Not Found
```python
def find_file(file_path: str) -> str:
    from pathlib import Path
    if Path(file_path).exists():
        return file_path
    filename = Path(file_path).name
    if Path(filename).exists():
        return filename
    raise FileNotFoundError(f"File not found: {file_path}")
```

### Issue 2: Memory Exceeded
```python
# Process in chunks
def process_large_file(file_path):
    with open(file_path, 'r') as f:
        for chunk in iter(lambda: f.read(1024*1024), ''):
            process_chunk(chunk)
```

### Issue 3: API Key Missing
```python
# Graceful fallback
api_key = os.environ.get('API_KEY')
if not api_key:
    logger.warning("No API key - using basic mode")
    return basic_process(data)
```

---

## 📚 Resources

- [Abyss Documentation](https://abyss.platform/docs)
- [Full Widget Guide](./ABYSS_WIDGET_CREATION_GUIDE.md)
- [Python 3.10 Docs](https://docs.python.org/3.10/)

---

## 🎯 Quick Commands

```bash
# Create widget structure
mkdir my-widget && cd my-widget
touch run.py requirements.txt .gitignore README.md
mkdir output && touch output/.gitkeep

# Test locally
python run.py

# Check output
ls -la output/

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest tests/
```

---

**Happy Widget Building! 🚀**

*Save this template and reuse for every new widget*
