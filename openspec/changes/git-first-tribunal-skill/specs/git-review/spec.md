## ADDED Requirements

### Requirement: Durable exclusive claims
The skill SHALL publish state only through a non-forced push based on the observed private state-ref head. A worker SHALL NOT act without confirmed claim publication and current actor/fence/lease.

#### Scenario: Concurrent claims
- **WHEN** two workers mutate the same observed head
- **THEN** at most one push succeeds and the loser reports a conflict rather than ownership.

### Requirement: Conditional follow-up
The skill SHALL retain all conditions by stable IDs and SHALL reject stale review packets after target changes.

#### Scenario: Fix and re-review
- **WHEN** a conditional candidate is changed
- **THEN** its next review requires the new commit, current evidence and fresh reviewer confirmations; old GO cannot be transferred.

### Requirement: Honest evidence and authority
A GO SHALL require complete configured criteria and reviewers, no hard veto, no missing evidence and no unresolved condition. GO SHALL NOT itself authorize a production side effect.

#### Scenario: Fixture evidence
- **WHEN** deterministic fixture reviews pass
- **THEN** receipts retain fixture mode and action_authorized=false; no live model review is claimed.

### Requirement: Host-driven discovery
The skill SHALL discover explicitly routed local tickets and all pages of approved GitHub issues. Source access failures SHALL remain blocked.

#### Scenario: Missing host scheduler
- **WHEN** the repository is merely opened without a host invoking its entry hook
- **THEN** no unattended heartbeat execution is claimed.
