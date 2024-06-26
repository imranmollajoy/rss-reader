When I first used the Arm-powered Surface Pro X in 2019, I loved the hardware but [disliked the software experience](/2019/11/6/20950487/microsoft-surface-pro-x-7-review-comparison-specs-photos). Everything felt like it was lagging. Microsoft didn’t have native versions of Edge or its Office apps, and it was clear the Surface Pro X had been released too early. With little support from developers, Windows on Arm was unlikely to succeed.

Nearly five years later, the Windows on Arm experience has improved dramatically. Qualcomm’s new Snapdragon X Elite and X Plus processors deliver a Windows 11 experience that feels like any regular laptop. Microsoft and Qualcomm have also been pushing software developers to create more ARM64 native apps, and it has made a huge difference.

Apps like Photoshop, Dropbox, and Zoom are all native, as are entertainment apps like Spotify, Prime, and Hulu. Even Chrome, Opera, Firefox, Vivaldi, Edge, and Brave are all on Arm now. That’s a good start, but there are still many apps that will have to be emulated on these latest Copilot Plus PCs, which is where Microsoft’s Prism emulator comes in.

Microsoft claims Prism is as efficient as Apple’s Rosetta 2 translation layer and can emulate apps twice as fast as the previous generation of Windows on Arm devices. I’ve been testing the Surface Laptop over the past week and haven’t run into the erratic behavior I saw on Microsoft’s previous emulator, which also impacted battery life on the Surface Pro X. But I also haven’t seen the dramatic improvements in emulated app performance that Microsoft promised.

