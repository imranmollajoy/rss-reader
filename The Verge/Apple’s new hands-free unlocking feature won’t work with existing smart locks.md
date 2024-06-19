Last week, Apple announced it’s bringing [hands-free unlocking](/2024/6/10/24172054/apple-home-homekit-robot-vacuum-support-smart-locks-wwdc24) for smart locks to [Apple Home](https://www.apple.com/home-app/) when iOS 18 arrives this fall. The new capability leverages the U1 [ultra wideband (UWB) chip](/2019/9/10/20859550/apple-iphone-11-pro-airdrop-u1-locator-chip-tag-tile-bluetooth-tracking) in many iPhones and Apple Watches to allow a [smart lock](/23393163/best-smart-door-lock) to open automatically as you approach the front door — no tapping required. 

But hands-free unlocking isn’t coming to your [existing Home Key smart lock](/23393163/best-smart-door-lock#:~:text=lock%20to%20get.-,Best%20smart%20lock%20for%20Apple%20Home%20with%20Apple%20Home%20Key,-%E2%86%B4) because no current locks have the hardware to support it. To use this cool new feature, you’re going to have to buy a new lock, and we likely won’t see any UWB-enabled smart locks until the end of 2024 at the earliest.

Apple’s hands-free unlocking won’t be coming to your existing Home Key smart lock

The new capability is part of [Home Key](https://support.apple.com/guide/iphone/unlock-your-door-with-a-home-key-iph0dc255875/ios) — a feature of the Apple Home smart home platform that lets you unlock compatible locks by tapping your iPhone or Apple Watch to them. With hands-free unlocking, you won’t have to pull out your phone or tap your watch to the lock to open it; instead, if you’re wearing your watch or your phone is in your pocket and it’s been unlocked by you in the last 24 hours, the door will unlock when you are six feet away and approaching from outside.

A smart lock can work with both Home Key unlocking options or just one, but as mentioned, it may be a while until we see any locks that support the new feature.

I spoke to several smart lock manufacturers following Apple’s announcement, and they all confirmed that their existing locks do not support UWB. This includes Aqara, U-tec, Yale, August, Level, Lockly, and SwitchBot. (Schlage did not respond.) 

Almost universally, the manufacturers I talked to said they were exploring potentially incorporating the tech, but only U-tec said it had a UWB lock in development. Clark Ruan, VP of U-tec, told me the [next-gen Ultraloq smart lock](/2024/1/3/24022990/ultraloq-bolt-matter-thread-smart-lock-ces24) will support UWB and is estimated to arrive in Q4 of this year.

With a UWB-capable smart lock, your phone / watch can communicate directly with the lock

Hands-free auto unlocking isn’t a new concept, versions of the feature have been available for years. August [first developed the capability](/circuitbreaker/2018/9/25/17898152/august-yale-smart-lock-assure-auto-unlock) to have your door unlock as you approach in 2013, and today several smart locks have this feature.

Apple Home also lets you set an automation to unlock a door automatically using geo-fencing. But it asks for permission to run the automation on your phone or watch every time, making this not hands-free and frankly a bit of a pain. [In my experience](/23367464/yale-assure-lock-2-touchscreen-keypad-wifi-review), neither solution — August’s auto-unlock tech nor Apple’s geo-fencing — is all that reliable. 

What’s new with Apple’s UWB-unlocking implementation is the technology. Instead of using the combination of Bluetooth Low Energy (BLE), Wi-Fi, GPS, and a third-party app that [most other solutions do](https://support.shopyalehome.com/en_us/how-does-auto-unlock-work-r1tW8RQyD), the feature uses UWB and BLE.

It’s the same tech we’ve seen [implemented for digital car keys](/2023/11/16/23964379/apple-iphone-digital-key-uwb-ccc-fira-working-group), such as [BMW’s Digital Key Plus](/2023/4/25/23697212/bmw-digital-key-plus-support-google-pixel-samsung-galaxy-devices), which uses UWB to know when you’re close to your car and unlock it automatically. With a UWB-capable smart lock, your phone/watch can communicate with it directly with no need to jump through several hoops to verify your location before unlocking your door. In theory, this should provide a more reliable, secure, and faster auto-unlock experience. 

*Hands-free unlocking is enabled using* [*Express Mode*](https://support.apple.com/guide/iphone/unlock-your-door-with-a-home-key-iph0dc255875/17.0/ios/17.0#iphbde57d7c1) *in the Home app, which bypasses the need to use Face or Touch ID to unlock a door.*

Image: Apple

UWB is a short-range, wireless communication protocol that operates at very high frequencies. It can provide [secure, precise, real-time location data](https://www.nxp.com/applications/enabling-technologies/connectivity/ultra-wideband-uwb:UWB) without needing line of sight — making it ideal for this type of use case.

According to Sujata Neidig, marketing director of NXP, [which makes UWB chips](https://www.nxp.com/applications/enabling-technologies/connectivity/ultra-wideband-uwb:UWB), the technology provides accurate distance and angle measurements without line of sight. Meaning it’s precise enough to know if you are inside the home approaching the door so it won’t unlock, outside approaching the door so it will unlock, or walking away from your door outside so it can lock as you leave.

For the car lock technology NXP has worked on, Neidig said the auto-unlock feature uses BLE for the initial connection between car and phone and then switches to UWB for precision unlocking to know which side to unlock first. She said a similar implementation can be used for a smart home door lock. The BLE radio is needed because, according to Neidig, UWB has a high power consumption. By using BLE initially to establish a connection the UWB radio can stay off for longer, reducing its power use.

While the higher power use of UWB isn’t great news for smart locks, which already struggle with battery life, the use cases for UWB in the smart home are exciting. I’ve been hoping to see Apple do more with its U1 chip, which has also made it into the HomePod Mini and second-gen HomePod.

*In 2021, Apple added a music hand-off feature from your iPhone to a HomePod that uses the U1 chip in both devices.*

Image: Apple

Prior to this new auto-unlock capability for the home, Apple has used UWB for things like, [music hand-off](/2021/1/26/22250856/homepod-mini-ultra-wideband-handoff-feature-update-ios-14-apple-iphone-u1), finding an AirTag, and [unlocking your car](/2021/1/14/22230569/bmw-digital-key-plus-iphone-unlock-u1-chip-ultra-wideband). But the potential is there for [advanced smart home automations](/2022/7/22/23274332/apple-wwdc-ios16-nearby-interactions-u1-uwb-feature-coming). With such precise location data, a HomePod could turn on lights in the bedroom when you walk past it from the living room into the bedroom, and then turn them on in the living room when you walk in the other direction. That would be very cool.

Hands-free unlocking for smart home locks will likely extend beyond Apple Home. Aliro, [a universal standard for smart locks](/2023/11/9/23952637/csa-aliro-new-standard-smart-locks-digital-access) that Apple is helping develop, plans to include UWB, along with BLE and NFC (which Apple uses for its tap-to-unlock Home Key technology), in its first specification.

We may well see hands-free unlocking come to more smart home platforms

While Aliro is in the very early stages, considering most high-end Android phones also support UWB, we may well see this hands-free unlocking capability come to more smart home platforms if the smart lock industry ultimately adopts it. Unlike with Apple’s tap-to-unlock Home Key feature, hands-free unlocking with UWB won’t require specific HomeKit certification; if the lock has [Matter certification](/22832127/matter-smart-home-products-thread-wifi-explainer) and the necessary hardware, it will work with Apple Home’s hands-free unlocking.

So, while it looks like we’re going to have to wait a while for this better, faster auto-unlock feature — and invest in new hardware — there are promising signs here. The very fragmented smart home industry is starting to coalesce around exciting new technologies with the potential to make our homes significantly smarter.
