# -*- coding: utf-8 -*-
# English source for the FAQ and blog of both sites. Tokens in answers/articles: {ts} {pc} {store} {mac} {win} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacy", more="Keep reading",
    cta_store="📱 Download TripSweep on the App Store",
    cta_play="🤖 Get TripSweep on Google Play",
    cta_mac="💻 Download PhotoCull for Mac", cta_win="🪟 Download PhotoCull for Windows",
    cross_label={"tripsweep": "Desktop app", "photocull": "Mobile app"},
    twin_android="Using an Android phone? Read the Android guide:",
    twin_iphone="Using an iPhone? Read the iPhone guide:",
    index={
        "tripsweep": dict(
            title="TripSweep blog — free up iPhone storage, delete duplicates",
            desc="Practical guides to free up iPhone storage, remove duplicate and similar photos and clean up old trips, without iCloud and without sending your photos anywhere.",
            h1="Guides to clean up your iPhone photos",
            intro="Short, practical guides to free up space on your iPhone, delete duplicates and keep only the best shots."),
        "photocull": dict(
            title="PhotoCull blog — sort photos on a Mac or PC",
            desc="Guides to sort thousands of photos faster on a big screen, compare similar shots side by side and clear your iPhone or Android phone from a Mac or PC.",
            h1="Guides to sort your photos on a computer",
            intro="Why a big screen changes how fast you can sort photos, and how to use it to clear your iPhone or Android phone."),
    },
)

FAQ_TRIPSWEEP_EXTRA = [
    ("What is the difference between duplicate photos and similar photos?",
     "Duplicates are identical copies of the same file. Similar photos are different shots of the same scene: a burst, five attempts at the same sunset, two near-identical selfies. Duplicates are easy to spot; similar photos are where most of the wasted space hides, and TripSweep groups both so you can keep one and delete the rest."),
    ("How does TripSweep choose the best photo in a group?",
     "It looks at sharpness, Apple's aesthetic score and faces, then suggests one shot per group. The suggestion is only a starting point: you can keep another photo, keep several, or skip the group. The analysis runs on your iPhone with Apple's Vision framework."),
    ("What does the Cleanup tab find?",
     "Identical copies, similar photos, blurry photos, screenshots and large videos, each in its own category with the space it takes. You start with the category that frees the most space and sort it in a few taps."),
    ("Will TripSweep suggest deleting my favorite photos?",
     "No. Photos you marked as favorites are never suggested for deletion, and nothing is deleted until you confirm."),
    ("Does TripSweep work on photos that have no GPS location?",
     "Yes. Photos without a location are grouped by event and month instead of by trip, so screenshots, saved images and photos taken with location services off are sorted too."),
    ("Can I hide my home and workplace from my trips?",
     "Yes. Add your home, work or any place you pass every day as an excluded place, so daily life doesn't show up as a trip and your real trips stand out. Pro makes custom places unlimited."),
    ("Can I back up or share a trip before deleting it?",
     "Yes. You can export a whole trip to your Mac or to the Files app, or share it with the people who were there, then delete it from your iPhone once it is safe elsewhere."),
    ("Do I need an internet connection or an account?",
     "No. TripSweep needs no account and works offline. Place names are recognised on your iPhone, and no photo, video or location is ever sent to a server. Only optional, anonymous usage statistics can be sent. You can turn them off in the About tab."),
    ("Does deleting in TripSweep also delete my photos from iCloud?",
     "If iCloud Photos is on, deleting a photo on your iPhone removes it from all your devices, because that is how iCloud Photos works. TripSweep deletes through “Recently Deleted”, so you have 30 days to change your mind, and iCloud space is freed once that album is emptied."),
    ("Can I review my iPhone photos on a big screen instead of the phone?",
     "Yes. <a href=\"{pc}\">PhotoCull</a> is the free desktop companion for Mac and Windows: it shows your iPhone's camera roll grouped by trip, compares similar photos side by side and lets you mark hundreds of photos in a few clicks. <a href=\"{pc}\">Learn more about PhotoCull</a>."),
    ("Can I delete photos in bulk from my computer instead of tapping on the phone?",
     "Yes, with <a href=\"{pc}\">PhotoCull</a> on a Mac or Windows PC. You mark the photos on the big screen, and the deletion is applied on your iPhone by TripSweep through “Recently Deleted”. The free version allows 6 photos a day from the Mac (see the plans on the TripSweep page), Pro 15, and Pro + Desktop removes the limit."),
    ("Which iPhones and iOS versions does TripSweep support?",
     "TripSweep needs iOS 18 or later. Similar-photo analysis uses Apple's Vision framework and is faster on recent iPhones, but works on every supported model. On Android, it needs Android 11 or later and is available on <a href=\"{play}\">Google Play</a>."),
]

