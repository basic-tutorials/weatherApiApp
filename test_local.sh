#!/bin/bash

# Local Test Script for Research Proposal Generator
# This script tests the widget locally before deploying to Abyss

echo "🧪 Testing Research Proposal Generator..."
echo ""

# Set test environment variables
export research_title="Machine Learning Applications in Climate Change Prediction"
export research_question="How can ensemble machine learning models improve long-term climate prediction accuracy compared to traditional climate models?"
export methodology="Comparative analysis of neural networks, random forests, and gradient boosting models using 50 years of historical climate data from NOAA. Models will be trained, validated, and tested using cross-validation techniques."
export expected_outcomes="Development of a hybrid ensemble model with 15-20% improved accuracy over current methods. Results will contribute to better climate policy decisions and disaster preparedness strategies."
export researcher_name="Dr. Jane Smith"
export institution="MIT Climate Research Lab"
export field_of_study="Sciences"
export duration_months="18"
export budget="125000"
export proposal_type="Grant Application"
export references="Smith, J. (2023). Climate modeling approaches. Nature Climate Change, 13(2), 145-160."
export ai_provider="anthropic"
export citation_format="APA"

# Optional: Add your API keys here for AI enhancement
# export ANTHROPIC_API_KEY="your-key-here"
# export OPENAI_API_KEY="your-key-here"

echo "📝 Test inputs configured"
echo "🚀 Running widget..."
echo ""

# Run the widget
python run.py

# Check results
echo ""
echo "📊 Checking outputs..."
ls -lh output/

if [ -f "output/research_proposal.pdf" ]; then
    echo "✅ PDF generated successfully!"
    echo "📄 File size: $(ls -lh output/research_proposal.pdf | awk '{print $5}')"
else
    echo "❌ PDF not generated"
fi

if [ -f "output/error.txt" ]; then
    echo "⚠️  Error file found:"
    cat output/error.txt
fi

echo ""
echo "🎉 Test complete!"
