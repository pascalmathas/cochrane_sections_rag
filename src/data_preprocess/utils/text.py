import ast
import re

_junk_stopwords = {
    "about",
    "above",
    "after",
    "again",
    "against",
    "all",
    "also",
    "although",
    "among",
    "and",
    "another",
    "any",
    "are",
    "around",
    "because",
    "been",
    "before",
    "being",
    "below",
    "between",
    "both",
    "but",
    "can",
    "cannot",
    "could",
    "did",
    "does",
    "doing",
    "done",
    "down",
    "during",
    "each",
    "either",
    "ever",
    "every",
    "few",
    "for",
    "from",
    "further",
    "had",
    "has",
    "have",
    "having",
    "here",
    "how",
    "however",
    "including",
    "into",
    "its",
    "itself",
    "just",
    "less",
    "like",
    "many",
    "may",
    "might",
    "more",
    "most",
    "much",
    "must",
    "near",
    "nearly",
    "neither",
    "never",
    "nor",
    "not",
    "now",
    "often",
    "once",
    "only",
    "other",
    "others",
    "our",
    "ours",
    "ourselves",
    "out",
    "over",
    "own",
    "same",
    "should",
    "since",
    "some",
    "somewhat",
    "still",
    "such",
    "than",
    "that",
    "the",
    "their",
    "theirs",
    "them",
    "themselves",
    "then",
    "there",
    "these",
    "they",
    "this",
    "those",
    "through",
    "thus",
    "too",
    "under",
    "until",
    "upon",
    "very",
    "was",
    "were",
    "what",
    "when",
    "where",
    "whether",
    "which",
    "while",
    "who",
    "whom",
    "whose",
    "why",
    "will",
    "with",
    "within",
    "without",
    "would",
    "yet",
    "you",
    "your",
    "yours",
    "yourself",
    "yourselves",
}


def _content_words(text):
    return [
        w
        for w in re.findall(r"[a-z][a-z\-]+", text.lower())
        if len(w) > 3 and w not in _junk_stopwords
    ]


def is_alignment_junk(insert_text):
    t = insert_text.strip()
    if not t:
        return True
    if t[0] in ")]}.,":
        return True
    if t.count(")") > t.count("("):
        return True
    if t.count("]") > t.count("["):
        return True
    if len(_content_words(t)) < 2:
        return True
    return False


def parse_simple(val):
    if isinstance(val, list):
        return val
    if isinstance(val, str):
        try:
            parsed = ast.literal_eval(val)
            if isinstance(parsed, list):
                return parsed
        except (ValueError, SyntaxError):
            pass
    return []
