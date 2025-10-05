"""
Research Proposal Generator - Main Entry Point

Transforms research ideas into professionally formatted proposals with proper
academic structure, saving students/researchers 10+ hours of work.
"""

import os
import sys
from pathlib import Path
import json

# Import utilities
from utils.ai_generator import AIGenerator
from utils.pdf_builder import PDFBuilder
from utils.templates import get_template
from utils.timeline import create_timeline


def setup_output_directory() -> Path:
    """Create and return output directory."""
    output_dir = Path('output')
    output_dir.mkdir(exist_ok=True)
    return output_dir


def get_inputs() -> dict:
    """Get inputs from environment variables."""
    return {
        # Required fields
        'research_title': os.environ.get('research_title', ''),
        'research_question': os.environ.get('research_question', ''),
        'methodology': os.environ.get('methodology', ''),
        'expected_outcomes': os.environ.get('expected_outcomes', ''),

        # Optional fields
        'researcher_name': os.environ.get('researcher_name', 'Anonymous Researcher'),
        'field_of_study': os.environ.get('field_of_study', 'Sciences'),
        'duration_months': int(os.environ.get('duration_months', '12')),

        # Fixed defaults (not exposed to user)
        'institution': '',
        'budget': '',
        'proposal_type': 'Research Project',
        'references': '',
        'ai_provider': 'openai',  # Fixed to OpenAI
        'citation_format': 'APA',
    }


def validate_inputs(inputs: dict) -> None:
    """Validate required inputs."""
    required = [
        'research_title',
        'research_question',
        'methodology',
        'expected_outcomes'
    ]

    for field in required:
        if not inputs.get(field):
            raise ValueError(
                f"Required field '{field}' is missing. "
                f"Please provide all required information."
            )

    # Validate duration
    if inputs['duration_months'] < 1 or inputs['duration_months'] > 60:
        raise ValueError("Duration must be between 1 and 60 months")


def get_api_key(provider: str) -> str:
    """Get API key for AI provider."""
    if provider == 'openai':
        return os.environ.get('OPENAI_API_KEY', '')
    elif provider == 'anthropic':
        return os.environ.get('ANTHROPIC_API_KEY', '')
    return ''


def process_proposal(inputs: dict, output_dir: Path) -> dict:
    """Main processing logic to generate research proposal."""
    print("🚀 Generating research proposal...")

    # Check if AI is available
    api_key = get_api_key(inputs['ai_provider'])

    # Initialize AI generator
    ai_generator = AIGenerator(
        provider=inputs['ai_provider'],
        api_key=api_key
    )

    # LAYER 1: Enhance user input for better quality
    enhanced_inputs = ai_generator.enhance_user_input(inputs)

    # Show what was enhanced (for debugging)
    if enhanced_inputs != inputs:
        print("\n📝 Input Enhancement Summary:")
        if enhanced_inputs['research_title'] != inputs['research_title']:
            print(f"   Title: {inputs['research_title'][:50]}...")
            print(f"   → {enhanced_inputs['research_title'][:50]}...")
        if enhanced_inputs['research_question'] != inputs['research_question']:
            print(f"   Question enhanced ✓")
        if enhanced_inputs['methodology'] != inputs['methodology']:
            print(f"   Methodology enhanced ✓")
        if enhanced_inputs['expected_outcomes'] != inputs['expected_outcomes']:
            print(f"   Outcomes enhanced ✓")
        print()

    # Use enhanced inputs for the rest of the process
    inputs = enhanced_inputs

    # Get template for field of study
    template = get_template(inputs['field_of_study'], inputs['proposal_type'])

    # Generate AI-enhanced content
    print("📝 Generating executive summary...")
    executive_summary = ai_generator.generate_executive_summary(
        title=inputs['research_title'],
        question=inputs['research_question'],
        methodology=inputs['methodology'],
        outcomes=inputs['expected_outcomes'],
        field=inputs['field_of_study'],
        proposal_type=inputs['proposal_type']
    )

    print("📚 Creating literature review framework...")
    literature_review = ai_generator.generate_literature_review(
        field=inputs['field_of_study'],
        topic=inputs['research_title'],
        question=inputs['research_question']
    )

    print("🔬 Expanding methodology section...")
    expanded_methodology = ai_generator.expand_methodology(
        methodology=inputs['methodology'],
        field=inputs['field_of_study'],
        research_type=inputs['proposal_type']
    )

    print("🎯 Generating research objectives...")
    objectives = ai_generator.generate_objectives(
        question=inputs['research_question'],
        field=inputs['field_of_study']
    )

    # Create timeline
    print("📅 Creating project timeline...")
    timeline_data = create_timeline(
        duration_months=inputs['duration_months'],
        proposal_type=inputs['proposal_type']
    )

    # Compile proposal data
    proposal_data = {
        'metadata': {
            'title': inputs['research_title'],
            'researcher': inputs['researcher_name'],
            'institution': inputs['institution'],
            'field': inputs['field_of_study'],
            'proposal_type': inputs['proposal_type'],
            'duration': inputs['duration_months'],
            'budget': inputs['budget'],
            'citation_format': inputs['citation_format']
        },
        'sections': {
            'executive_summary': executive_summary,
            'introduction': {
                'problem_statement': inputs['research_question'],
                'methodology_brief': inputs['methodology'],
                'significance': inputs['expected_outcomes']
            },
            'literature_review': literature_review,
            'objectives': objectives,
            'methodology': expanded_methodology,
            'expected_outcomes': inputs['expected_outcomes'],
            'timeline': timeline_data,
            'budget_breakdown': _create_budget_breakdown(inputs['budget']) if inputs['budget'] else None,
            'references': inputs.get('references', '')
        },
        'template': template
    }

    # Generate PDF
    print("📄 Building professional PDF...")
    pdf_builder = PDFBuilder(template)
    pdf_path = output_dir / 'research_proposal.pdf'
    pdf_builder.create_proposal(proposal_data, pdf_path)

    # Also save as JSON for reference
    json_path = output_dir / 'proposal_data.json'
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(proposal_data, f, indent=2)

    return {
        'status': 'success',
        'pdf_path': str(pdf_path),
        'json_path': str(json_path),
        'pages': pdf_builder.page_count,
        'sections': len(proposal_data['sections'])
    }


