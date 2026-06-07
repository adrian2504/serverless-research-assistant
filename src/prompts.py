RESEARCH_SYSTEM_PROMPT = """
You are a research assistant for technical papers, academic posters, and slide decks.

Your job:
- Be concise but rigorous.
- Do not invent details.
- If evidence is missing, say "Not specified in the document."
- Separate claims from evidence.
- Prefer structured markdown.
"""


def chunk_summary_prompt(chunk: str, chunk_number: int, total_chunks: int) -> str:
    return f"""
You are reading chunk {chunk_number} of {total_chunks} from a research document.

Extract the most important information from this chunk.

Return markdown with these sections:

## Main Points
- Bullet list

## Claims
- Bullet list of claims made in this chunk

## Methods / Technical Approach
- Bullet list

## Evidence / Results
- Bullet list

## Limitations or Open Questions
- Bullet list

Document chunk:
\"\"\"
{chunk}
\"\"\"
"""


def final_brief_prompt(chunk_summaries: str) -> str:
    return f"""
You are given summaries from chunks of a research document.

Create a polished research brief in markdown.

Use this exact structure:

# Research Brief

## 1. One-Sentence Summary
One sentence only.

## 2. Problem
What problem is the work trying to solve?

## 3. Core Idea
What is the main idea or proposed solution?

## 4. Key Claims
List the main claims.

## 5. Methodology
Explain the method, system, experiment, or analysis.

## 6. Evidence and Results
What evidence supports the claims?

## 7. Limitations
What are the weaknesses, missing details, or risks?

## 8. Future Work
What should be explored next?

## 9. Why This Matters
Explain why this work is useful.

## 10. 5-Minute Presenter Notes
Create short notes someone could use to explain this paper in a video.

Important:
- Do not hallucinate.
- If something is not present, say "Not specified in the document."
- Keep the language clear and technical.

Chunk summaries:
\"\"\"
{chunk_summaries}
\"\"\"
"""


def qa_prompt(question: str, context: str) -> str:
    return f"""
Answer the user's question using only the document context below.

If the answer is not in the context, say:
"I could not find this in the uploaded document."

Question:
{question}

Document context:
\"\"\"
{context}
\"\"\"

Return a clear answer in markdown.
"""