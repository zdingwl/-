# Serial Survival State Template

~~~yaml
serial_survival_state:
  world_phase:
    phase_name:
    absolute_time:
    relative_time:
    functioning_infrastructure:
    failing_infrastructure:
    public_belief:
    actual_threat:
    next_phase_trigger:

  future_knowledge:
    - id:
      event:
      source: personally_witnessed | reliably_confirmed | rumor | inferred
      original_time:
      original_location:
      known_fact:
      unknown_cause:
      confidence: high | medium | low
      actionable_value:
      dependencies_changed: false
      current_reliability: valid | drifting | invalid
      last_checked_at:

  timeline_divergence:
    divergence_score_or_stage:
    changed_events:
    saved_people:
    removed_resources:
    accelerated_threats:
    delayed_threats:
    invalidated_future_knowledge:

  resource_ledger:
    - resource:
      category:
      amount:
      unit:
      storage_location:
      max_capacity:
      daily_consumption:
      resupply_source:
      controller:
      known_by:
      critical_threshold:
      losses:
      last_updated_at:

  capability_ledger:
    - capability:
      unlocked_at:
      source:
      input:
      output:
      limits:
      cost:
      visibility:
      known_by:
      upgrade_path:
      cannot_do:

  secrecy_exposure:
    protagonist_secret:
    public_cover_story:
    confirmed_witnesses:
    suspicious_characters:
    factions_with_evidence:
    current_exposure_level:
    first_public_use:
    consequences_of_exposure:

  opposition_ladder:
    - opponent:
      level:
      goal:
      why_they_notice_protagonist:
      desired_resource_or_secret:
      current_information:
      current_strategy:
      adaptation_to_protagonist:
      damage_already_caused:
      next_escalation:

  open_hooks:
    - id:
      planted_at:
      surface_question:
      hidden_question:
      audience_knows:
      protagonist_knows:
      status: open | partial | paid | abandoned
      planned_payoff:
      payoff_horizon: episode | arc | season | multi_season
      dependency:
      risk_if_revealed_early:

  future_payoffs:
    - setup:
      planted_at:
      apparent_function:
      true_function:
      planned_payoff:
      target_episode_or_season:
      prerequisites:

  season_residue:
    resolved_this_season:
    intentionally_unresolved:
    changed_world_rules:
    next_season_pressure:
    multi_season_mysteries:
~~~
