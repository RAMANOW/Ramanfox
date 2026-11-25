<p align="center"><img src="docs/raman-fox-logo.png" width="128" alt="Raman Fox"></p>

# رامان فاکس · Raman Fox

**VPN رایگان Firefox برای کل گوشی و تلویزیون اندروید.** با حساب Firefox/Mozilla وارد شوید، یک کشور انتخاب کنید و وصل شوید.
**Firefox's free VPN (IP Protection) for your whole Android phone or Android TV.**

> غیررسمی؛ وابسته به Mozilla نیست. حجم ماهانه و حساب Mozilla مسئولیت خود شماست.
> Unofficial. Not affiliated with Mozilla. Your Mozilla account and its monthly data cap are your responsibility.

Based on [Foxhole VPN](https://github.com/Diercohen/foxhole-vpn) by Diercohen (MIT License).
Raman Fox 1.0.0 is Foxhole 1.3.3 with its own name, icon, languages and update channel; the connection code is Foxhole's, unchanged.

## امکانات · Features

- 🔑 ورود با حساب Firefox/Mozilla · sign in with your Firefox (Mozilla) account
- 🌍 همهٔ سرورهای Firefox VPN: آمریکا، آلمان، ژاپن، استرالیا، آرژانتین، آفریقای جنوبی · all Firefox VPN servers (US, DE, JP, AU, AR, ZA)
- 🛡️ VPN برای کل سیستم (همهٔ برنامه‌ها) یا فقط پراکسی SOCKS5/HTTP · whole-system VPN, or proxy only
- ✂️ تفکیک ترافیک (سایت‌ها و برنامه‌ها) · split tunneling by site and app
- 🇮🇷 سایت‌های ایرانی مستقیم، و «صرفه‌جویی در حجم» · Iranian sites direct, and Save data
- 🔎 بررسی «مسدود یا تحریم؟» برای هر سایت · blocked-or-sanctioned check per site
- 📊 مصرف حجم به تفکیک سایت · data by site
- ✈️ تلگرام با یک ضربه · Telegram in one tap
- 📺 تلویزیون اندروید، ورود تلویزیون از روی گوشی، و DNS هوشمند برای تلویزیون/کنسول · Android TV, sign a TV in from a phone, smart DNS
- 🟣 حالت رله (Google Apps Script) برای جاهایی که vpn.mozilla.org مسدود است · relay mode where Firefox VPN is blocked
- 🧮 حالت ماشین‌حساب، کاشی تنظیمات سریع و ویجت · calculator disguise, Quick Settings tile, widget
- 🗣️ فارسی (پیش‌فرض)، کوردی سورانی، English، Русский · Persian (default), Kurdish Sorani, English, Russian

## What Raman Fox changes from Foxhole 1.3.3

- Name «رامان فاکس» / Raman Fox, new launcher icon and TV banner (white fox + R on indigo→cyan), applicationId
  `com.ramanow.ramanfox`, so it installs beside Foxhole and is signed with its own key.
- Persian is the default language; Kurdish Sorani (`gui/renderer/ckb.js`, right to left, Vazirmatn) is added, with
  Persian shown for any text not yet translated into Kurdish.
- Foxhole's name in the UI is shown as Raman Fox (display only: `gui/renderer/app.js` `brandPage`, so every
  translation key and all connection code stay as they are).
- **Foxhole's hot-update channel is switched off** (`src/hot.ts` `HOT_DISABLED`; `hot.json` and `sign-hot.mjs`
  removed): Raman Fox never fetches Foxhole's signed hot.json, so it runs on 1.3.3's built-in Iran fixes.
- **App updates come only from this repo's releases** (`src/ui.ts` `REPO_URL`), looking for `raman-fox-<version>.apk`
  signed with Raman Fox's key; it never downloads Foxhole's APKs.
