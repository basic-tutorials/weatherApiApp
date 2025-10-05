"""
AI Content Generator

Generates academic content for research proposals using AI providers.
"""

import os


class AIGenerator:
    """Generate AI-enhanced content for research proposals."""

    def __init__(self, provider: str = 'openai', api_key: str = ''):
        """Initialize AI generator with provider."""
        self.provider = provider
        self.api_key = api_key
        self.client = None

        if api_key:
            self._init_client()

    def enhance_user_input(self, inputs: dict) -> dict:
        """
        Enhance and clean user input using AI before processing.
        This improves quality by fixing capitalization, grammar, and expanding brief inputs.
        """
        enhanced = inputs.copy()

        if not self.client:
            print("⚠️  No API key - using basic text formatting")
            # Even without AI, do basic formatting improvements
            enhanced['research_title'] = self._basic_title_format(inputs['research_title'])
            enhanced['research_question'] = self._basic_question_format(inputs['research_question'])
            enhanced['researcher_name'] = self._basic_name_format(inputs['researcher_name'])
            return enhanced

        print("✨ Enhancing user input with AI...")

        try:
            # Enhance research title
            enhanced['research_title'] = self._enhance_title(inputs['research_title'])

            # Enhance research question
            enhanced['research_question'] = self._enhance_question(inputs['research_question'])

            # Enhance methodology
            enhanced['methodology'] = self._enhance_methodology(inputs['methodology'], inputs['field_of_study'])

            # Enhance expected outcomes
            enhanced['expected_outcomes'] = self._enhance_outcomes(inputs['expected_outcomes'])

            # Fix researcher name
            enhanced['researcher_name'] = self._basic_name_format(inputs['researcher_name'])

            print("✅ Input enhancement complete")
            return enhanced

        except Exception as e:
            print(f"⚠️  AI enhancement failed: {e}. Using basic formatting.")
            # Fallback to basic formatting
            enhanced['research_title'] = self._basic_title_format(inputs['research_title'])
            enhanced['research_question'] = self._basic_question_format(inputs['research_question'])
            enhanced['researcher_name'] = self._basic_name_format(inputs['researcher_name'])
            return enhanced

    def _basic_title_format(self, title: str) -> str:
        """Basic title formatting without AI."""
        if not title or len(title.strip()) < 2:
            return title

        # Convert to Title Case
        title = title.strip()

        # Simple title case with proper handling of common words
        words = title.split()
        formatted_words = []

        # Words that should stay lowercase (unless first word)
        lowercase_words = {'a', 'an', 'and', 'as', 'at', 'but', 'by', 'for', 'in', 'nor', 'of', 'on', 'or', 'so', 'the', 'to', 'up', 'yet'}

        for i, word in enumerate(words):
            if i == 0 or word.lower() not in lowercase_words:
                # Capitalize first letter, keep rest as is (for acronyms like ML, AI)
                if word.isupper() and len(word) <= 3:  # Likely an acronym
                    formatted_words.append(word.upper())
                else:
                    formatted_words.append(word.capitalize())
            else:
                formatted_words.append(word.lower())

        return ' '.join(formatted_words)

    def _basic_question_format(self, question: str) -> str:
        """Basic question formatting without AI."""
        if not question or len(question.strip()) < 2:
            return question

        question = question.strip()

        # Capitalize first letter
        if question[0].islower():
            question = question[0].upper() + question[1:]

        # Ensure it ends with a question mark if it looks like a question
        question_words = ['how', 'what', 'why', 'when', 'where', 'who', 'can', 'does', 'is', 'will']
        if any(question.lower().startswith(word) for word in question_words):
            if not question.endswith('?'):
                question = question.rstrip('.') + '?'

        return question

    def _basic_name_format(self, name: str) -> str:
        """Basic name formatting without AI."""
        if not name or len(name.strip()) < 2:
            return name

        # Title case for names
        name = name.strip()

        # Handle special cases like "dr.", "prof.", etc.
        prefixes = {'dr.': 'Dr.', 'dr': 'Dr.', 'prof.': 'Prof.', 'prof': 'Prof.', 'mr.': 'Mr.', 'ms.': 'Ms.', 'mrs.': 'Mrs.'}

        words = name.split()
        formatted_words = []

        for word in words:
            word_lower = word.lower().rstrip('.')
            if word_lower in prefixes:
                formatted_words.append(prefixes[word_lower])
            else:
                formatted_words.append(word.capitalize())

        return ' '.join(formatted_words)


    def _enhance_title(self, title: str) -> str:
        """Clean and enhance research title."""
        if not title or len(title.strip()) < 3:
            return title

        prompt = f"""Improve this research title to be professional and academic:

Input: "{title}"

Requirements:
- Proper capitalization (Title Case)
- Clear and descriptive
- Academic tone
- Fix any grammar/spelling errors
- Keep it concise (under 15 words)
- DO NOT add quotes or extra formatting

Return ONLY the improved title, nothing else."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=100,
                    temperature=0.3
                )
                result = response.choices[0].message.content.strip().strip('"').strip("'")
                return result if result else title
            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=100,
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.content[0].text.strip().strip('"').strip("'")
                return result if result else title
        except Exception as e:
            print(f"   Title enhancement failed: {e}")
            # Fallback to basic formatting
            return self._basic_title_format(title)

    def _enhance_question(self, question: str) -> str:
        """Clean and enhance research question."""
        if not question or len(question.strip()) < 5:
            return question

        prompt = f"""Improve this research question to be clear and well-structured:

