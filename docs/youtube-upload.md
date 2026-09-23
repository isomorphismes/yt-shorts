# YouTube upload CI

The repository uploads rendered Shorts through the YouTube Data API `videos.insert` endpoint. The workflow uses Grease (`isomorphisms/grease`, including its pinned Oils-derived source) for the command steps and for `ci/youtube_upload.ysh`.

There is no separate Shorts upload endpoint. Upload a normal video; YouTube classifies square or vertical videos of at most 3 minutes as Shorts. The Grease uploader rejects landscape videos and videos longer than 180 seconds before making a network request.

Push and pull-request runs never upload a video; they only exercise the local Grease validation path. Network publishing exists only in the manually dispatched `upload` job.

## One-time Google setup

1. Create or select a Google Cloud project for this uploader.
2. Enable **YouTube Data API v3**.
3. Configure the OAuth consent screen.
4. Create an OAuth client. A Web application client is convenient if using Google's OAuth Playground to obtain the one-time refresh token.
5. If using OAuth Playground with your own client, add this authorized redirect URI to that OAuth client:

   `https://developers.google.com/oauthplayground`

6. In OAuth Playground settings, enable **Use your own OAuth credentials**, set **Access type** to **Offline**, and enter that client ID and client secret.
7. Authorize this scope:

   `https://www.googleapis.com/auth/youtube`

   This single scope covers both video upload and the channel-branding updates in `ci/youtube_brand.ysh`. The narrower `youtube.upload` scope is enough for `videos.insert`, but not for `channels.update`.

8. Exchange the authorization code for tokens and copy the refresh token.

Do not use the Playground's default OAuth credentials for CI: the Playground automatically revokes refresh tokens created with its own credentials after 24 hours. Also note that an OAuth consent screen left in Testing mode can issue refresh tokens that expire after 7 days. A persistent CI credential therefore needs an appropriate production OAuth configuration.

YouTube does not support ordinary service-account authentication for a normal channel upload. The refresh token represents the Google/YouTube channel identity that granted the scope.

If one Google login manages several YouTube channels, authorize each channel identity separately and keep one refresh token per channel. `ci/youtube_check.ysh --channel-id ...` provides a guard against using the wrong credential.

## GitHub Actions secrets

Add these repository Actions secrets:

- `YOUTUBE_CLIENT_ID`
- `YOUTUBE_CLIENT_SECRET`
- `YOUTUBE_REFRESH_TOKEN`

Never commit any of these values.

## Running the workflow

After `.github/workflows/youtube-upload.yml` is on the default branch, open **Actions → YouTube upload → Run workflow**. Run the workflow definition from the default branch and provide:

- `source_ref`: branch, tag, or commit containing the rendered MP4; defaults to `main`, for example use `teleman-wegert-k-loop` for that render branch
- `video_path`: repository-relative path to the MP4 on that ref
- `title`
- `description`
- `privacy_status`: private, unlisted, or public
- `category_id`: defaults to 27 (Education)
- `made_for_kids`: explicit true/false declaration
- `publish`: leave false for validation only; set true to actually upload

The first existing render that can use this is:

- `source_ref`: `teleman-wegert-k-loop`
- `video_path`: `teleman-riemann-surface/wegert-k-loop.mp4`

That renderer currently produces a 720x720, 14-second MP4, so it passes the uploader's square/vertical and duration checks.

The workflow always performs a Grease smoke test. The upload job then checks out `source_ref` and validates the selected video's dimensions and duration. With `publish=false`, it stops after printing the metadata. With `publish=true`, it exchanges the refresh token for a short-lived access token, starts a resumable `videos.insert` upload, uploads the MP4, and records the resulting YouTube video ID and URL in the Actions summary.

## Private-only API projects

YouTube currently restricts uploads from unaudited API projects created after July 28, 2020 to private viewing. OAuth authorization can therefore succeed while a requested `public` or `unlisted` upload remains private. Lifting that restriction requires the YouTube API project's compliance audit.

## Official references

- YouTube Data API `videos.insert`: https://developers.google.com/youtube/v3/docs/videos/insert
- YouTube Data API `channels.update`: https://developers.google.com/youtube/v3/docs/channels/update
- YouTube OAuth: https://developers.google.com/youtube/v3/guides/authentication
- OAuth Playground: https://developers.google.com/oauthplayground/
- Shorts eligibility: https://support.google.com/youtube/answer/15424877
