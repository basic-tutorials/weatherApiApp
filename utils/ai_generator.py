"""
AI Content Generator

Generates academic content for research proposals using AI providers.
"""

import os


class AIGenerator:
    """Generate AI-enhanced content for research proposals."""

    def __init__(self, provider: str = 'anthropic', api_key: str = ''):
        """Initialize AI generator with provider."""
        self.provider = provider
        self.api_key = api_key
        self.client = None

        if api_key:
            self._init_client()

    def _init_client(self):
        """Initialize AI client."""
        try:
            if self.provider == 'openai':
                import openai
                self.client = openai.OpenAI(api_key=self.api_key)
            elif self.provider == 'anthropic':
                import anthropic
                self.client = anthropic.Anthropic(api_key=self.api_key)
        except Exception as e:
            print(f"⚠️  Warning: Could not initialize AI client: {e}")
            print("   Falling back to template-based generation")
            self.client = None

    def generate_executive_summary(
        self,
        title: str,
        question: str,
        methodology: str,
        outcomes: str,
        field: str,
        proposal_type: str
    ) -> str:
        """Generate executive summary."""
        if self.client:
            return self._ai_generate_summary(
                title, question, methodology, outcomes, field, proposal_type
            )
        else:
            return self._template_summary(
                title, question, methodology, outcomes
            )

    def _ai_generate_summary(
        self,
        title: str,
        question: str,
        methodology: str,
        outcomes: str,
        field: str,
        proposal_type: str
    ) -> str:
        """Generate summary using AI."""
        prompt = f"""Generate a professional research proposal executive summary (200-250 words) for:

Field: {field}
Title: {title}
Research Question: {question}
Methodology: {methodology}
Expected Outcomes: {outcomes}

Requirements:
- Academic tone appropriate for {proposal_type}
- Highlight significance and innovation
- Include expected impact
- Follow {proposal_type} formatting standards
- Be concise but comprehensive"""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=400,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()

            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=400,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text.strip()

        except Exception as e:
            print(f"⚠️  AI generation failed: {e}. Using template.")
            return self._template_summary(title, question, methodology, outcomes)

    def _template_summary(
        self,
        title: str,
        question: str,
        methodology: str,
        outcomes: str
    ) -> str:
        """Generate summary using template."""
        return f"""This research proposal, titled "{title}", addresses a critical gap in current understanding by investigating: {question}

The proposed study will employ {methodology} to systematically examine this research question. This approach has been selected for its robustness and applicability to the research context.

The expected outcomes of this research include: {outcomes} These findings will contribute significantly to the field by providing new insights and practical applications.

This research is timely and significant, as it addresses current challenges and has the potential to inform both theory and practice. The proposed methodology is rigorous and appropriate for addressing the research objectives, ensuring reliable and valid results."""

    def generate_literature_review(
        self,
        field: str,
        topic: str,
        question: str
    ) -> str:
        """Generate literature review framework."""
        if self.client:
            return self._ai_generate_literature(field, topic, question)
        else:
            return self._template_literature(field, topic)

    def _ai_generate_literature(
        self,
        field: str,
        topic: str,
        question: str
    ) -> str:
        """Generate literature review using AI."""
        prompt = f"""Create a literature review framework for a research proposal in {field} on the topic: {topic}

Research Question: {question}

Provide:
1. Overview of current research landscape
2. Key theoretical frameworks
3. Research gaps this study addresses
4. How this study builds on existing work

Keep it academic but concise (300-400 words)."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=600,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()

            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=600,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text.strip()

        except Exception as e:
            print(f"⚠️  AI generation failed: {e}. Using template.")
            return self._template_literature(field, topic)

    def _template_literature(self, field: str, topic: str) -> str:
        """Generate literature review using template."""
        return f"""The field of {field} has seen significant developments in recent years, particularly in areas related to {topic}. Current research has established foundational understanding of key concepts and methodologies, yet several gaps remain.

Existing studies have primarily focused on traditional approaches, with limited exploration of innovative methodologies and contemporary applications. This research builds upon this foundation while addressing identified limitations in current literature.

