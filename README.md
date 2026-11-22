

# Generative Meal Planner & Pantry Diffing Grocery list

A structured meal planning and grocery optimization application built with Python, Streamlit, Pydantic, and the Google Gemini API. 

Designed to generate tailored meal plans in controlled batches, track pantry inventory locally to cut redundant grocery purchases, and estimate local store pricing on confirmed meal plans

## Live Demo & Quick Access

- **Hosted App:** [Insert Hosted App URL]
- **Scan to Open on Mobile:**

![App QR Code](./assets/qr-code.png)

*(Note: Will update link and QR code once `v1.0` is deployed.)*

---

## The Problem & Project Construction Approach 

Most AI recipe tools suffer from three common issues: `unstructured text outputs that break UI rendering`, `duplicate suggestions / meals`, and `prompts that waste tokens` by repeatedly recalculating ingredients and store prices before the user has even finalized their meals. 

This project aims to solve those problems through a structured pipeline:

1. **Predictable and Filtered AI Responses (Pydantic):** All Gemini responses are validated with strict Pydantic schemas (Title, Description, Metadata, Ingredients, and Instructions) so the frontend receives reliable JSON structures rather than free-form text or half-half responses.

2. **Batch Generation & Anti-Duplicate Context:** Instead of requesting a massive plan in one prompt, meals are generated in controlled batches (e.g., 3 to 5 meals per call). Follow-up requests ("Keep these, add more") pass existing meal names back into the context to prevent duplicate recipes.
  
(Due to inconsistency with Gemini, it is better to use multiple calls because it reduces the chances of having errors within JSON files, eliminates the potential for character response limits- which cut JSON files off halfway and break the program- and reduces potential for unwanted token costs)

3. **Unique ID State & Two-Step Deletion:** Every generated meal is assigned a unique identifier (`UUID` / index) in the master state store rather than relying on meal names. Users can toggle meal visibility or permanently remove meals using a two-step confirmation guard that prevents accidental deletions across Streamlit reruns.

4. **Standardized Pantry Presets & Client-Side Diffing:** Users log pre-owned pantry items using a searchable `master ingredient list`, preset `unit` selectors, and `quantity` inputs rather than free-text entry. Because both user inventory and Gemini's Pydantic schemas share the exact same standardized ingredient names and units, the app subtracts existing pantry quantities locally with zero string-parsing mismatches—requesting or pricing only net-needed ingredients.
   *(Additionally, users can optionally instruct the generator to `prioritize pre-owned ingredients` to minimize food waste and reduce grocery trips.)*
  
5. **Two-Stage Pricing Separation (`v2.0`):** Location lookup and local store pricing run in a separate pass (`Context 2`) *after* the user has edited and confirmed their final meal list, avoiding wasted API tokens on discarded recipes.

---

## System Architecture

```text
[User Inputs & Pantry Stock]
           │
           ▼
[Context 1: Batch Meal Generator] ──► Gemini API + Pydantic Schema Validation
           │
           ▼
[Master Meal State (Unique IDs)] ──► Toggle / Two-Step Delete / Add More (Anti-Dup)
           │
           ▼
[Local Pantry-Diffing Engine]    ──► Subtracts Pre-Owned Inventory
           │
           ▼
[Net Shopping List]              ──► (v2.0) Context 2: Location & Store Pricing Pass


```
***

**Tech Stack and Planned Architecture**

(v0.1 – v2.0): Python, Streamlit, Pydantic, Google Gemini API

(v2.1 – v3.0): FastAPI (decoupled REST backend), React Native / Expo (cross-platform mobile client)
***

Version Roadmap & Progress

***

PHASE 1:

Core Streamlit Prototype (v0.0.1 – v1.0 MAJOR)

- [X] v0.0.1: GitHub `README.md` and initial setup files are created. `README.md` has all planned and intended features listed in a clean format for readers. 

- [ ] v0.1: Streamlit layout, `st.session_state` setup, and sidebar controls (`meal count`, `diet`, `allergies`, `notes`)

- [ ] v0.2: Searchable preset ingredient catalog (`constants.py`), unit selectors, and pre-owned pantry inventory UI

- [ ] v0.3: Batch sizing and deletion count logic + UI integration

- [ ] v0.4: Gemini API integration and base prompt context

- [ ] v0.5: Anti-duplicate batch context for follow-up meal generation

- [ ] v0.6: Pydantic schemas for strict structured JSON validation

- [ ] v0.7: Unique ID assignment and master state store

- [ ] v0.8: Formatted `meal cards`, `visibility` toggles, two-step `delete confirmation`, and "keep these, add more" workflow

- [ ] v0.9: Client-side pantry-diffing engine and live-syncing shopping list

- [ ] v1.0: End-to-end polish, hosted deployment, and QR code integration, Update `README.md`

***
Phase 2: Location, Pricing & Budget Optimization 

(v1.1 – v2.0 MAJOR) (subject to change at a later date)

- [ ] v1.1 – `Location`/store inputs

- [ ] v1.2 – Confirmed state snapshot serializer (probably in JSON format)

- [ ] v1.3 – Pricing Pydantic schema

- [ ] v1.4 – Context 2 pricing pass

- [ ] v1.5 – Re-pricing diff rules

- [ ] v1.6 – `Budget cap` alerts

- [ ] v1.7 – Store grouping dropdowns

- [ ] v1.8 – Base unit conversions (auto-converting compatible scales like `g` ↔ `kg` and `ml` ↔ `L` during diffing)

- [ ] v1.9 to v2.0 – `local pricing` check and full polish, finish unfinished ideas and clean up all known errors in subversions (ie `v1.9.1, 1.9.2`...)

- [ ] v2.0 MAJOR: Full Polish + Release 

***

Local Setup & Installation

Steps are as follows 

Clone the repository

Bash
```
git clone https://github.com/nschulz331/Meal-Planning-App.git

cd Meal-Planning-App
```
Create and activate a virtual environment:

Bash
```
python -m venv venv

source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:

Bash
```
pip install -r requirements.txt
```
Configure environment variables:

Create a .env file or .streamlit/secrets.toml in the root directory and add your API key:

Code snippet
```
GEMINI_API_KEY="your_api_key_here"
```

(You could alternatively drop this into bash for a one-time test on your local host)

Run the application:

Bash
```
streamlit run streamlit_app.py
```

