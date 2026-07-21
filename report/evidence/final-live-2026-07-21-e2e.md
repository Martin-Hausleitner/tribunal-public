# Final live source, build, install, and E2E proof, 2026-07-21

All commands ran from the repository root unless the section explicitly says they ran from `/tmp`. No mock response was used. The bundled `local-rules` runs exercised the actual package implementation, and the installed evidence-backend driver parsed the real current GitHub snapshot before returning bounded backend results.

## Source-tree surfaces

### Three primary modes

`python examples/phase1_core_modes.py` exited `0` and executed `knowledge`, `critique`, and `ui_ux` with hard minimums. Each mode produced six isolated views over two effective rounds, the expected mode/persona routing, explicit gaps, `post-hoc-synthesis`, structural `40/100`, and `⚠️`.

The UI/UX output explicitly required viewport, interaction, accessibility, and repeated-use evidence rather than converting text inspection into a visual pass. The critique and knowledge outputs retained the structural-versus-semantic boundary. The Karpathy-inspired view serialized the non-endorsement/non-impersonation disclaimer.

### Concrete comparison case

The source command was:

```bash
python tribunal.py \
  --mode comparison \
  --rounds 2 \
  --hardness hard \
  --target "Decide whether to retain the dependency-free Codex Tribunal contract while composing established OSS for adversarial CI, semantic metrics, production orchestration, and observability; preserve every evidence gap." \
  --notebooklm-url https://notebooklm.google.com/notebook/80cffd38-0185-4f4d-ae00-bbc67c4bc515 \
  --json
```

Observed: exit `0`; comparison mode; requested/effective rounds `2/2`; six isolated views; `local-rules`/`builtin-local`; all view scores `50`; two evidence gaps per view; `post-hoc-synthesis`; final `50/100`; marker `⚠️`. The second gap correctly states that the local backend did not query NotebookLM and that the URL is provenance only.

`python examples/e2e_demo.py` also exited `0` on the repository's documented comparison example.

### Unit and compile gates

- `python -m unittest discover -s tests -v`: exit `0`; `18` tests passed in `0.237s`.
- `python -m py_compile tribunal.py personas/__init__.py scripts/csv_gate.py scripts/report_gate.py scripts/skill_gate.py tests/test_tribunal.py examples/e2e_demo.py examples/phase1_core_modes.py`: exit `0`.

The tests cover all three modes, per-view backend calls, Markdown/JSON behavior, hardness, capacity, failure closure, personas, provenance, NotebookLM URL validation, the `40/50` structural ceiling, unanimous gap-free marker rules, and operator-friendly CLI errors.

## Fresh distribution build

Build root: `/tmp/tribunal-final-live.SxGg9M`

`python -m build --outdir /tmp/tribunal-final-live.SxGg9M/dist` created an isolated PEP 517 environment, built the sdist, then built the wheel from that sdist, exit `0`.

- Wheel: `codex_tribunal-1.0.0-py3-none-any.whl`
- Wheel SHA-256: `a13a1cde76f6be99eaa0f13da3f1d5510bf538fdac71ef30b94586049d132ad0`
- Sdist: `codex_tribunal-1.0.0.tar.gz`
- Sdist SHA-256: `d2326911c846b201534e66b2705f95545dc29a826bf4d00995b2579c4a5edcc6`

The wheel contained `17` entries: `tribunal.py`, console/distribution metadata, the MIT license, `personas/__init__.py`, and all nine persona JSON files. The sdist also contained README, project metadata, source, tests, and persona data.

## Clean installation and installed CLI

The wheel was installed with `--no-deps` into `/tmp/tribunal-final-live.SxGg9M/venv`, exit `0`. Checks then ran from `/tmp`, outside the repository.

- Installed distribution version: `1.0.0`.
- Imported module: `/tmp/tribunal-final-live.SxGg9M/venv/lib/python3.12/site-packages/tribunal.py`.
- Installed persona count: `9`.
- Karpathy references remained the three bare public repositories `llama2.c`, `minGPT`, and `micrograd`.
- The synthetic neither-authored-nor-endorsed/non-impersonation disclaimer survived installation and JSON loading.

The installed `tribunal` console executed a two-round hard comparison case, exit `0`. Reduced observations were: six views; six unique persona slots across the two rounds; backend/engine `local-rules`; score set `{50}`; gap-count set `{2}`; `post-hoc-synthesis`; final `50`; marker `⚠️`; and the serialized Karpathy disclaimer.

## Installed Python API with actual frozen evidence