FAQ_PHOTOCULL = dict(
    title="PhotoCull FAQ — sort and delete photos from a Mac or Windows PC",
    desc="How to sort thousands of photos on a computer, compare similar shots, free up an iPhone or Android phone from a Mac or PC: answers about PhotoCull.",
    nav_home="PhotoCull", nav_desktop="Mobile app",
    h1="Questions and answers",
    intro="How to sort your photos faster from a computer, clear your iPhone or Android phone from a Mac or PC, and what PhotoCull does (and never does) with your photos.",
    qa=[
        ('How do I sort my iPhone photos on a computer, Mac or PC?',
         "Plug the iPhone into the computer with a USB cable, unlock it and tap Trust, then open <a href=\"{pc}\">PhotoCull</a>: it groups your camera roll by trip, compares similar shots side by side and marks hundreds of photos in a few clicks. Step-by-step guides: <a href=\"{post:sort-iphone-photos-on-mac}\">on a Mac</a> and <a href=\"{post:sort-iphone-photos-on-pc}\">on a Windows PC</a>."),
        ("Why sort photos on a computer instead of on the iPhone?",
         "A big screen shows more photos at once, a mouse and keyboard select hundreds of them in seconds, and comparing shots side by side is easier than flipping back and forth. Sorting a camera roll of thousands of photos is a few sittings on a phone and a much shorter session on a Mac or PC."),
        ("What is PhotoCull?",
         "PhotoCull is a free desktop app for Mac and Windows that groups your photos by trip, compares similar shots side by side and bulk-deletes what is not worth keeping. It reads your iPhone's camera roll over USB, or any folder of photos on your computer, and works 100% on-device."),
        ("How do I sort thousands of photos quickly?",
         "Open the Trips view: your library is grouped by trip with the space each one takes, so you start with the heaviest. Inside a trip, mark photos in bulk, compare the similar ones side by side and keep the best shot of each group. The same filters as the iOS app (single-day trips, excluded places like home or work, size) narrow things down."),
        ("How do I free up my iPhone storage from a Mac or PC?",
         "Plug in your iPhone by USB, open PhotoCull, mark the trips and photos you no longer need, and confirm. The deletion is applied on the iPhone by the free <a href=\"{ts}\">TripSweep app</a> through “Recently Deleted”, so it frees space as soon as you empty that album."),
        ("Can I delete photos from my iPhone directly from my computer?",
         "Yes, from a Mac or a Windows PC, with the <a href=\"{ts}\">TripSweep app</a> installed on the iPhone. From a Mac, free allows 6 photos a day, Pro 15 and Pro + Desktop removes the limit."),
        ("Is deleting from PhotoCull permanent?",
         "No. Deletions on the iPhone always go through the Photos app's “Recently Deleted” album, where photos stay for 30 days and can be restored. PhotoCull never performs an immediate permanent delete."),
        ("How do I connect my iPhone to PhotoCull?",
         "Use a USB cable, unlock the iPhone and tap “Trust” when asked. On a Mac nothing else is needed. On Windows, install the free Apple Devices app from the Microsoft Store, which provides the driver that lets PhotoCull read the iPhone."),
        ("Can I sort an Android phone's photos on my Mac or PC?",
         "Yes. PhotoCull connects to an Android phone over Wi-Fi on a Mac or a Windows PC, or by USB on Windows. You get the same trips view, side-by-side comparison and bulk deletion as with an iPhone. The phone needs the free <a href=\"{play}\">TripSweep app</a> (Android 11 or later), open on its Deletion tab."),
        ("How do I connect my Android phone over Wi-Fi?",
         "Put the phone and the computer on the same Wi-Fi network and open the Deletion tab in TripSweep on the phone. In PhotoCull, click Android phone and pick your phone, then allow the computer on the phone: the same 4-digit code shows on both screens. You do this once; next time it reconnects by itself. <a href=\"{post:sort-android-photos-on-mac}\">Step-by-step guide for Mac</a>."),
        ("Why doesn't my Mac see my Android phone over USB?",
         "macOS has no built-in support for the way Android phones share files over USB (MTP), so a Mac usually doesn't see them. Use the Wi-Fi connection instead: it works on every Mac, with no driver to install. On Windows, both USB and Wi-Fi work."),
        ("Is the Wi-Fi connection to my phone safe?",
         "Yes. The phone and the computer talk only on your local network, over an encrypted connection, and only after you allowed that computer on the phone with a matching code. Nothing goes through the internet, and you can revoke a computer from TripSweep at any time."),
        ("What happens to photos I delete on an Android phone?",
         "You confirm the deletion on the phone, in TripSweep, and the photos go to the phone's trash, where they stay 30 days and can be restored. PhotoCull never deletes anything permanently on its own."),
        ("Do I need the TripSweep iOS app?",
         "Not to browse, compare and sort an iPhone. You need it only to delete photos from the iPhone, because the deletion is applied on the phone. An Android phone needs the TripSweep Android app to connect at all. Folders on your computer can be sorted without either."),
        ("How do I find duplicate photos in a folder on my Mac or PC?",
         "Open the folder in PhotoCull (Open folder, or drop it onto the window). It looks through the subfolders, compares what the photos show and puts the same “≈ N” badge on exact copies, bursts and near-identical shots. Keep the best of each group and send the rest to the Trash or Recycle Bin. Guides: <a href=\"{post:find-duplicate-photos-on-mac}\">on a Mac</a>, <a href=\"{post:find-duplicate-photos-on-windows}\">on Windows</a>."),
        ("Can I use PhotoCull on photos stored on my computer, not on an iPhone?",
         "Yes. Open any folder: PhotoCull finds similar photos in it, shows the badges on the similar ones and lets you compare and delete with no daily limit."),
        ("How does PhotoCull find similar photos?",
         "It compares the content of your photos, not their file names, so bursts, near-identical shots and the same scene taken several times end up in the same group. You can compare up to 6 photos side by side and keep the sharpest, best-framed one."),
        ("How do I compare similar photos side by side?",
         "Select a group of similar photos and open the comparison: up to 6 photos are shown at the same size so you can judge focus, expressions and framing. Keep the best one and mark the rest."),
        ("Does PhotoCull work on Windows?",
         "Yes: Windows 10 and 11 (64-bit). Reading an iPhone requires the free Apple Devices app from the Microsoft Store. The app is not code-signed yet, so Windows SmartScreen may show a warning on first launch: choose “More info” then “Run anyway”."),
        ("Which Macs does PhotoCull support?",
         "Macs with Apple Silicon running macOS 11 or later. The app is signed and notarized by Apple, so it opens without a security warning."),
        ("Is PhotoCull free? Is there a subscription?",
         "PhotoCull is free to download and there is no subscription. Browsing, comparing and sorting are free, and sorting a folder on your computer is never limited. Deleting photos from an iPhone from a Mac is limited to 6 a day for free, 15 with TripSweep Pro and unlimited with Pro + Desktop (one-time purchases made in the TripSweep iOS app)."),
        ("Does PhotoCull send my photos to a server or the cloud?",
         "No. PhotoCull works 100% on-device: no account, no cloud, no photo, video or location is ever sent anywhere. Place recognition and similar-photo detection run on your computer. Only optional, anonymous usage statistics can be sent."),
        ("Will PhotoCull change or modify my original photos?",
         "No. PhotoCull only reads your photos to show and compare them. The only change it ever makes is the deletion you confirm."),
        ("How do I hide my home and workplace from the trips view?",
         "Add them as excluded places: daily life then stops showing up as a trip and your real trips stand out. The setting is the same as in the iOS app."),
        ("Can I clean up after a vacation from my computer?",
         "Yes, it is the typical use. After a trip, plug in the iPhone, open that trip in PhotoCull, compare the similar shots, keep the best of each and delete the rest. The <a href=\"{ts}\">TripSweep app</a> can also export the whole trip before you delete anything."),
        ("Can I use PhotoCull to prepare a photo album or a backup?",
         "PhotoCull helps you decide what is worth keeping: sort the trip, remove the duplicates and near-identical shots, then back up or share what is left. The <a href=\"{ts}\">TripSweep app</a> can export or share a whole trip."),
    ],
    footer_copy="© 2026 PhotoCull. Developed by Jeffrey Brignoli.",
    footer_privacy="Privacy", footer_kofi="Ko-fi",
)

