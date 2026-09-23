# YouTube channel branding

`ci/youtube_brand.ysh` is the Grease/YSH path for reusing the same profile/header art on YouTube without living in YouTube Studio.

## Source art

Keep one canonical copy of the art and point the script at it. For example:

```sh
ci/youtube_brand.ysh \
  --header branding/twitter-header.png \
  --profile branding/twitter-profile.png
```

The default is preparation only; it makes no network request. It writes:

- `branding/generated/youtube-banner.jpg` at 2560x1440
- `branding/generated/youtube-profile.jpg` at 800x800 when `--profile` is supplied

For the banner, the whole source header is kept inside YouTube's 1235x338 center safe area. The rest of the 2560x1440 canvas is a blurred copy of that same header, so no separate artwork has to be maintained.

## Apply the banner

The banner can be uploaded and assigned entirely through the YouTube Data API:

```sh
ci/youtube_brand.ysh \
  --header branding/twitter-header.png \
  --profile branding/twitter-profile.png \
  --channel-id UCxxxxxxxxxxxxxxxxxxxxxx \
  --apply
```

The script:

1. generates the YouTube-sized assets;
2. exchanges `YOUTUBE_REFRESH_TOKEN` for a short-lived access token;
3. resolves the authenticated channel and refuses to continue if `--channel-id` does not match;
4. uploads the banner with `channelBanners.insert`;
5. preserves the channel's existing mutable branding fields; and
6. assigns the returned banner URL with `channels.update`.

The environment variables are the same ones used by the uploader:

- `YOUTUBE_CLIENT_ID`
- `YOUTUBE_CLIENT_SECRET`
- `YOUTUBE_REFRESH_TOKEN`

The refresh token must include `https://www.googleapis.com/auth/youtube`; the narrower `youtube.upload` scope cannot update channel branding.

## Profile picture limitation

The YouTube Data API does not expose a method for replacing a channel's profile picture. `youtube_brand.ysh` therefore prepares the square image, but installing it remains a one-time manual channel-creation/setup step.

The profile can still be checked afterward because `channels.list` returns the channel thumbnail URLs.

## Check the channel

```sh
ci/youtube_check.ysh --channel-id UCxxxxxxxxxxxxxxxxxxxxxx
```

This prints the channel title, channel ID, handle when returned, current profile image URL, current banner URL when returned, uploads playlist, and made-for-kids status.

To verify a particular upload with the same credential:

```sh
ci/youtube_check.ysh \
  --channel-id UCxxxxxxxxxxxxxxxxxxxxxx \
  --video-id VIDEO_ID
```

For several channels under one Google login, keep one refresh token per channel identity and use the channel-ID assertion as the guardrail against publishing or branding the wrong channel.

## Official references

- Channel banner upload: https://developers.google.com/youtube/v3/docs/channelBanners/insert
- Channel metadata update: https://developers.google.com/youtube/v3/docs/channels/update
- Channel lookup: https://developers.google.com/youtube/v3/docs/channels/list