A `VerifiedPrimaryEvidenceBackend` driver imported the installed wheel, parsed `/home/coder/tribunal-public/report/evidence/github-snapshot.json`, required snapshot `2026-07-21T00:53:15Z`, required all `11` primary repository records, and required star points to equal zero. It then executed the installed API separately for:

```text
knowledge: views=3 score=82 marker=⚠️ debate=post-hoc-synthesis backends={'verified-primary-evidence'}
critique: views=3 score=82 marker=⚠️ debate=post-hoc-synthesis backends={'verified-primary-evidence'}
ui_ux: views=3 score=82 marker=⚠️ debate=post-hoc-synthesis backends={'verified-primary-evidence'}
```

Each backend view recorded the frozen snapshot/count and its isolated coordinate. Each deliberately retained one gap: this driver proves installed orchestration and frozen metadata parsing, not semantic winner quality or visual accessibility. The warning marker therefore remained truthful despite an average above 80.

## Expected-error surfaces

All three installed-console failures emitted one concise `tribunal: error:` message, no traceback, and exit `2`:

| Case | Observed message |
|---|---|
| Empty target | `target must be a non-empty string` |
| `--rounds 0` | `rounds must be >= 1` |
| `TRIBUNAL_ENGINE_QUOTAS_JSON={"local-rules":0}` | `configured engine capacity exhausted after 0 judge(s)` |

An earlier direct invalid-persona control likewise returned exit `2`, no traceback, and all unknown slugs. Current source builds every requested panel before engine allocation or backend evaluation, so it produced no partial judge side effect.

## Artifact gates

- `skill_gate.py`: pass.
- `csv_gate.py`: pass; `11` rows, one crown, score range `53..85`, snapshot `2026-07-21T00:53:15Z`.
- `report_gate.py`: pass; canonical NotebookLM URL, `11` matrix repositories, one crown.
- Strict current OpenSpec validation: pass.
- JSON parser and JSON/CSV/report consistency checks: pass.

## Independent post-reconciliation repeat

After restoring the judge packet to its accepted SHA-256, the root pass independently repeated every executable surface against the resulting checkout:

- Three-mode example: exit `0`; each mode produced six views over two hard-minimum rounds, structural `40/100`, explicit gaps, `post-hoc-synthesis`, and `⚠️`.
- Concrete source comparison with the canonical NotebookLM URL: exit `0`; six views, `local-rules`/`builtin-local`, two gaps per view, `50/100`, and `⚠️`.
- Unit discovery: `18/18` passed in `0.267s`; compile and both examples exited `0`.
- Skill, CSV, report, and strict current OpenSpec gates all passed.

A second isolated build at `/tmp/tribunal-final-live-RYNaTR` produced:

- wheel SHA-256 `e61cef19e810e01af802b3c3babb7e2ba0cc1a60750f5caa3ccf03cb1f0cae8a`;
- sdist SHA-256 `0ad6d87f8d51f0d9e5069da2e40c9c48bccd3da5e0ace2b614cb08d07becd187`;
- the same `17` wheel entries, including source, license, console metadata, `personas/__init__.py`, and all nine JSON personas.

That exact wheel installed with `--no-deps` into a fresh venv. From an outside directory, the installed console returned the expected six-view comparison summary, and the module resolved to `/tmp/tribunal-final-live-RYNaTR/venv/lib/python3.12/site-packages/tribunal.py`. Version `1.0.0`, nine personas, all three Karpathy repository URLs, and the synthetic disclaimer were observed directly.

The installed API then used a real `github-rest-evidence` backend, not a canned mock. The driver performed a live HTTPS request to `https://api.github.com/repos/Martin-Hausleitner/tribunal-public`, received HTTP `200`, verified repository identity and `archived=false`, and supplied that primary metadata independently to three judge requests. Observed result: three distinct persona views, six evidence items per view after orchestrator provenance, one explicit semantic-proof gap per view, `post-hoc-synthesis`, `82/100`, and truthful `⚠️`.

Five installed-console invalid cases were observed: empty target, zero rounds, missing quota file, placeholder NotebookLM URL, and unknown persona. Every case returned exit `2`, one concise `tribunal: error:` line, and no traceback.

The repeat confirms that the earlier frozen-snapshot backend and the later live GitHub REST backend both exercise the real installed `JudgeBackend` seam while retaining an honest gap. Neither is a claim of semantic target verification.

## Honest proof boundary

This E2E establishes source behavior, package build/content, clean installation, console/API usability, persona data/disclaimer survival, expected failure handling, stable provenance, and truthful warning behavior. It does not establish semantic target correctness, live provider-family independence, actual NotebookLM retrieval by the core, durable quota enforcement, production tracing, prompt-injection resistance, visual accessibility, or human task success.
