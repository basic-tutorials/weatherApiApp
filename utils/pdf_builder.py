"""
PDF Builder

Creates professionally formatted research proposal PDFs using ReportLab.
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Image
)
from reportlab.lib import colors
from datetime import datetime
from pathlib import Path


class PDFBuilder:
    """Build professional research proposal PDFs."""

    def __init__(self, template: dict):
        """Initialize PDF builder with template."""
        self.template = template
        self.page_count = 0
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()

    def _setup_custom_styles(self):
        """Setup custom paragraph styles."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=18,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))

        # Section heading
        self.styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=colors.HexColor('#2c3e50'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))

        # Subsection heading
        self.styles.add(ParagraphStyle(
            name='SubsectionHeading',
            parent=self.styles['Heading3'],
            fontSize=12,
            textColor=colors.HexColor('#34495e'),
            spaceAfter=8,
            spaceBefore=8,
            fontName='Helvetica-Bold'
        ))

        # Body text
        self.styles.add(ParagraphStyle(
            name='CustomBody',
            parent=self.styles['BodyText'],
            fontSize=11,
            leading=16,
            alignment=TA_JUSTIFY,
            spaceAfter=12
        ))

        # Metadata text
        self.styles.add(ParagraphStyle(
            name='Metadata',
            parent=self.styles['Normal'],
            fontSize=11,
            alignment=TA_CENTER,
            spaceAfter=6
        ))

    def create_proposal(self, data: dict, output_path: Path):
        """Create complete research proposal PDF."""
        # Create document
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=letter,
            rightMargin=1*inch,
            leftMargin=1*inch,
            topMargin=1*inch,
            bottomMargin=1*inch
        )

        # Build content
        story = []

        # Cover page
        story.extend(self._create_cover_page(data['metadata']))
        story.append(PageBreak())

        # Table of contents
        story.extend(self._create_toc())
        story.append(PageBreak())

        # Executive summary
        story.extend(self._create_section(
            "Executive Summary",
            data['sections']['executive_summary']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Introduction & Background
        story.extend(self._create_introduction_section(
            data['sections']['introduction']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Literature Review
        story.extend(self._create_section(
            "Literature Review",
            data['sections']['literature_review']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Research Objectives
        story.extend(self._create_objectives_section(
            data['sections']['objectives']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Methodology
        story.extend(self._create_section(
            "Methodology",
            data['sections']['methodology']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Expected Outcomes
        story.extend(self._create_section(
            "Expected Outcomes and Impact",
            data['sections']['expected_outcomes']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Timeline
        story.extend(self._create_timeline_section(
            data['sections']['timeline']
        ))
        story.append(Spacer(1, 0.3*inch))

        # Budget (if provided)
        if data['sections'].get('budget_breakdown'):
            story.extend(self._create_budget_section(
                data['sections']['budget_breakdown']
            ))
            story.append(Spacer(1, 0.3*inch))

        # References
        if data['sections'].get('references'):
            story.extend(self._create_references_section(
                data['sections']['references'],
                data['metadata']['citation_format']
            ))

        # Build PDF
        doc.build(story)
        self.page_count = len(story) // 10  # Rough estimate

    def _create_cover_page(self, metadata: dict) -> list:
        """Create cover page."""
        story = []

        # Add spacing from top
        story.append(Spacer(1, 1.5*inch))

        # Title
        title = Paragraph(
            metadata['title'],
            self.styles['CustomTitle']
        )
        story.append(title)
        story.append(Spacer(1, 0.5*inch))

        # Proposal type
        proposal_type = Paragraph(
            f"<i>{metadata['proposal_type']}</i>",
            self.styles['Metadata']
        )
        story.append(proposal_type)
        story.append(Spacer(1, 1*inch))

        # Researcher info
        researcher = Paragraph(
            f"<b>{metadata['researcher']}</b>",
            self.styles['Metadata']
        )
        story.append(researcher)

        institution = Paragraph(
            metadata['institution'] if metadata['institution'] else 'Research Institution',
            self.styles['Metadata']
        )
        story.append(institution)

        field = Paragraph(
            f"Field: {metadata['field']}",
            self.styles['Metadata']
        )
        story.append(field)
        story.append(Spacer(1, 0.5*inch))

        # Date
        date = Paragraph(
            datetime.now().strftime("%B %Y"),
            self.styles['Metadata']
        )
        story.append(date)

        return story

    def _create_toc(self) -> list:
        """Create table of contents."""
        story = []

        story.append(Paragraph(
            "Table of Contents",
            self.styles['SectionHeading']
        ))
        story.append(Spacer(1, 0.2*inch))

        toc_items = [
            "1. Executive Summary",
            "2. Introduction & Background",
            "3. Literature Review",
            "4. Research Questions and Objectives",
            "5. Methodology",
            "6. Expected Outcomes and Impact",
            "7. Timeline",
            "8. Budget Breakdown",
            "9. References"
        ]

        for item in toc_items:
            story.append(Paragraph(item, self.styles['CustomBody']))
            story.append(Spacer(1, 0.1*inch))

        return story

    def _create_section(self, title: str, content: str) -> list:
        """Create a standard section."""
        story = []

        # Section title
        story.append(Paragraph(title, self.styles['SectionHeading']))
        story.append(Spacer(1, 0.1*inch))

        # Content - split into paragraphs
        paragraphs = content.split('\n\n')
        for para in paragraphs:
            if para.strip():
                story.append(Paragraph(para.strip(), self.styles['CustomBody']))

        return story

    def _create_introduction_section(self, intro_data: dict) -> list:
        """Create introduction section."""
        story = []

        story.append(Paragraph(
            "Introduction & Background",
            self.styles['SectionHeading']
        ))
        story.append(Spacer(1, 0.1*inch))

        # Problem Statement
        story.append(Paragraph(
            "Problem Statement",
            self.styles['SubsectionHeading']
        ))
        story.append(Paragraph(
            intro_data['problem_statement'],
            self.styles['CustomBody']
        ))

        # Research Gap
        story.append(Paragraph(
            "Research Gap",
            self.styles['SubsectionHeading']
        ))
        story.append(Paragraph(
            "This research addresses a critical gap in current understanding by providing systematic investigation of the research question. Existing literature has not fully explored this area, creating an opportunity for meaningful contribution to the field.",
            self.styles['CustomBody']
        ))

        # Significance
        story.append(Paragraph(
            "Significance",
            self.styles['SubsectionHeading']
        ))
        story.append(Paragraph(
            intro_data['significance'],
            self.styles['CustomBody']
        ))

        return story

    def _create_objectives_section(self, objectives: dict) -> list:
        """Create research objectives section."""
        story = []

        story.append(Paragraph(
            "Research Questions and Objectives",
            self.styles['SectionHeading']
        ))
        story.append(Spacer(1, 0.1*inch))

        # Primary objective
        story.append(Paragraph(
            "Primary Research Objective",
            self.styles['SubsectionHeading']
        ))
        story.append(Paragraph(
            objectives['primary'],
            self.styles['CustomBody']
        ))

        # Sub-objectives
        story.append(Paragraph(
            "Specific Objectives",
            self.styles['SubsectionHeading']
        ))

        for i, obj in enumerate(objectives['sub_objectives'], 1):
            story.append(Paragraph(
                f"{i}. {obj}",
                self.styles['CustomBody']
            ))

        # Hypotheses
        if objectives.get('hypotheses'):
            story.append(Paragraph(
                "Research Hypotheses",
                self.styles['SubsectionHeading']
            ))
            for i, hyp in enumerate(objectives['hypotheses'], 1):
                story.append(Paragraph(
                    f"H{i}: {hyp}",
                    self.styles['CustomBody']
                ))

        return story

    def _create_timeline_section(self, timeline_data: dict) -> list:
        """Create timeline section with table."""
        story = []

        story.append(Paragraph(
            "Project Timeline",
            self.styles['SectionHeading']
        ))
        story.append(Spacer(1, 0.1*inch))

        # Create timeline table with Paragraph objects for proper wrapping
        table_data = [['Phase', 'Activities', 'Duration']]

        # Custom style for table cells
        cell_style = ParagraphStyle(
            'CellStyle',
            parent=self.styles['Normal'],
            fontSize=9,
            leading=11
        )

        for phase in timeline_data['phases']:
            table_data.append([
                Paragraph(phase['phase'], cell_style),
                Paragraph(phase['activities'], cell_style),
                Paragraph(phase['duration'], cell_style)
            ])

        table = Table(table_data, colWidths=[1.3*inch, 3.9*inch, 1.3*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        story.append(table)

        return story

    def _create_budget_section(self, budget_data: dict) -> list:
        """Create budget breakdown section."""
        story = []

        story.append(Paragraph(
            "Budget Breakdown",
            self.styles['SectionHeading']
        ))
        story.append(Spacer(1, 0.1*inch))

        story.append(Paragraph(
            f"<b>Total Budget:</b> ${budget_data['total']:,.2f}",
            self.styles['CustomBody']
        ))
        story.append(Spacer(1, 0.15*inch))

        # Create budget table with Paragraph objects
        table_data = [['Category', 'Amount', 'Percentage']]

        cell_style = ParagraphStyle(
            'BudgetCell',
            parent=self.styles['Normal'],
            fontSize=9,
            leading=11
        )

        for item in budget_data['categories']:
            table_data.append([
                Paragraph(item['name'], cell_style),
                Paragraph(f"${item['amount']:,.2f}", cell_style),
                Paragraph(f"{item['percentage']}%", cell_style)
            ])

        table = Table(table_data, colWidths=[2.8*inch, 2.2*inch, 1.5*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('TOPPADDING', (0, 1), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 6),
            ('RIGHTPADDING', (0, 0), (-1, -1), 6),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ]))

        story.append(table)

        return story

    def _create_references_section(self, references: str, format: str) -> list:
        """Create references section."""
        story = []

        story.append(Paragraph(
            "References",
            self.styles['SectionHeading']
        ))
        story.append(Spacer(1, 0.1*inch))

        story.append(Paragraph(
            f"<i>Citation Format: {format}</i>",
            self.styles['CustomBody']
        ))
        story.append(Spacer(1, 0.1*inch))

        # Split references by lines
        ref_lines = references.split('\n')
        for ref in ref_lines:
            if ref.strip():
                story.append(Paragraph(ref.strip(), self.styles['CustomBody']))

        return story