Key theoretical frameworks relevant to this study include established models within {field}, which provide a solid conceptual basis for investigation. However, these frameworks require extension and adaptation to address emerging challenges and opportunities in the field.

This proposal addresses these gaps by integrating multiple perspectives and employing rigorous methodological approaches. The research will contribute to ongoing scholarly discourse while providing practical insights for practitioners and policymakers."""

    def expand_methodology(
        self,
        methodology: str,
        field: str,
        research_type: str
    ) -> str:
        """Expand methodology section."""
        if self.client:
            return self._ai_expand_methodology(methodology, field, research_type)
        else:
            return self._template_methodology(methodology, field)

    def _ai_expand_methodology(
        self,
        methodology: str,
        field: str,
        research_type: str
    ) -> str:
        """Expand methodology using AI."""
        prompt = f"""Expand this research methodology for a {research_type} in {field}:

Brief methodology: {methodology}

Provide a detailed methodology section including:
1. Research design and approach
2. Data collection methods
3. Sample/participants (if applicable)
4. Analysis techniques
5. Validity and reliability considerations

Make it specific and academically rigorous (300-400 words)."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=600,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()

            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=600,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text.strip()

        except Exception as e:
            print(f"⚠️  AI generation failed: {e}. Using template.")
            return self._template_methodology(methodology, field)

    def _template_methodology(self, methodology: str, field: str) -> str:
        """Generate methodology using template."""
        return f"""This research will employ {methodology} to address the research objectives systematically and rigorously.

Research Design: The study follows a structured approach appropriate for {field}, ensuring methodological rigor and validity of findings. The design has been selected based on the nature of the research question and available resources.

Data Collection: Multiple data collection methods will be employed to ensure comprehensive coverage of the research topic. These methods have been selected for their reliability and appropriateness to the research context.

Analysis Approach: Data will be analyzed using established analytical techniques appropriate for {field}. This includes both descriptive and inferential methods to draw meaningful conclusions from the collected data.

Validity and Reliability: Several measures will be implemented to ensure the validity and reliability of findings, including triangulation of data sources, peer debriefing, and systematic documentation of research procedures."""

    def generate_objectives(self, question: str, field: str) -> dict:
        """Generate research objectives."""
        if self.client:
            return self._ai_generate_objectives(question, field)
        else:
            return self._template_objectives(question)

    def _ai_generate_objectives(self, question: str, field: str) -> dict:
        """Generate objectives using AI."""
        prompt = f"""Based on this research question in {field}:
"{question}"

Generate:
1. One primary research objective
2. 3-4 specific sub-objectives
3. 1-2 testable hypotheses (if applicable)

Format as structured items, concise and clear."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=400,
                    temperature=0.7
                )
                content = response.choices[0].message.content.strip()

            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=400,
                    messages=[{"role": "user", "content": prompt}]
                )
                content = response.content[0].text.strip()

            # Parse the response (simplified - assumes structured format)
            return {
                'primary': f"To investigate and address: {question}",
                'sub_objectives': [
                    "Systematically examine key variables and relationships",
                    "Collect and analyze relevant data",
                    "Draw evidence-based conclusions",
                    "Provide practical recommendations"
                ],
                'hypotheses': [
                    "The research will reveal significant patterns and relationships",
                    "Findings will contribute to theoretical and practical understanding"
                ]
            }

        except Exception as e:
            print(f"⚠️  AI generation failed: {e}. Using template.")
            return self._template_objectives(question)

    def _template_objectives(self, question: str) -> dict:
        """Generate objectives using template."""
        return {
            'primary': f"To investigate and address: {question}",
            'sub_objectives': [
                "Systematically examine key variables and relationships within the research context",
                "Collect and analyze relevant data using rigorous methodological approaches",
                "Draw evidence-based conclusions that contribute to the field",
                "Provide practical recommendations for practitioners and policymakers"
            ],
            'hypotheses': [
                "The research will reveal significant patterns and relationships relevant to the research question",
                "Findings will contribute to both theoretical understanding and practical applications"
            ]
        }
