"""
Field-Specific Templates

Provides templates customized for different fields of study.
"""


def get_template(field: str, proposal_type: str) -> dict:
    """Get template based on field of study and proposal type."""

    templates = {
        'Sciences': {
            'name': 'Sciences',
            'emphasis': 'empirical',
            'methodology_focus': 'experimental design and data collection',
            'sections': ['hypothesis', 'data_analysis', 'validation'],
            'formatting': {
                'citation_style': 'APA',
                'structure': 'IMRAD',  # Introduction, Methods, Results, Discussion
                'figures': True
            }
        },
        'Social Sciences': {
            'name': 'Social Sciences',
            'emphasis': 'qualitative and quantitative',
            'methodology_focus': 'mixed methods and surveys',
            'sections': ['theoretical_framework', 'sampling', 'ethics'],
            'formatting': {
                'citation_style': 'APA',
                'structure': 'traditional',
                'figures': True
            }
        },
        'Humanities': {
            'name': 'Humanities',
            'emphasis': 'interpretive',
            'methodology_focus': 'critical analysis and textual interpretation',
            'sections': ['theoretical_lens', 'primary_sources', 'argumentation'],
            'formatting': {
                'citation_style': 'MLA',
                'structure': 'narrative',
                'figures': False
            }
        },
        'Engineering': {
            'name': 'Engineering',
            'emphasis': 'applied',
            'methodology_focus': 'design and testing protocols',
            'sections': ['technical_specs', 'prototyping', 'performance_metrics'],
            'formatting': {
                'citation_style': 'IEEE',
                'structure': 'technical',
                'figures': True
            }
        },
        'Medical': {
            'name': 'Medical',
            'emphasis': 'clinical',
            'methodology_focus': 'clinical trials and patient outcomes',
            'sections': ['ethics_approval', 'patient_criteria', 'clinical_measures'],
            'formatting': {
                'citation_style': 'Vancouver',
                'structure': 'clinical',
                'figures': True
            }
        },
        'Business': {
            'name': 'Business',
            'emphasis': 'practical',
            'methodology_focus': 'case studies and market analysis',
            'sections': ['market_analysis', 'stakeholders', 'roi'],
            'formatting': {
                'citation_style': 'APA',
                'structure': 'executive',
                'figures': True
            }
        }
    }

    # Get template or default to Sciences
    template = templates.get(field, templates['Sciences'])

    # Add proposal type specific customizations
    template['proposal_type'] = proposal_type

    if proposal_type == 'Grant Application':
        template['sections'].extend(['budget_justification', 'impact_statement'])
        template['emphasis_areas'] = ['significance', 'innovation', 'impact']
    elif proposal_type == 'Thesis Proposal':
        template['sections'].extend(['literature_gap', 'contribution'])
        template['emphasis_areas'] = ['originality', 'feasibility', 'academic_rigor']
    elif proposal_type == 'Conference Abstract':
        template['sections'] = ['brief_method', 'key_findings', 'implications']
        template['emphasis_areas'] = ['novelty', 'relevance', 'clarity']
    else:  # Research Project
        template['sections'].extend(['deliverables', 'milestones'])
        template['emphasis_areas'] = ['methodology', 'outcomes', 'timeline']

    return template


def get_section_guidance(field: str, section: str) -> str:
    """Get field-specific guidance for a section."""

    guidance = {
        'Sciences': {
            'methodology': 'Emphasize experimental design, control variables, data collection protocols, and statistical analysis methods.',
            'literature_review': 'Focus on recent empirical studies, theoretical frameworks, and research gaps in current scientific understanding.',
            'outcomes': 'Specify measurable outcomes, expected data patterns, and potential scientific contributions.'
        },
        'Social Sciences': {
            'methodology': 'Detail sampling strategies, survey instruments, interview protocols, and mixed-methods approaches.',
            'literature_review': 'Integrate theoretical perspectives, previous empirical work, and social context.',
            'outcomes': 'Describe anticipated findings, policy implications, and social impact.'
        },
        'Humanities': {
            'methodology': 'Explain analytical frameworks, primary source selection, and interpretive approaches.',
            'literature_review': 'Synthesize critical theory, historical context, and scholarly debates.',
            'outcomes': 'Articulate intellectual contributions, new interpretations, and cultural significance.'
        },
        'Engineering': {
            'methodology': 'Specify design parameters, testing procedures, validation methods, and technical requirements.',
            'literature_review': 'Review existing technologies, engineering principles, and innovation opportunities.',
            'outcomes': 'Define technical specifications, performance metrics, and practical applications.'
        },
        'Medical': {
            'methodology': 'Detail clinical protocols, patient selection criteria, safety measures, and outcome measures.',
            'literature_review': 'Summarize clinical evidence, treatment gaps, and medical relevance.',
            'outcomes': 'Specify clinical endpoints, patient benefits, and healthcare implications.'
        },
        'Business': {
            'methodology': 'Outline research methods, data sources, analytical frameworks, and validation approaches.',
            'literature_review': 'Examine market trends, theoretical models, and business practices.',
            'outcomes': 'Project business impact, ROI, stakeholder benefits, and practical recommendations.'
        }
    }

    return guidance.get(field, guidance['Sciences']).get(section, '')


def get_timeline_template(proposal_type: str) -> list:
    """Get timeline phases based on proposal type."""

    templates = {
        'Grant Application': [
            {'name': 'Preparation & Setup', 'percentage': 10},
            {'name': 'Data Collection', 'percentage': 30},
            {'name': 'Analysis', 'percentage': 25},
            {'name': 'Results Interpretation', 'percentage': 20},
            {'name': 'Reporting & Dissemination', 'percentage': 15}
        ],
        'Thesis Proposal': [
            {'name': 'Literature Review', 'percentage': 20},
            {'name': 'Methodology Development', 'percentage': 15},
            {'name': 'Data Collection', 'percentage': 25},
            {'name': 'Analysis & Writing', 'percentage': 30},
            {'name': 'Revision & Defense', 'percentage': 10}
        ],
        'Research Project': [
            {'name': 'Project Setup', 'percentage': 10},
            {'name': 'Investigation', 'percentage': 35},
            {'name': 'Analysis', 'percentage': 25},
            {'name': 'Documentation', 'percentage': 20},
            {'name': 'Review & Delivery', 'percentage': 10}
        ],
        'Conference Abstract': [
            {'name': 'Research Execution', 'percentage': 50},
            {'name': 'Analysis', 'percentage': 30},
            {'name': 'Presentation Prep', 'percentage': 20}
        ]
    }

    return templates.get(proposal_type, templates['Research Project'])
