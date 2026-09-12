# yt-shorts

Source files and reproducible renders for short-form videos.

Each short lives in its own directory with its sources, narration, and render script.

## Publishing and channel setup

The YouTube automation runs under Grease:

- `ci/youtube_upload.ysh` validates and uploads rendered Shorts.
- `ci/youtube_brand.ysh` turns the same header/profile source art used elsewhere into YouTube-sized assets and can apply the channel banner through the API.
- `ci/youtube_check.ysh` reports which channel the OAuth token controls, its current profile/banner URLs, and optionally verifies an uploaded video.

Upload CI is documented in [`docs/youtube-upload.md`](docs/youtube-upload.md). Channel branding and the remaining one-time profile-picture step are documented in [`docs/youtube-branding.md`](docs/youtube-branding.md).

The YouTube smoke workflow also runs the pinned `ai-ci` contract kernel from
`ci/ai-ci/suite.tsv`. It adds static rejection of bypassable workflow changes,
language-boundary drift, narrative/provenance mismatch, and incomplete
evaluation manifests. The existing Grease, ffmpeg, ImageMagick, hash, and upload
validation checks are preserved as the executable artifact gates.
