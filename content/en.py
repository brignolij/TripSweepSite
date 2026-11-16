# -*- coding: utf-8 -*-
# English source for the FAQ and blog of the TripSweep site. Tokens in answers/articles: {ts} {pc} {store} (see link_tokens).

BLOG_UI = dict(
    nav="Blog", privacy="Privacy", more="Keep reading",
    cta_store="📱 Download TripSweep on the App Store",
    cta_play="🤖 Get TripSweep on Google Play",
    cross_label={"tripsweep": "Desktop app", "photocull": "Mobile app"},
    twin_android="Using an Android phone? Read the Android guide:",
    twin_iphone="Using an iPhone? Read the iPhone guide:",
    index={
        "tripsweep": dict(
            title="TripSweep blog — free up iPhone storage, delete duplicates",
            desc="Practical guides to free up iPhone storage, remove duplicate and similar photos and clean up old trips, without iCloud and without sending your photos anywhere.",
            h1="Guides to clean up your iPhone photos",
            intro="Short, practical guides to free up space on your iPhone, delete duplicates and keep only the best shots."),
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
     "Yes. <a href=\"{pc}\">PhotoCull</a> is the free desktop app for Mac and Windows: it shows your iPhone's camera roll grouped by trip, compares similar photos side by side and lets you mark hundreds of photos in a few clicks. <a href=\"{pc}\">Learn more about PhotoCull</a>."),
    ("Can I delete photos in bulk from my computer instead of tapping on the phone?",
     "Yes, with <a href=\"{pc}\">PhotoCull</a> on a Mac or Windows PC. You mark the photos on the big screen and PhotoCull deletes them directly over the USB cable, with no daily limit and nothing to buy. With an iPhone, this requires iCloud Photos turned off on the iPhone, and macOS 27 or later on a Mac (any Windows 10 or 11 works). The deletion is permanent on the iPhone, the photos do not go to “Recently Deleted”, but PhotoCull keeps a copy on your computer for 30 days by default. An Android phone connects by USB cable too, in “File transfer” mode, with nothing to install on the phone (Windows 10 or 11, or a Mac with macOS 27 or later)."),
    ("Which iPhones and iOS versions does TripSweep support?",
     "TripSweep needs iOS 18 or later. Similar-photo analysis uses Apple's Vision framework and is faster on recent iPhones, but works on every supported model. On Android, it needs Android 11 or later and is available on <a href=\"{play}\">Google Play</a>."),
]

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
      <p>If you prefer a big screen, <a href="{pc}">PhotoCull</a> does the same sorting on a Mac or Windows PC, with the phone connected by USB cable.</p>

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
}
