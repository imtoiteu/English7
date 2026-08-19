# -*- coding: utf-8 -*-
"""Human-readable titles for the recordings (page titles are unreliable for ELLLO)."""
import re

SG_TITLES = {
 "A1-13-Months": "Months of the year",
 "A1-16-Prepositions": "Prepositions of place",
 "A1-18-Nationalities": "Languages and nationalities",
 "A1-19-Can-Abilities": "Can — talking about abilities",
 "A1-20-Adverbs-Frequency": "Adverbs of frequency",
 "A1-24-Articles": "Articles: a / an / the",
 "A1-25-Any-Some": "Some and any",
 "A2-01-Present-Simple": "The present simple",
 "A2-03-Present-Continuous": "The present continuous",
 "A2-04-Will": "Will — predictions and promises",
 "A2-05-Going-To": "Going to — plans people have made",
 "A2-06-Past-Tense-Ed": "The past simple: -ed verbs",
 "A2-07-Past-Tense-Irregular": "The past simple: irregular verbs",
 "A2-08-Adjectives": "Adjectives and adverbs of degree",
 "A2-09-Comparatives": "Comparatives",
 "A2-10-Superlatives": "Superlatives",
 "A2-12-May-Might": "May and might",
 "A2-13-Connectors": "Connectors: but, so, because",
 "A2-14-Present-Continuous-Future": "The present continuous for future arrangements",
 "A2-17-Imperatives": "Imperatives",
 "A2-19-Expressing-Similarity": "Also, as well, too",
 "A2-22-Determiner-Nouns": "Determiners and plural nouns",
 "A2-23-Much-Many": "Much and many",
 "B1-07-Present-Perfect-Experience": "The present perfect: ever and never",
 "B1-08-Have-to-Must-Obligation.": "Have to and must — obligation",
 "B1-10-First-Conditional": "The first conditional",
}

OME_FIX = {
 "What will you this month?": "What will you do this month?",   # typo on the source page
}

def clean(kind, slug_title, page_title):
    """Return the title to print in the books."""
    if kind == "VOA":
        return (page_title or slug_title).replace("  ", " ").strip()
    if kind == "SG":
        return SG_TITLES.get(slug_title, re.sub(r'^[AB][12]-\d+-', '', slug_title).replace('-', ' '))
    # One Minute English: "Beginner English - #43 - What are monthly events...?"
    t = re.sub(r'^Beginner English\s*-\s*#?\d+\s*-\s*', '', page_title or '').strip()
    t = OME_FIX.get(t, t)
    return t or re.sub(r'^[AB][12]-\d+-', '', slug_title).replace('-', ' ').title()
