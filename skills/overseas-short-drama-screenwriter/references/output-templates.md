# Output Templates

Use these templates to keep long projects consistent.

## 1. Market Intelligence Summary

```text
# Market Intelligence

Target country:
Target language:
Target audience:
Research date:
Research window:
Platforms / sources checked:

## Current leaders
- ...

## Repeated genres / tropes
- ...

## Repeated relationship patterns
- ...

## Primary emotional promises
- ...

## Rising signals
- ...

## Saturated signals
- ...

## Opportunity gaps
- ...

## Local cultural notes
- ...

## Recommended creative directions
1. ...
2. ...
3. ...

Confidence / limitations:
...
```

## 2. Creative Brief

```yaml
creative_brief:
  target_country:
  target_language:
  target_platform:
  target_audience:
  genre:
  subgenre:
  tone:
  primary_emotion:
  secondary_emotion:
  audience_fantasy:
  current_market_signal:
  saturated_elements_to_avoid:
  opportunity_gap:
  protagonist_type:
  relationship_type:
  external_story_engine:
  differentiation:
  localization_notes:
  production_constraints:
```

## 3. Concept Pool

```text
# IDEA 01
English title:
Chinese title:
Genre:
Logline:
Protagonist:
Central relationship:
External goal:
Core conflict:
Central secret:
Opening hook:
Major reversal:
Emotional promise:
Series engine:
Market reason:
Originality difference:
Localization advantage:
Score: /100

# IDEA 02
...
```

## 4. Selected Project Bible

```text
# PROJECT

English title:
Chinese title:
Target market:
Genre:
Tone:
Episode count:
Episode duration:

# LOGLINE

...

# DRAMATIC QUESTION

...

# THEME QUESTION

...

# AUDIENCE PROMISE

...

# COMPLETE STORY SYNOPSIS

...

# ENDING

...
```

## 5. Character Bible

```yaml
character:
  name:
  age:
  nationality:
  city:
  profession:
  socioeconomic_position:
  public_identity:
  hidden_identity:
  external_goal:
  internal_need:
  fear:
  wound:
  flaw:
  strength:
  secret:
  leverage:
  false_belief:
  contradiction:
  opening_state:
  breaking_point:
  final_choice:
  ending_state:
  arc:
  speaking_style:
```

Repeat for each principal character.

## 6. Relationship Bible

```yaml
relationship:
  character_a:
  character_b:
  surface_relationship:
  hidden_truth:
  what_a_wants:
  what_b_wants:
  attraction_or_dependency:
  power_balance:
  conflict_of_interest:
  unequal_information:
  breaking_point:
  transformation:
  final_state:
```

## 7. Series Story Engine

```text
# Relationship Engine
...

# External Objective Engine
...

# Secret / Information Engine
...

# Antagonist Engine
...

# Why the story can sustain the requested episode count
...
```

## 8. Full-Series Arc

```text
PHASE 1 — Opening disruption
Episodes:
Story function:
Major events:
Relationship state:
Knowledge state:
End turn:

PHASE 2 — Commitment / entrapment
...

PHASE 3 — Escalation
...

PHASE 4 — Major reversal
...

PHASE 5 — Major loss
...

PHASE 6 — Counterattack
...

PHASE 7 — Convergence
...

PHASE 8 — Final choice / climax
...

PHASE 9 — Payoff
...
```

## 9. Episode Map

Use a table or repeated cards:

```yaml
episode:
  number: 1
  title:
  opening_state:
  opening_hook:
  protagonist_goal:
  obstacle:
  key_action:
  escalation:
  reveal_or_reversal:
  emotional_payoff:
  relationship_shift:
  cliffhanger:
  ending_state:
  next_question:
```

## 10. Episode Beat Sheet

```text
# EPISODE XX

Episode purpose:
Opening hook:
Main dramatic question:

Beat 1 — ...
Cause:
Action:
Result:

Beat 2 — ...
Cause:
Action:
Result:

Beat 3 — ...
...

Emotional payoff:
Relationship change:
Ending cliffhanger:
Continuity updates:
```

## 11. Scene List

```yaml
scene:
  id: E01-S01
  slugline:
  characters:
  pov:
  goal:
  opposing_force:
  tactic:
  conflict:
  reveal:
  turn:
  value_before:
  value_after:
  result:
  exit_question:
```

## 12. Full Screenplay — English Master

```text
EPISODE 01

INT. LOCATION - DAY

Visual action in present tense.

CHARACTER
Dialogue.

CHARACTER
Dialogue.

Action / turn.

CUT TO NEXT SCENE ONLY IF A TRANSITION IS ACTUALLY USEFUL.

INT. NEXT LOCATION - NIGHT

...

END OF EPISODE 01
```

Do not append storyboard prompts or image-generation prompts.

## 13. Chinese Review Version

When the user needs Chinese review support, provide either:

### Option A — Full Chinese screenplay version

Mirror the English screenplay scene by scene.

### Option B — Chinese review notes

```text
本集剧情目的：
核心冲突：
关键反转：
情绪回报：
结尾钩子：
英文对白中特别需要理解的潜台词：
本地化说明：
```

The English master remains authoritative for an English-market project unless the user says otherwise.

## 14. Continuity Update

After each episode:

```yaml
continuity_update:
  episode:
  current_time:
  character_locations:
  injuries:
  possessions:
  relationship_changes:
  new_information_by_character:
  secrets_revealed:
  setups_planted:
  setups_paid:
  unresolved_questions:
  legal_or_financial_changes:
  supernatural_rule_changes:
```

## 15. Revision Report

```text
# Revision Report

Overall score: /100

## Strongest elements
- ...

## Weakest elements
- ...

## Structural problems
- ...

## Character problems
- ...

## Episode / retention problems
- ...

## Dialogue problems
- ...

## Localization problems
- ...

## Continuity problems
- ...

## Originality risks
- ...

## Revisions completed
- ...

## Remaining risks
- ...
```

## 16. Final Delivery Package

For a complete project:

```text
01 Market Intelligence Summary
02 Creative Brief
03 Selected Concept
04 Complete Story Synopsis
05 Character Bible
06 Relationship Bible
07 Series Story Engine
08 Full-Series Arc
09 Complete Episode Map
10 Episode Beat Sheets
11 Complete English Master Screenplay
12 Chinese Review Version if requested
13 Continuity Bible
14 Revision / Quality Report
```

If the user explicitly requests only the screenplay, deliver the screenplay without forcing all planning documents into the visible answer.
