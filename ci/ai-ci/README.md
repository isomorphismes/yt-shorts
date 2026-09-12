# ai-ci consumer policy

`suite.tsv` is the first repository consumer of the deterministic kernel from
`isomorphisms/ai-ci`. The workflow pins that kernel by full commit SHA.
This first integration is deliberately scoped to `.github/workflows/youtube-smoke.yml`;
the separate publish-capable upload workflow is not part of this suite.

The consumer regression harness mutates this repository's own workflow,
release fixture, scripts, and evaluation manifest. It requires the first
failure to match the declared diagnostic:

| Escaped-defect case | Required diagnostic |
| --- | --- |
| mutable `actions/checkout` tag | `YT-SMOKE-ACTION-PIN` |
| release changes omitted from workflow paths | `YT-SMOKE-PATH-COVERAGE` |
| Grease invocation hidden in a multiline block | `YT-GREASE-INVOCATION` |
| `.ysh` file with a shell shebang | `YT-GREASE-SHEBANG` |
| POSIX string trap rejected by real YSH | `YT-POSIX-TRAP-BRAND` |
| voiceover drift from the canonical script | `YT-NARRATIVE-SCRIPT-VOICEOVER` |
| blank provenance-history field | `YT-PROVENANCE-FIELDS` |
| incomplete evaluation-manifest row | `YT-EVAL-CASES-FIELDS` |

These static contracts do not replace executable checks. In particular,
`ci/short_release_check.ysh` still owns URL and license validation, description
attribution, and render-input hashes. The uploader still owns video decoding,
shape, duration, metadata, credentials, and the network operation. Media
composition tests still own pixel and output-video behavior. A schema-valid
evaluation manifest also does not prove that its declared oracle is sound.