Microsoft’s claims are difficult to test without comparing previous Arm-based devices. [YouTuber Gary Explains did exactly that](https://youtu.be/_zdolfkCyCU), comparing the x86 or x64 versions of Firefox, Cinebench R23, and HandBrake on a Surface Pro X without Prism and then with the latest Windows 11 24H2 update that includes Prism.

*Microsoft’s new Surface devices are powered by Arm-based Qualcomm chips.*

Photo by Chris Welch / The Verge

Gary Explains found that Prism gave a 10 percent performance improvement in Speedometer 3 running on Firefox, an 8 percent jump in Cinebench R23 single core, and a 4.5 percent improvement in Cinebench R23 multicore compared to the previous emulator. HandBrake performance also improved by 8 percent thanks to Prism.

In my own testing, I’ve found that Prism handles compatibility for non-native apps well, but the performance varies depending on the complexity of the app. ShareX, a screenshot tool, works fine using the Prism emulator, but it’s a lightweight app. iA Writer and Notion aren’t native, but they run well on these latest Snapdragon chips, too. Discord also performs a lot better than I’ve seen on Arm in the past, but there’s still some occasional stuttering and a slight lag navigating between servers.

For more heavyweight apps, Prism doesn’t bring the experience up to what you’d find on an Intel- or AMD-powered laptop. Adobe’s Premiere Pro running emulated was practically unusable for editing a 4K video on the Surface Laptop, which is probably why Adobe is now blocking the installation of the x64 version on Snapdragon X Elite and Plus processors. An ARM64 version of Premiere Pro is planned for later this year.

Blender is another example of an emulated app with underwhelming performance. Blender doesn’t detect Qualcomm’s Adreno GPU, so everything hits the CPU instead. The performance for rendering projects is terrible as a result, with one test I performed taking more than 15 minutes to complete, compared to just over two minutes on a 13-inch MacBook Air M3. Blender will soon have a native ARM64 version, but I tested the early alpha copy, and it only marginally improved the results because it’s still not picking up the GPU correctly.

Intel has dominated the laptop GPU market with its integrated solutions for decades, so I suspect Qualcomm still needs to engage with developers of software like Blender to ensure apps are optimized for its GPUs. Blender illustrates that Microsoft’s Prism emulator can’t solve everything.

*Native ARM64 apps make the most of Microsoft’s new Surface devices.*

Photo by Chris Welch / The Verge

Speaking of GPUs, games also don’t “just work” on the Snapdragon X Elite and X Plus, despite Qualcomm’s assurances. I didn’t make a big deal out of this for the [Surface Laptop review](/2024/6/25/24185462/microsoft-surface-laptop-7th-edition-review) because it’s not a gaming laptop, but gaming on Windows on Arm is disappointing right now. *Shadow of the Tomb Raider* kept crashing for me when I attempted to play, and most of the other games I tried just refused to launch. *Fall Guys* throws up an unsupported error, as does *Halo Infinite*. *Destiny 2* didn’t even launch — no error, just a whole lot of nothing. *Starfield* did the same.

There aren’t many native Windows on Arm games, so Prism has its work cut out for it here. I managed to get *Grand Theft Auto V* working but with lots of frame stuttering. *Cyberpunk 2077* also ran on the Surface Laptop 7th Edition but at around 26fps on average at low settings on 1080p resolution. *The* *Witcher 3*, *Baldur’s Gate 3*, *Control*, *Rocket League*, and *Minecraft* all worked out of the box, too.

The biggest issue here is that most anticheat services use kernel drivers that [aren’t supported by emulation](https://devblogs.microsoft.com/directx/step-forward-for-gaming-on-arm-devices-2024/). BattlEye, a widely used anticheat service, is one of the rare exceptions that supports Windows on Arm, but it seems games like *Destiny 2* that utilize this anticheat software will need to be updated to run properly here. Thankfully, there is a [dedicated website](https://www.worksonwoa.com/games/) that tracks which games are supported and run well. I’m not holding out much hope for Arm-powered gaming laptops anytime soon, though.

*A lot of games use anticheat technologies that aren’t supported on Windows on Arm.*

Screenshot by Tom Warren / The Verge

Another thing I’ve run into is apps just refusing to install. Google Drive is the big one here, as it throws up an error about the Windows architecture of Copilot Plus PCs not being supported. Google’s Drive app on Windows integrates into the shell much like Dropbox, which is something Microsoft didn’t originally support on Windows on Arm. There is, however, a native version of Dropbox that integrates into File Explorer, so hopefully Google is able to deliver a similar experience soon.

There are compatibility issues with external devices, too. I’ve seen reports about Brother printers and scanners not working well on Arm or simply that generic printer drivers don’t support all of the features you’d expect. There’s no easy quick fix for accessories that require driver support, and that’s only likely to come based on the sheer amount of people using these new Copilot Plus PCs. I’m less concerned about the driver issues here because I think most people will be able to plug in the type of accessories (webcams, printers, storage drives) you use on a laptop and have them up and running with the built-in drivers in Windows 11.

VPN apps are still an issue on Windows Arm, too. Bitdefender, NordVPN, and Private Internet Access don’t work. VPN developers use TAP and TUN virtual adapters and devices and need a signed driver from Microsoft to work correctly. Fortunately, [*Android Authority* reports](https://www.androidauthority.com/copilot-plus-pcs-vpn-3452723/) that VPN developers are working on ARM64 versions.

That’s encouraging because the last time [I used Windows on Arm regularly in 2019](/2019/11/6/20950487/microsoft-surface-pro-x-7-review-comparison-specs-photos), I said, “Most of the apps I use on a daily basis haven’t been recompiled for ARM and probably never will be.” Now, it feels like app compatibility on Windows on Arm is changing on a daily basis, which is a scenario I wasn’t expecting to see five years ago.

While we’re in this transition point, you may need to use beta versions or download special builds of Windows apps that are ARM64 native — much like the macOS transition. That means the Windows Store versions of apps aren’t always ARM64, and you might be able to find the improved version on the web before the app store version is updated. That was the case initially with Slack earlier this month before the store version got updated.

*Microsoft has some extra settings to control the Prism emulator.*

Screenshot by Tom Warren / The Verge

For everything else, Microsoft does have some tools for power users that might improve app compatibility on Arm with existing unmodified x86 or x64 apps. There’s a program [compatibility troubleshooter](https://learn.microsoft.com/en-us/windows/arm/apps-on-arm-program-compat-troubleshooter#toggling-emulation-settings) that can help enable or disable emulation settings, and you can also toggle these in the properties of an executable. You can control things like hybrid execution mode to force the use of x86-only binaries, disable floating point optimization that could impact performance, and much more. You can also modify how an emulated app uses multiple CPU cores, which might improve performance or compatibility in certain apps.

Ultimately, it’s down to app developers to focus on native ARM64 support for their apps. The sheer amount of native apps that are now available shows things are heading in the right direction. These new Qualcomm chips also provide the brute-force power to emulate apps a little better, alongside Microsoft’s Prism improvements. Day to day, I think most people won’t even run into app issues here because a lot of the key apps are already native or run well in emulation.

I’m confident a lot more ARM64 apps are still on the way. During my testing, benchmark tools and apps were updated to support ARM64, catching me by surprise. I’m willing to bet that we won’t be discussing Prism or emulated app performance as much in a year or two because native ARM64 apps will be as common as x64 apps are today after the [transition from x86](https://www.jocheojeda.com/2024/05/25/the-transition-from-x86-to-x64-in-windows-a-detailed-overview/) began in the early 2000s. After 12 years of attempts to transition to Windows on Arm, it feels like Microsoft is finally about to succeed.

## Notepad by Tom Warren /

A weekly newsletter uncovering the secrets and strategy behind Microsoft’s era-defining bets on AI, gaming, and computing.

<a href="http://theverge.com/notepad-microsoft-newsletter" class="duet--article--dangerously-set-cms-markup inline-block whitespace-nowrap rounded-sm border border-blurple px-18 py-12 text-12 font-medium uppercase tracking-12 no-underline hover:bg-blurple hover:text-white md:ml-28">Subscribe</a>