BLOG = {
"tripsweep": [
dict(slug="free-up-iphone-storage",
     title="How to free up iPhone storage without iCloud — a practical guide",
     desc="Where your iPhone storage really goes and the fastest ways to free gigabytes of photos and videos without paying for more iCloud.",
     h1="How to free up iPhone storage without paying for iCloud",
     body="""      <p>“iPhone storage full” almost always means one thing: the Photos app. Photos and videos are usually the largest item in Settings → General → iPhone Storage, and most of that space is waste you can remove without losing a single memory.</p>

      <h2>1. Start with what weighs the most</h2>
      <p>Large videos are the fastest win: a few minutes of 4K video take as much room as hundreds of photos. Sort your videos by size, watch the first seconds, and delete the ones you will never open again. Screen recordings and videos sent to you by messaging apps are common offenders.</p>

      <h2>2. Delete similar photos, not just duplicates</h2>
      <p>The Photos app can find exact duplicates, but the real waste is near-identical shots: the burst of ten frames, five attempts at the same group photo, three selfies in a row. Keep the best of each group and delete the rest. This is where most people recover the most space, and the hardest part to do by hand.</p>

      <h2>3. Clear screenshots and blurry photos</h2>
      <p>Screenshots pile up unnoticed: tickets, maps, conversations you no longer need. Blurry photos and accidental shots are the same. They rarely deserve to stay, and they are quick to review as a batch.</p>

      <h2>4. Empty “Recently Deleted”</h2>
      <p>Deleted photos stay in the Recently Deleted album for 30 days and keep taking space. Once you are happy with your choices, empty it to actually get the storage back.</p>

      <h2>5. Clean up old trips, one by one</h2>
      <p>Old vacations are the biggest block of photos you never look at. Going trip by trip is easier than scrolling a library of thousands of photos: pick the heaviest trip, keep the highlights, delete the leftovers.</p>

      <h2>How TripSweep makes this faster</h2>
      <p><a href="{ts}">TripSweep</a> does these steps for you on the iPhone. Its Cleanup tab lists identical copies, similar photos, blurry photos, screenshots and large videos, each with the space it takes. Your trips are grouped by place and date and sorted by size, and a “Keep 1 per group” button handles a whole category in one tap. Favorites are never suggested for deletion, deletions go through “Recently Deleted”, and nothing ever leaves your phone: no account, no cloud. Only optional, anonymous usage statistics can be sent.</p>
      <p>If you prefer a big screen, <a href="{pc}">PhotoCull</a> does the same sorting on a Mac or Windows PC.</p>

      <h2>Do I need iCloud?</h2>
      <p>iCloud is a fine backup, but it is not a cleaning tool: it stores everything, including the duplicates. Cleaning first means you need less storage, wherever it is.</p>"""),
dict(slug="delete-duplicate-photos-iphone",
     title="How to delete duplicate and similar photos on iPhone",
     desc="Find exact duplicates, bursts and near-identical shots on your iPhone, keep the best one and delete the rest safely.",
     h1="How to delete duplicate and similar photos on your iPhone",
     body="""      <p>Duplicates quietly eat iPhone storage. Some are exact copies, but most are near-identical shots of the same moment. Here is how to find both and clean them up safely.</p>

      <h2>Duplicates and similar photos are not the same thing</h2>
      <p>An exact duplicate is the same file saved twice, for example after an import or a download. A similar photo is a different shot of the same scene: a burst, a few takes of a group photo, a selfie repeated until you were happy. Exact duplicates are easy to detect; similar photos are more common and take far more space.</p>

      <h2>The built-in way</h2>
      <p>Recent versions of iOS include a Duplicates album in the Photos app (under Utilities). It merges exact copies and is a good first pass. It does not group similar photos, so the bursts and near-identical shots stay in your library.</p>

      <h2>Removing similar photos</h2>
      <p>For similar shots you have to compare and choose. Open the group, look at sharpness, expressions and framing, keep the best photo and delete the others. Doing it by hand across thousands of photos is slow, which is why most people never finish.</p>

      <h2>Do it faster with TripSweep</h2>
      <p><a href="{ts}">TripSweep</a> finds identical copies and similar photos anywhere in your library and shows each group side by side without cropping. It suggests the best shot using sharpness, Apple's aesthetic score and faces, and the Cleanup tab's “Keep 1 per group” button sorts a whole category in one tap. Your favorites are never suggested for deletion.</p>

      <h2>Stay safe while you delete</h2>
      <ul>
        <li>Delete through the Photos app: deleted photos go to “Recently Deleted” for 30 days, so a mistake is reversible.</li>
        <li>Keep favorites: mark the photos you love before cleaning.</li>
        <li>Check iCloud Photos: if it is on, deleting on the iPhone deletes everywhere.</li>
        <li>Empty “Recently Deleted” at the end to get the space back.</li>
      </ul>

      <h2>Prefer a big screen?</h2>
      <p>With <a href="{pc}">PhotoCull</a> on a Mac or Windows PC you can compare up to six similar photos side by side and mark hundreds in a few clicks.</p>"""),
dict(slug="clean-up-vacation-photos",
     title="How to clean up old vacation photos and keep the best ones",
     desc="Turn a thousand holiday photos into a keeper album: group by trip, remove the near-identical shots, keep the highlights.",
     h1="How to clean up old vacation photos and keep the best ones",
     body="""      <p>A one-week trip easily produces a thousand photos and videos, and most of them are near-copies of a few good shots. Sorting them while the trip is fresh is easy; sorting them a year later is a chore. This method works for both.</p>

      <h2>1. Work trip by trip</h2>
      <p>A library of 20,000 photos is overwhelming; one trip of 800 photos is not. Group your photos by trip using their date and location, and handle one trip at a time, starting with the heaviest.</p>

      <h2>2. Remove the near-identical shots first</h2>
      <p>Most of a trip is variations of the same scene. For every group, keep the sharpest one with the best expressions and delete the others. This alone often halves the size of a trip.</p>

      <h2>3. Review the leftovers: screenshots, blurry photos, big videos</h2>
      <p>Tickets, maps, accidental photos and long videos you never rewatch are easy to remove once they are listed together.</p>

      <h2>4. Back up or share before you delete</h2>
      <p>Export the keeper photos to your computer or share them with the friends who were there. Only then delete the trip from your phone. Deletions go to “Recently Deleted”, which gives you 30 days to change your mind.</p>

      <h2>5. Photos without GPS</h2>
      <p>Photos taken with location off or saved from messages have no place. Group them by event and month instead, so they get sorted too.</p>

      <h2>How TripSweep helps</h2>
      <p><a href="{ts}">TripSweep</a> groups your photos and videos by trip (or by event and month when there is no GPS), shows how many gigabytes of similar photos each trip contains, suggests the best shot of each group and exports or shares a whole trip. You can exclude home and work so daily life doesn't look like a trip. Everything runs on your iPhone, offline.</p>
      <p>To do the same on a big screen, <a href="{pc}">PhotoCull</a> shows your iPhone's trips on a Mac or Windows PC.</p>"""),
dict(slug="free-up-android-storage",
     title="How to free up Android storage without Google One",
     desc="Where your Android storage really goes and the fastest ways to free gigabytes of photos and videos without paying for more cloud storage.",
     h1="How to free up Android storage without paying for Google One",
     body="""      <p>“Storage full” on an Android phone almost always means photos and videos. Settings → Storage shows it plainly, and most of that space is shots you will never look at again. Here is how to get it back without buying more cloud storage.</p>

      <h2>1. Start with what weighs the most</h2>
      <p>Long videos are the fastest win: a few minutes of 4K take as much room as hundreds of photos. Sort them by size, watch the first seconds and delete the ones you will never open again.</p>

      <h2>2. Delete similar photos, not just duplicates</h2>
      <p>Cleaner apps find exact copies, but the real waste is near-identical shots: bursts, five attempts at the same group photo, three selfies in a row. Keep the best of each group and delete the rest.</p>

      <h2>3. Clear screenshots and blurry photos</h2>
      <p>Screenshots of tickets, maps and conversations pile up unnoticed, and accidental or blurry shots too. They are quick to review as a batch.</p>

      <h2>4. Empty the trash</h2>
      <p>Deleted photos usually wait 30 days in the trash and keep taking space. Once you are happy with your choices, empty it to actually get the storage back.</p>

      <h2>5. Clean up old trips, one by one</h2>
      <p>Old vacations are the biggest block of photos you never look at. Going trip by trip is easier than scrolling thousands of photos: pick the heaviest trip, keep the highlights, delete the leftovers.</p>

      <h2>How TripSweep makes this faster</h2>
      <p><a href="{ts}">TripSweep</a> does these steps for you on the phone. Its Cleanup tab lists identical copies, similar photos, blurry photos, screenshots and large videos, each with the space it takes, and your trips are grouped automatically. It is free on <a href="{play}">Google Play</a> (Android 11 or later) and works 100% on the phone.</p>
      <p>If you prefer a big screen, <a href="{pc}">PhotoCull</a> does the same sorting on a Mac or Windows PC, connected over Wi-Fi.</p>

      <h2>Do I need Google One?</h2>
      <p>Cloud storage is a fine backup, but it is not a cleaning tool: it stores everything, duplicates included. Cleaning first means you need less storage, wherever it is.</p>"""),
dict(slug="delete-duplicate-photos-android",
     title="How to delete duplicate and similar photos on Android",
     desc="Find exact duplicates, bursts and near-identical shots on your Android phone, keep the best one and delete the rest safely.",
     h1="How to delete duplicate and similar photos on your Android phone",
     body="""      <p>Duplicates quietly eat an Android phone's storage. Some are exact copies, but most are near-identical shots of the same moment. Here is how to find both and clean them up safely.</p>

      <h2>Duplicates and similar photos are not the same thing</h2>
      <p>An exact duplicate is the same file saved twice, for example after a download, a messaging app or a restore. A similar photo is a different shot of the same scene: a burst, a few takes of a group photo, a selfie repeated until it looked right. File cleaners catch the first kind; the second kind takes far more space.</p>

      <h2>What Android offers</h2>
      <p>File manager apps can list exact duplicate files, and your gallery shows bursts. Neither compares near-identical shots for you or helps you pick the best one, so you end up flipping between photos one by one.</p>

      <h2>A faster way</h2>
      <p><strong>1. Group by scene.</strong> <a href="{ts}">TripSweep</a> compares the content of your photos, not their names, and groups shots of the same scene, so a burst of ten becomes one decision.</p>
      <p><strong>2. Keep the best one.</strong> It suggests one shot per group; you can keep another one, keep several or skip the group.</p>
      <p><strong>3. Delete safely.</strong> Deleted photos go to the phone's trash for 30 days, so a wrong choice can be undone.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything runs on the phone: no account, no upload. TripSweep is free on <a href="{play}">Google Play</a> (Android 11 or later).</li>
        <li>For a whole camera roll, comparing on a big screen with <a href="{pc}">PhotoCull</a> on a Mac or PC is faster still.</li>
      </ul>"""),
],
"photocull": [
dict(slug="sort-iphone-photos-on-mac",
     title="How to sort your iPhone photos on a Mac",
     desc="Sort thousands of iPhone photos on your Mac: what Photos and Image Capture can and can't do, and a faster way to group, compare and delete.",
     h1="How to sort your iPhone photos on a Mac",
     body="""      <p>Sorting a full camera roll on the iPhone means hours of tapping. On a Mac you see far more photos at once, select with the mouse and compare shots on a big screen. Here is how to do it, with the tools built into macOS and with a dedicated app.</p>

      <h2>With the tools built into macOS</h2>
      <ul>
        <li><strong>Photos:</strong> imports a copy of your iPhone photos to the Mac. Useful as a backup, but it doesn't tell you what to delete on the iPhone.</li>
        <li><strong>Image Capture:</strong> lists the iPhone's photos as plain files, with no grouping by trip and no way to compare similar shots.</li>
      </ul>
      <p>Both work, but with thousands of photos you are still scrolling one long list.</p>

      <h2>With PhotoCull, step by step</h2>
      <p><strong>1. Install PhotoCull.</strong> <a href="{mac}">Download it for free</a>: macOS 11 or later on Apple Silicon, signed and notarized by Apple.</p>
      <p><strong>2. Plug in the iPhone.</strong> Connect it with a USB cable, unlock it and tap Trust.</p>
      <p><strong>3. Sort trip by trip.</strong> The Trips view groups your camera roll by date and place and shows the space each trip takes. Start with the heaviest.</p>
      <p><strong>4. Compare and mark.</strong> Similar photos carry a badge: open up to six side by side, keep the best and mark the rest, along with screenshots and big videos you don't need.</p>
      <p><strong>5. Delete safely.</strong> The deletion is applied on the iPhone by the free <a href="{ts}">TripSweep app</a> through “Recently Deleted”, so you have 30 days to change your mind.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your Mac and your iPhone: no account, no cloud, no upload.</li>
        <li>PhotoCull never modifies your originals and only deletes what you confirm.</li>
        <li>From a Mac, free allows 6 deletions a day, TripSweep Pro 15, and Pro + Desktop is unlimited. Browsing and sorting are free, and sorting a folder of photos on the Mac is never limited.</li>
      </ul>"""),
dict(slug="sort-iphone-photos-on-pc",
     title="How to sort your iPhone photos on a Windows PC",
     desc="Sort thousands of iPhone photos on Windows 10 or 11: what the Photos app and File Explorer show, and a faster way to group, compare and delete.",
     h1="How to sort your iPhone photos on a Windows PC",
     body="""      <p>An iPhone and a Windows computer? You can still sort your photos on a big screen instead of the phone. Here is what Windows can do on its own, and a faster method.</p>

      <h2>With the tools built into Windows</h2>
      <ul>
        <li><strong>Photos app:</strong> imports a copy of your iPhone photos to the PC. Good for a backup, but it doesn't help you choose what to delete.</li>
        <li><strong>File Explorer:</strong> shows the iPhone's photos in folders such as 100APPLE, named IMG_0001 and so on, with no trips and no comparison of similar shots.</li>
      </ul>

      <h2>With PhotoCull, step by step</h2>
      <p><strong>1. Install Apple Devices.</strong> Get the free Apple Devices app from the Microsoft Store: Windows needs it to read an iPhone.</p>
      <p><strong>2. Install PhotoCull.</strong> Get it from the Microsoft Store or <a href="{win}">download it for free</a> (Windows 10/11, 64-bit). The download is not code-signed yet, so SmartScreen may warn on first launch.</p>
      <p><strong>3. Plug in the iPhone.</strong> Connect it with a USB cable, unlock it and tap Trust.</p>
      <p><strong>4. Sort trip by trip.</strong> The Trips view groups your camera roll by date and place and shows the space each trip takes. Start with the heaviest.</p>
      <p><strong>5. Compare, mark, delete.</strong> Similar photos carry a badge: compare up to six side by side, keep the best and mark the rest. The deletion is applied on the iPhone by the free <a href="{ts}">TripSweep app</a> through “Recently Deleted”, so you have 30 days to change your mind.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your PC and your iPhone: no account, no cloud, no upload.</li>
        <li>PhotoCull never modifies your originals and only deletes what you confirm.</li>
        <li>Browsing and sorting are free, and sorting a folder of photos already on the PC is never limited.</li>
      </ul>"""),
dict(slug="sort-photos-on-computer",
     title="How to sort thousands of photos faster on a Mac or Windows PC",
     desc="Why sorting photos on a big screen is so much faster than on a phone, and a simple method to go through thousands of photos in one sitting.",
     h1="How to sort thousands of photos faster on a Mac or PC",
     body="""      <p>If your camera roll holds ten thousand photos, sorting it on a phone screen is a project you will never finish. On a computer it can be a single evening. Here is why, and a method that works.</p>

      <h2>Why a computer is faster</h2>
      <ul>
        <li><strong>More on screen:</strong> dozens of photos at once instead of a handful.</li>
        <li><strong>Precise selection:</strong> a mouse and keyboard select hundreds of photos in seconds.</li>
        <li><strong>Real comparison:</strong> similar photos next to each other at a size where focus and expressions are visible.</li>
      </ul>

      <h2>A method that works</h2>
      <p><strong>1. Group by trip.</strong> Sorting by date and place breaks the library into manageable pieces. Start with the trip that takes the most space.</p>
      <p><strong>2. Remove the near-copies.</strong> Compare each group of similar shots, keep the best and mark the rest.</p>
      <p><strong>3. Filter the noise.</strong> Hide places you don't care about (home, work) so real trips stand out, and filter by size to find heavy files.</p>
      <p><strong>4. Delete in one go.</strong> Mark hundreds of photos and confirm once.</p>

      <h2>PhotoCull does exactly this</h2>
      <p><a href="{pc}">PhotoCull</a> is a free desktop app for Mac and Windows. Its Trips view groups the library by trip and shows the space each takes, similar photos carry a badge, and you can compare up to six side by side. It reads an iPhone over USB or any folder on your computer, works 100% on-device and never modifies your originals.</p>
      <p>Deletions on an iPhone go through the free <a href="{ts}">TripSweep app</a> and “Recently Deleted”, so a mistake can be undone for 30 days. Sorting a folder on your computer is never limited.</p>

      <h2>Tips for a long session</h2>
      <ul>
        <li>Work trip by trip, not by scrolling the whole library.</li>
        <li>Decide fast: if two shots look alike, keep one.</li>
        <li>Delete at the end of each trip, so progress is visible.</li>
      </ul>"""),
dict(slug="free-up-iphone-from-mac-or-pc",
     title="How to free up your iPhone storage from a Mac or Windows PC",
     desc="Plug in your iPhone, sort photos on a big screen and delete what you don't need, without iCloud and without sending anything online.",
     h1="How to free up your iPhone from a Mac or Windows PC",
     body="""      <p>Cleaning a full iPhone on the iPhone is tedious. From a computer you can see far more photos at once and decide faster. Here is the whole process.</p>

      <h2>What you need</h2>
      <ul>
        <li>A Mac (Apple Silicon, macOS 11+) or a Windows 10/11 PC.</li>
        <li>A USB cable. On Windows, also the free Apple Devices app from the Microsoft Store.</li>
        <li><a href="{pc}">PhotoCull</a>, free for both systems.</li>
        <li>For deleting from the iPhone: the free <a href="{ts}">TripSweep app</a> on the iPhone.</li>
      </ul>

      <h2>Step by step</h2>
      <p><strong>1. Plug in and trust.</strong> Connect the iPhone, unlock it and tap Trust.</p>
      <p><strong>2. Open the Trips view.</strong> PhotoCull groups your camera roll by trip and shows the space each takes.</p>
      <p><strong>3. Sort the heaviest trips.</strong> Compare similar shots, keep the best, and mark the rest, plus screenshots and big videos you don't need.</p>
      <p><strong>4. Confirm the deletion.</strong> From a Mac, the deletion is applied on the iPhone by TripSweep through “Recently Deleted”, on Windows too. Nothing is permanently erased at once.</p>
      <p><strong>5. Empty “Recently Deleted”.</strong> The storage comes back once the album is emptied.</p>

      <h2>Is it safe?</h2>
      <p>Yes: your photos stay on your devices, with no account, no cloud and no upload. Deleted photos stay 30 days in “Recently Deleted”, and PhotoCull only reads your photos until you confirm.</p>

      <h2>How many photos can I delete per day?</h2>
      <p>From a Mac, free allows 6 photos a day, TripSweep Pro 15 and Pro + Desktop is unlimited (see the plans on the TripSweep page). All are one-time purchases with no subscription. Browsing, comparing and sorting are free, and sorting a folder on your computer is never limited.</p>

      <h2>On Windows</h2>
      <p>The steps are the same on Windows 10 and 11. Install the free Apple Devices app from the Microsoft Store first, so PhotoCull can read the iPhone. The app is not code-signed yet, so SmartScreen may warn on first launch.</p>"""),
dict(slug="compare-similar-photos-keep-the-best",
     title="How to compare similar photos side by side and keep the best one",
     desc="A simple routine to choose the best shot among near-identical photos: what to look at, and how to do it quickly on a big screen.",
     h1="How to compare similar photos and keep the best one",
     body="""      <p>You took six photos of the same moment and they all look fine. Choosing the best takes seconds with the right method, and a few minutes with the wrong one.</p>

      <h2>What to check, in this order</h2>
      <ol>
        <li><strong>Focus.</strong> Zoom on the eyes or the main subject. A blurry subject is disqualifying.</li>
        <li><strong>Expressions.</strong> Eyes open, natural smiles, nobody mid-blink.</li>
        <li><strong>Framing.</strong> Nothing cut off, a clean background, the horizon straight.</li>
        <li><strong>Moment.</strong> If two shots are equal, keep the one that feels more alive.</li>
      </ol>

      <h2>Why side by side matters</h2>
      <p>Flipping between photos makes small differences hard to see. Seeing them next to each other at the same size makes the sharpest or best-framed one obvious. A computer screen shows up to six at once, where a phone shows one.</p>

      <h2>A faster routine</h2>
      <p>Group similar photos first, so you never hunt for them in the library. For each group, open the comparison, pick one and mark the others. You decide in seconds, not minutes.</p>

      <h2>Do it with PhotoCull</h2>
      <p><a href="{pc}">PhotoCull</a> shows a badge on similar photos, opens up to six side by side and lets you mark the rest in one click. It works on an iPhone connected by USB or on any folder on your Mac or PC, offline, and it never modifies your originals.</p>
      <p>On the phone itself, the <a href="{ts}">TripSweep app</a> suggests the best shot of each group using sharpness, Apple's aesthetic score and faces, and its “Keep 1 per group” button handles a whole category at once.</p>

      <h2>Keep, don't regret</h2>
      <p>When you are unsure, keep two. Deletions on an iPhone go through “Recently Deleted” for 30 days, so you can still change your mind.</p>"""),
dict(slug="find-duplicate-photos-on-mac",
     title="How to find duplicate and similar photos on a Mac",
     desc="Find exact copies, bursts and near-identical shots in your Mac's photo folders or on an external drive, keep the best and send the rest to the Trash.",
     h1="How to find duplicate and similar photos on a Mac",
     body="""      <p>Years of imports, camera cards and backups leave the same photos scattered across folders on a Mac. Some are exact copies; most are near-identical shots of the same moment. Here is how to find both, keep the best and free the space, without touching your Photos library.</p>

      <h2>What macOS offers</h2>
      <ul>
        <li><strong>Finder:</strong> sorting a folder by name or size helps spot obvious copies such as “IMG_1234 copy.jpg”, but not two different shots of the same scene.</li>
        <li><strong>Photos:</strong> its Duplicates album only covers photos already in the Photos library, not your other folders or drives.</li>
      </ul>

      <h2>With PhotoCull, step by step</h2>
      <p><strong>1. Install PhotoCull.</strong> <a href="{mac}">Download it for free</a>: macOS 11 or later on Apple Silicon, signed and notarized by Apple.</p>
      <p><strong>2. Open the folder.</strong> Click Open folder, or drop a folder onto the window. Subfolders are included, and so are external drives.</p>
      <p><strong>3. Look at the badges.</strong> PhotoCull compares the content of the photos, not their names: exact copies, bursts and near-identical shots get the same “≈ N” badge.</p>
      <p><strong>4. Keep the best one.</strong> Open a group to compare up to six photos side by side, keep the sharpest and mark the rest.</p>
      <p><strong>5. Delete safely.</strong> Marked files go to the Mac's Trash, where Put Back restores them if you change your mind.</p>

      <h2>Good to know</h2>
      <ul>
        <li>JPEG, HEIC, PNG, TIFF, WebP and RAW files (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) are supported, as well as MOV and MP4 videos.</li>
        <li>Photos are dated from their EXIF data, so copied folders still sort by the day they were taken.</li>
        <li>Sorting a folder is free and never limited. Everything runs on your Mac: no account, no upload.</li>
        <li>Photos libraries and app bundles inside the folder are skipped, so PhotoCull never digs into another app's files.</li>
      </ul>"""),
dict(slug="find-duplicate-photos-on-windows",
     title="How to find duplicate and similar photos on Windows",
     desc="Find exact copies, bursts and near-identical shots in your PC's photo folders or on an external drive, keep the best and send the rest to the Recycle Bin.",
     h1="How to find duplicate and similar photos on Windows 10 or 11",
     body="""      <p>Phone backups, camera cards and old copies leave the same photos in several folders on a PC. Some are exact duplicates, most are near-identical shots. Here is how to find both and clean them up safely.</p>

      <h2>What Windows offers</h2>
      <ul>
        <li><strong>File Explorer:</strong> sorting by name, size or date helps with obvious copies, but it can't tell that two different files show the same scene.</li>
        <li><strong>The Photos app:</strong> good for viewing and importing, with no tool to find similar shots and pick the best.</li>
      </ul>

      <h2>With PhotoCull, step by step</h2>
      <p><strong>1. Install PhotoCull.</strong> Get it for free <a href="{win}">for Windows 10 or 11</a> (64-bit), or from the Microsoft Store.</p>
      <p><strong>2. Open the folder.</strong> Click Open folder, or drop a folder onto the window. Subfolders and external drives are included.</p>
      <p><strong>3. Look at the badges.</strong> PhotoCull compares what the photos show, not their file names: exact copies, bursts and near-identical shots get the same “≈ N” badge.</p>
      <p><strong>4. Keep the best one.</strong> Compare up to six photos side by side, keep the sharpest, mark the rest.</p>
      <p><strong>5. Delete safely.</strong> Marked files go to the Recycle Bin, so you can restore them.</p>

      <h2>Good to know</h2>
      <ul>
        <li>JPEG, HEIC, PNG, TIFF, WebP and RAW files (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) are supported, as well as MOV and MP4 videos. HEIC thumbnails need Microsoft's free HEIF Image Extensions.</li>
        <li>Photos are dated from their EXIF data, so copied folders still sort by the day they were taken.</li>
        <li>Sorting a folder is free and never limited. Everything runs on your PC: no account, no upload.</li>
      </ul>"""),
dict(slug="sort-photo-folder-external-drive",
     title="How to sort a big folder of photos on a Mac or PC",
     desc="Old backups, camera cards, an external drive full of photos: a simple method to sort thousands of files by trip, remove near-duplicates and keep the best.",
     h1="How to sort a big folder of photos, or a whole external drive",
     body="""      <p>Everyone has one: a folder called “Photos to sort”, an old phone backup, an external drive filled over ten years. Thousands of files, no order, many near-duplicates. Here is a method to get through it in one sitting.</p>

      <h2>1. Open the whole folder at once</h2>
      <p>Don't go folder by folder. Open the top folder in <a href="{pc}">PhotoCull</a> (Open folder, or drop it onto the window): subfolders are included, and each photo is dated from its EXIF data rather than from the day it was copied.</p>

      <h2>2. Let the trips appear</h2>
      <p>The Trips view groups photos by date and place and shows the space each group takes. Ten years of files become a list of trips and events, and you start with the heaviest.</p>

      <h2>3. Collapse the near-duplicates</h2>
      <p>Bursts, repeated takes and copies of the same shot carry a “≈ N” badge. Compare up to six side by side, keep the best one, mark the rest. This step alone often removes a large share of the files.</p>

      <h2>4. Mark the obvious leftovers</h2>
      <p>Screenshots, blurry shots, accidental videos: mark them as you go. Nothing is deleted until you confirm.</p>

      <h2>5. Delete safely</h2>
      <p>Confirmed files go to the Trash on a Mac or the Recycle Bin on Windows, so a mistake can be undone. Empty it once you are sure.</p>

      <h2>Good to know</h2>
      <ul>
        <li>RAW files from cameras (CR2, CR3, NEF, ARW, RAF, ORF, RW2, DNG) are supported alongside JPEG, HEIC, PNG and videos.</li>
        <li>Sorting folders is free and never limited, on Mac (<a href="{mac}">download</a>) and Windows (<a href="{win}">download</a>).</li>
        <li>Your originals are never modified: the only change PhotoCull makes is the deletion you confirm.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-mac",
     title="How to sort your Android photos on a Mac",
     desc="A Mac doesn't read Android phones over USB. How to sort thousands of Android photos on a Mac anyway, over Wi-Fi, and delete what you don't need.",
     h1="How to sort your Android photos on a Mac",
     body="""      <p>Plug an Android phone into a Mac and, most of the time, nothing happens: macOS doesn't read Android phones over USB the way Windows does. Yet a Mac is the best place to sort a big camera roll, with a large screen, a mouse and side-by-side comparison. Here is what works.</p>

      <h2>What macOS can do on its own</h2>
      <ul>
        <li><strong>Image Capture:</strong> may see the phone if you choose “Transfer photos” (PTP) in its USB notification, but only as a flat list of files, with no grouping and no way to compare similar shots.</li>
        <li><strong>Google's Android File Transfer:</strong> no longer maintained, and it only copies files anyway.</li>
        <li><strong>Cloud upload:</strong> sending everything to an online service just to sort it is slow, uses your data plan and puts your photos on someone else's server.</li>
      </ul>

      <h2>With PhotoCull, over Wi-Fi, step by step</h2>
      <p><strong>1. Install both apps.</strong> <a href="{mac}">Download PhotoCull for Mac</a> for free (macOS 11 or later on Apple Silicon), and install the free <a href="{play}">TripSweep app from Google Play</a> on the phone (Android 11 or later).</p>
      <p><strong>2. Same Wi-Fi.</strong> Put the phone on the same Wi-Fi network as the Mac and open the Deletion tab in TripSweep.</p>
      <p><strong>3. Connect once.</strong> In PhotoCull, click Android phone and pick your phone. Allow the Mac on the phone: the same 4-digit code shows on both screens. Next time, it reconnects by itself.</p>
      <p><strong>4. Sort trip by trip.</strong> The Trips view groups the camera roll by date and place, with the space each trip takes. Similar photos carry a badge: compare up to six side by side, keep the best, mark the rest.</p>
      <p><strong>5. Delete safely.</strong> Click Delete and confirm on the phone, in TripSweep. Photos go to the phone's trash for 30 days, so a mistake can be undone.</p>

      <h2>Good to know</h2>
      <ul>
        <li>The connection stays on your local network and is encrypted; nothing goes through the internet.</li>
        <li>PhotoCull never modifies your originals and only deletes what you confirm on the phone.</li>
        <li>From the computer, free allows 6 deletions a day, TripSweep Pro 15, and Pro + Desktop is unlimited. Browsing and sorting are always free.</li>
        <li>Got an iPhone too? It connects to the Mac with a USB cable instead.</li>
      </ul>"""),
dict(slug="sort-android-photos-on-pc",
     title="How to sort your Android photos on a Windows PC",
     desc="Sort thousands of Android photos on Windows 10 or 11: what File Explorer and the Photos app show, and a faster way to group, compare and delete.",
     h1="How to sort your Android photos on a Windows PC",
     body="""      <p>Windows reads Android phones well, but reading is not sorting. With thousands of photos, the built-in tools leave you scrolling one long list of file names. Here is what they do, and a faster way to clear the phone from your PC.</p>

      <h2>With the tools built into Windows</h2>
      <ul>
        <li><strong>File Explorer:</strong> after you choose “File transfer” on the phone, its DCIM folder shows up as files. You can delete from there, but with no grouping and no way to compare similar shots.</li>
        <li><strong>The Photos app:</strong> imports a copy to the PC. A good backup, but it doesn't tell you what to remove from the phone.</li>
        <li><strong>Phone Link:</strong> shows recent photos only, one at a time.</li>
      </ul>

      <h2>With PhotoCull, step by step</h2>
      <p><strong>1. Install both apps.</strong> Get PhotoCull for free <a href="{win}">for Windows 10 or 11</a>, and the free <a href="{play}">TripSweep app from Google Play</a> on the phone (Android 11 or later).</p>
      <p><strong>2. Connect by USB or Wi-Fi.</strong> By USB: plug in the phone and choose “File transfer” in its USB notification. By Wi-Fi: put both on the same network. Then open the Deletion tab in TripSweep and click Android phone in PhotoCull.</p>
      <p><strong>3. Sort trip by trip.</strong> The Trips view groups the camera roll by date and place and shows the space each trip takes. Start with the heaviest.</p>
      <p><strong>4. Compare and mark.</strong> Similar photos carry a badge: open up to six side by side, keep the best and mark the rest, along with screenshots and big videos.</p>
      <p><strong>5. Delete safely.</strong> Confirm on the phone, in TripSweep: photos go to the phone's trash for 30 days.</p>

      <h2>Good to know</h2>
      <ul>
        <li>Everything stays on your PC and your phone: no account, no cloud, no upload.</li>
        <li>Deleting from File Explorer is immediate and permanent; going through TripSweep keeps the 30-day safety net.</li>
        <li>From the PC, free allows 6 deletions a day, TripSweep Pro 15, and Pro + Desktop is unlimited. Sorting a folder on the PC is never limited.</li>
      </ul>"""),
dict(slug="free-up-android-from-mac-or-pc",
     title="How to free up Android storage from a Mac or Windows PC",
     desc="Connect your Android phone, sort photos on a big screen and delete what you don't need, without paying for Google One and without uploading anything.",
     h1="How to free up your Android phone's storage from a Mac or PC",
     body="""      <p>When an Android phone runs out of space, photos and videos are almost always the reason. Clearing them on a small screen is slow. From a computer you see more at once and decide faster, without buying more cloud storage.</p>

      <h2>Why a computer helps</h2>
      <p>A big screen shows dozens of photos at once, a mouse selects hundreds in seconds, and comparing near-identical shots side by side is far easier than swiping back and forth. A camera roll that would take an evening on the phone takes minutes.</p>

      <h2>The method</h2>
      <p><strong>1. Connect the phone.</strong> Install <a href="{pc}">PhotoCull</a> on your Mac or PC and the free <a href="{play}">TripSweep app</a> on the phone. Connect over Wi-Fi (Mac and Windows) or by USB (Windows), with TripSweep open on the Deletion tab.</p>
      <p><strong>2. Start with what weighs the most.</strong> The Trips view shows the space each trip takes; long videos and old vacations usually free the most.</p>
      <p><strong>3. Remove the near-duplicates.</strong> Bursts and repeated shots of the same scene carry a badge. Compare them side by side, keep the best one, mark the rest.</p>
      <p><strong>4. Clear screenshots and blurry shots.</strong> They rarely deserve to stay and are quick to mark as a batch.</p>
      <p><strong>5. Confirm on the phone.</strong> TripSweep applies the deletion and moves the photos to the phone's trash, where they stay 30 days. Empty the trash once you are sure, to get the space back.</p>

      <h2>Do I need Google One?</h2>
      <p>Cloud storage is a fine backup, but it keeps everything, duplicates included. Cleaning first means you need less storage, on the phone and in the cloud.</p>

      <h2>Good to know</h2>
      <ul>
        <li>No account and no upload: the phone and the computer talk over your own network or cable.</li>
        <li>From the computer, free allows 6 deletions a day, Pro 15, and Pro + Desktop is unlimited.</li>
      </ul>"""),
],
}
