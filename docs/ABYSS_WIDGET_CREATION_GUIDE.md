# 🚀 Complete Abyss Widget Creation Guide

**A comprehensive guide for creating Python-based AI widgets on the Abyss platform**

---

## 📋 Table of Contents

1. [Quick Start Checklist](#quick-start-checklist)
2. [Project Structure](#project-structure)
3. [Core Files Setup](#core-files-setup)
4. [Input/Output Handling](#inputoutput-handling)
5. [Interface Design](#interface-design)
6. [Best Practices](#best-practices)
7. [Testing & Deployment](#testing--deployment)
8. [Common Patterns](#common-patterns)
9. [Troubleshooting](#troubleshooting)

---

## ✅ Quick Start Checklist

Before creating a widget, ensure you have:

- [ ] Clear widget purpose and functionality defined
- [ ] Python 3.10 compatible code
- [ ] All dependencies identified
- [ ] Input/output data structure planned
- [ ] Memory usage under 512MB
- [ ] Test data prepared

---

## 📁 Project Structure

### Required Structure

```
my-widget/
├── run.py                 # Entry point (REQUIRED)
├── requirements.txt       # Python dependencies (REQUIRED)
├── requirements.system    # System packages (optional)
├── output/                # Output directory (REQUIRED)
│   └── .gitkeep          # Keep directory in git
├── utils/                 # Your code modules (optional)
│   ├── __init__.py
│   ├── processor.py
│   └── formatter.py
├── tests/                 # Test suite (recommended)
│   ├── __init__.py
│   └── test_*.py
├── README.md             # Documentation (recommended)
├── .gitignore           # Git ignore file
└── .env                 # Local env vars (ignored)
```

### Directory Guidelines

- **Keep it simple**: Flat structure preferred for small widgets
- **Organize modules**: Use subdirectories for complex widgets
- **Separate concerns**: Split logic, processing, and formatting
- **Include tests**: Makes debugging and updates easier

---

## 🔧 Core Files Setup

### 1. `run.py` - Entry Point Template

```python
"""
[Widget Name] - Main Entry Point

Brief description of what this widget does.
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
        'input_field1': os.environ.get('input_field1', 'default_value'),
        'input_field2': os.environ.get('input_field2', ''),
        # Add more inputs as needed
    }

def validate_inputs(inputs: dict) -> None:
    """Validate required inputs."""
    required = ['input_field1']  # List required fields

    for field in required:
        if not inputs.get(field):
            raise ValueError(f"Required field '{field}' is missing")

def process_data(inputs: dict) -> dict:
    """Main processing logic."""
    # Your widget logic here
    result = {
        'output1': 'processed value',
        'output2': 'another value'
    }
    return result

def save_outputs(data: dict, output_dir: Path) -> None:
    """Save results to output directory."""
    # Example: Save as text
    with open(output_dir / 'result.txt', 'w') as f:
        f.write(str(data))

    # Example: Save as JSON
    import json
    with open(output_dir / 'result.json', 'w') as f:
        json.dump(data, f, indent=2)

def main():
    """Main execution function."""
    try:
        # Setup
        output_dir = setup_output_directory()

        # Get and validate inputs
        inputs = get_inputs()
        validate_inputs(inputs)

        # Process
        result = process_data(inputs)

        # Save outputs
        save_outputs(result, output_dir)

        print("✅ Processing complete!")
        return 0

    except Exception as e:
        # Save error to output
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)

        with open(output_dir / 'error.txt', 'w') as f:
            f.write(f"Error: {str(e)}\n")
            f.write(f"Please check your inputs and try again.")

        print(f"❌ Error: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

### 2. `requirements.txt` - Python Dependencies

```txt
# Core dependencies (always specify versions)
requests==2.31.0
pandas==2.0.3

# AI/ML libraries (if needed)
openai==1.12.0
anthropic==0.18.1

# Data processing
numpy==1.24.3
Pillow==10.0.0

# Utilities
python-dotenv==1.0.0

# Testing (optional)
pytest==7.4.3
pytest-cov==4.1.0
```

**Guidelines:**
- Always pin versions (use ==)
- Group by functionality
- Add comments for clarity
- Keep minimal (only what you need)
- Test locally first

### 3. `requirements.system` - System Packages

```txt
# PDF processing
poppler-utils

# OCR support
tesseract-ocr

# Media processing
ffmpeg

# Document processing
pandoc
```

**Common packages:**
- `poppler-utils` - PDF utilities
- `tesseract-ocr` - OCR engine
- `ffmpeg` - Video/audio processing
- `imagemagick` - Image processing
- `pandoc` - Document conversion

---

## 🔄 Input/Output Handling

### Input Methods

#### 1. Text Input
```python
# Single-line text
name = os.environ.get('name', 'Anonymous')

# Multi-line text (textarea)
description = os.environ.get('description', '')
```

#### 2. Number Input
```python
# Convert to appropriate type
age = int(os.environ.get('age', '0'))
price = float(os.environ.get('price', '0.0'))
```

#### 3. Boolean Input (Checkbox)
```python
# Checkbox values come as 'true' or 'false' strings
enable_feature = os.environ.get('enable_feature', 'false').lower() == 'true'
```

#### 4. Select/Radio Input
```python
# Single selection
format_type = os.environ.get('format', 'csv')  # csv, json, xml

# Validate choices
valid_formats = ['csv', 'json', 'xml']
if format_type not in valid_formats:
    format_type = 'csv'  # fallback to default
```

#### 5. File Input
```python
# File path provided by Abyss
file_path = os.environ.get('input_file', 'data.pdf')

# Robust file discovery
def find_file(file_path: str) -> str:
    """Find file with fallback strategies."""
    from pathlib import Path

    # Try exact path
    if Path(file_path).exists():
        return file_path

    # Try filename only
    filename = Path(file_path).name
    if Path(filename).exists():
        return filename

    # Try current directory for same extension
    ext = Path(file_path).suffix
    files = list(Path('.').glob(f'*{ext}'))
    if files:
        return str(files[0])

    return file_path  # Return original for error message
```

#### 6. Multi-Value Input
```python
# Comma-separated values
tags = os.environ.get('tags', '').split(',')
tags = [tag.strip() for tag in tags if tag.strip()]

# JSON input
import json
config = json.loads(os.environ.get('config', '{}'))
```

### Output Methods

#### 1. Text Output
```python
# Simple text file
with open('output/result.txt', 'w', encoding='utf-8') as f:
    f.write("Processing complete!\n")
    f.write(f"Result: {result}")
```

#### 2. JSON Output
```python
import json

data = {'status': 'success', 'result': result}
with open('output/data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
```

#### 3. CSV Output
```python
import csv

with open('output/data.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Column1', 'Column2'])  # Header
    writer.writerows(data)  # Data rows
```

#### 4. Image Output
```python
from PIL import Image

image = Image.new('RGB', (800, 600), color='white')
# ... process image ...
image.save('output/result.png')
```

#### 5. Multiple Files
```python
output_dir = Path('output')

# Main result
with open(output_dir / 'main.txt', 'w') as f:
    f.write(main_result)

# Additional data
with open(output_dir / 'details.json', 'w') as f:
    json.dump(details, f, indent=2)

# Summary
with open(output_dir / 'summary.txt', 'w') as f:
    f.write(f"Total items: {len(items)}\n")
    f.write(f"Status: Success\n")
```

---

## 🎨 Interface Design

### Field Types & Configuration

#### 1. Text Field
```yaml
Field Name: user_name
Label: Your Name
Type: Text Field
Required: Yes
Placeholder: John Doe
Description: Enter your full name
Default Value: ""
Max Length: 100
```

#### 2. Text Area
```yaml
Field Name: description
Label: Description
Type: Text Area
Required: No
Placeholder: Enter detailed description...
Description: Provide additional details
Rows: 5
```

#### 3. Number Field
```yaml
Field Name: quantity
Label: Quantity
Type: Number
Required: Yes
Min Value: 1
Max Value: 1000
Default Value: 1
Step: 1
```

#### 4. Select Dropdown
```yaml
Field Name: format
Label: Output Format
Type: Select
Required: No
Options:
  - value: csv, label: "CSV (Spreadsheet)"
  - value: json, label: "JSON (Structured)"
  - value: xml, label: "XML (Markup)"
Default: csv
```

#### 5. Radio Group
```yaml
Field Name: ai_provider
Label: AI Provider
Type: Radio Group
Required: No
Options:
  - value: openai, label: "OpenAI GPT-4"
  - value: anthropic, label: "Anthropic Claude"
  - value: local, label: "Local Model"
Default: openai
```

#### 6. Checkbox
```yaml
Field Name: enable_ocr
Label: Enable OCR
Type: Checkbox
Required: No
Options:
  - value: true, label: "Enable OCR for scanned documents"
Default: false
```

#### 7. Multi-Select
```yaml
Field Name: features
Label: Select Features
Type: Multi-Select
Required: No
Options:
  - "Feature A"
  - "Feature B"
  - "Feature C"
Description: Choose one or more features
```

#### 8. Date Field
```yaml
Field Name: start_date
Label: Start Date
Type: Date
Required: Yes
Min Date: 2024-01-01
Max Date: 2025-12-31
Default: Today
```

#### 9. File Upload
```yaml
Field Name: input_file
Label: Upload File
Type: File
Required: Yes
Accept: .pdf,.docx,.txt
Max Size: 5MB
Description: Upload your document (max 5MB)
```

### Interface Best Practices

1. **Field Naming**
   - Use descriptive names: `invoice_file` not `file1`
   - Use snake_case: `output_format` not `OutputFormat`
   - Match environment variable names exactly

2. **Labels & Descriptions**
   - Clear, concise labels
   - Add helpful descriptions
   - Include examples in placeholders

3. **Required vs Optional**
   - Mark truly required fields
   - Provide defaults for optional fields
   - Validate in code, not just UI

4. **Logical Ordering**
   - Required fields first
   - Group related fields
   - Most important fields at top

---

## 💡 Best Practices

### 1. Error Handling

```python
def main():
    try:
        # Your code here
        pass
    except FileNotFoundError as e:
        save_error(f"File not found: {e}", output_dir)
        return 1
    except ValueError as e:
        save_error(f"Invalid input: {e}", output_dir)
        return 1
    except Exception as e:
        save_error(f"Unexpected error: {e}", output_dir)
        return 1

def save_error(message: str, output_dir: Path):
    """Save user-friendly error message."""
    with open(output_dir / 'error.txt', 'w') as f:
        f.write(f"❌ Error: {message}\n\n")
        f.write("Troubleshooting:\n")
        f.write("1. Check your inputs\n")
        f.write("2. Ensure files are valid\n")
        f.write("3. Try again\n")
```

### 2. Logging

```python
import logging
from pathlib import Path

def setup_logger(output_dir: Path):
    """Setup logging to file and console."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(output_dir / 'widget.log'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(__name__)

# Usage
logger = setup_logger(output_dir)
logger.info("Processing started")
logger.warning("Large file detected")
logger.error("Failed to process")
```

### 3. Input Validation

```python
def validate_email(email: str) -> bool:
    """Validate email format."""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_file_size(file_path: str, max_mb: int = 5) -> None:
    """Validate file size."""
    from pathlib import Path
    size_mb = Path(file_path).stat().st_size / (1024 * 1024)
    if size_mb > max_mb:
        raise ValueError(f"File too large: {size_mb:.2f}MB (max {max_mb}MB)")

def validate_url(url: str) -> bool:
    """Validate URL format."""
    import re
    pattern = r'^https?://[^\s]+$'
    return bool(re.match(pattern, url))
```

### 4. Resource Management

```python
# Use context managers
with open('file.txt') as f:
    data = f.read()

# Clean up temporary files
import tempfile
import shutil

temp_dir = tempfile.mkdtemp()
try:
    # Use temp_dir
    process_files(temp_dir)
finally:
    shutil.rmtree(temp_dir)

# Limit memory usage
import sys
sys.setrecursionlimit(1000)  # Prevent stack overflow
```

### 5. API Key Handling

```python
def get_api_key(provider: str) -> str:
    """Get API key with fallback."""
    key = os.environ.get(f'{provider.upper()}_API_KEY')

    if not key:
        # Fallback to test mode or raise error
        logger.warning(f"No {provider} API key found")
        return None

    return key

# Usage with fallback
api_key = get_api_key('openai')
if api_key:
    # Use AI processing
    result = ai_process(data, api_key)
else:
    # Use basic processing
    result = basic_process(data)
```

---

## 🧪 Testing & Deployment

### Local Testing

```bash
# 1. Set environment variables
export input_field1="test value"
export input_file="test.pdf"

# 2. Run widget
python run.py

# 3. Check output
ls -la output/
cat output/result.txt
```

### Test Script Template

```python
# test_widget.py
import os
import subprocess
from pathlib import Path

def test_widget(inputs: dict):
    """Test widget with given inputs."""
    # Set environment variables
    env = os.environ.copy()
    env.update(inputs)

    # Run widget
    result = subprocess.run(
        ['python', 'run.py'],
        env=env,
        capture_output=True,
        text=True
    )

    # Check results
    assert result.returncode == 0, f"Widget failed: {result.stderr}"
    assert Path('output/result.txt').exists(), "No output file"

    print("✅ Test passed!")

# Run tests
if __name__ == "__main__":
    test_widget({
        'input_field1': 'test',
        'input_field2': 'value'
    })
```

### Abyss Platform Testing

1. **Pre-Test Checklist:**
   - [ ] All files in root directory
   - [ ] `output/` folder exists
   - [ ] `requirements.txt` complete
   - [ ] No hardcoded paths
   - [ ] Test data prepared

2. **Test Run Steps:**
   - Upload widget files
   - Configure interface fields
   - Add test inputs
   - Click "TEST RUN"
   - Check logs for errors
   - Verify output files

3. **Common Test Issues:**
   - File not found → Check file discovery logic
   - Missing API key → Add fallback to test mode
   - Memory exceeded → Optimize processing
   - Import errors → Check requirements.txt

### Deployment Checklist

- [ ] Widget tested successfully
- [ ] Example output prepared
- [ ] Title clear and concise (max 96 chars)
- [ ] 5 relevant tags added
- [ ] Description complete (min 150 chars)
- [ ] Thumbnail uploaded (16:10 ratio)
- [ ] Visibility set (PUBLIC/PRIVATE)
- [ ] Price determined
- [ ] All interface fields configured
- [ ] Documentation complete

---

## 🔄 Common Widget Patterns

### Pattern 1: File Processor

```python
# PDF processor, image converter, etc.
def main():
    file_path = find_file(os.environ.get('input_file'))
    output_format = os.environ.get('format', 'pdf')

    # Process
    result = process_file(file_path, output_format)

    # Save
    output_path = f'output/result.{output_format}'
    save_result(result, output_path)
```

### Pattern 2: AI Text Processor

```python
# Summarizer, translator, analyzer
def main():
    text = os.environ.get('input_text', '')
    ai_provider = os.environ.get('ai_provider', 'openai')

    # Process with AI
    api_key = os.environ.get(f'{ai_provider.upper()}_API_KEY')
    if api_key:
        result = ai_process(text, ai_provider, api_key)
    else:
        result = basic_process(text)

    # Save
    save_output(result, 'output/result.txt')
```

### Pattern 3: Data Transformer

```python
# CSV to JSON, format converter, etc.
def main():
    input_file = find_file(os.environ.get('input_file'))
    output_format = os.environ.get('output_format', 'json')

    # Read input
    data = read_data(input_file)

    # Transform
    transformed = transform_data(data, output_format)

    # Save
    save_data(transformed, f'output/result.{output_format}')
```

### Pattern 4: Web Scraper

```python
# Scraper, API fetcher, etc.
def main():
    url = os.environ.get('url', '')
    output_format = os.environ.get('format', 'json')

    # Validate URL
    if not validate_url(url):
        raise ValueError("Invalid URL")

    # Fetch data
    data = fetch_data(url)

    # Save
    save_data(data, f'output/data.{output_format}')
```

### Pattern 5: Batch Processor

```python
# Process multiple files
def main():
    # Get list of files (comma-separated or JSON)
    files_input = os.environ.get('files', '')
    files = files_input.split(',')

    results = []
    for file_path in files:
        result = process_file(file_path.strip())
        results.append(result)

    # Save combined results
    save_results(results, 'output/results.json')
```

---

## 🔧 Troubleshooting

### Common Issues & Solutions

#### 1. File Not Found
```python
# Problem: File path from Abyss doesn't exist
# Solution: Smart file discovery

def find_file(file_path: str) -> str:
    from pathlib import Path

    if Path(file_path).exists():
        return file_path

    filename = Path(file_path).name
    if Path(filename).exists():
        return filename

    # Check current directory for same extension
    ext = Path(file_path).suffix
    files = list(Path('.').glob(f'*{ext}'))
    if files:
        return str(files[0])

    raise FileNotFoundError(f"File not found: {file_path}")
```

#### 2. Memory Exceeded
```python
# Problem: Widget uses too much memory
# Solutions:

# Process in chunks
def process_large_file(file_path: str):
    chunk_size = 1024 * 1024  # 1MB chunks
    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            process_chunk(chunk)

# Use generators instead of lists
def read_lines(file_path: str):
    with open(file_path) as f:
        for line in f:
            yield line.strip()

# Clean up memory
import gc
gc.collect()
```

#### 3. Import Errors
```python
# Problem: Module not found
# Solution: Check requirements.txt

# Conditional imports
try:
    import optional_module
    HAS_OPTIONAL = True
except ImportError:
    HAS_OPTIONAL = False

if HAS_OPTIONAL:
    # Use optional feature
    pass
else:
    # Use alternative or skip
    pass
```

#### 4. Timeout Issues
```python
# Problem: Widget takes too long
# Solutions:

# Add timeout to requests
import requests
response = requests.get(url, timeout=30)

# Limit processing time
import signal

def timeout_handler(signum, frame):
    raise TimeoutError("Processing took too long")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(60)  # 60 second timeout
try:
    process_data()
finally:
    signal.alarm(0)  # Cancel alarm
```

#### 5. Encoding Issues
```python
# Always specify encoding
with open('file.txt', 'r', encoding='utf-8') as f:
    data = f.read()

with open('output.txt', 'w', encoding='utf-8') as f:
    f.write(data)

# Handle different encodings
import chardet

with open('file.txt', 'rb') as f:
    raw = f.read()
    encoding = chardet.detect(raw)['encoding']

with open('file.txt', 'r', encoding=encoding) as f:
    data = f.read()
```

---

## 📚 Widget Templates

### Minimal Widget Template

```python
import os
from pathlib import Path

def main():
    # Setup
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)

    # Get input
    user_input = os.environ.get('input', 'default')

    # Process
    result = f"Processed: {user_input}"

    # Save output
    with open(output_dir / 'result.txt', 'w') as f:
        f.write(result)

    print("✅ Complete!")

if __name__ == "__main__":
    main()
```

### Full-Featured Widget Template

```python
"""Widget Name - Description"""

import os
import sys
import logging
from pathlib import Path
from typing import Dict, Any, Optional

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def setup_output_directory() -> Path:
    """Create output directory."""
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    return output_dir

def get_inputs() -> Dict[str, Any]:
    """Get and validate inputs."""
    inputs = {
        'field1': os.environ.get('field1', ''),
        'field2': os.environ.get('field2', 'default'),
    }

    # Validate
    if not inputs['field1']:
        raise ValueError("field1 is required")

    return inputs

def process_data(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """Main processing logic."""
    logger.info("Processing data...")

    # Your logic here
    result = {
        'status': 'success',
        'output': 'processed data'
    }

    return result

def save_outputs(data: Dict[str, Any], output_dir: Path) -> None:
    """Save results to output directory."""
    import json

    # JSON output
    with open(output_dir / 'result.json', 'w') as f:
        json.dump(data, f, indent=2)

    # Text summary
    with open(output_dir / 'summary.txt', 'w') as f:
        f.write(f"Status: {data['status']}\n")
        f.write(f"Output: {data['output']}\n")

def save_error(error: Exception, output_dir: Path) -> None:
    """Save error information."""
    with open(output_dir / 'error.txt', 'w') as f:
        f.write(f"Error: {str(error)}\n\n")
        f.write("Please check your inputs and try again.")

def main() -> int:
    """Main execution."""
    try:
        logger.info("Starting widget...")

        # Setup
        output_dir = setup_output_directory()

        # Process
        inputs = get_inputs()
        result = process_data(inputs)

        # Output
        save_outputs(result, output_dir)

        logger.info("✅ Processing complete!")
        return 0

    except Exception as e:
        logger.error(f"❌ Error: {e}")
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)
        save_error(e, output_dir)
        return 1

if __name__ == "__main__":
    sys.exit(main())
```

---

## 🎯 Quick Reference

### Essential Snippets

```python
# 1. Environment variable input
value = os.environ.get('var_name', 'default')

# 2. File discovery
from pathlib import Path
file = Path(os.environ.get('file', 'default.pdf'))

# 3. Output file
Path('output').mkdir(exist_ok=True)
with open('output/result.txt', 'w') as f:
    f.write(result)

# 4. JSON output
import json
with open('output/data.json', 'w') as f:
    json.dump(data, f, indent=2)

# 5. Error handling
try:
    process()
except Exception as e:
    with open('output/error.txt', 'w') as f:
        f.write(f"Error: {e}")

# 6. API key with fallback
api_key = os.environ.get('API_KEY')
if api_key:
    ai_process()
else:
    basic_process()
```

### Platform Limits

- **Memory**: ≤512 MB
- **CPU**: ≤4 vCPUs
- **RAM**: ≤4 GB
- **Python**: 3.10
- **File size**: ≤5 MB (recommended)

### Required Files

1. ✅ `run.py` - Entry point
2. ✅ `requirements.txt` - Dependencies
3. ✅ `output/` - Output directory
4. ⚠️ `requirements.system` - System packages (if needed)

---

## 📖 Additional Resources

### Documentation Files to Include

```
widget-project/
├── README.md              # User-facing documentation
├── DEVELOPMENT.md         # Developer notes
├── CHANGELOG.md          # Version history
└── TROUBLESHOOTING.md    # Common issues
```

### README.md Template

```markdown
# Widget Name

Brief description of what the widget does.

## Features
- Feature 1
- Feature 2
- Feature 3

## Requirements
- Input 1: Description
- Input 2: Description (optional)

## Output
- Output 1: Description
- Output 2: Description

## Usage
1. Upload/Enter inputs
2. Click Run
3. Download results

## Examples
Example input → Expected output

## Limitations
- Limitation 1
- Limitation 2
```

---

## ✅ Final Checklist

Before deploying your widget:

### Code
- [ ] `run.py` works locally
- [ ] All inputs validated
- [ ] Outputs saved to `output/`
- [ ] Error handling implemented
- [ ] Logging added
- [ ] Memory usage optimized

### Files
- [ ] `requirements.txt` complete
- [ ] `requirements.system` if needed
- [ ] `output/` directory exists
- [ ] `.gitignore` configured
- [ ] `README.md` written

### Interface
- [ ] All fields configured
- [ ] Field names match env vars
- [ ] Required fields marked
- [ ] Descriptions clear
- [ ] Defaults set

### Testing
- [ ] Tested locally
- [ ] Tested on Abyss
- [ ] Edge cases handled
- [ ] Error cases tested
- [ ] Example output ready

### Deployment
- [ ] Title set (≤96 chars)
- [ ] Tags added (5 max)
- [ ] Description written (≥150 chars)
- [ ] Thumbnail uploaded
- [ ] Visibility set
- [ ] Price determined

---

**You're ready to create amazing Abyss widgets! 🚀**

For questions or issues, refer to the Abyss documentation or community forums.