- The desktop apps and the CLI are still in the tree (Foxhole's), but only the Android app is built and released here.

## Where vpn.mozilla.org is blocked (e.g. Iran)

Set up a **relay**: a free Google Apps Script on your own account. Use
**Settings → VPN relay → Set up step by step** (in the app, or `s` in the TUI);
it shows each click with a screenshot. The relay:

- reaches `vpn.mozilla.org` for foxhole when it's blocked, or refuses your
  country ("VPN not available in this region"): only small control calls,
  your traffic still goes through Firefox VPN. Once connected, even those go
  through the VPN, so the relay only gets the first pass of each connect;
- reaches the server list when it doesn't connect. Mozilla's account server
  (`api.accounts.firefox.com`: the VPN's token, and sign-ins) has turned the
  relay away since 2026-11 (HTTP 406), so where it's blocked, foxhole makes
  each next token through Firefox VPN while it's connected, and a TV or phone
  signed in from another device gets its first token with the sign-in.
  Without a relay, foxhole says which one is blocked and offers the setup; and
- can carry your browsing itself: pick **Relay** at the top of Locations.

**On an Android phone or TV**, make the relay on a computer (Apps Script's setup needs one), then bring it over on
the same Wi-Fi: on the phone or TV, **Settings → VPN relay → Get it from your computer** shows a QR code and a
6-character code; on the computer, or a phone that has the relay, **Settings → VPN relay → Send to a TV or phone**
scans the QR code or takes the code. A TV signed in from a phone or computer (**Settings → Sign in a TV or phone**) gets its
relay with the sign-in, and so does a phone or computer that picks **Sign in from another device** where it asks to sign in;
in the terminal UI, **Settings → Sign in a TV or phone** takes the code and sends both (tab leaves
the relay out), and a TV or phone waiting for a relay alone gets just the relay. On a TV the relay only reaches Mozilla: a TV's apps don't trust relay mode's certificate, so it has
no **Relay** location. iPhones don't have the relay yet.

**Split tunneling → Iranian sites direct** sends Iran's sites around the VPN: by
name (`.ir`, and 57,000 more from [iran-hosted-domains](https://github.com/bootmortis/iran-hosted-domains))
and by address ([Iran's ranges](https://github.com/ipverse/country-ip-blocks)), refreshed weekly through the VPN.
Banks and payment pages work, and that traffic costs Iran's cheaper rate instead of the VPN's data.
**Save data** goes further: every other site is tried directly first, and one that's blocked
(the filter's DNS answer, a reset, silence) goes through the VPN and is remembered for 3 days.
Your provider then sees which sites you visit. Sites that refuse Iranian addresses
([sanctioned](https://github.com/Chocolate4U/Iran-v2ray-rules)) always use the VPN.
On a Mac, Save data works in Proxy only mode.

**Settings → Smart DNS for a TV or console** (desktop app and TUI) makes your computer the DNS server of
the home's other devices: a smart TV, a PlayStation or Xbox, an iPhone. On the device, set DNS by hand to the
address Raman Fox shows. While Raman Fox is connected, a site Iran blocks (the network's DNS answers with the filter's
address, or stops a test handshake with it) or one that refuses Iran ([sanctioned](https://github.com/Chocolate4U/Iran-v2ray-rules)) is answered
with your computer's address: the device's connection comes to Raman Fox on port 443 or 80, and goes on through
the VPN to the site its TLS SNI or HTTP Host names. Every other site gets the network's own answer and goes direct.
Only the web and WhatsApp's messages go through: games' and calls' traffic doesn't. An iPhone's iCloud Private Relay and a browser's
secure DNS skip it. On an iPhone, every app except Safari needs its permission on, in **Settings → Privacy & Security → Local Network**, to reach your computer. When the computer is off, set the device's DNS back to automatic. On a Mac, the device's Telegram, which
doesn't use DNS, goes through too once the device has your computer as its router: Settings says how (and asks your
password once, for the network helper). Linux keeps ports 53, 80
and 443 for root: `sudo sysctl -w net.ipv4.ip_unprivileged_port_start=53` lets Raman Fox have them (add it to
`/etc/sysctl.d/` to keep it).

<!-- Share Raman Fox: hidden for now
**Settings → Share Raman Fox** gives the family's other devices your split tunneling's sites and, if you tick it, your
relay, so nobody else has to set one up. A phone on the same Wi-Fi scans its QR code with the camera and opens them in
Raman Fox; or send the link (`foxhole://settings?d=…`), and they paste it into **Settings → Import settings**, which
shows what it changes first. From an Android phone the same QR code also gives a phone without Raman Fox the app itself,
over the Wi-Fi or the phone's hotspot, with no internet (Android asks to let the browser install apps). Anyone with
the code or link can use your relay. Rules for apps stay each device's own.
-->

**Fixes without an update:** when the filtering changes, foxhole picks up the workaround (other addresses for
Mozilla's servers, more Google sites for relay mode to reach directly) and a short notice from [`hot.json`](hot.json),
which it checks against the developer's signing key. It fetches the file at start and every 6 hours from GitHub,
jsDelivr and githack, through the VPN when connected and through your relay when nothing else answers. A file that
doesn't verify, or is older than the one it has, is ignored.

Relay mode is web-only, slower, has no country choice and **doesn't hide your IP**
(Google forwards it). Sites with bot checks (Cloudflare, Reddit, ChatGPT) refuse
it. It needs foxhole's certificate trusted; foxhole asks after your first connect.
Command-line tools: `eval "$(foxhole env)"`. The script is in
[`assets/relay/Code.gs`](assets/relay/Code.gs).


## Building

```sh
npm ci && npm run build            # the core (TypeScript)
cd mobile && npm ci && npm run build   # the Android APK (Node 22.13+, JDK 17, Android SDK 37 + NDK 27.1)
```

The release key comes from `RAMANFOX_KEYSTORE` (a .jks file), `RAMANFOX_KEYSTORE_PASSWORD` and `RAMANFOX_KEY_ALIAS`;
without them the APK is signed with the debug key. The workflow `.github/workflows/release.yml` builds the universal
APK (phones and Android TV: arm64, armv7, x86_64) on a `v*.*.*` tag or by hand (Run workflow), and drafts a release.

## License

[MIT](LICENSE). Raman Fox is based on [Foxhole VPN](https://github.com/Diercohen/foxhole-vpn) © Dier Cohen (MIT);
Raman Fox's changes © RAMANOW, under the same license. The Iranian sites list in `assets/lists` is
bootmortis/iran-hosted-domains' (MIT, [its license](assets/lists/LICENSE-iran-hosted-domains)); Iran's address ranges
are ipverse/country-ip-blocks' (CC0). Vazirmatn (OFL) and Golos Text (OFL) fonts are in `gui/renderer/fonts`.
