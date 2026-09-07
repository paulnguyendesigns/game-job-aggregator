# Contributing

Thanks for considering a contribution! This project is a portfolio/learning project as well as a functional tool, so clarity is valued as much as correctness.

## Adding a company

1. Confirm the company actually exposes a **public** job board API (Greenhouse, Lever, or Ashby) or a documented public JSON endpoint. Do not guess an identifier.
2. Add an entry to the company configuration (introduced in Phase 2) with the verified `source` type and `identifier`.
3. Open a PR. No code changes should be required to add a company that uses an already-supported source type.

## Adding a new source type

1. Implement the `JobSource` interface (introduced in Phase 2) in `src/sources/`.
2. Your adapter must return a list of normalized `Job` objects — never raw API responses.
3. Add unit tests using fixture data (do not hit the live API in tests).

## Code style

- Type hints on all function signatures.
- Docstrings on public functions/classes.
- Small, single-purpose functions over large ones.
- No hardcoded credentials or API keys, ever.

## Running tests

```bash
pytest
```

## Reporting a data-quality issue

If you spot a listing that's wrong, expired, or not actually game-related, please open an issue with the job `id` from `internships.json` and a short description of the problem.
