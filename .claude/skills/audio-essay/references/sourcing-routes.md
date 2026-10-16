# Sourcing routes from the cloud environment

Tested 16 Oct 2026 from the Routine's environment (same egress, same proxy).
Hosts change; when a route below fails or a dead one revives, say so in the
log's Traps line and update this file with the date. Try each host once and
never retry a refusal in a loop.

The rule this file serves (SCRIPT_STYLE.md, Grounding): a number, date or
quotation that will be spoken comes from text the writer held. A WebFetch or
search summary only says what to fetch.

## Works, no key needed

- **PubMed connector** (attached to the Routine): `convert_article_ids` for
  DOI to PMCID, then `get_full_text_article`. Same coverage as Europe PMC's
  open XML; an empty full_text means a pre-2000 scan, so move on.
- **Europe PMC REST**: search
  `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:<doi>&format=json`,
  then full text `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`.
  A 500 means no licensed XML for that item (every pre-2000 scan, and some
  recent ones); do not retry. Worked for Ramsden 2016, Ioannidis 2005,
  Greenhalgh 2014, Senn 2023, Liu 2020.
- **OpenAlex**: `https://api.openalex.org/works/doi:<doi>` gives
  `best_oa_location` and the PMCID; it misses old scanned items.
- **Crossref**: `https://api.crossref.org/works/<doi>` for bibliographic facts.
- **arXiv**: the API at one request per three seconds (a 429 clears after a
  short wait), and `https://arxiv.org/pdf/<id>` then pdftotext.
- **Direct PDFs**: NBER (`nber.org/system/files/working_papers/wNNNNN/wNNNNN.pdf`),
  gwern.net/doc, author and university pages, curl then `pdftotext -layout`.
- **Internet Archive text**: find the item with
  `https://archive.org/advancedsearch.php?q=<query>&fl[]=identifier&output=json`,
  list files at `https://archive.org/metadata/<id>/files`, fetch the
  `_djvu.txt`. A 401 or 403 means lending-only; stop. Old journal issues are
  often here as OCR text, for example the BMJ 1948 streptomycin paper in
  `sim_british-medical-journal_1948-10-30_2_4582` and Doll and Hill 1950 in
  `sim_british-medical-journal_1950-09-30_2_4682`.
- **Project Gutenberg**: `https://www.gutenberg.org/cache/epub/<N>/pg<N>.txt`
  with `curl -L`.
- **WordPress public API** (Zamishka): see queue.md.

## Scanned PDFs

pdftotext returns nothing for an image-only scan and there is no OCR in the
environment. Download with curl, then read with the Read tool's `pages`
parameter, at most twenty pages per call, only the chapters the episode
needs. Cochrane 1972 (Nuffield Trust PDF, 94 pages) was read this way for 066.
The James Lind Library's page images load when the request carries
`Referer: https://www.jameslindlibrary.org/`; the Read tool can view them.

## Dead or walled from this egress (16 Oct 2026)

bmj.com, jamanetwork.com, thelancet.com, pnas.org, science.org,
journals.asm.org, tandfonline.com, journals.sagepub.com,
royalsocietypublishing.org, jstor.org (block page), theatlantic.com,
scholar.archive.org (bot wall), web.archive.org and api.fatcat.wiki
(connection reset), Semantic Scholar search (rate-limited), europepmc.org's
website and its PDF renderer (the REST API works), pmc.ncbi.nlm.nih.gov PDFs
(reCAPTCHA; the HTML is intermittent, one attempt only). A 200 can still be a
block page, so check the title and word count of what came back.

## Evidence series anchors (067-074)

Reachable in full text: Snow 1855 and Semmelweis 1861 (archive.org text);
Fisher, The Design of Experiments (archive.org, in.ernet.dli.2015.199572); the
1948 MRC streptomycin paper and Doll and Hill 1950 (archive.org BMJ issues
above); WHI 2002 (escholarship.org, qt3mr6f93p); Gigerenzer 2004, Mindless
Statistics (library.mpib-berlin.mpg.de); the ASA 2016 statement (amstat.org);
Ioannidis 2005 and Greenhalgh 2014 (Europe PMC XML).
Closed: ISIS-2 (Lancet 1988), Guyatt et al. 1992 (JAMA), Hill 1965, Hill 1990,
Hernán et al. 2008. For these, write from open restatements and the reception
pass, say in the sentence that a figure comes from a secondary account, and
log the gap.