def _create_budget_breakdown(budget_str: str) -> dict:
    """Create structured budget breakdown."""
    try:
        total_budget = float(budget_str.replace('$', '').replace(',', ''))

        # Standard research budget allocation
        return {
            'total': total_budget,
            'categories': [
                {'name': 'Personnel', 'amount': total_budget * 0.40, 'percentage': 40},
                {'name': 'Equipment', 'amount': total_budget * 0.25, 'percentage': 25},
                {'name': 'Materials & Supplies', 'amount': total_budget * 0.15, 'percentage': 15},
                {'name': 'Travel', 'amount': total_budget * 0.10, 'percentage': 10},
                {'name': 'Other Costs', 'amount': total_budget * 0.10, 'percentage': 10},
            ]
        }
    except:
        return None


def save_summary(result: dict, output_dir: Path) -> None:
    """Save execution summary."""
    with open(output_dir / 'summary.txt', 'w', encoding='utf-8') as f:
        f.write("✅ Research Proposal Generated Successfully!\n\n")
        f.write("=" * 60 + "\n")
        f.write("PROPOSAL GENERATION SUMMARY\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"Status: {result['status'].upper()}\n")
        f.write(f"PDF Generated: {result['pdf_path']}\n")
        f.write(f"Total Pages: {result['pages']}\n")
        f.write(f"Sections Created: {result['sections']}\n\n")
        f.write("Your professional research proposal is ready!\n")
        f.write("\n📄 Download the PDF from the output folder.\n")
        f.write("📊 Review the JSON file for structured data.\n")


def save_error(error: Exception, output_dir: Path) -> None:
    """Save error information."""
    with open(output_dir / 'error.txt', 'w', encoding='utf-8') as f:
        f.write(f"❌ Error: {str(error)}\n\n")
        f.write("=" * 60 + "\n")
        f.write("TROUBLESHOOTING\n")
        f.write("=" * 60 + "\n\n")
        f.write("1. Check that all required fields are filled:\n")
        f.write("   - Research title\n")
        f.write("   - Research question/problem statement\n")
        f.write("   - Methodology description\n")
        f.write("   - Expected outcomes\n")
        f.write("   - Researcher name\n\n")
        f.write("2. Ensure duration is between 1-60 months\n\n")
        f.write("3. If using AI features, check API key is provided\n\n")
        f.write("4. Try again with corrected inputs\n")


def main():
    """Main execution function."""
    try:
        # Setup
        output_dir = setup_output_directory()

        # Get and validate inputs
        inputs = get_inputs()
        validate_inputs(inputs)

        # Process
        result = process_proposal(inputs, output_dir)

        # Save summary
        save_summary(result, output_dir)

        print("\n✅ Processing complete!")
        print(f"📄 Your research proposal is ready: {result['pdf_path']}")
        return 0

    except Exception as e:
        output_dir = Path('output')
        output_dir.mkdir(exist_ok=True)
        save_error(e, output_dir)

        print(f"\n❌ Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
