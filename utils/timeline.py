"""
Timeline Generator

Creates project timeline and Gantt chart data for research proposals.
"""

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from utils.templates import get_timeline_template


def create_timeline(duration_months: int, proposal_type: str) -> dict:
    """Create timeline with phases and milestones."""

    # Get timeline template for proposal type
    phases_template = get_timeline_template(proposal_type)

    # Calculate phase durations
    phases = []
    start_date = datetime.now()
    current_date = start_date

    for phase_template in phases_template:
        phase_months = (duration_months * phase_template['percentage']) / 100
        phase_months = max(1, round(phase_months))  # At least 1 month

        end_date = current_date + relativedelta(months=phase_months)

        # Generate activities based on phase name
        activities = _generate_activities(phase_template['name'], proposal_type)

        phases.append({
            'phase': phase_template['name'],
            'activities': activities,
            'duration': f"{phase_months} month{'s' if phase_months > 1 else ''}",
            'start_date': current_date.strftime('%B %Y'),
            'end_date': end_date.strftime('%B %Y'),
            'months': phase_months
        })

        current_date = end_date

    # Generate milestones
    milestones = _generate_milestones(phases, proposal_type)

    return {
        'phases': phases,
        'milestones': milestones,
        'total_duration': duration_months,
        'start_date': start_date.strftime('%B %Y'),
        'end_date': current_date.strftime('%B %Y')
    }


def _generate_activities(phase_name: str, proposal_type: str) -> str:
    """Generate activities description for a phase."""

    activities_map = {
        'Preparation & Setup': 'Literature review, team assembly, ethics approval, resource acquisition',
        'Project Setup': 'Planning, resource allocation, preliminary research, stakeholder engagement',
        'Literature Review': 'Comprehensive literature search, critical analysis, theoretical framework development',
        'Methodology Development': 'Design research instruments, pilot testing, refinement of protocols',
        'Data Collection': 'Systematic data gathering, participant recruitment, fieldwork, experiments',
        'Investigation': 'Primary research, data collection, experimentation, field studies',
        'Analysis': 'Data processing, statistical analysis, interpretation of findings',
        'Analysis & Writing': 'Data analysis, results interpretation, thesis drafting, literature integration',
        'Results Interpretation': 'Findings synthesis, theoretical implications, practical applications',
        'Documentation': 'Report writing, documentation, results compilation',
        'Reporting & Dissemination': 'Final report, presentations, publications, stakeholder communication',
        'Presentation Prep': 'Abstract finalization, slide preparation, presentation rehearsal',
        'Revision & Defense': 'Thesis revision, defense preparation, final edits',
        'Review & Delivery': 'Quality review, final deliverables, project closure',
        'Research Execution': 'Core research activities, data collection, experimental work'
    }

    return activities_map.get(phase_name, 'Research activities and task completion')


def _generate_milestones(phases: list, proposal_type: str) -> list:
    """Generate key milestones based on phases."""

    milestones = []

    milestone_templates = {
        'Grant Application': [
            'Ethics approval obtained',
            'Data collection completed',
            'Preliminary results available',
            'Final report submitted'
        ],
        'Thesis Proposal': [
            'Proposal defense',
            'Literature review completed',
            'Data collection finished',
            'First draft completed',
            'Final thesis defense'
        ],
        'Research Project': [
            'Project kickoff',
            'Mid-point review',
            'Data analysis completed',
            'Final deliverables submitted'
        ],
        'Conference Abstract': [
            'Research completed',
            'Abstract submitted',
            'Presentation ready'
        ]
    }

    template_milestones = milestone_templates.get(
        proposal_type,
        milestone_templates['Research Project']
    )

    # Distribute milestones across phases
    if len(phases) > 0:
        milestone_interval = len(phases) / len(template_milestones)

        for i, milestone_text in enumerate(template_milestones):
            phase_index = min(int(i * milestone_interval), len(phases) - 1)
            milestones.append({
                'milestone': milestone_text,
                'target_date': phases[phase_index]['end_date']
            })

    return milestones


def create_gantt_chart_data(timeline: dict) -> dict:
    """Create data structure for Gantt chart visualization."""

    gantt_data = {
        'chart_title': 'Project Timeline',
        'total_months': timeline['total_duration'],
        'tasks': []
    }

    month_counter = 0

    for phase in timeline['phases']:
        gantt_data['tasks'].append({
            'task': phase['phase'],
            'start_month': month_counter,
            'duration': phase['months'],
            'end_month': month_counter + phase['months']
        })
        month_counter += phase['months']

    return gantt_data