Input: "{question}"

Requirements:
- Proper grammar and punctuation
- Clear and specific
- Academic tone
- Start with question words (How, What, Why, etc.) if appropriate
- Fix capitalization and spelling
- Keep the core meaning

Return ONLY the improved question, nothing else."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                    temperature=0.3
                )
                result = response.choices[0].message.content.strip().strip('"').strip("'")
                return result if result else question
            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=150,
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.content[0].text.strip().strip('"').strip("'")
                return result if result else question
        except Exception as e:
            print(f"   Question enhancement failed: {e}")
            # Fallback to basic formatting
            return self._basic_question_format(question)

    def _enhance_methodology(self, methodology: str, field: str) -> str:
        """Expand and enhance methodology description."""
        if not methodology or len(methodology.strip()) < 10:
            return methodology

        prompt = f"""Expand this brief methodology into a clear, detailed description for a {field} research proposal:

Input: "{methodology}"

Requirements:
- Expand to 3-4 sentences
- Professional academic tone
- Proper grammar and punctuation
- Include specific methods/approaches
- Make it concrete and actionable
- Fix any errors

Return ONLY the enhanced methodology, nothing else."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=250,
                    temperature=0.4
                )
                result = response.choices[0].message.content.strip().strip('"').strip("'")
                return result if result else methodology
            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=250,
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.content[0].text.strip().strip('"').strip("'")
                return result if result else methodology
        except Exception as e:
            print(f"   Methodology enhancement failed: {e}")
            return methodology

    def _enhance_outcomes(self, outcomes: str) -> str:
        """Enhance expected outcomes description."""
        if not outcomes or len(outcomes.strip()) < 5:
            return outcomes

        prompt = f"""Improve this expected outcomes description to be professional and compelling:

Input: "{outcomes}"

Requirements:
- Proper grammar and punctuation
- Professional academic tone
- Clear and specific
- Describe impact and significance
- 2-3 sentences
- Fix any errors

Return ONLY the improved outcomes, nothing else."""

        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=200,
                    temperature=0.4
                )
                result = response.choices[0].message.content.strip().strip('"').strip("'")
                return result if result else outcomes
            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=200,
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.content[0].text.strip().strip('"').strip("'")
                return result if result else outcomes
        except Exception as e:
            print(f"   Outcomes enhancement failed: {e}")
            return outcomes

    def _init_client(self):
        """Initialize AI client."""
        try:
            if self.provider == 'openai':
                from openai import OpenAI
                self.client = OpenAI(api_key=self.api_key)
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
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=500,
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
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=700,
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
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=700,
                    temperature=0.7
                )
                return response.choices[0].message.content.strip()

            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=700,
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
